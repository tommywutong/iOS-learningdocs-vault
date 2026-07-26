---
title: UIMotionEffect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimotioneffect
source_url: 'https://developer.apple.com/documentation/uikit/uimotioneffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimotioneffect.json'
content_hash: 'sha256:552de1a3b06373a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMotionEffect

<sub>Class</sub>

An abstract superclass for defining motion-based modifiers for views.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIMotionEffect
```

## Overview

Subclasses of [UIMotionEffect](uimotioneffect.md) are responsible for defining the behavior to apply to a view when motion is detected. They do this by overriding the [- keyPathsAndRelativeValuesForViewerOffset:](<uimotioneffect/keypathsandrelativevalues(forvieweroffset_).md>) method and returning one or more key paths representing the view properties to modify.

### Subclassing notes

This class is abstract and can’t be instantiated directly. You can use the [UIInterpolatingMotionEffect](uiinterpolatingmotioneffect.md) class to implement effects or you can subclass and implement your own effects. If you subclass, your subclass must conform to the [NSCopying](../foundation/nscopying.md) and [NSCoding](../foundation/nscoding.md) protocols and must implement the [- keyPathsAndRelativeValuesForViewerOffset:](<uimotioneffect/keypathsandrelativevalues(forvieweroffset_).md>) method.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [UIInterpolatingMotionEffect](uiinterpolatingmotioneffect.md), [UIMotionEffectGroup](uimotioneffectgroup.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Initializing a motion effect

- [- init](<uimotioneffect/init().md>) — Initializes the motion effect to its default state.
- [- initWithCoder:](<uimotioneffect/init(coder_).md>) — Creates a motion effect from data in an unarchiver.

### Getting the key paths

- [- keyPathsAndRelativeValuesForViewerOffset:](<uimotioneffect/keypathsandrelativevalues(forvieweroffset_).md>) — For a given set of offset values, returns the view properties (and corresponding values) to update.
