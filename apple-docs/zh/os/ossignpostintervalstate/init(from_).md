---
title: 'init(from:)'
framework: os
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/os/ossignpostintervalstate/init(from:)'
source_url: 'https://developer.apple.com/documentation/os/ossignpostintervalstate/init(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/ossignpostintervalstate/init%28from%3A%29.json'
content_hash: 'sha256:5034d53c08623bae'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSSignpostIntervalState](../ossignpostintervalstate.md)

# init(from:)

<sub>初始化方法</sub>

从所提供的解码器中解码时间区间状态。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
required init(from decoder: any Decoder) throws
```

## 参数

- `decoder` — 要从中读取数据的解码器。

## 讨论

> [!important] 重要
> 你不会直接调用此方法。相反，你用来解码时间区间状态的对象（必须遵循 [Decoder](../../swift/decoder.md) 协议）会在序列化过程中代表你调用它。

如果从解码器读取失败，或者解码器的数据已损坏或无效，此初始化方法会抛出错误。
