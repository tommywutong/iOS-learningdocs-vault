---
title: 使用 SQLite Magellan 漏洞让 Chrome 70 崩溃
source: worthdoingbadly (Zhuowei Zhang)
source_key: worthdoingbadly
source_url: 'https://worthdoingbadly.com/sqlitebug/'
original_language: en
published: 2018-12-14
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:25d74767c9b66953'
translated: true
---

> 原文：[Crash Chrome 70 with the SQLite Magellan bug](https://worthdoingbadly.com/sqlitebug/)　·　worthdoingbadly (Zhuowei Zhang)

# 使用 SQLite Magellan 漏洞让 Chrome 70 崩溃

2018 年 12 月 14 日

本概念验证使用[腾讯 Blade 团队的 Magellan SQLite3 漏洞](https://blade.tencent.com/magellan/index_en.html)导致 Chrome 渲染器进程崩溃。它基于修复该漏洞的提交中的[一个 SQLite 测试用例](https://www.sqlite.org/src/info/940f2adc8541a838)。

如果你正在使用 Chrome 70 或更低版本，点击下面的按钮即可使此页面崩溃：

你的浏览器的 user agent 是：无法在未启用 JavaScript 的情况下获取。请开启 JavaScript！

[此页面的源代码，托管于 GitHub](https://github.com/zhuowei/worthdoingbadly.com/blob/master/_posts/2018-12-14-sqlitebug.html)。

# 注册以获取更多信息

我正在研究此问题对浏览器的影响。若想在我更新此页面时收到通知，请注册我的邮件列表：

# 预期会发生什么？

按下按钮后，页面应该会崩溃：

![截图](https://worthdoingbadly.com/assets/blog/sqlitebug/sqlite_cropped.png)

在 Android 5.1 上，我在 memcpy 中遇到了段错误：

```
        F/libc    ( 3801): Fatal signal 11 (SIGSEGV), code 1, fault addr 0xe0ddb457 in tid 3854 (Database thread)
        I/DEBUG   (  142): *** *** *** *** *** *** *** *** *** *** *** *** *** *** *** ***
        I/DEBUG   (  142): Build fingerprint: 'google/nakasi/grouper:5.1/LMY47D/1743759:user/release-keys'
        I/DEBUG   (  142): Revision: '0'
        I/DEBUG   (  142): ABI: 'arm'
        I/DEBUG   (  142): pid: 3801, tid: 3854, name: Database thread  >>> com.android.chrome:sandboxed_process6 <<<
        I/DEBUG   (  142): signal 11 (SIGSEGV), code 1 (SEGV_MAPERR), fault addr 0xe0ddb457
        I/DEBUG   (  142):     r0 e0ddb457  r1 611be0ab  r2 00000002  r3 ff000000
        I/DEBUG   (  142):     r4 611be038  r5 00000002  r6 611be0a9  r7 7fffffff
        I/DEBUG   (  142):     r8 00000001  r9 611be0ab  sl 80000001  fp 00000000
        I/DEBUG   (  142):     ip 00000066  sp 6defd3a0  lr 00000074  pc 4025eb62  cpsr 680f2430
        I/DEBUG   (  142): 
        I/DEBUG   (  142): backtrace:
        I/DEBUG   (  142):     #00 pc 0000fb62  /system/lib/libc.so (__memcpy_base+217)
        I/DEBUG   (  142):     #01 pc 018d0e1d  /data/app/com.android.chrome-1/base.apk
```

# 影响范围

受影响：经测试，会导致一个标签页/一个窗口崩溃：

- Android 5.1 和 9 上的 Chrome 70.0.3538.110
- macOS 10.14 上的 Electron 2.0.12

不受影响：

- Android 8.1 上的 Chrome 71.0.3578.98（已修复）
- Safari（SQLite3 中未启用 FTS）
- 非基于 Chrome 的浏览器（不支持 WebSQL）

[https://worthdoingbadly.com/sqlitebug/](https://worthdoingbadly.com/sqlitebug/)
