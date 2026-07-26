---
title: suddenTerminationDisabled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/activityoptions/suddenterminationdisabled
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/activityoptions/suddenterminationdisabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/activityoptions/suddenterminationdisabled.json'
content_hash: 'sha256:76579942718e597b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProcessInfo](../../processinfo.md) · [ActivityOptions](../activityoptions.md)

# suddenTerminationDisabled

<sub>Type Property</sub>

A flag to prevent sudden termination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var suddenTerminationDisabled: ProcessInfo.ActivityOptions { get }
```

## Discussion

This is included by [NSActivityUserInitiatedAllowingIdleSystemSleep](userinitiatedallowingidlesystemsleep.md).

## See Also

### Constants

- [NSActivityIdleDisplaySleepDisabled](idledisplaysleepdisabled.md) — A flag to require the screen to stay powered on.
- [NSActivityIdleSystemSleepDisabled](idlesystemsleepdisabled.md) — A flag to prevent idle sleep.
- [NSActivityAutomaticTerminationDisabled](automaticterminationdisabled.md) — A flag to prevent automatic termination.
- [NSActivityUserInitiated](userinitiated.md) — A flag to indicate the app is performing a user-requested action.
- [NSActivityUserInteractive](userinteractive.md) — A flag to indicate the app is responding to user interaction.
- [NSActivityUserInitiatedAllowingIdleSystemSleep](userinitiatedallowingidlesystemsleep.md) — A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [NSActivityBackground](background.md) — A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [NSActivityLatencyCritical](latencycritical.md) — A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [NSActivityAnimationTrackingEnabled](animationtrackingenabled.md) — A flag to track the activity with an animation signpost interval.
- [NSActivityTrackingEnabled](trackingenabled.md) — A flag to track the activity with a signpost interval.
