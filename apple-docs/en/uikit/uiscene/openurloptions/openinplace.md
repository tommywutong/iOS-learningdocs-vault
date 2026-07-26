---
title: openInPlace
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/openurloptions/openinplace
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/openurloptions/openinplace'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/openurloptions/openinplace.json'
content_hash: 'sha256:ea4067234096c169'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIScene](../../uiscene.md) · [OpenURLOptions](../openurloptions.md)

# openInPlace

<sub>Instance Property</sub>

A Boolean value that indicates whether you should open the URL at its current location instead of copying it to your app’s container.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var openInPlace: Bool { get }
```

## Discussion

When the value of this property is [false](../../../swift/false.md), copy the document to your app’s container before opening the file. When the value of this property is [true](../../../swift/true.md), open the existing URL in its current location.
