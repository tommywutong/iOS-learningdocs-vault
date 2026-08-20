---
title: 谓词编程指南
apple_id: TP40001789
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/AdditionalChapters/Introduction.html
archived_at: '2026-07-15T07:17:41.514450Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md)


[下一页](Creating%20Predicates.md)

# 简介

谓词（predicate）为在 Cocoa 中描述查询提供了一种通用手段。谓词系统能够应对为数众多的应用领域，其中包括 Core Data 和 Spotlight。本文档从总体上介绍谓词，包括它们的用法、语法以及局限。

在 Cocoa 中，_谓词_是一条求值结果为布尔值（真或假）的逻辑语句。谓词分为两类，分别称为_比较谓词_和_复合谓词_：

- _比较谓词_（comparison predicate）用一个_运算符_（operator）比较两个_表达式_（expression）。这两个表达式分别称为谓词的左端和右端（运算符位于中间）。比较谓词先对表达式求值，再以求值结果调用运算符，并返回调用结果。
- _复合谓词_（compound predicate）比较另外两个或多个谓词的求值结果，或者对另一个谓词取反。

Cocoa 支持种类广泛的谓词，包括以下这些：

- 简单比较，例如 `grade == 7` 或 `firstName like 'Mark'`
- 不区分大小写或不区分变音符号的查找，例如 `name contains[cd] 'citroen'`
- 逻辑运算，例如 `(firstName beginswith 'M') AND (lastName like 'Adderley')`

你还可以为关系创建谓词——例如 `group.name matches 'work.*'`、`ALL children.age > 12` 和 `ANY children.age > 12`——也可以为诸如 `@sum.items.price < 1000` 这样的运算创建谓词。

Cocoa 谓词提供了一种编码查询的方式，这种方式与存放待检索数据的存储无关。你可以用谓词来表达逻辑条件，从而约束 Spotlight 和 Core Data 检索到的对象集合，也可以用它对内存中的对象做筛选。

你可以对任意类的对象使用谓词，但对于你想在谓词中使用的那些键，该类必须符合[键值编码](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25)规范。

### 谓词相关的类

Cocoa 提供了 [NSPredicate](https://developer.apple.com/documentation/foundation/nspredicate) 以及它的两个子类 [NSComparisonPredicate](https://developer.apple.com/documentation/foundation/nscomparisonpredicate) 和 [NSCompoundPredicate](https://developer.apple.com/documentation/foundation/nscompoundpredicate)。

`NSPredicate` 类提供了对谓词求值的方法，以及从字符串（例如 `firstName like 'Mark'`）创建谓词的方法。当你从字符串创建谓词时，`NSPredicate` 会为你创建相应的谓词实例和表达式实例。在某些场景下，你会想自己创建比较谓词或复合谓词，这时就可以使用 `NSComparisonPredicate` 和 `NSCompoundPredicate` 类。

Cocoa 中的谓词表达式由 [NSExpression](https://developer.apple.com/documentation/foundation/nsexpression) 类的实例表示。最简单的谓词表达式代表一个常量值。不过更常见的是，你使用的表达式会去取谓词当前求值对象上某个键路径（key path）对应的值。你还可以创建表达式来代表谓词当前正在求值的对象、充当变量的占位符，或者返回对数组执行某项运算的结果。

关于创建谓词和表达式的更多内容，请参阅[创建谓词](Creating%20Predicates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojtfvbuuqseijeegqq)。

### 约束与局限

如果你将谓词用于 Core Data 或 Spotlight，请注意它们必须能与对应的数据存储配合工作。谓词查询并没有特定的实现语言；根据后端存储的要求（如果确实存在后端存储的话），一次谓词查询可能被翻译成 SQL、XML 或其他格式。

Cocoa 谓词系统的目标是支持一组实用的运算符，因此它既不是所有后端存储所支持运算符的并集，也不是它们的交集。所以，并非所有可能的谓词查询都能被所有后端存储支持，也并非所有后端存储支持的运算都能用 `NSPredicate` 和 `NSExpression` 对象表达。后端可能会降级处理某个谓词（例如把区分大小写的比较变成不区分大小写的比较），也可能在你尝试使用不受支持的运算符时抛出异常。例如：

- `matches` 运算符使用 `regex`，因此 Core Data 的 SQL 存储并不支持它——不过它在内存筛选中可以正常工作。
- Core Data 的 SQL 存储在每次查询中只支持一个对多运算；因此在发往 SQL 存储的任何谓词中，`ALL`、`ANY` 和 `IN` 这三个运算符里只能出现一个（而且该运算符只能出现一次）。
- 任意的 SQL 查询未必都能翻译成谓词。
- `ANYKEY` 运算符只能配合 Spotlight 使用。
- Spotlight 不支持关系。

以下各篇文章介绍 Cocoa 谓词的基础知识，说明如何创建和使用谓词对象，并定义谓词语法：

- [创建谓词](Creating%20Predicates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojtfvbuuqseijeegqq)介绍如何以编程方式正确地实例化谓词，以及如何从托管对象模型中取出谓词。
- [使用谓词](Using%20Predicates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojufvbuuqseijeegqq)说明如何使用谓词，并讨论一些与性能相关的问题。
- [NSPredicate 与 Spotlight 查询字符串的比较](Comparison%20of%20NSPredicate%20and%20Spotlight%20Query%20Strings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnzqfvjvomi)对比 NSPredicate 查询与 Spotlight 查询。
- [谓词格式串语法](Predicate%20Format%20String%20Syntax.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojvfvbuuqseijeegqq)介绍谓词格式串（predicate format string）的语法。
- [Cocoa 谓词的 BNF 定义](BNF%20Definition%20of%20Cocoa%20Predicates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoojwfvbuuqseijeegqq)用巴科斯-诺尔范式（Backus-Naur Form）记法给出 Cocoa 谓词的定义。

[下一页](Creating%20Predicates.md)

