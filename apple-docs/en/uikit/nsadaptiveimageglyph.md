---
title: NSAdaptiveImageGlyph
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsadaptiveimageglyph
source_url: 'https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsadaptiveimageglyph.json'
content_hash: 'sha256:49f3e3c480679c70'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSAdaptiveImageGlyph

<sub>Class</sub>

A data object for an emoji-like image that can appear in attributed text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSAdaptiveImageGlyph
```

## Overview

An [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) contains an image that automatically adapts to different sizes and resolutions. The text system creates instances of this type to represent custom emojis that people create using the system interfaces. This type manages multiple images, along with metadata describing how to adapt those images correctly to different fonts and font attributes.

Typically, you receive new [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) objects only from the text-input system. When someone creates a new emoji and inserts it into their text, TextKit creates an instance of this type to represent it. If your app examines or changes the attributes of attributed strings, preserve the [adaptiveImageGlyph](../foundation/nsattributedstring/key/adaptiveimageglyph.md) attribute in Swift or the [NSAdaptiveImageGlyphAttributeName](nsadaptiveimageglyphattributename.md) attribute in Objective-C when making any changes. For example, if you filter unknown attributes in a custom text-storage object, update your code to preserve this attribute. The value of the attribute is an [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) containing the emoji data. You can save the image data with the rest of your content and use the data to recreate the type later.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CTAdaptiveImageProviding](../coretext/ctadaptiveimageproviding.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an adaptive image glyph

- [- initWithImageContent:](<nsadaptiveimageglyph/init(imagecontent_).md>) — Create an adaptive image glyph from previously saved data.
- [- initWithCoder:](<nsadaptiveimageglyph/init(coder_).md>)

### Getting the image data

- [imageContent](nsadaptiveimageglyph/imagecontent.md) — The raw data for the image.

### Getting the content metadata

- [contentIdentifier](nsadaptiveimageglyph/contentidentifier.md) — A unique identifier for this image.
- [contentDescription](nsadaptiveimageglyph/contentdescription.md) — An alternate textual description of the image contents.
- [contentType](nsadaptiveimageglyph/contenttype.md) — The image data format to use for this image type.

### Examining attributed strings

- [adaptiveImageGlyph](../foundation/nsattributedstring/key/adaptiveimageglyph.md) — The adaptive image glyph for the text.

### Initializers

- [init(_:)](<nsadaptiveimageglyph/init(__).md>)

## See Also

### Attachments

- [NSTextAttachment](nstextattachment.md) — The values for the attachment characteristics of attributed strings and related objects.
- [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) — A container object that associates a text attachment at a particular document location with a view object.
- [NSTextAttachmentContainer](nstextattachmentcontainer.md) — A set of methods that defines the interface to text attachment objects from a layout manager.
- [NSTextAttachmentLayout](nstextattachmentlayout.md) — A set of methods that defines the interface to attachment objects from a text layout manager.
