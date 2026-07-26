---
title: identifier
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringevent/identifier
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringevent/identifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringevent/identifier.json'
content_hash: 'sha256:d0ac62c4d7a03589'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitoringEvent](../clmonitoringevent.md)

# identifier

<sub>Instance Property</sub>

A string that represents the identifier of a monitored condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (strong, readonly) NSString * identifier;
```

## See Also

### Event properties

- [date](date.md) — The date the event occurs.
- [refinement](refinement.md) — An optional instance of a condition that represents the most specific condition to that this event can apply to.
- [state](state.md) — The state of the condition at the time of the event.
- [CLMonitoringState](../clmonitoringstate.md) — Values that represent the current state of a monitoring condition.
