---
title: 如何在 Swift 中更优雅地处理 Core Data 非可选属性
source: Jesse Squires
source_key: jessesquires
source_url: 'https://www.jessesquires.com/blog/2022/01/26/core-data-optionals/'
original_language: en
published: 2022-01-26
status: active
license: © 2014–2026 Jesse Squires → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:6c921d92fbed1334'
translated: true
---

> 原文：[How to more gracefully handle non-optional Core Data properties in Swift](https://www.jessesquires.com/blog/2022/01/26/core-data-optionals/)　·　Jesse Squires

Tom Harrington 在[一篇近期文章](https://atomicbird.com/blog/clash-of-the-optionals/)中探讨了 Core Data 中可选值与非可选值在框架与 Swift 交互时产生的问题。这是一篇很好的概述，你应该[读一读](https://atomicbird.com/blog/clash-of-the-optionals/)。文章中分享了一些改善局面的变通方法，但我想分享一种更健壮的解法。

总结一下那篇文章：Swift 与 Core Data 对可选值（optional）和非可选值（non-optional）的区分存在差异。在 Swift 中，_编译器_ 强制要求值的存在或缺失，这使得你能在_编译时保证_某个值是否安全可用。而 Core Data 中，_框架_ 负责这项强制性校验，但只能_在运行时_完成。两者语境下，“optional”都意味着你可能没有值，需要对应处理这种缺失。差异出现在“_非_ optional”值上。在 Swift 中，非可选属性在初始化之后永远不会是 `nil`。如果是 `var`，它的值可能改变，但不会变成 `nil`。Swift 编译器在编译时就强制这条规则。而 Core Data 中，非可选属性在保存变更到模型时不能为 `nil`，除此以外对初始化没有强制要求。Core Data 框架通过运行时的校验规则来执行这条限制，即 [`validateForInsert()`](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506683-validateforinsert) 和 [`validateForUpdate()`](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506998-validateforupdate)。如果校验失败，你会遇到错误——甚至更糟，崩溃。

即使你在 Core Data 模型中将属性标记为非可选，Xcode 生成的 Swift `NSManagedObject` 子类中仍然是_可选_属性。你可以把它们改成非可选，一切看起来仍然能工作。你可以省略一个合适的 Swift 指定初始化器，也可以调用默认的 `init()` 而不_实际_初始化任何属性。正如 [Tom 指出](https://atomicbird.com/blog/clash-of-the-optionals/)的，这是因为特殊的 `@NSManaged` 特性告诉编译器这些属性的值会在运行时由 Core Data 提供，因此 Swift 严格的初始化规则不再适用。只有你，作为开发者，才能确保一切正确初始化——否则就会崩溃。

#### * * *

我们不想放弃，索性把所有 Core Data 属性都变成可选。那会给代码库的其他部分带来巨大负担。问题在于：我们如何才能安全地（或者说尽可能安全地）为 `NSManagedObject` 子类实现非可选属性？Swift 编译器在这方面无法帮助我们强制校验，所以我们必须确保在初始化托管对象（managed object）时，_始终_为非可选属性赋值。

#### 在模型编辑器中提供默认值？

在[模型编辑器](https://developer.apple.com/documentation/coredata/creating_a_core_data_model)中，你可以为非可选属性定义默认值。这对简单情况有效，但很多值往往_没有_好的默认值，尤其是如果我们是在向用户索取数据。即便像时间戳这样的属性，模型编辑器也不够。你可以提供一个具体的默认 `Date` 值，但如果你的对象有 `dateCreated` 属性，你实际上想把它初始化为 [`Date.now`](https://developer.apple.com/documentation/foundation/date/3766590-now)，这在编辑器里是做不到的。Tom [建议](https://atomicbird.com/blog/clash-of-the-optionals/)我们实现 [`awakeFromInsert()`](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506548-awakefrominsert) 来应对这种情况。这个方法可行，但我们还能做得更好。

### 正确处理 Core Data 非可选属性

如果无法为非可选属性提供默认值，或者模型编辑器无法满足我们的需求，我们可以通过以下一系列步骤来弥补 Core Data 在 Swift 中的不足，让模型尽可能健壮。

#### 1. 提供唯一的指定初始化器

假设我们有一个 `Item` 类，其中_所有_属性都是非可选的。部分有默认值，但其他需要用户输入。我们可以这样定义类：

```
public final class Item: NSManagedObject {
    @NSManaged public private(set) var itemId: String
    @NSManaged public private(set) var dateCreated: Date
    @NSManaged public var name: String
    @NSManaged public var unitCost: NSDecimalNumber
    @NSManaged public var unitPrice: NSDecimalNumber
    @NSManaged public var stockCount: Int
}
```

注意：

1. Swift 编译器不会产生任何初始化错误。如果去掉 `@NSManaged`，它会报错。
2. 使用 `@NSManaged` 要求属性必须是 `var`。然而，`itemId` 和 `dateCreated` 一旦我们初始化并保存了 `Item` 之后就不应再改变。如果能把它们标记为 `let` 就好了，但不行。作为替代，我们可以把 setter 标记为 `private`，在 App 代码的其他部分强制这一点。
3. Swift 编译器会阻止我们将这些属性设为 `nil`——这项强制校验仍然有效。

现在我们可以编写一个指定初始化器（designated initializer），在可能的地方提供默认值。

```
public final class Item: NSManagedObject {
    // 上面定义的属性

    public init(context: NSManagedObjectContext,
                itemId: String = UUID().uuidString,
                dateCreated: Date = Date.now,
                name: String,
                unitCost: NSDecimalNumber,
                unitPrice: NSDecimalNumber,
                stockCount: Int = 0) {
        let entity = NSEntityDescription.entity(forEntityName: "Item", in: context)!
        super.init(entity: entity, insertInto: context)
        self.itemId = itemId
        self.dateCreated = dateCreated
        self.name = name
        self.unitCost = unitCost
        self.unitPrice = unitPrice
        self.stockCount = stockCount
    }

    @objc
    override private init(entity: NSEntityDescription, insertInto context: NSManagedObjectContext?) {
        super.init(entity: entity, insertInto: context)
    }
}
```

注意：

1. 我们必须调用 `super` 的 [`init(entity:insertInto:)`](https://developer.apple.com/documentation/coredata/nsmanagedobject/1506357-init) 实现，这是 `NSManagedObject` 的指定初始化器。
2. 即使不直接使用，我们也必须重写 `init(entity:insertInto:)` 以满足 Core Data 的预期，否则框架会在运行时崩溃，错误信息是：`Fatal error: Use of unimplemented initializer 'init(entity:insertInto:)' for class 'Item'`。这是因为 Core Data 在底层做了大量 Objective-C 运行时操作。我们将其标记为 `private` 以防止调用方使用。
3. 我们可以在这里省略初始化所有属性，编译器不会报错——再次感谢 `@NSManaged`。但我们会在运行时崩溃。（下面会解决这个问题。）

#### 2. 阻止调用无效的初始化器

目前为止，我们差不多完成了。下一个问题是，我们_仍然_可以在代码其他地方调用两个无效的初始化器。

1. 从 `NSObject` 继承的默认 `init()`
2. 从 `NSManagedObject` 继承的便捷初始化器 [`init(context:)`](https://developer.apple.com/documentation/coredata/nsmanagedobject/1640602-init)

同样，因为 `@NSManaged` 的存在，Swift 的初始化规则在这里不适用。单纯记住或告诉团队只使用某个特定的初始化器很容易出错。幸运的是，我们可以通过将它们标记为不可用（unavailable）来阻止调用。这不仅会在使用时产生编译器错误，还会阻止它们出现在 Xcode 的自动补全中。

```
public final class Item: NSManagedObject {
    // 属性和指定初始化器在上面

    @available(*, unavailable)
    public init() {
        fatalError("\(#function) not implemented")
    }

    @available(*, unavailable)
    public convenience init(context: NSManagedObjectContext) {
        fatalError("\(#function) not implemented")
    }
}
```

现在如果你尝试写 `Item()` 或 `Item(context: moc)`，编译器会产生“该初始化器不可用”的错误。

#### 3. 编写单元测试以帮助防止将来的错误

最后一步是编写单元测试来进一步验证我们所有的假设。希望你已经有让模型通过 Core Data 往返的测试。如果没有，现在就去写！

托管对象测试应该：

1. 创建模型并手动验证所有属性。
2. 保存模型并验证保存成功。
3. 如果 `NSManagedObjectContext.save()` 抛出错误，测试应该失败。
4. 保存后获取模型并验证其属性。
5. 获取并修改模型的属性，保存，然后再次验证。

对 Core Data 中每个模型都提供充分的测试覆盖，我们就能确信可以捕获到日后修改模型时可能产生的大多数错误。例如，如果在 `init` 中忘记初始化某个属性（如上所述），保存时校验会失败，测试也因此失败。或者，假设我们添加了一个新的非可选属性，并在 Core Data 模型编辑器中正确地标记为非可选，但忘记把它加入指定初始化器，代码可以编译通过，但——同样——保存时校验会失败，测试也会失败。

现在我们已经有了大部分常规保护措施——不过，还有一些注意事项。

#### 4. 注意事项与警告

如前所述，为了强制执行通常由 Swift 帮我们完成的规则，这里有很多手动工作。在 Xcode 编辑器和代码中修改模型时，需要确保它们的属性和可选性一致，正确更新指定初始化器，并更新测试。这需要高度谨慎，在大型团队中尤其困难。在这种情况下，完整的单元测试覆盖绝对必要，而这同样需要高度的责任心去维护。

也许这并不明显，但所有这些意味着你不应该让 Xcode 自动生成托管对象子类的定义。自从 Xcode 开始把这些定义放在 `/DerivedData/` 而不是项目的根目录下，这就已经成问题。自己编写这些类很容易，不需要 Xcode（错误地）替你完成。额外的好处是，你可以将这些文件纳入版本控制（version control），而不是依赖 Xcode 的“魔法”。

另外要注意 Objective-C 与 Swift 之间的桥接问题。在 Objective-C 中，你可以使用 `NS_UNAVAILABLE` 宏来将初始化器标记为不可用，就像我们在 Swift 中做的那样。此外，你可以利用 Objective-C 的[空值注解](https://developer.apple.com/documentation/swift/objective-c_and_c_code_customization/designating_nullability_in_objective-c_apis)来改善与 Swift 的互操作。

最后，有可能会遇到与[故障（faulting）](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/FaultingandUniquing.html)相关的问题。根据我的经验，这主要是理论上的，在实践中不会构成问题。但仍然是需要注意的事项。

[Core Data 编程指南](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/FaultingandUniquing.html)：

> 托管对象通常表示持久化存储（persistent store）中持有的数据。在某些情况下，托管对象可能是一个故障（fault）——即属性值尚未从外部数据存储加载的对象。故障机制减少了你 App 消耗的内存。故障是一个占位对象，代表一个尚未完全实现的托管对象，或者一个表示关系的集合对象。
> 
> […]
> 
> 当故障被触发时，如果数据在其缓存中可用，Core Data 不会回到存储。缓存命中时，将故障转换为已实现的托管对象非常快——基本上与正常实例化托管对象相同。如果数据在缓存中不可用，Core Data 会自动对故障对象执行获取请求（fetch）；这会引发到持久化存储的一次往返以获取数据，然后数据再次缓存在内存中。
> 
> 一个对象是否为故障，仅仅意味着某个给定的托管对象是否已填充了所有持久化属性并可供使用。如果你需要判断一个对象是否为故障，请调用其 `isFault` 方法，而不触发该故障（不访问任何关系或属性）。

我_认为_这意味着有可能取到一些对象，其非可选属性在被获取时_没有_初始化，当从 Swift 访问这些属性时可能导致崩溃。`NSFetchRequest` 有一个属性可以控制这一点，即 [`includesPropertyValues`](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506387-includespropertyvalues)，其默认值为 `true`。[文档](https://developer.apple.com/documentation/coredata/nsfetchrequest/1506387-includespropertyvalues)解释：

> 一个布尔值，指示在执行获取请求时，是否从持久化存储中获取属性数据。[…]
> 
> 你可以将 `includesPropertyValues` 设置为 `false`，以避免创建表示属性值的对象，从而减少内存开销。然而，通常只应在确定不会用到实际属性数据时才这样做。[…]
> 
> 在正常获取请求期间（`includesPropertyValues` 为 `true`），Core Data 会获取匹配记录的 Object ID 和属性数据，将信息填入行缓存（row cache），并返回作为故障的托管对象（参见 `returnsObjectsAsFaults`）。虽然这些故障是托管对象，但它们的属性数据全部驻留在行缓存中，直到故障被触发。触发故障时，Core Data 从行缓存中检索数据——无需再回数据库。
> 
> 如果 `includesPropertyValues` 为 `false`，Core Data 只获取匹配记录的 Object ID 信息——它不会填充行缓存。

在默认行为下，Core Data 会获取模型中的所有属性。对于一对一关系，另一个模型的属性会被缓存，并且当访问该托管对象时，故障会立即触发。对于用集合（collection）表示的一对多关系，问题不大，因为空集合不会带来崩溃风险。换句话说，你在故障方面_应该_没有问题，但应该仔细检查你的获取请求。再次强调，我在实践中没有遇到过这方面的问题，而且单元测试也应该有助于发现和预防问题。

希望这对你改进 Core Data 模型有所帮助！样板代码虽然令人遗憾，但肯定比什么都没有强。
