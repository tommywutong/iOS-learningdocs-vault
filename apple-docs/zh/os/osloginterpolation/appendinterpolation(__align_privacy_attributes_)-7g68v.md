---
title: 'appendInterpolation(_:align:privacy:attributes:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-7g68v'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-7g68v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aalign%3Aprivacy%3Aattributes%3A%29-7g68v.json'
content_hash: 'sha256:441f58963f13b83c'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:align:privacy:attributes:)

<sub>实例方法</sub>

使用指定属性追加一个插值字符串。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ argumentString: @autoclosure @escaping () -> String, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

## 参数

- `argumentString` — 插值字符串。系统会自动将此值包装在闭包中。

- `align` — 系统在日志消息中呈现该值时使用的对齐方式和最小列数。更多信息参见 [OSLogStringAlignment](../oslogstringalignment.md)。默认值是 [none](../oslogstringalignment/none.md)。

- `privacy` — 该值的隐私级别，系统在日志消息中呈现该值时会应用此级别。更多信息参见 [OSLogPrivacy](../oslogprivacy.md)。默认值是 [auto](../oslogprivacy/auto.md)。

- `attributes` — 关于该值的附加信息。处理日志消息的工具会解释这些属性，你通常以键值对形式提供。例如，Instruments 会处理你嵌入在该值中的任何工程类型。更多信息参见 [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31)。

## 讨论

> [!important] 重要
> 不要直接调用此方法。相反，当你向日志消息追加插值字符串时，框架会自动调用它。

## 另请参阅

### 追加字符串

- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-6tazr.md>) — 追加一个插值字符串。
