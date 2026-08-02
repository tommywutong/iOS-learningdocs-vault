---
title: 数值与值编程主题
apple_id: 10000038i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2008-02-08'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NumbersandValues/Articles/Numbers.html
archived_at: '2026-07-15T07:17:18.524641Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数值与值编程主题](Introduction%20to%20Numbers%20and%20Other%20Values.md)


[下一页](Using%20Decimal%20Numbers.md)[上一页](Using%20Values.md)

# 使用数值

`NSNumber` 是 `NSValue` 的子类，可以以任意 C 标量（数值）类型提供值。它定义了一组方法，专门用于创建数值对象，并以带符号或无符号的 `char`、`short int`、`int`、`NSInteger`、`long int`、`long long int`、`float`、`double` 或 `BOOL` 的形式访问其值。

```objc
NSInteger nine = 9;
float ten = 10.0;

NSNumber *nineFromInteger = [NSNumber alloc] initWithInteger:nine];
NSNumber *tenFromFloat = [NSNumber numberWithFloat:ten];
```

你也可以使用 `@` 直接以字面量创建数值对象：

```objc
NSNumber *nineFromInteger = @9;
NSNumber *tenFromFloat = @10.0;
NSNumber *nineteenFromExpression = @(nine + ten);
```

`NSNumber` 定义了 `compare:` 方法，用于确定两个 `NSNumber` 对象的先后顺序：

```objc
NSComparisonResult comparison = [nineFromInteger compare:tenFromFloat];
// comparison = NSOrderedAscending

float aFloat = [nineFromInteger floatValue];
// aFloat = 9.0
BOOL ok = [tenFromFloat boolValue];
// ok = YES
```

`NSNumber` 对象会记录创建它时所用的数值类型，在比较不同数值类型的 `NSNumber` 对象、以及以 C 数值类型返回值时，它遵循 C 语言的数值转换规则。有关类型转换的信息，请参阅任意一本标准 C 参考手册。（不过，如果你向一个数值对象请求它的 [objCType](https://developer.apple.com/documentation/foundation/nsnumber/1807278-objctype)，返回的类型不一定与接收者创建时所用的方法相匹配。）

如果你用一个无法容纳该值的类型向 `NSNumber` 对象请求其值，得到的将是错误的结果——例如，向一个以大于 `FLT_MAX` 的 `double` 创建的数值请求其 `float` 值，或向一个以大于 `NSInteger` 最大值的 `float` 创建的数值请求其 `integer` 值。

```objc
NSNumber *bigNumber = @(FLT_MAX);
NSInteger badInteger = [bigNumber integerValue];
NSLog(@"bigNumber: %@; badInteger: %d", bigNumber, badInteger);
// 输出："bigNumber: 3.402823e+38; badInteger: 0"
```

[下一页](Using%20Decimal%20Numbers.md)[上一页](Using%20Values.md)
