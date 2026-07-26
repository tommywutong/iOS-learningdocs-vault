---
title: ScrollPhase
framework: SwiftUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/scrollphase
source_url: 'https://developer.apple.com/documentation/swiftui/scrollphase'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/scrollphase.json'
content_hash: 'sha256:066f205fd7b3a4a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# ScrollPhase

<sub>Enumeration</sub>

A type that describes the state of a scroll gesture of a scrollable view like a scroll view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum ScrollPhase
```

## Overview

A scroll gesture can be in one of four phases: - idle: No active scroll is occurring. - panning: An active scroll being driven by the user is occurring. - decelerating: The user has stopped driving a scroll and the scroll view is decelerating to its final target. - animating: The system is animating to a final target as a result of a programmatic animated scroll from using a [ScrollViewReader](scrollviewreader.md) or [scrollPosition(id:anchor:)](<view/scrollposition(id_anchor_).md>) modifier.

SwiftUI provides you a value of this type when using the [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) modifier.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting scroll gesture states

- [ScrollPhase.animating](scrollphase/animating.md) — The animating phase where the scroll view is animating towards a final target.
- [ScrollPhase.decelerating](scrollphase/decelerating.md) — The decelerating phase where the user use has stopped interacting with the scroll view and the scroll view is decelerating towards its final target.
- [ScrollPhase.idle](scrollphase/idle.md) — The idle phase where no kind of scrolling is occurring.
- [ScrollPhase.interacting](scrollphase/interacting.md) — The interacting phase where the user is interacting with the scroll view.
- [ScrollPhase.tracking](scrollphase/tracking.md) — The tracking phase where the scroll view is tracking a potential scroll by the user but the user hasn’t started a scroll.

### Checking for active scrolling

- [isScrolling](scrollphase/isscrolling.md) — Whether the scroll view is actively scrolling.

## See Also

### Responding to scroll view changes

- [onScrollGeometryChange(for:of:action:)](<view/onscrollgeometrychange(for_of_action_).md>) — Adds an action to be performed when a value, created from a scroll geometry, changes.
- [onScrollTargetVisibilityChange(idType:threshold:_:)](<view/onscrolltargetvisibilitychange(idtype_threshold___).md>) — Adds an action to be called with information about what views would be considered visible.
- [onScrollVisibilityChange(threshold:_:)](<view/onscrollvisibilitychange(threshold___).md>) — Adds an action to be called when the view crosses the threshold to be considered on/off screen.
- [onScrollPhaseChange(_:)](<view/onscrollphasechange(__).md>) — Adds an action to perform when the scroll phase of the first scroll view in the hierarchy changes.
- [ScrollGeometry](scrollgeometry.md) — A type that defines the geometry of a scroll view.
- [ScrollPhaseChangeContext](scrollphasechangecontext.md) — A type that provides you with more content when the phase of a scroll view changes.
