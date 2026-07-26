---
title: atomicWrite
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdata/writingoptions/atomicwrite
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/writingoptions/atomicwrite'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/writingoptions/atomicwrite.json'
content_hash: 'sha256:50f7ca3c12c6f7b5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [WritingOptions](../writingoptions.md)

# atomicWrite

<sub>Type Property</sub>

An option that attempts to write data to an auxiliary file first and then exchange the files.

> [!warning] Deprecated
> Use [NSDataWritingAtomic](atomic.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var atomicWrite: NSData.WritingOptions { get }
```
