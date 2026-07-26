---
title: UIInterfaceOrientationMask
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinterfaceorientationmask
source_url: 'https://developer.apple.com/documentation/uikit/uiinterfaceorientationmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinterfaceorientationmask.json'
content_hash: 'sha256:6b2e27b1f716cc26'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIInterfaceOrientationMask

<sub>Structure</sub>

Constants that specify a view controller’s supported interface orientations.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct UIInterfaceOrientationMask
```

## Overview

Starting in iOS 8, you should employ the [UITraitCollection](uitraitcollection.md) and [UITraitEnvironment](uitraitenvironment.md) APIs, and size class properties as used in those APIs, instead of using [UIInterfaceOrientation](uiinterfaceorientation.md) constants or otherwise writing your app in terms of interface orientation.

In earlier versions of iOS, you returned these constants from the [- supportedInterfaceOrientationsForWindow:](<uiapplication/supportedinterfaceorientations(for_).md>) method or when determining which orientations to support in your app’s view controllers.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [UIInterfaceOrientationMaskPortrait](uiinterfaceorientationmask/portrait.md) — The view controller supports a portrait interface orientation.
- [UIInterfaceOrientationMaskLandscapeLeft](uiinterfaceorientationmask/landscapeleft.md) — The view controller supports a landscape-left interface orientation.
- [UIInterfaceOrientationMaskLandscapeRight](uiinterfaceorientationmask/landscaperight.md) — The view controller supports a landscape-right interface orientation.
- [UIInterfaceOrientationMaskPortraitUpsideDown](uiinterfaceorientationmask/portraitupsidedown.md) — The view controller supports an upside-down portrait interface orientation.
- [UIInterfaceOrientationMaskLandscape](uiinterfaceorientationmask/landscape.md) — The view controller supports both landscape-left and landscape-right interface orientation.
- [UIInterfaceOrientationMaskAll](uiinterfaceorientationmask/all.md) — The view controller supports all interface orientations.
- [UIInterfaceOrientationMaskAllButUpsideDown](uiinterfaceorientationmask/allbutupsidedown.md) — The view controller supports all but the upside-down portrait interface orientation.

### Initializers

- [init(rawValue:)](<uiinterfaceorientationmask/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

## See Also

### Managing interface geometry

- [- application:supportedInterfaceOrientationsForWindow:](<uiapplicationdelegate/application(__supportedinterfaceorientationsfor_).md>) — Asks the delegate for the interface orientations to use for the view controllers in the specified window. _(deprecated)_
- [UIInterfaceOrientation](uiinterfaceorientation.md) — Constants that specify the orientation of the app’s user interface.
- [UIApplicationInvalidInterfaceOrientationException](uiapplication/invalidinterfaceorientationexception.md) — An exception that’s thrown if a view controller or the app returns an invalid set of supported interface orientations.
