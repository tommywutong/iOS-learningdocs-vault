---
title: UIPencilHoverPose
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, visionOS 26.2+]
languages: [swift, swift, swift, swift, swift, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilhoverpose
source_url: 'https://developer.apple.com/documentation/uikit/uipencilhoverpose'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilhoverpose.json'
content_hash: 'sha256:73ab3052814a3fbd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPencilHoverPose

<sub>Class</sub>

An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPencilHoverPose
```

## Overview

Use the hover pose of Apple Pencil to support more complex interactions in response to a double tap or squeeze. Information about the hover pose — such as azimuth, altitude, and hover distance — is available when a person holds a supported model of Apple Pencil close to the screen during a double tap or squeeze.

The following code example shows how to use the [location](uipencilhoverpose/location.md) of a hover pose to present a contextual palette near the tip of Apple Pencil.

```swift
func pencilInteraction(_ interaction: UIPencilInteraction,
                       didReceiveSqueeze squeeze: UIPencilInteraction.Squeeze) {
    let preferredAction = UIPencilInteraction.preferredSqueezeAction
    
    if preferredAction == .showContextualPalette, squeeze.phase == .ended {
        if let anchorPoint = squeeze.hoverPose?.location {
            presentContextualPalette(atLocation: anchorPoint)
        }
    }
}
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the hover characteristics

- [location](uipencilhoverpose/location.md) — The location of an Apple Pencil above the view’s bounds, in view’s coordinate space.
- [altitudeAngle](uipencilhoverpose/altitudeangle.md) — A value that represents the altitude angle of Apple Pencil.
- [azimuthAngle](uipencilhoverpose/azimuthangle.md) — A value that represents the azimuth angle of Apple Pencil.
- [azimuthUnitVector](uipencilhoverpose/azimuthunitvector.md) — A value that represents the azimuth unit vector of Apple Pencil in the specified view.
- [rollAngle](uipencilhoverpose/rollangle.md) — A value that represents the barrel-roll angle of Apple Pencil.
- [zOffset](uipencilhoverpose/zoffset.md) — A value that represents the normalized distance between the screen and Apple Pencil.

## See Also

### Apple Pencil interactions in UIKit

- [UIPencilInteraction](uipencilinteraction.md) — An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [UIPencilInteractionDelegate](uipencilinteractiondelegate.md) — The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [Tap](uipencilinteraction/tap.md) — An interaction that represents a double tap on Apple Pencil.
- [Squeeze](uipencilinteraction/squeeze.md) — An interaction that represents a squeeze on Apple Pencil.
- [Phase](uipencilinteraction/phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
