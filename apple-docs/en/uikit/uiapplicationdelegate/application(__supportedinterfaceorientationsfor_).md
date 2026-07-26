---
title: 'application(_:supportedInterfaceOrientationsFor:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+（27.0 起废弃）, iPadOS 6.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationdelegate/application(_:supportedinterfaceorientationsfor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationdelegate/application%28_%3Asupportedinterfaceorientationsfor%3A%29.json'
content_hash: 'sha256:3a8edbba6d058c7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationDelegate](../uiapplicationdelegate.md)

# application(_:supportedInterfaceOrientationsFor:)

<sub>Instance Method</sub>

Asks the delegate for the interface orientations to use for the view controllers in the specified window.

> [!warning] Deprecated
> Use [- supportedInterfaceOrientationsForWindowScene:](<../uiwindowscenedelegate/supportedinterfaceorientations(for_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func application(_ application: UIApplication, supportedInterfaceOrientationsFor window: UIWindow?) -> UIInterfaceOrientationMask
```

## Parameters

- `application` — Your singleton app object.

- `window` — The window whose interface orientations you want to retrieve.

## Return Value

A bit mask of the [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md) constants that indicate the orientations to use for the view controllers.

## Discussion

This method returns the total set of interface orientations supported by the app. When determining whether to rotate a particular view controller, the orientations returned by this method are intersected with the orientations supported by the root view controller or topmost presented view controller. The app and view controller must agree before the rotation is allowed.

If you do not implement this method, the app uses the values in the `UIInterfaceOrientation` key of the app’s `Info.plist` as the default interface orientations.

## See Also

### Managing interface geometry

- [UIInterfaceOrientation](../uiinterfaceorientation.md) — Constants that specify the orientation of the app’s user interface.
- [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md) — Constants that specify a view controller’s supported interface orientations.
- [UIApplicationInvalidInterfaceOrientationException](../uiapplication/invalidinterfaceorientationexception.md) — An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.
