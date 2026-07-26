---
title: dispatch_set_context
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_set_context
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_set_context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_set_context.json'
content_hash: 'sha256:ab7513d7772e1f15'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_set_context

<sub>Function</sub>

Associates an application-defined context with the object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_set_context(dispatch_object_t object, void *context);
```

## Parameters

- `object` — This parameter cannot be `NULL`.

- `context` — The new application-defined context for the object. This can be `NULL`.

## Discussion

Your application can associate custom context data with the object, to be used only by your application. Your application must allocate and deallocate the data as appropriate.

## See Also

### Updating Contextual Data

- [dispatch_get_context](dispatch_get_context.md) — Returns the application-defined context of an object.
