---
title: 'registerForTraitChanges(_:handler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges(_:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitchangeobservable-67e94/registerfortraitchanges%28_%3Ahandler%3A%29.json'
content_hash: 'sha256:6daf5dbca86f0ca3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitChangeObservable](../uitraitchangeobservable-67e94.md)

# registerForTraitChanges(_:handler:)

<sub>Instance Method</sub>

Registers a list of traits to observe and a closure to execute when one of the observed traits changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@discardableResult @MainActor func registerForTraitChanges<TraitEnvironment>(_ traits: [UITrait], handler: @escaping Self.TraitChangeHandler<TraitEnvironment>) -> any UITraitChangeRegistration where TraitEnvironment : UITraitEnvironment
```

## Parameters

- `traits` — An array of traits to observe for changes.

- `handler` — A closure that the system executes when one of the registered traits changes.

## Return Value

An opaque token you can use to stop observing trait changes by passing to [unregisterForTraitChanges(_:)](<unregisterfortraitchanges(__).md>). You don’t have to unregister your observations, and you can safely ignore this value.

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

- [registerForTraitChanges(_:action:)](<registerfortraitchanges(__action_).md>) — Registers a list of traits to observe, and calls a method on the receiving object when one of the observed traits changes.
- [registerForTraitChanges(_:target:action:)](<registerfortraitchanges(__target_action_).md>) — Registers a list of traits to observe, and calls a method on the specified target object when one of the observed traits changes.
- [unregisterForTraitChanges(_:)](<unregisterfortraitchanges(__).md>) — Tells the system to stop observing previously registered traits.
- [TraitChangeHandler](traitchangehandler.md) — A closure the system executes when observed traits change.
- [UITraitChangeRegistration](../uitraitchangeregistration.md)
