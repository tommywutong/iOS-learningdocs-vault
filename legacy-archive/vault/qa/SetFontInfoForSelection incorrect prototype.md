---
title: SetFontInfoForSelection incorrect prototype
apple_id: DTS10003395
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-10-04'
source_url: https://developer.apple.com/library/archive/qa/qa1375/_index.html
archived_at: '2026-07-18T02:30:27.702698Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1375

# SetFontInfoForSelection incorrect prototype

## Q:  I'm trying to use the SetFontInfoForSelection API so that my text adapts to the User's choice in the Font Panel but I never receive the notifications, what's going on?

A: I'm trying to use the SetFontInfoForSelection API so that my text adapts to the User's choice in the Font Panel but I never receive the notifications, what's going on?

This is a known bug in the header file FontPanel.h. SetFontInfoForSelection is prototyped to take a HIObjectRef as its fourth and last parameter where in fact, it should be an EventTargetRef. The name of that parameter, iFPEventTarget, reflects more accurately the kind of parameter which is expected.

A simple typecast solves this problem:

__Listing 1__  For a window.

```
SetFontInfoForSelection(..., ..., ..., (HIObjectRef)GetWindowEventTarget(theWindow));
```

or

__Listing 2__  For a control.

```
SetFontInfoForSelection(..., ..., ..., (HIObjectRef)GetControlEventTarget(theControl));
```

Even when the header file is fixed in an upcoming release, the typecast, although unnecessary, will still work correctly.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-04 | New document that describes the incorrect prototyping of the SetFontInfoForSelection API and gives a workaround. |

