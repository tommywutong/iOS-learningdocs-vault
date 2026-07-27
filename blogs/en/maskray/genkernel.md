---
title: genkernel
source: MaskRay (宋方睿)
source_key: maskray
source_url: 'https://maskray.me/blog/2010-05-24-genkernel-in-gentoo'
original_language: en
published: 2010-05-24
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:0d5ce22f54895281'
translated: false
---

> 原文：[genkernel](https://maskray.me/blog/2010-05-24-genkernel-in-gentoo)　·　MaskRay (宋方睿)

[2010-05-24](https://maskray.me/blog/2010-05-24-genkernel-in-gentoo)

# genkernel

第一次爲gentoo編譯內核，發現默認選項沒有有線網絡支持（沒有eth0設備），也不管哪些選項是自己真正需要的，選了很多。恰好`linux-2.6.34-gentoo`出來了，就嘗試着重新配置一下。

```bash
genkernel --bootloader=grub --menuconfig --no-clean all
```

以前不知道要用`--no-clean`，每次編譯都要花很長時間，這個選項可以讓`genkernel`不去執行 `make clean`，第二次編譯花的時間就會少很多

File systems \<_\> The Extended 4 (ext4) filesystem #我大部分分區用的是 ext4，這一項默認沒有設 \<_\> Reiserfs support #/usr/portage 下有很多目錄和小文件，所以我單獨掛載在一個 reiserfs 分區 -_- Native language support \<_\> Simplified Chinese charset (CP936, GB2312) \<*\> Traditional Chinese charset (Big5)

Executable file formats / Emulations [*] IA32 Emulation #這個好像是執行 32-bit ELF 的，否則像 firefox-bin wine 等就無法運行

我的網卡是Broadcom Corporation NetLink BCM57780 Gigabit Ethernet PCIe

```plaintext
Device Drivers
    Network device support
        PHY Device support and infrastructure
            [*] Drivers for Broadcom PHYs
        Ethernet (100 Mbit)
            [*] Broadcom Tigon3 support
```

我的framebuffer的配置：

```bash
emerge -av v86d
```

```plaintext
General Setup ->
    (/usr/share/v86d/initramfs) Initramfs source file(s)
Device Drivers
    <*> Connector - unified userspace <-> kernelspace linker
    Support for frame buffer devices
        [*] Enable firmware EDID
        [*] Enable Video mode handling helpers
    [ ] Enable Tile Blitting Support #選擇了這一項 CONFIG_FB_CON_DECOR 選項就沒有了
        [*] Userspace VESA VGA graphics support
    Console display driver support
        Framebuffer Console Support
            [*] Support for the Framebuffer Console Decorations
```
