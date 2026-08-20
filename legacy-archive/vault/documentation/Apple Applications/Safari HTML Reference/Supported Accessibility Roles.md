---
title: Safari HTML Reference
apple_id: TP40002049
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: WebKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariHTMLRef/Articles/AccessibilityRoles.html
archived_at: '2026-07-15T05:19:03.985523Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari HTML Reference](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Supported%20Meta%20Tags.md)

# Supported Accessibility Roles

Accessibility roles from the WAI-ARIA specification that are supported in Safari are described here.

WebKit now has elementary support for the WAI-ARIA specification. Developers can assign a value to the `role` attribute of a `div` or `span` element, indicating the purpose of a custom interface element on a webpage. This enables accessibility utilities to interact with these elements as they would with standard inputs and menus. The following example shows an image that is recognized by accessibility utilities as a button:

```
<div role="button" tabindex="0" onkeydown="return buttonEvent(event);" onclick="return buttonEvent(event);">
    <img src="myimage.jpg">
</div>
```

More information on the WAI-ARIA specification can be found at [http://www.w3.org/TR/wai-aria/](http://www.w3.org/TR/wai-aria/).

A standard button.

A standard checkbox.

A group of elements that should not be included individually in a page summary or table of contents.

The heading for a section of a page.

A collection of elements that compose an image.

A hyperlink.

A dropdown list of options.

A list item.

A standard menu.

A container of menus.

An option in a menu.

A checkable menu item.

A radio button menu item in a group of mutually exclusive choices.

An item in a dropdown list.

A visual indicator of the progress of a task.

A radio button in a group of mutually exclusive choices.

A text input field.

[Next](Document%20Revision%20History.md)[Previous](Supported%20Meta%20Tags.md)

