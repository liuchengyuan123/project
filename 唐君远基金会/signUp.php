<?php
header('Content-Type:application/json; charset=utf-8');
$json_arr = array('errCode'=>0, 'errMsg'=>'');
//echo "signUp\n";
if (!isset($_POST))
{
    $json_arr['errCode'] = -1;
    $json_arr['errMsg'] = 'Not POST method.';
    exit(json_encode($json_arr));
}
$link = mysqli_connect("localhost", "root", "lamp.sh");
if (!$link)
{
    $json_arr['errCode'] = -1;
    $json_arr['errMsg'] = mysqli_connect_error();
  //  echo mysqli_connect_error(), "\n";
    exit(json_encode($json_arr));
}
mysqli_query($link, "SET NAMES 'gb2312'");
if (!mysqli_select_db($link, "work_bench"))
{
    $json_arr['errCode'] = -1;
    $json_arr['errMsg'] = 'Cannot connect to database.';
    exit(json_encode($json_arr));
}
//echo"fuck\n";
mysqli_query($link, "set character_set_client = utf8;");
mysqli_query($link, "set character_set_results = utf8;");
mysqli_query($link, "set character_set_connection = utf8;");
mysqli_query($link, "set collation_connection = utf8_general_ci;");
$sql = "select 编号 from 人才表 where 电子邮箱 = '$_POST[email]';";
$result = mysqli_query($link, $sql);
$num = mysqli_num_rows($result);
if ($num >= 1)
{
    $json_arr['errCode'] = -1;
    $json_arr['errMsg'] = 'Email is in used.';
    exit(json_encode($json_arr));
}
//echo "kjahdjkjasd\n";
$insert = "insert into 人才表(电子邮箱) values ('$_POST[email]');";
//echo $insert, "\n";
$ret = mysqli_query($link, $insert);
//var_dump($ret);
//echo"\n";
if (!$ret)
{
    $json_arr['errCode'] = -1;
    $json_arr['errMsg'] = mysqli_error($link);
    //echo $json_arr['errMsg'], "\n";
    exit($json_arr);
}
//echo "success\n";
$salt = md5(uniqid(microtime(true),true));
$password = md5(uniqid(microtime(true),true));
$saltword = md5($password).$salt;
$saltword = md5($saltword);
$ret = mysqli_query($link, "UPDATE 人才表 SET 密码='$saltword', salt='$salt' WHERE 电子邮箱='$_POST[email]';");
//echo "UPDATE 人才表 SET 密码='$saltword', salt='$salt' WHERE 电子邮箱='$_POST[email]';";
if (!$ret)
{
    $json_arr['errCode'] = -1;
    $json_arr['errMsg'] = mysqli_error($link);
    exit(json_encode($json_arr));
}
//var_dump($ret);
$message = "密码:$password";
$subject = "确认注册";
$headers = "From: waytocode@163.com";
mail($_POST[email], $subject, $message, $headers);
$json_arr['errCode'] = 0;
exit($json_arr);
