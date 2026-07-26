---
title: DispatchObject
framework: Dispatch
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchobject
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchobject.json'
content_hash: 'sha256:5eb1bf23cd6100d3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DispatchObject

<sub>Class</sub>

The base class for most dispatch types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class DispatchObject
```

## Overview

There are many types of dispatch objects, including [DispatchQueue](dispatchqueue.md), [DispatchGroup](dispatchgroup.md), and [DispatchSource](dispatchsource.md). The base dispatch object interfaces allow you to manage memory, pause and resume execution, define object context, log task data, and more.

## Relationships

- **Inherits From**: [OS_object](../os/os_object.md)

- **Inherited By**: [DispatchGroup](dispatchgroup.md), [DispatchIO](dispatchio.md), [DispatchQueue](dispatchqueue.md), [DispatchSemaphore](dispatchsemaphore.md), [DispatchSource](dispatchsource.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Activating, Suspending, and Resuming

- [dispatch_activate](<dispatchobject/activate().md>) — Activates the dispatch object.
- [dispatch_resume](<dispatchobject/resume().md>) — Resumes the invocation of block objects on a dispatch object.
- [dispatch_suspend](<dispatchobject/suspend().md>) — Suspends the invocation of block objects on a dispatch object.

### Changing the Assigned Target Queue

- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — Specifies the dispatch queue on which to perform work associated with the current object.

## See Also

### Dispatch Objects

- [DispatchPredicate](dispatchpredicate.md) — Logical conditions to evaluate within a given execution context.
- [dispatchPrecondition(condition:)](<dispatchprecondition(condition_).md>) — Checks a dispatch condition necessary for further execution.
- [Dispatch Objects](dispatch-objects.md) — The basic behaviors supported by all dispatch types.
