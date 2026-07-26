---
title: 'init(identifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsbackgroundactivityscheduler/init(identifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/init(identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/init%28identifier%3A%29.json'
content_hash: 'sha256:a94362462793adac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# init(identifier:)

<sub>Initializer</sub>

Initializes a background activity scheduler object with a specified unique identifier.

<sub>macOS</sub>

```swift
init(identifier: String)
```

## Parameters

- `identifier` — A unique string, in reverse DNS notation, that identifies the activity. For example, `com.example.MyApp.updatecheck`. `nil` and zero-length strings are not allowed.

## Return Value

A new background activity scheduler object of type [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md).

## Discussion

The string passed to the `identifier` parameter should remain constant for an activity across launches of your app because the system uses this unique identifier to track the number of times the activity has run and to improve the heuristics for deciding when to run it again in the future. See [Create a Scheduler](../nsbackgroundactivityscheduler.md#Create-a-Scheduler).

## See Also

### Related Documentation

- [identifier](identifier.md) — A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
