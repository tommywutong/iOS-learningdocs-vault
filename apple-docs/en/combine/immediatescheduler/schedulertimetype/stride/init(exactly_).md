---
title: 'init(exactly:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/immediatescheduler/schedulertimetype/stride/init(exactly:)'
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler/schedulertimetype/stride/init(exactly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler/schedulertimetype/stride/init%28exactly%3A%29.json'
content_hash: 'sha256:4ee6aad5647580f7'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Combine](../../../../combine.md) · [ImmediateScheduler](../../../immediatescheduler.md) · [SchedulerTimeType](../../schedulertimetype.md) · [Stride](../stride.md)

# init(exactly:)

<sub>Initializer</sub>

Creates an immediate scheduler time interval from a binary integer type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<T>(exactly source: T) where T : BinaryInteger
```

## Discussion

If `exactly` can’t convert to an `Int`, the resulting time interval is `nil`.

## See Also

### Creating Scheduler Time Strides

- [init(_:)](<init(__).md>) — Creates an immediate scheduler time interval from the given time interval.
- [init(floatLiteral:)](<init(floatliteral_).md>) — Creates an immediate scheduler time interval from a floating-point seconds value.
- [init(integerLiteral:)](<init(integerliteral_).md>) — Creates an immediate scheduler time interval from an integer seconds value.
