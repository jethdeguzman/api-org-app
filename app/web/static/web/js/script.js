$(document).ready(function() {
    $('.btn-continue').click(function(e) {
        e.preventDefault();
        text = $(this).data('continue-text');
        formName = $(this).attr('form');
        form = $('#' + formName);
        swal({
            title: "Are you sure?",
            text: text,
            type: "warning",
            showCancelButton: true,
            cancelButtonText: 'No',
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "Yes",
            closeOnConfirm: false
        }, function(isConfirm) {
            if (isConfirm) {
                form.submit();
            }
        });
    });

    $('#checklists-select').change(function(){
        window.location.href=$(this).val();
    });
});
