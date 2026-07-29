---
title: KVC 集合操作符
source: NSHipster (Mattt)
source_key: nshipster
source_url: 'https://nshipster.com/kvc-collection-operators/'
original_language: en
published: 2012-12-03
status: active
license: CC BY-NC（页脚明示）→ 可非商业再分发，须署名
archived_at: 2026-07-27
content_hash: 'sha256:e3ce2aa5da9d3c9c'
translated: true
---

> 原文：[KVC Collection Operators](https://nshipster.com/kvc-collection-operators/)　·　NSHipster (Mattt)

# [KVC 集合操作符](https://nshipster.com/kvc-collection-operators/)

作者：[Mattt](https://nshipster.com/authors/mattt/)　　2012 年 12 月 3 日

Ruby 开发者们嘲笑 Objective-C 臃肿的语法。

尽管我们在夏天凭借[简洁的新对象字面量](https://nshipster.com/at-compiler-directives/)减轻了一些负担，但那些红发恶霸仍然用他们的 `map` 单行代码和花哨的 [`Symbol#to_proc`](http://pragdave.me/blog/2005/11/04/symboltoproc/) 来嘲弄我们。

说实话，一门语言有多优雅（或巧妙），很大程度上取决于它如何避免循环。`for`、`while`；甚至[快速枚举表达式](https://nshipster.com/enumerators/)都令人烦恼。无论你如何粉饰，循环始终是一段代码，而它做的事情用自然语言描述起来要简单得多。

“获取这个数组中所有员工的平均薪资”，而不是……

```
double totalSalary = 0.0;
for (Employee *employee in employees) {
  totalSalary += [employee.salary doubleValue];
}
double averageSalary = totalSalary / [employees count];
```

哎。

幸运的是，[键值编码（Key-Value Coding）](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueCoding/Articles/KeyValueCoding.html)为我们提供了一种更简洁——几乎像 Ruby 一样——的方式来实现这一点：

```
[employees valueForKeyPath:@"@avg.salary"];
```

[KVC 集合操作符](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/KeyValueCoding/Articles/CollectionOperators.html)允许使用 `valueForKeyPath:` 中的键路径（key path）表示法对集合执行操作。只要在键路径中看到 `@`，它就表示一个特定的聚合函数，其结果可以返回或链接，就像任何其他键路径一样。

集合操作符根据它们返回的值类型分为以下三类：

- **简单集合操作符**：根据操作符的不同，返回字符串、数字或日期。
- **对象操作符**：返回一个数组。
- **数组与集合操作符**：根据操作符的不同，返回一个数组或集合。

理解这些操作符工作原理的最佳方式是看它们的实际应用。考虑一个 `Product` 类，以及一个包含以下数据的 `products` 数组：

```
@interface Product : NSObject
@property NSString *name;
@property double price;
@property NSDate *launchedOn;
@end
```

> 键值编码会自动将标量值装箱和拆箱为 `NSNumber` 或 `NSValue`，以确保一切正常工作。

| 名称 | 价格 | 发布日期 |
|---|---|---|
| iPhone 5 | $199 | 2012 年 9 月 21 日 |
| iPad Mini | $329 | 2012 年 11 月 2 日 |
| MacBook Pro | $1699 | 2012 年 6 月 11 日 |
| iMac | $1299 | 2012 年 11 月 2 日 |

### 简单集合操作符

- `@count`：以 `NSNumber` 形式返回集合中的对象数量。
- `@sum`：将集合中的每个对象转换为 `double`，计算总和，并将总和以 `NSNumber` 形式返回。
- `@avg`：获取集合中每个对象的 `double` 值，并将平均值以 `NSNumber` 形式返回。
- `@max`：使用 `compare:` 确定最大值。对象必须支持相互比较才能正常工作。
- `@min`：与 `@max` 相同，但返回集合中的最小值。

_示例_：

```
[products valueForKeyPath:@"@count"]; // 4
[products valueForKeyPath:@"@sum.price"]; // 3526.00
[products valueForKeyPath:@"@avg.price"]; // 881.50
[products valueForKeyPath:@"@max.price"]; // 1699.00
[products valueForKeyPath:@"@min.launchedOn"]; // June 11, 2012
```

### 对象操作符

假设我们有一个 `inventory` 数组，代表我们当地 Apple Store 的当前库存（iPad Mini 库存不足，而新款 iMac 尚未上架，因此没有库存）：

```
NSArray *inventory = @[iPhone5, iPhone5, iPhone5, iPadMini, macBookPro, macBookPro];
```

- `@unionOfObjects` / `@distinctUnionOfObjects`：返回一个数组，包含操作符右侧键路径中指定属性的对象。`@distinctUnionOfObjects` 会去除重复项，而 `@unionOfObjects` 则不会。

_示例_：

```
[inventory valueForKeyPath:@"@unionOfObjects.name"]; // "iPhone 5", "iPhone 5", "iPhone 5", "iPad Mini", "MacBook Pro", "MacBook Pro"
[inventory valueForKeyPath:@"@distinctUnionOfObjects.name"]; // "iPhone 5", "iPad Mini", "MacBook Pro"
```

### 数组与集合操作符

数组与集合操作符类似于对象操作符，但它们作用于 `NSArray` 和 `NSSet` 的集合。

例如，如果我们想比较多个门店的库存，比如 `appleStoreInventory`（与上例相同）和 `verizonStoreInventory`（售卖 iPhone 5 和 iPad Mini，且两者均有库存），这将非常有用。

- `@distinctUnionOfArrays` / `@unionOfArrays`：返回一个数组，包含集合中每个数组合并后的值，具体由操作符右侧的键路径指定。如你所料，`distinct` 版本会去除重复值。
- `@distinctUnionOfSets`：类似于 `@distinctUnionOfArrays`，但它期望一个包含 `NSSet` 对象的 `NSSet`，并返回一个 `NSSet`。由于集合本身不能包含重复值，因此只有 `distinct` 操作符。

_示例_：

```
[@[appleStoreInventory, verizonStoreInventory] valueForKeyPath:@"@distinctUnionOfArrays.name"]; // "iPhone 5", "iPad Mini", "MacBook Pro"
```

---

## 这可能是个糟糕的主意

奇怪的是，[Apple 关于 KVC 集合操作符的文档](https://developer.apple.com/library/ios/documentation/Cocoa/Conceptual/KeyValueCoding/Articles/CollectionOperators.html)特意强调了以下几点：

> **注意**：目前无法定义你自己的集合操作符。

这一点说清楚是有道理的，因为大多数人在第一次看到集合操作符时都会想到这个。

然而，事实证明，这实际上是 _可以_ 实现的，只需借助我们的朋友 `objc/runtime` 一点帮助。

[Guy English](https://twitter.com/gte) 有一篇[相当精彩的博文](http://kickingbear.com/blog/archives/9)，他在其中对 `valueForKeyPath:` 进行了[方法调配（swizzle）](https://gist.github.com/4196641#file_kb_collection_extensions.m)，以解析一个自定义的 [DSL](https://en.wikipedia.org/wiki/Domain-specific_language)，从而将现有功能扩展到有趣的效果：

```
NSArray *names = [allEmployees valueForKeyPath: @"[collect].{daysOff<10}.name"];
```

这段代码将获取休假少于 10 天的所有员工的名字（毫无疑问，是为了提醒他们休假！）。

或者，再极端一点：

```
NSArray *albumCovers = [records valueForKeyPath:@"[collect].{artist like 'Bon Iver'}.<NSUnarchiveFromDataTransformerName>.albumCoverImageData"];
```

Ruby 爱好者们，羡慕吧。这个单行代码过滤了一个唱片集，找出艺术家名字匹配 "Bon Iver" 的唱片，并从匹配唱片的专辑封面图像数据中初始化一个 `NSImage`。

这是个好主意吗？可能不是。（`NSPredicate` 很棒，而且把复杂的逻辑拆分开来是被低估的做法）

这非常酷吗？当然！这个巧妙的例子展示了未来 Objective-C DSL 和元编程的一个可能方向。

---

KVC 集合操作符是任何想要节省几行代码并同时看起来很酷的人必须掌握的知识。

虽然像 Ruby 这样的脚本语言在其单行代码能力上拥有显著更多的灵活性，但也许我们应该花点时间赞赏 Objective-C 和集合操作符中所蕴含的克制。毕竟，Ruby 慢得要命，对吧？\</troll\>
