---
title: refinement
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringevent/refinement
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringevent/refinement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringevent/refinement.json'
content_hash: 'sha256:b3089768a989752f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLMonitoringEvent](../clmonitoringevent.md)

# refinement

<sub>Instance Property</sub>

An optional instance of a condition that represents the most specific condition to that this event can apply to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (strong, readonly) CLCondition * refinement;
```

## Discussion

The type of the refinement condition depends on the monitored condition itself.

## See Also

### Event properties

- [date](date.md) — The date the event occurs.
- [identifier](identifier.md) — A string that represents the identifier of a monitored condition.
- [state](state.md) — The state of the condition at the time of the event.
- [CLMonitoringState](../clmonitoringstate.md) — Values that represent the current state of a monitoring condition.
