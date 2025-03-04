function get_table_head(columns) {
    var thead = document.createElement("thead")
    var tr = document.createElement("tr");
    for (let i = 0; i < columns.length; i++) {
        var th = document.createElement("th");
        th.appendChild(document.createTextNode(columns[i]));
        tr.appendChild(th);
    }
    thead.appendChild(tr);
    return thead;
}

function get_table_body(table_data) {
    var tbody = document.createElement("tbody");
    for (let i = 0; i < table_data.length; i++) {
        var tr = document.createElement("tr");
        for (var j = 0; j < table_data[i].length; j++) {
            var td = document.createElement("td");
            td.textContent = table_data[i][j];
            tr.appendChild(td);
        }
        tbody.appendChild(tr);
    }
    return tbody;
}

function get_table(table_data, columns) {
    var table = document.createElement("table");
    table.setAttribute("class", "table table-striped");
    table.appendChild(get_table_head(columns));
    table.appendChild(get_table_body(table_data));
    return table;
}

function put_component(component, div_id){
    div = document.getElementById(div_id);
    div.appendChild(component);
}