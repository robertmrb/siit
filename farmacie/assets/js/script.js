// mesaj daca pacientul nu e gasit

$(document).ready(function() {
    var verify = $("#chk_td").length;
        if (verify == 0) {
            $("#no-data").text("Nici un pacient nu a fost gasit");
        }
    });

// validare campuri

function validateEmail(email){
    var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}

function validateAll() {

    var nume = $("#nume").val();
    var telefon = $("#telefon").val();
    var email = $("#email").val();
    var varsta = $("#varsta").val();
    var gen = $("#gen").val();
    var medicament = $("#medicament").val();
    var stoc = $("#stoc").val();

    if (nume == '') {
        swal("Atentie", "Trebuie completat un nume", "error")
        return false;
    }
    else if (nume.split(' ').length < 2) {
        swal("Atentie", "Trebuie completat cu nume si prenume", "error")
        return false;
    }
    else if (telefon == '') {
        swal("Atentie", "Trebuie completat un nr de telefon", "error")
        return false;
    }
    else if (email == '') {
        swal("Atentie", "Trebuie completat o adresa de mail", "error")
        return false;
    }
    else if (!(validateEmail(email))) {
        swal("Atentie", "Trebuie completat o adresa de mail valida", "error")
        $("#email").val("");
        return false;
    }
    else if (varsta == '') {
        swal("Atentie", "Trebuie completata varsta", "error")
        return false;
    }
    else if (gen == '') {
        swal("Atentie", "Trebuie completat genul", "error")
        return false;
    }
    else if (medicament == '') {
        swal("Atentie", "Trebuie completat medicament", "error")
        return false;
    }
    else if (stoc == '') {
        swal("Atentie", "Trebuie completat stocul", "error")
        return false;
    }

    else {
        return true;
    }
}
$("#btn-add").bind("click", validateAll);


// validare numai litere la nume
$(document).ready(function() {
    jQuery('input[name="nume"]').keyup(function() {
        var letter = jQuery(this).val();
        var allow = letter.replace(/[^a-zA-Z _]/g, '');
        jQuery(this).val(allow);
    });
    // numele sa nu inceapa cu spatiu
    $("input").on("keypress", function(e) {
        if (e.which === 32 && !this.value.length)
        e.preventDefault();
    });

});

//acceptare numai cifre varsta
$("#varsta").keyup(function() {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
});

//acceptare numai cifre telefon
$("#telefon").keyup(function() {
    if (!/^[0-9]*$/.test(this.value)) {
        this.value = this.value.split(/[^0-9]/).join('');
    }
});