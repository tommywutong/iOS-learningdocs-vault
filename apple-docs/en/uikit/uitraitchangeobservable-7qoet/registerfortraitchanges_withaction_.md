---
title: 'registerForTraitChanges:withAction:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withaction:'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withaction:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges%3Awithaction%3A.json'
content_hash: 'sha256:e9887ca9c82ce4c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-7qoet.md)

# registerForTraitChanges:withAction:

<sub>Instance Method</sub>

Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (id<UITraitChangeRegistration>) registerForTraitChanges:(NSArray<Class<UITraitDefinition>> *) traits withAction:(SEL) action;
```

## Parameters

- `traits` — An array of traits to observe for changes.

- `action` — A selector identifying the method the system calls when one of the registered trait changes.

## Return Value

An opaque token you can use to stop observing trait changes by passing to [unregisterForTraitChanges(_:)](<../uitraitchangeobservable-67e94/unregisterfortraitchanges(__).md>). You don’t have to unregister your observations, and you can safely ignore this value.

## Discussion

This is a convenience method for [registerForTraitChanges(_:target:action:)](<../uitraitchangeobservable-67e94/registerfortraitchanges(__target_action_).md>) when the object receiving the registration is the target of the action. For example, when you register for changes on `self`, the `target` is `self`.

The following example calls [- setNeedsLayout](<../uiview/setneedslayout().md>) in response to changes to size traits:

```swift
let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

// Register for size class changes on self, and invalidate the layout in response to changes.
registerForTraitChanges(sizeTraits, action: #selector(UIView.setNeedsLayout))
```

## See Also

### Observing trait changes

- [registerForTraitChanges:withHandler:](registerfortraitchanges_withhandler_.md) — Registers a list of traits to observe and a closure to execute when one of the observed traits changes.
- [registerForTraitChanges:withTarget:action:](registerfortraitchanges_withtarget_action_.md) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges:](unregisterfortraitchanges_.md) — Tells the system to stop observing previously registered traits.
- [UITraitChangeHandler](../uitraitchangehandler.md)
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
