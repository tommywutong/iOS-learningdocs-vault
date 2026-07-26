---
title: UnsafeMutableRawBufferPointer
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2022/03/UnsafeMutableRawBufferPointer/'
original_language: en
published: 2022-03-02
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6a66bb4118856168'
translated: false
---

> 原文：[UnsafeMutableRawBufferPointer](https://belkadan.com/blog/2022/03/UnsafeMutableRawBufferPointer/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [Dynamic Linking Is Bad For Apps And Static Linking Is Also Bad For Apps](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/)

[#TalkPay](https://belkadan.com/blog/2022/03/TalkPay/) »

« [Swift Regrets: Wrap-up](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=swift)

[Default Arguments and Label-based Overloading](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=swift) »

## [UnsafeMutableRawBufferPointer](#)

Because it came up at work, a recap of Swift pointer nomenclature:

- Unsafe - because it is
- ? Mutable - vs const
- ? Raw - vs typed, puts the specialness of C’s `void *` in its own type
- ? Buffer - knows its length
- Pointer - because it doesn’t own the data

_Originally posted [on Twitter](https://twitter.com/UINT_MIN/status/1499201275740577793)._

This entry was posted on [March](https://belkadan.com/blog/2022/03) 02, [2022](https://belkadan.com/blog/2022) and is filed under [Technical](https://belkadan.com/blog/technical). Tags: [Swift](https://belkadan.com/blog/tags/swift), [Social media import](https://belkadan.com/blog/tags/social-media-import)
