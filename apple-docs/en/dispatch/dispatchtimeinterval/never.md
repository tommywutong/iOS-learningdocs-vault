---
title: DispatchTimeInterval.never
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchtimeinterval/never
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchtimeinterval/never'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchtimeinterval/never.json'
content_hash: 'sha256:a3e4c54c1461fd01'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchTimeInterval](../dispatchtimeinterval.md)

# DispatchTimeInterval.never

<sub>Case</sub>

No interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case never
```

## Discussion

Use this case to specify a time interval that never occurs. For example, specify this value for a timer’s repeat interval to prevent a timer from repeating.

## See Also

### Enumeration Cases

- [DispatchTimeInterval.seconds(_:)](<seconds(__).md>) — A number of seconds.
- [DispatchTimeInterval.milliseconds(_:)](<milliseconds(__).md>) — A number of milliseconds.
- [DispatchTimeInterval.microseconds(_:)](<microseconds(__).md>) — A number of microseconds.
- [DispatchTimeInterval.nanoseconds(_:)](<nanoseconds(__).md>) — A number of nanoseconds.
