---
title: CLMonitorConfiguration
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitorconfiguration
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitorconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitorconfiguration.json'
content_hash: 'sha256:e12ea991cb777b27'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLMonitorConfiguration

<sub>Class</sub>

An object for configuring a location monitor instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLMonitorConfiguration : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Creating a monitor configuration

- [configWithMonitorName:queue:eventHandler:](clmonitorconfiguration/configwithmonitorname_queue_eventhandler_.md) — Creates a location monitor instance with the name, dispatch queue, and event handler you specify.

### Instance properties

- [eventHandler](clmonitorconfiguration/eventhandler.md) — The block the framework calls as the event handler for the location monitor instance.
- [name](clmonitorconfiguration/name.md) — The name of the monitor instance.
- [queue](clmonitorconfiguration/queue.md) — The dispatch queue to bind the instance of a location monitor to.

## See Also

### Creating a monitor

- [requestMonitorWithConfiguration:completion:](clmonitor-6ynwz/requestmonitorwithconfiguration_completion_.md) — Creates a location monitor with the configuration and event handler you provide.
