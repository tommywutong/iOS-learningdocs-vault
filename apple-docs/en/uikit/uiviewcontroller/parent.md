---
title: parent
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiviewcontroller/parent
source_url: 'https://developer.apple.com/documentation/uikit/uiviewcontroller/parent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiviewcontroller/parent.json'
content_hash: 'sha256:3e11496af9157eb8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIViewController](../uiviewcontroller.md)

# parent

<sub>Instance Property</sub>

The parent view controller of the recipient.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var parent: UIViewController? { get }
```

## Discussion

If the recipient is a child of a container view controller, this property holds the view controller it is contained in. If the recipient has no parent, the value in this property is `nil`.

Prior to iOS 5.0, if a view did not have a parent view controller and was being presented, the presenting view controller would be returned. On iOS 5, this behavior no longer occurs. Instead, use the [presentingViewController](presentingviewcontroller.md) property to access the presenting view controller.

## See Also

### Getting other related view controllers

- [presentingViewController](presentingviewcontroller.md) — The view controller that presented this view controller.
- [presentedViewController](presentedviewcontroller.md) — The view controller that is presented by this view controller, or one of its ancestors in the view controller hierarchy.
- [splitViewController](splitviewcontroller.md) — The nearest ancestor in the view controller hierarchy that is a split view controller.
- [navigationController](navigationcontroller.md) — The nearest ancestor in the view controller hierarchy that is a navigation controller.
- [tabBarController](tabbarcontroller.md) — The nearest ancestor in the view controller hierarchy that is a tab bar controller.
