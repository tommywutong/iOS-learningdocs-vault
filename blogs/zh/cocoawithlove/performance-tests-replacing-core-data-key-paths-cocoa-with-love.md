---
title: '性能测试：替换 Core Data 键路径 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2009/11/performance-tests-replacing-core-data.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:2bd59db205c18e8e'
translated: true
---

> 原文：[Performance tests: Replacing Core Data Key Paths | Cocoa with Love](https://www.cocoawithlove.com/2009/11/performance-tests-replacing-core-data.html)　·　Cocoa with Love (Matt Gallagher)

在 Mac OS X 10.5 中，Core Data 从以 `valueForKey:` 作为访问 Core Data 属性（attribute）和关系（relationship）的推荐方式，切换到了自动生成的存取方法（accessor method）。这个新方法在获取值时速度更快，但缺乏 `NSKeyValueCoding` 那种能够通过单条语句合并「对多」（to‑many）关系中每个对象提取的值的能力。

在这篇文章中，我将探讨用一种直接调用存取方法的方式来替换 `NSKeyValueCoding` 提供的 `NSSet` 遍历和 `NSSet` 合并能力，看看能否将自动生成存取方法带来的性能提升延伸到涉及 `NSSet` 遍历的场景中。

## 访问 NSManagedObject 的属性和关系

在本文中，我将使用以下模型来测试 Core Data 程序的性能：

![](https://www.cocoawithlove.com/assets/objc-era/modelentities.png)

如果你不熟悉 Core Data 实体图，这里的关键点在于：每个 `Company` 可以有多个 `Project`，每个 `Project` 可以有多个 `Employee`。

在这个模型下，如果我有一个指向某个 `Company` 对象的指针 `aCompany`，获取公司名很简单：

```objc
NSString *companyName = aCompany.name;
```

这里访问的 `name` 属性是通过 `NSManagedObject` 为我们提供的自动生成存取方法实现的。

在 Mac OS X 10.5 之前，访问 Core Data 值的唯一方式是使用键值编码（key value coding）：

```objc
NSString *companyName = [aCompany valueForKey:@"name"];
```

为什么弃用键值编码？主要原因在于性能（尽管语法改进和类型安全也有帮助）。使用键值编码获取名称 100 万次需要 0.284016 秒，而使用自动生成的属性存取方法则降至 0.109017 秒——速度快了 2.6 倍。

## Set 遍历

但键值编码（「旧」方法）相对于自动生成的方法仍有一个重要优势：在遍历「对多」关系返回的 set 时，它更快。

例如，如果我想获取 `aCompany` 使用的所有 `Project` 名称的完整 set，使用键值编码（Key Value Coding）很简单：

```objc
NSSet *projectNames = [aCompany valueForKeyPath:@"projects.name"];
```

这之所以有效，是因为 `NSSet` 对 `NSKeyValueCoding` 协议（protocol）的实现会自动向自身内部遍历，以获取它包含的每个 `Project` 对象的名称。

使用存取方法，简单的等价实现是：

```objc
NSMutableSet *result = [NSMutableSet set];
for (Project *project in aCompany.projects)
{
    NSString *name = project.name;
    if (value)
    {
        [result addObject:value];
    }
}
```

这不仅比键值编码方法代码量更多，而且实际上 _更慢_。对于 10000 个 `Company` 对象，每个有 100 个 `Project` 对象，键值编码方法耗时 0.25692 秒，而使用自动存取器的简单方法耗时 0.52873 秒。

新的改进方法从快 2.6 倍变成了慢 2 倍。

## 修复速度问题

### 旧方法反而更快了

在我说明为什么「新」方法更慢之前，首先需要注意的一点是，键值编码方法（「旧」方法）在使用 set 遍历时实际上 _更快_。尽管涉及从 `Company` 遍历到 `Project` 并对名称进行唯一化（uniquing）以形成单个 `NSSet` 的额外工作，键值编码仅耗时 0.25692 秒来获取 100 万个 `Project` 名称，而此前获取 100 万个 `Company` 名称耗时 0.284016 秒。

这并不是一个错误；尽管工作量更大，键值编码在内部（作为键路径的一部分）迭代 set 时，性能反而比外部迭代（就像我迭代 100 万个 `Company` 对象时那样）更好。

尽管有这些改进，我们使用自动生成存取方法的方法仍然应该能够击败键值编码，但优势显然会比 `aCompany.name` 迭代时小得多。

### 修复新方法

基本性能分析很快揭示了问题与实际的属性存取器关系不大。速度慢的主要原因是 `addObject:`。

在查看分析器堆栈中的私有方法后，很明显原因是重分配。每当 `NSMutableSet` 需要扩容时，它都会重新分配其内部存储，导致性能不佳。

我们可以基于最坏情况大小（所有 `Project` 名称唯一）预分配整个 set。代码变成：

```objc
NSSet *projects = aCompany.projects;
NSMutableSet *result = [NSMutableSet setWithCapacity:[projects count]];
for (Project *project in projects)
{
    NSString *name = project.name;
    if (value)
    {
        [result addObject:value];
    }
}
```

成功！这个版本现在运行耗时 0.19104 秒（从 0.52873 秒下降），现在比键值编码方法快 25%。

我们不再快 2.6 倍，但 `NSSet` 内部对键值编码的实现在这里比我们有优势：由于它可以内部访问存储，它能比我们更好地优化对「对多」关系的迭代以及新 set 的构建。

## 分类实现

为了将来重用上述方法，我们可以在 `NSSet` 上实现一个分类（category）。

将包含两个方法：

- `objectValuesForProperty:`
- `coalescedValuesForProperty:`

第一个方法将实现前面提到的示例（即 `NSSet` 包含基本对象的情况）。

第二个方法将复制键值编码操作符 `@distinctUnionOfSets` 的行为（用于处理 `NSSet` 中包含另一个 `NSSet`，并且需要合并子 set 内部对象的情况）。

第二个方法的一个例子是，获取某个 `Company` 的所有 `Employee` 对象。在键值编码中，我们会写：

```objc
NSSet *allEmployees = [aCompany valueForKeyPath:@"projects.@distinctUnionOfSets.employees"];
```

使用 `coalescedValuesForProperty:` 方法，我们可以写：

```objc
NSSet *allEmployees = [aCompany.projects coalescedValuesForProperty:@selector(employees)];
```

实现如下：

```objc
#import &lt;objc/message.h&gt;

@implementation NSSet (PropertyCoalescing)

- (NSSet *)objectValuesForProperty:(SEL)propertySelector
{
    NSMutableSet *result = [NSMutableSet setWithCapacity:[self count]];
    for (id object in self)
    {
        id value = objc_msgSend(object, propertySelector);
        if (value)
        {
            [result addObject:value];
        }
    }
    return result;
}

- (NSSet *)coalescedValuesForProperty:(SEL)propertySelector
{
    NSInteger count = 0;
    for (id object in self)
    {
        count += [objc_msgSend(object, propertySelector) count];
    }
    NSMutableSet *result = [NSMutableSet setWithCapacity:count];
    for (id object in self)
    {
        id value = objc_msgSend(object, propertySelector);
        if (value)
        {
            [result unionSet:value];
        }
    }
    return result;
}

@end
```

使用 `coalescedValuesForProperty:` 方法时，我们遍历整个 set 两次以获取大小，但这仍然是最快的选择——实际上，该方法比键值编码方法快约 35%，而 `objectValuesForProperty:` 的改进是 25%。

## 结论

> 应要求，以下是测试中使用的代码：[PropertyAccessors.zip](https://www.cocoawithlove.com/assets/objc-era/PropertyAccessors.zip)（32kB）。这是为了配合这篇文章仓促拼凑的，所以不一定写得好，但如果你感兴趣，可以看看。

我编写这段代码并进行这些性能测试，是因为我有大量代码使用键值编码遍历「对多」关系。我担心既然 Core Data 出于性能原因推荐使用自动生成的存取方法，那么在这些情况下我使用键值编码会比应有的速度慢得多。

结果是，虽然确实可以在 Core Data 中遍历 set 时改进键值编码的性能，但改进幅度只有 25-35%，而非像在单个属性访问中，用存取方法替换键值编码那样带来的 260% 提升。键值编码在处理 set 时相当高效——确实比访问单个属性时高效得多。

当然，本文介绍的方法所提供的 35% 速度提升，在性能关键区域无疑会很有用。

关于实现本身：永远不要低估将内存重分配保持在最低限度对性能的影响。从一个零容量的 `NSSet` 开始，并使用 `addObject:` 不断扩容，其速度比一次性分配慢 3 倍。

分配的 `NSMutableSet` 容量足够容纳所有对象，但如果对象并非全部唯一，则会比实际需要更大。如果这种额外的内存使用是个问题，你可以在生成 set 后复制一份。副本的大小将严格符合需要，然后你可以释放原始 set。缺点是这个复制过程会增加大约 10-15% 的时间消耗。
