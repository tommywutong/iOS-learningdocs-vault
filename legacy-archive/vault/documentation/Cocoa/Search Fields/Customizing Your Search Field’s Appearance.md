---
title: Search Fields
apple_id: 10000168i
resource_type: Guide
platform: macOS
topic: User Experience
technology: AppKit
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SearchFields/Articles/CustomizingSearchFields.html
archived_at: '2026-07-15T07:18:56.056958Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Search Fields](Introduction%20to%20Search%20Fields.md)


[Next](Document%20Revision%20History.md)[Previous](Implementing%20the%20Target.md)

# Customizing Your Search Field’s Appearance

You can specify the behavior of search fields in a xib file, like most Cocoa controls, without writing any source code. This is described in [Adding a Search Field to Your Application](Adding%20a%20Search%20Field%20to%20Your%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgi2dilkcifbemskcjfaq). If you want to change a search field’s appearance, for example, its buttons or field locations, this article describes how.

In general, avoid changing the search button cell unless you want a custom appearance or behavior. Typically, the search button has two behaviors: it either displays a menu (if a menu template is set), or it invokes the search field’s action method (when the button is clicked). The cancel button appears only if there is text in the search field.

You change the search button cell by sending `setSearchButtonCell:` to the button’s cell, and change the cancel button cell by sending `setCancelButtonCell:` to the button’s cell. To remove the search button or the cancel button, set the cell for that button to `nil`.

If you have customized either the search and cancel buttons, you can easily “reset” their attributes to the search field cell's default image, alternate image, target, and action. You do this for the search button by sending `resetSearchButtonCell` to the button’s cell, and for the cancel button by sending `resetCancelButtonCell` to the button’s cell. All other attributes of the search field cell are not changed.

The following `NSSearchFieldCell` methods return the bounds for the buttons and the text field. Override these methods to position the items differently. `NSSearchFieldCell` assumes that there is a search button, text field, and cancel button, from left to right.

- [searchButtonRectForBounds:](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399450-searchbuttonrectforbounds)
- [cancelButtonRectForBounds:](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399472-cancelbuttonrect)
- [searchButtonRectForBounds:](https://developer.apple.com/documentation/appkit/nssearchfieldcell/1399450-searchbuttonrectforbounds)

[Next](Document%20Revision%20History.md)[Previous](Implementing%20the%20Target.md)

