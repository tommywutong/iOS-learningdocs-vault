---
title: CLMonitor
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitor-6ynwz
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-6ynwz.json'
content_hash: 'sha256:f619688a7eadcf19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLMonitor

<sub>Class</sub>

An object that monitors the conditions you add to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLMonitor : NSObject
```

## Overview

Use `CLMonitor` to monitor for and observe events such as the entry to a specific geographic area or proximity to a beacon with characteristics that you specify.

This service is unavailable in a compatible iPad or iPhone app running in visionOS.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Creating a monitor

- [requestMonitorWithConfiguration:completion:](clmonitor-6ynwz/requestmonitorwithconfiguration_completion_.md) — Creates a location monitor with the configuration and event handler you provide.
- [CLMonitorConfiguration](clmonitorconfiguration.md) — An object for configuring a location monitor instance.

### Accessing the location monitor’s identifiers

- [monitoredIdentifiers](clmonitor-6ynwz/monitoredidentifiers.md) — An array that contains all the identifiers for each condition that the monitor is monitoring.
- [name](clmonitor-6ynwz/name.md) — The name associated with the location monitor instance.

### Adding and removing conditions

- [addConditionForMonitoring:identifier:](clmonitor-6ynwz/addconditionformonitoring_identifier_.md) — Adds a condition to monitor with the identifier you provide.
- [addConditionForMonitoring:identifier:assumedState:](clmonitor-6ynwz/addconditionformonitoring_identifier_assumedstate_.md) — Adds a condition to monitor with the state and identifier you provide.
- [monitoringRecordForIdentifier:](clmonitor-6ynwz/monitoringrecordforidentifier_.md) — Gets the monitoring record containing the condition and most recent monitoring event for the identifier you supply, if applicable.
- [removeConditionFromMonitoringWithIdentifier:](clmonitor-6ynwz/removeconditionfrommonitoringwithidentifier_.md) — Removes the monitoring record with the identifier from monitoring.

### Location monitor events

- [CLMonitoringEvent](clmonitoringevent.md) — The object that the framework passes to the monitor’s callback handler upon receiving an event.
- [CLMonitoringRecord](clmonitoringrecord.md) — An object that represents a condition and its associated information that a location monitor is monitoring.

### Location monitor conditions

- [CLCircularGeographicCondition](clcirculargeographiccondition.md) — A circular geographic condition that a center point and radius define.
- [CLBeaconIdentityCondition](clbeaconidentitycondition.md) — A condition that describes the identity characteristics of a beacon.

## See Also

### Monitoring

- [CLUpdate](clupdate.md) — An object that represents a location update.
