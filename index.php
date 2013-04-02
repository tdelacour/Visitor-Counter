<!DOCTYPE html>
<html>
<head>
   <title> PHP Visitor counter </title>
</head>
<body>
<?php
   $output=shell_exec('python readCount.py.cgi');
   echo "The Visitor Counter is: $output";
   shell_exec('python addCount.py.cgi');
?>
</body>
</html>
