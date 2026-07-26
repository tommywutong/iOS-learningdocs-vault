---
title: 'init(frame:collectionViewLayout:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionview/init(frame:collectionviewlayout:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionview/init(frame:collectionviewlayout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionview/init%28frame%3Acollectionviewlayout%3A%29.json'
content_hash: 'sha256:df0191e4daf25167'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionView](../uicollectionview.md)

# init(frame:collectionViewLayout:)

<sub>Initializer</sub>

Creates a collection view object with the specified frame and layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(frame: CGRect, collectionViewLayout layout: UICollectionViewLayout)
```

## Parameters

- `frame` — The frame rectangle for the collection view, measured in points. The origin of the frame is relative to the superview in which you plan to add it. This frame is passed to the superclass during initialization.

- `layout` — The layout object to use for organizing items. The collection view stores a strong reference to the specified object. Must not be `nil`.

## Return Value

An initialized collection view object, or `nil` if the object couldn’t be created.

## Discussion

Use this method when initializing a collection view object programmatically.

This method is the designated initializer.

## See Also

### Creating a collection view

- [- initWithCoder:](<init(coder_).md>) — Creates a collection view object from data in a given unarchiver.
