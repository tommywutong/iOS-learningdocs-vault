---
title: dispatch_get_specific
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_get_specific
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_get_specific'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_get_specific.json'
content_hash: 'sha256:feee2ad22a417224'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_get_specific

<sub>Function</sub>

Returns the value for the key associated with the current dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void *dispatch_get_specific(const void *key);
```

## Parameters

- `key` — The key associated with the dispatch queue on which the current block is executing. Keys are only compared as pointers and never dereferenced. Passing a string constant directly is not recommended.

## Return Value

The context value for the specified key; otherwise `NULL` if the key was not set for the queue (or its target queue) or the queue is a global concurrent queue.

## Discussion

This function is intended to be called from a block executing in a dispatch queue. You use it to obtain context data associated with the queue. Calling this method from code not running in a dispatch queue returns `NULL` because there is no queue to provide context.

## See Also

### Getting and Setting Contextual Data

- [dispatch_queue_set_specific](dispatch_queue_set_specific.md) — Sets the key/value data for the specified dispatch queue.
- [dispatch_queue_get_specific](dispatch_queue_get_specific.md) — Gets the value for the key associated with the specified dispatch queue.
