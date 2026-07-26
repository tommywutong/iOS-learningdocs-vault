---
title: 'schedule(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsbackgroundactivityscheduler/schedule(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/schedule(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbackgroundactivityscheduler/schedule%28_%3A%29.json'
content_hash: 'sha256:ccadcf6ee1857b64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBackgroundActivityScheduler](../nsbackgroundactivityscheduler.md)

# schedule(_:)

<sub>Instance Method</sub>

Begins scheduling the background activity.

<sub>macOS</sub>

```swift
func schedule(_ block: @escaping @Sendable (@escaping NSBackgroundActivityScheduler.CompletionHandler) -> Void)
```

## Parameters

- `block` — A block of code to execute when the scheduler runs. This block will be called on a serial background queue appropriate for the level of quality of service specified. See [qualityOfService](qualityofservice.md).

## Discussion

When your block is called, it’s passed a completion handler as an argument. Configure the block to invoke this handler, passing it a result of type [Result](result.md) to indicate whether the activity finished ([NSBackgroundActivityResultFinished](result/finished.md)) or should be deferred ([NSBackgroundActivityResultDeferred](result/deferred.md)) and rescheduled for a later time. Failure to invoke the completion handler results in the activity not being rescheduled. For work that will be deferred and rescheduled, the block may optionally adjust scheduler properties, such as [interval](interval.md) or [tolerance](tolerance.md), before calling the completion handler. See [Schedule Activity with scheduleWithBlock:](../nsbackgroundactivityscheduler.md#Schedule-Activity-with-scheduleWithBlock).

## See Also

### Related Documentation

- [Result](result.md) — These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.

### Scheduling Activity

- [CompletionHandler](completionhandler.md)
