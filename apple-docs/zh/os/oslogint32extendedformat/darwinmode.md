---
title: OSLogInt32ExtendedFormat.darwinMode
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogint32extendedformat/darwinmode
source_url: 'https://developer.apple.com/documentation/os/oslogint32extendedformat/darwinmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogint32extendedformat/darwinmode.json'
content_hash: 'sha256:15858ef7f7b286da'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogInt32ExtendedFormat](../oslogint32extendedformat.md)

# OSLogInt32ExtendedFormat.darwinMode

<sub>Case</sub>

将 32 位整数显示为 Darwin 文件模式的格式。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case darwinMode
```

## 讨论

使用此选项可将插值格式化为 Darwin 文件模式，例如 `-rwx------`。由于 Darwin 使用八进制值以数值形式表示文件模式，请向格式化器传入八进制字面量。或者，将八进制值转换为其 32 位整数等价形式，再对该值进行插值。有关使用八进制字面量的更多信息，请参阅 [Numeric Literals](https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html#ID323)。

下面的示例使用 `darwinMode` 格式化器格式化八进制字面量 `0o700`：

```swift
// 使用指定的子系统和分类创建一个 logger。
let logger = Logger(subsystem: "com.example.OSLogValueFormatting",
                    category: "Formatter Output")
        
// Darwin 使用八进制值以数值形式表示文件模式。利用 Swift
// 对八进制字面量的支持，将文件模式赋给一个 32 位
// 整数变量。
let value: Int32 = 0o700
        
// 使用指定格式将该值写入日志。
logger.info(".darwinMode output is \(value, format: .darwinMode)")
```

系统会把以下消息写入日志：

```
[Formatter Output] .darwinMode formats the value as -rwx------
```

## 另请参阅

### 获取格式

- [OSLogInt32ExtendedFormat.ipv4Address](ipv4address.md) — 将 32 位整数显示为 IPv4 地址的格式。
- [OSLogInt32ExtendedFormat.secondsSince1970](secondssince1970.md) — 将 32 位整数显示为日期的格式。
- [OSLogInt32ExtendedFormat.darwinErrno](darwinerrno.md) — 将 32 位整数显示为 Darwin 错误号的格式。
- [OSLogInt32ExtendedFormat.darwinSignal](darwinsignal.md) — 将 32 位整数显示为 Darwin 信号的格式。
- [OSLogInt32ExtendedFormat.bitrate](bitrate.md) — 将 32 位整数显示为比特率的格式。
- [OSLogInt32ExtendedFormat.bitrateIEC](bitrateiec.md) — 将 32 位整数显示为 IEC 比特率的格式。
- [OSLogInt32ExtendedFormat.byteCount](bytecount.md) — 将 32 位整数显示为字节的格式。
- [OSLogInt32ExtendedFormat.byteCountIEC](bytecountiec.md) — 将 32 位整数显示为 IEC 字节的格式。
- [OSLogInt32ExtendedFormat.truth](truth.md) — 将 32 位整数显示为 true 或 false 的格式。
- [OSLogInt32ExtendedFormat.answer](answer.md) — 将 32 位整数显示为 yes 或 no 的格式。
