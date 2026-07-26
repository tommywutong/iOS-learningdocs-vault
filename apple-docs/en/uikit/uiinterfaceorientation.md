---
title: UIInterfaceOrientation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterfaceorientation
source_url: 'https://developer.apple.com/documentation/uikit/uiinterfaceorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterfaceorientation.json'
content_hash: 'sha256:58d0186988ea87ab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIInterfaceOrientation

<sub>Enumeration</sub>

Constants that specify the orientation of the app’s user interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIInterfaceOrientation
```

## Overview

Starting in iOS 8, you should employ the [UITraitCollection](uitraitcollection.md) and [UITraitEnvironment](uitraitenvironment.md) APIs, and size class properties as used in those APIs, instead of using [UIInterfaceOrientation](uiinterfaceorientation.md) constants or otherwise writing your app in terms of interface orientation.

In earlier versions of iOS, you used these constants in the [statusBarOrientation](uiapplication/statusbarorientation.md) property and the [- setStatusBarOrientation:animated:](<uiapplication/setstatusbarorientation(__animated_).md>) method.

> [!important] Important
> Notice that [UIDeviceOrientationLandscapeRight](uideviceorientation/landscaperight.md) is assigned to [UIInterfaceOrientationLandscapeLeft](uiinterfaceorientation/landscapeleft.md) and [UIDeviceOrientationLandscapeLeft](uideviceorientation/landscapeleft.md) is assigned to [UIInterfaceOrientationLandscapeRight](uiinterfaceorientation/landscaperight.md). The reason for this is that rotating the device requires rotating the content in the opposite direction.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Orientations

- [UIInterfaceOrientationUnknown](uiinterfaceorientation/unknown.md) — The orientation of the device is unknown.
- [UIInterfaceOrientationPortrait](uiinterfaceorientation/portrait.md) — The device is in portrait mode, with the device upright and the Home button on the bottom.
- [UIInterfaceOrientationPortraitUpsideDown](uiinterfaceorientation/portraitupsidedown.md) — The device is in portrait mode but is upside down, with the device upright and the Home button at the top.
- [UIInterfaceOrientationLandscapeLeft](uiinterfaceorientation/landscapeleft.md) — The device is in landscape mode, with the device upright and the Home button on the left.
- [UIInterfaceOrientationLandscapeRight](uiinterfaceorientation/landscaperight.md) — The device is in landscape mode, with the device upright and the Home button on the right.

### Orientation Checks

- [UIInterfaceOrientationIsLandscape](uiinterfaceorientation/islandscape.md) — A Boolean value that indicates whether the user interface is currently presented in a landscape orientation.
- [UIInterfaceOrientationIsPortrait](uiinterfaceorientation/isportrait.md) — A Boolean value that indicates whether the user interface is currently presented in a portrait orientation.

### Initializers

- [init(rawValue:)](<uiinterfaceorientation/init(rawvalue_).md>)

## See Also

### Managing interface geometry

- [- application:supportedInterfaceOrientationsForWindow:](<uiapplicationdelegate/application(__supportedinterfaceorientationsfor_).md>) — Asks the delegate for the interface orientations to use for the view controllers in the specified window. _(deprecated)_
- [UIInterfaceOrientationMask](uiinterfaceorientationmask.md) — Constants that specify a view controller’s supported interface orientations.
- [UIApplicationInvalidInterfaceOrientationException](uiapplication/invalidinterfaceorientationexception.md) — An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.
