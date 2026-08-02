---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/CharacterSets.html
archived_at: '2026-07-15T07:19:29.196833Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Scanners.md)[上一页](Characters%20and%20Grapheme%20Clusters.md)

# 字符集

`NSCharacterSet` 对象表示一组 Unicode 字符。`NSString` 和 `NSScanner` 对象使用 `NSCharacterSet` 对象把字符归为一组以供搜索操作使用，这样它们就能在搜索过程中找到某个特定集合中的任意字符。

字符集（character set）对象表示一组 Unicode 字符。字符集由一个[类簇](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7)的实例来表示。该类簇的两个公开类 `NSCharacterSet` 和 `NSMutableCharacterSet` 分别声明了[不可变](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectMutability.html#//apple_ref/doc/uid/TP40008195-CH42)字符集和可变字符集的编程接口。不可变字符集在创建时即已确定，此后不能再更改。可变字符集在创建之后仍可以更改。

字符集对象本身不执行任何任务；它只是持有一组字符值，用于限定针对字符串的操作。`NSString` 和 `NSScanner` 类定义了一些以 `NSCharacterSet` 对象为参数的方法，用来查找若干字符中的任意一个。例如，下面这段代码找出 `myString:` 中第一个大写字母的范围。

```objc
NSString *myString = @"some text in an NSString...";
NSCharacterSet *characterSet = [NSCharacterSet uppercaseLetterCharacterSet];
NSRange letterRange = [myString rangeOfCharacterFromSet:characterSet];
```

这段代码执行之后，在调用 `rangeOfCharacterFromSet:` 之后，`letterRange.location` 等于“NSString”中第一个“N”的索引。如果该字符串的第一个字母是“S”，那么 `letterRange.location` 就会是 `0`。

`NSCharacterSet` 定义了一些类方法，用来返回常用的字符集，例如字母（大写或小写）、十进制数字、空白字符等等。这些“标准”字符集始终是不可变的，即使它们是通过向 `NSMutableCharacterSet` 发送消息创建的也一样。关于标准字符集的更多信息，请参阅[标准字符集与 Unicode 定义](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2tgljxgqzdimi)。

你可以把某个标准字符集作为起点来构建自定义字符集：先制作它的一份可变副本，然后修改这份副本。（你也可以从零开始，用 `alloc` 和 `init` 创建一个可变字符集，再往里添加字符。）例如，下面这段代码创建了一个包含字母、数字和基本标点符号的字符集：

```objc

NSMutableCharacterSet *workingSet = [[NSCharacterSet alphanumericCharacterSet] mutableCopy];
[workingSet addCharactersInString:@";:,."];
NSCharacterSet *finalCharacterSet = [workingSet copy];
```

要用 Unicode 码点来定义自定义字符集，可以参考下面这段代码（它创建的字符集包含换页符和行分隔符）：

```objc
UniChar chars[] = {0x000C, 0x2028};
NSString *string = [[NSString alloc] initWithCharacters:chars
                            length:sizeof(chars) / sizeof(UniChar)];
NSCharacterSet *characterSet = [NSCharacterSet characterSetWithCharactersInString:string];
```


由于字符集常常出现在对性能要求很高的代码中，你应当了解使用它们时哪些方面会影响应用的性能。可变字符集通常比不可变字符集开销大得多。它们占用更多内存，而且求反（这是扫描字符串时经常执行的操作）的代价很高。因此，你应当遵循以下准则：

- 尽量少创建可变字符集。
- 把字符集缓存起来（比如放在一个全局字典中），而不是不断地重新创建它们。
- 当创建的自定义字符集在创建之后不需要再改变时，请为最终的字符集制作一份不可变副本供实际使用，并丢弃用作中间结果的可变字符集。或者，你也可以按[创建字符集文件](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dmlktk4zq)中的说明创建一个字符集文件，并把它存放在应用的 main bundle 中。
- 同样地，应避免[归档](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Archiving.html#//apple_ref/doc/uid/TP40008195-CH1)字符集对象；改为把它们存放在字符集文件中。归档可能导致同一个字符集在不同的归档文件中被重复保存，既浪费磁盘空间，也会在每次读取不同归档时在内存中产生重复副本。

如果你的应用频繁使用某个自定义字符集，就应当把它的定义保存到一个资源文件中并从中加载，而不是每次需要创建该字符集时都逐个显式添加字符。你可以获取字符集的位图表示（一个 `NSData` 对象）并把该对象保存到文件，以此保存这个字符集：

```objc
NSData *charSetRep = [finalCharacterSet bitmapRepresentation];
NSURL *dataURL = <#URL for character set#>;
NSError *error;
BOOL result = [charSetRep writeToURL:dataURL options:NSDataWritingAtomic error:&error];
```

按照惯例，字符集文件名使用 `.bitmap` 扩展名。如果你希望别人也能使用你的字符集文件，就应当遵循这一惯例。要读取扩展名为 `.bitmap` 的字符集文件，只需使用 `characterSetWithContentsOfFile:` 方法。

诸如 `letterCharacterSet` 所返回的这类标准字符集，是依据 Unicode 标准确立的规范性类别和资讯性类别（例如 Uppercase Letter、Combining Mark 等）来正式定义的。标准字符集的正式定义在大多数情况下由标准中定义的一个或多个类别给出。例如，`lowercaseLetterCharacterSet` 返回的字符集包含规范性类别 Lowercase Letters 中的所有字符，而 `letterCharacterSet` 返回的字符集则包含所有 Letter 类别中的字符。

注意，这些类别本身的定义可能会随 Unicode 标准的新版本而变化。你可以从 [http://www.unicode.org/](http://www.unicode.org/) 下载定义类别成员关系的文件。

[下一页](Scanners.md)[上一页](Characters%20and%20Grapheme%20Clusters.md)

