---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOMetaRefresh.html
archived_at: '2026-07-15T08:14:42.867644Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOMetaRefresh

## Component Description

The WOMetaRefresh component inserts an HTML `<META
REFRESH=...>` tag into your page, which instructs
the user's browser to display a new page after a specified time
interval. You can use the WOMetaRefresh component to create pages
that refresh themselves regularly (for example, a stock price page),
or display a message and jump to a new page (for example, a page
that jumps to a website from an outdated URL).

Note that not all browsers support page refreshing.

## Synopsis

WOMetaRefresh { seconds=_aNumber_;
pageName=_aString_; | action=_aMethod_;
};

## Bindings

**seconds**
: Number of seconds before the page is refreshed.

**pageName**
: Component to navigate to after the page is refreshed.

**action**
: Action method to invoke after the page is refreshed.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
