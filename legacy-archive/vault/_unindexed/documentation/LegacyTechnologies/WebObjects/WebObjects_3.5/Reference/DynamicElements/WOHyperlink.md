---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/Reference/DynamicElements/WOHyperlink.html
archived_at: '2026-07-15T07:55:27.314025Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElementsTOC.md) [!Previous Section](WOHiddenField.md)

## WOHyperlink

### Synopsis

__WOHyperlink__ __{__ __action__=_aMethod_ | __href__=_aURL_ | __pageName__=_aString___;__ [__fragmentIdentifier__=_anchorFragment___;__] [__string__=_aString___;__] [__target__=_frameName___;__] [__disabled__=YES|NO__;__] ... __};__

### Description

WOHyperlink generates a hypertext link in an HTML document.

**__action__**
: Action method to invoke when this element is activated. The method must return a WOElement.

**__href__**
: URL to direct the browser to when the image is clicked.

**__pageName__**
: Name of WebObjects page to display when the link is clicked.

**__fragmentIdentifier__**
: Named location to display in the destination page.

**__string__**
: Text displayed to the user as the link. If you include any text between the <WEBOBJECT ...> and </WEBOBJECT> tags for this element, the contents of __string__ is appended to that text.

**__target__**
: Frame in a frameset that will receive the page returned as a result of the user's click.

**__disabled__**
: If evaluates to YES, the content string is displayed, but the hyperlink is not active.

### Examples

[Simple examples](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=HyperlinkEx1)

[Disabling a hyperlink](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=HyperlinkEx2)

[Linking to an external site](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=HyperlinkEx3)

[Specifying a string within a hyperlink](http://localhost/cgi-bin/WebObjects/Examples/WebScript/DynamicElements?ExamplePage=HyperlinkEx4)

[!Table of Contents](DynamicElementsTOC.md) [!Next Section](WOImage.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
