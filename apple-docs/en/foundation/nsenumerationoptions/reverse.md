---
title: reverse
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsenumerationoptions/reverse
source_url: 'https://developer.apple.com/documentation/foundation/nsenumerationoptions/reverse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsenumerationoptions/reverse.json'
content_hash: 'sha256:b4cd0dfe23321bcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSEnumerationOptions](../nsenumerationoptions.md)

# reverse

<sub>Type Property</sub>

Specifies that the enumeration should be performed in reverse.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var reverse: NSEnumerationOptions { get }
```

## Discussion

This option is available for `NSArray` and `NSIndexSet` classes; its behavior is undefined for `NSDictionary` and `NSSet` classes, or when combined with the `NSEnumerationConcurrent` flag.

## See Also

### Constants

- [NSEnumerationConcurrent](concurrent.md) — Specifies that the Block enumeration should be concurrent.
