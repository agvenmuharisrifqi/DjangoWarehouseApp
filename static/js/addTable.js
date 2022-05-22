function addInput(...args) {
    let idTable, input1, input2;
    try {
        idTable = id_tab;
        input1 = inp1;
        input2 = inp2;
    } catch (error) {
        idTable = 'table_input',
            input1 = '<input type="text">'
        input2 = '<input type="text">'
    }
    const table = document.getElementById(idTable).querySelector("tbody");
    let idx = table.rows.length,
        row = table.insertRow(idx),
        // Cell
        cell1 = row.insertCell(0),
        cell2 = row.insertCell(1),
        cell3 = row.insertCell(2),
        cell4 = row.insertCell(3),
        cell5 = row.insertCell(4),
        btnRemove = document.createElement("button");
    btnRemove.setAttribute("class", "delete-table")
    btnRemove.setAttribute("type", "button")
    btnRemove.setAttribute("title", "Delete")
    btnRemove.innerHTML = '<i class="fa-solid fa-circle-minus text-danger"></i>'
    cell2.setAttribute("class", "quantity")
    cell3.setAttribute("class", "product-price")
    cell4.setAttribute("class", "product-total")
    cell5.setAttribute("class", "actions")
    // Cell Add To Row
    cell1.innerHTML = `<div class="autocomplete-wrapper">${input1}</div>`;
    cell2.innerHTML = input2;
    cell3.innerHTML = '<sup>Rp. </sup><span class="price">0</span>';
    cell4.innerHTML = '<sup>Rp. </sup><span class="total">0</span>';
    cell5.appendChild(btnRemove);
}

function delInput(idTable, elem) {
    let index_row = elem.rowIndex,
        check_row = [...document.getElementById(idTable).querySelectorAll("tbody tr")],
        table = document.getElementById(idTable).querySelector("tbody"),
        len = table.rows.length,
        position,
        check_index;
    check_index = check_row.map((elemet, index) => ({position_row: elemet.rowIndex, position_index: index}));
    position = check_index.find(check => check.position_row === index_row)
    if (len > 1 && position) {
        table.deleteRow(position.position_index);
    }
}