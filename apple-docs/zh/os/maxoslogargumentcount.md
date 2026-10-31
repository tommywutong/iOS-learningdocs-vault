---
title: maxOSLogArgumentCount
framework: os
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/maxoslogargumentcount
source_url: 'https://developer.apple.com/documentation/os/maxoslogargumentcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/maxoslogargumentcount.json'
content_hash: 'sha256:0372fcbbcb7c0120'
translated: true
---

> 导航：[Technologies](../technologies.md) · [os](../os.md)

# maxOSLogArgumentCount

<sub>全局变量</sub>

日志消息可包含的插值表达式的最大数量。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var maxOSLogArgumentCount: UInt8 { get }
```

## 讨论

对于包含插值的日志消息，系统会限制单条消息可包含的表达式总数。下面的示例展示了一个包含插值的字符串：

```swift
let fileID = 941
let message = "Created a file with ID \(fileID)"
```

## 另请参阅

### 获取消息详情

- [bufferSize](oslogmessage/buffersize.md) — 日志系统接收到的缓冲区的字节大小。
- [interpolation](oslogmessage/interpolation.md) — 日志消息的字符串插值。
