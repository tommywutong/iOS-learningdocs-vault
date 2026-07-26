---
title: 'removeBehavior(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/removebehavior(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/removebehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/removebehavior%28_%3A%29.json'
content_hash: 'sha256:0cda6b4e3018a684'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# removeBehavior(_:)

<sub>Instance Method</sub>

Removes a specified dynamic behavior from a dynamic animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func removeBehavior(_ behavior: UIDynamicBehavior)
```

## Parameters

- `behavior` — The dynamic behavior instance that you want to remove from the animator. The dynamic animator ignores your use of this method if you: - Provide a `nil` value - Provide a dynamic behavior instance that is not part of the animator’s behavior hierarchy

## See Also

### Initializing and managing a dynamic animator

- [- initWithReferenceView:](<init(referenceview_).md>) — Initializes a dynamic animator with a specified view as its reference view.
- [- initWithCollectionViewLayout:](<init(collectionviewlayout_).md>) — Initializes a dynamic animator with a specified collection view layout.
- [- itemsInRect:](<items(in_).md>) — Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [- addBehavior:](<addbehavior(__).md>) — Adds a dynamic behavior to a dynamic animator.
- [- removeAllBehaviors](<removeallbehaviors().md>) — Removes all of the dynamic behaviors from a dynamic animator.
