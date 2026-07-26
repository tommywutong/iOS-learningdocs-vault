---
title: dispatch_once
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_once-c.func
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_once-c.func'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_once-c.func.json'
content_hash: 'sha256:93218f25684394a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_once

<sub>Function</sub>

Executes a block object only once for the lifetime of an application.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_once(dispatch_once_t *predicate, dispatch_block_t block);
```

## Parameters

- `predicate` — A pointer to a [dispatch_once_t](dispatch_once_t.md) structure that is used to test whether the block has completed or not.

- `block` — The block object to execute once.

## Discussion

This function is useful for initialization of global data (singletons) in an application. Always call this function before using or testing any variables that are initialized by the block.

If called simultaneously from multiple threads, this function waits synchronously until the block has completed.

The predicate must point to a variable stored in global or static scope. The result of using a predicate with automatic or dynamic storage (including Objective-C instance variables) is undefined.

## See Also

### Executing a Task Only Once

- [dispatch_once_f](dispatch_once_f-c.func.md) — Executes an application-defined function only once for the lifetime of an application.
- [dispatch_once_t](dispatch_once_t.md) — A predicate for use with the `dispatch_once` function.
