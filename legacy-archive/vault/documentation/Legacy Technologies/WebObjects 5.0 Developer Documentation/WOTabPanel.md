---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOTabPanel.html
archived_at: '2026-07-15T08:14:45.719517Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOTabPanel

## Component Description

The WOTabPanel component displays a tab panel. When the user
selects a tab the corresponding panel appears.

![[image: Art/WOExtWOTabPanel.gif]](Art/WOExtWOTabPanel.gif)

This component can be embedded within a WOForm. When the WOTabPanel
contains form fields that are bound to an enterprise object's
attributes, the HTML element the user clicks to change tabs must
be a submit button. This ensures that the values the user types
into these fields get stored in the enterprise object. If the HTML
element the user clicks is a hyperlink, the enterprise object's
attributes are not updated when the user switches tabs and the form
field values are lost. The `submitActionName` binding determines
the whether the HTML element that switches tabs is a hyperlink or
a submit button.

## Synopsis

WOTabPanel { tabs=_anArray_;
selectedTab=_aString_; [tabNameKey=_aString_;]
[nonSelectedBgColor=_hexString_;]
[bgcolor=_hexString_;] [textColor=_hexString_;]
[submitActionName=_anActionName_;]
};

## Bindings

**tabs**
: An array of objects representing the tabs. For example,
the array could be named `movieArray` and
contain Movie objects.

**selectedTab**
: The object corresponding to the currently selected tab.
For example, `currentMovie` could represent
the currently selected object in `movieArray` .
This attribute gets updated each time the tab panel is redisplayed.
In addition, this attribute defines the initially selected object and
defaults to the first object in the list.

**tabNameKey**
: A key representing the tab object's name string displayed
in the tab. For the movie example, the name key is set to "title"
and the WOTabPanel will display `currentMovie.title`.
If your tab objects are Strings (NSStrings in Objective-C), do not
set this attribute.

**nonSelectedBgColor**
: Color of the tabs that are not selected.

**bgcolor**
: Color of the selected tab and the main panel area.

**textColor**
: Color of the text within the tab.

**submitActionName**
: The name of an action that is called when a new tab
is selected. This attribute functions only when the tab panel is
embedded within a WOForm. If `submitActionName` is
not defined or is set to `null`, the
tab selectors are hyperlinks. Otherwise the tab selectors are submit
buttons. If you want the tab selector to be a submit button, but
don't want to call an action, set this attribute to the empty
string (`""`).

## Example

The WOTabPanel component is used in conjunction with the WOKeyValueConditional
which conditionally displays the tab panel contents depending on
the tab the user selects. The following example shows the HTML,
template, and Java files for the parent component containing a tab
panel.

> ```
> <WEBOBJECT NAME=TabPanel1>
>     <WEBOBJECT NAME=KeyValueConditional1>
>         This is the content<BR>for the first tab.<BR>
>     </WEBOBJECT>
>     <WEBOBJECT NAME=KeyValueConditional2>
>         This is the content<BR>for the second tab.<BR>
>     </WEBOBJECT>
> </WEBOBJECT>
> ```

> ```
> TabPanel1: WOTabPanel {
>     tabs = keyList;
>     selectedTab = selection;
> }
> KeyValueConditional1: WOKeyValueConditional {
>     key = "selection";
>     value = "first";
> }
> KeyValueConditional2: WOKeyValueConditional {
>     key = "selection";
>     value = "second";
> }
> ```

> ```
> protected NSArray keyList;
> protected String selection;
>
> public Main() {
>     keyList = new NSArray(new Object[] {"first","second"});
> }
> ```

The parent component's constructor initializes the key list.
The `selection` string
holds the current selection which the WOKeyValueConditional components
query to decide if they should display their contents.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
