---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WORedirect.html
archived_at: '2026-07-15T08:15:15.730124Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

# WORedirect

> **__Inherits from:__**
> : WOComponent: WOElement: Object

> **__Implements:__**
> : NSKeyValueCoding: NSKeyValueCoding.ErrorHandling: NSKeyValueCodingAdditions: NSValidation: WOActionResults: Cloneable: Serializable

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WORedirect is a subclass of WOComponent that may be used to force the user's browser to redirect to another URL. You should only return this component as a response to an action method and never use it in an declarations file directly. This component can be useful, for example, if you have an image map with both static and dynamic actions.

## Constructors

---

### WORedirect

`public WORedirect (WOContext aContext)`

Description forthcoming.

---

## Instance Methods

---

### appendToResponse

`public void appendToResponse(WOResponse aResponse, WOContext aContext)`

Description forthcoming.

---

### setURL

`public void setURL(String aURL)`

Sets the URL to which the user's browser should be redirected to _aURL_.

---

### url

`public String url()`

Returns the URL to which the user's browser will be redirected when this component is returned.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
