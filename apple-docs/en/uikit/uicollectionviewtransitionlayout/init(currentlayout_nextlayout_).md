---
title: 'init(currentLayout:nextLayout:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewtransitionlayout/init(currentlayout:nextlayout:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/init(currentlayout:nextlayout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewtransitionlayout/init%28currentlayout%3Anextlayout%3A%29.json'
content_hash: 'sha256:8398fd8d33864b64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewTransitionLayout](../uicollectionviewtransitionlayout.md)

# init(currentLayout:nextLayout:)

<sub>Initializer</sub>

Initializes and returns a transition layout object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(currentLayout: UICollectionViewLayout, nextLayout newLayout: UICollectionViewLayout)
```

## Parameters

- `currentLayout` — The layout object currently in use by the collection view.

- `newLayout` — The new layout object that is being installed into the collection view.

## Return Value

An initialized transition layout object or `nil` if the object could not be created.

## Discussion

This method initializes the transition layout object and saves references to the current and new layout objects so that you can access them later. If you subclass and implement your own initialization method, you must call this method to initialize the superclass.

## See Also

### Initializing the transition layout object

- [- initWithCoder:](<init(coder_).md>) — Creates a transition layout object from data in an unarchiver.
