---
title: 归档与序列化编程指南
apple_id: 10000047i
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Data Management
technology: Foundation
published: '2012-07-17'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Articles/subclassing.html
archived_at: '2026-07-15T05:25:45.175951Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [归档与序列化编程指南](Introduction.md)


[下一页](Serializing%20Property%20Lists.md)[上一页](Forward%20and%20Backward%20Compatibility%20for%20Keyed%20Archives.md)

# NSCoder 子类化

`NSCoder` 的接口相当通用且广泛，声明了用于编码和解码带键和不带键的对象及值的方法。具体子类不要求恰当地实现 `NSCoder` 的所有方法，可以显式地将自身限定为只支持某些类型的操作。例如，`NSArchiver` 没有实现 `decode...` 方法，而 `NSUnarchiver` 没有实现 `encode...` 方法。此外，这两个类都没有实现用于编码和解码键控归档的键控编码方法。对 `NSArchiver` 调用 `decode` 方法，或对 `NSUnarchiver` 调用 `encode` 方法，都会抛出 `NSInvalidArgumentException`。

如果你定义了一个不支持键控编码的 `NSCoder` 子类，你的子类至少必须重写以下方法：

- `encodeValueOfObjCType:at:`
- `decodeValueOfObjCType:at:`
- `encodeDataObject:`
- `decodeDataObject`
- `versionForClassName:`

如果你的子类支持键控编码，除了上述方法外，你还必须重写 `allowsKeyedCoding` 方法（使其返回 `YES`），以及 `NSCoder` 定义的所有键控编码方法。在这两种情况下，如果你为编码和解码分别创建了独立的类，则不需要在解码器类中重写编码方法，也不需要在编码器类中重写解码方法。

请注意，`encodeObject:` 和 `decodeObject` 不属于基本方法之列。它们被抽象地定义为使用 Objective-C 类型码 “@” 调用 `encodeValueOfObjCType:at:` 或 `decodeValueOfObjCType:at:`。你对后两个方法的实现必须处理这种情况，在编码对象之前和解码对象之后，调用该对象的 `encodeWithCoder:` 或 `initWithCoder:` 方法，并向该对象发送适当的替换消息（如 [Making Substitutions During Coding](Encoding%20and%20Decoding%20Objects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dqljzg4ydomq) 中所述）。

你的子类可以重写其他方法，为特定情况提供专门的处理。具体来说，你可以实现以下任意方法：

- `encodeRootObject:`
- `encodeConditionalObject:`
- `encodeBycopyObject:`
- `encodeByrefObject:`

有关这些方法所需行为的更多信息，请参阅各个方法的说明。`NSCoder` 对这些方法的默认实现只是简单地调用 `encodeObject:`。

如果你重写 `encodeConditionalObject:` 以支持条件对象（参见 [Conditional Objects](Archives.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqhe2dmljrgqzdemby)），请注意，首次无条件编码可能会发生在任意数量的条件编码请求之后，因此你的编码器在所有其他对象都编码完成之前，无法确定哪些条件对象需要被编码。

对于对象来说，被编码的对象要对自身的编码全权负责。不过，有几个类会把这一职责交还给编码器对象，原因可能是出于性能考虑，也可能是因为正确的支持需要比对象自身所掌握的更多信息。Foundation 中值得注意的、这样做的类是 `NSData` 和 `NSPort`。由于 `NSData` 的底层特性，优化对它来说十分重要。因此，`NSData` 对象在收到 `encodeWithCoder:` 和 `initWithCoder:` 消息时，总是会要求其编码器使用 `encodeDataObject:` 和 `decodeDataObject` 方法直接处理其内容。类似地，`NSPort` 对象会要求其编码器使用 `encodePortObject:` 和 `decodePortObject` 方法（仅由 `NSPortCoder` 实现）来处理自身。这是因为 `NSPort` 表示的是保存在操作系统本身中的信息，向另一个进程传输时需要特殊处理。

这些特殊情况不会影响编码器对象的使用者，因为这种重定向是由类自身在其 `NSCoding` 协议方法中处理的。不过，具体编码器子类的实现者，必须自行实现适当的自定义方法来编码和解码 `NSData`（以及在相关情况下的 `NSPort`）对象。

[下一页](Serializing%20Property%20Lists.md)[上一页](Forward%20and%20Backward%20Compatibility%20for%20Keyed%20Archives.md)
