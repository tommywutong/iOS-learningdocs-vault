---
title: 'prepare(forAnimatedBoundsChange:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicollectionviewlayout/prepare(foranimatedboundschange:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/prepare(foranimatedboundschange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/prepare%28foranimatedboundschange%3A%29.json'
content_hash: 'sha256:39e512b61aec505c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# prepare(forAnimatedBoundsChange:)

<sub>Instance Method</sub>

Prepares the layout object for animated changes to the view’s bounds or the insertion or deletion of items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func prepare(forAnimatedBoundsChange oldBounds: CGRect)
```

## Parameters

- `oldBounds` — The current bounds of the collection view.

## Discussion

The collection view calls this method before performing any animated changes to the view’s bounds or before the animated insertion or deletion of items. This method is the layout object’s opportunity to perform any calculations needed to prepare for those animated changes. Specifically, you might use this method to calculate the initial or final positions of inserted or deleted items so that you can return those values when asked for them.

You can also use this method to perform additional animations. Any animations you create are added to the animation block used to handle the insertions, deletions, and bounds changes.

## See Also

### Coordinating animated changes

- [- finalizeAnimatedBoundsChange](<finalizeanimatedboundschange().md>) — Cleans up after any animated changes to the view’s bounds or after the insertion or deletion of items.
