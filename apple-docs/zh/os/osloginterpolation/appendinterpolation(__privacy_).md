---
title: 'appendInterpolation(_:privacy:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/osloginterpolation/appendinterpolation(_:privacy:)'
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation/appendinterpolation(_:privacy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation/appendinterpolation%28_%3Aprivacy%3A%29.json'
content_hash: 'sha256:76ff40f36f85b831'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInterpolation](../osloginterpolation.md)

# appendInterpolation(_:privacy:)

<sub>实例方法</sub>

追加一个插值的对象描述。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func appendInterpolation(_ argumentObject: @autoclosure @escaping () -> NSObject, privacy: OSLogPrivacy = .auto)
```

## 参数

- `argumentObject` — 你想将其描述添加到消息中的对象。此函数会调用该对象的 [description](../../objectivec/nsobjectprotocol/description.md) 方法，并将该值并入消息字符串。

- `privacy` — 信息的隐私级别。如果不指定此参数，默认规则会隐去对象描述。

## 讨论

不要直接调用此函数。对此类型的值进行插值时，系统会自动调用它。在字符串中指定该值时，你可以加入任意所示参数，以更改该值的默认呈现方式。

## 另请参阅

### 追加对象

- [appendInterpolation(_:privacy:attributes:)](<appendinterpolation(__privacy_attributes_)-3czd2.md>) — 追加一个带指定属性的插值对象描述。
