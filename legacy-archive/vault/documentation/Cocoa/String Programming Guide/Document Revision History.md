---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/RevisionHistory.html
archived_at: '2026-07-15T07:19:35.682742Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Index.md)[上一页](Drawing%20Strings.md)

# 文档修订历史

下表描述了 _字符串编程指南_ 的变更。

| __日期__ | __说明__ |
| --- | --- |
| 2014-02-11 | 增加了关于词边界划分的说明，并把章节标题改为“词、段落与换行”。 |
| 2013-09-17 | 修正了“格式化字符串对象”一文中代码片段的排版错误。 |
| 2012-12-13 | 澄清了对 NSAnchoredSearch 选项的描述。 |
| 2012-07-17 | 更新了代码片段，以采用新的 Objective-C 特性。 |
| 2012-06-11 | 把字符串常量的字符集更正为 UTF-8。增加了关于使用 localizedStandardCompare: 实现 Finder 式排序的指导。增加了避免对从右到左书写的语言使用 %s 的注意事项。修订了“字符串格式说明符”一文。 |
| 2009-10-15 | 增加了指向 Cocoa Core Competencies 的链接。 |
| 2008-10-15 | 新增了关于字符簇的文章；更新了字符串格式说明符列表。 |
| 2007-10-18 | 修正了少量排版错误。 |
| 2007-07-10 | 在“字符串格式说明符”中增加了关于 NSInteger 和 NSUInteger 的说明。 |
| 2007-03-06 | 修正了少量排版错误。 |
| 2007-02-08 | 修正了不完整的句子，并改进了“扫描器”一文中的示例。 |
| 2006-12-05 | 增加了演示搜索和路径操作的代码示例。 |
| 2006-11-07 | 对“扫描器”一文做了少量修订。 |
| 2006-10-03 | 增加了指向路径操作方法的链接。 |
| 2006-06-28 | 修正了排版错误。 |
| 2006-05-23 | 新增了一篇文章“从文件和 URL 读取字符串以及将字符串写入文件和 URL”；大幅更新了“创建与转换字符串”。 |
|  | 把“创建字符集”并入[字符集](Character%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dmlkciffeessiindq)。 |
| 2006-01-10 | 把标题从“Strings”改为符合参考文档一致性规范的名称。 |
| 2004-06-28 | 增加了[格式化字符串对象](Formatting%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dglkdjjbekqkfjbea)一文。在简介中增加了 _Data Formatting_ 和 Core Foundation _Strings_ 编程主题。 |
| 2004-02-06 | 增加了关于自定义 Unicode 字符集的说明，并补回了“创建字符集”中缺失的代码片段。增加了关于[绘制字符串](Drawing%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2tclkcijbuqqkhirdq)的说明和交叉引用。重写了简介并增加了索引。 |
| 2003-09-09 | 在[搜索、比较与排序字符串](Searching%2C%20Comparing%2C%20and%20Sorting%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dslkdjjbeer2cifeq)中增加了 `NSNumericSearch` 的说明。 |
| 2003-03-17 | 恢复了[扫描器](Scanners.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dolkcineukrshjbbq)中缺失的示例代码。 |
| 2003-01-17 | 更新了[创建与转换字符串对象](Creating%20and%20Converting%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dqlkdjjbegssijbeq)，推荐使用 UTF8 编码，并指出 `cString...` 系列方法即将废弃。 |
| 2002-11-12 | 在已有主题中加入了修订历史。 |

[下一页](Index.md)[上一页](Drawing%20Strings.md)

