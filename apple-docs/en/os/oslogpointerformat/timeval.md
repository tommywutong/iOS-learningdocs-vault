---
title: OSLogPointerFormat.timeval
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogpointerformat/timeval
source_url: 'https://developer.apple.com/documentation/os/oslogpointerformat/timeval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogpointerformat/timeval.json'
content_hash: 'sha256:1c55a3670739567a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPointerFormat](../oslogpointerformat.md)

# OSLogPointerFormat.timeval

<sub>Case</sub>

An option to display the pointer bytes as a time value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case timeval
```

## Discussion

This option prints an easily readable `timeval` structure.

## See Also

### Getting the Format Options

- [OSLogPointerFormat.none](none.md) — An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.ipv6Address](ipv6address.md) — An option to display the pointer bytes as an IPv6 network address.
- [OSLogPointerFormat.sockaddr](sockaddr.md) — An option to display the pointer bytes as a socket address.
- [OSLogPointerFormat.timespec](timespec.md) — An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.uuid](uuid.md) — An option to display the pointer bytes as a formatted UUID.
