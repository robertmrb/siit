// mesaj daca pacientul nu e gasit

$(document).ready(function() {
    var verify = $("#chk_td").length;
        if (verify == 0) {
            $("#no-data").text("Nici un pacient nu a fost gasit");
        }
    });