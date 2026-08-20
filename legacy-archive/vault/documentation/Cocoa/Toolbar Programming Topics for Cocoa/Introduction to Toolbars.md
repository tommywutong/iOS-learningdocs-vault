---
title: Toolbar Programming Topics for Cocoa
apple_id: 10000109i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Toolbars/Toolbars.html
archived_at: '2026-07-15T07:20:55.805746Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](How%20Toolbars%20Work.md)

# Introduction to Toolbars

NSToolbar and NSToolbarItem provide you with a standard way to display a toolbar for a titled window below its title bar. These classes also provide users with a standard way to customize toolbars and save those customizations.

This programming topic describes how to use toolbars. It contains the following articles:

- [How Toolbars Work](How%20Toolbars%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42talkcijbugrsiifbq) gives basic information on toolbars.
- [Toolbar Management Checklist](Toolbar%20Management%20Checklist.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tclkdjjbeerkijjaq) describes what happens when you create a toolbar.
- [Adding and Removing Toolbar Items](Adding%20and%20Removing%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tklkcijbuossdirfa) describes managing toolbar items, and the role of the NSToolbar delegate.
- [Setting a Toolbar Item’s Representation](Setting%20a%20Toolbar%20Item%E2%80%99s%20Representation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg4zdelkcijbuorsgjbcq) describes the different ways a toolbar item can be represented and how to set them.
- [Validating Toolbar Items](Validating%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tglkciffeorsiirca) describes how to set whether a toolbar item is clickable or not.
- [Setting a Toolbar Item’s Size](Setting%20a%20Toolbar%20Item%E2%80%99s%20Size.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tilkciffekrshifba) describes how to set a toolbar item’s minimum and maximum size.
- [Selectable Toolbar Items](Selectable%20Toolbar%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydqlkdjjbeoscii5dq) describes how to support selectable toolbar items.
- [Subclassing NSToolbarItem](Subclassing%20NSToolbarItem.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqg42tmlkciffeeqkhjfeq) describes the methods to override when subclassing NSToolbarItem.
- [Techniques for Toolbar Management](Techniques%20for%20Toolbar%20Management.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambqha2tslkciffeorsiirca) describes how to determine if a toolbar has items in the overflow menu and how to calculate toolbar height.

The following sample code is available through Apple Developer Connection:

- _[iSpend](../../../samplecode/iSpend/iSpend.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgnrsgu)_ shows how to add basic toolbar support to an application.
- _[ToolbarSample: Using NSToolbar to construct a window toolbar](https://developer.apple.com/library/archive/samplecode/ToolbarSample/Introduction/Intro.html#//apple_ref/doc/uid/DTS10000413)_ implements an example toolbar including using custom views in a toolbar item.
[Next](How%20Toolbars%20Work.md)

