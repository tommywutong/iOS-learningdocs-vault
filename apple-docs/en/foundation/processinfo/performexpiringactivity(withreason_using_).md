---
title: 'performExpiringActivity(withReason:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.2+, iPadOS 8.2+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/processinfo/performexpiringactivity(withreason:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/performexpiringactivity(withreason:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/performexpiringactivity%28withreason%3Ausing%3A%29.json'
content_hash: 'sha256:320dfdbe1faf7f6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# performExpiringActivity(withReason:using:)

<sub>Instance Method</sub>

Performs the specified block asynchronously and notifies you if the process is about to be suspended.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func performExpiringActivity(withReason reason: String, using block: @escaping @Sendable (Bool) -> Void)
```

## Parameters

- `reason` — A string used in debugging to indicate the reason the activity began. This parameter must not be `nil` or an empty string.

- `block` — A block containing the work to be performed by the activity. The block has no return value and takes the following parameter: - **expired** — A Boolean indicating whether the process is about to be suspended. If the value is [true](../../swift/true.md), the process is about to be suspended so you should take whatever steps are needed to stop in progress work. If it is [false](../../swift/false.md), start the planned tasks.

## Discussion

Use this method to perform tasks when your process is executing in the background. This method queues `block` for asynchronous execution on a concurrent queue. When your process is in the background, the method tries to take a task assertion to ensure that your block has time to execute. If it is unable to take a task assertion, or if the time allotted for the task assertion expires, the system executes your block with the parameter set to [true](../../swift/true.md). If it is able to take the task assertion, it executes the block and passes [false](../../swift/false.md) for the expired parameter.

If your block is still executing and the system need to suspend the process, the system executes your block a second time with the `expired` parameter set to [true](../../swift/true.md). Your block must be prepared to handle this case. When the expired parameter is [true](../../swift/true.md), stop any in-progress tasks as quickly as possible.

## See Also

### Managing activities

- [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) — Begin an activity using the given options and reason.
- [- endActivity:](<endactivity(__).md>) — Ends the given activity.
- [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>) — Synchronously perform an activity defined by a given block using the given options.
- [ActivityOptions](activityoptions.md) — Option flags used with [- beginActivityWithOptions:reason:](<beginactivity(options_reason_).md>) and [- performActivityWithOptions:reason:usingBlock:](<performactivity(options_reason_using_).md>).
