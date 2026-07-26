---
title: 'advanced(by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/operationqueue/schedulertimetype/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/foundation/operationqueue/schedulertimetype/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operationqueue/schedulertimetype/advanced%28by%3A%29.json'
content_hash: 'sha256:4b97cf45575bd6e9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [OperationQueue](../../operationqueue.md) · [SchedulerTimeType](../schedulertimetype.md)

# advanced(by:)

<sub>Instance Method</sub>

Calculates an operation queue scheduler time by advancing the scheduler time type’s date by the given interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by n: OperationQueue.SchedulerTimeType.Stride) -> OperationQueue.SchedulerTimeType
```

## Parameters

- `n` — The time interval to advance [date](date.md) by.

## Return Value

An operation queue scheduler time advanced by the given interval from [date](date.md).

## See Also

### Managing Scheduler Time Type Properties

- [date](date.md) — The date this type represents.
- [distance(to:)](<distance(to_).md>) — The distance to another operation queue scheduler time.
- [Stride](stride.md) — The interval by which operation queue times advance.
