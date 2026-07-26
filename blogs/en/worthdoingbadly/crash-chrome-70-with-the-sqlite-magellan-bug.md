---
title: Crash Chrome 70 with the SQLite Magellan bug
source: worthdoingbadly (Zhuowei Zhang)
source_key: worthdoingbadly
source_url: 'https://worthdoingbadly.com/sqlitebug/'
original_language: en
published: 2018-12-14
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:25d74767c9b66953'
translated: false
---

> 原文：[Crash Chrome 70 with the SQLite Magellan bug](https://worthdoingbadly.com/sqlitebug/)　·　worthdoingbadly (Zhuowei Zhang)

# Crash Chrome 70 with the SQLite Magellan bug

Dec 14, 2018

This proof-of-concept crashes the Chrome renderer process using [Tencent Blade Team's Magellan SQLite3 bug](https://blade.tencent.com/magellan/index_en.html). It's based on [a SQLite test case](https://www.sqlite.org/src/info/940f2adc8541a838) from the commit that fixed the bug.

If you're using Chrome 70 or below, tap the button below to crash this page:

Your browser's user agent is: not available without JavaScript. Turn it on!

[Source code for this page on GitHub](https://github.com/zhuowei/worthdoingbadly.com/blob/master/_posts/2018-12-14-sqlitebug.html).

# Sign up for more information

I'm working on understanding how this issue affects browsers. To get notified when I update this page, please sign up to my mailing list:

# What's supposed to happen?

After you press the button, the page should crash:

![screenshot](https://worthdoingbadly.com/assets/blog/sqlitebug/sqlite_cropped.png)

On Android 5.1, I get a segfault in memcpy:

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

# What's affected?

Affected: tested, causes one tab/one window to crash:

- Chrome 70.0.3538.110 on Android 5.1 and 9
- Electron 2.0.12 on macOS 10.14

Not affected:

- Chrome 71.0.3578.98 on Android 8.1 (already fixed)
- Safari (doesn't have FTS enabled in SQLite3)
- Browsers not based on Chrome (no WebSQL support)
