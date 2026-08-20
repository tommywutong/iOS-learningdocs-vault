---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/NSImageAdditions.html
archived_at: '2026-07-15T08:11:45.669162Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)

# NSImage Additions

> __Category
> of:__ NSImage

> __Declared in:__ : EOInterface/EOControlAssociation.h

---

## Category Description

---

Enterprise Objects Framework adds one method to NSImage to
aid in conversion of image data from databases. This method is used
as a factory method for custom value archiving, as described in
the EOCustomClassArchiving informal protocol specification. See
the NSImage class specification in the Application Kit documentation
for a list supported image file formats.

## Class Methods

---

### imageWithData:

`+ imageWithData:(NSData *)imageData`

Creates an NSImage from _imageData_ and
returns it.

__See Also:__  __-
initWithData:__ (NSImage class of the Application Kit), __-
TIFFRepresentation__ (NSImage class of the Application
Kit)

---

[![Table of Contents](attachments/images/up.gif)](../EOInterfaceTOC.md)
