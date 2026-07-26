---
title: 'beginActivity(options:reason:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/beginactivity(options:reason:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/beginactivity(options:reason:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/beginactivity%28options%3Areason%3A%29.json'
content_hash: 'sha256:889674b3e2de99b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# beginActivity(options:reason:)

<sub>Instance Method</sub>

Begin an activity using the given options and reason.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func beginActivity(options: ProcessInfo.ActivityOptions = [], reason: String) -> any NSObjectProtocol
```

## Parameters

- `options` — Options for the activity. See [ActivityOptions](activityoptions.md) for possible values.

- `reason` — A string used in debugging to indicate the reason the activity began.

## Return Value

An object token representing the activity.

## Discussion

Indicate completion of the activity by calling [- endActivity:](<endactivity(__).md>) passing the returned object as the argument.

## See Also

### Managing activities

- [- endActivity:](<endactivity(__).md>) — Ends the given activity.
- [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>) — Synchronously perform an activity defined by a given block using the given options.
- [- performExpiringActivityWithReason:usingBlock:](<performexpiringactivity(withreason_using_).md>) — Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ActivityOptions](activityoptions.md) — Option flags used with [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) and [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>).
