---
title: isValid
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/port/isvalid
source_url: 'https://developer.apple.com/documentation/foundation/port/isvalid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/port/isvalid.json'
content_hash: 'sha256:d3d4dab9132f139a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Port](../port.md)

# isValid

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isValid: Bool { get }
```

## Discussion

[false](../../swift/false.md) if the receiver is known to be invalid, otherwise [true](../../swift/true.md).

An `NSPort` object becomes invalid when its underlying communication resource, which is operating system dependent, is closed or damaged.

## See Also

### Validation

- [- invalidate](<invalidate().md>) — Marks the receiver as invalid and posts an [NSPortDidBecomeInvalidNotification](didbecomeinvalidnotification.md) to the default notification center.
