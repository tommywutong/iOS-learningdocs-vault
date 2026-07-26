---
title: 'record(for:)'
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/clmonitor-2r51v/record(for:)'
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/record(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitor-2r51v/record%28for%3A%29.json'
content_hash: 'sha256:f6375a216672f17e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitor](../clmonitor-2r51v.md)

# record(for:)

<sub>Instance Method</sub>

A record that contains a condition and the most recent event your app receives.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
func record(for identifier: String) -> CLMonitor.Record?
```

## Parameters

- `identifier` — A string that identifies the monitored condition.

## Return Value

Returns a [Record](record.md), or `nil` if the system can’t find the identifier.

## See Also

### Adding and removing conditions

- [add(_:identifier:)](<add(__identifier_).md>) — Adds the given condition for monitoring.
- [add(_:identifier:assuming:)](<add(__identifier_assuming_).md>) — Adds the monitoring condition with the identifier and initial state you specify.
- [remove(_:)](<remove(__).md>) — Removes the condition and its enclosed record associated with the identifier you provide.
