---
title: UIDynamicAnimatorDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidynamicanimatordelegate
source_url: 'https://developer.apple.com/documentation/uikit/uidynamicanimatordelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidynamicanimatordelegate.json'
content_hash: 'sha256:33b6f90fc4cf188d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDynamicAnimatorDelegate

<sub>Protocol</sub>

To respond to the pausing or resumption of UIKit dynamic animation, configure a custom class to adopt the [UIDynamicAnimatorDelegate](uidynamicanimatordelegate.md) protocol. Then, in a dynamic animator (an instance of the [UIDynamicAnimator](uidynamicanimator.md) class), set the delegate to be an instance of your custom class.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIDynamicAnimatorDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to animation pausing and resumption

- [- dynamicAnimatorDidPause:](<uidynamicanimatordelegate/dynamicanimatordidpause(__).md>) — Called when a dynamic animator pauses the animations for its behaviors’ associated dynamic items.
- [- dynamicAnimatorWillResume:](<uidynamicanimatordelegate/dynamicanimatorwillresume(__).md>) — Called when a dynamic animator is about to resume the animations for its behaviors’ associated dynamic items.

## See Also

### Responding to animation changes

- [delegate](uidynamicanimator/delegate.md) — The delegate for responding to pausing or resumption of animation.
