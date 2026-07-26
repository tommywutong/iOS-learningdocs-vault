---
title: shouldDefer
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsbackgroundactivityscheduler/shoulddefer
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/shoulddefer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/shoulddefer.json'
content_hash: 'sha256:655c3077c2e94e56'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# shouldDefer

<sub>Instance Property</sub>

A Boolean value indicating whether your app should stop performing background activity and resume at a more optimal time.

<sub>macOS</sub>

```swift
var shouldDefer: Bool { get }
```

## Discussion

Your app can check the `shouldDefer` property while executing scheduled background activity. If this property contains a value of [true](../../swift/true.md), system conditions have changed since the time the activity started and deferral is recommended. For example, perhaps the user unplugged the Mac and it’s now running on battery power. In this case, your app should finish what it’s currently doing, save its state, and invoke its completion handler with a value of [NSBackgroundActivityResultDeferred](result/deferred.md). The system will invoke your activity again at a more optimal time, and your app can restore its previous state and resume where it left off. See [Detect Whether to Defer Activity](../nsbackgroundactivityscheduler.md#Detect-Whether-to-Defer-Activity) and [Configure Scheduler Properties](../nsbackgroundactivityscheduler.md#Configure-Scheduler-Properties).

## See Also

### Related Documentation

- [Result](result.md) — These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.

### Background Scheduler Attributes

- [identifier](identifier.md) — A unique reverse DNS notation string, such as `com.example.MyApp.updatecheck`, that identifies the activity.
- [repeats](repeats.md) — A Boolean value indicating whether the activity should be rescheduled after it completes.
- [interval](interval.md) — An integer providing a suggested interval between scheduling and invoking the activity.
- [qualityOfService](qualityofservice.md) — A value of type `NSQualityOfService`, which controls how aggressively the system schedules the activity.
- [tolerance](tolerance.md) — A value of type [TimeInterval](../timeinterval.md), which specifies a range of time during which the background activity may occur.
