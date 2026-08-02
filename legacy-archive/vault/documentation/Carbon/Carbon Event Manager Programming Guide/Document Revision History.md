---
title: Carbon Event Manager Programming Guide
apple_id: TP30000989
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/Carbon_Event_Manager/ApdxARev/CarbonEventsApdxRev.html
archived_at: '2026-07-15T05:22:31.511707Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Carbon Event Manager Programming Guide](Introduction%20to%20Carbon%20Event%20Manager%20Programming%20Guide.md)


[Next](Control%20Events%20Versus%20Classic%20Control%20Messages.md)[Previous](Carbon%20Event%20Manager%20Tasks.md)

# Document Revision History

This table describes the changes to _Carbon Event Manager Programming Guide_.

| __Date__ | __Notes__ |
| 2005-07-07 | Changed title from "Handling Carbon Events." Made minor content updates and bug fixes. |
|  | Added some information about HIView-based mouse tracking areas to [Mouse Tracking Regions (Mac OS X v.10.2 and Later)](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugsceivcesscc). |
|  | Described workaround trick for getting standard application event handlers when processing events manually. |
|  | Removed event parameters appendix (now documented with the event kinds in the API references). |
|  | Added link to _Apple Events Programming Guide_. |
| 2003-06-04 | Added note to [Standard Handlers](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwviucykjcummjqgq) describing the difference between default behavior and standard event handling for an event. |
|  | Updated art files. |
| 2003-04-30 | Specified in the parameter appendix that `kEventWindowContextualMenuSelect` also contains the parameters available to `kEventMouseDown`. |
|  | Also removed superfluous section head. |
| 2002-10-04 | Updated for Mac OS X 10.2. |
|  | Added text to [Carbon Events Versus WaitNextEvent](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwviucykjcummjqg4) indicating that standard menu event and Apple event handlers are installed only when you call `RunApplicationEventLoop`. |
|  | Added warning to [Creating and Registering an Event Handler](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqgu) that plugins must explictly remove any event handlers they install before being unloaded. Otherwise, the system may attempt to call event handler code that no longer exists. Added similar warning to [Installing Timers](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiinfeer2f). |
|  | Corrected error in [Listing 3-4](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiinfekq2f), adding an `EventRef` parameter to the `CallNextEventHandler` call. |
|  | Added new section, [Queue-Synchronized Events (Mac OS X v.10.2 and Later)](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugscejfbemskk). |
|  | Added note about the new `kEventParamWindowMouseLocation` parameter to [Mouse Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqha). |
|  | Removed all suggestions to use Classic Event Manager functions such as `Button` and `WaitMouseUp` in [Mouse Button Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiireeissd), and replaced them with a warning that these functions use excessive processor time (especially on Mac OS X). |
|  | Replaced deprecated mouse tracking result constants (`kMouseTrackingMousePressed/Released/Moved`) in [Tracking Mouse Movements](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqhe) with newer equivalents: `kMouseTrackingMouseDown/Up/Dragged`. Added new tracking result constants as well. |
|  | Added warning about the `kMouseTrackingMouseMoved` constant: The `kMouseTrackingMouseMoved` constant has been repurposed for Mac OS X version 10.2 and later. In earlier system software versions, `kMouseTrackingMouseMoved` was equivalent to the `kMouseTrackingMouseDragged` result, indicating that the mouse was moved while the mouse button was _down_. In Mac OS X 10.2. and later, you receive the `kMouseTrackingMouseMoved` tracking result if the user moves the mouse while the mouse button is _up_. If you have code that interprets `kMouseTrackingMouseMoved` in its older sense, you should update it before running it on Mac OS X version 10.2 or later. |
|  | Removed unnecessary `GetMouse` call in [Listing 3-8](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiirfeorsh). |
|  | Added new section [Mouse Tracking Regions (Mac OS X v.10.2 and Later)](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugsceivcesscc). |
|  | Added material about idle timers to [Installing Timers](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiinfeer2f), which are available in Mac OS X 10.2 and later. |
|  | Added information about the `kEventParamPostTarget` event parameter in [Creating Your Own Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjrga). Also updated information about how the standard event dispatcher handles unrecognized events (it sends them to the application event target). |
|  | Updated available event parameters in “Event Parameters and Types for Common Event Kinds.” Added event parameters for application events. |
| 2001-06-22 | Added additional sections [The Handler Stack](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwueqkcineegscb) and [An Event Propagation Example](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwueqkcjfcegrkf) to clarify how events are propagated through the containment hierarchy. |
|  | Removed note from [Standard Handlers](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwviucykjcummjqgq) indicating that the standard handler acts like the outermost object in a containment hierarchy. The actual mechanism is a bit more subtle than that. |
|  | Added third item to the event handling list in [The Event Model](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwviucykjcummjqgy) indicating that events that are not processed will be discarded. |
|  | Defined window dimension constants in [Listing 3-2](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiireucssh) to make the code compilable. |
|  | Clarified in [Command Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqg4) that command events are first sent to the event target they are associated with (that is, the menu or control). |
| 2001-05-11 | WWDC draft. |
|  | Document title changed to _Handling Carbon Events_ from the _Carbon Event Manager Handbook_. |
|  | Correction: The Carbon Event Manager does not replace the functionality of the Notification Manager. |
|  | Terminology change: References to the “default event handler” changed to “standard event handler” to better match the API and internal usage. |
|  | System Requirements section moved to the introductory chapter. Also, the Carbon Event Manager is available in CarbonLib 1.1.1 and later, not 1.2 as previously stated. |
|  | Added Note to [Standard Handlers](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwviucykjcummjqgq) (formerly Default Handlers) indicating that the standard window handler includes support for control events, and the standard application handler includes support for menu events. |
|  | In [Carbon Events Versus WaitNextEvent](Carbon%20Event%20Manager%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgiwviucykjcummjqg4), maximum timeout for `WaitNextEvent` should be 7FFFFFFF. Idle processing information changed to use null events instead of idle events. |
|  | In [Event Classes and Kinds](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqgm), clarified which handler actually calls SetPort and Begin/EndUpdate. It’s `kEventWindowUpdate`, not `kEventDrawContent`. |
|  | Indicated that `RunApplicationEventLoop` installs ths standard application event handler, which includes a simple quit Apple event handler in [Executing the Event Loop](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqgq). |
|  | Clarified in [Creating and Registering an Event Handler](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqgu) that the event handler UPP is not automatically released; you must dispose of it yourself. |
|  | Added warning comment in [Listing 3-4](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiinfekq2f) to indicate that the standard handler for the window close event removes the window, you can’t attempt to access it as part of your post-processing. |
|  | Correction in [Other Event Attributes](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqgy): `EventTime` is a floating point number, not an integer. |
|  | In [Command Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqg4), command IDs were introduced with Mac OS 8.0, not 8.5 as stated. Also the `myEvents` parameter in the `InstallApplicationEventHandler` call needs an “&”. The `commandID` field of the `commandStruct` variable starts with a lower-case c, not upper case. Added note indicating that Interface Builder makes it easy to assign command IDs to controls and menu items. |
|  | In [Text Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiivbekski), the user focus event target is a valid event target that does not change. If you install a handler on this target, then any events targeted at the current user focus will automatically be sent to your handler before being sent to the actual event target that has the user focus. |
|  | Correction in [Mouse Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjqha): The coordinates of the mouse position in `kEventParamMouseLocation` are given in global coordinates, not local as previously stated. |
|  | Added Mac OS X only mask constants `kEventKeyModifierNumLockMask` and `kEventKeyModifierFnMask` to [Table 3-1](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskii5buuqke). |
|  | Correction in [Installing Timers](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiinfeer2f): Event handlers are not associated with a particular event loop. Also added clarification in the Note as to which functons will run the event loop. |
|  | In [Processing Events Manually](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwugskiizeuqskg), clarified what handlers `RunApplicationEventLoop` installs: handlers to begin menu tracking, dispatch Apple events, and process the quit Apple event. |
|  | In [Creating Your Own Events](Carbon%20Event%20Manager%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsobzfvbuqmrqgmwviucykjcummjrga), indicated that you can pass 0 for the `when` parameter in `CreateEvent`, which specifies the current event time. |
|  | In “Event Parameters and Types for Common Event Kinds” updated text input event constant names to reflect latest header. |
| 2001-04-30 | Preliminary review draft. Includes material from the older Carbon Events document. |

[Next](Control%20Events%20Versus%20Classic%20Control%20Messages.md)[Previous](Carbon%20Event%20Manager%20Tasks.md)

