---
title: 'appendInterpolation(_:format:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:)-686xc'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:format:privacy:)-686xc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aformat%3Aprivacy%3A%29-686xc.json'
content_hash: 'sha256:b9905e3e449ada93'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:format:privacy:)

<sub>实例方法</sub>

向消息添加一个布尔参数。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ boolean: @autoclosure @escaping () -> Bool, format: OSLogBoolFormat = .truth, privacy: OSLogPrivacy = .auto)
```

## 参数

- `boolean` — 要添加到消息中的布尔值。

- `format` — 要应用到布尔值的格式。你可以将布尔值格式化为 true/false 或 yes/no 字符串。如果不指定此参数，默认格式使用 true/false 字符串。更多信息参见 [OSLogBoolFormat](../oslogboolformat.md)。

- `privacy` — 信息的隐私级别。如果不指定此参数，系统使用默认规则来决定是否显示该信息。

## 讨论

不要直接调用此函数。对此类型的值进行插值时，系统会自动调用它。在字符串中指定该值时，你可以加入任意所示参数，以更改该值的默认呈现方式。
