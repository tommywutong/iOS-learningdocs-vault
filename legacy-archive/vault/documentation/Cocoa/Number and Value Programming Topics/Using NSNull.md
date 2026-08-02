---
title: 数值与值编程主题
apple_id: 10000038i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/Articles/Null.html
archived_at: '2026-07-15T07:17:17.985632Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数值与值编程主题](Introduction%20to%20Numbers%20and%20Other%20Values.md)


[下一页](Document%20Revision%20History.md)[上一页](Using%20Decimal%20Numbers.md)

# 使用 NSNull

`NSNull` 类定义了一个单例对象，用于在禁止以 `nil` 作为值的场合（典型情况是数组或字典之类的集合对象）表示空值。

```objc
NSNull *nullValue = [NSNull null];
NSArray *arrayWithNull = @[nullValue];
NSLog(@"arrayWithNull: %@", arrayWithNull);
// 输出："arrayWithNull: (<null>)"
```

需要重点理解的是，`NSNull` 实例在语义上不同于 `NO` 或 `false`——后两者都表示逻辑值，而 `NSNull` 实例表示值的缺失。`NSNull` 实例在语义上等价于 `nil`，但同样重要的是要明白它并不等于 `nil`。因此，要判断某个值是否为 null 对象，必须进行直接的对象比较。

```objc
id aValue = [arrayWithNull objectAtIndex:0];
if (aValue == nil) {
    NSLog(@"equals nil");
}
else if (aValue == [NSNull null]) {
    NSLog(@"equals NSNull instance");
    if ([aValue isEqual:nil]) {
        NSLog(@"isEqual:nil");
    }
}
// 输出："equals NSNull instance"
```

[下一页](Document%20Revision%20History.md)[上一页](Using%20Decimal%20Numbers.md)
