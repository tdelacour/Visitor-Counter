<!DOCTYPE html>
<html>
<head>
   <title> PHP Visitor counter </title>
</head>
<body>
<?php
   $output=shell_exec('python readCount.py.cgi');
   echo "The Visitor Counter is: $output";
   echo "<br/>";
   echo "<br/>";
   echo "<br/>";
   shell_exec('python addCount.py.cgi');
   $user_agent=$_SERVER['HTTP_USER_AGENT'];
   $array=preg_split("/[\(\)]/", $user_agent);
   $x=$array[1];
   $command="python osCounter.py.cgi \"$x\"";
   $escapedcmd=escapeshellcmd($command);
   $var=shell_exec($escapedcmd);
   $varArray=explode('*', $var);
   echo "Operating Systems of Visitors are: " .  str_repeat('&nbsp;', 48) . "(Count)";
   echo "<br/>";
   echo "<br/>";
   foreach($varArray as $val){
      echo $val;
      echo "<br/>";
   }
?>
</body>
</html>
