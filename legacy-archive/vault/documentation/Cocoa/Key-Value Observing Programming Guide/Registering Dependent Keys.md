---
title: 键值观察编程指南
apple_id: 10000177i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/Articles/KVODependentKeys.html
archived_at: '2026-07-15T07:16:18.603750Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [键值观察编程指南](Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md)


[下一页](Key-Value%20Observing%20Implementation%20Details.md)[上一页](KVO%20Compliance.md)

# 注册依赖键

在许多情况下，一个属性的值依赖于另一个对象中一个或多个其他属性的值。如果其中一个属性的值发生变化，派生属性的值也应被标记为已更改。如何确保为这些依赖属性发出键值观察[通知](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Notification.html#//apple_ref/doc/uid/TP40008195-CH35)，取决于关系的基数。

要为对一关系自动触发通知，你应当[重写](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/MethodOverriding.html#//apple_ref/doc/uid/TP40008195-CH57) `keyPathsForValuesAffectingValueForKey:`，或者实现一个遵循该方法所定义模式的合适方法来注册依赖键。

例如，一个人的全名同时依赖于名和姓。返回全名的方法可以这样写：

```objc
- (NSString *)fullName {
    return [NSString stringWithFormat:@"%@ %@",firstName, lastName];
}
```

由于 `firstName` 或 `lastName` 属性的变化会影响 `fullName` 属性的值，观察 `fullName` 属性的应用必须在其中任何一个发生变化时收到通知。

一种解决方案是重写 `keyPathsForValuesAffectingValueForKey:`，指定人的 `fullName` 属性依赖于 `lastName` 和 `firstName` 属性。[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tslktk4yq) 给出了这种依赖关系的实现示例：

__清单 1__　`keyPathsForValuesAffectingValueForKey:` 的实现示例

```objc
+ (NSSet *)keyPathsForValuesAffectingValueForKey:(NSString *)key {

    NSSet *keyPaths = [super keyPathsForValuesAffectingValueForKey:key];

    if ([key isEqualToString:@"fullName"]) {
        NSArray *affectingKeys = @[@"lastName", @"firstName"];
        keyPaths = [keyPaths setByAddingObjectsFromArray:affectingKeys];
    }
    return keyPaths;
}
```

你的重写通常应调用 super，并返回一个包含由此所得集合中所有成员的集合（以免干扰超类中对该方法的重写）。

你也可以通过实现一个遵循命名约定 `keyPathsForValuesAffecting<Key>` 的类方法来达到同样的效果，其中 `<Key>` 是依赖于其他值的属性名（首字母大写）。按照这一模式，[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tslktk4yq) 中的代码可以重写为名为 `keyPathsForValuesAffectingFullName` 的类方法，如[清单 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsge3tslktk4za) 所示。

__清单 2__　`keyPathsForValuesAffecting<Key>` 命名约定的实现示例

```objc
+ (NSSet *)keyPathsForValuesAffectingFullName {
    return [NSSet setWithObjects:@"lastName", @"firstName", nil];
}
```

当你使用[类别](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Category.html#//apple_ref/doc/uid/TP40008195-CH5)为现有类添加计算属性时，无法重写 `keyPathsForValuesAffectingValueForKey:` 方法，因为你不应在类别中重写方法。在这种情况下，可以实现一个匹配的 `keyPathsForValuesAffecting<Key>` 类方法来利用这一机制。

`keyPathsForValuesAffectingValueForKey:` 方法不支持包含对多关系的键路径。例如，假设你有一个 Department 对象，它与 Employee 之间存在对多关系（`employees`），而 Employee 有一个 salary 属性。你可能希望 Department 对象拥有一个 `totalSalary` 属性，依赖于该关系中所有 Employee 的薪水。但你无法通过诸如 `keyPathsForValuesAffectingTotalSalary` 并返回 `employees.salary` 作为键来做到这一点。

在这两种情况下都有两种可行的解决方案：

1. 你可以使用键值观察，将父对象（本例中为 Department）注册为所有子对象（本例中为 Employee）相关属性的观察者。当子对象被添加到关系中或从中移除时，你必须相应地添加和移除作为观察者的父对象（参阅[注册键值观察](Registering%20for%20Key-Value%20Observing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2telkciffekqkjivcq)）。在 `observeValueForKeyPath:ofObject:change:context:` 方法中，你响应变化并更新依赖值，如以下代码片段所示：

```objc
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context {

    if (context == totalSalaryContext) {
        [self updateTotalSalary];
    }
    else
    // deal with other observations and/or invoke super...
}

- (void)updateTotalSalary {
    [self setTotalSalary:[self valueForKeyPath:@"employees.@sum.salary"]];
}

- (void)setTotalSalary:(NSNumber *)newTotalSalary {

    if (totalSalary != newTotalSalary) {
        [self willChangeValueForKey:@"totalSalary"];
        _totalSalary = newTotalSalary;
        [self didChangeValueForKey:@"totalSalary"];
    }
}

- (NSNumber *)totalSalary {
    return _totalSalary;
}
```
2. 如果你在使用 Core Data，可以将父对象注册到应用的通知中心，作为其托管对象上下文的观察者。父对象应以类似键值观察的方式响应子对象发出的相关更改通知。

[下一页](Key-Value%20Observing%20Implementation%20Details.md)[上一页](KVO%20Compliance.md)
