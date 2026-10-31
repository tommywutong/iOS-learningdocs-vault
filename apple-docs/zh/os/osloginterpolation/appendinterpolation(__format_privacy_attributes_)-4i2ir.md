---
title: 'appendInterpolation(_:format:privacy:attributes:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-4i2ir'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-4i2ir'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aprivacy%3Aattributes%3A%29-4i2ir.json'
content_hash: 'sha256:c5a91f5809ff97f3'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:privacy:attributes:)

<sub>实例方法</sub>

追加一个带指定属性的插值 32 位整数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Int32, format: OSLogInt32ExtendedFormat, privacy: OSLogPrivacy = .auto, attributes: String)
```

## 参数

- `number` — 插值的 32 位整数。系统会自动将此值包装在闭包中。

- `format` — 系统在日志消息中呈现该值时要应用的格式。更多信息参见 [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md)。

- `privacy` — 该值的隐私级别，系统在日志消息中呈现该值时会应用此级别。更多信息参见 [OSLogPrivacy](../oslogprivacy.md)。默认值是 [auto](../oslogprivacy/auto.md)。

- `attributes` — 关于该值的附加信息。处理日志消息的工具会解释这些属性，你通常以键值对形式提供。例如，Instruments 会处理你嵌入在该值中的任何工程类型。更多信息参见 [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31)。

## 讨论

> [!important] 重要
> 不要直接调用此方法。相反，当你向日志消息追加一个插值的 32 位整数时，框架会自动调用它。

## 另请参阅

### 追加有符号整数

- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-8kli1.md>) — 追加一个插值的整数。
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-5ihzf.md>) — 追加一个插值的 8 位整数。
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-190d0.md>) — 追加一个插值的 16 位整数。
- [appendInterpolation(_:format:privacy:)](<appendinterpolation(__format_privacy_)-3ji02.md>) — 追加一个插值的 32 位整数。
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-2sb1i.md>) — 追加一个带指定对齐方式的插值 32 位整数。
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-802m9.md>) — 追加一个插值的 64 位整数。
