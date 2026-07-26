---
title: DISPATCH_CURRENT_QUEUE_LABEL
framework: Dispatch
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_current_queue_label
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_current_queue_label'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_current_queue_label.json'
content_hash: 'sha256:a6ebce0a6ececd22'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_CURRENT_QUEUE_LABEL

<sub>Macro</sub>

Pass this constant to the [dispatch_queue_get_label](dispatch_queue_get_label.md) function to retrieve the label of the current queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
#define DISPATCH_CURRENT_QUEUE_LABEL
```

## See Also

### Managing Queue Attributes

- [dispatch_queue_get_label](dispatch_queue_get_label.md) — Returns the label you assigned to the dispatch queue at creation time.
- [dispatch_set_target_queue](<dispatchobject/settarget(queue_).md>) — Specifies the dispatch queue on which to perform work associated with the current object.
