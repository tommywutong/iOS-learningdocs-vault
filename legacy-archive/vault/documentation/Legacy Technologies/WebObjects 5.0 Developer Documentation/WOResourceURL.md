---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOResourceURL.html
archived_at: '2026-07-15T08:14:39.241164Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOResourceURL

## Element Description

WOResourceURL enables the creation of URLs to return resources,
such as images and sounds. You can use this element for a variety
of purposes, but it is primarily intended to support JavaScript
within a WebObjects application.

## Synopsis

WOResourceURL { filename= _imageFileName_;
[framework = _frameworkBaseName_ |
"app";] | data=_dataObject_;
mimeType=_typeString_; [key=_cacheKey_;]...
};

## Bindings

**filename**
: Path to the resource relative to the WebServerResources
directory.

**framework**
: Framework that contains the resource file. This attribute
is only necessary if the file is in a different location from the
component. That is, if the component and the file are both in the application
or if the component and the file are both in the same framework,
this attribute isn't necessary. If the resource file is in a framework
and the component is in an application, specify the framework's
name here (minus the `.framework` extension).
If the resource file should be in the application but the component
is in a framework, specify the `"app"` keyword
in place of the framework name.

**data**
: Specifies any resource in the form of an NSData;
this data can come from a database, a file, or memory. If you specify
resource data, you must specify a MIME type.

**mimeType**
: A string designating a MIME resource type, such as `"image/gif"`;
this type tells the client what to do with __data__.
If you provide __data__ but no MIME type, WebObjects
will raise.

**key**
: A string that functions as a key for caching the data
specified in __data__. If you do not provide a
key, the data object must be fetched each time it is needed. For
further information, see the reference documentation for the WOResourceManager class,
particularly that for the __flushDataCache__ method.

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
