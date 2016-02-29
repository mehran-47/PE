// Called when we select "Import -> Import from Dropbox" in the tool.
function opendropbox() {
    requireAuth({trigger: 'ACTION'}).then(function() {
        opendropboxContinue();
    });
}
function opendropboxContinue() {
    addMessage('Opening Dropbox');
    function done() {
        delMessage('Opening Dropbox');
    }

    Dropbox.choose({
        success: function(files) {
            var file = files[0];
            console.log("Dropbox files selected", files);
            done();
            addMessage('Loading Dropbox file');
            $.post("/dropbox/fetch", {
                name: file.name,
                link: file.link
                }, function(res) {
                    fileResp(res);
                });
        },
        cancel: done,
        linkType: "direct",
        multiselect: false,
        extensions: ['.txt', '.csv', '.xls', '.xlsx', '.mdb', '.res']
    });
}
