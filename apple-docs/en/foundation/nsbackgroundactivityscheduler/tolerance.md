---
title: tolerance
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/tolerance
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/tolerance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/tolerance.json'
content_hash: 'sha256:ff408b87e2b6c0d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# tolerance

<sub>Instance Property</sub>

A value of type [TimeInterval](../timeinterval.md), which specifies a range of time during which the background activity may occur.

<sub>macOS</sub>

```swift
var tolerance: TimeInterval { get set }
```

## Discussion

A nominal fire date for scheduled background activity is calculated based on a combination of the [interval](interval.md) property value and the time the activity began or the last execution date. The [tolerance](tolerance.md) property specifies a grace period—a range of time before and after the nominal fire date, during which the activity may be invoked. As the activity nears the end of its grace period, the system schedules the activity more aggressively. The default tolerance period is half the value of the [interval](interval.md) property. See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Related Documentation

- [TimeInterval](../timeinterval.md) — A number of seconds.

### Background Scheduler Attributes

- [identifier](identifier.md) — A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [repeats](repeats.md) — A Boolean value indicating whether the activity should be rescheduled after it completes.
- [interval](interval.md) — An integer providing a suggested interval between scheduling and invoking the activity.
- [qualityOfService](qualityofservice.md) — A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [shouldDefer](shoulddefer.md) — A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
