---
title: OSLogInt32ExtendedFormat.answer
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogint32extendedformat/answer
source_url: 'https://developer.apple.com/documentation/os/oslogint32extendedformat/answer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogint32extendedformat/answer.json'
content_hash: 'sha256:ce04a0e06d14f6e7'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md)

# OSLogInt32ExtendedFormat.answer

<sub>Case</sub>

将 32 位整数显示为 yes 或 no 的格式。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case answer
```

## 讨论

使用此选项可将插值格式化为 `YES` 或 `NO`。格式化器会把所有正的和负的非零值转换为 `YES`，仅把零转换为 `NO`。下面的示例将 answer 格式化器应用于 32 位整数值 `0`：

```swift
// 使用指定的子系统和分类创建一个 logger。
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// 指定要插值的值。
let value: Int32 = 0
                
// 使用指定格式将该值写入日志。
logger.info(".answer output is \(value, format: .answer)")
```

系统会把以下消息写入日志：

```
[Formatter Output] .answer output is NO
```

## 另请参阅

### 获取格式

- [OSLogInt32ExtendedFormat.ipv4Address](ipv4address.md) — 将 32 位整数显示为 IPv4 地址的格式。
- [OSLogInt32ExtendedFormat.secondsSince1970](secondssince1970.md) — 将 32 位整数显示为日期的格式。
- [OSLogInt32ExtendedFormat.darwinErrno](darwinerrno.md) — 将 32 位整数显示为 Darwin 错误号的格式。
- [OSLogInt32ExtendedFormat.darwinMode](darwinmode.md) — 将 32 位整数显示为 Darwin 文件模式的格式。
- [OSLogInt32ExtendedFormat.darwinSignal](darwinsignal.md) — 将 32 位整数显示为 Darwin 信号的格式。
- [OSLogInt32ExtendedFormat.bitrate](bitrate.md) — 将 32 位整数显示为比特率的格式。
- [OSLogInt32ExtendedFormat.bitrateIEC](bitrateiec.md) — 将 32 位整数显示为 IEC 比特率的格式。
- [OSLogInt32ExtendedFormat.byteCount](bytecount.md) — 将 32 位整数显示为字节的格式。
- [OSLogInt32ExtendedFormat.byteCountIEC](bytecountiec.md) — 将 32 位整数显示为 IEC 字节的格式。
- [OSLogInt32ExtendedFormat.truth](truth.md) — 将 32 位整数显示为 true 或 false 的格式。
