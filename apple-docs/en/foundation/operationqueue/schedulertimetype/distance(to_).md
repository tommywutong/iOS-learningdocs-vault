---
title: 'distance(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/schedulertimetype/distance(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/schedulertimetype/distance%28to%3A%29.json'
content_hash: 'sha256:bd1e93c2df487480'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [OperationQueue](../../operationqueue.md) · [SchedulerTimeType](../schedulertimetype.md)

# distance(to:)

<sub>Instance Method</sub>

The distance to another operation queue scheduler time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: OperationQueue.SchedulerTimeType) -> OperationQueue.SchedulerTimeType.Stride
```

## Parameters

- `other` — Another operation queue scheduler time.

## Return Value

The time interval between this time and the other time.

## See Also

### Managing Scheduler Time Type Properties

- [date](date.md) — The date this type represents.
- [advanced(by:)](<advanced(by_).md>) — Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.
- [Stride](stride.md) — The interval by which operation queue times advance.
