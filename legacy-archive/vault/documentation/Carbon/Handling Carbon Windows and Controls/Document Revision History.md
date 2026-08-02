---
title: Handling Carbon Windows and Controls
apple_id: TP30001004
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HandlingWindowsControls/hitb-apdx_b_history/hitb-apdx_b_history.html
archived_at: '2026-07-15T05:22:46.957283Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Handling Carbon Windows and Controls](Introduction%20to%20Handling%20Carbon%20Windows%20and%20Controls.md)


[Next](Glossary.md)[Previous](Carbon%20Events%20Versus%20Classic%20DefProc%20Messages.md)

# Document Revision History

This table describes the changes to _Handling Carbon Windows and Controls_.

| __Date__ | __Notes__ |
| 2005-07-07 | Fixed bugs and updated older links. Noted that function QDAddRectToDirtyRegion should be used when drawing directly into a graphics port. |
| 2002-09-30 | Revised public release. |
|  | Corrected text for the `kWindowCompositingAttribute` in [Table 2-2](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdjbcucrsd): The compositing mode is specific to the Control Manager, and does not have anything to do with the Quartz compositor. |
|  | Added info to [Cycling Through Windows (Mac OS X 10.2 and Later)](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jivdemscf) about the `kWindowMenuIncludeRotate` option that you can pass to `CreateStandardWindowMenu` to add a “Cycle Windows” menu item to the Window menu. |
|  | Corrected text for `kEventControlBoundsChanged` in [Table 3-7](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jiveekskk): The Control Manager sends you a `kEventControlDraw` event after the bounds changed; you do not need to send the event to yourself. |
| 2002-08-21 | Updated review draft. |
|  | Updated most code examples to use the Carbon Event Manager macro `GetEventTypeCount` for the number of registered events rather than hard coding a specific value. |
|  | Updated code examples to explicitly assign universal procedure pointers (UPPs) to variables rather than inline their creation in function calls (for example, [Listing 3-2](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2ji5eusqsj)). Doing so promotes better memory management as you can dispose of the UPPs when you no longer need them. |
|  | Added note indicating that the standard handler for `kEventWindowClose` automatically calls `DisposeWindow`,. |
|  | Added drawer window class to [Table 2-1](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdizeuuqke) and added section [Manipulating Drawers (Mac OS X 10.2 and later)](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jjbeuessb). |
|  | Added `kWindowCompositingAttribute`, `kWindowMetalAttribute`, and `kWindowIgnoreClicksAttribute` to [Table 2-2](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdjbcucrsd). Also corrected spelling of the `kWindowResizableAttribute` constant. |
|  | Added new section, [Cycling Through Windows (Mac OS X 10.2 and Later)](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jivdemscf). |
|  | Removed drawing into an offscreen graphics world in [Listing 3-18](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jirauiskf). Because Mac OS X automatically double buffers windows, you should no longer buffer windows yourself. Also added new event, `kEventWindowInit` to demonstrate the Appearance Manager function `SetThemeWindowBackground`. |
|  | In [Listing 3-19](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jjjaugssc), added new event (`kEventWindowInit`) to event specification. Changed window class to movable modal to support theme background set in [Listing 3-18](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jirauiskf). |
|  | Added new section, [Drawing Using Quartz](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jizceirkd) to describe the basics of using Quartz from Carbon. . |
|  | Added more information and code about simple control tracking to [Creating a Custom Control](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jivaumqsf). Also added a new section, [Custom Control Tracking](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jjbeesrcj), and split out the registration information in [Registering Your Custom Control](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jjffekski). |
|  | Added new section, [Introducing HIObject and HIView (Mac OS X 10. 2 and Later)](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2ji5beuscf). |
| 2002-04-22 | Revised beta. First public release . |
|  | Corrected window class hierarchy in [Window Classes](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdirceorsf), placing Help windows below Overlay and Utility windows. |
|  | Removed “combo box” from [Figure 2-11](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjxge). |
|  | Changed the advantages of [Editable Unicode Text Fields](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjuge). QuickDraw enhancements will soon allow you to draw antialiased text using editable text fields. |
|  | Changed [Figure 2-27](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdivdecrsh) in [Drawing Events](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjwgq) to show an update region appearing during a window resize rather than window movement. Window buffering in Mac OS X makes the latter event less likely. |
|  | Added note to [Embedding Controls](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjwgm) indicating that on Mac OS X (but not Mac OS 9) you can embed controls from one window into another. |
|  | Removed sample code from [Adding Window Proxy Icons](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjxgm), as it needs to be updated. |
|  | In [Creating a Custom Control](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jivaumqsf), added caveats indicating that the control or window drawn using the Appearance Manager `DrawThemeXXXX` functions don’t necessarily appear wholly within the bounds you pass into the function. |
|  | Added index. |
| 2002-04-04 | Beta draft. |
|  | Book title changed to _Inside Mac OS X: Handling Carbon Windows and Controls_ from _Inside Carbon: Handling Windows and Controls_. |
|  | Added more information about new window naming conventions in [Anatomy of a Window](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjsga). |
|  | Added definition of a control indicator to [Controls](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdi5cueq2i) and the Glossary |
|  | Added help windows to window layer hierarchy in [Window Classes](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdirceorsf) |
|  | Added text to [Window Classes](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdirceorsf) to define the difference between window layering and window ordering. |
|  | Added `kWindoeToolbarButtonAttribute` to [Table 2-2](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdjbcucrsd). |
|  | Pop-up buttons renamed pop-up menus and moved to a separate section: [Pop-Up Controls](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdjjceqrkk). |
|  | Scrolling text boxes renamed [Scrolling Text Fields](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjtgq). |
|  | Edit text fields renamed [Editable Text Fields](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwueqsdizduiq2h). |
|  | Edit Unicode text fields renamed [Editable Unicode Text Fields](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjuge). |
|  | User panes renamed Custom panes. |
|  | Visual Separators renamed [Separator Lines](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjvgu). |
|  | Placards moved from “Button Controls” to [Miscellaneous Controls](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwviucykjcummjvgy). |
|  | Added new section, [Accessibility and Section 508 Compliance](Window%20and%20Control%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqguwugsscizaumscd). |
|  | Added text promoting the virtues of Interface Builder over other layout methods in [Using Interface Builder](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjsga). Also added info emphasizing compatibility with older resource-based windows and controls. |
|  | Added note to [Creating a Window From a Nib file](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjtgm) reminding developers to create separate nib files if they contain localizable text. |
|  | Emphasized that in [Window Bounds Changed Events](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjtg4) that a window resize must be constrained so that it doesn’t overwrite the Dock. |
|  | Added usage do’s and don’ts from the Aqua HIG in [Creating and Displaying Sheets](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjvgi). |
|  | Added new sections, [Changing the Modification State](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jijbemssj) and [Ordering Windows](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jijfegr2f). |
|  | Added `Get/SetWindowProperty` functions to [Window Reference Constants](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjwge). |
|  | Added new section,[Adding Window Proxy Icons](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywviucykjcummjxgm). |
|  | Added new section [Window Groups (Mac OS X Only)](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jjbeeeqkc). |
|  | Cleaned up terminology in [Live Scrolling](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywugsscinbegssg). “Scroll bar” refers to the entire control. Replaced “scroll control value” with “scroller value.” |
|  | Added new material to [Custom Windows and Controls](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jijbegqsh), including [Creating a Custom Control](Window%20and%20Control%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambufvbuqmrqgywueq2jivaumqsf). |
|  | Added additional glossary terms. |
|  | Added this Document Version History. |
| 2002-01-28 | Alpha draft for internal review. |

[Next](Glossary.md)[Previous](Carbon%20Events%20Versus%20Classic%20DefProc%20Messages.md)

