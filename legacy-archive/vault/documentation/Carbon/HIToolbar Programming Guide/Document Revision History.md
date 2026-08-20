---
title: HIToolbar Programming Guide
apple_id: TP40000958
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-07-07'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/UsingHIToolbar/HIToolbar_apdx_a_history/HIToolbar_apdx_a_history.html
archived_at: '2026-07-15T05:24:45.181789Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [HIToolbar Programming Guide](HIToolbar%20Concepts.md)


[Previous](Toolbar%20Tasks.md)

# Document Revision History

This table describes the changes to _HIToolbar Programming Guide_.

| __Date__ | __Notes__ |
| 2005-07-07 | Changed title from "Using HIToolbar." Made minor bug fix. |
| 2003-04-30 | In [What Is a Toolbar?](HIToolbar%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnjyfvbuqmrqgewviucykjcummjqgi), indicated that the user can cycle between display modes by command-clicking the toolbar button. |
|  | Added info in [What Is a Toolbar?](HIToolbar%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnjyfvbuqmrqgewviucykjcummjqgi) describing how the user can bring up the configuration sheet. |
|  | Added overflow menu screen shot, [Figure 1-4](HIToolbar%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnjyfvbuqmrqgewugsscivdekrkc). |
|  | Added new section [Model-View-Controller for HIToolbar](HIToolbar%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnjyfvbuqmrqgewugsscivducrkg) showing how HIToolbar fits into the model-view-controller design convention. |
|  | Added command ID as one of the data types associated with toolbar items in [Toolbar Items](HIToolbar%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnjyfvbuqmrqgewugsscivbuirkj). |
|  | Removed `kHIToolbarItemValidAttrs` and `kHIToolbarItemMutableAttrs` from [Toolbar Item Attributes](Toolbar%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecssiifauery), as these constants may change over time. |
|  | In [Creating Items from an Identifier](Toolbar%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecssijjeuora), indicated that toolbar items that do not have a command ID associated with them will not be enabled when they appear in the overflow menu. |
|  | Added info to [Creating Items from an Identifier](Toolbar%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecssijjeuora) describing cases where you might not want to assign a command ID to a toolbar item. |
|  | Replaced `'void'` with `typeVoidPtr` in [Listing 2-5](Toolbar%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecssgi5cuora) in the `SetEventParameter` call for the construct event. |
|  | Added specific information in [Creating Items from a Drag](Toolbar%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecsseinfeqqi) about what kind of data you can store in response to the `kEventToolbarItemGetPersistentData` event. |
|  | Indicated in [Creating Items from a Drag](Toolbar%20Tasks.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgmjqfvbecsseinfeqqi) that if you handle the `kEventToolbarItemPerformAction` event, you must also set the command ID of the toolbar item to `kHIToolbarCommandPressAction`. |
|  | Removed Panther-specific information. |
| 2003-03-01 | Preliminary review draft. |

[Previous](Toolbar%20Tasks.md)

