---
title: 键值编码编程指南
apple_id: 10000107i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/RevisionHistory.html
archived_at: '2026-07-15T07:16:15.589867Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值编码编程指南](index.md)



## 文档修订历史

下表说明了《键值编码编程指南》的变更。

| 日期 | 说明 |
| --- | --- |
| 2016-10-27 | 现代化并更新了内容。 |
| 2012-07-17 | 针对 OS X v10.8 更新，纳入新的 Objective-C 功能。 |
| 2011-06-06 | 针对 OS X v10.7 更新，纳入有序唯一化关系。 |
| 2010-09-01 | 阐明 `valueWithRect:` 仅适用于 OS X。修订“集合运算符”一章。 |
| 2010-04-28 | 修正了排版错误。 |
| 2010-01-20 | 阐明“注册依赖键”与 Core Data 托管对象之间的交互。修正“可变无序访问器”的描述。 |
| 2009-02-04 | 添加了大量任务信息和示例代码。 |
| 2007-06-06 | 添加警告，说明数组和集合运算符遇到 `nil` 值时会引发异常。 |
| 2007-01-08 | 添加注意事项：应检查 `validateName:error:` 中的 `error` 参数，并确保返回有效的 `NSError` 对象。 |
| 2006-06-28 | 将《键值观察编程指南》添加到相关文档列表中。 |
| 2006-04-04 | 添加了 `-get<Key>:range:` 访问器模式的示例方法签名。 |
| 2006-03-08 | 修正了 `@distinctUnionOfArrays` 示例中的变量名。 |
| 2005-08-11 | 更改了“为何使用键值编码”一文的标题。 |
| 2005-07-07 | 添加了集合运算符 `@unionOfSets` 和 `@distinctUnionOfSets` 的说明。阐明 `validateValue:forKey:` 的返回策略。 |
| 2005-04-29 | 修正了少量排版错误。 |
| 2004-08-31 | 更新了目录。阐明 `@sum` 数组运算符会在[使用集合运算符](CollectionOperators.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tmlkciffekqkjivcq)中返回 `NSNumber`。修正了少量排版错误。 |
| 2004-06-28 | 修正了排版错误。 |
| 2004-04-19 | 阐明在“对多属性的集合访问器模式”中，索引式访问器方法会使属性表现为数组。 |
| 2003-10-15 | 针对 OS X v10.3 重写了《键值编码》。 |
| 2003-07-19 | 更新[访问器搜索模式](SearchImplementation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2tklkdjjbeeqsgizaq)，加入 OS X v10.3 中已弃用方法的信息。 |
| 2002-11-12 | 为《键值编码》添加了修订历史。 |
