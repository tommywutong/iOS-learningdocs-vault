---
title: 归档与序列化编程指南
apple_id: 10000047i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/codingctypes.html
archived_at: '2026-07-15T05:25:41.078010Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [归档与序列化编程指南](Introduction.md)


[下一页](Forward%20and%20Backward%20Compatibility%20for%20Keyed%20Archives.md)[上一页](Encoding%20and%20Decoding%20Objects.md)

# 编码和解码 C 数据类型

`NSKeyedArchiver` 和 `NSKeyedUnarchiver` 提供了大量用于处理非对象数据的方法。整数可以使用 `encodeInt:forKey:`、`encodeInt32:forKey:` 或 `encodeInt64:forKey:` 编码。同样，实数可以使用 `encodeFloat:forKey:` 或 `encodeDouble:forKey:` 编码。其他方法用于编码布尔值和字节数组。这些类还提供了若干便捷方法，用于处理 Cocoa 中使用的特殊数据类型，例如 `NSPoint`、`NSSize` 和 `NSRect`。

`NSKeyedArchiver` 和 `NSKeyedUnarchiver` 并未提供用于编码和解码聚合类型（例如结构体、数组和位域）的方法。以下小节将提供一些处理不受支持的数据类型的建议。

你无法编码一个指针，然后在解码时得到有用的结果。你必须编码该指针所指向的信息。这在非键控编码中同样适用。

指向 C 字符串（`char *`）的指针是一种特殊情况，因为它们可以被视为字节数组，使用 `encodeBytes:length:forKey:` 进行编码。你也可以用一个临时的 `NSString` 对象包装 C 字符串，然后归档该字符串。解码时执行相反的过程。创建 `NSString` 对象时，请务必留意字符串的字符集编码，并选择合适的创建方法。

如果你要编码一个字节数组，只需使用提供的方法即可完成。

对于其他算术类型，可以用该数组创建一个 `NSData` 对象。_请注意，在这种情况下，处理平台的字节序问题是你自己的责任。_ 处理平台字节序通常有两种方式。第一种方法是将数组的元素（或者说，数组的临时副本）逐个转换为规范的字节序（大端或小端），使用 _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_ 中 [Swapping Bytes](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/universal_binary/universal_binary_byte_swap/universal_binary_swap.html#//apple_ref/doc/uid/TP40002217-CH243) 一节所讨论的函数（另请参阅 _Foundation Functions Reference_ 中的 "Byte Ordering"），然后将结果作为缓冲区提供给 `NSData`（或者，你也可以直接用 `encodeBytes:length:forKey:` 写入字节）。解码时，你必须反向执行这一过程，将大端或小端的规范形式转换为当前主机的表示形式。另一种方法是原样使用该数组，并在一个单独的键值（可能是一个布尔值）中记录归档创建时主机的字节序。解码时，读取该字节序键，并将其与当前主机的字节序进行比较，仅在两者不同的情况下才交换数值。

或者，你也可以将数组的每个元素分别以其原生类型归档，也许可以使用受数组语法启发的键名，比如 "theArray[0]"、"theArray[1]" 等等。这不是一种特别高效的技术，但你可以借此忽略字节序问题。

处理 C 对象数组最简单的方法，是使用 `initWithObjects:count:` 将该数组临时包装进一个 `NSArray` 对象，编码这个数组对象，然后再丢弃该对象。因为对象包含其他需要被编码的信息，所以你不能只是把指针数组直接嵌入一个 `NSData` 对象——每个对象都必须单独归档。解码时，对取回的数组使用 `getObjects:`，将对象取出到一个（大小正确的）已分配的 C 数组中。

归档结构体或一组位域的最佳方法，是分别归档各个字段，并为每个字段选择合适的编码/解码方法类型。如果你愿意，键名可以由结构体字段名组成，比如 "theStruct.order"、"theStruct.flags" 等等。这会使归档在一定程度上依赖源代码中字段的名称，而这些名称随着时间推移可能会被重命名，但如果你想保持兼容性，归档所用的键就不能改变。

你不应该用一个 `NSData` 对象包装一个结构体然后直接归档它。如果结构体包含对象或指针字段，data 对象无法正确地对它们进行归档。你还会因此依赖编译器如何决定结构体的内存布局，而这种布局可能在不同版本的编译器之间发生变化，并可能取决于其他因素。编译器并不受限于必须按照你在源代码中指定的方式来组织结构体——例如，字段之间可能存在任意的、不可见的内部填充字节，而这些填充字节的数量可能在没有任何提示的情况下、在不同平台上发生变化。此外，任何宽度为多字节的字段在处理字节序问题时都不会得到正确处理。你会给自己带来各种各样的兼容性麻烦。

同样，位域绝不应该通过将多个位域的原始比特读取为一个整数并编码该整数的方式进行编码。（不过，通过位移和 OR 操作手动从多个位域构造一个整数并对其进行编码，可以避免下文中提到的大部分陷阱。）尽管 C 标准对编译器有一些要求，但编译器在实际如何组织数据、选择将哪些位存储在何处，以及可能选择不使用哪些位（字段间的填充位）方面，仍然拥有一定的自由度。这些位的位置在不同编译器之间，或者随着某个特定编译器的演进，都可能有所不同。除此之外，你还必须处理字节序问题。整数内部比特的顺序，在编码归档的机器和解码归档的机器上可能是不同的。最后，通过编码原始比特，你会限制该类未来的发展，使其必须使用与你需要支持的最旧归档相同的位域大小。否则，你就必须能够自行解析旧的比特流并初始化新的比特流，妥善处理编译器和平台方面的问题。

与对象的实例变量一般情况类似，你并不需要归档结构体或位域的每一个字段。你只需要编码和解码保留结构体状态所必需的字段。那些是计算得出或以其他方式从其他数据派生出来的字段，不应被归档。

更复杂的数据类型，例如聚合体的数组，通常可以使用简单数据类型的技术，再结合针对你特定应用程序的自定义逻辑来处理。

[下一页](Forward%20and%20Backward%20Compatibility%20for%20Keyed%20Archives.md)[上一页](Encoding%20and%20Decoding%20Objects.md)
