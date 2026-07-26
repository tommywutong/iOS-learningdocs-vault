---
title: finalizeAnimatedBoundsChange()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicollectionviewlayout/finalizeanimatedboundschange()
source_url: 'https://developer.apple.com/documentation/uikit/uicollectionviewlayout/finalizeanimatedboundschange()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicollectionviewlayout/finalizeanimatedboundschange%28%29.json'
content_hash: 'sha256:8e19e45064394c69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICollectionViewLayout](../uicollectionviewlayout.md)

# finalizeAnimatedBoundsChange()

<sub>Instance Method</sub>

Cleans up after any animated changes to the view’s bounds or after the insertion or deletion of items.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func finalizeAnimatedBoundsChange()
```

## Discussion

The collection view calls this method after creating the animations for changing the view’s bounds or after the animated insertion or deletion of items. This method is the layout object’s opportunity to do any cleanup related to those operations.

You can also use this method to perform additional animations. Any animations you create are added to the animation block used to handle the insertions, deletions, and bounds changes.

## See Also

### Coordinating animated changes

- [- prepareForAnimatedBoundsChange:](<prepare(foranimatedboundschange_).md>) — Prepares the layout object for animated changes to the view’s bounds or the insertion or deletion of items.
