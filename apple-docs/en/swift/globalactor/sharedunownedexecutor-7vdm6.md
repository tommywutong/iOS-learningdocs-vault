---
title: sharedUnownedExecutor
framework: Swift
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/globalactor/sharedunownedexecutor-7vdm6
source_url: 'https://developer.apple.com/documentation/swift/globalactor/sharedunownedexecutor-7vdm6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/globalactor/sharedunownedexecutor-7vdm6.json'
content_hash: 'sha256:65af10648ebb1162'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [GlobalActor](../globalactor.md)

# sharedUnownedExecutor

<sub>Type Property</sub>

Shorthand for referring to the `shared.unownedExecutor` of this global actor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var sharedUnownedExecutor: UnownedSerialExecutor { get }
```

## Discussion

When declaring a global actor with a custom executor, prefer to implement the underlying actor’s [unownedExecutor](../actor/unownedexecutor.md) property, and leave this `sharedUnownedExecutor` default implementation in-place as it will simply delegate to the `shared.unownedExecutor`.

The value of this property must be equivalent to `shared.unownedExecutor`, as it may be used by the Swift concurrency runtime or explicit user code with that assumption in mind.

Returning different executors for different invocations of this computed property is also illegal, as it could lead to inconsistent synchronization of the underlying actor.

> [!info] See Also
> [SerialExecutor](../serialexecutor.md)
