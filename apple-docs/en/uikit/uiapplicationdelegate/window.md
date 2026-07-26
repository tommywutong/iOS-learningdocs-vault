---
title: window
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationdelegate/window
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/window'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/window.json'
content_hash: 'sha256:a4a5bb181905f6e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# window

<sub>Instance Property</sub>

The window to use when presenting a storyboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var window: UIWindow? { get set }
```

## Discussion

This property contains the window used to present the app’s visual content on the device’s main screen.

Implementation of this property is required if your app’s `Info.plist` file contains the `UIMainStoryboardFile` key. Fortunately, the Xcode project templates usually include a synthesized declaration of the property automatically for the app delegate. The default value of this synthesized property is `nil`, which causes the app to create a generic [UIWindow](../uiwindow.md) object and assign it to the property. If you want to provide a custom window for your app, you must implement the getter method of this property and use it to create and return your custom window.

For more information about the [UIMainStoryboardFile](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/iPhoneOSKeys.html#//apple_ref/doc/uid/TP40009252-SW9) key, see [Information Property List Key Reference](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009247).
