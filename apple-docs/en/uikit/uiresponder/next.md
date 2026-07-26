---
title: next
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/next
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/next'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/next.json'
content_hash: 'sha256:f43c55d027ff080a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# next

<sub>Instance Property</sub>

Returns the next responder in the responder chain, or `nil` if there’s no next responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var next: UIResponder? { get }
```

## Return Value

The next object in the responder chain, or `nil` if this is the last object in the chain.

## Discussion

The [UIResponder](../uiresponder.md) class doesn’t store or set the next responder automatically, so this method returns `nil` by default. Subclasses must override this method and return an appropriate next responder. For example, [UIView](../uiview.md) implements this method and returns the [UIViewController](../uiviewcontroller.md) object that manages it (if it has one) or its superview (if it doesn’t). [UIViewController](../uiviewcontroller.md) similarly implements the method and returns its view’s superview. [UIWindow](../uiwindow.md) returns the application object. The shared [UIApplication](../uiapplication.md) object normally returns `nil`, but it returns its app delegate if that object is a subclass of [UIResponder](../uiresponder.md) and hasn’t already been called to handle the event.

## See Also

### Managing the responder chain

- [isFirstResponder](isfirstresponder.md) — Returns a Boolean value indicating whether this object is the first responder.
- [canBecomeFirstResponder](canbecomefirstresponder.md) — Returns a Boolean value indicating whether this object can become the first responder.
- [- becomeFirstResponder](<becomefirstresponder().md>) — Asks UIKit to make this object the first responder in its window.
- [canResignFirstResponder](canresignfirstresponder.md) — Returns a Boolean value indicating whether the responder is willing to relinquish first-responder status.
- [- resignFirstResponder](<resignfirstresponder().md>) — Notifies this object that it has been asked to relinquish its status as first responder in its window.
