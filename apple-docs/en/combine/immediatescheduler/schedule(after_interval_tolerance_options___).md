---
title: 'schedule(after:interval:tolerance:options:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/immediatescheduler/schedule(after:interval:tolerance:options:_:)'
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler/schedule(after:interval:tolerance:options:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler/schedule%28after%3Ainterval%3Atolerance%3Aoptions%3A_%3A%29.json'
content_hash: 'sha256:0139fb097c833694'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [ImmediateScheduler](../immediatescheduler.md)

# schedule(after:interval:tolerance:options:_:)

<sub>Instance Method</sub>

Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func schedule(after date: ImmediateScheduler.SchedulerTimeType, interval: ImmediateScheduler.SchedulerTimeType.Stride, tolerance: ImmediateScheduler.SchedulerTimeType.Stride, options: ImmediateScheduler.SchedulerOptions?, _ action: @escaping () -> Void) -> any Cancellable
```

## Discussion

The immediate scheduler ignores `date` and performs the action immediately.

## See Also

### Scheduling actions

- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
