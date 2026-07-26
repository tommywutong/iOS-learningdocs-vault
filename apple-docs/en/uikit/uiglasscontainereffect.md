---
title: UIGlassContainerEffect
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiglasscontainereffect
source_url: 'https://developer.apple.com/documentation/uikit/uiglasscontainereffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiglasscontainereffect.json'
content_hash: 'sha256:5903619177171aab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGlassContainerEffect

<sub>Class</sub>

A `UIGlassContainerEffect` renders multiple glass elements into a combined effect.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@MainActor class UIGlassContainerEffect
```

## Overview

When using `UIGlassContainerEffect` with a `UIVisualEffectView` you can add individual glass elements to the visual effect view’s contentView by nesting `UIVisualEffectView`‘s configured with `UIGlassEffect`. In that configuration, the glass container will render all glass elements in one combined view, behind the visual effect view’s `contentView`.

## Relationships

- **Inherits From**: [UIVisualEffect](uivisualeffect.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [spacing](uiglasscontainereffect/spacing.md) — The spacing specifies the distance between elements at which they begin to merge.

## See Also

### Liquid Glass effects

- [UIGlassEffect](uiglasseffect.md) — A visual effect that renders a glass material.
