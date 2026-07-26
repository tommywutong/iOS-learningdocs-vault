---
title: invalidInterfaceOrientationException
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/invalidinterfaceorientationexception
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/invalidinterfaceorientationexception'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/invalidinterfaceorientationexception.json'
content_hash: 'sha256:f9329419bcb67b4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# invalidInterfaceOrientationException

<sub>Type Property</sub>

An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class let invalidInterfaceOrientationException: NSExceptionName
```

## Discussion

This exception is thrown if a view controller or the app returns `0` instead of a valid set of supported interface orientation values. It is also thrown if the orientation returned by a view controller’s [preferredInterfaceOrientationForPresentation](../uiviewcontroller/preferredinterfaceorientationforpresentation.md) method does not match one of the view controller’s supported orientations.

## See Also

### Managing interface geometry

- [- application:supportedInterfaceOrientationsForWindow:](<../uiapplicationdelegate/application(__supportedinterfaceorientationsfor_).md>) — Asks the delegate for the interface orientations to use for the view controllers in the specified window. _(deprecated)_
- [UIInterfaceOrientation](../uiinterfaceorientation.md) — Constants that specify the orientation of the app’s user interface.
- [UIInterfaceOrientationMask](../uiinterfaceorientationmask.md) — Constants that specify a view controller’s supported interface orientations.
