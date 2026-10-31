---
title: OSLogPointerFormat.sockaddr
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogpointerformat/sockaddr
source_url: 'https://developer.apple.com/documentation/os/oslogpointerformat/sockaddr'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogpointerformat/sockaddr.json'
content_hash: 'sha256:2a6466e9f4d290a9'
translated: true
---

> 导航：[技术](../../technologies.md) · [os](../../os.md) · [OSLogPointerFormat](../oslogpointerformat.md)

# OSLogPointerFormat.sockaddr

<sub>Case</sub>

将指针字节显示为套接字地址的选项。

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case sockaddr
```

## 讨论

此选项打印易于阅读的 `sockaddr` 结构体。

## 另请参阅

### 获取格式选项

- [OSLogPointerFormat.none](none.md) — 将指针视为原始字节且不对其进行格式化的选项。
- [OSLogPointerFormat.ipv6Address](ipv6address.md) — 将指针字节显示为 IPv6 网络地址的选项。
- [OSLogPointerFormat.timespec](timespec.md) — 将指针字节显示为时间规格的选项。
- [OSLogPointerFormat.timeval](timeval.md) — 将指针字节显示为时间值的选项。
- [OSLogPointerFormat.uuid](uuid.md) — 将指针字节显示为格式化 UUID 的选项。
