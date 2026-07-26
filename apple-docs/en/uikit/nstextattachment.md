---
title: NSTextAttachment
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nstextattachment
source_url: 'https://developer.apple.com/documentation/uikit/nstextattachment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextattachment.json'
content_hash: 'sha256:4dcd93782d65fdff'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSTextAttachment

<sub>Class</sub>

The values for the attachment characteristics of attributed strings and related objects.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSTextAttachment
```

## Overview

The [NSAttributedString](../foundation/nsattributedstring.md) class uses text attachment objects as the values for attachment attributes (stored in the attributed string under the [attachment](../foundation/nsattributedstring/key/attachment.md) key in Swift or the [NSAttachmentAttributeName](nsattachmentattributename.md) key in Objective-C).

A text attachment object contains either an [NSData](../foundation/nsdata.md) object or an [FileWrapper](../foundation/filewrapper.md) object, which in turn holds the contents of the attached file. The properties of this class configure the appearance of the text attachment in your interface. In macOS, the text attachment also uses a cell object that conforms to the [NSTextAttachmentCellProtocol](../appkit/nstextattachmentcellprotocol.md) protocol to draw the image that represents the text and handles mouse events. For more information about text attachments, see the [NSAttributedString](../foundation/nsattributedstring.md) and [NSTextView](../appkit/nstextview.md).

In macOS 12 and iOS 15 and later, [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) and [NSTextAttachmentLayout](nstextattachmentlayout.md) provide additional capabilities to represent document locations in terms of an [NSTextLocation](nstextlocation.md) or an [NSTextRange](nstextrange.md), and provide support for view-based text attachments.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [NSTextAttachmentContainer](nstextattachmentcontainer.md), [NSTextAttachmentLayout](nstextattachmentlayout.md), [UIAccessibilityContentSizeCategoryImageAdjusting](uiaccessibilitycontentsizecategoryimageadjusting.md)

## Topics

### Initializing a text attachment

- [init(fileWrapper:)](<../appkit/nstextattachment/init(filewrapper_).md>) — Creates a text attachment object to contain the specified file wrapper.
- [- initWithData:ofType:](<nstextattachment/init(data_oftype_).md>) — Creates a text attachment object with the specified data.
- [+ textAttachmentWithImage:](<nstextattachment/init(image_).md>) — Creates a text attachment object to contain the specified image.

### Defining the attachment’s contents

- [bounds](nstextattachment/bounds.md) — The layout bounds of the text attachment’s graphical representation in the text coordinate system.
- [contents](nstextattachment/contents.md) — The contents for the text attachment.
- [fileType](nstextattachment/filetype.md) — The file type of the contents for the text attachment.
- [image](nstextattachment/image.md) — An instance of the relevant image class that represents the contents of the text attachment object.
- [fileWrapper](nstextattachment/filewrapper.md) — The text attachment’s file wrapper.
- [allowsTextAttachmentView](nstextattachment/allowstextattachmentview.md) — A Boolean value that determines whether the text attachment uses text attachment views.
- [usesTextAttachmentView](nstextattachment/usestextattachmentview.md) — A Boolean value that indicates whether the text attachment uses text attachment views.
- [lineLayoutPadding](nstextattachment/linelayoutpadding.md) — The layout padding before and after the text attachment bounds.

### Setting the attachment cell

- [attachmentCell](../appkit/nstextattachment/attachmentcell.md) — The object that draws the icon for the text attachment and handles mouse events.

### Constants

- [NSAttachmentCharacter](nstextattachment/character.md) — Specifies a character that denotes an attachment.

### Convenience methods

- [+ registerTextAttachmentViewProviderClass:forFileType:](<nstextattachment/registerviewproviderclass(__forfiletype_).md>) — Registers a specific file type with the attachment view provider.
- [+ textAttachmentViewProviderClassForFileType:](<nstextattachment/textattachmentviewproviderclass(forfiletype_).md>) — Returns the text attachment view provider class, if any, for the file type you specify.

### Initializers

- [init(coder:)](<nstextattachment/init(coder_).md>)

## See Also

### Attachments

- [NSTextAttachmentViewProvider](nstextattachmentviewprovider.md) — A container object that associates a text attachment at a particular document location with a view object.
- [NSAdaptiveImageGlyph](nsadaptiveimageglyph.md) — A data object for an emoji-like image that can appear in attributed text.
- [NSTextAttachmentContainer](nstextattachmentcontainer.md) — A set of methods that defines the interface to text attachment objects from a layout manager.
- [NSTextAttachmentLayout](nstextattachmentlayout.md) — A set of methods that defines the interface to attachment objects from a text layout manager.
