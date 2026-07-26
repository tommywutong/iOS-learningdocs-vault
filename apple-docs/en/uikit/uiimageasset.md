---
title: UIImageAsset
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimageasset
source_url: 'https://developer.apple.com/documentation/uikit/uiimageasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimageasset.json'
content_hash: 'sha256:3b55a81a6df1c590'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIImageAsset

<sub>Class</sub>

A container for a collection of images that represent multiple ways of describing a single piece of artwork.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIImageAsset
```

## Overview

A common use case for [UIImageAsset](uiimageasset.md) is the grouping of multiple images of the same item at different display scales. Image asset objects aren’t assigned to instances of [UIImage](uiimage.md) rather; [UIImage](uiimage.md) provides an asset when multiple representations of an image are available. Images retrieved from image asset catalogs using the [+ imageNamed:](<uiimage/init(named_).md>) or [+ imageNamed:inBundle:compatibleWithTraitCollection:](<uiimage/init(named_in_compatiblewith_).md>) methods automatically have an image asset object that allows access to other images from the catalog.

### Register an image

When you register an image with an image asset, you associate a [UITraitCollection](uitraitcollection.md) object with the image. The trait collection must contain the [displayScale](uitraitcollection/displayscale.md) and [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) trait properties. If you don’t define these traits in the trait collection, the following defaults are assigned:

- [displayScale](uitraitcollection/displayscale.md) = `1.0`
- [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) = [UIUserInterfaceIdiomUnspecified](uiuserinterfaceidiom/unspecified.md)

For example, if you create a trait collection that only contains a horizontal size class, the default display scale and idiom are added when the image is registered.

### Retrieve an image

When you retrieve or unregister an image from an image asset, you do so using the trait collection that was used to register the image. To ensure the correct image is retrieved, the trait collection used must contain the [displayScale](uitraitcollection/displayscale.md) and [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) traits. If these traits aren’t defined in the trait collection, the following defaults are assigned:

- [displayScale](uitraitcollection/displayscale.md) = scale of the current device
- [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) = the type of interface used on the current device

For example, if you create a trait collection that only contains a horizontal size class, the default display scale and idiom of the current device are added when searching the `UIImageAsset` for an image.

[UIImageView](uiimageview.md) automatically retrieves the correct image when [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) is called on it.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](../foundation/nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializing an image asset

- [- init](<uiimageasset/init().md>) — Creates a new image asset object.
- [- initWithCoder:](<uiimageasset/init(coder_).md>) — Creates an image asset from data in an unarchiver.

### Registering and unregistering images

- [- registerImage:withTraitCollection:](<uiimageasset/register(__with_)-2plm5.md>) — Registers an image with the specified trait collection.
- [- registerImage:withConfiguration:](<uiimageasset/register(__with_)-89c5b.md>) — Registers an image with the specified image configuration details.
- [- unregisterImageWithTraitCollection:](<uiimageasset/unregister(imagewith_).md>) — Unregisters the image with the specified trait collection from the image asset.
- [- unregisterImageWithConfiguration:](<uiimageasset/unregisterimage(with_).md>) — Unregisters the image with the specified image configuration details from the image asset.

### Retrieving an image from an image asset

- [- imageWithTraitCollection:](<uiimageasset/image(with_)-3dsgf.md>) — Retrieves the variant of the image that best matches the specified trait collection.
- [- imageWithConfiguration:](<uiimageasset/image(with_)-8jdwv.md>) — Retrieves the variant of the image that best matches the specified image configuration details.

## See Also

### Assets

- [NSDataAsset](nsdataasset.md) — An object from a data set type stored in an asset catalog.
