$(document).ready(function () {
    $("#example").dataTable({
        sDom: 'B<"input-wrapper"f>t<"pagination-wrapper"p>',
        buttons: [{
                extend: 'excelHtml5',
                text: 'Download as EXCEL',
            },
            {
                extend: 'pdfHtml5',
                text: 'Download as PDF',
            },
        ],
        lengthChange: false,
        pagingType: "full_numbers",
        language: {
            paginate: {
                first: "&laquo;",
                last: "&raquo;",
                previous: "&lsaquo;",
                next: "&rsaquo;"
            },
            searchPlaceholder: "Search in here ...",
        },
        paging: false,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: [0, -1],
            searchable: false
        }],
        order: [
            [1, 'asc']
        ],
        oLanguage: {
            sSearch: "Ctrl + /",
            sEmptyTable: "No data available in table",
            sZeroRecords: "There is no data that matches the keyword you provided",
            sInfoEmpty: "No entries to show",
        }
    });
});
let deleteSelected = [];
$('input.table-check').each(function () {
    $(this).on("click", function () {
        var check = $(this).is(":checked") ? true : false;
        if (check) {
            $("#button_selected").show();
            deleteSelected.push(`Delete id ${this.value}`);
        } else {
            deleteSelected = deleteSelected.filter(id => id !== `Delete id ${this.value}`);
        }
        if (deleteSelected.length === 0) {
            $("#button_selected").hide();

        }
    })
});
$(document).keydown(function (event) {
    if (event.ctrlKey && event.keyCode == 191) {
        $("#example_filter label input").focus();
    };
});