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
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPointerFormat](../oslogpointerformat.md)

# OSLogPointerFormat.sockaddr

<sub>Case</sub>

An option to display the pointer bytes as a socket address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case sockaddr
```

## Discussion

This option prints an easily readable `sockaddr` structure.

## See Also

### Getting the Format Options

- [OSLogPointerFormat.none](none.md) — An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.ipv6Address](ipv6address.md) — An option to display the pointer bytes as an IPv6 network address.
- [OSLogPointerFormat.timespec](timespec.md) — An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.timeval](timeval.md) — An option to display the pointer bytes as a time value.
- [OSLogPointerFormat.uuid](uuid.md) — An option to display the pointer bytes as a formatted UUID.
