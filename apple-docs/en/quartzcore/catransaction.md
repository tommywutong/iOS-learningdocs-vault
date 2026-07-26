---
title: CATransaction
framework: Core Animation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransaction
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction.json'
content_hash: 'sha256:f92a9fc7acf7fae4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Animation](../quartzcore.md)

# CATransaction

<sub>Class</sub>

A mechanism for grouping multiple layer-tree operations into atomic updates to the render tree.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class CATransaction
```

## Overview

`CATransaction` is the Core Animation mechanism for batching multiple layer-tree operations into atomic updates to the render tree. Every modification to a layer tree must be part of a transaction. Nested transactions are supported.

Core Animation supports two types of transactions: _implicit_ transactions and _explicit_ transactions. Implicit transactions are created automatically when the layer tree is modified by a thread without an active transaction and are committed automatically when the thread’s runloop next iterates. Explicit transactions occur when the the application sends the [CATransaction](catransaction.md) class a [+ begin](<catransaction/begin().md>) message before modifying the layer tree, and a [+ commit](<catransaction/commit().md>) message afterwards.

[CATransaction](catransaction.md) allows you to override default animation properties that are set for animatable properties. You can customize duration, timing function, whether changes to properties trigger animations, and provide a handler that informs you when all animations from the transaction group are completed.

During a transaction you can temporarily acquire a recursive spin lock for managing property atomicity.

[CATransaction](catransaction.md) supports nested transactions. The following code shows how you can fade out a layer (named `transitioningLayer`) over a 2 second duration while scaling it to three times its original size. The scale animation is within a nested transaction with its own duration of 1 second. After the outer transaction completes, a completion block removes `transitioningLayer` from its parent layer.

```swift
let transitioningLayer = CALayer()
     
// Outer transaction animates `opacity` to 0 over 2 seconds
CATransaction.begin()
CATransaction.setAnimationDuration(2)
CATransaction.setCompletionBlock {
    transitioningLayer.removeFromSuperlayer()
}
    
transitioningLayer.opacity = 0
     
// Inner transaction animates scale to (3, 3, 3) over 1 second
CATransaction.begin()
CATransaction.setAnimationDuration(1)
     
transitioningLayer.transform = CATransform3DMakeScale(3, 3, 3)
     
CATransaction.commit() // Commits inner transaction
CATransaction.commit() // Commits outer transaction
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating and Committing Transactions

- [+ begin](<catransaction/begin().md>) — Begin a new transaction for the current thread.
- [+ commit](<catransaction/commit().md>) — Commit all changes made during the current transaction.
- [+ flush](<catransaction/flush().md>) — Flushes any extant implicit transaction.

### Overriding Animation Duration and Timing

- [+ animationDuration](<catransaction/animationduration().md>) — Returns the animation duration used by all animations within this transaction group.
- [+ setAnimationDuration:](<catransaction/setanimationduration(__).md>) — Sets the animation duration used by all animations within this transaction group.
- [+ animationTimingFunction](<catransaction/animationtimingfunction().md>) — Returns the timing function used for all animations within this transaction group.
- [+ setAnimationTimingFunction:](<catransaction/setanimationtimingfunction(__).md>) — Sets the timing function used for all animations within this transaction group.

### Temporarily Disabling Property Animations

- [+ disableActions](<catransaction/disableactions().md>) — Returns whether actions triggered as a result of property changes made within this transaction group are suppressed.
- [+ setDisableActions:](<catransaction/setdisableactions(__).md>) — Sets whether actions triggered as a result of property changes made within this transaction group are suppressed.

### Getting and Setting Completion Block Objects

- [+ completionBlock](<catransaction/completionblock().md>) — Returns the completion block object.
- [+ setCompletionBlock:](<catransaction/setcompletionblock(__).md>) — Sets the completion block object.

### Managing Concurrency

- [+ lock](<catransaction/lock().md>) — Attempts to acquire a recursive spin-lock lock, ensuring that returned layer values are valid until unlocked.
- [+ unlock](<catransaction/unlock().md>) — Relinquishes a previously acquired transaction lock.

### Getting and Setting Transaction Properties

- [+ setValue:forKey:](<catransaction/setvalue(__forkey_).md>) — Sets the arbitrary keyed-data for the specified key.
- [+ valueForKey:](<catransaction/value(forkey_).md>) — Returns the arbitrary keyed-data specified by the given key.

### Constants

- [Transaction properties](transaction-properties.md) — These constants define the property keys used by [+ valueForKey:](<catransaction/value(forkey_).md>) and [+ setValue:forKey:](<catransaction/setvalue(__forkey_).md>).

## See Also

### Animation Groups

- [CAAnimationGroup](caanimationgroup.md) — An object that allows multiple animations to be grouped and run concurrently.
