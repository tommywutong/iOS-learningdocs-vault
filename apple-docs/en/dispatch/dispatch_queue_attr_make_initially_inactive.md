---
title: dispatch_queue_attr_make_initially_inactive
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_queue_attr_make_initially_inactive
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_queue_attr_make_initially_inactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_queue_attr_make_initially_inactive.json'
content_hash: 'sha256:0de5c0e733882865'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_queue_attr_make_initially_inactive

<sub>Function</sub>

Returns an attribute that configures a dispatch queue as initially inactive.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern dispatch_queue_attr_tdispatch_queue_attr_make_initially_inactive(dispatch_queue_attr_t attr);
```

## Parameters

- `attr` — Other queue attributes that you want to combine with the initially inactive attribute.

## Return Value

An updated set of queue attributes that includes the initially inactive attribute.

## Discussion

When you configure a dispatch queue with this attribute, the queue does not execute tasks until you call its [dispatch_activate](<dispatchobject/activate().md>) method.

## See Also

### Configuring Queue Execution Parameters

- [dispatch_queue_attr_t](dispatch_queue_attr_t.md) — Attributes describing the behaviors of a dispatch queue.
- [dispatch_queue_attr_make_with_qos_class](dispatch_queue_attr_make_with_qos_class.md) — Returns attributes suitable for creating a dispatch queue with the desired quality-of-service information.
- [dispatch_queue_get_qos_class](dispatch_queue_get_qos_class.md) — Returns the quality-of-service class for the specified queue.
- [dispatch_qos_class_t](dispatch_qos_class_t.md) — Quality-of-service classes that specify the priorities for executing tasks.
- [dispatch_queue_attr_make_with_autorelease_frequency](dispatch_queue_attr_make_with_autorelease_frequency.md) — Returns an attribute that specifies how the dispatch queue manages autorelease pools for the blocks it executes.
- [dispatch_autorelease_frequency_t](dispatch_autorelease_frequency_t.md) — Constants indicating the frequency with which a dispatch queue creates autorelease pools for its tasks.
