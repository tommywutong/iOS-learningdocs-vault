---
title: 'init(navigationBarClass:toolbarClass:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationcontroller/init(navigationbarclass:toolbarclass:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationcontroller/init(navigationbarclass:toolbarclass:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationcontroller/init%28navigationbarclass%3Atoolbarclass%3A%29.json'
content_hash: 'sha256:1aab1fd196cc8f29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationController](../uinavigationcontroller.md)

# init(navigationBarClass:toolbarClass:)

<sub>Initializer</sub>

Initializes and returns a newly created navigation controller that uses your custom bar subclasses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(navigationBarClass: AnyClass?, toolbarClass: AnyClass?)
```

## Parameters

- `navigationBarClass` — Specify the custom [UINavigationBar](../uinavigationbar.md) subclass you want to use, or specify `nil` to use the standard [UINavigationBar](../uinavigationbar.md) class.

- `toolbarClass` — Specify the custom [UIToolbar](../uitoolbar.md) subclass you want to use, or specify `nil` to use the standard [UIToolbar](../uitoolbar.md) class.

## Return Value

The initialized navigation controller object or `nil` if there was a problem initializing the object.

## Discussion

To customize the overall appearance of a navigation bar, use [UIAppearance](../uiappearance.md) APIs instead of this method. If you use this initialization method to create a navigation bar that uses custom bar subclasses, you are responsible for pushing and setting view controllers before presenting the navigation controller onscreen.

## See Also

### Creating a navigation controller

- [- initWithRootViewController:](<init(rootviewcontroller_).md>) — Initializes and returns a newly created navigation controller.
- [- initWithNibName:bundle:](<init(nibname_bundle_).md>) — Creates a navigation controller with the nib file in the specified bundle.
- [- initWithCoder:](<init(coder_).md>) — Creates a navigation controller from data in an unarchiver.
