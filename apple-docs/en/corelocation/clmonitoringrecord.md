---
title: CLMonitoringRecord
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringrecord
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringrecord'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringrecord.json'
content_hash: 'sha256:b252dd2ef7c91c55'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLMonitoringRecord

<sub>Class</sub>

An object that represents a condition and its associated information that a location monitor is monitoring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLMonitoringRecord : NSObject
```

## Overview

When handling a new [CLMonitoringEvent](clmonitoringevent.md), the `CLMonitoringRecord` available for the indicated identifier from the [CLMonitor](clmonitor-2r51v.md) contains the prior event. The `CLMonitoringRecord` updates with the new event when the handling is complete.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Event properties

- [condition](clmonitoringrecord/condition.md) — The condition that the framework is monitoring events for.
- [lastEvent](clmonitoringrecord/lastevent.md) — An object that contains the specifics of the most recent event.

## See Also

### Location monitor events

- [CLMonitoringEvent](clmonitoringevent.md) — The object that the framework passes to the monitor’s callback handler upon receiving an event.
