---
title: 'addConditionForMonitoring:identifier:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clmonitor-6ynwz/addconditionformonitoring:identifier:'
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz/addconditionformonitoring:identifier:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-6ynwz/addconditionformonitoring%3Aidentifier%3A.json'
content_hash: 'sha256:82e473411156a61d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-6ynwz.md)

# addConditionForMonitoring:identifier:

<sub>Instance Method</sub>

Adds a condition to monitor with the identifier you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) addConditionForMonitoring:(CLCondition *) condition identifier:(NSString *) identifier;
```

## Parameters

- `condition` — A [CLCondition](../clcondition-swift.protocol.md) to monitor for.

- `identifier` — A string you use to identify this condition.

## See Also

### Adding and removing conditions

- [addConditionForMonitoring:identifier:assumedState:](addconditionformonitoring_identifier_assumedstate_.md) — Adds a condition to monitor with the state and identifier you provide.
- [monitoringRecordForIdentifier:](monitoringrecordforidentifier_.md) — Gets the monitoring record containing the condition and most recent monitoring event for the identifier you supply, if applicable.
- [removeConditionFromMonitoringWithIdentifier:](removeconditionfrommonitoringwithidentifier_.md) — Removes the monitoring record with the identifier from monitoring.
