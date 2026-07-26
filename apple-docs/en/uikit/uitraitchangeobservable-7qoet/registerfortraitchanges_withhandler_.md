---
title: 'registerForTraitChanges:withHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges:withhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-7qoet/registerfortraitchanges%3Awithhandler%3A.json'
content_hash: 'sha256:e4fe9313a592243d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-7qoet.md)

# registerForTraitChanges:withHandler:

<sub>Instance Method</sub>

Registers a list of traits to observe and a closure to execute when one of the observed traits changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (id<UITraitChangeRegistration>) registerForTraitChanges:(NSArray<Class<UITraitDefinition>> *) traits withHandler:(UITraitChangeHandler) handler;
```

## Parameters

- `traits` — An array of traits to observe for changes.

- `handler` — A closure that the system executes when one of the registered traits changes.

## Return Value

An opaque token you can use to stop observing trait changes by passing to [unregisterForTraitChanges(_:)](<../uitraitchangeobservable-67e94/unregisterfortraitchanges(__).md>). You don’t have to unregister your observations, and you can safely ignore this value.

## Discussion

The first parameter of the closure provides access to the observed object whose traits have changed, so you don’t need to create a weak reference. When registering for changes on self, use `self` as the name and `Self` as the type of the first parameter.

The following example registers size class traits so that the system executes the closure when a size class trait changes in the view’s trait collection:

```swift
let sizeTraits: [UITrait] = [UITraitVerticalSizeClass.self, UITraitHorizontalSizeClass.self]

// Register for size class changes on self. Declare the first paramteter as `self: Self`.
// Declaring self as the first parameter eliminates the need to capture self from outside the closure, and avoids strong reference cycles.
registerForTraitChanges(sizeTraits) { (self: Self, previousTraitCollection: UITraitCollection) in
    // Handle the trait change.
}

// Register for size class changes on a different view of class MyView.
view.registerForTraitChanges(sizeTraits) { (view: MyView, previousTraitCollection: UITraitCollection) in
    // Handle the trait change.
}
```

## See Also

### Observing trait changes

- [registerForTraitChanges:withAction:](registerfortraitchanges_withaction_.md) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges:withTarget:action:](registerfortraitchanges_withtarget_action_.md) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges:](unregisterfortraitchanges_.md) — Tells the system to stop observing previously registered traits.
- [UITraitChangeHandler](../uitraitchangehandler.md)
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
