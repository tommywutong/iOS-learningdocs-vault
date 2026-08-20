---
title: 键值观察编程指南
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVOCompliance.html
archived_at: '2026-07-15T07:16:18.106547Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值观察编程指南](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)


[下一页](Registering%20Dependent%20Keys.md)[上一页](Registering%20for%20Key-Value%20Observing.md)

# 符合 KVO 规范

要使一个类被视为对某个特定属性符合 KVO 规范，必须确保以下几点：

- 该类必须按照[确保符合 KVC 规范](../Key-Value%20Coding%20Programming%20Guide/Compliant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3te)中的规定，对该属性[符合键值编码规范](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25)。

  KVO 支持与 KVC 相同的数据类型，包括 Objective-C 对象以及“标量和结构体支持”中列出的标量和结构体。
- 该类会为该属性发出 KVO 更改[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)。
- 依赖键已得到适当注册（参阅[注册依赖键](Registering%20Dependent%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tslkciffekqkjivcq)）。

确保发出更改通知有两种技术。自动支持由 `NSObject` 提供，默认对类中所有[符合键值编码规范](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25)的属性可用。通常，只要你遵循标准的 Cocoa 编码和命名约定，就可以使用自动更改通知——无需编写任何额外代码。

手动更改通知可以对通知发出的时机提供更多控制，但需要额外编写代码。你可以通过实现类方法 [automaticallyNotifiesObserversForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1409370-automaticallynotifiesobservers) 来控制子类属性的自动通知。

`NSObject` 提供了自动键值更改通知的基本实现。自动键值更改通知会将通过符合键值编码规范的[访问器](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/AccessorMethod.html#//apple_ref/doc/uid/TP40008195-CH2)以及键值编码方法所做的更改告知观察者。例如，`mutableArrayValueForKey:` 返回的[集合](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Collection.html#//apple_ref/doc/uid/TP40008195-CH10)代理对象也支持自动通知。

清单 1 所示的示例会使属性 `name` 的所有观察者收到更改通知。

__清单 1__　触发 KVO 更改通知的方法调用示例

```objc
// Call the accessor method.
[account setName:@"Savings"];

// Use setValue:forKey:.
[account setValue:@"Savings" forKey:@"name"];

// Use a key path, where 'account' is a kvc-compliant property of 'document'.
[document setValue:@"Savings" forKeyPath:@"account.name"];

// Use mutableArrayValueForKey: to retrieve a relationship proxy object.
Transaction *newTransaction = <#Create a new transaction for the account#>;
NSMutableArray *transactions = [account mutableArrayValueForKey:@"transactions"];
[transactions addObject:newTransaction];
```


在某些情况下，你可能希望控制通知过程，例如，为了尽量减少触发因应用自身原因而不必要的通知，或将多个更改合并为一条通知。手动更改通知提供了实现这些目的的手段。

手动通知和自动通知并不互相排斥。你可以在已有的自动通知之外自由发送手动通知。更常见的情况是，你可能希望完全接管某个特定属性的通知。此时，你需要[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) `NSObject` 的 `automaticallyNotifiesObserversForKey:` 实现。对于想要禁用自动通知的属性，子类的 `automaticallyNotifiesObserversForKey:` 实现应返回 `NO`。对于无法识别的键，子类实现应调用 super。清单 2 中的示例为 `balance` 属性启用手动通知，其余所有键的通知则交由超类决定。

__清单 2__　automaticallyNotifiesObserversForKey: 的实现示例

```objc
+ (BOOL)automaticallyNotifiesObserversForKey:(NSString *)theKey {

    BOOL automatic = NO;
    if ([theKey isEqualToString:@"balance"]) {
        automatic = NO;
    }
    else {
        automatic = [super automaticallyNotifiesObserversForKey:theKey];
    }
    return automatic;
}
```

要实现手动观察者通知，你需要在更改值之前调用 [willChangeValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1416222-willchangevalueforkey)，在更改值之后调用 [didChangeValueForKey:](https://developer.apple.com/documentation/objectivec/nsobject/1411809-didchangevalue)。清单 3 中的示例为 `balance` 属性实现了手动通知。

__清单 3__　实现手动通知的访问器方法示例

```objc
- (void)setBalance:(double)theBalance {
    [self willChangeValueForKey:@"balance"];
    _balance = theBalance;
    [self didChangeValueForKey:@"balance"];
}
```

你可以先检查值是否已更改，从而尽量减少发送不必要的通知。清单 4 中的示例会测试 `balance` 的值，仅在其发生变化时才发出通知。

__清单 4__　在发出通知前测试值是否更改

```objc
- (void)setBalance:(double)theBalance {
    if (theBalance != _balance) {
        [self willChangeValueForKey:@"balance"];
        _balance = theBalance;
        [self didChangeValueForKey:@"balance"];
    }
}
```

如果一次操作导致多个键发生变化，你必须像清单 5 所示那样嵌套更改通知。

__清单 5__　为多个键嵌套更改通知

```objc
- (void)setBalance:(double)theBalance {
    [self willChangeValueForKey:@"balance"];
    [self willChangeValueForKey:@"itemChanged"];
    _balance = theBalance;
    _itemChanged = _itemChanged+1;
    [self didChangeValueForKey:@"itemChanged"];
    [self didChangeValueForKey:@"balance"];
}
```

对于有序对多关系，你不仅要指定发生变化的键，还要指定更改的类型以及所涉及对象的索引。更改类型是一个 [NSKeyValueChange](https://developer.apple.com/documentation/foundation/nskeyvaluechange)，取值为 `NSKeyValueChangeInsertion`、`NSKeyValueChangeRemoval` 或 `NSKeyValueChangeReplacement`。受影响对象的索引以 [NSIndexSet](https://developer.apple.com/documentation/foundation/nsindexset) 对象的形式传入。

清单 6 中的代码片段演示了如何包装对多关系 `transactions` 中对象的删除操作。

__清单 6__　对多关系中手动观察者通知的实现

```objc
- (void)removeTransactionsAtIndexes:(NSIndexSet *)indexes {
    [self willChange:NSKeyValueChangeRemoval
        valuesAtIndexes:indexes forKey:@"transactions"];

    // Remove the transaction objects at the specified indexes.

    [self didChange:NSKeyValueChangeRemoval
        valuesAtIndexes:indexes forKey:@"transactions"];
}
```

[下一页](Registering%20Dependent%20Keys.md)[上一页](Registering%20for%20Key-Value%20Observing.md)
