// "Google Picker" - sleek iframe modal for picking files from Google drive
// Ref: http://stackoverflow.com/questions/22435410/google-drive-picker-api

function opengdrive() {
    requireAuth({trigger: 'ACTION'}).then(function() {
        opengdriveContinue();
    });
}
function opengdriveContinue() {
    addMessage('Opening Google Drive');
    gapi.load('auth', {'callback': gdriveOnAuthApiLoad});
    gapi.load('picker');
}

function gdriveOnAuthApiLoad() {
    window.gapi.auth.authorize({
        'client_id': ENV.GOOGLEDRIVE_CLIENT_ID,
        'scope': ['https://www.googleapis.com/auth/drive']
    }, gdriveHandleAuthResult);
}

var oauthToken;
function gdriveHandleAuthResult(authResult) {
    if(authResult && !authResult.error){
        oauthToken = authResult.access_token;
        gdriveCreatePicker();
    }
}

function gdriveCreatePicker() {
    var SpreadView = new google.picker.View(google.picker.ViewId.SPREADSHEETS);
    var DocView = new google.picker.DocsView(google.picker.ViewId.DOCS)
        .setMimeTypes("text/plain,text/csv");
    var picker = new google.picker.PickerBuilder()
        .addView(SpreadView)
        .addView(DocView)
        .setOAuthToken(oauthToken)
        .setDeveloperKey(ENV.GOOGLEDRIVE_DEVELOPER_KEY)
        .setCallback(gdrivePickerCallback)
        .build();
    picker.setVisible(true);
}

function gdrivePickerCallback(data) {
    delMessage('Opening Google Drive');
    if (data[google.picker.Response.ACTION] == google.picker.Action.PICKED) {
        var doc = data[google.picker.Response.DOCUMENTS][0];
        addMessage('Importing Google Drive file');
        $.post("/gdrive/fetch", {
            'oauthToken': oauthToken,
            'fileId': doc.id,
            'name': doc.name
        },
        function(res) {
            delMessage('Importing Google Drive file');
            fileResp(res);
        });
}
}
