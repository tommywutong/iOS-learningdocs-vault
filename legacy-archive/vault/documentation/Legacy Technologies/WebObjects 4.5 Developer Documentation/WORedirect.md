---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WORedirect.html
archived_at: '2026-07-15T08:11:47.006858Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)

# WORedirect

> __Inherits
> from:__  [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) [WOElement](WOElement.md#apple-k5huk3dfnvsw45a) NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

WORedirect is a subclass of [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) that may be used to force
the user's browser to redirect to another URL. You should only return
this component as a response to an action method and never use it
in an declarations file directly. This component can be useful,
for example, if you have an image map with both static and dynamic
actions.

## Instance Methods

---

### setURL

`public void setURL(String aURL)`

Sets the URL to which the user's browser should
be redirected to _aURL_.

---

### url

`public String url()`

Returns the URL to which the user's browser
will be redirected when this component is returned.

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
