---
title: dispatch_release
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_release
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_release'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_release.json'
content_hash: 'sha256:f313fc8538290e85'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_release

<sub>Function</sub>

Decrements the reference count (the retain count) of a dispatch object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_release(dispatch_object_t object);
```

## Parameters

- `object` — The object to release. This parameter cannot be `NULL`.

## Discussion

A dispatch object is asynchronously deallocated once all references to it are released (the reference count becomes zero). When your application no longer needs a dispatch object that it has created, it should call this function to release its interest in the object and allow its memory to be deallocated when appropriate. Note that GCD does not guarantee that a given client has the last or only reference to a given object.

> [!important] Important
> If your app is built with a deployment target of macOS 10.8 and later or iOS v6.0 and later, dispatch queues are typically managed by ARC, so you do not need to retain or release the dispatch queues.
>
> For compatibility with existing code, this behavior is configurable. See `GCD Objects and Automatic Reference Counting` for details.

Your application does not need to retain or release the global (main and concurrent) dispatch queues; calling this function on global dispatch queues has no effect.

> [!important] Important
> It is a programmer error to call this function on an object that is currently suspended, because suspension implies that there is still work to be done. Therefore, always balance calls to [dispatch_suspend](<dispatchobject/suspend().md>) and [dispatch_resume](<dispatchobject/resume().md>) so that the dispatch object is fully resumed when the last reference is released. The behavior when releasing the last reference to a dispatch object while it is in a suspended state is undefined.

## See Also

### Managing Memory

- [dispatch_retain](dispatch_retain.md) — Increments the reference count (the retain count) of a dispatch object.
- [dispatch_set_finalizer_f](dispatch_set_finalizer_f.md) — Sets the finalizer function for a dispatch object.
