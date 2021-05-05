const email_validate = (email) => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
};

let formLock = 0;

const login = () => {


    if (formLock === 0) {
        formLock = 1;
        let email = $('#email');
        let password = $('#password');

        if (!email_validate(email.val())) {
            toastr.error('e-mail hatalıdır !', 'Hata');
            formLock = 0;
            return false;
        }

        if (password.val() === '') {
            toastr.error('şifre boş olamaz !', 'Hata');
            formLock = 0;
            return false;
        }

        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/auth/login',
            data: {
                email: email.val(),
                password: password.val()
            },
            beforeSend: () => {
                toastr.info('giriş yapılıyor..', 'Bilgi')
            },
            success: (response) => {
                formLock = 0;
                if (response.status === 'ok') {
                    toastr.success(response.message, 'Başarılı');
                    setTimeout(() => {
                        window.location.href = '/';
                    }, 1300)
                } else {
                    toastr.error(response.message, 'Hata');
                }
            },
        });

    }

};

const delete_appointment_confirm = (id) => {
    $('#delete_appointment_id').val(id);
};

const delete_appointment = () => {
    let appointment_id = $('#delete_appointment_id');

    if (formLock === 0) {
        formLock = 1;
        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/appointment/delete',
            data: {
                appointment_id: appointment_id.val()
            },
            success: (response) => {
                formLock = 0;
                if (response.status === 'ok') {
                    toastr.success(response.message, 'Başarılı');
                    $('[data-row="row-' + appointment_id.val() + '"]').stop().fadeOut();
                    toastr.clear();
                    $('#deleteModal').modal('hide');
                    setTimeout(() => {
                        // row delete
                        $('[data-row="row-' + appointment_id.val() + '"]').remove();
                    }, 1300)
                } else {
                    toastr.error(response.message, 'Hata');
                }
            }
        });
    }
};

const change_appointment_status = (id, status) => {
    if (formLock === 0) {
        formLock = 1;
        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/appointment/change_status',
            data: {
                appointment_id: id,
                appointment_status: status
            },
            success: (response) => {
                formLock = 0;
            }
        });
    }
};

const get_appointment = (appointment_id) => {
    if (formLock === 0) {
        formLock = 1;

        $.ajax({
            type: 'POST',
            dataType: 'json',
            data: {
                appointment_id: appointment_id
            },
            url: '/appointment/get',
            success: (response) => {
                if (response.status === 'ok') {

                    formLock = 0;

                    let formModal = $('#formModal');
                    let appointmentForm = $('#appointment-form');

                    let data = response.data;

                    let appointment_date = format_date(data.appointment_date);

                    formModal.find('.modal-header > .modal-title').html('Edit Appointment');
                    appointmentForm.find('input#appointment_id').val(data.appointment_id);
                    appointmentForm.find('input#appointment_title').val(data.appointment_title);
                    appointmentForm.find('input#appointment_date').val(appointment_date);
                    appointmentForm.find('textarea#appointment_detail').val(data.appointment_detail);

                }
            }
        });
    }
};

const format_date = (date_str) => {
    let split_date = date_str.split('-');
    let day = split_date[2];
    let month = split_date[1];
    let year = split_date[0];

    return day + '/' + month + '/' + year;
};

const save_appointment = () => {
    if (formLock === 0) {
        formLock = 1;
        let appointment_id = $('#appointment_id');
        let appointment_title = $('#appointment_title');
        let appointment_date = $('#appointment_date');
        let appointment_detail = $('#appointment_detail');

        if (appointment_title.val() === '') {
            toastr.error('Randevu başlığı gereklidir!', 'Hata');
            formLock = 0;
            return false;
        }

        if (appointment_date.val() === '') {
            toastr.error('Randevu tarihi gereklidir!', 'Hata');
            formLock = 0;
            return false;
        }

        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/appointment/save',
            data: {
                appointment_id: appointment_id.val(),
                appointment_title: appointment_title.val(),
                appointment_date: appointment_date.val(),
                appointment_detail: appointment_detail.val()
            },
            beforeSend: () => {
                toastr.info('kaydediliyor..', 'Bilgi')
            },
            success: (response) => {
                formLock = 0;
                if (response.status === 'ok') {
                    $('#formModal input, #formModal textarea').val('');
                    toastr.success(response.message, 'Başarılı');
                    setTimeout(() => {
                        window.location.href = '/appointment';
                    }, 1300)
                } else {
                    toastr.error(response.message, 'Hata');
                }
            },
        });

    }
};

const load_more = () => {
    if (formLock === 0) {
        formLock = 1;
        let last_id_row = $('.appointments .body:last-child').attr('data-row');
        let last_id = last_id_row.split('-')[1];
        let load_more_button = $('.btn_load_more');

        $.ajax({
            type: 'POST',
            dataType: 'json',
            url: '/appointment/load_more',
            data: {
                last_id: last_id
            },
            beforeSend: () => {
                load_more_button.html('loading...');
            },
            success: (response) => {
                formLock = 0;
                if (response.status === 'ok') {
                    load_more_button.html('load more');
                    let data_length = response.data.length;
                    let code = '';
                    for ( let i = 0; i<data_length; i++ ) {
                        code += '<div class="body py-2 rounded-3 my-2" data-row="row-'+response.data[i].appointment_id+'">';
                        code += '<ul class="d-flex justify-content-between">';
                        code += '<li>'+response.data[i].appointment_id+'</li>';
                        code += '<li>'+response.data[i].appointment_title+'</li>';
                        code += '<li>'+date_format_for_list(response.data[i].appointment_date)+'</li>';
                        code += '<li><ul>';
                        code += '<li><a role="button" onClick="get_appointment('+response.data[i].appointment_id+')" data-bs-toggle="modal" data-bs-target="#formModal"><i class="fas fa-edit"></i></a></li>';
                        code += '<li><a role="button" onClick="delete_appointment_confirm('+response.data[i].appointment_id+')" data-bs-toggle="modal" data-bs-target="#deleteModal"><i class="fas fa-trash"></i></a></li>';
                        code += '<li>';
                        let checked = '';
                        if ( response.data[i].appointment_status === 1 ) {
                            checked = 'checked';
                        }
                        code += '<input type="checkbox" '+checked+' onChange="change_appointment_status('+response.data[i].appointment_id+', '+new_appointment_status(response.data[i].appointment_status)+')" id="switch_appointment_status" class="position-absolute" /><label for="switch_appointment_status">Toggle</label>';
                        code += '</li></ul></li></ul></div>';
                    }

                    $('.appointments .table').append(code);
                }
            },
        });
    }
};

const date_format_for_list = (date_str) => {
    //2021-05-20
    let split_date = date_str.split('-');
    let day = split_date[2];
    let month = split_date[1];
    let year = split_date[0];

    return day + '.' + month + '.' + year;
};

const new_appointment_status = (appointment_status) => {
    return appointment_status === '1' ? '0' : '1';
};

$(document).ready(function () {
    let datepicker = $('#appointment_date');

    if (datepicker.length) {
        datepicker.datepicker({
            minDate: 0,
            dateFormat: "dd/mm/yy"
        });
    }
})