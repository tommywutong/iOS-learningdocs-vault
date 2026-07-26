---
title: UIFocusAnimationContext
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocusanimationcontext
source_url: 'https://developer.apple.com/documentation/uikit/uifocusanimationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusanimationcontext.json'
content_hash: 'sha256:136a0623bee49eed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusAnimationContext

<sub>Protocol</sub>

Information about focusing animations being performed by the system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIFocusAnimationContext : NSObjectProtocol
```

## Overview

You don’t adopt this protocol in your custom classes. When a focus update occurs and the system provides you with a [UIFocusAnimationCoordinator](uifocusanimationcoordinator.md) object, you can use that object to specify custom focus-related animations. When the time comes for the system to execute your animations, it delivers an object that adopts this protocol to your animation block. The context object contains information about the system animations that you can use to configure the behavior of your own animations. For example, you might configure your animations to be exactly half the duration of the system animations.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the animation attributes

- [duration](uifocusanimationcontext/duration.md) — The duration (measured in seconds) of the focus animation.

## See Also

### Adding animations to focus updates

- [- addCoordinatedFocusingAnimations:completion:](<uifocusanimationcoordinator/addcoordinatedfocusinganimations(__completion_).md>) — Runs the specified set of animations together with the system animations for adding focus to an item.
- [- addCoordinatedUnfocusingAnimations:completion:](<uifocusanimationcoordinator/addcoordinatedunfocusinganimations(__completion_).md>) — Runs the specified set of animations together with the system animations for removing focus from an item.
- [- addCoordinatedAnimations:completion:](<uifocusanimationcoordinator/addcoordinatedanimations(__completion_).md>) — Specifies the animations to coordinate with the active focus animation.
