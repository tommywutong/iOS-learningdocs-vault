---
title: CGSetLocalEventsFilterDuringSupressionState
framework: Core Graphics
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgsetlocaleventsfilterduringsupressionstate
source_url: 'https://developer.apple.com/documentation/coregraphics/cgsetlocaleventsfilterduringsupressionstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgsetlocaleventsfilterduringsupressionstate.json'
content_hash: 'sha256:df12d29c675e215a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGSetLocalEventsFilterDuringSupressionState

<sub>Macro</sub>

<sub>Mac Catalyst, macOS</sub>

```objc
#define CGSetLocalEventsFilterDuringSupressionState(filter, state)
```

## See Also

### Deprecated Functions

- [CGPostKeyboardEvent](<cgpostkeyboardevent(______).md>) — Synthesizes a low-level keyboard event on the local machine. _(deprecated)_
- [CGPostMouseEvent](cgpostmouseevent.md) — Synthesizes a low-level mouse-button event on the local machine. _(deprecated)_
- [CGPostScrollWheelEvent](cgpostscrollwheelevent.md) — Synthesizes a low-level scrolling event on the local machine. _(deprecated)_
- [CGEnableEventStateCombining](<cgenableeventstatecombining(__).md>) — Enables or disables the merging of actual key and mouse state with the application-specified state in a synthetic event. _(deprecated)_
- [CGInhibitLocalEvents](<cginhibitlocalevents(__).md>) — Turns off local hardware events in the current session. _(deprecated)_
- [CGSetLocalEventsFilterDuringSuppressionState](<cgsetlocaleventsfilterduringsuppressionstate(____).md>) — Filters local hardware events from the keyboard and mouse during the short interval after a synthetic event is posted. _(deprecated)_
- [CGSetLocalEventsSuppressionInterval](<cgsetlocaleventssuppressioninterval(__).md>) — Sets the time interval in seconds that local hardware events are suppressed after posting a synthetic event. _(deprecated)_
