---
title: Object Runtime
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/object-runtime
source_url: 'https://developer.apple.com/documentation/foundation/object-runtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/object-runtime.json'
content_hash: 'sha256:dd6e4c4c8642fb4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Object Runtime

<sub>API Collection</sub>

Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.

## Topics

### Object Basics

- [NSObject](../objectivec/nsobject-swift.class.md) — The root class of most Objective-C class hierarchies, from which subclasses inherit a basic interface to the runtime system and the ability to behave as Objective-C objects.
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md) — The group of methods that are fundamental to all Objective-C objects.
- [NSKeyValueCoding](../objectivec/nskeyvaluecoding.md) — A mechanism by which you can access the properties of an object indirectly by name or key.

### Copying

- [NSCopying](nscopying.md) — A protocol that objects adopt to provide functional copies of themselves.
- [NSMutableCopying](nsmutablecopying.md) — A protocol that mutable objects adopt to provide functional copies of themselves.

### Value Wrappers and Transformations

- [NSNumber](nsnumber.md) — An object wrapper for primitive scalar numeric values.
- [NSValue](nsvalue.md) — A simple container for a single C or Objective-C data item.
- [ValueTransformer](valuetransformer.md) — An abstract class used to transform values from one representation to another.

### Swift Support

- [ReferenceConvertible](referenceconvertible.md) — A decoration applied to types that are backed by a Foundation reference type.
- [Classes Bridged to Swift Standard Library Value Types](classes-bridged-to-swift-standard-library-value-types.md) — Use bridged reference types when you need reference semantics or Foundation-specific behavior.

### Remote Objects

- [NSProxy](nsproxy.md) — An abstract superclass defining an API for objects that act as stand-ins for other objects or for objects that don’t exist yet.

### Memory Management

- [Memory Management Functions](memory-management-functions.md) — Perform low-level memory management tasks.

### Objective-C Runtime

- [Objective-C Runtime Utilities](objective-c-runtime-utilities.md) — Interact with the Objective-C runtime.

### Versions and API Availability

- [Foundation Framework Version Numbers](foundation-framework-version-numbers.md) — Recognize the constants for comparing the current running version of Foundation against known OS version numbers.

### Legacy

- [Distributed Objects Support](distributed-objects-support.md) — Enable communication among objects in different processes, both locally and on remote systems.
- [Objective-C Garbage Collection](objective-c-garbage-collection.md) — Interface with the legacy garbage collection system.

## See Also

### Low-Level Utilities

- [XPC](xpc.md) — Manage secure interprocess communication.
- [Processes and Threads](processes-and-threads.md) — Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md) — Use low-level Unix features to manage input and output among files, processes, and the network.
