---
title: 'prepareForTransition(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/preparefortransition(from:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/preparefortransition(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/preparefortransition%28from%3A%29.json'
content_hash: 'sha256:ca9dea49078ce6f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# prepareForTransition(from:)

<sub>Instance Method</sub>

Tells the layout object to prepare to be installed as the layout for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepareForTransition(from oldLayout: UICollectionViewLayout)
```

## Parameters

- `oldLayout` — The layout object installed in the collection view at the beginning of the transition. You might use this object to provide different ending attributes based on the starting layout object.

## Discussion

Prior to performing a layout transition, the collection view calls this method so that your layout object can perform any initial calculations needed to generate layout attributes.

## See Also

### Transitioning between layouts

- [- prepareForTransitionToLayout:](<preparefortransition(to_).md>) — Tells the layout object that it is about to be removed as the layout for the collection view.
- [- finalizeLayoutTransition](<finalizelayouttransition().md>) — Tells the layout object to perform any final steps before the transition animations occur.
