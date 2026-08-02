---
title: Form Programming Topics
apple_id: 10000021i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2002-11-12'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Form/Tasks/SettingFormAppearance.html
archived_at: '2026-07-15T07:15:54.975222Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Form Programming Topics](Introduction%20to%20Forms.md)


[Next](Managing%20Form%20Entries.md)[Previous](How%20Forms%20Work.md)

# Setting a Form’s Appearance

Generally, you’ll use Interface Builder to modify the appearance of a form. But you can also modify it programmatically, with the methods described here.

Use these NSForm methods to set the appearance of all the entries in a form:

- To set the font of the entries’ titles or text fields, use `setTitleFont:` or `setTextFont:`.
- To set the alignment of the entries’ titles or text fields, use `setTitleAlignment:` or `setTextAlignment:`., with one of these as the argument: `NSRightTextAlignment`, `NSCenterTextAlignment`, or `NSLeftTextAlignment`.
- To set the spacing between entries (in pixels), use `setInterlineSpacing:`.
- To set the width of the entries (including their titles and text fields), use `setEntryWidth:`.
- To set how the text fields are outlined, use `setBordered:` and `setBezeled:`. A border is a thin line around the field. A bezel is an outline shaded to look three-dimensional. If both of these are set to `NO`, then the text fields are not outlined.

Use the NSFormCell methods in the following list to set the appearance of one of the entries in a form. You can access a particular entry with `cellAtIndex:`; for example, `[myForm cellAtIndex:1]`.

- To set the font of an entry’s title or text field, use `setTitleFont:` or `setTextFont:`.
- To set the alignment of the entries’ titles or text fields, use `setTitleAlignment:` or `setTextAlignment:`., with one of these as the argument: `NSRightTextAlignment`, `NSCenterTextAlignment`, or `NSLeftTextAlignment`.
- To set the title of an entry, use `setTitle:`. If you want the title to contained styled text, use `setAttributedTitle:`.

[Next](Managing%20Form%20Entries.md)[Previous](How%20Forms%20Work.md)

