---
title: dispatch_workloop_set_autorelease_frequency
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_workloop_set_autorelease_frequency
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_workloop_set_autorelease_frequency'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_workloop_set_autorelease_frequency.json'
content_hash: 'sha256:6be42bca7f487245'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_workloop_set_autorelease_frequency

<sub>Function</sub>

Configures how the workloop manages the autorelease pools for the blocks it executes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_workloop_set_autorelease_frequency(dispatch_workloop_t workloop, dispatch_autorelease_frequency_t frequency);
```

## Parameters

- `workloop` — The workloop object you want to modify.

- `frequency` — The autorelease behavior attribute to apply to the dispatch queue. For a list of possible values, see [dispatch_autorelease_frequency_t](dispatch_autorelease_frequency_t.md).

## See Also

### Configuring the Workloop Behavior

- [dispatch_set_qos_class_floor](dispatch_set_qos_class_floor.md) — Specifies the minimum quality-of-service level for a dispatch queue, source, or workloop.
- [dispatch_queue_get_qos_class](dispatch_queue_get_qos_class.md) — Returns the quality-of-service class for the specified queue.
