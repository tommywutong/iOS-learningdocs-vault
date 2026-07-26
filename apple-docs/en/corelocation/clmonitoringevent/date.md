---
title: date
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringevent/date
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringevent/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringevent/date.json'
content_hash: 'sha256:a513bac1e204bca6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitoringEvent](../clmonitoringevent.md)

# date

<sub>Instance Property</sub>

The date the event occurs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (strong, readonly) NSDate * date;
```

## See Also

### Event properties

- [identifier](identifier.md) — A string that represents the identifier of a monitored condition.
- [refinement](refinement.md) — An optional instance of a condition that represents the most specific condition to that this event can apply to.
- [state](state.md) — The state of the condition at the time of the event.
- [CLMonitoringState](../clmonitoringstate.md) — Values that represent the current state of a monitoring condition.
