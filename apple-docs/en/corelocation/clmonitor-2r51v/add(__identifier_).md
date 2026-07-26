---
title: 'add(_:identifier:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clmonitor-2r51v/add(_:identifier:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/add(_:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/add%28_%3Aidentifier%3A%29.json'
content_hash: 'sha256:90c4a29d22d64fed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-2r51v.md)

# add(_:identifier:)

<sub>Instance Method</sub>

Adds the given condition for monitoring.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func add(_ Condition: any CLCondition, identifier: String)
```

## Parameters

- `Condition` — The condition to monitor.

- `identifier` — A string that identifies the monitored condition.

## Discussion

The framework encapsulates the condition in an instance of [Record](record.md) and then associates the record, along with the condition with the given identifier. The initial state is [CLRegionStateUnknown](../clregionstate/unknown.md).

## See Also

### Adding and removing conditions

- [add(_:identifier:assuming:)](<add(__identifier_assuming_).md>) — Adds the monitoring condition with the identifier and initial state you specify.
- [record(for:)](<record(for_).md>) — A record that contains a condition and the most recent event your app receives.
- [remove(_:)](<remove(__).md>) — Removes the condition and its enclosed record associated with the identifier you provide.
