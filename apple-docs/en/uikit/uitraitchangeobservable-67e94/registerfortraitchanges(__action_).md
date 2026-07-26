---
title: 'registerForTraitChanges(_:action:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges(_:action:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges(_:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges%28_%3Aaction%3A%29.json'
content_hash: 'sha256:552f9b74b481caea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-67e94.md)

# registerForTraitChanges(_:action:)

<sub>Instance Method</sub>

Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@discardableResult @MainActor func registerForTraitChanges(_ traits: [UITrait], action: Selector) -> any UITraitChangeRegistration
```

## Parameters

- `traits` — An array of traits to observe for changes.

- `action` — A selector identifying the method the system calls when one of the registered trait changes.

## Return Value

An opaque token you can use to stop observing trait changes by passing to [unregisterForTraitChanges(_:)](<unregisterfortraitchanges(__).md>). You don’t have to unregister your observations, and you can safely ignore this value.

## Discussion

This is a convenience method for [registerForTraitChanges(_:target:action:)](<registerfortraitchanges(__target_action_).md>) when the object receiving the registration is the target of the action. For example, when you register for changes on `self`, the `target` is `self`.

The following example calls [- setNeedsLayout](<../uiview/setneedslayout().md>) in response to changes to size traits:

```swift
let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

// Register for size class changes on self, and invalidate the layout in response to changes.
registerForTraitChanges(sizeTraits, action: #selector(UIView.setNeedsLayout))
```

## See Also

### Observing trait changes

- [registerForTraitChanges(_:handler:)](<registerfortraitchanges(__handler_).md>) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges(_:target:action:)](<registerfortraitchanges(__target_action_).md>) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges(_:)](<unregisterfortraitchanges(__).md>) — Tells the system to stop observing previously registered traits.
- [TraitChangeHandler](traitchangehandler.md) — A closure the system executes when observed traits change.
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
