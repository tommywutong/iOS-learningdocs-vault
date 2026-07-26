---
title: 'advanced(by:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/immediatescheduler/schedulertimetype/advanced(by:)'
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/advanced(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler/schedulertimetype/advanced%28by%3A%29.json'
content_hash: 'sha256:f270e1d6df58461f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [ImmediateScheduler](../../immediatescheduler.md) · [SchedulerTimeType](../schedulertimetype.md)

# advanced(by:)

<sub>Instance Method</sub>

Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func advanced(by n: ImmediateScheduler.SchedulerTimeType.Stride) -> ImmediateScheduler.SchedulerTimeType
```

## Parameters

- `n` — The amount to advance by. The `ImmediateScheduler` ignores this value.

## Return Value

An empty `SchedulerTimeType`.

## See Also

### Calculating time offsets

- [distance(to:)](<distance(to_).md>) — Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.
