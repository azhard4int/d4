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
    ajax_request_post('user/', formData, user.login_success, user.login_failed)

};
//login success callback
user.login_success = function(m)
{

};
//login error callback
user.login_failed = function(m)
{

};