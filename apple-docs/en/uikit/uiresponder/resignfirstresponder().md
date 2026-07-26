---
title: resignFirstResponder()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/resignfirstresponder()
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/resignfirstresponder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/resignfirstresponder%28%29.json'
content_hash: 'sha256:b3e95987898dd38d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# resignFirstResponder()

<sub>Instance Method</sub>

Notifies this object that it has been asked to relinquish its status as first responder in its window.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func resignFirstResponder() -> Bool
```

## Discussion

The default implementation returns [true](../../swift/true.md), resigning first responder status. You can override this method in your custom responders to update your object’s state or perform other actions, such as removing the highlight from a selection. You can also return [false](../../swift/false.md), refusing to relinquish first responder status. If you override this method, you must call `super` (the superclass implementation) at some point in your code.

## See Also

### Managing the responder chain

- [nextResponder](next.md) — Returns the next responder in the responder chain, or `nil` if there’s no next responder.
- [isFirstResponder](isfirstresponder.md) — Returns a Boolean value indicating whether this object is the first responder.
- [canBecomeFirstResponder](canbecomefirstresponder.md) — Returns a Boolean value indicating whether this object can become the first responder.
- [- becomeFirstResponder](<becomefirstresponder().md>) — Asks UIKit to make this object the first responder in its window.
- [canResignFirstResponder](canresignfirstresponder.md) — Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
