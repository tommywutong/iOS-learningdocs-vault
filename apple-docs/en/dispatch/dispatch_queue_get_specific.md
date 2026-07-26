---
title: dispatch_queue_get_specific
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_get_specific
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_get_specific'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_get_specific.json'
content_hash: 'sha256:2f3e29a997e4753d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_queue_get_specific

<sub>Function</sub>

Gets the value for the key associated with the specified dispatch queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void *dispatch_queue_get_specific(dispatch_queue_t queue, const void *key);
```

## Parameters

- `queue` — The queue containing the desired context data. This parameter must not be `NULL`.

- `key` — The key that identifies the associated context data. Keys are only compared as pointers and are never dereferenced. Thus, you can use a pointer to a static variable for a specific subsystem or any other value that allows you to identify the value uniquely. Specifying a pointer to a string constant is not recommended.

## Return Value

The context data associated with `key` or `NULL` if no context was found.

## Discussion

You can use this method to get the context data associated with a specific dispatch queue. Blocks executing on a queue can use the [dispatch_get_specific](dispatch_get_specific.md) function to retrieve the context associated with that specific queue instead.

## See Also

### Getting and Setting Contextual Data

- [dispatch_get_specific](dispatch_get_specific.md) — Returns the value for the key associated with the current dispatch queue.
- [dispatch_queue_set_specific](dispatch_queue_set_specific.md) — Sets the key/value data for the specified dispatch queue.
