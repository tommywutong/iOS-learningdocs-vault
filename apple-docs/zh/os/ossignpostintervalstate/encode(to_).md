---
title: 'encode(to:)'
framework: os
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostintervalstate/encode(to:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate/encode(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate/encode%28to%3A%29.json'
content_hash: 'sha256:77889492aad172c5'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignpostIntervalState](../ossignpostintervalstate.md)

# encode(to:)

<sub>实例方法</sub>

将时间区间状态编码到所提供的编码器中。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode(to encoder: any Encoder) throws
```

## 参数

- `encoder` — 要写入数据的编码器。

## 讨论

> [!important] 重要
> 你不会直接调用此方法。相反，你用来编码时间区间状态的对象（必须遵循 [Encoder](../../swift/encoder.md) 协议）会在序列化过程中代表你调用它。

如果时间区间状态对该指定编码器的格式无效，此方法会抛出错误。
