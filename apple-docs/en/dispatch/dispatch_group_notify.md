---
title: dispatch_group_notify
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_group_notify
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_group_notify'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_group_notify.json'
content_hash: 'sha256:0f8d9ed7a43559b0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_group_notify

<sub>Function</sub>

Schedules a block object to be submitted to a queue when a group of previously submitted block objects have completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_group_notify(dispatch_group_t group, dispatch_queue_t queue, dispatch_block_t block);
```

## Parameters

- `group` — The dispatch group to observe. The group is retained by the system until the block has run to completion. This parameter cannot be `NULL`.

- `queue` — The queue to which the supplied block is submitted when the group completes. The queue is retained by the system until the block has run to completion. This parameter cannot be `NULL`.

- `block` — The block to submit when the group completes. This function performs a `Block_copy` and `Block_release` on behalf of the caller.  This parameter cannot be `NULL`.

## Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately.

When the notification block is submitted, the group is empty. The group can either be released with [dispatch_release](dispatch_release.md) or be reused for additional block objects. See [dispatch_group_async](dispatch_group_async.md) for more information.

## See Also

### Adding a Completion Handler

- [dispatch_group_notify_f](dispatch_group_notify_f.md) — Schedules an application-defined function to be submitted to a queue when a group of previously submitted block objects have completed.
