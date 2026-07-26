---
title: 'init(named:in:with:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/init(named:in:with:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/init(named:in:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/init%28named%3Ain%3Awith%3A%29.json'
content_hash: 'sha256:ab166049eb35bd7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# init(named:in:with:)

<sub>Initializer</sub>

Creates an image by using the named image asset that’s compatible with the configuration you specify.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(named name: String, in bundle: Bundle?, with configuration: UIImage.Configuration?)
```

## Parameters

- `name` — The name of the image asset or file.

- `bundle` — The bundle containing the image file or asset catalog. Specify `nil` to search the app’s main bundle.

- `configuration` — The image configuration that you want. Use this parameter to specify traits and other details that define which variant of the image you want. For example, when requesting a custom symbol image, you can specify whether you want the thin, regular, or bold image variant.

## Return Value

An object containing the image variant that matches the specified configuration data, or `nil` if no suitable image was found.

## Discussion

When searching the asset catalog, this method prefers an asset containing a symbol image over an asset with the same name containing a bitmap image. Because the system supports symbol images in iOS 13 or later, you may include both types of assets in the same asset catalog. The system automatically falls back to the bitmap image on earlier versions of iOS.

You can’t use this method to load system symbol images; use the [+ systemImageNamed:withConfiguration:](<init(systemname_withconfiguration_).md>) method instead.

This method checks the system caches for an image object with the name you specify, and returns the variant of that image that best matches the trait collection you specify. If a matching image object isn’t in the cache, this method creates the image from an available asset catalog or loads the image from disk.

The system may purge cached image data at any time to free up memory. Purging occurs only for unused images that are in the cache.

## See Also

### Loading and caching images

- [Providing images for different appearances](../providing-images-for-different-appearances.md) — Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md) — Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbol images for your app](../creating-custom-symbol-images-for-your-app.md) — Create, organize, and annotate symbol images using SF Symbols.
- [+ imageNamed:inBundle:compatibleWithTraitCollection:](<init(named_in_compatiblewith_).md>) — Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [init(named:in:variableValue:configuration:)](<init(named_in_variablevalue_configuration_).md>) — Creates an image by using the name, configuration, and variable value you specify.
- [+ imageNamed:](<init(named_).md>) — Creates an image object from the specified named asset.
- [init(imageLiteralResourceName:)](<init(imageliteralresourcename_).md>) — Returns the image object for the specified resource.
- [+ systemImageNamed:withConfiguration:](<init(systemname_withconfiguration_).md>) — Creates an image object that contains a system symbol image with the specified configuration.
- [init(systemName:variableValue:configuration:)](<init(systemname_variablevalue_configuration_).md>) — Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [+ systemImageNamed:compatibleWithTraitCollection:](<init(systemname_compatiblewith_).md>) — Creates an image object that contains a system symbol image appropriate for the specified traits.
- [+ systemImageNamed:](<init(systemname_).md>) — Creates an image object that contains a system symbol image.
- [init(resource:)](<init(resource_).md>)
- [Building high-performance lists and collection views](../building-high-performance-lists-and-collection-views.md) — Improve the performance of lists and collections in your app with prefetching and image preparation.
