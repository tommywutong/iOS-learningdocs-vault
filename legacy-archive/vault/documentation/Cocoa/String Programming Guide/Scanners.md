---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/Scanners.html
archived_at: '2026-07-15T07:19:31.733761Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](String%20Representations%20of%20File%20Paths.md)[上一页](Character%20Sets.md)

# 扫描器

`NSScanner` 对象扫描 `NSString` 对象中的字符，通常是解释这些字符并把它们转换成数值和字符串值。你在创建扫描器时为它指定字符串，随后每当你请求一项内容，扫描器就沿着该字符串的字符从头向尾推进。

`NSScanner` 是一个[类簇](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassCluster.html#//apple_ref/doc/uid/TP40008195-CH7)，只有一个公开类 [NSScanner](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/cl/NSScanner)。一般来说，你通过调用[类方法](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/ClassMethod.html#//apple_ref/doc/uid/TP40008195-CH8) [scannerWithString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/clm/NSScanner/scannerWithString:) 或 [localizedScannerWithString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/clm/NSScanner/localizedScannerWithString:) 来实例化扫描器对象。这两个方法都会返回一个用你传入的字符串初始化好的扫描器对象。新创建的扫描器从字符串的开头开始。你用 `scan...` 系列方法来扫描其中的成分，例如 [scanInt:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanInt:)、[scanDouble:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanDouble:) 和 [scanString:intoString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanString:intoString:)。如果你要扫描多行内容，通常会写一个 `while` 循环，一直执行到扫描器到达字符串末尾为止，如下面的代码片段所示：

```objc
float aFloat;
NSScanner *theScanner = [NSScanner scannerWithString:aString];
while ([theScanner isAtEnd] == NO) {

    [theScanner scanFloat:&aFloat];
    // 实现代码继续 ...
}
```

你可以用 [setCaseSensitive:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setCaseSensitive:) 方法配置扫描器，让它区分或忽略大小写。扫描器默认忽略大小写。

扫描操作从扫描位置开始，并把扫描器推进到所扫描值的表示形式（如果有的话）中最后一个字符之后。举例来说，从字符串“`137 small cases of bananas`”中扫描出一个整数之后，扫描器的位置会是 3，也就是数字紧后面的那个空格。你经常需要推进扫描位置，跳过自己不关心的字符。你可以用 [setScanLocation:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setScanLocation:) 方法修改隐式的扫描位置，从而向前跳过一定数量的字符（出错后也可以用这个方法重新扫描字符串的某一部分）。不过通常来说，你要么想跳过属于某个特定字符集的字符，要么想扫描并越过某个特定字符串，要么想一直扫描到某个特定字符串为止。

你可以用 [setCharactersToBeSkipped:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setCharactersToBeSkipped:) 方法为扫描器配置一个跳过字符集。在任何一次扫描操作的开头，扫描器都会忽略这些应被跳过的字符。但一旦它找到了可扫描的字符，就会把所有符合请求的字符都纳入进来。扫描器默认跳过空白字符和换行符。注意，跳过字符集始终是区分大小写的。例如，要跳过所有英文元音字母，你必须把跳过字符集设置为字符串“AEIOUaeiou”中的那些字符。

如果你想从当前位置一直读取到某个特定字符串为止，可以使用 [scanUpToString:intoString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanUpToString:intoString:)（如果你只是想跳过中间这些字符，第二个参数可以传 `NULL`）。例如，给定下面这个字符串：

```
137 small cases of bananas
```

你可以像下面的例子那样，用 [scanUpToString:intoString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/scanUpToString:intoString:) 找出容器的类型和数量。

```objc
NSString *bananas = @"137 small cases of bananas";
NSString *separatorString = @" of";

NSScanner *aScanner = [NSScanner scannerWithString:bananas];

NSInteger anInteger;
[aScanner scanInteger:&anInteger];
NSString *container;
[aScanner scanUpToString:separatorString intoString:&container];
```

需要特别注意的是，这里的搜索字符串（`separatorString`）是 `" of"`。扫描器默认会忽略空白字符，所以整数后面的那个空格被忽略了。但一旦扫描器开始积累字符，在到达搜索字符串之前的所有字符都会被加入输出字符串。因此，如果搜索字符串是 `"of"`（前面没有空格），`container` 的第一个值就是“small cases ”（包含后面那个空格）；如果搜索字符串是 `" of"`（前面带一个空格），`container` 的第一个值就是“small cases”（后面不带空格）。

在一直扫描到某个字符串之后，扫描位置就停在该字符串的开头。因此，如果你想越过这个字符串继续扫描，就必须先把你刚才扫描到的那个字符串本身扫描掉。下面的代码片段演示了如何在上例中跳过搜索字符串，并确定容器中产品的类型。注意这里用 [substringFromIndex:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSStringClassCluster/Description.html#//apple_ref/occ/instm/NSString/substringFromIndex:) 达到了一直扫描到字符串末尾的效果。

```objc
[aScanner scanString:separatorString intoString:NULL];
NSString *product;
product = [[aScanner string] substringFromIndex:[aScanner scanLocation]];
// 也可以写成：
// product = [bananas substringFromIndex:[aScanner scanLocation]];
```


假设你有一个字符串，其中包含这样几行：

- Product: Acme Potato Peeler; Cost: 0.98 73
- Product: Chef Pierre Pasta Fork; Cost: 0.75 19
- Product: Chef Pierre Colander; Cost: 1.27 2

下面的例子交替使用多种扫描操作来提取产品名称和价格（为简单起见，价格按 `float` 读取），并跳过预期中的子串“Product:”和“Cost:”以及分号。注意，由于扫描器默认会跳过空白字符和换行符，循环中并没有对它们做任何特殊处理（尤其是，取最后那个整数时不需要再额外处理空白字符）。

```objc
NSString *string = @"Product: Acme Potato Peeler; Cost: 0.98 73\n\
Product: Chef Pierre Pasta Fork; Cost: 0.75 19\n\
Product: Chef Pierre Colander; Cost: 1.27 2\n";

NSCharacterSet *semicolonSet;
NSScanner *theScanner;

NSString *PRODUCT = @"Product:";
NSString *COST = @"Cost:";

NSString *productName;
float productCost;
NSInteger productSold;

semicolonSet = [NSCharacterSet characterSetWithCharactersInString:@";"];
theScanner = [NSScanner scannerWithString:string];

while ([theScanner isAtEnd] == NO)
{
    if ([theScanner scanString:PRODUCT intoString:NULL] &&
        [theScanner scanUpToCharactersFromSet:semicolonSet
            intoString:&productName] &&
        [theScanner scanString:@";" intoString:NULL] &&
        [theScanner scanString:COST intoString:NULL] &&
        [theScanner scanFloat:&productCost] &&
        [theScanner scanInteger:&productSold])
    {
        NSLog(@"Sales of %@: $%1.2f", productName, productCost * productSold);
    }
}
```


扫描器的部分扫描行为取决于 [locale](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Internationalization.html#//apple_ref/doc/uid/TP40008195-CH23)，它规定了语言以及值表示形式的惯例。`NSScanner` 只使用 locale 中对小数分隔符的定义（由名为 `NSDecimalSeparator` 的键给出）。你可以用 [localizedScannerWithString:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/clm/NSScanner/localizedScannerWithString:) 创建一个使用用户 locale 的扫描器，也可以用 [setLocale:](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/Frameworks/ObjC/Foundation/Classes/NSScannerClassCluster/Description.html#//apple_ref/occ/instm/NSScanner/setLocale:) 显式设置 locale。如果你使用的方法没有指定 locale，扫描器就采用默认的 locale 值。

[下一页](String%20Representations%20of%20File%20Paths.md)[上一页](Character%20Sets.md)

