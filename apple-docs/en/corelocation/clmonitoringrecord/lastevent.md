---
title: lastEvent
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringrecord/lastevent
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringrecord/lastevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringrecord/lastevent.json'
content_hash: 'sha256:da8fdee8ff4a4dd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitoringRecord](../clmonitoringrecord.md)

# lastEvent

<sub>Instance Property</sub>

An object that contains the specifics of the most recent event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (strong, readonly) CLMonitoringEvent * lastEvent;
```

## Discussion

This includes the state, the date, and the specifics of the condition, if applicable.

## See Also

### Event properties

- [condition](condition.md) — The condition that the framework is monitoring events for.
