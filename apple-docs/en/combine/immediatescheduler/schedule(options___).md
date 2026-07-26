---
title: 'schedule(options:_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/immediatescheduler/schedule(options:_:)'
source_url: 'https://developer.apple.com/documentation/combine/immediatescheduler/schedule(options:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/immediatescheduler/schedule%28options%3A_%3A%29.json'
content_hash: 'sha256:c0a75c5c925ebe31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [ImmediateScheduler](../immediatescheduler.md)

# schedule(options:_:)

<sub>Instance Method</sub>

Performs the action at the next possible opportunity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(options: ImmediateScheduler.SchedulerOptions?, _ action: @escaping () -> Void)
```

## See Also

### Scheduling actions

- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date.
