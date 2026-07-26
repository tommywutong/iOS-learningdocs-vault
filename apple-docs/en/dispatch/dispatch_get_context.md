---
title: dispatch_get_context
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_get_context
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_get_context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_get_context.json'
content_hash: 'sha256:5d2e0703383237fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_get_context

<sub>Function</sub>

Returns the application-defined context of an object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void *dispatch_get_context(dispatch_object_t object);
```

## Parameters

- `object` — This parameter cannot be `NULL`.

## Return Value

The context of the object; can be `NULL`.

## Discussion

Your application can associate custom context data with the object, to be used only by your application. Your application must allocate and deallocate the data as appropriate.

## See Also

### Updating Contextual Data

- [dispatch_set_context](dispatch_set_context.md) — Associates an application-defined context with the object.
