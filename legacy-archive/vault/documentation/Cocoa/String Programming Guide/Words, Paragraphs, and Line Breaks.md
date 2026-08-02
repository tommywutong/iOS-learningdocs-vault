---
title: 字符串编程指南
apple_id: 10000035i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/stringsParagraphBreaks.html
archived_at: '2026-07-15T07:19:34.688911Z'
---
> 导航：[总目录](../../../README.md) · [文档](../../../_indexes/documentation.md) · [字符串编程指南](Introduction%20to%20String%20Programming%20Guide.md)


[下一页](Characters%20and%20Grapheme%20Clusters.md)[上一页](Searching%2C%20Comparing%2C%20and%20Sorting%20Strings.md)

# 词、段落与换行

本文介绍词边界和段落边界是如何定义的、换行是如何表示的，以及如何按段落切分字符串。

文本系统按照 [Unicode Standard Annex #29](http://www.unicode.org/reports/tr29/#Word_Boundaries) 以语言相关的方式确定词边界，并按该文档所述针对 locale 做了额外定制。在 OS X 上，Cocoa 提供了与词边界相关的 API，例如 `NSAttributedString` 的 [doubleClickAtIndex:](https://developer.apple.com/documentation/foundation/nsattributedstring/1534748-doubleclickatindex) 和 [nextWordFromIndex:forward:](https://developer.apple.com/documentation/foundation/nsattributedstring/1535305-nextwordfromindex) 方法，但你无法修改词边界算法本身的工作方式。

换行或段落分隔可以有多种表示方式。历史上曾使用过 `\n`、`\r` 和 `\r\n`。Unicode 定义了一个含义明确的段落分隔符 `U+2029`（Cocoa 为其提供了常量 `NSParagraphSeparatorCharacter`），以及一个含义明确的行分隔符 `U+2028`（Cocoa 为其提供了常量 `NSLineSeparatorCharacter`）。

在 Cocoa 文本系统中，`NSParagraphSeparatorCharacter` 始终被当作段落分隔处理，而 `NSLineSeparatorCharacter` 始终被当作换行处理，且不是段落分隔——也就是段落内部的换行。然而在其他环境中，这些字符会被如何处理几乎没有保证。例如，POSIX 层面的软件通常只把 `\n` 识别为分隔符。某些较早的 Macintosh 软件只识别 `\r`，某些 Windows 软件只识别 `\r\n`。而且往往并不区分换行与段落分隔。

该使用哪种换行或段落分隔字符，取决于你的数据将被如何使用，以及会在哪些平台上使用。Cocoa 文本系统把 `\n`、`\r` 和 `\r\n` 全部识别为段落分隔——等价于 `NSParagraphSeparatorCharacter`。当它插入段落分隔时（例如通过 `insertNewline:`），使用的是 `\n`。通常 `NSLineSeparatorCharacter` 只用于那些明确属于换行而非段落分隔的场合，例如 `insertLineBreak:`，或者用于表示 HTML 的 `<br>` 元素。

如果你的分隔明确是换行而不是段落分隔，那么通常应当使用 `NSLineSeparatorCharacter`。否则，你可以根据可能处理你文本的其他软件来选择 `\n`、`\r` 或 `\r\n`。Cocoa 的默认选择通常是 `\n`。

要“按段落”切分字符串，一种常见做法就是直接这样写：

```objc
NSArray *arr = [myString componentsSeparatedByString:@"\n"];
```

但这种做法忽略了一个事实：字符串中的段落分隔或换行还可能有其他多种表示方式——`\r`、`\r\n`，或者 Unicode 分隔符。

你应该改用那些会考虑各种可能行结束符的方法——例如 [enumerateSubstringsInRange:options:usingBlock:](https://developer.apple.com/documentation/foundation/nsstring/1416774-enumeratesubstringsinrange) 和 [enumerateLinesUsingBlock:](https://developer.apple.com/documentation/foundation/nsstring/1408459-enumeratelinesusingblock)——如下例所示。

```objc
NSString *string = /* 假设它已经存在 */;
NSRange range = NSMakeRange(0, string.length);
[string enumerateSubstringsInRange:range
                           options:NSStringEnumerationByParagraphs
                        usingBlock:^(NSString * _Nullable paragraph, NSRange paragraphRange, NSRange enclosingRange, BOOL * _Nonnull stop) {             // ... }];
```

[下一页](Characters%20and%20Grapheme%20Clusters.md)[上一页](Searching%2C%20Comparing%2C%20and%20Sorting%20Strings.md)

