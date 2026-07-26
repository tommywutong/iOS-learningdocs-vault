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
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSLogPointerFormat

<sub>Enumeration</sub>

The formatting options for pointer data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum OSLogPointerFormat
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Getting the Format Options

- [OSLogPointerFormat.none](oslogpointerformat/none.md) — An option to treat the pointer as raw bytes, and not format it.
- [OSLogPointerFormat.ipv6Address](oslogpointerformat/ipv6address.md) — An option to display the pointer bytes as an IPv6 network address.
- [OSLogPointerFormat.sockaddr](oslogpointerformat/sockaddr.md) — An option to display the pointer bytes as a socket address.
- [OSLogPointerFormat.timespec](oslogpointerformat/timespec.md) — An option to display the pointer bytes as a time specification.
- [OSLogPointerFormat.timeval](oslogpointerformat/timeval.md) — An option to display the pointer bytes as a time value.
- [OSLogPointerFormat.uuid](oslogpointerformat/uuid.md) — An option to display the pointer bytes as a formatted UUID.

## See Also

### Value Formatters

- [OSLogBoolFormat](oslogboolformat.md) — The formatting options for Boolean values.
- [OSLogIntegerFormatting](oslogintegerformatting.md) — The formatting options for integer values.
- [OSLogInt32ExtendedFormat](oslogint32extendedformat.md) — The formatting options for 32-bit integer values.
- [OSLogFloatFormatting](oslogfloatformatting.md) — The formatting options for double and floating-point numbers.
