---
title: name
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitorconfiguration/name
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitorconfiguration/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitorconfiguration/name.json'
content_hash: 'sha256:bcef1eda24265df5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitorConfiguration](../clmonitorconfiguration.md)

# name

<sub>Instance Property</sub>

The name of the monitor instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (readonly) NSString * name;
```

## Discussion

`name` can contain only alphanumeric characters and can’t start with an underscore (_).

## See Also

### Instance properties

- [eventHandler](eventhandler.md) — The block the framework calls as the event handler for the location monitor instance.
- [queue](queue.md) — The dispatch queue to bind the instance of a location monitor to.
