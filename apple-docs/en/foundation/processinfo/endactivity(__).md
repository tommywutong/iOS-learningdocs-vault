---
title: 'endActivity(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/endactivity(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/endactivity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/endactivity%28_%3A%29.json'
content_hash: 'sha256:d3facb6e43856b6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# endActivity(_:)

<sub>Instance Method</sub>

Ends the given activity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func endActivity(_ activity: any NSObjectProtocol)
```

## Parameters

- `activity` — An activity object returned by [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>).

## See Also

### Managing activities

- [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) — Begin an activity using the given options and reason.
- [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>) — Synchronously perform an activity defined by a given block using the given options.
- [- performExpiringActivityWithReason:usingBlock:](<performexpiringactivity(withreason_using_).md>) — Performs the specified block asynchronously and notifies you if the process is about to be suspended.
- [ActivityOptions](activityoptions.md) — Option flags used with [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) and [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>).
