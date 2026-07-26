---
title: 'distance(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/schedulertimetype/distance(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/schedulertimetype/distance%28to%3A%29.json'
content_hash: 'sha256:14f50995185affa1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RunLoop](../../runloop.md) · [SchedulerTimeType](../schedulertimetype.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the distance to another run loop scheduler time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: RunLoop.SchedulerTimeType) -> RunLoop.SchedulerTimeType.Stride
```

## Parameters

- `other` — Another run loop time.

## Return Value

The time interval between this time and the provided time.

## See Also

### Working with Scheduler Time Intervals

- [Stride](stride.md) — The interval by which run loop times advance.
- [advanced(by:)](<advanced(by_).md>) — Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.
