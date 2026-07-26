---
title: OSLogPointerFormat.timespec
framework: os
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/oslogpointerformat/timespec
source_url: 'https://developer.apple.com/documentation/os/oslogpointerformat/timespec'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/oslogpointerformat/timespec.json'
content_hash: 'sha256:7e0a4ce48535aa19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [os](../../os.md) · [OSLogPointerFormat](../oslogpointerformat.md)

# OSLogPointerFormat.timespec

<sub>Case</sub>

An option to display the pointer bytes as a time specification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case timespec
```

## Discussion

This option prints an easily readable `timespec` structure.

## See Also

### Getting the Format Options

- [OSLogPointerFormat.none](none.md) — An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.ipv6Address](ipv6address.md) — An option to display the pointer bytes as an IPv6 network address.
- [OSLogPointerFormat.sockaddr](sockaddr.md) — An option to display the pointer bytes as a socket address.
- [OSLogPointerFormat.timeval](timeval.md) — An option to display the pointer bytes as a time value.
- [OSLogPointerFormat.uuid](uuid.md) — An option to display the pointer bytes as a formatted UUID.
