---
title: 15-inch MacBook Pro (mid-2010) Crashing to Black Screen
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2012/05/15-inch-mbp-mid-2010-crashing-to-black-screen/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:abfb6b4454dbbf50'
translated: false
---

> 原文：[15-inch MacBook Pro (mid-2010) Crashing to Black Screen](https://oleb.net/blog/2012/05/15-inch-mbp-mid-2010-crashing-to-black-screen/)　·　Ole Begemann

# 15-inch MacBook Pro (mid-2010) Crashing to Black Screen

A few months ago, my mid-2010 MacBook Pro began crashing regularly. All of a sudden, the screen would turn black and the machine would not react to any keyboard or mouse input anymore. All I could do was hold down the power button to turn the computer off.

At first, these crashes were pretty rare (perhaps once a week). Over the last months they became more and more frequent, though; in recent weeks, my machine would crash to the blank screen at least once per day.

No matter what I tried, the crashes were not reproducible. They would often (but not always) happen immediately after the computer woke from sleep; other occurrences seemed totally random just as I was switching between apps or just moving the mouse pointer across the screen. The crashes happened at least on OS X 10.7.3 and 10.7.4.

When I rebooted the machine after such a crash, I invariably got the report that a kernel panic had occurred. Here is an excerpt from a typical crash log:

```
Interval Since Last Panic Report:  9147 sec
Panics Since Last Report:          1
Anonymous UUID:                    8E0F3CDF-5FE0-49F5-BFD7-1B28C94D4BA0

Fri May 18 09:54:36 2012
panic(cpu 0 caller 0xffffff7f80918947): NVRM[0/1:0:0]: Read Error 0x00000100: CFG 0xffffffff 0xffffffff 0xffffffff, BAR0 0xd2000000 0xffffff8113bbc000 0x0a5480a2, D0, P3/4
Backtrace (CPU 0), Frame : Return Address
0xffffff80f0bf3610 : 0xffffff8000220792
0xffffff80f0bf3690 : 0xffffff7f80918947
0xffffff80f0bf3720 : 0xffffff7f80a08aa4
0xffffff80f0bf3770 : 0xffffff7f80a08b64
0xffffff80f0bf37d0 : 0xffffff7f80cb5749
0xffffff80f0bf3910 : 0xffffff7f80a27bed
0xffffff80f0bf3940 : 0xffffff7f809222c2
0xffffff80f0bf39f0 : 0xffffff7f8091dbc4
0xffffff80f0bf3be0 : 0xffffff7f8091e6ed
0xffffff80f0bf3cc0 : 0xffffff7f817c0542
0xffffff80f0bf3d40 : 0xffffff7f817c1364
0xffffff80f0bf3d80 : 0xffffff7f817bec95
0xffffff80f0bf3da0 : 0xffffff7f817c1c61
0xffffff80f0bf3de0 : 0xffffff7f817c20d9
0xffffff80f0bf3e00 : 0xffffff7f817bef04
0xffffff80f0bf3e20 : 0xffffff7f817d636d
0xffffff80f0bf3e40 : 0xffffff7f817d64b8
0xffffff80f0bf3ea0 : 0xffffff7f817e8560
0xffffff80f0bf3ec0 : 0xffffff7f817e89d8
0xffffff80f0bf3ef0 : 0xffffff800063c5b6
0xffffff80f0bf3f30 : 0xffffff800063b330
0xffffff80f0bf3f70 : 0xffffff800063b1d4
0xffffff80f0bf3fb0 : 0xffffff8000820057
      Kernel Extensions in backtrace:
         com.apple.NVDAResman(7.1.8)[560E1257-BF5E-3B0B-95F0-15033A0D1B97]@0xffffff7f808b8000->0xffffff7f80b91fff
            dependency: com.apple.iokit.IOPCIFamily(2.6.8)[06C77CAA-586C-3AA7-94B7-A544F470025E]@0xffffff7f80843000
            dependency: com.apple.iokit.IONDRVSupport(2.3.2)[D05CFB53-FB72-3613-8162-2D188DB04738]@0xffffff7f808a6000
            dependency: com.apple.iokit.IOGraphicsFamily(2.3.2)[2D2A4A31-EB4F-3730-BE3A-76C061685FC5]@0xffffff7f8086e000
         com.apple.nvidia.nv50hal(7.1.8)[7596DB8C-AE9D-3C87-B11A-0ED8F940CAF8]@0xffffff7f80b92000->0xffffff7f80eb3fff
            dependency: com.apple.NVDAResman(7.1.8)[560E1257-BF5E-3B0B-95F0-15033A0D1B97]@0xffffff7f808b8000
         com.apple.GeForce(7.1.8)[00925AF3-22EE-3858-8BD3-06AE57DFCC86]@0xffffff7f8177d000->0xffffff7f8183cfff
            dependency: com.apple.NVDAResman(7.1.8)[560E1257-BF5E-3B0B-95F0-15033A0D1B97]@0xffffff7f808b8000
            dependency: com.apple.iokit.IONDRVSupport(2.3.2)[D05CFB53-FB72-3613-8162-2D188DB04738]@0xffffff7f808a6000
            dependency: com.apple.iokit.IOPCIFamily(2.6.8)[06C77CAA-586C-3AA7-94B7-A544F470025E]@0xffffff7f80843000
            dependency: com.apple.iokit.IOGraphicsFamily(2.3.2)[2D2A4A31-EB4F-3730-BE3A-76C061685FC5]@0xffffff7f8086e000

BSD process name corresponding to current thread: kernel_task

Mac OS version:
11E53

Kernel version:
Darwin Kernel Version 11.4.0: Mon Apr  9 19:32:15 PDT 2012; root:xnu-1699.26.8~1/RELEASE_X86_64
Kernel UUID: A8ED611D-FB0F-3729-8392-E7A32C5E7D74
System model name: MacBookPro6,2 (Mac-F22586C8)

…
```

One common feature of all the crashlogs were the kernel extensions in the backtrace at the time of the crash: `com.apple.NVDAResman`, `com.apple.nvidia.nv50hal`, `com.apple.GeForce`. All three are part of the Nvidia graphics drivers for the MacBook Pro’s [Nvidia GeForce GT 330M](http://www.geforce.com/hardware/desktop-gpus/geforce-gt-330m) GPU. This made me suspect that the issue had something to do with the GPU hardware or software. Perhaps the computer crashed every time the system switched from the integrated graphics hardware to the dedicated GPU?

# Known issue, Apple replaces logic board for free

After a lot of googling, I finally found an Apple support document that dealt with exactly my problem: [MacBook Pro (15-inch, Mid 2010): Intermittent black screen or loss of video](http://support.apple.com/kb/TS4088?viewlocale=en_US).

> Apple has determined that a small number of MacBook Pro (15-inch, Mid 2010) computers may intermittently freeze or stop displaying video on the built-in display or on an external display connected to the MacBook Pro. In this situation, you may also see a restart warning message before the video is lost or the display turns black or gray. Affected computers were manufactured between April 2010 and February 2011.

Fortunately, Apple offers a free repair for affected computers if they are not older than ~~two~~three years:

> Apple will service affected 15-inch MacBook Pro computers free of charge until three years from date of purchase. Apple will provide further extensions to this program as needed.

I bought my MBP in June 2010 so I was lucky enough to get it repaired for free. They replaced the entire logic board, which otherwise would have cost me hundreds of euros. I had a look inside the case and it seems they even replaced the fans with brand-new ones (or cleaned the old ones really thoroughly)!

![My mid-2010 MacBook Pro from the inside](https://oleb.net/media/2012-05-30-iPh-010590.jpg)

<sub>My mid-2010 MacBook Pro with its brand-new replaced logic board. They even replaced the old fans!</sub>

If you also have a mid-2010 MacBook Pro that is younger than ~~two~~three years and you experience crashes from time to time, it might be worth bringing it to an Apple store.

**Update September 17, 2012:** Apple extended the coverage of their free logic board replacement program from two to three years after date of purchase.
