---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/NSImageAdditions.html
archived_at: '2026-07-18T01:28:47.175253Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOViewLayout-2.md)

---

# NSImage Additions

__Inherits From:__
NSObject

__Declared in:__
EOInterface/EOControlAssociation.h

---

## Class Description

Enterprise Objects Framework adds one method to NSImage to aid in conversion of image data from databases. This method is used as a factory method for custom value archiving, as described in the EOCustomClassArchiving informal protocol specification. See the NSImage class specification in the Application Kit documentation for a list supported image file formats.

---

## Class Methods

---

### imageWithData:

+ `imageWithData:`(NSData \*)_imageData_

Creates an NSImage from _imageData_ and returns it.

__See also:__

- initWithData:
(NSImage class of the Application Kit),
- TIFFRepresentation
(NSImage class
of the Application Kit)

---

[!](EOViewLayout-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
