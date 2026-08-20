---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html
archived_at: '2026-07-15T07:19:30.676700Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](String%20Format%20Specifiers.md)[上一页](Creating%20and%20Converting%20String%20Objects.md)

# 格式化字符串对象

本文介绍如何用格式字符串创建字符串、如何在格式字符串中使用非 ASCII 字符，以及开发者在使用 `NSLog` 或 `NSLogv` 时常犯的一个错误。

`NSString` 使用的格式字符串，其语法与其他格式化对象所用的语法类似。它支持为 ANSI C 函数 `printf()` 定义的那些格式字符，另外还支持用 `%@` 表示任意对象（参见[字符串格式说明符](String%20Format%20Specifiers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denrvfvjvomi) 和 [IEEE printf 规范](http://www.opengroup.org/onlinepubs/009695399/functions/printf.html)）。如果对象能响应 `descriptionWithLocale:` 消息，`NSString` 就会发送该消息来取得其文本表示；否则它会发送 `description` 消息。Localizing String Resources 介绍了如何在本地化字符串中处理和重新排列可变参数。

在格式字符串中，‘`%`’ 字符表示这里是一个值的占位符，紧随其后的字符决定了期望什么类型的值以及如何格式化它。例如，格式字符串 `"%d houses"` 期望用一个整数值来替换格式表达式 '`%d`'。`NSString` 支持为 ANSI C 函数 `printf()` 定义的那些格式字符，另外还支持用 ‘`@`’ 表示任意对象。如果对象能响应 `descriptionWithLocale:` 消息，`NSString` 就会发送该消息来取得其文本表示，否则它会发送 `description` 消息。

值的格式化会受用户当前 locale 的影响，locale 是一个 `NSDictionary` 对象，指定了数字、日期以及其他各类格式。`NSString` 只使用 locale 中对小数分隔符的定义（由名为 `NSDecimalSeparator` 的键给出）。如果你使用的方法没有指定 locale，字符串就会采用默认 locale。

你可以使用 `NSString` 的 [stringWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithFormat:) 方法以及其他相关方法，配合 `printf` 风格的格式说明符和参数列表来创建字符串，具体说明见[创建与转换字符串对象](Creating%20and%20Converting%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dqlkdjjbegssijbeq)。下面的示例演示了如何用各种格式说明符和参数来创建字符串。

```objc
NSString *string1 = [NSString stringWithFormat:@"A string: %@, a float: %1.2f",
                                               @"string", 31415.9265];
// string1 的内容是 "A string: string, a float: 31415.93"

NSNumber *number = @1234;
NSDictionary *dictionary = @{@"date": [NSDate date]};
NSString *baseString = @"Base string.";
NSString *string2 = [baseString stringByAppendingFormat:
        @" A number: %@, a dictionary: %@", number, dictionary];
// string2 的内容是 "Base string. A number: 1234, a dictionary: {date = 2005-10-17 09:02:01 -0700; }"
```


你可以使用 `stringWithFormat:` 和 `stringWithUTF8String:` 等方法，在字符串中包含非 ASCII 字符（包括 Unicode 字符）。

```objc
NSString *s = [NSString stringWithFormat:@"Long %C dash", 0x2014];
```

由于 `\xe2\x80\x94` 就是 `0x2014` 对应的 3 字节 UTF-8 字符串，你也可以这样写：

```objc
NSString *s = [NSString stringWithUTF8String:"Long \xe2\x80\x94   dash"];
```


实用函数 `NSLog()` 和 `NSLogv()` 使用 `NSString` 的字符串格式化服务来记录错误消息。请注意，正因如此，你在为这些函数指定参数时必须小心。一个常见错误是传入一个本身就包含格式化字符的字符串，如下例所示。

```objc
NSString *string = @"A contrived string %@";
NSLog(string);
// 应用程序在这里很可能会因为 signal 10 (SIGBUS) 而崩溃
```

更好（更安全）的做法是用一个格式字符串来输出另一个字符串，如下例所示。

```objc
NSString *string = @"A contrived string %@";
NSLog(@"%@", string);
// 输出：A contrived string %@
```

[下一页](String%20Format%20Specifiers.md)[上一页](Creating%20and%20Converting%20String%20Objects.md)

