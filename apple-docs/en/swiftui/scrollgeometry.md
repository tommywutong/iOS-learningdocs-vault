---
title: ScrollGeometry
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollgeometry
source_url: 'https://developer.apple.com/documentation/swiftui/scrollgeometry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollgeometry.json'
content_hash: 'sha256:c1ddbf1cc6acbbc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollGeometry

<sub>Structure</sub>

A type that defines the geometry of a scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ScrollGeometry
```

## Overview

SwiftUI provides you values of this type when using modifiers like `View/onScrollGeometryChange(_:action:)` or [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>).

## Relationships

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(contentOffset:contentSize:contentInsets:containerSize:)](<scrollgeometry/init(contentoffset_contentsize_contentinsets_containersize_).md>) — Creates a scroll geometry.

### Instance Properties

- [bounds](scrollgeometry/bounds.md) — The bounds rect of the scroll view.
- [containerSize](scrollgeometry/containersize.md) — The size of the container of the scroll view.
- [contentInsets](scrollgeometry/contentinsets.md) — The content insets of the scroll view.
- [contentOffset](scrollgeometry/contentoffset.md) — The content offset of the scroll view.
- [contentSize](scrollgeometry/contentsize.md) — The size of the content of the scroll view.
- [visibleRect](scrollgeometry/visiblerect.md) — The visible rect of the scroll view.

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](<view/onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<view/onscrolltargetvisibilitychange(idtype_threshold___).md>) — Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](<view/onscrollvisibilitychange(threshold___).md>) — Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) — Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollPhase](scrollphase.md) — A type that describes the state of a scroll gesture of a scrollable view like a scroll view.
- [ScrollPhaseChangeContext](scrollphasechangecontext.md) — A type that provides you with more content when the phase of a scroll view changes.
