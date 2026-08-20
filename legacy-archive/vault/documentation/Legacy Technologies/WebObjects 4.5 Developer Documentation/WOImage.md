---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOImage.html
archived_at: '2026-07-15T08:09:53.332621Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOImage

## Element Description

A WOImage displays an image in the HTML. It corresponds to
the HTML element `<IMG SRC="URL">`.

## Synopsis

WOImage { src=_aURL_;
| value=_imageData_; | filename= _imageFileName_;
[framework = _frameworkBaseName_ |
"app" ;] | data=_dataObject_;
mimeType=_typeString_; [key=_cacheKey_;]...
};

## Bindings

**src**
: URL containing the image data. Use this attribute for
complete URLs; for relative URLs use __filename__ instead.

**value**
: Image data in the form of a WOElement object. This data
can come from a database, a file, or memory.

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
is in a framework, specify the `"app"` keyword
in place of the framework name.

**data**
: Specifies an image resource in the form of an NSData;
this data can come from a database, a file, or memory. If you specify
resource data, you must specify a MIME type.

**mimeType**
: A string designating a MIME resource type, such as `"image/gif"`,
to be put in the content-type header; this type tells the client
what to do with data. If you provide __data__ but no
MIME type, WebObjects will raise.

**key**
: A string that the application uses as a key for caching
the data specified in __data__. If you do not
provide a key, the data object must be fetched each time it is needed.
For further information, see the reference documentation for the WOResourceManager class, particularly
that for the __flushDataCache__ method.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
