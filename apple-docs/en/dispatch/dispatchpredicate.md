---
title: DispatchPredicate
framework: Dispatch
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchpredicate
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchpredicate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchpredicate.json'
content_hash: 'sha256:713aa5568dc0af8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchPredicate

<sub>Enumeration</sub>

Logical conditions to evaluate within a given execution context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum DispatchPredicate
```

## Overview

You use dispatch predicates with the [dispatchPrecondition(condition:)](<dispatchprecondition(condition_).md>) method.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Predicates

- [DispatchPredicate.onQueue(_:)](<dispatchpredicate/onqueue(__).md>) — A predicate that indicates the evaluated context is the associated dispatch queue.
- [DispatchPredicate.onQueueAsBarrier(_:)](<dispatchpredicate/onqueueasbarrier(__).md>) — A predicate that indicates the evaluated context is the associated dispatch queue as part of a barrier operation.
- [DispatchPredicate.notOnQueue(_:)](<dispatchpredicate/notonqueue(__).md>) — A predicate that indicates the evaluated context is not the associated dispatch queue.

## See Also

### Dispatch Objects

- [DispatchObject](dispatchobject.md) — The base class for most dispatch types.
- [dispatchPrecondition(condition:)](<dispatchprecondition(condition_).md>) — Checks a dispatch condition necessary for further execution.
- [Dispatch Objects](dispatch-objects.md) — The basic behaviors supported by all dispatch types.
