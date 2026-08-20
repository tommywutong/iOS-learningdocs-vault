---
title: 归档与序列化编程指南
apple_id: 10000047i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html
archived_at: '2026-07-15T05:25:39.999013Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[下一页](Object%20Graphs.md)

# 归档与序列化简介

归档和序列化是两种创建与体系结构无关的层次化数据字节流的方式。字节流随后可以写入文件，或传输给另一个进程，也许是通过网络传输。当字节流被解码时，其层次结构会被重新生成。归档提供了一组相互关联的对象和值的详细记录。序列化仅记录属性列表值的简单层次结构。

阅读本文档可以学习如何创建和提取对象图的归档表示。

本编程主题包含以下文章：

- [Object Graphs](Object%20Graphs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4tglkdjjbeirsjijeq) 介绍了对象图的概念，并讨论了将对象转换为字节流的两种技术：归档和序列化。
- [Archives](Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dmlkciffeiqskifeq) 描述了不同类型的归档和归档器类。
- [Creating and Extracting Archives](Creating%20and%20Extracting%20Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dslkcifbeoqsiinaq) 描述了如何创建和提取归档。
- [Encoding and Decoding Objects](Encoding%20and%20Decoding%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dqlkcineuqqskircq) 描述了如何实现使对象能够在归档中编码和解码的方法。
- [Encoding and Decoding C Data Types](Encoding%20and%20Decoding%20C%20Data%20Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgi4tilkcijbuerciijeq) 描述了如何编码和解码那些在归档类中没有便捷方法的 C 数据类型。
- [Forward and Backward Compatibility for Keyed Archives](Forward%20and%20Backward%20Compatibility%20for%20Keyed%20Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrga2tklkcineugrsgi5cq) 提供了一些技巧，帮助你的类在键控归档中与之前和之后的版本保持更好的兼容性。
- [Subclassing NSCoder](Subclassing%20NSCoder.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tclkcifbekskfjbdq) 提供了一些关于如何创建自己的编码器类的技巧。
- [Serializing Property Lists](Serializing%20Property%20Lists.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2telkcifbeerkkivcq) 描述了如何创建和读取属性列表的序列化表示。

[下一页](Object%20Graphs.md)
