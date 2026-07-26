---
title: concurrent
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsenumerationoptions/concurrent
source_url: 'https://developer.apple.com/documentation/foundation/nsenumerationoptions/concurrent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsenumerationoptions/concurrent.json'
content_hash: 'sha256:5e135a3f195dca6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSEnumerationOptions](../nsenumerationoptions.md)

# concurrent

<sub>Type Property</sub>

Specifies that the Block enumeration should be concurrent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var concurrent: NSEnumerationOptions { get }
```

## Discussion

The order of invocation is nondeterministic and undefined; this flag is a hint and may be ignored by the implementation under some circumstances; the code of the Block must be safe against concurrent invocation.

## See Also

### Constants

- [NSEnumerationReverse](reverse.md) — Specifies that the enumeration should be performed in reverse.
