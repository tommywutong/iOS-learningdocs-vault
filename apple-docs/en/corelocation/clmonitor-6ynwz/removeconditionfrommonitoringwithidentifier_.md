---
title: 'removeConditionFromMonitoringWithIdentifier:'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clmonitor-6ynwz/removeconditionfrommonitoringwithidentifier:'
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-6ynwz/removeconditionfrommonitoringwithidentifier:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-6ynwz/removeconditionfrommonitoringwithidentifier%3A.json'
content_hash: 'sha256:69c74076d4c89f7e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-6ynwz.md)

# removeConditionFromMonitoringWithIdentifier:

<sub>Instance Method</sub>

Removes the monitoring record with the identifier from monitoring.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) removeConditionFromMonitoringWithIdentifier:(NSString *) identifier;
```

## Parameters

- `identifier` — A string that identifies the monitoring record.

## See Also

### Adding and removing conditions

- [addConditionForMonitoring:identifier:](addconditionformonitoring_identifier_.md) — Adds a condition to monitor with the identifier you provide.
- [addConditionForMonitoring:identifier:assumedState:](addconditionformonitoring_identifier_assumedstate_.md) — Adds a condition to monitor with the state and identifier you provide.
- [monitoringRecordForIdentifier:](monitoringrecordforidentifier_.md) — Gets the monitoring record containing the condition and most recent monitoring event for the identifier you supply, if applicable.
