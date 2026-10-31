---
title: 'appendInterpolation(_:align:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-8hwmt'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:)-8hwmt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aalign%3Aprivacy%3A%29-8hwmt.json'
content_hash: 'sha256:cb5d7efba2ea2066'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:align:privacy:)

<sub>实例方法</sub>

追加一个插值类型描述。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ value: @autoclosure @escaping () -> any Any.Type, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto)
```

## 参数

- `value` — 一个 Swift 类型。

- `align` — 应用于类型名称的对齐方式。使用此参数指定包含该名称的列宽，以及名称在该列内的对齐方式。如果不指定此参数，系统不会对齐该值。

- `privacy` — 信息的隐私级别。如果不指定此参数，系统使用默认规则来决定是否显示该信息。

## 讨论

不要直接调用此函数。系统在插值此类型的值时会自动调用它。在字符串中指定该值时，你可以包含任意所示参数，以更改该值的默认呈现方式。

## 另请参阅

### 追加泛型类型

- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-84m60.md>) — 追加某个类型的插值文本表示。
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-xyum.md>) — 使用指定属性追加某个类型的插值文本表示。
- [appendInterpolation(_:format:align:privacy:attributes:)](<appendinterpolation(__format_align_privacy_attributes_)-8107a.md>) — 使用指定属性追加一个插值数值类型。
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-9hehv.md>) — 使用指定属性追加一个插值类型描述。
