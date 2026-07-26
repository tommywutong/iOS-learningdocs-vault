---
title: 'init(named:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/init(named:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/init(named:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/init%28named%3A%29.json'
content_hash: 'sha256:b2d034cbfb7a6810'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# init(named:)

<sub>Initializer</sub>

Creates an image object from the specified named asset.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(named name: String)
```

## Parameters

- `name` — The name of the image asset or file.

## Return Value

An object containing an unconfigured version of the image, or `nil` if the method could not find the specified image.

## Discussion

When searching the asset catalog, this method prefers an asset containing a symbol image over an asset with the same name containing a bitmap image. Because the system supports symbol images iOS 13 or later, you may include both types of assets in the same asset catalog. In iOS 12 or earlier, the system automatically chooses the bitmap image.

You can’t use this method to load system symbol images; use the [+ systemImageNamed:](<init(systemname_).md>) method instead.

This method checks the system caches for an image object with the name you specify, and returns the variant of that image that’s best suited for the main screen. If a matching image object isn’t in the cache, this method creates the image from an available asset catalog or loads the image from disk.

The system may purge cached image data at any time to free up memory. Purging occurs only for unused images that are in the cache.

In iOS 9 and later, this method is thread safe.

### Special Considerations

If you intend to display an image only once and don’t want it added to the system’s cache, create it using the [imageWithContentsOfFile:](imagewithcontentsoffile_.md) method instead. Keeping single-use images out of the system image cache can potentially improve the memory use characteristics of your app.

## See Also

### Loading and caching images

- [Providing images for different appearances](../providing-images-for-different-appearances.md) — Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md) — Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbol images for your app](../creating-custom-symbol-images-for-your-app.md) — Create, organize, and annotate symbol images using SF Symbols.
- [+ imageNamed:inBundle:compatibleWithTraitCollection:](<init(named_in_compatiblewith_).md>) — Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [+ imageNamed:inBundle:withConfiguration:](<init(named_in_with_).md>) — Creates an image by using the named image asset that’s compatible with the configuration you specify.
- [init(named:in:variableValue:configuration:)](<init(named_in_variablevalue_configuration_).md>) — Creates an image by using the name, configuration, and variable value you specify.
- [init(imageLiteralResourceName:)](<init(imageliteralresourcename_).md>) — Returns the image object for the specified resource.
- [+ systemImageNamed:withConfiguration:](<init(systemname_withconfiguration_).md>) — Creates an image object that contains a system symbol image with the specified configuration.
- [init(systemName:variableValue:configuration:)](<init(systemname_variablevalue_configuration_).md>) — Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [+ systemImageNamed:compatibleWithTraitCollection:](<init(systemname_compatiblewith_).md>) — Creates an image object that contains a system symbol image appropriate for the specified traits.
- [+ systemImageNamed:](<init(systemname_).md>) — Creates an image object that contains a system symbol image.
- [init(resource:)](<init(resource_).md>)
- [Building high-performance lists and collection views](../building-high-performance-lists-and-collection-views.md) — Improve the performance of lists and collections in your app with prefetching and image preparation.
