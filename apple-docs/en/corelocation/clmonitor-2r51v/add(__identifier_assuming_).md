---
title: 'add(_:identifier:assuming:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clmonitor-2r51v/add(_:identifier:assuming:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/add(_:identifier:assuming:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/add%28_%3Aidentifier%3Aassuming%3A%29.json'
content_hash: 'sha256:6b1b248ae07e8abe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-2r51v.md)

# add(_:identifier:assuming:)

<sub>Instance Method</sub>

Adds the monitoring condition with the identifier and initial state you specify.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func add(_ condition: any CLCondition, identifier: String, assuming state: CLMonitor.Event.State)
```

## Parameters

- `condition` — The condition to monitor.

- `identifier` — A string that identifies the monitored condition.

- `state` — The monitoring state to initialize the condition with.

## See Also

### Adding and removing conditions

- [add(_:identifier:)](<add(__identifier_).md>) — Adds the given condition for monitoring.
- [record(for:)](<record(for_).md>) — A record that contains a condition and the most recent event your app receives.
- [remove(_:)](<remove(__).md>) — Removes the condition and its enclosed record associated with the identifier you provide.
