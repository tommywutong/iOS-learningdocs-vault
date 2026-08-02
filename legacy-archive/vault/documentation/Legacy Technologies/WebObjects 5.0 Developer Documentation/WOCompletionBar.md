---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOCompletionBar.html
archived_at: '2026-07-15T08:14:42.688414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOCompletionBar

## Component Description

The WOCompletionBar component displays a progress bar on a
page. You might use WOCompletionBar in the status page of your long-running
action (see the WOLongResponsePage Class).

## Synopsis

WOCompletionBar { valueMin=_aNumber_;
valueMax=_aNumber_; [value=_aNumber_;]
[numberformat=_numberFormatString_;]
[progressColor=_hexString_;]
[backgroundColor=_hexString_;]
[width=_aNumber_;] [border=_aString_;]
[align=_aString_;] };

## Bindings

**valueMin**
: Minimum value for the bar or value at which the bar
begins.

**valueMax**
: Maximum value for the bar or value at which the bar
ends.

**value**
: The current amount completed. The bar sizes to this
number and displays the number inside itself. The value must be
between `valueMin` and `valueMax`.

**numberformat**
: A format string that specifies how `value` should
be formatted as a number. If a number format is used, `value` must
be assigned an NSNumber object. If the value can't be interpreted
according to the format you specify, the value is set to `nil`.
See the NSNumberFormatter class specification for a description
of the number format syntax.

**progressColor**
: Color for showing the value. That is, this color shows
the amount completed.

**backgroundColor**
: Color for the uncompleted portion.

**width**
: Width of the bar. This attribute is passed directly
to the HTML `TABLE` that
makes up the bar.

**border**
: Thickness of the bar's border in pixels. This attribute
is passed directly to the HTML `TABLE` that
makes up the bar.

**align**
: Alignment of the displayed number within the completed
portion of the bar. This attribute is passed directly to the HTML `FONT` specification
for the number.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
