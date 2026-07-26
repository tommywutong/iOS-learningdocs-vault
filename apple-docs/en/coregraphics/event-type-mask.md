---
title: Event Type Mask
framework: Core Graphics
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/event-type-mask
source_url: 'https://developer.apple.com/documentation/coregraphics/event-type-mask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/event-type-mask.json'
content_hash: 'sha256:1a8ff92b4b76325f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md) · [Quartz Event Services](quartz-event-services.md)

# Event Type Mask

<sub>API Collection</sub>

Specifies an event mask that represents all event types.

## Overview

This constant is typically used with the functions [CGEventTapCreate](<cgevent/tapcreate(tap_place_options_eventsofinterest_callback_userinfo_).md>) and [CGEventTapCreateForPSN](<cgevent/tapcreateforpsn(processserialnumber_place_options_eventsofinterest_callback_userinfo_).md>) to register an event tap that observes all input events.

## See Also

### Constants

- [CGEventField](cgeventfield.md) — Constants used as keys to access specialized fields in low-level events.
- [CGEventFilterMask](cgeventfiltermask.md) — Specify masks for classes of low-level events that can be filtered during event suppression states.
- [CGEventFlags](cgeventflags.md) — Constants that indicate the modifier key state at the time an event is created, as well as other event-related states.
- [CGEventSourceStateID](cgeventsourcestateid.md) — Constants that specify the possible source states of an event source.
- [Event Source Token](event-source-token.md) — Specifies any input event type.
- [CGEventSuppressionState](cgeventsuppressionstate.md) — Specify the event suppression states that can occur after posting an event.
- [CGEventTapLocation](cgeventtaplocation.md) — Constants that specify possible tapping points for events.
- [CGEventTapOptions](cgeventtapoptions.md) — Constants that specify whether a new event tap is an active filter or a passive listener.
- [CGEventTapPlacement](cgeventtapplacement.md) — Constants that specify where a new event tap is inserted into the list of active event taps.
- [CGEventType](cgeventtype.md) — Constants that specify the different types of input events.
- [CGMouseButton](cgmousebutton.md) — Constants that specify buttons on a one, two, or three-button mouse.
- [CGEventMouseSubtype](cgeventmousesubtype.md) — Constants used with the [kCGMouseEventSubtype](cgeventfield/mouseeventsubtype.md) event field.
- [CGScrollEventUnit](cgscrolleventunit.md) — Constants that specify the unit of measurement for a scrolling event.
