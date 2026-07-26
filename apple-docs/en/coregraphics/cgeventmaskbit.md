---
title: CGEventMaskBit
framework: Core Graphics
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [Mac Catalyst, macOS]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coregraphics/cgeventmaskbit
source_url: 'https://developer.apple.com/documentation/coregraphics/cgeventmaskbit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coregraphics/cgeventmaskbit.json'
content_hash: 'sha256:3c872fd40c2abb8c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Graphics](../coregraphics.md)

# CGEventMaskBit

<sub>Macro</sub>

Generates an event mask for a single type of event.

<sub>Mac Catalyst, macOS</sub>

```objc
#define CGEventMaskBit(eventType)
```

## Parameters

- `eventType` — An event type constant. Pass one of the constants listed in [CGEventType](cgeventtype.md).

## Return Value

An event mask that represents the specified event.

## Discussion

This macro converts an event type constant into a mask. You can use this mask to specify that an event tap should observe the event. For more information, see [CGEventMask](cgeventmask.md).

## See Also

### Working With Event Taps

- [CGEventTapCreate](<cgevent/tapcreate(tap_place_options_eventsofinterest_callback_userinfo_).md>) — Creates an event tap.
- [CGEventTapCreateForPSN](<cgevent/tapcreateforpsn(processserialnumber_place_options_eventsofinterest_callback_userinfo_).md>) — Creates an event tap for a specified process.
- [CGEventTapEnable](<cgevent/tapenable(tap_enable_).md>) — Enables or disables an event tap.
- [CGEventTapIsEnabled](<cgevent/tapisenabled(tap_).md>) — Returns a Boolean value indicating whether an event tap is enabled.
- [CGEventTapPostEvent](<cgevent/tappostevent(__).md>) — Posts a Quartz event from an event tap into the event stream.
- [CGEventPost](<cgevent/post(tap_).md>) — Posts a Quartz event into the event stream at a specified location.
- [CGEventPostToPSN](<cgevent/posttopsn(processserialnumber_).md>) — Posts a Quartz event into the event stream for a specific application.
- [CGGetEventTapList](<cggeteventtaplist(______).md>) — Gets a list of currently installed event taps.
