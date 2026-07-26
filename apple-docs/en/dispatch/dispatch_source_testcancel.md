---
title: dispatch_source_testcancel
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_testcancel
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_testcancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_testcancel.json'
content_hash: 'sha256:945b85985f78852e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_source_testcancel

<sub>Function</sub>

Tests whether the given dispatch source has been canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern intptr_t dispatch_source_testcancel(dispatch_source_t source);
```

## Parameters

- `source` — The dispatch source to be tested. This parameter cannot be `NULL`.

## Return Value

Non-zero if canceled and zero if not canceled.

## Discussion

Your application can use this function to test whether a dispatch source object has been canceled by a call to [dispatch_source_cancel](dispatch_source_cancel.md). The result of this function is non-zero immediately after [dispatch_source_cancel](dispatch_source_cancel.md) has been called.

## See Also

### Canceling a Dispatch Source

- [dispatch_source_cancel](dispatch_source_cancel.md) — Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.
