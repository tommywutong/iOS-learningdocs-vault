---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/Reference/DynamicElements/WOHyperlink.html
archived_at: '2026-07-15T07:49:41.204712Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynamicElements.book.md)
[!Previous Section](WOHiddenField.md)

---

# __WOHyperlink__

### Synopsis

__WOHyperlink__ __{__ __action__=_`aMethod`_ | __href__=_`aURL`_ | __pageName__=_`aString`___;__ [__fragmentIdentifier__=_`anchorFragment`___;__] [__string__=_`aString`___;__] [__target__=_`frameName`___;__] [__disabled__=YES|NO__;__] ... __};

### Description__

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
: Text displayed to the user as the link. If you include any text between the <WEBOBJECTS ...> and </WEBOBJECT> tags for this element, the contents of __string__ is appended to that text.

**__target__**
: Frame in a frameset that will receive the page returned as a result of the user's click.

**__disabled__**
: If evaluates to YES, the content string is displayed, but the hyperlink is not active.

### Examples

[Simple examples](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=HyperlinkEx1)

[Disabling a hyperlink](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=HyperlinkEx2)

[Linking to an external site](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=HyperlinkEx3)

[Specifying a string within a hyperlink](http://wofapps4.apple.com/cgi-bin/WebObjects-3/DynamicElements?ExamplePage=HyperlinkEx4)

[!Table of Contents](DynamicElements.book.md)
[!Next Section](WOImage.md)
