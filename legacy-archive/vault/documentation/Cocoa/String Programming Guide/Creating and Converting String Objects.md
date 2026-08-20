---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/CreatingStrings.html
archived_at: '2026-07-15T07:19:29.735981Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Formatting%20String%20Objects.md)[上一页](Strings.md)

# 创建与转换字符串对象

`NSString` 及其子类 `NSMutableString` 提供了多种创建字符串对象的方式，其中大多数都围绕它所支持的各种字符编码展开。虽然字符串对象总是以 Unicode 字符的形式呈现自身的内容，但它们可以把内容与许多其他编码相互转换，例如 7 位 ASCII、ISO Latin 1、EUC 和 Shift-JIS。类方法 [availableStringEncodings](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/availableStringEncodings) 会返回受支持的编码。在把 C 字符串转换成字符串对象（或反过来）时，你可以显式指定编码，也可以使用默认的 C 字符串编码——它因平台而异，由 `defaultCStringEncoding` 类方法返回。

在源代码中创建字符串对象最简单的方式，是使用 [Objective-C](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectiveC.html#//apple_ref/doc/uid/TP40008195-CH43)  的 `@"..."` 构造：

```objc
NSString *temp = @"Contrafibularity";
```

注意，用这种方式创建字符串常量时，你应该使用 UTF-8 字符。对于本地化文本，你可以把实际的 Unicode 数据直接放进字符串里，例如 `NSString *hello = @"こんにちは";`。你也可以在字符串中插入 `\u` 或 `\U` 来表示非图形字符。

Objective-C 字符串常量是在编译期创建的，并在程序的整个执行过程中一直存在。编译器会以模块为单位让这类对象常量保持唯一，而且它们永远不会被释放。你可以像给其他任何字符串发[消息](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Message.html#//apple_ref/doc/uid/TP40008195-CH59)一样，直接给字符串常量发送消息：

```objc
BOOL same = [@"comparison" isEqualToString:myString];
```


要从 C 字符串[创建](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectCreation.html#//apple_ref/doc/uid/TP40008195-CH39)一个 `NSString` 对象，你可以使用 [initWithCString:encoding:](https://developer.apple.com/documentation/foundation/nsstring/1411950-init) 之类的方法。你必须正确地指定该 C 字符串的字符编码。类似的方法还可以让你从多种编码的字符创建字符串对象。方法 `initWithData:encoding:` 让你能把存放在 `NSData` 对象中的字符串数据转换成 `NSString` 对象。

```objc
char *utf8String = /* 假设它已经存在。 */ ;
NSString *stringFromUTFString = [[NSString alloc] initWithUTF8String:utf8String];

char *macOSRomanEncodedString = /* 假设它已经存在 */ ;
NSString *stringFromMORString =
            [[NSString alloc] initWithCString:macOSRomanEncodedString
                              encoding:NSMacOSRomanStringEncoding];

NSData *shiftJISData =  /* 假设它已经存在 */ ;
NSString *stringFromShiftJISData =
            [[NSString alloc] initWithData:shiftJISData
                              encoding:NSShiftJISStringEncoding];
```

下面的例子把一个包含 UTF-8 字符的 `NSString` 对象转换成 ASCII 数据，然后再转换回 `NSString` 对象。

```objc
unichar ellipsis = 0x2026;
NSString *theString = [NSString stringWithFormat:@"To be continued%C", ellipsis];

NSData *asciiData = [theString dataUsingEncoding:NSASCIIStringEncoding allowLossyConversion:YES];

NSString *asciiString = [[NSString alloc] initWithData:asciiData encoding:NSASCIIStringEncoding];

NSLog(@"Original: %@ (length %d)", theString, [theString length]);
NSLog(@"Converted: %@ (length %d)", asciiString, [asciiString length]);

// 输出：
// Original: To be continued… (length 16)
// Converted: To be continued... (length 18)
```


要创建内容可变的字符串，你通常会用 [stringWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithFormat:): 或 [initWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:)（本地化字符串则用 [localizedStringWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/localizedStringWithFormat:)）。这些方法及其同类以格式字符串作为模板，把你提供的值（字符串和其他对象、数值等等）插入其中。关于它们以及所支持的格式说明符，参见[格式化字符串对象](Formatting%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dglkdjjbekqkfjbea)。

你可以用 [stringByAppendingString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByAppendingString:) 和 [stringByAppendingFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByAppendingFormat:) 方法，把已有的字符串对象拼接成新字符串——把一个字符串接在另一个之后，后一个方法还会用到格式字符串。

```objc
NSString *hString = @"Hello";
NSString *hwString = [hString stringByAppendingString:@", world!"];
```


在创建要呈现给用户的字符串时，你应该重视应用程序的[本地化](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23)。一般来说，你应该避免在代码里直接创建用户可见的字符串。相反，你应该把代码中的字符串当作查询本地化字典的键，由字典提供用户首选语言下的用户可见字符串。这通常意味着使用 [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring) 及类似的宏，如下面的例子所示。

```objc
NSString *greeting = NSLocalizedStringFromTable
    (@"Hello", @"greeting to present in first launch panel", @"greetings");
```

关于应用程序国际化的更多内容，参见 _[国际化与本地化指南](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_。Localizing String Resources 一文介绍了如何在本地化字符串中处理和重新排列可变参数。

你可以用多种方式组合和提取字符串。组合两个字符串最简单的方式是把一个追加到另一个之后。[stringByAppendingString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByAppendingString:) 方法返回一个由接收者和给定参数拼接而成的字符串对象。

```objc
NSString *beginning = @"beginning";
NSString *alphaAndOmega = [beginning stringByAppendingString:@" and end"];
// alphaAndOmega 是 @"beginning and end"
```

你也可以用 [initWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:)、[stringWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithFormat:) 和 [stringByAppendingFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByAppendingFormat:) 方法，按模板把多个字符串组合起来；这些方法在[格式化字符串对象](Formatting%20String%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dglkdjjbekqkfjbea)中有更详细的说明。

你可以用 [substringToIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/substringToIndex:)、[substringFromIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/substringFromIndex:) 和 [substringWithRange:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/substringWithRange:) 方法，从字符串的开头或末尾提取到某个索引为止的子串，或者提取指定范围内的子串。你还可以用 [componentsSeparatedByString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/componentsSeparatedByString:) 方法（依据一个分隔字符串）把字符串拆分成若干子串。下面的例子演示了这些方法——注意基于索引的方法中，索引是从 `0` 开始的：

```objc
NSString *source = @"0123456789";
NSString *firstFour = [source substringToIndex:4];
// firstFour 是 @"0123"

NSString *allButFirstThree = [source substringFromIndex:3];
// allButFirstThree 是 @"3456789"

NSRange twoToSixRange = NSMakeRange(2, 4);
NSString *twoToSix = [source substringWithRange:twoToSixRange];
// twoToSix 是 @"2345"

NSArray *split = [source componentsSeparatedByString:@"45"];
// split 包含 { @"0123", @"6789" }
```

如果你需要按模式匹配（而不是按索引）来提取字符串，应该使用扫描器——参见[扫描器](Scanners.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dolkcineukrshjbbq)。

要从字符串对象获取 C 字符串，推荐使用 `UTF8String`。它会返回一个采用 UTF8 字符串编码的 `const char *`。

```objc
const char *cString = [@"Hello, world" UTF8String];
```

你拿到的这个 C 字符串归某个临时对象所有，一旦发生自动释放它就会失效。如果你想得到一个长期有效的 C 字符串，就必须创建一个缓冲区，并把该方法返回的 `const char *` 的内容复制进去。

类似的方法还可以让你从 Unicode 编码或任意编码的字符创建字符串对象，以及按这些编码提取数据。`initWithData:encoding:` 和 `dataUsingEncoding:` 负责与 `NSData` 对象之间的这类转换。

下表汇总了创建与转换字符串对象最常用的方式：

| 来源 | 创建方法 | 提取方法 |
| --- | --- | --- |
| 代码中 | `@"..."` 编译器构造 | 无 |
| UTF8 编码 | [stringWithUTF8String:](https://developer.apple.com/documentation/foundation/nsstring/1497379-stringwithutf8string) | [UTF8String](https://developer.apple.com/documentation/foundation/nsstring/1411189-utf8string) |
| Unicode 编码 | [stringWithCharacters:length:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/stringWithCharacters:length:) | [getCharacters:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/getCharacters:)  [getCharacters:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/getCharacters:range:) |
| 任意编码 | [initWithData:encoding:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithData:encoding:) | [dataUsingEncoding:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/dataUsingEncoding:) |
| 已有的字符串 | [stringByAppendingString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByAppendingString:)  [stringByAppendingFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/stringByAppendingFormat:) | 无 |
| 格式字符串 | [localizedStringWithFormat:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/clm/NSString/localizedStringWithFormat:)  [initWithFormat:locale:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/initWithFormat:locale:) | 使用 `NSScanner` |
| 本地化字符串 | [NSLocalizedString](https://developer.apple.com/documentation/foundation/nslocalizedstring) 及类似的宏 | 无 |

[下一页](Formatting%20String%20Objects.md)[上一页](Strings.md)

