---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOThresholdColoredNumber.html
archived_at: '2026-07-15T08:14:46.996126Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOThresholdColoredNumber

## Component Description

The WOThresholdColoredNumber component displays a number in
one of two colors depending on whether the number is above or below
a threshold.

## Synopsis

WOThresholdColoredNumber { lowColor=_hexString_;
highColor=_hexString_; threshold=_aNumber_;
value=_aNumber_; [numberformat=_numberFormatString_;]
};

## Bindings

**lowColor**
: The color in which the number is rendered when the number
is below the threshold. Defaults to "`#FF0000`".

**highColor**
: The color in which the number is rendered when the number
is equal to or above the threshold. Defaults to "`#00FF00`".

**threshold**
: The threshold at which the number's rendered color
is changed.

**value**
: The displayed number.

**numberformat**
: A format string that specifies how `value` should
be formatted as a number. If the value can't be interpreted according
to the format you specify, the value is set to `nil`.
See the NSNumberFormatter class specification for a description
of the number format syntax.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
