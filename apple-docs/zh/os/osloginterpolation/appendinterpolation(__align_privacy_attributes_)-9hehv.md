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
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-9hehv'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:align:privacy:attributes:)-9hehv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aalign%3Aprivacy%3Aattributes%3A%29-9hehv.json'
content_hash: 'sha256:2c0ca35951896acb'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:align:privacy:attributes:)

<sub>实例方法</sub>

使用指定属性追加一个插值类型描述。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ value: @autoclosure @escaping () -> any Any.Type, align: OSLogStringAlignment = .none, privacy: OSLogPrivacy = .auto, attributes: String)
```

## 参数

- `value` — 插值类型，系统会自动将其包装在闭包中。类型本身不会出现在日志消息中。相反，系统会纳入该类型的描述。

- `align` — 系统在日志消息中呈现该值时使用的对齐方式和最小列数。更多信息参见 [OSLogStringAlignment](../oslogstringalignment.md)。默认值是 [none](../oslogstringalignment/none.md)。

- `privacy` — 该值的隐私级别，系统在日志消息中呈现该值时会应用此级别。更多信息参见 [OSLogPrivacy](../oslogprivacy.md)。默认值是 [auto](../oslogprivacy/auto.md)。

- `attributes` — 关于该值的附加信息。处理日志消息的工具会解释这些属性，你通常以键值对形式提供。例如，Instruments 会处理你嵌入在该值中的任何工程类型。更多信息参见 [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31)。

## 讨论

> [!important] 重要
> 不要直接调用此方法。相反，当你向日志消息追加插值类型描述时，框架会自动调用它。

## 另请参阅

### 追加泛型类型

- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-84m60.md>) — 追加某个类型的插值文本表示。
- [appendInterpolation(_:align:privacy:attributes:)](<appendinterpolation(__align_privacy_attributes_)-xyum.md>) — 使用指定属性追加某个类型的插值文本表示。
- [appendInterpolation(_:format:align:privacy:attributes:)](<appendinterpolation(__format_align_privacy_attributes_)-8107a.md>) — 使用指定属性追加一个插值数值类型。
- [appendInterpolation(_:align:privacy:)](<appendinterpolation(__align_privacy_)-8hwmt.md>) — 追加一个插值类型描述。
