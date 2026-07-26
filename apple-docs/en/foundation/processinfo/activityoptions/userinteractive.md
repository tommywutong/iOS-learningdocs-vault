---
title: userInteractive
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/activityoptions/userinteractive
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/activityoptions/userinteractive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/activityoptions/userinteractive.json'
content_hash: 'sha256:f1085cbfe9afb524'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProcessInfo](../../processinfo.md) · [ActivityOptions](../activityoptions.md)

# userInteractive

<sub>Type Property</sub>

A flag to indicate the app is responding to user interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var userInteractive: ProcessInfo.ActivityOptions { get }
```

## Discussion

Examples of user-interactive actions include scrolling and interactively dismissing from a navigation controller.

## See Also

### Constants

- [NSActivityIdleDisplaySleepDisabled](idledisplaysleepdisabled.md) — A flag to require the screen to stay powered on.
- [NSActivityIdleSystemSleepDisabled](idlesystemsleepdisabled.md) — A flag to prevent idle sleep.
- [NSActivitySuddenTerminationDisabled](suddenterminationdisabled.md) — A flag to prevent sudden termination.
- [NSActivityAutomaticTerminationDisabled](automaticterminationdisabled.md) — A flag to prevent automatic termination.
- [NSActivityUserInitiated](userinitiated.md) — A flag to indicate the app is performing a user-requested action.
- [NSActivityUserInitiatedAllowingIdleSystemSleep](userinitiatedallowingidlesystemsleep.md) — A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [NSActivityBackground](background.md) — A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [NSActivityLatencyCritical](latencycritical.md) — A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [NSActivityAnimationTrackingEnabled](animationtrackingenabled.md) — A flag to track the activity with an animation signpost interval.
- [NSActivityTrackingEnabled](trackingenabled.md) — A flag to track the activity with a signpost interval.
