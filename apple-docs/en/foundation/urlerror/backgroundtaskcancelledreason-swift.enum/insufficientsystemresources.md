---
title: URLError.BackgroundTaskCancelledReason.insufficientSystemResources
framework: Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.enum/insufficientsystemresources
source_url: 'https://developer.apple.com/documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.enum/insufficientsystemresources'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlerror/backgroundtaskcancelledreason-swift.enum/insufficientsystemresources.json'
content_hash: 'sha256:6d6f0386976575dd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [URLError](../../urlerror.md) · [BackgroundTaskCancelledReason](../backgroundtaskcancelledreason-swift.enum.md)

# URLError.BackgroundTaskCancelledReason.insufficientSystemResources

<sub>Case</sub>

A reason that indicates the system canceled the background task because it lacks sufficient resources to perform the task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case insufficientSystemResources
```

## Discussion

This error results from factors including (but not limited to) battery capacity, thermal condition, network connectivity, and cellular data plan.

## See Also

### Cancellation reasons

- [URLError.BackgroundTaskCancelledReason.backgroundUpdatesDisabled](backgroundupdatesdisabled.md) — A reason that indicates the system canceled the background task because background tasks are disabled.
- [URLError.BackgroundTaskCancelledReason.userForceQuitApplication](userforcequitapplication.md) — A reason that indicates the system canceled the background task because the user force-quit the application.
