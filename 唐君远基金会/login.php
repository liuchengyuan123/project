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
	exit(json_encode($json_arr));
}
mysqli_query($link, "SET NAMES 'gbk2312'");
if (!mysqli_select_db($link, "work_bench"))
{
	$json_arr['errCode'] = -1;
	$json_arr['errMsg'] = "Cannot connect to database.";
	exit(json_encode($json_arr));
}
mysqli_query($link, "set character_set_client = utf8;");
mysqli_query($link, "set character_set_results = utf8;");
mysqli_query($link, "set character_set_connection = utf8;");
mysqli_query($link, "set collation_connection = utf8_general_ci;");
$sql = "select * from 人才表 where 电子邮箱='$_POST[email]';";
$result = mysqli_query($link, $sql);
$row = mysqli_fetch_array($result);
$salt = $row['salt'];
$saltword = md5($_POST[password]).$salt;
$saltword = md5($saltword);
if ($saltword != $row['密码'])
{
	$json_arr['errCode'] = -1;
	$json_arr['errMsg'] = 'password wrong';
	exit(json_encode($json_arr));
}
echo "login succeed!\n";
$info = array('status'=>$row['审核']);
array_push($json_arr, $info);
exit(json_encode($json_arr);
