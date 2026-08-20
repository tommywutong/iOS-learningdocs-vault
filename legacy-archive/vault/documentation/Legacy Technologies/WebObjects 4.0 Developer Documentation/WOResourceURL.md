---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOResourceURL.html
archived_at: '2026-07-15T08:00:48.218340Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Dynamic Elements](Dynamic%20Element%20Specifications.md)

---

# WOResourceURL

---

# Synopsis

WOResourceURL { filename= _imageFileName_; [framework = _frameworkBaseName_|"app" ;] | data=_dataObject_; mimeType=_typeString_; [key=_cacheKey_;]... };

---

# Description

WOResourceURL enables the creation of URLs to return resources, such as images and sounds. You can use this element for a variety of purposes, but it is primarily intended to support JavaScript within a WebObjects application.

---

# Bindings

**---

### filename

Path to the resource relative to the WebServerResources directory.

**---

### framework

Framework that contains the resource file. This attribute is only necessary if the file is in a different location from the component. That is, if the component and the file are both in the application or if the component and the file are both in the same framework, this attribute isn't necessary. If the resource file is in a framework and the component is in an application, specify the framework's name here (minus the .framework extension). If the resource file should be in the application but the component is in a framework, specify the "app" keyword in place of the framework name.

**---

### data

Specifies any resource in the form of an NSData; this data can come from a database, a file, or memory. If you specify resource data, you must specify a MIME type.

**---

### mimeType

A string designating a MIME resource type, such as "image/gif"; this type tells the client what to do with data. If you provide data but no MIME type, WebObjects will raise.

**---

### key

A string that functions as a key for caching the data specified in data. If you do not provide a key, the data object must be fetched each time it is needed. For further information, see the reference documentation for WOResourceManager, particularly that for the flushDataCache method.**********

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
