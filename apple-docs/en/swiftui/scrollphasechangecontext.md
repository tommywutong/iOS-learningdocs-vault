---
title: ScrollPhaseChangeContext
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollphasechangecontext
source_url: 'https://developer.apple.com/documentation/swiftui/scrollphasechangecontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollphasechangecontext.json'
content_hash: 'sha256:90d55c3aca00afd9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollPhaseChangeContext

<sub>Structure</sub>

A type that provides you with more content when the phase of a scroll view changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollPhaseChangeContext
```

## Overview

You don’t create this type directly. Instead, SwiftUI provides an instance of this type in the [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) modifier.

## Topics

### Instance Properties

- [geometry](scrollphasechangecontext/geometry.md) — The geometry of the scroll view at the time of the scroll phase change.
- [velocity](scrollphasechangecontext/velocity.md) — The velocity of the scroll view at the time of the scroll phase change.

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](<view/onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<view/onscrolltargetvisibilitychange(idtype_threshold___).md>) — Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](<view/onscrollvisibilitychange(threshold___).md>) — Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) — Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollGeometry](scrollgeometry.md) — A type that defines the geometry of a scroll view.
- [ScrollPhase](scrollphase.md) — A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
