Собирается на Debian Bullseye для него же

Зависимости:
```
apt-get install build-essential fakeroot
apt-get build-dep linux
```

Получение репозитория
```
git clone https://github.com/GurovRoman/mipt-linux2-modules
cd mipt-linux2-modules
```

Так как в репозиторий не входит само ядро, а только патч для него, для начала придется скачать ядро Debian и интегрировать в репозиторий
```
apt-get install linux-source-5.4
tar --skip-old-files -xaf /usr/src/linux-source-5.4.tar.xz
```

Перед сборкой ядро необходимо конфигурировать так, как вам удобно, например:
```
cd linux-source-5.4
make menuconfig
cd ..
```

Теперь можно запускать сборку
```
./build.sh
```

После сборки в рабочей директории появятся .deb файлы, которые нужно установить через `dpkg -i`. После установки кастомного ядра и перезагрузки, модуль можно запускать через `insmod custom_module/phonebook.ko`
