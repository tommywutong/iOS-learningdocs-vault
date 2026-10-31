---
title: OSLogInt32ExtendedFormat.secondsSince1970
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogint32extendedformat/secondssince1970
source_url: 'https://developer.apple.com/documentation/os/oslogint32extendedformat/secondssince1970'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogint32extendedformat/secondssince1970.json'
content_hash: 'sha256:33bee4c424666db6'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md)

# OSLogInt32ExtendedFormat.secondsSince1970

<sub>Case</sub>

将 32 位整数显示为日期的格式。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case secondsSince1970
```

## 讨论

使用此选项可将插值格式化为日期和时间，例如 `2007-01-09 09:41:00`。格式化器会把你提供的值视为以秒为单位的时长，并将其加到 UNIX epoch（纪元）上，以计算要显示的日期。UNIX epoch 是一种用自 1970 年 1 月 1 日 00:00:00 UTC 起经过的秒数来描述特定时间点的方法。

下面的示例将 `secondsSince1970` 格式化器应用于 32 位整数值 `604_800`，即整整一周的秒数：

```swift
// 使用指定的子系统和分类创建一个 logger。
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// 指定要插值的值。在本例中，是整整一周的
// 秒数。
let value: Int32 = 604_800
                
// 使用指定格式将该值写入日志。
logger.info(".secondsSince1970 output is \(value, format: .secondsSince1970)")
```

系统会把以下消息写入日志：

```
[Formatter Output] .secondsSince1970 output is 1970-01-08 00:00:00
```

## 另请参阅

### 获取格式

- [OSLogInt32ExtendedFormat.ipv4Address](ipv4address.md) — 将 32 位整数显示为 IPv4 地址的格式。
- [OSLogInt32ExtendedFormat.darwinErrno](darwinerrno.md) — 将 32 位整数显示为 Darwin 错误号的格式。
- [OSLogInt32ExtendedFormat.darwinMode](darwinmode.md) — 将 32 位整数显示为 Darwin 文件模式的格式。
- [OSLogInt32ExtendedFormat.darwinSignal](darwinsignal.md) — 将 32 位整数显示为 Darwin 信号的格式。
- [OSLogInt32ExtendedFormat.bitrate](bitrate.md) — 将 32 位整数显示为比特率的格式。
- [OSLogInt32ExtendedFormat.bitrateIEC](bitrateiec.md) — 将 32 位整数显示为 IEC 比特率的格式。
- [OSLogInt32ExtendedFormat.byteCount](bytecount.md) — 将 32 位整数显示为字节的格式。
- [OSLogInt32ExtendedFormat.byteCountIEC](bytecountiec.md) — 将 32 位整数显示为 IEC 字节的格式。
- [OSLogInt32ExtendedFormat.truth](truth.md) — 将 32 位整数显示为 true 或 false 的格式。
- [OSLogInt32ExtendedFormat.answer](answer.md) — 将 32 位整数显示为 yes 或 no 的格式。
