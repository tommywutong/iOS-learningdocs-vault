---
title: 'windowScene(_:didUpdate:interfaceOrientation:traitCollection:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+（26.0 起废弃）, iPadOS 13.0+（26.0 起废弃）, Mac Catalyst 13.1+（26.0 起废弃）, visionOS 1.0+（26.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdate:interfaceorientation:traitcollection:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiwindowscenedelegate/windowscene(_:didupdate:interfaceorientation:traitcollection:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwindowscenedelegate/windowscene%28_%3Adidupdate%3Ainterfaceorientation%3Atraitcollection%3A%29.json'
content_hash: 'sha256:fe662f294924fccb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWindowSceneDelegate](../uiwindowscenedelegate.md)

# windowScene(_:didUpdate:interfaceOrientation:traitCollection:)

<sub>Instance Method</sub>

Notifies you when the size, orientation, or traits of a scene change.

> [!warning] Deprecated
> Use windowScene(_: didUpdateEffectiveGeometry:) to be notified of the scene's geometry changes, or use traits whose values are inherited from the scene via the traitCollection of views and view controllers instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func windowScene(_ windowScene: UIWindowScene, didUpdate previousCoordinateSpace: any UICoordinateSpace, interfaceOrientation previousInterfaceOrientation: UIInterfaceOrientation, traitCollection previousTraitCollection: UITraitCollection)
```

## Parameters

- `windowScene` — The window scene object whose environment changed.

- `previousCoordinateSpace` — The previous coordinate space of the scene. Get the current coordinate space from the [coordinateSpace](../uiwindowscene/coordinatespace.md) property of the `windowScene` object.

- `previousInterfaceOrientation` — The previous interface orientation for your content. Get the current interface orientation from the [interfaceOrientation](../uiwindowscene/interfaceorientation.md) property of the `windowScene` object.

- `previousTraitCollection` — The previous traits for the window. Get the current window traits from the [traitCollection](../uiwindowscene/traitcollection.md) property of the `windowScene` object.

## Discussion

The window scene environment typically changes in response to user actions. For example, the interface orientation changes in response to device orientation changes or screen mode in response to moving to another screen. Similarly, the user may resize scenes on iPad, which causes UIKit to report a change to the scene’s coordinate space. Use these changes to make any needed changes to your scene’s content or interface.

## See Also

### Related Documentation

- [Presenting content on a connected display](../presenting-content-on-a-connected-display.md) — Fill connected displays with additional content from your app.
