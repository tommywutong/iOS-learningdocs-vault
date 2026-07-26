---
title: interval
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/interval
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/interval'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/interval.json'
content_hash: 'sha256:dad864efb2455e0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# interval

<sub>Instance Property</sub>

An integer providing a suggested interval between scheduling and invoking the activity.

<sub>macOS</sub>

```swift
var interval: TimeInterval { get set }
```

## Discussion

For repeating activities, the value of this property is also the suggested interval between invocations. See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Background Scheduler Attributes

- [identifier](identifier.md) — A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [repeats](repeats.md) — A Boolean value indicating whether the activity should be rescheduled after it completes.
- [qualityOfService](qualityofservice.md) — A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [shouldDefer](shoulddefer.md) — A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [tolerance](tolerance.md) — A value of type [TimeInterval](../timeinterval.md), which specifies a range of time during which the background activity may occur.
