---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOBody.html
archived_at: '2026-07-15T08:14:38.860008Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOBody

## Element Description

WOBody specifies the background image to display for the HTML
page. All bindings for this element are related to the background
image.

## Synopsis

WOBody {src=_aURL_ | filename= _imageFileName_;
[framework = _frameworkBaseName_|"app"
;] | data=_dataObject_; mimeType=_typeString_;
[key=_cacheKey_;]... };

## Bindings

**src**
: URL containing the image data. Use this attribute for
complete URLs; for relative URLs use __filename__ instead.

**filename**
: Path to the image relative to the WebServerResources
directory.

**framework**
: Framework that contains the image file. This attribute
is only necessary if the image file is in a different location from
the component. That is, if the component and the image file are both
in the application or if the component and the image file are both
in the same framework, this attribute isn't necessary. If the
image file is in a framework and the component is in an application,
specify the framework's name here (minus the `.framework` extension).
If the image file should be in the application but the component
is in a framework, specify the "app" keyword in place
of the framework name.

**data**
: Specifies any resource in the form of an NSData object;
this data can come from a database, a file, or memory. If you specify
resource data, you must specify a MIME type.

**mimeType**
: A string designating a MIME resource type, such as "image/gif";
this type tells the client what to do with data. If you provide __data__ but
no MIME type, WebObjects will raise.

**key**
: A string that functions as a key for caching the data
specified in __data__. If you do not provide a
key, the data object must be fetched each time it is needed. For
further information, see the reference documentation for the WOResourceManager class
(pay particular attention to the __flushDataCache__ method).

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
