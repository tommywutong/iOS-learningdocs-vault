---
title: Clickable Static Text Item
apple_id: DTS10003409
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2004-10-05'
source_url: https://developer.apple.com/library/archive/qa/qa1380/_index.html
archived_at: '2026-07-18T02:30:29.191790Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1380

# Clickable Static Text Item

## Q:  I know this is not in accordance with the Human Interface Guidelines but I really need to have a clickable static text item and even though my static text item is enabled, I never receive its command. What's happening?

A: I know this is not in accordance with the Human Interface Guidelines but I really need to have a clickable static text item and even though my static text item is enabled, I never receive its command. What's happening?

First of all, yes, a clickable static text item is not a good Human Interface since there is nothing in the appearance of the item which lets the user know that he can expect some behavior or action when he is going to click on it, but that being said...

You could install a `kEventControlClick` handler on your static text item and this handler would receive the `mouseDown` events in your item. The problem with that approach is that it is not forgiving and violates even more rules of the Human Interface Guidelines. The user should be able to change his mind in between the moment that he clicked in the item and the moment that he releases the mouse button. The Mac OS Look and Feel is based on the `mouseUp`s, not the `mouseDown`s, thus the usual behavior of tracking the user's actions before acknowledging a successful hit.

The real problem comes from the fact that the static text control, scrupulous in respecting the Human Interface Guidelines, always returns `kControlNoPart` when the `hitTest` message is sent to that item. Thus the tracking process is not started and the hit is never successful and you never receive the command ID that you set for that item.

To elegantly solve the problem, you just have to provide a new handler for the `kEventControlHitTest` event. Something like the code shown in Listing 1:

__Listing 1__  The `hitTest` handler.

```
pascal OSStatus StaticTextHitTestHandler(     EventHandlerCallRef nextHandler, EventRef inEvent, void* userData)     {     OSStatus status = noErr;     ControlRef theControl;     HIPoint hiPoint;     HIRect hiBounds;     Boolean inBouns;     ControlPartCode partCode;      status = GetEventParameter(inEvent, kEventParamDirectObject, typeControlRef,         NULL, sizeof(theControl), NULL, &theControl);     require_noerr(status, ExitHitTest);      status = GetEventParameter(inEvent, kEventParamMouseLocation, typeHIPoint,         NULL, sizeof(hiPoint), NULL, &hiPoint);     require_noerr(status, ExitHitTest);      status = HIViewGetBounds(theControl, &hiBounds);     require_noerr(status, ExitHitTest);      inBounds = (CGRectContainsPoint(hiBounds, hiPoint) == 1);     partCode = (inBounds)?kControlButtonPart:kControlNoPart;     status = SetEventParameter(inEvent, kEventParamControlPart, typeControlPartCode,         sizeof(partCode), &partCode);     require_noerr(status, ExitHitTest);  ExitHitTest:     return status;     }
```

and you install this handler with the code shown in Listing 2:

__Listing 2__  Installing the `hitTest` handler.

```
 EventTypeSpec eventType = {kEventClassControl, kEventControlHitTest};     InstallControlEventHandler(staticTextItemControl,         StaticTextHitTestHandler, 1, &eventType, NULL, NULL);
```

If you do this, then you will receive correctly the command ID in your command process handler and your static text item acts as a push button except that there is no visual feedback during its tracking which still doesn't make it a good Human Interface citizen.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-10-05 | New document that explains how to make a static text item respond to clicks |

