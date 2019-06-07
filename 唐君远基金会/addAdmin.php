<?php
header('Content-Type:application/json; charset=utf-8');
$json_arr = array('errCode'=>0, 'errMsg'=>'');
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
mysqli_query($link, "set character_set_client = utf8;");
mysqli_query($link, "set character_set_results = utf8;");
mysqli_query($link, "set character_set_connection = utf8;");
mysqli_query($link, "set collation_connection = utf8_general_ci;");
$sql = "select 编号 from 管理员 where 邮箱 = '$_POST[email]';";
$result = mysqli_query($link, $sql);
$num = mysqli_num_rows($result);
if ($num >= 1)
{
	$json_arr['errCode'] = -1;
	$json_arr['errMsg'] = 'Email is in used.';
	exit(json_encode($json_arr));
}
$sql = "INSERT INTO 管理员(姓名, 用户名, 密码, 邮箱) VALUES ('$_POST[name]','$_POST[adminName]','$_POST[tel]','$_POST[email]','$_POST[password]')";
$result = mysqli_query($link, $sql);
if (!$result)
{
	$json_arr['errCode'] = -1;
	$json_arr['errMsg'] = mysqli_error($link);
	//echo $json_arr['errMsg'], "\n";
	exit($json_arr);
}
exit(json_encode($json_arr));
