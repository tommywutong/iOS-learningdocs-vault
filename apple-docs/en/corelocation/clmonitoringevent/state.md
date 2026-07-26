---
title: state
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringevent/state
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringevent/state'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringevent/state.json'
content_hash: 'sha256:9e7ac7856aa22264'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitoringEvent](../clmonitoringevent.md)

# state

<sub>Instance Property</sub>

The state of the condition at the time of the event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) CLMonitoringState state;
```

## See Also

### Event properties

- [date](date.md) — The date the event occurs.
- [identifier](identifier.md) — A string that represents the identifier of a monitored condition.
- [refinement](refinement.md) — An optional instance of a condition that represents the most specific condition to that this event can apply to.
- [CLMonitoringState](../clmonitoringstate.md) — Values that represent the current state of a monitoring condition.
