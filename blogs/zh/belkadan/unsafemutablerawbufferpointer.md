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
translated: true
---

> 原文：[UnsafeMutableRawBufferPointer](https://belkadan.com/blog/2022/03/UnsafeMutableRawBufferPointer/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [动态链接对 App 不好，静态链接同样对 App 不好](https://belkadan.com/blog/2022/02/Dynamic-Linking-and-Static-Linking/)

[#TalkPay](https://belkadan.com/blog/2022/03/TalkPay/) »

« [Swift 的遗憾：总结](https://belkadan.com/blog/2021/12/Swift-Regrets-Wrap-up/?tag=swift)

[默认参数与基于标签的重载](https://belkadan.com/blog/2022/04/Default-Arguments-and-Label-based-Overloading/?tag=swift) »

## [UnsafeMutableRawBufferPointer](#)

因为工作里提到了这个话题，这里回顾一下 Swift 指针的命名法：

- Unsafe——因为它确实如此
- ? Mutable——相对于 const 而言
- ? Raw——相对于带类型的而言，把 C 语言 `void *` 的特殊性单独归入了它自己的类型
- ? Buffer——知道自己的长度
- Pointer——因为它不拥有数据

_最初发布于 [Twitter](https://twitter.com/UINT_MIN/status/1499201275740577793)。_

本文发表于 [三月](https://belkadan.com/blog/2022/03) 02 日, [2022](https://belkadan.com/blog/2022)，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[社交媒体导入](https://belkadan.com/blog/tags/social-media-import)
