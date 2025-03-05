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

function create_layout(input, parent_component = null) {
    let main_component = null;

    for (let i = 0; i < input.length; i++) {
        const [tag, attributes] = Object.entries(input[i])[0];
        const current_component = document.createElement(tag);

        if (!main_component) {
            main_component = current_component;
        }

        Object.entries(attributes).forEach(([key, value]) => {
            if (Array.isArray(value) && value.length > 0 && typeof value[0] === "object") {
                value.forEach(child => {
                    const child_component = create_layout([child], current_component);
                    current_component.appendChild(child_component);
                });
            } else {
                if (key === "innerHTML") {
                       current_component.appendChild(document.createTextNode(value));
                }
                else {
                    current_component.setAttribute(key, value);
                }

            }
        });

        if (parent_component) {
            parent_component.appendChild(current_component);
        }
    }

    return main_component;
}

function add_component_to_div(component, div_id) {
    var div = document.getElementById(div_id);
    div.appendChild(component);
}


