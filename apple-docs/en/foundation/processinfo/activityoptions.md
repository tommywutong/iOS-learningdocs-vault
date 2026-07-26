---
title: ProcessInfo.ActivityOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/activityoptions
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/activityoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/activityoptions.json'
content_hash: 'sha256:cb07d5888179e898'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# ProcessInfo.ActivityOptions

<sub>Structure</sub>

Option flags used with [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) and [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ActivityOptions
```

## Overview

To include one of these individual flags in one of the sets, use bitwise `OR`; for example, during a presentation you might use:

```objc
NSActivityUserInitiated | NSActivityIdleDisplaySleepDisabled
```

To exclude from one of the sets, use bitwise `AND` with `NOT`; for example, during a user initiated action that may be safely terminated with no application interaction in case of logout you might use:

```objc
NSActivityUserInitiated & ~NSActivitySuddenTerminationDisabled
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSActivityIdleDisplaySleepDisabled](activityoptions/idledisplaysleepdisabled.md) — A flag to require the screen to stay powered on.
- [NSActivityIdleSystemSleepDisabled](activityoptions/idlesystemsleepdisabled.md) — A flag to prevent idle sleep.
- [NSActivitySuddenTerminationDisabled](activityoptions/suddenterminationdisabled.md) — A flag to prevent sudden termination.
- [NSActivityAutomaticTerminationDisabled](activityoptions/automaticterminationdisabled.md) — A flag to prevent automatic termination.
- [NSActivityUserInitiated](activityoptions/userinitiated.md) — A flag to indicate the app is performing a user-requested action.
- [NSActivityUserInteractive](activityoptions/userinteractive.md) — A flag to indicate the app is responding to user interaction.
- [NSActivityUserInitiatedAllowingIdleSystemSleep](activityoptions/userinitiatedallowingidlesystemsleep.md) — A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [NSActivityBackground](activityoptions/background.md) — A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [NSActivityLatencyCritical](activityoptions/latencycritical.md) — A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [NSActivityAnimationTrackingEnabled](activityoptions/animationtrackingenabled.md) — A flag to track the activity with an animation signpost interval.
- [NSActivityTrackingEnabled](activityoptions/trackingenabled.md) — A flag to track the activity with a signpost interval.

### Initializers

- [init(rawValue:)](<activityoptions/init(rawvalue_).md>)
- [NSActivityIdleDisplaySleepDisabled](activityoptions/idledisplaysleepdisabled.md) — A flag to require the screen to stay powered on.
- [NSActivityIdleSystemSleepDisabled](activityoptions/idlesystemsleepdisabled.md) — A flag to prevent idle sleep.
- [NSActivitySuddenTerminationDisabled](activityoptions/suddenterminationdisabled.md) — A flag to prevent sudden termination.
- [NSActivityAutomaticTerminationDisabled](activityoptions/automaticterminationdisabled.md) — A flag to prevent automatic termination.
- [NSActivityUserInitiated](activityoptions/userinitiated.md) — A flag to indicate the app is performing a user-requested action.
- [NSActivityUserInteractive](activityoptions/userinteractive.md) — A flag to indicate the app is responding to user interaction.
- [NSActivityUserInitiatedAllowingIdleSystemSleep](activityoptions/userinitiatedallowingidlesystemsleep.md) — A flag to indicate the app is performing a user-requested action, but that the system can sleep on idle.
- [NSActivityBackground](activityoptions/background.md) — A flag to indicate the app has initiated some kind of work, but not as the direct result of user request.
- [NSActivityLatencyCritical](activityoptions/latencycritical.md) — A flag to indicate the activity requires the highest amount of timer and I/O precision available.
- [NSActivityAnimationTrackingEnabled](activityoptions/animationtrackingenabled.md) — A flag to track the activity with an animation signpost interval.
- [NSActivityTrackingEnabled](activityoptions/trackingenabled.md) — A flag to track the activity with a signpost interval.

## See Also

### Managing activities

- [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) — Begin an activity using the given options and reason.
- [- endActivity:](<endactivity(__).md>) — Ends the given activity.
- [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>) — Synchronously perform an activity defined by a given block using the given options.
- [- performExpiringActivityWithReason:usingBlock:](<performexpiringactivity(withreason_using_).md>) — Performs the specified block asynchronously and notifies you if the process is about to be suspended.
