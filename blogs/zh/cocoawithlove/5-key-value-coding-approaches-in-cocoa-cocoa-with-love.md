---
title: 'Cocoa 中实现键值编码的 5 种方式 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2010/01/5-key-value-coding-approaches-in-cocoa.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:d01eb4e58ffcfe37'
translated: true
---

> 原文：[5 key-value coding approaches in Cocoa | Cocoa with Love](https://www.cocoawithlove.com/2010/01/5-key-value-coding-approaches-in-cocoa.html)　·　Cocoa with Love (Matt Gallagher)

键值编码（KVC）是一种将通用操作与它可能作用的具体属性解耦的方式。它最常与 `NSKeyValueCoding` 协议联系在一起，但还有许多其他方式可以实现相同效果。本文将介绍键值编码为何重要，并展示实现这一模式的 5 种不同方法，每种方法都有自己的优势。

## 引言

`NSKeyValueCoding` 协议从 Mac OS X 10.0 起就存在于 Cocoa 中，但直到 Mac OS X 10.3，用户界面绑定展示出它的潜力后，它才真正留下深刻印记：用户界面控件可以通过配置数据而不是修改代码，连接到对象上的属性。

虽然键值编码的核心概念存在于（或可以在其中实现于）大多数编程框架中，但它在 Cocoa 中的普遍程度和渗透范围都很不寻常，尤其是和其他编译型应用框架相比。

尽管键值编码无处不在，你仍可以选择避免使用它。不过，Apple 引入它是有原因的：这是一个简单的设计模式，能为代码带来很大益处。因此，本文将讨论键值编码是什么、它如何改进代码，以及可以用哪些不同方法实现这种效果。

## 什么是键值编码？

键值编码背后的理念非常简单：不直接获取或设置对象的特定属性，而是传入一个“键”（通常是字符串），然后获取或设置与该键关联的属性。

这听起来可能很像 `NSDictionary`。

例如：

```objc
// Set a property directly...
someObject.someProperty = someValue;

// ...or set the same property using key-value coding
[someObject setValue:someValue forKey:@"someProperty"];
```

为什么要这样做？答案是，它将“为属性设置值”这一动作与涉及的具体属性解耦了。

想象一个用于编辑姓名和地址的表格：

![](https://www.cocoawithlove.com/assets/objc-era/tablescreenshot.png)

如果不使用键值编码，`NSTableViewDataSource` 中处理某一行编辑的方法可能如下：

```objc
- (void)tableView:(NSTableView *)aTableView
    setObjectValue:(NSString *)anObject
    forTableColumn:(NSTableColumn *)aTableColumn
    row:(int)rowIndex
{
    if ([[aTableColumn identifier] isEqual:@"name"])
    {
        [[records objectAtIndex:rowIndex] setName:anObject];
    }
    else if ([[aTableColumn identifier] isEqual:@"address"])
    {
        [[records objectAtIndex:rowIndex] setAddress:anObject];
    }
}
```

使用键值编码后，方法变成：

```objc
- (void)tableView:(NSTableView *)aTableView
    setObjectValue:(NSString *)anObject
    forTableColumn:(NSTableColumn *)aTableColumn
    row:(int)rowIndex
{
    [[records objectAtIndex:rowIndex] setValue:anObject forKey:[aTableColumn identifier]];
}
```

我之前谈过绑定：这种方法并没有使用用户界面绑定（那样根本不需要代码）。这里实际上只是展示了绑定可能采用的一种简化实现方式。

这种键值编码方式更好，因为它不需要针对每个属性的编辑分别处理条件。这就是键值编码的本质。

而且，随着数据集规模增大，键值编码仍然同样高效。一个有 1,000 列的表格，编辑所需的代码量仍然相同。

## KVC 方式 1：NSKeyValueCoding 协议

到目前为止我展示的所有键值编码都使用了 `NSKeyValueCoding` 协议。其实，虽然我称它为协议，但它实际上是一个“非正式协议”（即 `NSObject` 上的一个 category）。

这个 category 实现了 `setValue:forKey:` 和 `valueForKey:` 方法，你可以用 `NSString` 键来设置和获取值。

### 优点

- 自动查找 getter 和 setter 方法；如果找不到 getter 或 setter，甚至会直接获取或设置 ivar。这意味着大多数属性会自动支持 `NSKeyValueCoding`。关于查找路径的更多信息，请参阅我之前的文章 [Key Value Information post](https://www.cocoawithlove.com/2008/07/key-value-information.html)。
- 支持 key path（用于遍历多个属性）。
- 可与 `NSKeyValueObserving` 集成，以实现 Observer 设计模式。
- 提供处理未定义键的回退机制和方式。

### 缺点

- 扩展后的查找路径使其成为几种键值编码方式中速度最慢的一种（参阅我之前关于性能的文章 [Replacing Core Data Key Paths](https://www.cocoawithlove.com/2009/11/performance-tests-replacing-core-data.html)）。
- 类中必须存在与属性名匹配、且能被 `NSKeyValueCoding` 找到的方法或 ivar。
- 只支持将 `NSString` 作为属性键。

## KVC 方式 2：手动实现 NSKeyValueCoding 行为的子集

`NSKeyValueCoding` 协议会根据 selector 名称查找方法，也会根据名称查找 ivar。

这些工作你完全可以自己完成。

```objc
// Manual KVC setter method implementation
NSString *setterString = [@"set" stringByAppendingString:[someKeyString capitalizedString]];
[someObject performSelector:NSSelectorFromString(setterString) withObject:someValue];

// Manual KVC ivar setter
object_setInstanceVariable(someObject, someKeyString, someValue);
```

为什么不直接使用 `NSKeyValueCoding`，而要这样做？只有在你想避开通常会被 `NSKeyValueCoding` 找到的方法或 ivar 时，才会使用这种方式。它允许你定义自己的查找路径。

### 优点

- 比 `NSKeyValueCoding` 更能控制查找路径。
- 速度可能比 `NSKeyValueCoding` 更快。
- 即使类不继承自 `NSObject`、因而没有 `NSKeyValueCoding` 实现，也可以工作。
- 手动实现的方法可以获取和设置非对象值。

### 缺点

- 不如 `NSKeyValueCoding` 灵活。
- 在大多数情况下，它比使用 `NSKeyValueCoding` 更费工夫。

## KVC 方式 3：关联对象

Objective-C 2.0 runtime（用于 iPhone 和 64 位 Mac OS X 应用）允许你将任意对象与另一个对象关联起来。这样，runtime 中的任何对象都可以拥有一组按键设置的任意额外属性，而不需要对象本身提供 ivar 或方法支持。

```objc
objc_setAssociatedObject(someObject, someKey, someValue, OBJC_ASSOCIATION_RETAIN_NONATOMIC);
```

使用这种方式的主要原因，是你想从对象外部为它设置属性，也就是说，不需要对象支持、参与属性访问，甚至不需要知道属性访问的存在。程序的其他部分可以出于自身目的为对象设置属性。

### 优点

- 不需要对象提供任何支持（方法或 ivar）。
- 键可以是任意指针（因此在使用 `OBJC_ASSOCIATION_ASSIGN` 时，对象也可以作为键）。
- 可能是最快的 KVC 方式。

### 缺点

- 键是指针而不是对象，因此如果使用对象，它必须是指针唯一的对象（也就是说，如果用同一个字符串值的不同分配实例进行获取和设置，就无法工作）。
- 不会影响对象上的 ivar 或方法。通常这意味着，如果你希望对象本身知道发生了变化，就必须使用其他方式。

## KVC 方式 4：将 selector 作为键

键值编码主要是根据键查找属性，然后对查找到的属性执行操作。

Objective-C 的核心就有一种查找机制：方法查找。这种查找的键就是 selector。

```objc
objc_msgSend(someObject, someSetterSelector, someValue);
```

这种方式类似于手动实现 `NSKeyValueCoding` 中与方法相关的部分，但它不根据键生成 selector 字符串，再查找 selector 字符串，而是直接使用 selector 作为键。

这种方式的缺点是，获取和设置需要使用不同的 selector。

### 优点

- 在通过方法实现的方式中速度最快（这很好，因为方法可重写，因此对支持子类更加友好）。
- 可以获取和设置非对象数据（不过获取 `float`、`double` 和 `struct` 属性时，需要使用 `objc_msgSend_fpret` 和 `objc_msgSend_stret`）。

### 缺点

- 获取和设置需要使用不同的键。
- selector 不是对象，因此不能直接存入 Objective-C 数组和字典（必须使用 CoreFoundation 或 `NSValue` 包装器）。

## KVC 方式 5：自己实现

键值编码的最后一种方式是自己处理实现。如果需要最大限度的灵活性（处理不寻常的键和值），或希望从单个对象暴露不同的键值集合，就可以采用这种方式。

最简单的做法是暴露一个 getter 和 setter 方法，然后简单地从对象包含的字典中获取或设置值。

```objc
- (void)setCollectionValue:(id)value forKey:(NSString *)key
{
    [collectionDictionary setObject:value forKey:key];
}

- (id)getCollectionValueForKey:(NSString *)key
{
    return [collectionDictionary objectForKey:key];
}
```

至于值的内部存储，你可以使用 Cocoa 中的任意键值存储结构：

- `NSMutableDictionary`
- `NSMapTable`
- `CFMutableDictionaryRef`
- `self` 或其他对象上的关联对象（见上文）

也可以使用自己的存储方案。

### 优点

- 单个对象可以暴露多个、相互独立的集合。
- 可以获取和设置底层集合支持的任何数据类型。
- 对回退机制和特殊情况的处理最灵活。

### 缺点

- 必须由目标类实现（不能用于任意对象）。
- 无法与 `NSKeyValueObserving` 或其他任何 `NSKeyValueCoding` 概念互操作。

## 结论

键值编码并非强制要求，当然可以完全不使用它来实现整个项目。不过，它是减少重复代码、提高类的可复用性的优秀代码模式之一，因为它能将操作与属性及数据解耦。

如你所见，程序中可以使用多种不同的键值编码方式。`NSKeyValueCoding` 可能是 Cocoa 中最灵活、最可复用且支持最完善的方式，因此除非你需要其他方式的某项优势，或希望将问题的解决方案限制在较小范围内，否则它可能是最佳选择。
