---
title: 'init(rootViewController:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/init(rootviewcontroller:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/init(rootviewcontroller:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/init%28rootviewcontroller%3A%29.json'
content_hash: 'sha256:fa8dfcfba7a1a5e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# init(rootViewController:)

<sub>Initializer</sub>

Initializes and returns a newly created navigation controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(rootViewController: UIViewController)
```

## Parameters

- `rootViewController` — The view controller that resides at the bottom of the navigation stack. This object cannot be an instance of the [UITabBarController](../uitabbarcontroller.md) class.

## Return Value

The initialized navigation controller object or `nil` if there was a problem initializing the object.

## Discussion

This is a convenience method for initializing the receiver and pushing a root view controller onto the navigation stack. Every navigation stack must have at least one view controller to act as the root.

## See Also

### Creating a navigation controller

- [- initWithNavigationBarClass:toolbarClass:](<init(navigationbarclass_toolbarclass_).md>) — Initializes and returns a newly created navigation controller that uses your custom bar subclasses.
- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Creates a navigation controller with the nib file in the specified bundle.
- [- initWithCoder:](<init(coder_).md>) — Creates a navigation controller from data in an unarchiver.
