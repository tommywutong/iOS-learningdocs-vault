---
title: CLMonitoringState
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clmonitoringstate
source_url: 'https://developer.apple.com/documentation/corelocation/clmonitoringstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clmonitoringstate.json'
content_hash: 'sha256:01087700d1ed090f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLMonitoringState

<sub>Enumeration</sub>

Values that represent the current state of a monitoring condition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
enum CLMonitoringState : NSUInteger;
```

## Topics

### Condition states

- [CLMonitoringStateSatisfied](clmonitoringstate/clmonitoringstatesatisfied.md) — The condition is in a satisfied state.
- [CLMonitoringStateUnknown](clmonitoringstate/clmonitoringstateunknown.md) — The condition is in an unknown state.
- [CLMonitoringStateUnsatisfied](clmonitoringstate/clmonitoringstateunsatisfied.md) — The condition is in an unsatisfied state.
- [CLMonitoringStateUnmonitored](clmonitoringstate/clmonitoringstateunmonitored.md) — The condition is in an unmonitored state.

## See Also

### Event properties

- [date](clmonitoringevent/date.md) — The date the event occurs.
- [identifier](clmonitoringevent/identifier.md) — A string that represents the identifier of a monitored condition.
- [refinement](clmonitoringevent/refinement.md) — An optional instance of a condition that represents the most specific condition to that this event can apply to.
- [state](clmonitoringevent/state.md) — The state of the condition at the time of the event.
