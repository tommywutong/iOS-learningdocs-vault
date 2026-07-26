---
title: dispatch_block_testcancel
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_block_testcancel
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_block_testcancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_block_testcancel.json'
content_hash: 'sha256:337e68f34dcddc04'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_block_testcancel

<sub>Function</sub>

Tests whether the given dispatch block has been canceled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern intptr_t dispatch_block_testcancel(dispatch_block_t block);
```

## Parameters

- `block` — The dispatch block to test cancel. The result of passing `NULL` or a block object not returned by the [dispatch_block_create](dispatch_block_create.md) or [dispatch_block_create_with_qos_class](dispatch_block_create_with_qos_class.md) function is undefined.

## Return Value

Returns a non-zero value if the dispatch block is canceled, otherwise zero.

## See Also

### Canceling a Work Item

- [dispatch_block_cancel](dispatch_block_cancel.md) — Cancels the specified dispatch block asynchronously.
