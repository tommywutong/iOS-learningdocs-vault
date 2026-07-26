---
title: reservedSpaceLength
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/port/reservedspacelength
source_url: 'https://developer.apple.com/documentation/foundation/port/reservedspacelength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/port/reservedspacelength.json'
content_hash: 'sha256:64d7523cadb2b1c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# reservedSpaceLength

<sub>Instance Property</sub>

The number of bytes of space reserved by the receiver for sending data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var reservedSpaceLength: Int { get }
```

## Discussion

The number of bytes reserved by the receiver for sending data. The default length is `0`.

## See Also

### Setting information

- [- sendBeforeDate:components:from:reserved:](<send(before_components_from_reserved_).md>) — This method is provided for subclasses that have custom types of `NSPort`.
- [- sendBeforeDate:msgid:components:from:reserved:](<send(before_msgid_components_from_reserved_).md>) — This method is provided for subclasses that have custom types of `NSPort`.
