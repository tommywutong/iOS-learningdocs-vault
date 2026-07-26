---
title: dispatch_once_t
framework: Dispatch
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_once_t
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_once_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_once_t.json'
content_hash: 'sha256:8f738bbcbc66f034'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_once_t

<sub>Type Alias</sub>

A predicate for use with the `dispatch_once` function.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef intptr_t dispatch_once_t;
```

## Discussion

Variables of this type must have global or static scope.  The result of using this type with automatic or dynamic allocation is undefined. See [dispatch_get_global_queue](dispatch_get_global_queue.md) for details.

## See Also

### Executing a Task Only Once

- [dispatch_once](dispatch_once-c.func.md) — Executes a block object only once for the lifetime of an application.
- [dispatch_once_f](dispatch_once_f-c.func.md) — Executes an application-defined function only once for the lifetime of an application.
