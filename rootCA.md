ruhshona@ruhshona-Lenovo-V15-G4-AMN ~> sudo apt install docker.io -y
Чтение списков пакетов… Готово
Построение дерева зависимостей… Готово
Чтение информации о состоянии… Готово         
Будут установлены следующие дополнительные пакеты:
  bridge-utils containerd pigz runc ubuntu-fan
Предлагаемые пакеты:
  ifupdown aufs-tools btrfs-progs cgroupfs-mount | cgroup-lite debootstrap
  docker-buildx docker-compose-v2 docker-doc rinse zfs-fuse | zfsutils
Следующие НОВЫЕ пакеты будут установлены:
  bridge-utils containerd docker.io pigz runc ubuntu-fan
Обновлено 0 пакетов, установлено 6 новых пакетов, для удаления отмечено 0 пакетов, и 298 пакетов не обновлено.
Необходимо скачать 75.7 MB архивов.
После данной операции объём занятого дискового пространства возрастёт на 288 MB.
Пол:1 http://uz.archive.ubuntu.com/ubuntu noble/universe amd64 pigz amd64 2.8-1 [65.6 kB]
Пол:2 http://uz.archive.ubuntu.com/ubuntu noble/main amd64 bridge-utils amd64 1.7.1-1ubuntu2 [33.9 kB]
Пол:3 http://uz.archive.ubuntu.com/ubuntu noble-updates/main amd64 runc amd64 1.3.3-0ubuntu1~24.04.3 [8,815 kB]
Пол:4 http://uz.archive.ubuntu.com/ubuntu noble-updates/main amd64 containerd amd64 1.7.28-0ubuntu1~24.04.2 [38.4 MB]
Пол:5 http://uz.archive.ubuntu.com/ubuntu noble-updates/universe amd64 docker.io amd64 28.2.2-0ubuntu1~24.04.1 [28.3 MB]
Пол:6 http://uz.archive.ubuntu.com/ubuntu noble-updates/universe amd64 ubuntu-fan all 0.12.16+24.04.1 [34.2 kB]
Получено 75.7 MB за 13с (6,045 kB/s)                                           
Предварительная настройка пакетов …
Выбор ранее не выбранного пакета pigz.
(Чтение базы данных … на данный момент установлено 235964 файла и каталога.)
Подготовка к распаковке …/0-pigz_2.8-1_amd64.deb …
Распаковывается pigz (2.8-1) …
Выбор ранее не выбранного пакета bridge-utils.
Подготовка к распаковке …/1-bridge-utils_1.7.1-1ubuntu2_amd64.deb …
Распаковывается bridge-utils (1.7.1-1ubuntu2) …
Выбор ранее не выбранного пакета runc.
Подготовка к распаковке …/2-runc_1.3.3-0ubuntu1~24.04.3_amd64.deb …
Распаковывается runc (1.3.3-0ubuntu1~24.04.3) …
Выбор ранее не выбранного пакета containerd.
Подготовка к распаковке …/3-containerd_1.7.28-0ubuntu1~24.04.2_amd64.deb …
Распаковывается containerd (1.7.28-0ubuntu1~24.04.2) …
Выбор ранее не выбранного пакета docker.io.
Подготовка к распаковке …/4-docker.io_28.2.2-0ubuntu1~24.04.1_amd64.deb …
Распаковывается docker.io (28.2.2-0ubuntu1~24.04.1) …
Выбор ранее не выбранного пакета ubuntu-fan.
Подготовка к распаковке …/5-ubuntu-fan_0.12.16+24.04.1_all.deb …
Распаковывается ubuntu-fan (0.12.16+24.04.1) …
Настраивается пакет runc (1.3.3-0ubuntu1~24.04.3) …
Настраивается пакет bridge-utils (1.7.1-1ubuntu2) …
Настраивается пакет pigz (2.8-1) …
Настраивается пакет containerd (1.7.28-0ubuntu1~24.04.2) …
Created symlink /etc/systemd/system/multi-user.target.wants/containerd.service →
 /usr/lib/systemd/system/containerd.service.
Настраивается пакет ubuntu-fan (0.12.16+24.04.1) …
Created symlink /etc/systemd/system/multi-user.target.wants/ubuntu-fan.service →
 /usr/lib/systemd/system/ubuntu-fan.service.
Настраивается пакет docker.io (28.2.2-0ubuntu1~24.04.1) …
info: Выбирается GID из диапазона от 100 до 999 …
info: Добавляется группа «docker» (GID 131) …
Created symlink /etc/systemd/system/multi-user.target.wants/docker.service → /us
r/lib/systemd/system/docker.service.
Created symlink /etc/systemd/system/sockets.target.wants/docker.socket → /usr/li
b/systemd/system/docker.socket.
Обрабатываются триггеры для man-db (2.12.0-4build2) …
ruhshona@ruhshona-Lenovo-V15-G4-AMN ~> sudo systemctl enable --now docker
ruhshona@ruhshona-Lenovo-V15-G4-AMN ~> docker run -it --name test-ca ubuntu:22.04 bash
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied

Run 'docker run --help' for more information
ruhshona@ruhshona-Lenovo-V15-G4-AMN ~ [126]> sudo docker run -it --name test-ca ubuntu:22.04 bash
Unable to find image 'ubuntu:22.04' locally
22.04: Pulling from library/ubuntu
b1cba2e842ca: Pull complete 
Digest: sha256:3ba65aa20f86a0fad9df2b2c259c613df006b2e6d0bfcc8a146afb8c525a9751
Status: Downloaded newer image for ubuntu:22.04
root@7a580310fbbd:/# 
root@7a580310fbbd:/# 
root@7a580310fbbd:/# 
root@7a580310fbbd:/# 
root@7a580310fbbd:/# apt update
Get:1 http://security.ubuntu.com/ubuntu jammy-security InRelease [129 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy InRelease [270 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [128 kB]
Get:4 http://security.ubuntu.com/ubuntu jammy-security/universe amd64 Packages [1301 kB]
Get:5 http://archive.ubuntu.com/ubuntu jammy-backports InRelease [127 kB]
Get:6 http://archive.ubuntu.com/ubuntu jammy/universe amd64 Packages [17.5 MB]
Get:7 http://security.ubuntu.com/ubuntu jammy-security/multiverse amd64 Packages [62.6 kB]
Get:8 http://security.ubuntu.com/ubuntu jammy-security/main amd64 Packages [3780 kB]
Get:9 http://security.ubuntu.com/ubuntu jammy-security/restricted amd64 Packages [6652 kB]
Get:10 http://archive.ubuntu.com/ubuntu jammy/multiverse amd64 Packages [266 kB]
Get:11 http://archive.ubuntu.com/ubuntu jammy/main amd64 Packages [1792 kB]    
Get:12 http://archive.ubuntu.com/ubuntu jammy/restricted amd64 Packages [164 kB]
Get:13 http://archive.ubuntu.com/ubuntu jammy-updates/universe amd64 Packages [1613 kB]
Get:14 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages [4120 kB]
Get:15 http://archive.ubuntu.com/ubuntu jammy-updates/restricted amd64 Packages [6877 kB]
Get:16 http://archive.ubuntu.com/ubuntu jammy-updates/multiverse amd64 Packages [70.9 kB]
Get:17 http://archive.ubuntu.com/ubuntu jammy-backports/universe amd64 Packages [37.2 kB]
Get:18 http://archive.ubuntu.com/ubuntu jammy-backports/main amd64 Packages [83.9 kB]
Fetched 44.9 MB in 11s (4062 kB/s)                                             
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
4 packages can be upgraded. Run 'apt list --upgradable' to see them.
root@7a580310fbbd:/# apt install -y openssl ca-certificates
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  ca-certificates openssl
0 upgraded, 2 newly installed, 0 to remove and 4 not upgraded.
Need to get 1346 kB of archives.
After this operation, 2511 kB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 openssl amd64 3.0.2-0ubuntu1.21 [1184 kB]
Get:2 http://archive.ubuntu.com/ubuntu jammy-updates/main amd64 ca-certificates all 20240203~22.04.1 [162 kB]
Fetched 1346 kB in 1s (1320 kB/s)         
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package openssl.
(Reading database ... 4393 files and directories currently installed.)
Preparing to unpack .../openssl_3.0.2-0ubuntu1.21_amd64.deb ...
Unpacking openssl (3.0.2-0ubuntu1.21) ...
Selecting previously unselected package ca-certificates.
Preparing to unpack .../ca-certificates_20240203~22.04.1_all.deb ...
Unpacking ca-certificates (20240203~22.04.1) ...
Setting up openssl (3.0.2-0ubuntu1.21) ...
Setting up ca-certificates (20240203~22.04.1) ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based fronte
nd cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 78.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Ter
m::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/pe
rl/5.34.0 /usr/local/share/perl/5.34.0 /usr/lib/x86_64-linux-gnu/perl5/5.34 /usr
/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/
5.34 /usr/share/perl/5.34 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/
FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Updating certificates in /etc/ssl/certs...
146 added, 0 removed; done.
Processing triggers for ca-certificates (20240203~22.04.1) ...
Updating certificates in /etc/ssl/certs...
0 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
root@7a580310fbbd:/# exit
exit
ruhshona@ruhshona-Lenovo-V15-G4-AMN ~> sudo docker cp ~/M/secure-local-web-system/ca/rootCA.crt test-ca:/root/rootCA.crt
lstat /home/ruhshona/M: no such file or directory
ruhshona@ruhshona-Lenovo-V15-G4-AMN ~ [1]> sudo docker cp ~/MyGitProjects/secure-local-web-system/ca/rootCA.crt test-ca:/root/rootCA.crt
Successfully copied 4.1kB to test-ca:/root/rootCA.crt
ruhshona@ruhshona-Lenovo-V15-G4-AMN ~> sudo docker start -ai test-ca
root@7a580310fbbd:/# cp /root/rootCA.crt /usr/local/share/ca-certificates/rootCA.crt
root@7a580310fbbd:/# update-ca-certificates
Updating certificates in /etc/ssl/certs...
rehash: warning: skipping ca-certificates.crt,it does not contain exactly one certificate or CRL
1 added, 0 removed; done.
Running hooks in /etc/ca-certificates/update.d...
done.
root@7a580310fbbd:/# openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt /usr/local/share/ca-certificates/rootCA.crt
/usr/local/share/ca-certificates/rootCA.crt: OK
root@7a580310fbbd:/# exit
exit

