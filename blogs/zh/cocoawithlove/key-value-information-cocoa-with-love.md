---
title: '键值信息 | Cocoa with Love'
source: Cocoa with Love (Matt Gallagher)
source_key: cocoawithlove
source_url: 'https://www.cocoawithlove.com/2008/07/key-value-information.html'
original_language: en
published: ''
status: frozen
license: All rights reserved（页脚明示）→ 严格私有
archived_at: 2026-07-27
content_hash: 'sha256:899ffe3f83498fb8'
translated: true
---

> 原文：[Key Value Information | Cocoa with Love](https://www.cocoawithlove.com/2008/07/key-value-information.html)　·　Cocoa with Love (Matt Gallagher)

NSKeyValueCoding 在 Cocoa 中随处可见（Bindings、Core Data、集合等），但尽管它是一种连接对象的动态方式，却不提供关于自身运行方式的动态信息：对象支持哪些键，以及用于读写值的自定义方法。本文将介绍 NSKeyValueCoding 的工作方式，并展示如何获取任意类或对象所支持的键及其方法。

## “Cocoa 编程基础”往期内容……

键值编码是一种在对象上获取和设置数据的方式。键值编码意味着：使用对象上的通用方法，请它针对某个特定名称（即“键”）获取或设置值。通过对象上的通用方法，键值编码将对象如何获取或设置“键”对应值的具体机制抽象出来。

键值编码关注的是连接逻辑；它通常不负责实际读取或修改值的工作（这由普通的 getter 和 setter 方法完成），而是定义以抽象方式调用 getter 和 setter 的规则。

它至少在以下 5 种场景中特别有用：

- 将对象呈现为简单的数据存储，即使底层实现并不简单（例如 NSManagedObject）。
- 为处理数量可变的命名值提供简单而灵活的接口（例如 NSDictionary）。
- 无需知道所处理对象的具体类型，例如在用户界面绑定中通用地连接对象。
- 通过“键路径”轻松串联访问操作，并提供处理以这种方式访问的数据集合的运算符。
- 对数据的通用访问使其他服务成为可能，例如 NSKeyValueObserving。

它主要通过以下两个基本方法完成这些工作：

```objc
- (id)valueForKey:(NSString *)key
- (void)setValue:(id)value forKey:(NSString *)key
```

这两个方法定义在 [NSKeyValueCoding](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Protocols/NSKeyValueCoding_Protocol/Reference/Reference.html) 非正式协议中（所有 NSObject 都会隐式实现该协议）。

## 它是如何工作的？

一旦开始追问某件事的工作方式，你就会立即进入灰色地带。[文档](http://developer.apple.com/documentation/Cocoa/Reference/Foundation/Protocols/NSKeyValueCoding_Protocol/Reference/Reference.html)至少告诉我们以下内容：

- 默认实现会调用 `-(id)<key>` 或 `-(void)set<key>:` 方法（如果存在）来完成工作。如果找不到这些方法，还会尝试其他几个方法名。
- 如果没有找到方法，会自动访问名称与键相同的实例变量（除非类明确禁用了此功能）。
- 如果连匹配的实例变量也找不到，就会调用 `-(id)valueForUndefinedKey:(NSString *)key` 方法；该方法默认抛出 NSUndefinedKeyException。

提炼这些信息后，在大多数情况下可以假定：只要某个类支持 `-(id)<key>` 和 `-(void)set<key>:` 方法，或者拥有名为“key”的属性，键值编码就能对该类上的任意“键”工作。有时，重写 `valueForUndefinedKey:` 也会支持其他键，但这完全取决于具体实现。大多数其他键与对象的组合都会抛出 NSUndefinedKeyException。

## 确定性的答案

键值编码的核心是动态连接、简化和抽象，因此你最终可能会遇到这样的情况：想从对象获取一个值，但需要在运行时检查它是否支持该值对应的键。

遗憾的是，键查找有许多回退选项，而且还可能存在可重写的 `valueForUndefinedKey:` 等方法，因此没有某个特定属性可以直接告诉你一个键是否受支持。

从最一般的意义上说，判断对象是否支持给定键的唯一方法是：

```objc
BOOL supportsSomeKey = YES;
@try
{
    [object valueForKey:somekey];
}
@catch (NSException *e)
{
    if ([[e name] isEqualTo:NSUndefinedKeyException])
    {
        supportsSomeKey = NO;
    }
}
```

如果抛出 NSUndefinedKeyException，就说明它不接受这个键。

## 更详细但不那么确定的答案

如果你认为故意触发异常是对编程的犯罪，或者想了解某个键的值是如何访问的，那么可能需要采用不同的方法。

根据具体情况，你可以执行 NSKeyValueCoding 自身可能执行的查找：也就是根据“键”名称构造不同的访问器方法名，将其转换为 SEL，然后询问类或对象是否处理这个 selector。

这正是我最近在一段实验代码中采用的方法。我的代码使用 Core Data 的 NSManagedObject，想检查通用 NSManagedObject，看看我是否针对特定键编写了自定义访问器方法（区别于自动生成的访问器方法）。我使用了下面的方法：

```objc
+ (SEL)getterSelectorForKey:(NSString *)key
{
    NSString *capitalizedKey =
        [[[key substringToIndex:1] uppercaseString]
            stringByAppendingString:[key substringFromIndex:1]];

    NSString *getString = [@"get" stringByAppendingString:capitalizedKey];
    SEL getSelector = NSSelectorFromString(getString);
    if ([self instancesRespondToSelector:getSelector])
    {
        return getSelector;
    }

    SEL plainSelector = NSSelectorFromString(key);
    if ([self instancesRespondToSelector:plainSelector])
    {
        return plainSelector;
    }

    NSString *isString = [@"is" stringByAppendingString:capitalizedKey];
    SEL isSelector = NSSelectorFromString(isString);
    if ([self instancesRespondToSelector:isSelector])
    {
        return isSelector;
    }

    return nil;
}
```

将它放在 NSManagedObject 分类中，就可以查找指定键的任意自定义访问器；该方法只需遵循文档中描述的查找路径，在访问器存在时找到它。

由于它是在类上调用的，上述方法能够区分自定义访问器和 Core Data 自动生成的访问器。Core Data 自动生成的访问器只存在于对象实例上（类的方法列表中没有它们），因此上述方法只会返回我要查找的自定义编译方法。

你也可以用类似的方法获取键值编码中使用的其他类型方法，例如：

```objc
+ (SEL)setterSelectorForKey:(NSString *)key;
+ (SEL)addObjectSelectorForKey:(NSString *)key;
+ (SEL)removeObjectSelectorForKey:(NSString *)key;
+ (SEL)countOfSelectorForKey:(NSString *)key;
+ (SEL)objectInAtIndexForKey:(NSString *)key;
```

同样，如果你想了解可能直接访问实例变量的键值编码，可以使用 class_getClassVariable 获取名称与键相同的实例变量。
