---
title: 数据格式化指南
apple_id: 10000029i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/Articles/dfNumberFormatting10_4.html
archived_at: '2026-07-15T07:14:35.432241Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [数据格式化指南](Introduction%20to%20Data%20Formatting%20Programming%20Guide%20For%20Cocoa.md)


[下一页](Formatters%20and%20User%20Interface%20Elements.md)[上一页](Date%20Formatters.md)

# 数字格式化器

`NSNumberFormatter` 提供了两个便捷方法——[stringFromNumber:](https://developer.apple.com/documentation/foundation/nsnumberformatter/1418046-stringfromnumber) 和 [numberFromString:](https://developer.apple.com/documentation/foundation/numberformatter/1408845-number)——分别用于创建数字的字符串表示形式，以及从字符串创建数字对象。如果想在不创建格式化器对象的情况下生成数字的本地化字符串表示形式，可以使用类方法 [localizedStringFromNumber:numberStyle:](https://developer.apple.com/documentation/foundation/numberformatter/1416418-localizedstring)。

如果你在解析字符串时有更复杂的需求，除了从 `NSFormatter` 继承来的方法（例如 [getObjectValue:forString:errorDescription:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSFormatter/Description.html#//apple_ref/occ/instm/NSFormatter/getObjectValue:forString:errorDescription:)）之外，[getObjectValue:forString:range:error:](https://developer.apple.com/documentation/foundation/nsnumberformatter/1412588-getobjectvalue) 方法允许你指定要解析的字符串子范围，并返回实际被解析的字符串范围。（如果解析失败，则指出失败发生的位置。）它还会返回一个 `NSError` 对象，其中可以包含关于该问题的丰富信息。

数字格式化器上有许多可以读取和设置的属性。向用户展示信息时，通常应直接使用 `NSNumberFormatter` 的样式常量，来指定一组预定义的属性，从而决定格式化后的数字如何显示。但如果你需要以精确的格式生成数字的表示形式，就应该使用格式字符串。

`NSNumberFormatter` 让你可以轻松地使用用户在系统偏好设置的“国际化”面板中配置的设置来格式化各种数字。`NSNumberFormatter` 的样式常量——`NSNumberFormatterDecimalStyle`、`NSNumberFormatterCurrencyStyle`、`NSNumberFormatterPercentStyle`、`NSNumberFormatterScientificStyle`，或用于生成数字文字表示形式的 `NSNumberFormatterSpellOutStyle`——指定了一组属性，用于按照用户的偏好设置决定数字的显示方式。

你可以使用 [setNumberStyle:](https://developer.apple.com/documentation/foundation/nsnumberformatter/1416915-numberstyle) 指定数字格式化器的样式。[清单 1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnryfvjvomq) 演示了如何使用格式化器样式格式化数字。

__清单 1__  使用格式化器样式格式化数字

```objc
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setNumberStyle:NSNumberFormatterDecimalStyle];
NSString *formattedNumberString = [numberFormatter stringFromNumber:@122344.4563];
NSLog(@"formattedNumberString: %@", formattedNumberString);
// 在 en_US 语言环境下的输出："formattedNumberString: formattedNumberString: 122,344.453"
```


格式字符串使用 Unicode 技术标准 #35 中的格式模式。该标准的版本会随操作系统版本而变化：

- OS X v10.9 和 iOS 7 使用 [tr35-31 版本](http://www.unicode.org/reports/tr35/tr35-31/tr35-numbers.html#Number_Format_Patterns)。
- OS X v10.8 和 iOS 6 使用 [tr35-25 版本](http://www.unicode.org/reports/tr35/tr35-25.html#Number_Format_Patterns)。
- iOS 5 使用 [tr35-19 版本](http://www.unicode.org/reports/tr35/tr35-19.html#Number_Format_Patterns)。
- OS X v10.7 和 iOS 4.3 使用 [tr35-17 版本](http://www.unicode.org/reports/tr35/tr35-17.html#Number_Format_Patterns)。
- iOS 4.0、iOS 4.1 和 iOS 4.2 使用 [tr35-15 版本](http://www.unicode.org/reports/tr35/tr35-15.html#Number_Format_Patterns)。
- iOS 3.2 使用 [tr35-12 版本](http://www.unicode.org/reports/tr35/tr35-12.html#Number_Format_Patterns)。
- OS X v10.6、iOS 3.0 和 iOS 3.1 使用 [tr35-10 版本](http://unicode.org/reports/tr35/tr35-10.html#Number_Format_Patterns)。
- OS X v10.5 使用 [tr35-6 版本](http://unicode.org/reports/tr35/tr35-6.html#Number_Format_Patterns)。
- OS X v10.4 使用 [tr35-4 版本](http://unicode.org/reports/tr35/tr35-4.html#Number_Format_Patterns)。

请注意，使用 Unicode 格式字符串格式时，应将格式字符串中的字面文本用单引号（`''`）括起来。

你可以使用 [setPositiveFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setPositiveFormat:) 和 [setNegativeFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSNumberFormatter/Description.html#//apple_ref/occ/instm/NSNumberFormatter/setNegativeFormat:) 指定数字格式化器的格式字符串。[清单 2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdgnryfvjvooi) 演示了如何使用格式字符串格式化数字。

__清单 2__  使用格式字符串格式化数字

```objc
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setPositiveFormat:@"###0.##"];
NSString *formattedNumberString = [numberFormatter stringFromNumber:@122344.4563];
NSLog(@"formattedNumberString: %@", formattedNumberString);
// 在 en_US 语言环境下的输出："formattedNumberString: formattedNumberString: 122,344.45"
```


如果使用带有 "%" 字符的格式字符串来格式化百分比，结果可能会让人困惑。请看下面的例子：

```objc
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setPositiveFormat:@"0.00%;0.00%;-0.00%"];
NSLog(@"%@", [numberFormatter stringFromNumber:@4.0]);
// 输出："400.00%"。
```

由于该格式字符串指定使用百分比，`NSNumberFormatter` 会把数字 4 解释为一个分数（其中 1 表示 100%），并按此渲染（4 = 4/1 = 400%）。

如果你想把一个数字表示为百分比，应该使用 `NSNumberFormatterPercentStyle` 样式——这样还能确保百分比按照该语言环境的规范正确格式化：

```objc
NSNumberFormatter *numberFormatter = [[NSNumberFormatter alloc] init];
[numberFormatter setNumberStyle:NSNumberFormatterPercentStyle];

NSLocale *usLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"en_US"];
[numberFormatter setLocale:usLocale];
NSLog(@"en_US: %@", [numberFormatter stringFromNumber:@4.0]);
// 输出："en_US: 400%"。

NSLocale *faLocale = [[NSLocale alloc] initWithLocaleIdentifier:@"fa_IR"];
[numberFormatter setLocale:faLocale];
NSLog(@"fa_IR: %@", [numberFormatter stringFromNumber:@4.0]);
// 输出："fa_IR: ‪‪٪۴۰۰‬.‬"
```


`NSNumberFormatter` 提供了若干方法（例如 [setMaximumFractionDigits:](https://developer.apple.com/documentation/foundation/nsnumberformatter/1415364-maximumfractiondigits)），让你可以管理某个实例作为输入所允许的 _小数位数_。"小数位数"是指小数分隔符之后的数字（在英语语言环境中，小数分隔符通常称为"小数点"）。

[下一页](Formatters%20and%20User%20Interface%20Elements.md)[上一页](Date%20Formatters.md)

