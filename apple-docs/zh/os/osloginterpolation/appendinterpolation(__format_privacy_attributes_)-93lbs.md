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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:attributes:)-93lbs'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aprivacy%3Aattributes%3A%29-93lbs.json'
content_hash: 'sha256:779046553b44d591'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:privacy:attributes:)

<sub>实例方法</sub>

追加一个带指定属性的插值原始字节集合。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ pointer: @autoclosure @escaping () -> UnsafeRawBufferPointer, format: OSLogPointerFormat = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

## 参数

- `pointer` — 插值的原始字节集合。系统会自动将此值包装在闭包中。

- `format` — 系统在日志消息中呈现该值时要应用的格式。更多信息参见 [OSLogPointerFormat](../oslogpointerformat.md)。默认值是 [OSLogPointerFormat.none](../oslogpointerformat/none.md)。

- `privacy` — 该值的隐私级别，系统在日志消息中呈现该值时会应用此级别。更多信息参见 [OSLogPrivacy](../oslogprivacy.md)。默认值是 [auto](../oslogprivacy/auto.md)。

- `attributes` — 关于该值的附加信息。处理日志消息的工具会解释这些属性，你通常以键值对形式提供。例如，Instruments 会处理你嵌入在该值中的任何工程类型。更多信息参见 [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31)。

## 讨论

> [!important] 重要
> 不要直接调用此方法。相反，当你向日志消息追加一个插值的原始字节集合时，框架会自动调用它。

## 另请参阅

### 追加指针数据

- [appendInterpolation(_:bytes:format:privacy:)](<appendinterpolation(__bytes_format_privacy_).md>) — 追加插值的指针数据。
- [appendInterpolation(_:bytes:format:privacy:attributes:)](<appendinterpolation(__bytes_format_privacy_attributes_).md>) — 追加带指定属性的插值指针数据。
- [appendInterpolation(_:format:privacy:)](<appendinterpolation(__format_privacy_)-5qaau.md>) — 追加一个插值的原始字节集合。
