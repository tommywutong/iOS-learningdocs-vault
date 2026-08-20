---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/WOExtensions/WOIFrame.html
archived_at: '2026-07-15T08:14:42.831788Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md) 

# WOIFrame

## Component Description

The WOIFrame component inserts an IFRAME tag into your page.
This tag is a container to create an in-line or floating frame:
a frame in which the contents of another HTML document can be seen.
The difference between an IFRAME and a normal frame is that the
floating frame can be seen inside a document and is treated as a
part of the document. This means that when you scroll through the
page the frame will scroll with it. IFRAME tags are supported by
Microsoft's Internet Explorer browser. If you want to insert a FRAME
tags, as used by Netscape's browser, use the WOFrame dynamic element documented
in the _Dynamic Elements Reference_.

The HTML content displayed within the WOIFrame can come from
a method, a URL, or a WebObjects page.

## Synopsis

WOIFrame { value=_aMethod_;
| src=_aURL_; | pageName=_aString_;
[frameborder=_aString_;]
[height=_aString_;] [marginheight=_aString_;]
[marginwidth=_aString_;] [name=_aString_;]
scrolling=_aString_; width=_aString_;
};

## Bindings

**value**
: Method that supplies the content for this frame.

**src**
: External source that supplies the content for this frame.

**pageName**
: Name of WebObjects page that supplies the content for
this frame.

**frameborder**
: Specifies whether or not a border should be displayed
for the frame. This attribute is passed through to the `IFRAME` HTML
tag.

**height**
: Specifies the height of the frame to the browser, either
as a number of pixels or as a percentage of the current screen height.

**marginheight**
: Controls the vertical margins for the frame (margins
are specified in pixels). This attribute is passed through to the `IFRAME` HTML
tag.

**marginwidth**
: Controls the horizontal margins for the frame (margins
are specified in pixels). This attribute is passed through to the `IFRAME` HTML
tag.

**name**
: Assigns a name to the frame so it can be targeted by
links in other documents or, more commonly, from other frames in
the same document. This attribute is passed through to the `IFRAME` HTML
tag.

**scrolling**
: Specifies whether or not the frame should have scrollbar.
This attribute is passed through to the `IFRAME` HTML
tag.

**width**
: Specifies the width of the frame to the browser, either
as a number of pixels or as a percentage of the current screen width.
This attribute is passed through to the `IFRAME` HTML tag.

[![Table of Contents](attachments/Reference/WOExtensions/images/up.gif)](WOExtensionsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
