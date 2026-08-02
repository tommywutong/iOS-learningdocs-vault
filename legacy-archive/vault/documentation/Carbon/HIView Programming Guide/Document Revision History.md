---
title: HIView Programming Guide
apple_id: TP30000923
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/HIViewDoc/HIView_apdx_a_history/HIView_apdx_a_history.html
archived_at: '2026-07-15T05:22:33.467526Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HIView Programming Guide](Introduction%20to%20HIView%20Programming%20Guide.md)


[Previous](HIView%20Tasks.md)

# Document Revision History

This table describes the changes to _HIView Programming Guide_.

| __Date__ | __Notes__ |
| 2007-10-31 | Added information about HICocoaView. |
| 2007-04-03 | Made minor technical and editorial corrections. |
| 2005-04-29 | Changed the title from _Introducing HIView_. |
| 2003-10-15 | Clarified that menus are HIObjects, but they are displayed using menu content views. |
|  | Added binding and positioning illustrations. |
|  | In [Creating Custom Menus](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwueqkkjbfegqsd), changed feature bit `kControlDoesNotUseSpecialParts` to `kHIViewDoesNotUseSpecialParts`. |
|  | Updated information under [kEventControlSetFocusPart](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjtgq), indicating that the handler must call `HIViewSetNeedsDisplayInRegion`. |
| 2003-09-16 | Updated conceptual information to include menu content views. |
|  | Specified that the combo box turns into a scrolling list if you exceed a certain number of menu items. |
|  | Added information about new views, [Text View](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwueqsdircueqsd) and [Web View](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwueqsdijceossc). |
|  | Added new section about automating view layout. |
|  | Added new section about manipulating menu views. |
|  | Clarified in [Handling HIObject Events](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwueqkcivbuqrce) that when setting the `kEventParamHIObjectInstance` parameter for the construct event, the type should be `typeVoidPtr`, not `typeHIObjectRef`. |
|  | Clarified in [Handling HIObject Events](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwueqkcivbuqrce) that the instance data you set in the `kEventHIObjectConstruct` handler is then passed to your event handler in the `userData` parameter. |
|  | Added simple destruct handler, [Listing 2-8](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwueqkki5aucq2k). |
|  | Added additional requirements for enabling drag-and-drop in [Handling Drag and Drop Events](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjrgq). |
|  | Added new section, [Creating Custom Menus](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwueqkkjbfegqsd). |
| 2002-09-28 | Added additional drawing details to [The Drawing Model](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwviucykjcummjqgu). |
|  | Indicated in [Translating Coordinates](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjqg4) that you can pass null for a view parameter to convert to or from window-relative coordinates. |
|  | Added information to [Drawing in Views](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjqha) about how to transform a context if you want to draw using Quartz coordinates. |
|  | Qualified in [Creating a Combo Box](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjrgu) that if you do not specify the `kHIComboBoxAutoSizeListAttribute` attribute when creating the combo box, you must size it yourself using the appropriate `SetControlData` tags. |
|  | Correction in [Handling HIObject Events](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwueqkcivbuqrce): you _should_ dispose of instance data in your `kEventHIObjectDestruct` handler. |
|  | Qualified info about part codes in [Handling Hit-Test Events](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjrge): custom part codes should be in the range 1-127. Your application can respond to negative part code values, but it should never return them from a `kEventControlHitTest` handler. |
| 2002-09-23 | Cleaned up usage of “control” and “view” throughout the document to conform to the standard defined in [Views Versus Controls and Menus](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwviucykjcummjqgq). |
|  | Removed mention of the toolbar control, as it is not a view, and cannot be directly accessed by the developer. Revised [Figure 1-1](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwugsscinfeqr2k) to reflect this change. |
|  | Corrected text throughout the document to remove mention of the Quartz compositor and discuss the HIView compositor instead. |
|  | Revised [The Coordinate System](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwviucykjcummjqgy) to correctly describe the HIView coordinate system. The HIView coordinate axis is identical to the QuickDraw axis. |
|  | Added information about `HIPoint`, `HISize`, and `HIRect` to [The Coordinate System](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwviucykjcummjqgy). |
|  | Updated combo box screen shots in [Figure 1-7](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwueq2jjbcuurkj). |
|  | Added information about how much work is done by the standard event handler in [Changing Keyboard Focus](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjqgy). |
|  | Added example to [Translating Coordinates](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjqg4). |
|  | Added warning to [Drawing in Views](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjqha) indicating that you should not pass `false` to the `HIViewSetNeedsDisplay` or `HIViewSetNeedsDisplayInRegion` functions, as this may unintentionally suppress updates in other intersecting views. |
|  | Added note to [Creating a Scroll View](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjqhe), indicating that if you want to embed custom views in a scroll view, they must support the `kEventClassScrollable` events. |
|  | Added attribute constant names for optional features in [Creating a Combo Box](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjrgu). |
|  | Changed “Calvin” to “Hobbes” in [Listing 2-4](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwugsscirbuoqsh) to match the combo box in [Figure 1-7](HIView%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqgqwueq2jjbcuurkj). |
|  | Greatly expanded [Creating Custom Views](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwugsscindeuq2f), adding sample code and more descriptions. |
|  | Clarified in [Handling Draw Events](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjrgi) that the `kEventControlDraw` event passes a region handle to you that you can use to constrain drawing to the visible parts of your view. |
|  | Added info to [Handling Drag and Drop Events](HIView%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmrtfvbuqmrqguwviucykjcummjrgq) indicating that you must return a `kEventParamControlLikesDrag` Boolean parameter when responding to the the `kEventControlDragEntered` event. |
| 2002-09-02 | Preliminary review draft. |

[Previous](HIView%20Tasks.md)

