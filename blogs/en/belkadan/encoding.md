---
title: Encoding
source: Belkadan (Jordan Rose, 前 Swift 编译器工程师)
source_key: belkadan
source_url: 'https://belkadan.com/blog/tags/encoding'
original_language: en
published: ''
status: active
license: Copyright 2012–2020 Jordan Rose → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:bff8bdccc4600a94'
translated: false
---

> 原文：[Encoding](https://belkadan.com/blog/tags/encoding)　·　Belkadan (Jordan Rose, 前 Swift 编译器工程师)

## [YAML is (not) my preferred configuration format](https://belkadan.com/blog/2026/03/YAML-Is-Not-My-Preferred-Configuration-Format/?tag=encoding)

17 March 2026

Sometimes you have configuration files or simple data files that you want to maintain by hand, in a text editor. There are dozen of reusable formats for this, but only a few of them really support _hierarchical_ entries. You can argue that configuration files should stay relatively flat, but if you eventually run into a situation where you _need_ hierarchy, you’ll be unhappy not to have it.

[(Continue reading…)](https://belkadan.com/blog/2026/03/YAML-Is-Not-My-Preferred-Configuration-Format/?tag=encoding)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Encoding](https://belkadan.com/blog/tags/encoding)

## [Protobuf Is Almost Streamable](https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/?tag=encoding)

14 December 2023

[Protobuf](https://protobuf.dev) is a binary (non-textual) encoding format invented by Google. It has some nice properties and some less nice properties.^[1](#fn:recommendation) But one that’s a little frustrating is that it’s _almost_ a streamable format—that is, one where you can process data as it comes in, rather than waiting until you’ve read all of it.

[(Continue reading…)](https://belkadan.com/blog/2023/12/Protobuf-Is-Almost-Streamable/?tag=encoding)

Posted in [Technical](https://belkadan.com/blog/technical). Tags: [Encoding](https://belkadan.com/blog/tags/encoding)
