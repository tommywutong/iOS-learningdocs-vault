---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOHyperlink.html
archived_at: '2026-07-15T08:09:53.320996Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOHyperlink

## Element Description

WOHyperlink generates a hypertext link in an HTML document.

## Synopsis

WOHyperlink { action=_aMethod_ |
href=_aURL_; | pageName=_aString_;
| directActionName=_anActionName_; actionClass=_className_;
[fragmentIdentifier=_anchorFragment_;]
[string=_aString_;] [target=_frameName_;]
[disabled=_aBoolean_;] ... };

## Bindings

**action**
: Action method to invoke when this element is activated.
The method must return a WOElement.

**href**
: URL to direct the browser to when the link is clicked.

**pageName**
: Name of WebObjects page to display when the link is
clicked.

**directActionName**
: The name of the direct action method (minus the "Action"
suffix) to invoke when this element is activated.

**actionClass**
: The name of the class in which the method designated
in __directActionName__ can be found. Defaults
to DirectAction.

**fragmentIdentifier**
: Named location to display in the destination page.

**string**
: Text displayed to the user as the link. If you include
any text between the `<WEBOBJECT ...> and
</WEBOBJECT>` tags for this element,
the contents of string is appended to that text.

**target**
: Frame in a frameset that will receive the page returned
as a result of the user's click.

**disabled**
: If evaluates to `true` (or `YES`),
the content string is displayed, but the hyperlink is not active.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
