---
title: identifier
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/identifier
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/identifier.json'
content_hash: 'sha256:302a8a4192e4379c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# identifier

<sub>Instance Property</sub>

A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.

<sub>macOS</sub>

```swift
var identifier: String { get }
```

## Discussion

This string should remain constant for an activity across launches of your app because the system uses this unique identifier to track the number of times the activity has run and to improve the heuristics for deciding when to run it again in the future. `nil` and zero-length strings are not allowed. See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Related Documentation

- [- initWithIdentifier:](<init(identifier_).md>) — Initializes a background activity scheduler object with a specified unique identifier.

### Background Scheduler Attributes

- [repeats](repeats.md) — A Boolean value indicating whether the activity should be rescheduled after it completes.
- [interval](interval.md) — An integer providing a suggested interval between scheduling and invoking the activity.
- [qualityOfService](qualityofservice.md) — A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [shouldDefer](shoulddefer.md) — A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [tolerance](tolerance.md) — A value of type [TimeInterval](../timeinterval.md), which specifies a range of time during which the background activity may occur.
