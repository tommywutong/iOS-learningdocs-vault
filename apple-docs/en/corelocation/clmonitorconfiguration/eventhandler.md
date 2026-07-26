---
title: eventHandler
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitorconfiguration/eventhandler
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitorconfiguration/eventhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitorconfiguration/eventhandler.json'
content_hash: 'sha256:1a720ff8c903ca63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitorConfiguration](../clmonitorconfiguration.md)

# eventHandler

<sub>Instance Property</sub>

The block the framework calls as the event handler for the location monitor instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) void (^eventHandler)(CLMonitor *monitor, CLMonitoringEvent *event);
```

## See Also

### Instance properties

- [name](name.md) — The name of the monitor instance.
- [queue](queue.md) — The dispatch queue to bind the instance of a location monitor to.
