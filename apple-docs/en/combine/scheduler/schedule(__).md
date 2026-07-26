---
title: 'schedule(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/scheduler/schedule(_:)'
source_url: 'https://developer.apple.com/documentation/combine/scheduler/schedule(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/scheduler/schedule%28_%3A%29.json'
content_hash: 'sha256:efbccac2deeb7f7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Scheduler](../scheduler.md)

# schedule(_:)

<sub>Instance Method</sub>

Performs the action at the next possible opportunity, without options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(_ action: @escaping () -> Void)
```

## See Also

### Scheduling actions

- [schedule(after:_:)](<schedule(after___).md>) — Performs the action at some time after the specified date, using the scheduler’s minimum tolerance.
- [schedule(after:interval:_:)](<schedule(after_interval___).md>) — Performs the action at some time after the specified date, at the specified frequency, using minimum tolerance possible for this Scheduler.
- [schedule(after:interval:tolerance:_:)](<schedule(after_interval_tolerance___).md>) — Performs the action at some time after the specified date, at the specified frequency, taking into account tolerance if possible.
- [schedule(after:interval:tolerance:options:_:)](<schedule(after_interval_tolerance_options___).md>) — Performs the action at some time after the specified date, at the specified frequency, optionally taking into account tolerance if possible.
- [schedule(after:tolerance:_:)](<schedule(after_tolerance___).md>) — Performs the action at some time after the specified date.
- [schedule(after:tolerance:options:_:)](<schedule(after_tolerance_options___).md>) — Performs the action at some time after the specified date.
- [schedule(options:_:)](<schedule(options___).md>) — Performs the action at the next possible opportunity.
