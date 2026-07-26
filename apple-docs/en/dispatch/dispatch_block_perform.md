---
title: dispatch_block_perform
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_block_perform
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_block_perform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_block_perform.json'
content_hash: 'sha256:7e48a0c98edc2965'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_block_perform

<sub>Function</sub>

Creates, synchronously executes, and releases a dispatch block from the specified block and flags.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_block_perform(dispatch_block_flags_t flags, dispatch_block_t block);
```

## Parameters

- `flags` — Configuration flags for the block object. For possible values, see [dispatch_block_flags_t](dispatch_block_flags_t.md). Passing a value that is not a bitwise OR of valid flags results in `NULL` being returned.

- `block` — The block to create the dispatch block from.

## Discussion

This function is equivalent to the following code:

```objc
dispatch_block_t b = dispatch_block_create(flags, block);
b();
Block_release(b);
```

This functionality may be implemented more efficiently internally by not requiring a copy to the heap of the specified block or the allocation of a new block object.
