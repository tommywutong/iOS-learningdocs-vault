---
title: OSLogInt32ExtendedFormat.byteCountIEC
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogint32extendedformat/bytecountiec
source_url: 'https://developer.apple.com/documentation/os/oslogint32extendedformat/bytecountiec'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogint32extendedformat/bytecountiec.json'
content_hash: 'sha256:5bc913b6b829227d'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md)

# OSLogInt32ExtendedFormat.byteCountIEC

<sub>Case</sub>

将 32 位整数显示为 IEC 字节的格式。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case byteCountIEC
```

## 讨论

使用此选项可将插值格式化为 IEC 字节，例如 `100 KiB`。下面的示例将 `byteCountIEC` 格式化器应用于 32 位整数值 `102_400`：

```swift
// 使用指定的子系统和分类创建一个 logger。
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
                
// 指定要插值的值。
let value: Int32 = 102_400
                
// 使用指定格式将该值写入日志。
logger.info(".byteCountIEC output is \(value, format: .byteCountIEC)")
```

系统会把以下消息写入日志：

```
[Formatter Output] .byteCountIEC output is 100 KiB
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
- [OSLogInt32ExtendedFormat.truth](truth.md) — 将 32 位整数显示为 true 或 false 的格式。
- [OSLogInt32ExtendedFormat.answer](answer.md) — 将 32 位整数显示为 yes 或 no 的格式。
