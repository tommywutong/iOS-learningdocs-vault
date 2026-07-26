---
title: qualityOfService
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/qualityofservice
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/qualityofservice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/qualityofservice.json'
content_hash: 'sha256:009c66f7cc1fbee6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# qualityOfService

<sub>Instance Property</sub>

A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.

<sub>macOS</sub>

```swift
var qualityOfService: QualityOfService { get set }
```

## Discussion

Options include:

- NSQualityOfServiceUserInteractive
- NSQualityOfServiceUserInitiated
- NSQualityOfServiceUtility
- NSQualityOfServiceBackground

The default value is `NSQualityOfServiceBackground`. If you upgrade the quality of service above this level, the system schedules the activity more aggressively. The default value is the recommended value for most activities. See [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties). For information about quality of service, see [Prioritize Work at the Task Level](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/PrioritizeWorkAtTheTaskLevel.html#//apple_ref/doc/uid/TP40013929-CH35) in [Energy Efficiency Guide for Mac Apps](https://developer.apple.com/library/archive/documentation/Performance/Conceptual/power_efficiency_guidelines_osx/index.html#//apple_ref/doc/uid/TP40013929).

## See Also

### Background Scheduler Attributes

- [identifier](identifier.md) — A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [repeats](repeats.md) — A Boolean value indicating whether the activity should be rescheduled after it completes.
- [interval](interval.md) — An integer providing a suggested interval between scheduling and invoking the activity.
- [shouldDefer](shoulddefer.md) — A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.
- [tolerance](tolerance.md) — A value of type [TimeInterval](../timeinterval.md), which specifies a range of time during which the background activity may occur.
