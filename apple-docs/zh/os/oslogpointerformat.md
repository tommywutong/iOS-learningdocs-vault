---
title: OSLogPointerFormat
framework: os
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogpointerformat
source_url: 'https://developer.apple.com/documentation/os/oslogpointerformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogpointerformat.json'
content_hash: 'sha256:da81cd1445af1abd'
translated: true
---

> 导航：[技术](../technologies.md) · [os](../os.md)

# OSLogPointerFormat

<sub>枚举</sub>

指针数据的格式化选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum OSLogPointerFormat
```

## 关系

- **遵循**： [Equatable](../swift/equatable.md)、[Hashable](../swift/hashable.md)

## 主题

### 获取格式选项

- [OSLogPointerFormat.none](oslogpointerformat/none.md) — 将指针视为原始字节且不对其进行格式化的选项。
- [OSLogPointerFormat.ipv6Address](oslogpointerformat/ipv6address.md) — 将指针字节显示为 IPv6 网络地址的选项。
- [OSLogPointerFormat.sockaddr](oslogpointerformat/sockaddr.md) — 将指针字节显示为套接字地址的选项。
- [OSLogPointerFormat.timespec](oslogpointerformat/timespec.md) — 将指针字节显示为时间规格的选项。
- [OSLogPointerFormat.timeval](oslogpointerformat/timeval.md) — 将指针字节显示为时间值的选项。
- [OSLogPointerFormat.uuid](oslogpointerformat/uuid.md) — 将指针字节显示为格式化 UUID 的选项。

## 另请参阅

### 值格式化器

- [OSLogBoolFormat](oslogboolformat.md) — 布尔值的格式化选项。
- [OSLogIntegerFormatting](oslogintegerformatting.md) — 整数值的格式化选项。
- [OSLogInt32ExtendedFormat](oslogint32extendedformat.md) — 32 位整数值的格式化选项。
- [OSLogFloatFormatting](oslogfloatformatting.md) — double 和浮点数的格式化选项。
