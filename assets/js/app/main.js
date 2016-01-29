/**
 * Created by azhar on 1/18/16.
 */
var BASE_URL = "http://127.0.0.1/"
function generate_token()
{
    var csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].value
    return csrf_token;
}
function ajax_request_post(url, data, success_function, error_function)
{
    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        success: success_function,
        error:error_function
    })
}
//main app functions
var user = function (){};
user.login = function()
{
    //get_token = generate_token();
    var formData = $('#loginForm').serialize();
    ajax_request_post('/user/login/', formData, user.login_success, user.login_failed)

};
//login success callback
user.login_success = function(m)
{
    var resp = JSON.parse(m);
    if (resp.status==true)
    {
        window.location.href = '/user/'
    }
};
//login error callback
user.login_failed = function(m)
{

};

user.vm_start = function(vm_id)
{
    data = {
        'vm_id': vm_id,
        'csrfmiddlewaretoken': generate_token
    };
    ajax_request_post('/user/vm_start/', data, user.vm_success_message, user.vm_error_message)
};

user.vm_pause = function(vm_id)
{

    data = {
        'vm_id': vm_id,
        'csrfmiddlewaretoken': generate_token
    };
    ajax_request_post('/user/vm_pause/', data, user.vm_success_message, user.vm_error_message)
};

user.vm_shutdown = function(vm_id)
{
    data = {
        'vm_id': vm_id,
        'csrfmiddlewaretoken': generate_token
    };
    ajax_request_post('/user/vm_shutdown/', data, user.vm_success_message, user.vm_error_message)
};

user.vm_reboot = function(vm_id)
{
    data = {
        'vm_id': vm_id,
        'csrfmiddlewaretoken': generate_token
    };
    ajax_request_post('/user/vm_reboot/', data, user.vm_success_message, user.vm_error_message)
};

user.vm_success_message = function(m)
{

};

user.vm_error_message = function(m)
{

};

user.profile_settings = function()
{
     var formData = $('#profileSettings').serialize();
     ajax_request_post('/user/settings/', formData, user.login_success, user.login_failed)
};