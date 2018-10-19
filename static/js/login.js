//登录表单提交
function login_form_submit(){
    var $jsLoginBtn = $('#jsLoginBtn'),
        $jsLoginTips = $('#jsLoginTips'),
        $accountl = $("#account_l"),
        args = window.location.search.substr(1,window.location.search.length).split('&'),
        arg = [],
        verify = verifyDialogSubmit(
        [
            {id: '#account_l', tips: Dml.Msg.epUserName, errorTips: Dml.Msg.erUserName, regName: 'phMail', require: true},
            {id: '#password_l', tips: Dml.Msg.epPwd, errorTips: Dml.Msg.erPwd, regName: 'pwd', require: true}
        ]
    );
    if(!verify){
       return;
    }
    var autoLogin = false;
    if ($('#jsAutoLogin').is(':checked')){
        autoLogin = true;
    }
    $.each(args, function(key,value){
        arg = value.split('=');
        if(arg[0] == 'name'){
            return false;
        }
    });
    $.ajax({
        cache: false,
        type: 'post',
        dataType:'json',
        url:"/user/login/",
        data:$('#jsLoginForm').serialize() + '&autologin='+autoLogin + '&' + arg[0] + '=' + arg[1],
        async: true,
        beforeSend:function(XMLHttpRequest){
            $jsLoginBtn.val("登录中...");
            $jsLoginBtn.attr("disabled","disabled");
        },
        success: function(data) {
            if(data.account_l){
                Dml.fun.showValidateError($accountl, data.account_l);
            }else if(data.password_l){
                Dml.fun.showValidateError($("#password_l"),data.password_l);
            }else{
                if(data.status == "success"){
                    $('#jsLoginForm')[0].reset();
                    window.location.href = data.url;
                }else if(data.status == "failure"){
                    //注册账户处于未激活状态
                    if(data.msg=='no_active'){
                        zyemail = $accountl.val();
                        zyUname = zyemail;
                        $('#jsEmailToActive').html(zyemail);
                        var url = zyemail.split('@')[1],
                            $jsGoToEmail = $('#jsGoToEmail');
                        $jsGoToEmail.attr("href",hash[url]);
                        if(undefined==hash[url] || hash[url]==null){
                            $jsGoToEmail.parent().hide();
                        }
                         Dml.fun.showDialog('#jsUnactiveForm');
                    }
                    else{
                        $jsLoginTips.html("账号或者密码错误，请重新输入").show();
                    }
                }
            }
        },
        complete: function(XMLHttpRequest){
            $jsLoginBtn.val("登录");
            $jsLoginBtn.removeAttr("disabled");
        }
    });

}