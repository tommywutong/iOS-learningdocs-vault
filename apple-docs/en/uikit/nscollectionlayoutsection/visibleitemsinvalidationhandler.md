---
title: visibleItemsInvalidationHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutsection/visibleitemsinvalidationhandler
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutsection/visibleitemsinvalidationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutsection/visibleitemsinvalidationhandler.json'
content_hash: 'sha256:b005a384a181f9a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSCollectionLayoutSection](../nscollectionlayoutsection.md)

# visibleItemsInvalidationHandler

<sub>Instance Property</sub>

A closure called before each layout cycle to allow modification of the items in the section immediately before they’re displayed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var visibleItemsInvalidationHandler: NSCollectionLayoutSectionVisibleItemsInvalidationHandler? { get set }
```
