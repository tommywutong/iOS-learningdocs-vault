---
title: delegate
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimation/delegate
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimation/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimation/delegate.json'
content_hash: 'sha256:df8019eb74e31152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimation](../caanimation.md)

# delegate

<sub>Instance Property</sub>

Specifies the receiver’s delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var delegate: (any CAAnimationDelegate)? { get set }
```

## Discussion

Defaults to `nil`.

> [!important] Important
> The `delegate` object is retained by the receiver. This is a rare exception to the memory management rules described in [Advanced Memory Management Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/MemoryMgmt/Articles/MemoryMgmt.html#//apple_ref/doc/uid/10000011i).
>
> An instance of `CAAnimation` should not be set as a delegate of itself. Doing so (outside of a garbage-collected environment) will cause retain cycles.
