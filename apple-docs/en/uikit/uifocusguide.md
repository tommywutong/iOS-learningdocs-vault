---
title: UIFocusGuide
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusguide
source_url: 'https://developer.apple.com/documentation/uikit/uifocusguide'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusguide.json'
content_hash: 'sha256:45f21e17d3b2abc5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusGuide

<sub>Class</sub>

An object that exposes nonview areas as focusable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIFocusGuide
```

## Overview

As a subclass of [UILayoutGuide](uilayoutguide.md), a focus guide is not a view and does not define a new view or participate in the view hierarchy at all, except as an Auto Layout guide. Unlike [UILayoutGuide](uilayoutguide.md), [UIFocusGuide](uifocusguide.md) represents an invisible, focusable region that can redirect focus movement to other views. The `UIFocus.h` header file, including its related classes and its protocol, creates a single high-level software interface for controlling focus in apps that use focus-based input. This programming interface also helps to control focus behavior on the screen.

## Relationships

- **Inherits From**: [UILayoutGuide](uilayoutguide.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)

## Topics

### Enabling focus

- [enabled](uifocusguide/isenabled.md) — A Boolean value that indicates whether the guide is focusable.
- [preferredFocusEnvironments](uifocusguide/preferredfocusenvironments.md) — An array of focus environments to which the guide directs focus, ordered by priority.
- [preferredFocusedView](uifocusguide/preferredfocusedview.md) — The view that the focus will be redirected to if this guide is focused. _(deprecated)_

## See Also

### Focus guides

- [Creating custom navigation interactions](creating-custom-navigation-interactions.md) — Build nonstandard navigation interactions that move focus to the desired location.
