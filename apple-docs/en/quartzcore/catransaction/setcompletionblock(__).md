---
title: 'setCompletionBlock(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/catransaction/setcompletionblock(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/catransaction/setcompletionblock(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransaction/setcompletionblock%28_%3A%29.json'
content_hash: 'sha256:12dbeb14d7ca06eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransaction](../catransaction.md)

# setCompletionBlock(_:)

<sub>Type Method</sub>

Sets the completion block object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func setCompletionBlock(_ block: (() -> Void)?)
```

## Parameters

- `block` — A block object called when animations for this transaction group are completed. The block object takes no parameters and returns no value.

## Discussion

The completion block object that is guaranteed to be called (on the main thread) as soon as all animations subsequently added by this transaction group have completed (or have been removed.) If no animations are added before the current transaction group is committed (or the completion block is set to a different value,) the block will be invoked immediately.

## See Also

### Getting and Setting Completion Block Objects

- [+ completionBlock](<completionblock().md>) — Returns the completion block object.
