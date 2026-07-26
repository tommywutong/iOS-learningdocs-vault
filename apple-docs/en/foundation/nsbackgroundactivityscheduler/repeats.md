---
title: repeats
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/repeats
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/repeats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/repeats.json'
content_hash: 'sha256:8d64cd167efbafc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# repeats

<sub>Instance Property</sub>

A Boolean value indicating whether the activity should be rescheduled after it completes.

<sub>macOS</sub>

```swift
var repeats: Bool { get set }
```

## Discussion

The default value for this property is [false](../../swift/false.md). See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Background Scheduler Attributes

- [identifier](identifier.md) — A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [interval](interval.md) — An integer providing a suggested interval between scheduling and invoking the activity.
- [qualityOfService](qualityofservice.md) — A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [shouldDefer](shoulddefer.md) — A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [tolerance](tolerance.md) — A value of type [TimeInterval](../timeinterval.md), which specifies a range of time during which the background activity may occur.
