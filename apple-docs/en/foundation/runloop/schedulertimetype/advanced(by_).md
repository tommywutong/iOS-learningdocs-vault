---
title: 'advanced(by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/runloop/schedulertimetype/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/foundation/runloop/schedulertimetype/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/runloop/schedulertimetype/advanced%28by%3A%29.json'
content_hash: 'sha256:2efcb80e4bce9471'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [RunLoop](../../runloop.md) · [SchedulerTimeType](../schedulertimetype.md)

# advanced(by:)

<sub>Instance Method</sub>

Returns a run loop scheduler time calculated by advancing this instance’s time by the given interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by n: RunLoop.SchedulerTimeType.Stride) -> RunLoop.SchedulerTimeType
```

## Parameters

- `n` — A time interval to advance.

## Return Value

A dispatch queue time advanced by the given interval from this instance’s time.

## See Also

### Working with Scheduler Time Intervals

- [Stride](stride.md) — The interval by which run loop times advance.
- [distance(to:)](<distance(to_).md>) — Returns the distance to another run loop scheduler time.
