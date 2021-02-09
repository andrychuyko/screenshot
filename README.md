# Screenshot
Periodicaly screenshot multi display and send image to server without local save

Периодическое создание снимков экрана для нескольких мониторов с отправкой их на сервер без сохранения локального файла с изображением

Имя файла генерируется на основании имени машины и даты-времени

По умолчанию скриншот делается раз в 20 секунд

Серверная часть может быть какой угодно, например на PHP

```php
<?php 
$file1 = $_FILES['pic']['tmp_name']; 
$name = basename($_FILES['pic']['name']); 
$dir='screenshot/'; //не обозначаем дирикторию, сохраняем в корень папки 
 
if (!file_exists($file1)) 
{ 
   echo "Ошибка, файл не загружен"; 
} 
else 
{ 
   move_uploaded_file($file1, $dir.$name); 
   echo "Файл $name загружен "; 
}
?>
```
