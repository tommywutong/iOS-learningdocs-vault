---
title: Dispatch Objects
framework: Dispatch
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch-objects
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch-objects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch-objects.json'
content_hash: 'sha256:c3b19c5771a6861b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# Dispatch Objects

<sub>API Collection</sub>

The basic behaviors supported by all dispatch types.

## Overview

There are many types of dispatch objects, including [dispatch_queue_t](dispatch_queue_t.md), [dispatch_group_t](dispatch_group_t.md), and [dispatch_source_t](dispatch_source_t.md). The base dispatch object interfaces allow you to manage memory, pause and resume execution, define object context, log task data, and more.

By default, dispatch objects are declared as Objective-C types when you build them with an Objective-C compiler. This behavior lets you adopt ARC and enable memory leak checks by the static analyzer. It also lets you add your objects to Cocoa collections.

## Topics

### Activating, Suspending, and Resuming the Object

- [dispatch_activate](<dispatchobject/activate().md>) — Activates the dispatch object.
- [dispatch_suspend](<dispatchobject/suspend().md>) — Suspends the invocation of block objects on a dispatch object.
- [dispatch_resume](<dispatchobject/resume().md>) — Resumes the invocation of block objects on a dispatch object.
- [dispatch_object_t](dispatch_object_t.md) — A dispatch object.

### Changing the Assigned Target Queue

- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — Specifies the dispatch queue on which to perform work associated with the current object.

## See Also

### Dispatch Objects

- [DispatchObject](dispatchobject.md) — The base class for most dispatch types.
- [DispatchPredicate](dispatchpredicate.md) — Logical conditions to evaluate within a given execution context.
- [dispatchPrecondition(condition:)](<dispatchprecondition(condition_).md>) — Checks a dispatch condition necessary for further execution.
