---
title: Why am I not receiving kEventControlHit events for some of the parts of my
  custom HIView?
apple_id: DTS10003752
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2005-07-14'
source_url: https://developer.apple.com/library/archive/qa/qa1439/_index.html
archived_at: '2026-07-18T02:30:44.304742Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1439

# Why am I not receiving kEventControlHit events for some of the parts of my custom HIView?

## Q:  Why am I not receiving `kEventControlHit` events for some of the parts of my custom `HIView`?

A: Why am I not receiving `kEventControlHit` events for some of the parts of my custom `HIView`?

The Control Manager of the early days of the Macintosh was using 1 byte part codes. The values from 1 to 127 were available to any non-moving part, while the values from 128 to 255 were reserved for indicators. 0 meant no part.

Since the `HIView` architecture is an extension of the Control Manager, part codes can now use the range 1 to 32767, but the special meaning of the earlier ranges has been preserved. Currently the range 256 to 32767 is meaningful only in HIMenuViews.

If

- you create a custom `HIView`, _and_
- you handle the `kEventControlHitTest` event, _and_
- you wish to receive `kEventControlHit` events, _and/or_
- you wish to receive `kEventCommandProcess` events if your `HIView` has a command ID,

then you must return a part code in the range 1 to 127 in your `kEventControlHitTest` handler.

If you do not wish to reuse the part code range currently used by Apple (1 to 27 in Mac OS X v10.4), we suggest that you use custom part codes starting at 127 and going down if you have multiple parts.

__Listing 1__  Typical `kEventControlHitTest` handler.

```swift
case kEventControlHitTest: {     // the point parameter is in view-local coords.     HIPoint	pt;     GetEventParameter(inEvent, kEventParamMouseLocation, typeHIPoint, NULL, sizeof(pt), NULL, &pt);      HIRect	bounds;     HIViewGetBounds(myData->view, &bounds);      if (CGRectContainsPoint(bounds, pt))     {         ControlPartCode part = 127;          SetEventParameter(inEvent, kEventParamControlPart, typeControlPartCode, sizeof(part), &part);         result = noErr;     }     else         result = eventNotHandledErr;      break; }
```

If you wish to handle `kEventControlTrack` events yourself then you are free to use any part code value between 1 and 32767. You are then responsible for posting or sending the other kinds of events according to your custom `HIView` design.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-07-14 | New document that explains why part codes greater than 127 should not be used |

