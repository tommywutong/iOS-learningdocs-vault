---
title: trackingEnabled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/activityoptions/trackingenabled
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/activityoptions/trackingenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/activityoptions/trackingenabled.json'
content_hash: 'sha256:c80ea437bd39ade3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [ProcessInfo](../../processinfo.md) · [ActivityOptions](../activityoptions.md)

# trackingEnabled

<sub>Type Property</sub>

A flag to track the activity with a signpost interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var trackingEnabled: ProcessInfo.ActivityOptions { get }
```

## Discussion

To help you investigate perfomance issues in your app, use [NSActivityTrackingEnabled](trackingenabled.md) to track the timing of a user interaction by annotating the beginning and end of an activity using a signpost interval.

Calling [- beginActivityWithOptions:reason:](<../beginactivity(options_reason_).md>) to begin the activity returns an object token that you retain for the duration of the activity. The logging system produces a distinct message, useful in debugging, if the object token is de-allocated before you call [- endActivity:](<../endactivity(__).md>).

The flag [NSActivityTrackingEnabled](trackingenabled.md) differs from [NSActivityAnimationTrackingEnabled](animationtrackingenabled.md) in the type of interval signposts the logging system emits. Use [NSActivityAnimationTrackingEnabled](animationtrackingenabled.md) when the interaction involves an animation.

## See Also

### Related Documentation

- [Recording Performance Data](../../../os/recording-performance-data.md) — Add signposts to record interesting time-based events.

### Constants

- [NSActivityIdleDisplaySleepDisabled](idledisplaysleepdisabled.md) — A flag to require the screen to stay powered on.
- [NSActivityIdleSystemSleepDisabled](idlesystemsleepdisabled.md) — A flag to prevent idle sleep.
- [NSActivitySuddenTerminationDisabled](suddenterminationdisabled.md) — A flag to prevent sudden termination.
- [NSActivityAutomaticTerminationDisabled](automaticterminationdisabled.md) — A flag to prevent automatic termination.
- [NSActivityUserInitiated](userinitiated.md) — A flag to indicate the app is performing a user-requested action.
- [NSActivityUserInteractive](userinteractive.md) — A flag to indicate the app is responding to user interaction.
- [NSActivityUserInitiatedAllowingIdleSystemSleep](userinitiatedallowingidlesystemsleep.md) — A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [NSActivityBackground](background.md) — A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [NSActivityLatencyCritical](latencycritical.md) — A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [NSActivityAnimationTrackingEnabled](animationtrackingenabled.md) — A flag to track the activity with an animation signpost interval.
