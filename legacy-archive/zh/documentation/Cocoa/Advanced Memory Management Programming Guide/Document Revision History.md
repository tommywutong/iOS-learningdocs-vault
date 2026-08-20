---
title: 高级内存管理编程指南
apple_id: 10000011i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Performance
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/RevisionHistory.html
archived_at: '2026-07-15T07:16:41.052759Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [高级内存管理编程指南](About%20Memory%20Management.md)


[上一页](Using%20Autorelease%20Pool%20Blocks.md)

# 文档修订历史

下表描述了 _高级内存管理编程指南_ 的变更情况。

| __日期__ | __说明__ |
| --- | --- |
| 2012-07-17 | 更新为以 @autoreleasepool 块的方式来描述自动释放。 |
| 2011-09-28 | 更新以反映引入 ARC 之后本文档的新定位。 |
| 2011-03-24 | 为提高清晰度和简洁性进行了重大修订。 |
| 2010-12-21 | 澄清了 mutable copy 的命名规则。 |
| 2010-06-24 | 对内存管理基本规则做了少量措辞调整，以强调其简洁性。对“内存管理实践”做了少量补充。 |
| 2010-02-24 | 更新了 iOS 3.0 中处理内存警告的说明；部分重写了“对象所有权与处置”。 |
| 2009-10-21 | 扩充了“内存管理实践”中关于存取方法的章节。 |
| 2009-08-18 | 添加了指向相关概念的链接。 |
| 2009-07-23 | 更新了在 OS X 上声明 outlet 的指导说明。 |
| 2009-05-06 | 更正了排版错误。 |
| 2009-03-04 | 更正了排版错误。 |
| 2009-02-04 | 更新了“Nib 对象”一文。 |
| 2008-11-19 | 添加了关于在垃圾回收环境中使用自动释放池的章节。 |
| 2008-10-15 | 修正了缺失的图片。 |
| 2008-02-08 | 修正了指向“Carbon-Cocoa 集成指南”的失效链接。 |
| 2007-12-11 | 更正了排版错误。 |
| 2007-10-31 | 针对 OS X v10.5 进行了更新。更正了少量排版错误。 |
| 2007-06-06 | 更正了少量排版错误。 |
| 2007-05-03 | 更正了排版错误。 |
| 2007-01-08 | 添加了关于 nib 文件内存管理的文章。 |
| 2006-06-28 | 添加了一条关于 dealloc 与应用程序终止的注释。 |
| 2006-05-23 | 重新组织了本文档中的文章以改善阅读流程；更新了“对象所有权与处置”。 |
| 2006-03-08 | 澄清了关于对象所有权和 dealloc 的论述。把关于存取方法的论述移到了单独的一篇文章中。 |
| 2006-01-10 | 更正了排版错误。更新了文档标题，原标题为“Memory Management”。 |
| 2004-08-31 | 修改了“相关主题”链接，并更新了主题引言。 |
| 2003-06-06 | 在[使用自动释放池块](Using%20Autorelease%20Pool%20Blocks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqga2dolkdjjbemqsfireq)中扩充了对“自动释放池被释放时都有哪些对象会被释放”的说明，将显式和隐式自动释放的对象都包含在内。 |
| 2002-11-12 | 为已有主题添加了修订历史。它将用于记录该主题内容的变更。 |

[上一页](Using%20Autorelease%20Pool%20Blocks.md)

