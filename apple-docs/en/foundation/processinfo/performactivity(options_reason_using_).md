---
title: 'performActivity(options:reason:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/performactivity(options:reason:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/performactivity(options:reason:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/performactivity%28options%3Areason%3Ausing%3A%29.json'
content_hash: 'sha256:7459511f05864169'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# performActivity(options:reason:using:)

<sub>Instance Method</sub>

Synchronously perform an activity defined by a given block using the given options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performActivity(options: ProcessInfo.ActivityOptions = [], reason: String, using block: @escaping () -> Void)
```

## Parameters

- `options` — Options for the activity. See [ActivityOptions](activityoptions.md) for possible values.

- `reason` — A string used in debugging to indicate the reason the activity began.

- `block` — A block containing the work to be performed by the activity.

## Discussion

The activity will be automatically ended after `block` returns.

## See Also

### Managing activities

- [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) — Begin an activity using the given options and reason.
- [- endActivity:](<endactivity(__).md>) — Ends the given activity.
- [- performExpiringActivityWithReason:usingBlock:](<performexpiringactivity(withreason_using_).md>) — Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ActivityOptions](activityoptions.md) — Option flags used with [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) and [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>).
