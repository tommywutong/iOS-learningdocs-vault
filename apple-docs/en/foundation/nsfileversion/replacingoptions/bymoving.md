---
title: byMoving
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/replacingoptions/bymoving
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/replacingoptions/bymoving'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/replacingoptions/bymoving.json'
content_hash: 'sha256:62e0d27034b36721'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSFileVersion](../../nsfileversion.md) · [ReplacingOptions](../replacingoptions.md)

# byMoving

<sub>Type Property</sub>

An option to perform replacing by moving a file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var byMoving: NSFileVersion.ReplacingOptions { get }
```

## Discussion

This option results in moving the old version of the file out of the version store instead of copying the new contents into the file’s version. Use this option in conjunction with a file coordinator to make sure the operation is coordinated with other clients of the file.
