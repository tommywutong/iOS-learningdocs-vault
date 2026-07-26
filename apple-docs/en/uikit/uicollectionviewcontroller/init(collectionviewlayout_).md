---
title: 'init(collectionViewLayout:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewcontroller/init(collectionviewlayout:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewcontroller/init(collectionviewlayout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewcontroller/init%28collectionviewlayout%3A%29.json'
content_hash: 'sha256:d0dcb1560fd92553'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewController](../uicollectionviewcontroller.md)

# init(collectionViewLayout:)

<sub>Initializer</sub>

Initializes a collection view controller and configures the collection view with the provided layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(collectionViewLayout layout: UICollectionViewLayout)
```

## Parameters

- `layout` — The layout object to associate with the collection view. The layout controls how the collection view presents its cells and supplementary views.

## Return Value

An initialized `UICollectionViewController` object or `nil` if the object could not be created.

## See Also

### Creating a collection view controller

- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Returns a newly initialized view controller with the nib file in the specified bundle.
- [- initWithCoder:](<init(coder_).md>) — Creates a collection view controller with the nib file in the specified bundle.
