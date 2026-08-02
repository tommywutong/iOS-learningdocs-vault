---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/SearchingStrings.html
archived_at: '2026-07-15T07:19:32.244917Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Words%2C%20Paragraphs%2C%20and%20Line%20Breaks.md)[上一页](Reading%20Strings%20From%20and%20Writing%20Strings%20To%20Files%20and%20URLs.md)

# 搜索、比较与排序字符串

字符串类提供了一些方法，用于在字符串中查找字符和子串，以及把一个字符串与另一个字符串进行[比较](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ObjectComparison.html#//apple_ref/doc/uid/TP40008195-CH37)。这些方法在判断两个字符序列是否等价时遵循 Unicode 标准。字符串类提供的比较方法能正确处理组合字符序列；不过，当效率很重要、并且你能保证组合字符序列采用某种规范形式（canonical form）时，你也可以选择指定字面搜索（literal search）。

搜索方法和比较方法各有若干个变体。每一类中最简单的那个版本搜索或比较整个字符串。其他变体则允许你改变组合字符序列的比较方式，并指定字符串中要参与搜索或比较的具体字符范围；你还可以在给定 locale 的上下文中搜索和比较字符串。

以下是基本的搜索方法和比较方法：

| 搜索方法 | 比较方法 |
| --- | --- |
| [rangeOfString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:) | [compare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:) |
| [rangeOfString:options:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:) | [compare:options:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:options:) |
| [rangeOfString:options:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:range:) | [compare:options:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:options:range:) |
| [rangeOfString:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1417348-range) | [compare:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1414561-compare) |
| [rangeOfCharacterFromSet:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:) |  |
| [rangeOfCharacterFromSet:options:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:options:) |  |
| [rangeOfCharacterFromSet:options:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfCharacterFromSet:options:range:) |  |

你用 `rangeOfString:...` 系列方法在接收者中搜索子串。`rangeOfCharacterFromSet:...` 系列方法则从给定的字符集合中搜索单个字符。

只有当子串完整地包含在指定范围内时才能被找到。如果你为搜索或比较方法指定了范围，并且没有请求 `NSLiteralSearch`（见下文），那么该范围的两端都不能把组合字符序列切断；一旦切断，你可能得到不正确的结果。（[rangeOfComposedCharacterSequenceAtIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfComposedCharacterSequenceAtIndex:) 的方法说明里有一段示例代码，演示如何把范围调整到字符序列的边界上。）

你也可以用 `NSScanner` 的实例来扫描字符串中的数值和字符串值。关于扫描器的更多内容，参见[扫描器](Scanners.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dolkcineukrshjbbq)。`NSString` 和 `NSScanner` 这两个类簇的搜索操作都使用 `NSCharacterSet` 类簇。关于字符集的更多内容，参见[字符集](Character%20Sets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dmlkciffeessiindq)。

如果你只是想判断某个字符串是否包含给定的模式，可以使用谓词：

```objc
BOOL match = [myPredicate evaluateWithObject:myString];
```

关于谓词的更多内容，参见 _[谓词编程指南](../Predicate%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytoobz)_。

`compare:...` 系列方法返回接收者与给定字符串之间的字典序关系。还有另外几个方法可以判断两个字符串是否相等，或者一个字符串是否是另一个的前缀或后缀，但它们没有可以指定搜索选项或范围的变体。

比较字符串最简单的方法是 [compare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:)——它等同于调用 [compare:options:range:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:options:range:) 时不带任何选项，并把接收者的完整长度作为范围。如果你想指定比较选项（`NSCaseInsensitiveSearch`、`NSLiteralSearch` 或 `NSNumericSearch`），可以使用 [compare:options:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/compare:options:)；如果你想指定 locale，可以使用 [compare:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1414561-compare)。`NSString` 还提供了各种便捷方法，让你无需直接指定范围和选项就能完成常见的比较，例如 [caseInsensitiveCompare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/caseInsensitiveCompare:) 和 [localizedCompare:](https://developer.apple.com/documentation/foundation/nsstring/1416999-localizedcompare)。

如果你想让字符串的比较结果与 Finder 中呈现的顺序一致，应该使用 [compare:options:range:locale:](https://developer.apple.com/documentation/foundation/nsstring/1414561-compare)，传入用户的 locale 以及下列选项：`NSCaseInsensitiveSearch`、`NSNumericSearch`、`NSWidthInsensitiveSearch` 和 `NSForcedOrderingSearch`。示例参见[像 Finder 那样排序字符串](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge2dslktk4yq)。

若干搜索方法和比较方法接受一个 “options” 参数。它是一个位掩码，为操作附加更多约束。你可以组合下列选项来构造这个掩码（并非每个方法都支持全部选项）：

| 搜索选项 | 效果 |
| --- | --- |
| [NSCaseInsensitiveSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSCaseInsensitiveSearch) | 忽略字符之间的大小写差异。 |
| [NSLiteralSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSLiteralSearch) | 执行逐字节的比较。字面序列（例如组合字符序列）只要有差异，就被视为不匹配——哪怕在其他情况下它们会被认为是等价的。使用这个选项可以让某些操作的速度大幅提升。 |
| [NSBackwardsSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSBackwardsSearch) | 从范围的末尾向开头进行搜索。 |
| [NSAnchoredSearch](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/TypesAndConstants/FoundationTypesConstants/Description.html#//apple_ref/c/econst/NSAnchoredSearch) | 只在范围开头的字符上进行搜索；如果同时指定了 `NSBackwardsSearch`，则只在范围末尾的字符上进行搜索。开头或末尾没有匹配就意味着什么也找不到，即使字符串的其他位置存在匹配的字符序列也是如此。 |
| [NSNumericSearch](https://developer.apple.com/documentation/foundation/nsstringcompareoptions/nsnumericsearch) | 与 `compare:options:` 系列方法一起使用时，成组的数字会被当作一个数值来参与比较。例如 `Filename9.txt` < `Filename20.txt` < `Filename100.txt`。 |

目前，搜索和比较的执行效果等同于指定了 `NSLiteralSearch` 选项。

`NSString` 提供了 [hasPrefix:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/hasPrefix:) 和 [hasSuffix:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/hasSuffix:) 方法，可用于查找与前缀或后缀_完全_匹配的情况。下面的例子演示了如何用 [rangeOfString:options:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/rangeOfString:options:) 组合多个选项来执行_不区分大小写_的搜索。

```objc
NSString *searchString = @"age";

NSString *beginsTest = @"Agencies";
NSRange prefixRange = [beginsTest rangeOfString:searchString
    options:(NSAnchoredSearch | NSCaseInsensitiveSearch)];

// prefixRange = {0, 3}

NSString *endsTest = @"BRICOLAGE";
NSRange suffixRange = [endsTest rangeOfString:searchString
    options:(NSAnchoredSearch | NSCaseInsensitiveSearch | NSBackwardsSearch)];

// suffixRange = {6, 3}
```


下面几个例子演示了各种字符串比较方法以及相关选项的用法。第一个例子展示的是最简单的比较方法。

```objc
NSString *string1 = @"string1";
NSString *string2 = @"string2";
NSComparisonResult result;
result = [string1 compare:string2];
// result = -1 (NSOrderedAscending)
```

你可以用 `NSNumericSearch` 选项按数值比较字符串：

```objc
NSString *string10 = @"string10";
NSString *string2 = @"string2";
NSComparisonResult result;

result = [string10 compare:string2];
// result = -1 (NSOrderedAscending)

result = [string10 compare:string2 options:NSNumericSearch];
// result = 1 (NSOrderedDescending)
```

你可以使用便捷方法（[caseInsensitiveCompare:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/caseInsensitiveCompare:) 和 [localizedCaseInsensitiveCompare:](https://developer.apple.com/documentation/foundation/nsstring/1417333-localizedcaseinsensitivecompare)）来执行不区分大小写的比较：

```objc
NSString *string_a = @"Aardvark";
NSString *string_A = @"AARDVARK";

result = [string_a compare:string_A];
// result = 1 (NSOrderedDescending)

result = [string_a caseInsensitiveCompare:string_A];
// result = 0 (NSOrderedSame)
// 等价于 [string_a compare:string_A options:NSCaseInsensitiveSearch]
```


要让字符串的排序方式与 OS X v10.6 及更高版本中 Finder 的做法一致，请使用 [localizedStandardCompare:](https://developer.apple.com/documentation/foundation/nsstring/1409742-localizedstandardcompare) 方法。凡是在列表和表格中呈现文件名或其他字符串、且适合采用 Finder 风格排序的场合，都应该使用它。该方法的确切行为在不同的本地化环境下并不相同，因此调用方不应依赖字符串的确切排序顺序。

下面的例子展示了实现类似功能的另一种做法：比较字符串，使其顺序与 Finder 中呈现的一致，同时还演示了如何对字符串数组排序。首先，定义一个包含相关比较选项的排序函数（出于效率考虑，把用户的 locale 作为上下文传入——这样它只需查询一次）。

```objc
int finderSortWithLocale(id string1, id string2, void *locale)
{
    static NSStringCompareOptions comparisonOptions =
        NSCaseInsensitiveSearch | NSNumericSearch |
        NSWidthInsensitiveSearch | NSForcedOrderingSearch;

    NSRange string1Range = NSMakeRange(0, [string1 length]);

    return [string1 compare:string2
                    options:comparisonOptions
                    range:string1Range
                    locale:(NSLocale *)locale];
}
```

你把这个函数作为参数传给 [sortedArrayUsingFunction:context:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSArrayClassCluster/Description.html#//apple_ref/occ/instm/NSArray/sortedArrayUsingFunction:context:)，并把用户当前的 locale 作为上下文：

```objc
NSArray *stringsArray = @[@"string 1",
                          @"String 21",
                          @"string 12",
                          @"String 11",
                          @"String 02"];

NSArray *sortedArray = [stringsArray sortedArrayUsingFunction:finderSortWithLocale
                                     context:[NSLocale currentLocale]];

// sortedArray 包含 { "string 1", "String 02", "String 11", "string 12", "String 21" }
```

[下一页](Words%2C%20Paragraphs%2C%20and%20Line%20Breaks.md)[上一页](Reading%20Strings%20From%20and%20Writing%20Strings%20To%20Files%20and%20URLs.md)

