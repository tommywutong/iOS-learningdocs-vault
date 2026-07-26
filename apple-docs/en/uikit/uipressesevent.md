---
title: UIPressesEvent
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipressesevent
source_url: 'https://developer.apple.com/documentation/uikit/uipressesevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipressesevent.json'
content_hash: 'sha256:35fd75c66efd529b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPressesEvent

<sub>Class</sub>

An event that describes the state of a set of physical buttons that are available to the device, such as those on an associated remote or game controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIPressesEvent
```

## Relationships

- **Inherits From**: [UIEvent](uievent.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reading the event button presses

- [allPresses](uipressesevent/allpresses.md) — The state of all physical buttons in the event.
- [- pressesForGestureRecognizer:](<uipressesevent/presses(for_).md>) — Returns the state of all physical buttons in the event that are associated with a particular gesture recognizer.

## See Also

### Button presses

- [UIPress](uipress.md) — An object that represents the presence or movement of a button press on the screen for a particular event.
