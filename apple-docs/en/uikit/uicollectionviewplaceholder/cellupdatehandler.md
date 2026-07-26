---
title: cellUpdateHandler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewplaceholder/cellupdatehandler
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewplaceholder/cellupdatehandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewplaceholder/cellupdatehandler.json'
content_hash: 'sha256:79c5437fe0c8d259'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewPlaceholder](../uicollectionviewplaceholder.md)

# cellUpdateHandler

<sub>Instance Property</sub>

The block that updates the contents of the placeholder cell.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var cellUpdateHandler: ((UICollectionViewCell) -> Void)? { get set }
```

## Discussion

Specify a block that configures or updates the appearance of your placeholder cell. The collection view calls this block when the placeholder cell becomes visible, and at other appropriate times.
