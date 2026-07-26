---
title: 一个闪亮的魔数
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/2019/02/A-Shiny-Magic-Number/'
original_language: en
published: 2019-02-21
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:e04fe59324584983'
translated: true
---

> 原文：[A Shiny Magic Number](https://belkadan.com/blog/2019/02/A-Shiny-Magic-Number/)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

« [误导性指标与 UX 权衡](https://belkadan.com/blog/2018/04/Misleading-Metrics/)

[\> 向东](https://belkadan.com/blog/2019/08/go-east/) »

« [「FIXME」不总是意味着「修复我」](https://belkadan.com/blog/2018/04/FIXME/?tag=swift)

[离开 Apple](https://belkadan.com/blog/2019/11/Leaving-Apple/?tag=swift) »

## [一个闪亮的魔数](#)

既然 Swift 的某个代号已经被[一个「权威消息源」泄露出来了](https://oleb.net/2019/chris-lattner-swift-origins/)，我就顺便说说我埋进去的一个小彩蛋：swiftmodule 文件的「魔数」是 `E2 9C A8 0E`。前三个字节是 ✨（U+2728 SPARKLES）的 UTF-8 编码。

最后一个字节也有讲究：作为字符它是 U+000E SHIFT OUT，一个基本没人用的 ASCII 控制字符。它十进制也是「14」，就像「2014」——我们当时希望 Swift 1 能在这一年发布。（我记得我做这个的时候是 2013 年。）

现在回头看，我其实有点后悔这么做，因为一个二进制格式的魔数最好完全不是合法的 UTF-8，不过紧接着的四个字节是 LLVM bitstream 格式的开头，这几乎能保证后两个字节是 00 00。所以它不会被误认成文本。

现在我正在做那个将会取代 swiftmodule 文件的格式（在某些情况下，见 [https://forums.swift.org/t/plan-for-module-stability/14551](https://forums.swift.org/t/plan-for-module-stability/14551)）。不过那个 ✨ 会继续留在相关的 swiftdoc 文件里（`E2 9C A8 07`），这个格式后来证明是值得稳定下来的二进制格式。

感谢 [Harlan Haskins](https://mastodon.social/@harlan) 推了我一把，让我讲出这个故事。（他也是模块稳定性工作的合作者之一。）

P.S. 如果你不知道这里说的「魔数」是什么，那今天算你走运！去看看 [https://en.wikipedia.org/wiki/File_format#Magic_number](https://en.wikipedia.org/wiki/File_format#Magic_number)，里面还有一句很有意思的话，「魔法数据库」。

_最初发布于 [Twitter](https://twitter.com/UINT_MIN/status/1098628355539124224)。_

本文发表于 [二月](https://belkadan.com/blog/2019/02) 21 日, [2019](https://belkadan.com/blog/2019)，归类于 [技术](https://belkadan.com/blog/technical)。标签：[Swift](https://belkadan.com/blog/tags/swift)、[社交媒体导入](https://belkadan.com/blog/tags/social-media-import)
