function check_pass(){
var p = $('#pass').val();
var c = $('#cpass').val();
if(p==c){
 $('#signup').attr('disable',false).css({'background':'#6dabe4'});
 $('#msz').html('');
}else{
 $('#signup').attr('disable',true).css({'background':'red'});
 $('#msz').html("<small>Password didn't matches</small> ");
}
}
