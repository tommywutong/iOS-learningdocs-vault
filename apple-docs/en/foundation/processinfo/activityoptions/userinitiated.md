---
title: userInitiated
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/activityoptions/userinitiated
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/activityoptions/userinitiated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/activityoptions/userinitiated.json'
content_hash: 'sha256:cce6b2de2c113bdc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProcessInfo](../../processinfo.md) · [ActivityOptions](../activityoptions.md)

# userInitiated

<sub>Type Property</sub>

A flag to indicate the app is performing a user-requested action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var userInitiated: ProcessInfo.ActivityOptions { get }
```

## Discussion

Examples of user initiated actions are exporting or downloading a user-specified file or dismissing a form sheet.

## See Also

### Constants

- [NSActivityIdleDisplaySleepDisabled](idledisplaysleepdisabled.md) — A flag to require the screen to stay powered on.
- [NSActivityIdleSystemSleepDisabled](idlesystemsleepdisabled.md) — A flag to prevent idle sleep.
- [NSActivitySuddenTerminationDisabled](suddenterminationdisabled.md) — A flag to prevent sudden termination.
- [NSActivityAutomaticTerminationDisabled](automaticterminationdisabled.md) — A flag to prevent automatic termination.
- [NSActivityUserInteractive](userinteractive.md) — A flag to indicate the app is responding to user interaction.
- [NSActivityUserInitiatedAllowingIdleSystemSleep](userinitiatedallowingidlesystemsleep.md) — A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [NSActivityBackground](background.md) — A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [NSActivityLatencyCritical](latencycritical.md) — A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [NSActivityAnimationTrackingEnabled](animationtrackingenabled.md) — A flag to track the activity with an animation signpost interval.
- [NSActivityTrackingEnabled](trackingenabled.md) — A flag to track the activity with a signpost interval.
