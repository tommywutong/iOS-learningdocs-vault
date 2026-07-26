---
title: canResignFirstResponder
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/canresignfirstresponder
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/canresignfirstresponder'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/canresignfirstresponder.json'
content_hash: 'sha256:e20e5eaa7d414b5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# canResignFirstResponder

<sub>Instance Property</sub>

Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var canResignFirstResponder: Bool { get }
```

## Return Value

[true](../../swift/true.md) if the responder can resign first-responder status; otherwise, [false](../../swift/false.md).

## Discussion

This method returns [true](../../swift/true.md) by default. You can override this method in your custom responders and return a different value if needed. For example, a text field containing invalid content might want to return [false](../../swift/false.md) to ensure that the user corrects that content first.

## See Also

### Managing the responder chain

- [nextResponder](next.md) — Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [isFirstResponder](isfirstresponder.md) — Returns a Boolean value indicating whether this object is the first responder.
- [canBecomeFirstResponder](canbecomefirstresponder.md) — Returns a Boolean value indicating whether this object can become the first responder.
- [- becomeFirstResponder](<becomefirstresponder().md>) — Asks UIKit to make this object the first responder in its window.
- [- resignFirstResponder](<resignfirstresponder().md>) — Notifies this object that it has been asked to relinquish its status as first responder in its window.
