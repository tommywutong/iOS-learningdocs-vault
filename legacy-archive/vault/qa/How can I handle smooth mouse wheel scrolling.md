---
title: How can I handle smooth mouse wheel scrolling?
apple_id: DTS10003823
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2005-11-29'
source_url: https://developer.apple.com/library/archive/qa/qa1453/_index.html
archived_at: '2026-07-18T02:30:49.220598Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1453

# How can I handle smooth mouse wheel scrolling?

## Q:  How can I handle smooth mouse wheel scrolling?

A: How can I handle smooth mouse wheel scrolling?

Smooth scrolling on Mac OS X is available when using the Mighty Mouse or the scrolling trackpad hardware of 2005 PowerBooks.

A new Carbon Event was implemented in Tiger (Mac OS X v10.4) to handle this smooth mouse wheel scrolling but it was not documented nor available in the public headers.

This new Carbon Event will be available in a later Development Tools release but you can take advantage of it immediately using the information contained in Listing 1.

In general, if your application uses the standard window event handler and installs kEventMouseWheelMoved event handlers on a view, window, or application event target, then your application will continue to work properly on Tiger. Your application may need to change, however, if you assume that kEventMouseWheelMoved events will be found in the event queue. In that case, you will need to look for kEventMouseScroll events as well.

Prior to Tiger, the kEventMouseWheelMoved event was sent in response to a mouse wheel movement. This event contained an integer value specifying the number of lines (or other discrete document units) that should be scrolled by the application. Scrolling could only occur in one direction at a time, and the event specified whether scrolling should occur in the X axis or Y axis.

In Tiger and later, the kEventMouseScroll event will be sent when smooth-scrolling hardware is in use. Examples of smooth-scrolling hardware are the scrolling trackpad on a 2005 PowerBook or a Mighty Mouse. Other hardware may support this feature in the future. For other types of scroll wheels, kEventMouseWheelMoved is still generated.

kEventMouseScroll is different from kEventMouseWheelMoved in these ways:

- it specifies a scroll amount in both the X and Y axis in the same event.
- the scroll amount is specified in pixels, not in lines.

Prior to Tiger, the toolbox posted kEventMouseWheelMoved events to the main event queue when the user scrolled a mouse wheel, and these events were dispatched to the event dispatcher target by WaitNextEvent and RunApplicationEventLoop. In Tiger and later, the toolbox posts kEventMouseScroll events to the main event queue; it never posts kEventMouseWheelMoved events if smooth scrolling hardware is in use.

When a kEventMouseScroll event is dispatched by the event dispatcher, it is sent to the window target that would have received the kEventMouseWheelMoved event in Panther (Mac OS X v10.3). However, if the window target does not handle the event, then the default HIObject handler will retrieve the kEventMouseWheelMoved event from the kEventParamEventRef parameter of the Scroll event, and send the MouseWheelMoved event to the window. This preserves compatibility with existing applications that only handle the kEventMouseWheelMoved event at the window level.

If neither the kEventMouseScrolled nor the kEventMouseWheelMoved event is handled by the window event target, then the standard window event handler will send the kEventMouseScrolled event to the view under the mouse. If the view does not handle the event, then the default HIObject handler will send the corresponding kEventMouseWheelMoved event to the view under the mouse. This preserves compatibility with applications that only handle the kEventMouseWheelMoved event at the view level. If neither event is handled, then each event will be sent to the view's parent view, and so on up the control hierarchy.

__Listing 1__  kEventMouseScroll header excerpt.

```swift
enum { kEventParamMouseWheelSmoothVerticalDelta       = 'saxy', // typeSInt32 kEventParamMouseWheelSmoothHorizontalDelta     = 'saxx', // typeSInt32 };  /*  *  kEventClassMouse / kEventMouseScroll  *   *  Summary:  *    The user wants to scroll the object underneath the given mouse location  * (the window specified in the kEventParamWindowRef parameter)  *    by the specified number of pixels.  *   *  Mac OS X threading:  *    Not thread safe  *   *  Parameters:  *   * --> kEventParamMouseLocation (in, typeHIPoint)  *          The mouse location, in global coordinates.  *   * --> kEventParamWindowRef (in, typeWindowRef)  *          The window under the mouse.  *   * --> kEventParamWindowMouseLocation (in, typeHIPoint)  *          The window-relative position of the mouse in the window  *          given in the kEventParamWindowRef parameter. 0,0 is at the  *          top left of the structure of the window.  *   * --> kEventParamWindowPartCode (in, typeWindowPartCode)  *          The part code that the mouse location hit in the window.  *          This parameter only exists if the WindowRef parameter  *          exists. This saves you the trouble of calling FindWindow,  *          which is expensive on Mac OS X as it needs to call the  *          Window Server.  *   * --> kEventParamKeyModifiers (in, typeUInt32)  *          The keyboard modifiers that were pressed when the event was  *          generated.  *   * --> kEventParamMouseWheelSmoothVerticalDelta (in, typeSInt32)  *          A typeSInt32 indicating how many pixels to scroll vertically.  *          Do not multiply this by your line height the same way you would  *          for the kEventParamMouseWheelDelta parameter of a  *          kEventMouseWheelMoved event. Both this and the equivalent  *          Horizontal parameter may be present in an event; if so, you  *          should scroll both horizontally and vertically if you can.  *   * --> kEventParamMouseWheelSmoothHorizontalDelta (in, typeSInt32)  *          A typeSInt32 indicating how many pixels to scroll horizontally.  *          Do not multiply this by your line height the same way you would  *          for the kEventParamMouseWheelDelta parameter of a  *          kEventMouseWheelMoved event. Both this and the equivalent  *          Vertical parameter may be present in an event; if so, you  *          should scroll both horizontally and vertically if you can.  *   * --> kEventParamEventRef (in, typeEventRef)  *          A typeEventRef of a compatibility kEventMouseWheelMoved event  *          that corresponds to this event. This parameter may not always be  *          present. This parameter is used by the event dispatching  *          mechanism to make sure that objects which don't register for  *          kEventMouseScroll events can see kEventMouseWheelMoved events  *          instead. You may extract this event and examine its contents  *          if your code requires a kEventMouseWheelMoved event  *   *  Availability:  *    Mac OS X: in version 10.4 and later in Carbon.framework  *    CarbonLib: not available  */ enum {   kEventMouseScroll             = 11 };
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2005-11-29 | New document that details an undocumented Carbon Event which will be added to the public headers in a later DevTools release. |

