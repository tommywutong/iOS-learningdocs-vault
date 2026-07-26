---
title: Unmanaged
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unmanaged
source_url: 'https://developer.apple.com/documentation/swift/unmanaged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unmanaged.json'
content_hash: 'sha256:0cc0302688ebd7a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Unmanaged

<sub>Structure</sub>

A type for propagating an unmanaged object reference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Unmanaged<Instance> where Instance : AnyObject
```

## Overview

When you use this type, you become partially responsible for keeping the object alive.

## Relationships

- **Conforms To**: [AtomicOptionalRepresentable](../synchronization/atomicoptionalrepresentable.md), [AtomicRepresentable](../synchronization/atomicrepresentable.md), [BitwiseCopyable](bitwisecopyable.md), [Copyable](copyable.md), [Escapable](escapable.md), [Sendable](sendable.md), [SendableMetatype](sendablemetatype.md)

## Topics

### Instance Methods

- [autorelease()](<unmanaged/autorelease().md>) — Performs an unbalanced autorelease of the object.
- [release()](<unmanaged/release().md>) — Performs an unbalanced release of the object.
- [retain()](<unmanaged/retain().md>) — Performs an unbalanced retain of the object.
- [takeRetainedValue()](<unmanaged/takeretainedvalue().md>) — Gets the value of this unmanaged reference as a managed reference and consumes an unbalanced retain of it.
- [takeUnretainedValue()](<unmanaged/takeunretainedvalue().md>) — Gets the value of this unmanaged reference as a managed reference without consuming an unbalanced retain of it.
- [toOpaque()](<unmanaged/toopaque().md>) — Unsafely converts an unmanaged class reference to a pointer.

### Type Methods

- [fromOpaque(_:)](<unmanaged/fromopaque(__).md>) — Unsafely turns an opaque C pointer into an unmanaged class reference.
- [passRetained(_:)](<unmanaged/passretained(__).md>) — Creates an unmanaged reference with an unbalanced retain.
- [passUnretained(_:)](<unmanaged/passunretained(__).md>) — Creates an unmanaged reference without performing an unbalanced retain.

### Default Implementations

- [AtomicOptionalRepresentable Implementations](unmanaged/atomicoptionalrepresentable-implementations.md)
- [AtomicRepresentable Implementations](unmanaged/atomicrepresentable-implementations.md)

## See Also

### Reference Counting

- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-4mmpv.md>) — Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [withExtendedLifetime(_:_:)](<withextendedlifetime(____)-59dz3.md>) — Evaluates a closure while ensuring that the given instance is not destroyed before the closure returns.
- [extendLifetime(_:)](<extendlifetime(__).md>) — Extends the lifetime of the given instance.
