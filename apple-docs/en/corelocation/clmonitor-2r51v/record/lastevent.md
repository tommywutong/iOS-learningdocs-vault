---
title: lastEvent
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v/record/lastevent
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/record/lastevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/record/lastevent.json'
content_hash: 'sha256:eafb87f0fb3d59be'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Location](../../../corelocation.md) · [CLMonitor](../../clmonitor-2r51v.md) · [Record](../record.md)

# lastEvent

<sub>Instance Property</sub>

The most recent event the monitor records.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
let lastEvent: CLMonitor.Event
```

## Discussion

The event record contains the specifics of the most recent event, including its state, date, and the specifics of the condition, if applicable.

## See Also

### Record characteristics

- [condition](condition.md) — The condition that the framework is monitoring for.
