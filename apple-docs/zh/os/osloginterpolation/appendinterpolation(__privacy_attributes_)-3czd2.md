---
title: 'appendInterpolation(_:privacy:attributes:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:privacy:attributes:)-3czd2'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:privacy:attributes:)-3czd2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aprivacy%3Aattributes%3A%29-3czd2.json'
content_hash: 'sha256:339db309d4028366'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:privacy:attributes:)

<sub>实例方法</sub>

追加一个带指定属性的插值对象描述。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ argumentObject: @autoclosure @escaping () -> NSObject, privacy: OSLogPrivacy = .auto, attributes: String)
```

## 参数

- `argumentObject` — 插值对象，系统会自动将其包装在闭包中。对象本身不会出现在日志消息中。相反，系统会调用该对象的 [description](../../objectivec/nsobjectprotocol/description.md) 方法，并并入其返回的值。

- `privacy` — 插值的隐私级别，系统在日志消息中呈现该值时会应用此级别。更多信息参见 [OSLogPrivacy](../oslogprivacy.md)。默认值是 [auto](../oslogprivacy/auto.md)。

- `attributes` — 关于插值的附加信息。处理日志消息的工具会解释这些属性，你通常以键值对形式提供。例如，Instruments 会处理你嵌入在该值中的任何工程类型。更多信息参见 [Instruments Developer Help](https://help.apple.com/instruments/developer/mac/current/#/devcd5016d31)。

## 讨论

> [!important] 重要
> 不要直接调用此方法。相反，当你向日志消息追加一个插值的对象描述时，框架会自动调用它。

## 另请参阅

### 追加对象

- [appendInterpolation(_:privacy:)](<appendinterpolation(__privacy_).md>) — 追加一个插值的对象描述。
