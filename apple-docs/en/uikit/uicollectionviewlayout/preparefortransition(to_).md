---
title: 'prepareForTransition(to:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/preparefortransition(to:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/preparefortransition(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/preparefortransition%28to%3A%29.json'
content_hash: 'sha256:727b708b0a5dd4c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# prepareForTransition(to:)

<sub>Instance Method</sub>

Tells the layout object that it is about to be removed as the layout for the collection view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepareForTransition(to newLayout: UICollectionViewLayout)
```

## Parameters

- `newLayout` — The layout object to be installed in the collection view at the end of the transition. You might use this object to provide different starting attributes depending on the final layout object.

## Discussion

Prior to performing a layout transition, the collection view calls this method so that your layout object can perform any initial calculations needed to generate layout attributes.

## See Also

### Transitioning between layouts

- [- prepareForTransitionFromLayout:](<preparefortransition(from_).md>) — Tells the layout object to prepare to be installed as the layout for the collection view.
- [- finalizeLayoutTransition](<finalizelayouttransition().md>) — Tells the layout object to perform any final steps before the transition animations occur.
