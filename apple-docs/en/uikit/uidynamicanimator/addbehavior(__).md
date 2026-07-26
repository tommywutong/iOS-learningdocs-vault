---
title: 'addBehavior(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidynamicanimator/addbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimator/addbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimator/addbehavior%28_%3A%29.json'
content_hash: 'sha256:f74cb68ee9c648f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDynamicAnimator](../uidynamicanimator.md)

# addBehavior(_:)

<sub>Instance Method</sub>

Adds a dynamic behavior to a dynamic animator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func addBehavior(_ behavior: UIDynamicBehavior)
```

## Parameters

- `behavior` — The dynamic behavior instance you are adding. The dynamic animator ignores your use of this method if you: - Provide a `nil` value - Provide a behavior instance that you’ve already added to the animator at the same level in the behavior hierarchy > [!important] Important > The dynamic animator raises an exception if you provide a behavior instance that you’ve already added to the animator at a different level in the behavior hierarchy.

## See Also

### Initializing and managing a dynamic animator

- [- initWithReferenceView:](<init(referenceview_).md>) — Initializes a dynamic animator with a specified view as its reference view.
- [- initWithCollectionViewLayout:](<init(collectionviewlayout_).md>) — Initializes a dynamic animator with a specified collection view layout.
- [- itemsInRect:](<items(in_).md>) — Returns the dynamic items, from the animator’s behaviors, that intersect a specified rectangle.
- [- removeBehavior:](<removebehavior(__).md>) — Removes a specified dynamic behavior from a dynamic animator.
- [- removeAllBehaviors](<removeallbehaviors().md>) — Removes all of the dynamic behaviors from a dynamic animator.
