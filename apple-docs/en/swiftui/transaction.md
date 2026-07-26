---
title: Transaction
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/transaction
source_url: 'https://developer.apple.com/documentation/swiftui/transaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/transaction.json'
content_hash: 'sha256:1b444b7f68067485'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Transaction

<sub>Structure</sub>

The context of the current state-processing update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Transaction
```

## Overview

Use a transaction to pass an animation between views in a view hierarchy.

The root transaction for a state change comes from the binding that changed, plus any global values set by calling [withTransaction(_:_:)](<withtransaction(____).md>) or [withAnimation(_:_:)](<withanimation(____).md>).

## Topics

### Creating a transaction

- [init()](<transaction/init().md>) — Creates a transaction.
- [init(animation:)](<transaction/init(animation_).md>) — Creates a transaction and assigns its animation property.

### Managing animations

- [animation](transaction/animation.md) — The animation, if any, associated with the current state change.
- [disablesAnimations](transaction/disablesanimations.md) — A Boolean value that indicates whether views should disable animations.
- [addAnimationCompletion(criteria:_:)](<transaction/addanimationcompletion(criteria___).md>) — Adds a completion to run when the animations created with this transaction are all complete.

### Managing window dismissal

- [dismissBehavior](transaction/dismissbehavior.md) — The behavior for how windows will dismiss programmatically when used in conjunction with [DismissWindowAction](dismisswindowaction.md).

### Getting information about a transaction

- [isContinuous](transaction/iscontinuous.md) — A Boolean value that indicates whether the transaction originated from an action that produces a sequence of values.
- [scrollTargetAnchor](transaction/scrolltargetanchor.md) — The preferred alignment of the view within a scroll view’s visible region when scrolling to a view.
- [tracksVelocity](transaction/tracksvelocity.md) — Whether this transaction will track the velocity of any animatable properties that change.
- [subscript(_:)](<transaction/subscript(__).md>) — Accesses the transaction value associated with a custom key.

### Instance Properties

- [scrollContentOffsetAdjustmentBehavior](transaction/scrollcontentoffsetadjustmentbehavior.md) — The behavior a scroll view will have regarding content offset adjustments for the current transaction.
- [scrollPositionUpdatePreservesVelocity](transaction/scrollpositionupdatepreservesvelocity.md) — Whether a programmatic update to the scroll position of a scroll view preserves the current velocity of any active scroll of the scroll view.

## See Also

### Moving an animation to another view

- [withTransaction(_:_:)](<withtransaction(____).md>) — Executes a closure with the specified transaction and returns the result.
- [withTransaction(_:_:_:)](<withtransaction(______).md>) — Executes a closure with the specified transaction key path and value and returns the result.
- [transaction(_:)](<view/transaction(__).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(value:_:)](<view/transaction(value___).md>) — Applies the given transaction mutation function to all animations used within the view.
- [transaction(_:body:)](<view/transaction(__body_).md>) — Applies the given transaction mutation function to all animations used within the `body` closure.
- [Entry()](<entry().md>) — Creates an environment values, transaction, container values, or focused values entry.
- [TransactionKey](transactionkey.md) — A key for accessing values in a transaction.
