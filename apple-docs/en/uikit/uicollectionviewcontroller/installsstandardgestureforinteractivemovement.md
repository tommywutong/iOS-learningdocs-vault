---
title: installsStandardGestureForInteractiveMovement
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcontroller/installsstandardgestureforinteractivemovement
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/installsstandardgestureforinteractivemovement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller/installsstandardgestureforinteractivemovement.json'
content_hash: 'sha256:5ac12feef4f848a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewController](../uicollectionviewcontroller.md)

# installsStandardGestureForInteractiveMovement

<sub>Instance Property</sub>

A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var installsStandardGestureForInteractiveMovement: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md). When [true](../../swift/true.md), the collection view controller installs a standard gesture recognizer (based on a long-press gesture) to manage the reordering of views inside the collection view. The collection view’s data source must declare its support for reordering items by implementing the appropriate methods. Setting this property to [false](../../swift/false.md) prevents the installation of this gesture recognizer.

## See Also

### Configuring the collection view behavior

- [clearsSelectionOnViewWillAppear](clearsselectiononviewwillappear.md) — A Boolean value indicating if the controller clears the selection when the collection view appears.
