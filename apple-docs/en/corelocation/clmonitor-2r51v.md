---
title: CLMonitor
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-2r51v
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v.json'
content_hash: 'sha256:c35166988361b804'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLMonitor

<sub>Class</sub>

An object that monitors the conditions you add to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
actor CLMonitor
```

## Overview

Use `CLMonitor` to monitor for and observe events such as the entry to a specific geographic area or proximity to a beacon with characteristics that you specify.

This service is unavailable in a compatible iPad or iPhone app running in visionOS.

## Relationships

- **Conforms To**: [Actor](../swift/actor.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a monitor

- [init(_:)](<clmonitor-2r51v/init(__).md>) — Creates a location monitor with the name you specify.

### Adding and removing conditions

- [add(_:identifier:)](<clmonitor-2r51v/add(__identifier_).md>) — Adds the given condition for monitoring.
- [add(_:identifier:assuming:)](<clmonitor-2r51v/add(__identifier_assuming_).md>) — Adds the monitoring condition with the identifier and initial state you specify.
- [record(for:)](<clmonitor-2r51v/record(for_).md>) — A record that contains a condition and the most recent event your app receives.
- [remove(_:)](<clmonitor-2r51v/remove(__).md>) — Removes the condition and its enclosed record associated with the identifier you provide.

### Accessing the location monitor’s identifiers

- [identifiers](clmonitor-2r51v/identifiers.md) — An array that contains the identifiers of the conditions the framework is monitoring.

### Accessing the monitor’s events

- [events](clmonitor-2r51v/events-swift.property.md) — An asynchronous sequence of events that represent the conditions the monitor object observes.

### Monitor conditions

- [BeaconIdentityCondition](clmonitor-2r51v/beaconidentitycondition.md) — A condition that describes the characteristics of a beacon.
- [CircularGeographicCondition](clmonitor-2r51v/circulargeographiccondition.md) — A condition that describes a circular geographic area that a center point and radius define.

### Monitor events

- [Event](clmonitor-2r51v/event.md) — An event object that the framework passes to the events sequence in the monitor.
- [Record](clmonitor-2r51v/record.md) — A structure that represents a condition and its associated event information that the framework is monitoring.
- [Events](clmonitor-2r51v/events-swift.struct.md) — A type that represents an asynchronous sequence of events.
