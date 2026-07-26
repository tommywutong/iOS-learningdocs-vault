---
title: dispatch_set_finalizer_f
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_set_finalizer_f
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_set_finalizer_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_set_finalizer_f.json'
content_hash: 'sha256:d6090e413b9b6556'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_set_finalizer_f

<sub>Function</sub>

Sets the finalizer function for a dispatch object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_set_finalizer_f(dispatch_object_t object, dispatch_function_t finalizer);
```

## Parameters

- `object` — The dispatch object to modify. This parameter cannot be `NULL`.

- `finalizer` — The finalizer function pointer.

## Discussion

The finalizer for a  dispatch object is invoked on that object’s target queue after all references to the object are released. The application can use the finalizer to release any resources associated with the object, such as the object’s application-defined context. The context parameter passed to the finalizer function is the current context of the dispatch object at the time the finalizer call is made. The finalizer is not called if the application-defined context is `NULL`.

## See Also

### Managing Memory

- [dispatch_retain](dispatch_retain.md) — Increments the reference count (the retain count) of a dispatch object.
- [dispatch_release](dispatch_release.md) — Decrements the reference count (the retain count) of a dispatch object.
