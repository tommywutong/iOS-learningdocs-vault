---
title: clearsSelectionOnViewWillAppear
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewcontroller/clearsselectiononviewwillappear
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/clearsselectiononviewwillappear'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller/clearsselectiononviewwillappear.json'
content_hash: 'sha256:2e56b610b8078769'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewController](../uicollectionviewcontroller.md)

# clearsSelectionOnViewWillAppear

<sub>Instance Property</sub>

A Boolean value indicating if the controller clears the selection when the collection view appears.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var clearsSelectionOnViewWillAppear: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md). When [true](../../swift/true.md), the collection view controller clears the collection view’s current selection when it receives a [- viewWillAppear:](<../uiviewcontroller/viewwillappear(__).md>) message. Setting this property to [false](../../swift/false.md) preserves the selection.

## See Also

### Configuring the collection view behavior

- [installsStandardGestureForInteractiveMovement](installsstandardgestureforinteractivemovement.md) — A Boolean value indicating whether the collection view controller installs a standard gesture recognizer to drive the reordering process.
