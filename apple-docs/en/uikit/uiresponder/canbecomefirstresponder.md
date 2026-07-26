---
title: canBecomeFirstResponder
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/canbecomefirstresponder
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/canbecomefirstresponder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/canbecomefirstresponder.json'
content_hash: 'sha256:671b3640058346c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# canBecomeFirstResponder

<sub>Instance Property</sub>

Returns a Boolean value indicating whether this object can become the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canBecomeFirstResponder: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the responder can become the first responder; otherwise, [false](../../swift/false.md).

## Discussion

This method returns [false](../../swift/false.md) by default. Subclasses must override this method and return [true](../../swift/true.md) to be able to become first responder.

Don’t call this method on a view that’s not currently in the active view hierarchy. The result is undefined.

## See Also

### Managing the responder chain

- [nextResponder](next.md) — Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [isFirstResponder](isfirstresponder.md) — Returns a Boolean value indicating whether this object is the first responder.
- [- becomeFirstResponder](<becomefirstresponder().md>) — Asks UIKit to make this object the first responder in its window.
- [canResignFirstResponder](canresignfirstresponder.md) — Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [- resignFirstResponder](<resignfirstresponder().md>) — Notifies this object that it has been asked to relinquish its status as first responder in its window.
