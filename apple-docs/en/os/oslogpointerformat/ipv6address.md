---
title: OSLogPointerFormat.ipv6Address
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogpointerformat/ipv6address
source_url: 'https://developer.apple.com/documentation/os/oslogpointerformat/ipv6address'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogpointerformat/ipv6address.json'
content_hash: 'sha256:7fd6cde2d1d0dee9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPointerFormat](../oslogpointerformat.md)

# OSLogPointerFormat.ipv6Address

<sub>Case</sub>

An option to display the pointer bytes as an IPv6 network address.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case ipv6Address
```

## Discussion

This option formats an `in6_addr` structure as an easily readable string.

## See Also

### Getting the Format Options

- [OSLogPointerFormat.none](none.md) — An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.sockaddr](sockaddr.md) — An option to display the pointer bytes as a socket address.
- [OSLogPointerFormat.timespec](timespec.md) — An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.timeval](timeval.md) — An option to display the pointer bytes as a time value.
- [OSLogPointerFormat.uuid](uuid.md) — An option to display the pointer bytes as a formatted UUID.
