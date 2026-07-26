---
title: finalizeLayoutTransition()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/finalizelayouttransition()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/finalizelayouttransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/finalizelayouttransition%28%29.json'
content_hash: 'sha256:74901b4520f3ef25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# finalizeLayoutTransition()

<sub>Instance Method</sub>

Tells the layout object to perform any final steps before the transition animations occur.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func finalizeLayoutTransition()
```

## Discussion

The collection view calls this method after it has gathered all of the layout attributes needed to perform a transition from one layout to another. You can use this method to clean up any data structures or caches created by your implementations of the [- prepareForTransitionFromLayout:](<preparefortransition(from_).md>) or [- prepareForTransitionToLayout:](<preparefortransition(to_).md>) methods.

## See Also

### Transitioning between layouts

- [- prepareForTransitionFromLayout:](<preparefortransition(from_).md>) — Tells the layout object to prepare to be installed as the layout for the collection view.
- [- prepareForTransitionToLayout:](<preparefortransition(to_).md>) — Tells the layout object that it is about to be removed as the layout for the collection view.
