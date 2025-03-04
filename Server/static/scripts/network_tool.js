

function post(args) {
    axios({
        method: "post",
        url: "/post",
        data: args
    })
        .then(function (response) {
            console.log(response);
        })
        .catch(function (response) {
            console.log(response);
        });
}
