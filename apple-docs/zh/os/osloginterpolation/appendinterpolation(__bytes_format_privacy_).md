---
title: 'appendInterpolation(_:bytes:format:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:bytes:format:privacy:)'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:bytes:format:privacy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Abytes%3Aformat%3Aprivacy%3A%29.json'
content_hash: 'sha256:d74c25f47515cac9'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:bytes:format:privacy:)

<sub>实例方法</sub>

追加插值的指针数据。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ pointer: @autoclosure @escaping () -> UnsafeRawPointer, bytes: @autoclosure @escaping () -> Int, format: OSLogPointerFormat = .none, privacy: OSLogPrivacy = .auto)
```

## 参数

- `pointer` — 其内容要添加到消息中的指针。

- `bytes` — 指针数据中的字节数。

- `format` — 要应用到指针的格式。你可以将指针格式化为若干不同选项之一。如果不指定此参数，系统不会格式化该值。更多信息参见 [OSLogPointerFormat](../oslogpointerformat.md)。

- `privacy` — 信息的隐私级别。如果不指定此参数，系统使用默认规则来决定是否显示该信息。

## 讨论

不要直接调用此函数。对此类型的值进行插值时，系统会自动调用它。在字符串中指定该值时，你可以加入任意所示参数，以更改该值的默认呈现方式。

## 另请参阅

### 追加指针数据

- [appendInterpolation(_:bytes:format:privacy:attributes:)](<appendinterpolation(__bytes_format_privacy_attributes_).md>) — 追加带指定属性的插值指针数据。
- [appendInterpolation(_:format:privacy:)](<appendinterpolation(__format_privacy_)-5qaau.md>) — 追加一个插值的原始字节集合。
- [appendInterpolation(_:format:privacy:attributes:)](<appendinterpolation(__format_privacy_attributes_)-93lbs.md>) — 追加一个带指定属性的插值原始字节集合。
