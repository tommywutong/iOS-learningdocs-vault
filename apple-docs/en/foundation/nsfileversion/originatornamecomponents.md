---
title: originatorNameComponents
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsfileversion/originatornamecomponents
source_url: 'https://developer.apple.com/documentation/foundation/nsfileversion/originatornamecomponents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfileversion/originatornamecomponents.json'
content_hash: 'sha256:80e647c3bcce1c1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFileVersion](../nsfileversion.md)

# originatorNameComponents

<sub>Instance Property</sub>

The name components of the user who created this version of the file. Is nil if the file is not shared or if the current user is the originator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var originatorNameComponents: PersonNameComponents? { get }
```
