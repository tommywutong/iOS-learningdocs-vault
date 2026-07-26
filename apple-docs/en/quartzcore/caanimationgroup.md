---
title: CAAnimationGroup
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimationgroup
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimationgroup'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimationgroup.json'
content_hash: 'sha256:bb922ca73ca7648a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CAAnimationGroup

<sub>Class</sub>

An object that allows multiple animations to be grouped and run concurrently.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CAAnimationGroup
```

## Overview

The grouped animations run in the time space specified by the [CAAnimationGroup](caanimationgroup.md) instance.

The duration of the grouped animations are not scaled to the duration of their [CAAnimationGroup](caanimationgroup.md). Instead, the animations are clipped to the duration of the animation group. For example, a 10 second animation grouped within an animation group with a duration of 5 seconds displays only the first 5 seconds of the animation.

The following code shows how you can create a grouped animation containing  opacity and scale animations to fade out a layer while expanding it. The animation starts with an opacity of `1` and a scale of `1` on all axes. As the animation’s scale increases to `(3, 3, 3)`, the opacity drops to `0` and the animated layer vanishes.

```swift
let fadeOut = CABasicAnimation(keyPath: "opacity")
fadeOut.fromValue = 1
fadeOut.toValue = 0
fadeOut.duration = 1
     
let expandScale = CABasicAnimation()
expandScale.keyPath = "transform"
expandScale.valueFunction = CAValueFunction(name: kCAValueFunctionScale)
expandScale.fromValue = [1, 1, 1]
expandScale.toValue = [3, 3, 3]
     
let fadeAndScale = CAAnimationGroup()
fadeAndScale.animations = [fadeOut, expandScale]
fadeAndScale.duration = 1
```

> [!important] Important
> The [delegate](caanimation/delegate.md) and [removedOnCompletion](caanimation/isremovedoncompletion.md) properties of animations in the [animations](caanimationgroup/animations.md) array are currently ignored. The [CAAnimationGroup](caanimationgroup.md) delegate does receive these messages.

## Relationships

- **Inherits From**: [CAAnimation](caanimation.md)

- **Conforms To**: [CAAction](caaction.md), [CAMediaTiming](camediatiming.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Grouped animations

- [animations](caanimationgroup/animations.md) — An array of `CAAnimation` objects to be evaluated in the time space of the receiver.

## See Also

### Animation Groups

- [CATransaction](catransaction.md) — A mechanism for grouping multiple layer-tree operations into atomic updates to the render tree.
