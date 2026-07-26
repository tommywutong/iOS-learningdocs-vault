---
title: dispatch_group_notify_f
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_group_notify_f
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_group_notify_f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_group_notify_f.json'
content_hash: 'sha256:47247775a5334947'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_group_notify_f

<sub>Function</sub>

Schedules an application-defined function to be submitted to a queue when a group of previously submitted block objects have completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_group_notify_f(dispatch_group_t group, dispatch_queue_t queue, void *context, dispatch_function_t work);
```

## Parameters

- `group` — The dispatch group to observe. The group is retained by the system until the application-defined function has run to completion. This parameter cannot be `NULL`.

- `queue` — The queue to which the supplied block is submitted when the group completes. The queue is retained by the system until the application-defined function has run to completion. This parameter cannot be `NULL`.

- `context` — The application-defined context parameter to pass to the application-defined function.

- `work` — The application-defined function to invoke on the target queue. The first parameter passed to this function is the value in the `context` parameter.

## Discussion

This function schedules a notification block to be submitted to the specified queue when all blocks associated with the dispatch group have completed. If the group is empty (no block objects are associated with the dispatch group), the notification block object is submitted immediately.

When the notification block is submitted, the group is empty, and can be reused for additional blocks. See [dispatch_group_async](dispatch_group_async.md) for more information.

If your app isn’t using ARC, you should call [dispatch_release](dispatch_release.md) on a dispatch group when it’s no longer needed.

## See Also

### Adding a Completion Handler

- [dispatch_group_notify](dispatch_group_notify.md) — Schedules a block object to be submitted to a queue when a group of previously submitted block objects have completed.
