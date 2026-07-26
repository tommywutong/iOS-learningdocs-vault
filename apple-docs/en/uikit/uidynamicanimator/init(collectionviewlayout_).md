---
title: 'init(collectionViewLayout:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/init(collectionviewlayout:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/init(collectionviewlayout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/init%28collectionviewlayout%3A%29.json'
content_hash: 'sha256:1c3885f6b4bab19e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# init(collectionViewLayout:)

<sub>Initializer</sub>

Initializes a dynamic animator with a specified collection view layout.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(collectionViewLayout layout: UICollectionViewLayout)
```

## Parameters

- `layout` — The collection view layout for the dynamic animator, serving as the reference view for a dynamic animator in collection-view mode.

## Return Value

The initialized dynamic animator, or `nil` if there was a problem initializing the object.

## Discussion

When you initialize a dynamic animator with this method, the behaviors (and their dynamic items) that you add to the animator employ the collection view layout’s coordinate system.

## See Also

### Initializing and managing a dynamic animator

- [- initWithReferenceView:](<init(referenceview_).md>) — Initializes a dynamic animator with a specified view as its reference view.
- [- itemsInRect:](<items(in_).md>) — Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [- addBehavior:](<addbehavior(__).md>) — Adds a dynamic behavior to a dynamic animator.
- [- removeBehavior:](<removebehavior(__).md>) — Removes a specified dynamic behavior from a dynamic animator.
- [- removeAllBehaviors](<removeallbehaviors().md>) — Removes all of the dynamic behaviors from a dynamic animator.
