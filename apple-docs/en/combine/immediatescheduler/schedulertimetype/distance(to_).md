---
title: 'distance(to:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/immediatescheduler/schedulertimetype/distance(to:)'
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/distance(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler/schedulertimetype/distance%28to%3A%29.json'
content_hash: 'sha256:5d1e0265d4c046fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [ImmediateScheduler](../../immediatescheduler.md) · [SchedulerTimeType](../schedulertimetype.md)

# distance(to:)

<sub>Instance Method</sub>

Returns the distance to another immediate scheduler time; this distance is always `0` in the context of an immediate scheduler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(to other: ImmediateScheduler.SchedulerTimeType) -> ImmediateScheduler.SchedulerTimeType.Stride
```

## Parameters

- `other` — The other scheduler time.

## Return Value

`0`, as a `Stride`.

## See Also

### Calculating time offsets

- [advanced(by:)](<advanced(by_).md>) — Advances the time by the specified amount; this is meaningless in the context of an immediate scheduler.
