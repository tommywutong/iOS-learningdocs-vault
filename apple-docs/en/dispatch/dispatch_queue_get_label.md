---
title: dispatch_queue_get_label
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_get_label
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_get_label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_get_label.json'
content_hash: 'sha256:d15c3f8d4c16b4df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_queue_get_label

<sub>Function</sub>

Returns the label you assigned to the dispatch queue at creation time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern const char *dispatch_queue_get_label(dispatch_queue_t queue);
```

## Parameters

- `queue` — The dispatch queue from which to get the label. Specify [DISPATCH_CURRENT_QUEUE_LABEL](dispatch_current_queue_label.md) to retrieve the label of the current queue.

## Return Value

The label of the queue, or `NULL` if the queue was not provided a label during initialization.

## See Also

### Managing Queue Attributes

- [DISPATCH_CURRENT_QUEUE_LABEL](dispatch_current_queue_label.md) — Pass this constant to the [dispatch_queue_get_label](dispatch_queue_get_label.md) function to retrieve the label of the current queue.
- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — Specifies the dispatch queue on which to perform work associated with the current object.
