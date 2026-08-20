---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Reference/DynamicElements/WOImageButton.html
archived_at: '2026-07-15T08:09:53.347513Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Dynamic Elements

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)

---

# WOImageButton

## Element Description

WOImageButton is a graphical submit button. Clicking the image
generates a request and submits the enclosing form's values. You
often use WOImageButton when you need more than one submit button within
a form.

## Synopsis

WOImageButton { filename=_anImageName_;
[framework=_aFrameworkName_ | "app";]
| src=_aURL_; | value=_aMethod_;
action=_aMethod_; | data=_dataObject_;
mimeType=_typeString_; [key=_cacheKey_;] [imageMapFile=_aString_;]
[name=_aString_;] [x=_aNumber_;
y=_aNumber_;] [disabled=_aBoolean_;]
... };

## Bindings

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

**src**
: URL containing the image data. Use this attribute for
complete URLs; for relative URLs use __filename__ instead.

**value**
: Image data in the form of a WOElement object.
This data can come from a database, a file, or memory.

**action**
: Action method to invoke when this element is clicked.

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
provide a key, the data object must be reloaded each time it is
needed. For further information, see the reference documentation
for the WOResourceManager class, particularly
that for the __flushDataCache__ method.

**imageMapFile**
: Name of the image map file. See the [WOActiveImage](WOActiveImage.md#apple-ijdumqsdi5cue) description for more
information.

**name**
: Name that uniquely identifies this element within the
form. You may specify a name or let WebObjects automatically assign
one at runtime.

**x, y**
: If specified, returns the coordinates of the user's
click within the image.

**disabled**
: If __disabled__ evaluates to `true` (or `YES`),
the element generates a static image (`<IMG>`)
instead of an active image.

[![up](attachments/images/up.gif)](DynamicElementsTOC.md)
