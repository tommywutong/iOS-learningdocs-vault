---
title: 属性字符串编程指南
apple_id: 10000036i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2014-02-11'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AttributedStrings/Tasks/AccessingAttrs.html
archived_at: '2026-07-15T05:25:51.368107Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [属性字符串编程指南](Introduction%20to%20Attributed%20String%20Programming%20Guide.md)


[下一页](Changing%20an%20Attributed%20String.md)[上一页](Creating%20Attributed%20Strings%20in%20Cocoa.md)

# 访问属性

属性字符串通过名称来标识属性，将值存储在一个 `NSDictionary` 对象中的属性名下，而该字典又与一个 `NSRange` 相关联，用以指明字典中的属性所适用的字符范围。除标准属性外，你还可以为一段字符范围指定任意你希望的属性名值对。

对于不可变的属性字符串，需要在创建字符串时就指定所有属性。在 Java 中使用构造函数；在 Objective-C 中，则使用诸如 `initWithString:attributes:` 之类的方法来显式传入包含名值对的 `NSDictionary` 对象，或使用不指定任何属性的 `initWithString:` 方法。此外，Application Kit 对 `NSAttributedString` 的扩展还添加了可接受 RTF 文件或 HTML 文件的方法。关于如何使用可变属性字符串设置属性的信息，请参阅[更改属性字符串](Changing%20an%20Attributed%20String.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqge3delkcijbuer2dirdq)。

要从任一类型的属性字符串中获取属性值，可使用以下任一方法：

- `attributesAtIndex:effectiveRange:`
- `attributesAtIndex:longestEffectiveRange:inRange:`
- `attribute:atIndex:effectiveRange:`
- `attribute:atIndex:longestEffectiveRange:inRange:`
- `fontAttributesInRange:`
- `rulerAttributesInRange:`

前两个方法返回给定索引处的所有属性，`attribute:...` 系列方法则返回单个指定属性的值。Application Kit 对 `NSAttributedString` 的扩展还添加了 `fontAttributesInRange:` 和 `rulerAttributesInRange:`，二者分别返回仅适用于字符或整段的属性。

前四个方法还会以引用方式返回属性的有效范围（effective range）和最长有效范围（longest effective range）。这些范围可以帮助你确定属性的作用范围。从概念上讲，属性字符串中的每个字符都有各自独立的一组属性；但通常了解一系列连续字符是否具有相同的属性和值会很有用，这样例程就可以以大于单个字符的块来遍历属性字符串。在获取有效范围时，属性字符串只是在其属性映射表（本质上就是给定索引处所适用属性的字典）中查找信息。而在获取最长有效范围时，属性字符串会继续检查超出该基本范围之外的字符，只要属性值保持相同就会一直检查下去。这种额外的比较会增加这些方法的执行时间，但可以保证获得所请求属性的精确最大范围。

以引用方式返回有效范围的方法，并不保证返回属性所适用的最大范围；它们只保证返回属性适用的某个范围。实际上，它们会返回属性字符串内部存储机制中可直接获取到的任意范围，具体取决于实现方式以及属性字符串被修改的确切历史。

另一方面，以引用方式返回最长有效范围的方法，则保证返回包含指定索引、且所涉及属性适用的最长范围（受传入的 `inRange:` 参数值的约束）。出于效率考虑，`inRange:` 参数应尽可能小，只需覆盖调用者关心的范围即可。

当你按属性范围遍历属性字符串时，具体使用哪种方法取决于具体情况。如果需要对每个范围执行一些处理，并且你知道最终必须处理某个属性的完整范围，那么使用最长有效范围的方法可能会更高效，因为这样就不必分段处理该范围。但是，使用最长有效范围方法时应当谨慎，因为如果不限制 `inRange:` 参数，最长有效范围可能会相当长——甚至可能是整个文档的长度。

下面的 Objective-C 代码片段展示了如何基于有效范围以分块方式遍历属性字符串。这里虚构的 analyzer 对象用于统计每种字体下的字符数。只要获取到的有效范围尚未到达属性字符串的末尾，while 循环就会继续执行，每次获取紧接在上一次获取范围之后生效的字体。每获取到一个字体属性，analyzer 就会统计该有效范围内的字符数。在此示例中，连续调用 `attribute:atIndex:effectiveRange:` 有可能返回相同的值。

```objc
NSAttributedString *attrStr;
unsigned int length;
NSRange effectiveRange;
id attributeValue;

length = [attrStr length];
effectiveRange = NSMakeRange(0, 0);

while (NSMaxRange(effectiveRange) < length) {
    attributeValue = [attrStr attribute:NSFontAttributeName
        atIndex:NSMaxRange(effectiveRange) effectiveRange:&effectiveRange];
    [analyzer tallyCharacterRange:effectiveRange font:attributeValue];
}
```

相比之下，下一个 Objective-C 代码片段则依据每种字体的最大有效范围来遍历属性字符串。在这个例子中，analyzer 统计的是字体变化次数，而这一信息未必能仅通过获取有效范围来体现。在这个例子中，while 循环的条件取决于限制范围（limiting range）的长度，该范围最初为整个属性字符串的长度，并随着循环的进行逐渐缩小。在 analyzer 记录下字体变化之后，限制范围会根据所获取的最长有效范围进行相应调整。

```objc
NSAttributedString *attrStr;
NSRange limitRange;
NSRange effectiveRange;
id attributeValue;

limitRange = NSMakeRange(0, [attrStr length]);

while (limitRange.length > 0) {
    attributeValue = [attrStr attribute:NSFontAttributeName
        atIndex:limitRange.location longestEffectiveRange:&effectiveRange
        inRange:limitRange];
    [analyzer recordFontChange:attributeValue];
    limitRange = NSMakeRange(NSMaxRange(effectiveRange),
        NSMaxRange(limitRange) - NSMaxRange(effectiveRange));
}
```

请注意，第二个代码片段更加复杂。正因如此，加之 `attribute:atIndex:longestEffectiveRange:inRange:` 比 `attribute:atIndex:effectiveRange:` 稍慢，通常应仅在你所执行的工作确实需要时才使用它。在大多数情况下，按有效范围操作就已足够。

[下一页](Changing%20an%20Attributed%20String.md)[上一页](Creating%20Attributed%20Strings%20in%20Cocoa.md)

