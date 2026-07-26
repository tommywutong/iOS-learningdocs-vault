---
title: tracksVelocity
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction/tracksvelocity
source_url: 'https://developer.apple.com/documentation/swiftui/transaction/tracksvelocity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction/tracksvelocity.json'
content_hash: 'sha256:3238b77bdd5ce43e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [Transaction](../transaction.md)

# tracksVelocity

<sub>Instance Property</sub>

Whether this transaction will track the velocity of any animatable properties that change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var tracksVelocity: Bool { get set }
```

## Discussion

This property can be enabled in an interactive context to track velocity during a user interaction so that when the interaction ends, an animation can use the accumulated velocities to create animations that preserve them. This tracking is mutually exclusive with an animation being used during a view change, since if there is an animation, it is responsible for managing its own velocity.

Gesture onChanged and updating callbacks automatically set this property to true.

This example shows an interaction which applies changes, tracking velocity until the final change, which applies an animation (which will start with the velocity that was tracked during the previous changes). These changes could come from a server or from an interactive control like a slider.

```swift
func receiveChange(change: ChangeInfo) {
    var transaction = Transaction()
    if change.isFinal {
        transaction.animation = .spring
    } else {
        transaction.tracksVelocity = true
    }
    withTransaction(transaction) {
        state.applyChange(change)
    }
}
```

## See Also

### Getting information about a transaction

- [isContinuous](iscontinuous.md) — A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.
- [scrollTargetAnchor](scrolltargetanchor.md) — The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.
- [subscript(_:)](<subscript(__).md>) — Accesses the transaction value associated with a custom key.
