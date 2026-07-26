---
title: 'items(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/items(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/items(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/items%28in%3A%29.json'
content_hash: 'sha256:a3e6e446216f12f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# items(in:)

<sub>Instance Method</sub>

Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func items(in rect: CGRect) -> [any UIDynamicItem]
```

## Parameters

- `rect` — The rectangle you are interested in.

## Return Value

The dynamic items, from the animator’s behaviors, that intersect the specified rectangle.

## Discussion

The coordinate system that pertains to the `rect` parameter depends on how you initialized the animator, as described in the Overview in this document.

## See Also

### Initializing and managing a dynamic animator

- [- initWithReferenceView:](<init(referenceview_).md>) — Initializes a dynamic animator with a specified view as its reference view.
- [- initWithCollectionViewLayout:](<init(collectionviewlayout_).md>) — Initializes a dynamic animator with a specified collection view layout.
- [- addBehavior:](<addbehavior(__).md>) — Adds a dynamic behavior to a dynamic animator.
- [- removeBehavior:](<removebehavior(__).md>) — Removes a specified dynamic behavior from a dynamic animator.
- [- removeAllBehaviors](<removeallbehaviors().md>) — Removes all of the dynamic behaviors from a dynamic animator.
