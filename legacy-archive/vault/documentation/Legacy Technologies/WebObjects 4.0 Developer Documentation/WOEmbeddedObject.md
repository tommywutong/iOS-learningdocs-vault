---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOEmbeddedObject.html
archived_at: '2026-07-15T08:00:36.012870Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOEmbeddedObject

---

# Synopsis

WOEmbeddedObject {value=_aMethod_; | src=_aURL_; | filename= _imageFileName_; [framework = _frameworkBaseName_|"app";] | data=_dataObject_; mimeType=_typeString_; [key=_cacheKey_;]... };

---

# Description

A WOEmbeddedObject provides support for Netscape plug-ins. It corresponds to the HTML element <EMBED SRC = >. If the embedded object's content comes from outside the WebObjects application, use the src attribute. If the embedded object's content is returned by a method within the WebObjects application, use the filename attribute or the data and mimeType attributes.

---

# Bindings

**---

### value

The content for this embedded object in the form of a WOElement object. This data can come from a database, a file, or memory.

**---

### src

URL containing the embedded object. Use this attribute for complete URLs; for relative URLs use filename instead.

**---

### filename

Path to the embedded object relative to the WebServerResources directory.

**---

### framework

Framework that contains the embedded object. This attribute is only necessary if the object is in a different location from the component. That is, if the component and the embedded object are both in the application or if the component and the embedded object are both in the same framework, this attribute isn't necessary. If the embedded object is in a framework and the component is in an application, specify the framework's name here minus the .framework extension. If the embedded object should be in the application but the component is in a framework, specify the "app" keyword in place of the framework name.

**---

### data

Specifies any resource in the form of an NSData; this data can come from a database, a file, or memory. If you specify resource data, you must specify a MIME type.

**---

### mimeType

A string designating a MIME resource type, such as "image/gif"; this type tells the client what to do with data. If you provide data but no MIME type, WebObjects will raise.

**---

### key

A string that functions as a key for caching the data specified in data. If you do not provide a key, the data object is fetched each time it is needed. For further information, see the reference documentation for WOResourceManager, particularly that for the flushDataCache method.**************

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
