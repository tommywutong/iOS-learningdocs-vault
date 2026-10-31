---
title: 'appendInterpolation(_:format:align:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:)-8kli1'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:align:privacy:)-8kli1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aalign%3Aprivacy%3A%29-8kli1.json'
content_hash: 'sha256:978477cee83c8786'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:align:privacy:)

<sub>实例方法</sub>

追加一个插值的整数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ number: @autoclosure @escaping () -> Int, format: OSLogIntegerFormatting = .decimal, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

## 参数

- `number` — 要添加到消息中的整数值。

- `format` — 要应用到整数值的格式。你可以将整数格式化为十进制、十六进制或八进制值。如果不指定此参数，默认格式使用十进制值。更多信息参见 [OSLogIntegerFormatting](../oslogintegerformatting.md)。

- `align` — 要应用到该值的对齐方式。使用此参数可指定包含数据的列宽，以及数据在该列内的对齐方式。如果不指定此参数，系统不会对该值进行对齐。

- `privacy` — 信息的隐私级别。如果不指定此参数，系统使用默认规则来决定是否显示该信息。

## 讨论

不要直接调用此函数。对此类型的值进行插值时，系统会自动调用它。在字符串中指定该值时，你可以加入任意所示参数，以更改该值的默认呈现方式。

## 另请参阅

### 追加有符号整数

- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-5ihzf.md>) — 追加一个插值的 8 位整数。
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-190d0.md>) — 追加一个插值的 16 位整数。
- [appendInterpolation(_:format:privacy:)](<appendinterpolation(__format_privacy_)-3ji02.md>) — 追加一个插值的 32 位整数。
- [appendInterpolation(_:format:privacy:attributes:)](<appendinterpolation(__format_privacy_attributes_)-4i2ir.md>) — 追加一个带指定属性的插值 32 位整数。
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-2sb1i.md>) — 追加一个带指定对齐方式的插值 32 位整数。
- [appendInterpolation(_:format:align:privacy:)](<appendinterpolation(__format_align_privacy_)-802m9.md>) — 追加一个插值的 64 位整数。
