---
title: 'init(referenceView:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/init(referenceview:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/init(referenceview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/init%28referenceview%3A%29.json'
content_hash: 'sha256:7bcdd3a1aadcb559'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# init(referenceView:)

<sub>Initializer</sub>

Initializes a dynamic animator with a specified view as its reference view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(referenceView view: UIView)
```

## Parameters

- `view` — The view for the dynamic animator, called the _reference view_.

## Return Value

The initialized dynamic animator, or `nil` if there was a problem initializing the object.

## Discussion

When you initialize a dynamic animator with this method, the behaviors (and their dynamic items) that you add to the animator employ the reference view’s coordinate system.

## See Also

### Initializing and managing a dynamic animator

- [- initWithCollectionViewLayout:](<init(collectionviewlayout_).md>) — Initializes a dynamic animator with a specified collection view layout.
- [- itemsInRect:](<items(in_).md>) — Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [- addBehavior:](<addbehavior(__).md>) — Adds a dynamic behavior to a dynamic animator.
- [- removeBehavior:](<removebehavior(__).md>) — Removes a specified dynamic behavior from a dynamic animator.
- [- removeAllBehaviors](<removeallbehaviors().md>) — Removes all of the dynamic behaviors from a dynamic animator.
