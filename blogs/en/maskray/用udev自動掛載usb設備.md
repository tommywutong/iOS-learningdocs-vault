---
title: 用udev自動掛載usb設備
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2011-08-12-udev-automount-usb'
original_language: en
published: 2011-08-12
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fbac791e22db3c8c'
translated: false
---

> 原文：[用udev自動掛載usb設備](https://maskray.me/blog/2011-08-12-udev-automount-usb)　·　MaskRay (宋方睿)

[2011-08-12](https://maskray.me/blog/2011-08-12-udev-automount-usb)

# 用udev自動掛載usb設備

前幾天看了 `udev` 的介紹，今天正好 `#ubuntu-cn@freenode` 裏有人問，就把這個老大難問題解決掉了。

代碼如下：

```
KERNEL!="sd[b-z]?", GOTO="automount_exit"
ACTION=="add", SUBSYSTEM=="block", RUN+="/bin/mkdir /media/%E{ID_FS_LABEL}-%E{ID_FS_UUID}", RUN+="/bin/mount -o uid=1000,user,codepage=936,utf8 $root/%k /media/%E{ID_FS_LABEL}-%E{ID_FS_UUID}"
ACTION=="remove", SUBSYSTEM=="block", RUN+="/bin/umount /media/%E{ID_FS_LABEL}-%E{ID_FS_UUID}", RUN+="/bin/rmdir /media/%E{ID_FS_LABEL}-%E{ID_FS_UUID}"
LABEL="automount_exit"
```

保存爲 `/etc/udev/rules.d/` 下的某個文件。

第一行用 `glob` 跳過名稱非 `sd[b-z]?` 字樣的。

`%E{ID_FS_LABEL}` 是卷標，`%E{ID_FS_UUID}` 是 `UUID`，第二行就是檢測 `add` 事件，先根據卷標和 `UUID` 在 `/media/` 下創建一個目錄然後掛載。

第三行是相應的卸載命令。
