---
title: NSShadow
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsshadow
source_url: 'https://developer.apple.com/documentation/uikit/nsshadow'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsshadow.json'
content_hash: 'sha256:d67a69f4bc1a3ffc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSShadow

<sub>Class</sub>

An object you use to specify attributes to create and style a drop shadow during drawing operations.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class NSShadow
```

## Overview

When you create shadows, the system draws them in the default user coordinate space, where coordinates are independent from the pixel values of any particular device. Rotations, translations, and other transformations of the current transformation matrix (CTM) don’t affect the shadow or the apparent position of the shadow’s light source.

A shadow has two positional parameters: an x-offset and a y-offset. Express these values with a single size data type ([CGSize](../corefoundation/cgsize.md) in iOS, [NSSize](../foundation/nssize.md) in macOS), using the units of the default user coordinate space. Positive values for these offsets extend down and to the right from the user’s perspective.

In addition to its positional parameters, a shadow also contains a blur radius, which specifies how much the system blurs a drawn object’s image mask before compositing the image onto the destination. A value of `0` produces no blur. Larger values produce an increasingly large blurred shadow.

You can use an [NSShadow](nsshadow.md) object in one of two ways. First, you can set it, like a color or a font, where `NSShadow` attributes apply to everything you draw until you apply another shadow or restore a previous graphics state. Second, you can use an `NSShadow` instance as the value for the [shadow](../foundation/nsattributedstring/key/shadow.md) text attribute in Swift or the [NSShadowAttributeName](nsshadowattributename.md) text attribute in Objective-C, so the system applies the shadow to the glyphs corresponding to the characters bearing this attribute.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md)

## Topics

### Creating a shadow

- [- init](<nsshadow/init().md>) — Creates a shadow object with default values.
- [- initWithCoder:](<nsshadow/init(coder_).md>) — Creates a shadow object from data in an unarchiver.

### Managing a shadow

- [shadowOffset](nsshadow/shadowoffset.md) — The shadow’s relative position, which you specify with horizontal and vertical offset values.
- [shadowBlurRadius](nsshadow/shadowblurradius.md) — The blur radius of the shadow.
- [shadowColor](nsshadow/shadowcolor.md) — The color of the shadow.

### Setting a shadow

- [set()](<../appkit/nsshadow/set().md>) — Sets the shadow of subsequent drawing operations to the current shadow.
