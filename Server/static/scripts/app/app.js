var components = {}

function get(item) {
    axios({
        method: "get",
        url: "/get",
        params: {"component": item}
    })

        .then(function (response) {
            components = response.data;
        })
        .catch(function (response) {
            console.log(response);
        });
}

var count = 0;
function create_layout(input, result=null, _key=null) {
    if (input instanceof Array) {
        console.log(input);
        Object.entries(input).forEach(([key, value]) => {
            if (result === null) {
                result = document.createElement(key);
            }
            if (value instanceof Object) {
                create_layout(value, result)
            }
            else if (value instanceof Array) {
                for (let i = 0; i < input.length; i++) {
                    create_layout(value, result)
                }
            }
        else {
                result.setAttribute(key, value);
            }
        })
    }

}