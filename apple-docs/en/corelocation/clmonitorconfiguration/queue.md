---
title: queue
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitorconfiguration/queue
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitorconfiguration/queue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitorconfiguration/queue.json'
content_hash: 'sha256:97c67004a8e2f1d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitorConfiguration](../clmonitorconfiguration.md)

# queue

<sub>Instance Property</sub>

The dispatch queue to bind the instance of a location monitor to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) dispatch_queue_t queue;
```

## Discussion

You need to perform all interactions related to the [CLMonitor](../clmonitor-2r51v.md) instance on this queue, and the framework delivers events that the `CLMonitor` instance generates to the handler on this queue.

## See Also

### Instance properties

- [eventHandler](eventhandler.md) — The block the framework calls as the event handler for the location monitor instance.
- [name](name.md) — The name of the monitor instance.
