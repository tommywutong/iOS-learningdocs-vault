---
title: unownedExecutor
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/actor/unownedexecutor
source_url: 'https://developer.apple.com/documentation/swift/actor/unownedexecutor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/actor/unownedexecutor.json'
content_hash: 'sha256:9210272ab319317d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Actor](../actor.md)

# unownedExecutor

<sub>Instance Property</sub>

Retrieve the executor for this actor as an optimized, unowned reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var unownedExecutor: UnownedSerialExecutor { get }
```

## Discussion

This property must always evaluate to the same executor for a given actor instance, and holding on to the actor must keep the executor alive.

This property will be implicitly accessed when work needs to be scheduled onto this actor.  These accesses may be merged, eliminated, and rearranged with other work, and they may even be introduced when not strictly required.  Visible side effects are therefore strongly discouraged within this property.

> [!info] See Also
> [SerialExecutor](../serialexecutor.md)

> [!info] See Also
> [TaskExecutor](../taskexecutor.md)
