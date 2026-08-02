---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/Reference/DynamicElements/WOActiveImage.html
archived_at: '2026-07-15T08:14:38.827901Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md) 

# WOActiveImage

## Element Description

A WOActiveImage displays an image within the HTML page. If
the WOActiveImage is disabled, it simply displays its image as a
passive element in the page. If enabled, the image is active; that
is, clicking the image generates a request.

WOActiveImages are intended to be used outside of an HTML
form. WOActiveImage functions as a mapped, active image. When the
user clicks such a WOActiveImage, the coordinates of the click are sent
back to the server. Depending on where the user clicks, different
actions can be invoked. An image map file associates actions with
each of the defined areas of the image. If an image map file is
not specified, the method specified by the action attribute is performed
when the image is clicked, or if the __href__ attribute
is specified, the image acts as a hyperlink and takes you to that
destination.

Within an HTML form, a WOActiveImage functions as a graphical
submit button. However, it is better to use a [WOImageButton](WOImageButton.md#apple-ijbeuskdjbduk) instead
of WOActiveImage to create a graphic submit button or a mapped image
within a form.

## Synopsis

WOActiveImage {filename= _imageFileName_;
[framework = _frameworkBaseName_|"app";]
| src=_aURL_; | value=_aMethod_;
action=_aMethod_ | href=_aURL_;
| data=_dataObject_; mimeType=_typeString_; [key=_cacheKey_;]
[imageMapFile=_aString_]; [name=_aString_;]
[x=_aNumber_; y=_aNumber_;] [target=_frameName_;]
[disabled=_aBoolean_;] ... };

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
image file is in a framework and the component is in the application,
specify the framework's name here (minus the .framework extension).
If the image file should be in the application but the component
is in a framework, specify the "app" keyword in place
of the framework name.

**src**
: URL containing the image data. Use this attribute for
complete URLs; for relative URLs use __filename__ instead.

**value**
: Image data in the form of a WOElement object.
This data can come from a database, a file, or memory.

**action**
: Method to invoke when this element is clicked. If __imageMapFile__ is
specified, __action__ is only invoked if the
click is outside any mapped area. In other words, __action__ defines
the default action of the active image.

**href**
: URL to direct the browser to as a default when the image
is clicked and no hot zones are hit.

**data**
: Specifies an image resource in the form of an NSData;
this data can come from a database, a file, or memory. If you specify
resource data, you must specify a MIME type.

**mimeType**
: A string designating a MIME resource type, such as "image/gif",
to be put in the content-type header field; this type tells the
client what to do with data. If you provide __data__ but
no MIME type, WebObjects will raise.

**key**
: A string that the application uses as a key for caching
the data specified in __data__. If you do not
provide a key, the data object must be fetched each time it is needed.
For further information, see the reference documentation for the WOResourceManager class,
(in particular, see the __flushDataCache__ method).

**imageMapFile**
: Name of the image map file.

**name**
: If __name__ is specified then the
hit point is specified as
name.x=_value_; name.y=_value_;
in the form. This is useful when you need to use this element to
submit a form to an external URL that expects the hit point to be
expressed in a certain format.

**x, y**
: If specified, returns the coordinates of the user's
click within the image.

**target**
: Frame in a frameset that will receive the page returned
as a result of the user's click.

**disabled**
: If disabled evaluates to `true` (or `YES`),
a regular image element (`<IMG>`)
is generated rather than an active image.

## The Image Map File

If the __imageMapFile__ is specified,
WebObjects searches for the image map file in the application and,
if the image is in a framework, the search continues in the framework
where the image resides. You should put image map files into the
Resources suitcase in your Project Builder project. If your project has
localized images, the image map file may also need to be localized.
If you choose to have localized mapped images, you must have a corresponding
map file for each localized image (unless you only have one map
file which is not in any locale-specific .lproj directory).

|  |
| --- |
| The image map file must be in the same location as the image. For example, if the image is in a framework, the image map file must be in that same framework. |

Each line in the image map file has this format:

_shape_ _action_ _coordinate-list_

**_shape_**
: Either `rect`, `circle`,
or `poly`. For a `rect` shape,
the coordinates x1,y1 specify the upper-left corner of the hot zone,
and x2,y2 specify lower-right corner. For a `circle` shape,
the x1,y1 is the origin, and x2,y2 is a point on the circle. For
the `poly` shape, each
coordinate is a vertex: up to 100 vertices are supported.

**_action_**
: Name of the method to invoke when the image is clicked.

**_coordinate-list_**
: The list of coordinates (x1,y1 x2,y2 ...) as described
under _shape_, above.

Here are some sample entries in an image map file:

> ```
> rect home 0,0 135,56
> rect buy 135,0 270,56
> ```

[![Table of Contents](attachments/Reference/DynamicElements/images/up.gif)](DynamicElementsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
