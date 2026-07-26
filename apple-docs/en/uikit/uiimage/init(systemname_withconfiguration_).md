---
title: 'init(systemName:withConfiguration:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimage/init(systemname:withconfiguration:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimage/init(systemname:withconfiguration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimage/init%28systemname%3Awithconfiguration%3A%29.json'
content_hash: 'sha256:2bcf497ba7f8e848'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImage](../uiimage.md)

# init(systemName:withConfiguration:)

<sub>Initializer</sub>

Creates an image object that contains a system symbol image with the specified configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init?(systemName name: String, withConfiguration configuration: UIImage.Configuration?)
```

## Parameters

- `name` — The name of the system symbol image.

- `configuration` — The image configuration the system applies to the image.

## Return Value

The object containing the image variant that matches the specified configuration data, or `nil` if no suitable image was found.

## Discussion

Use this method to retrieve system-defined symbol images. To retrieve a custom symbol image you store in an asset catalog, use the [+ imageNamed:inBundle:withConfiguration:](<init(named_in_with_).md>) method instead.

This method checks the system caches for an image with the specified name and returns the variant of that image that’s best suited for the configuration you specify. If a matching image object isn’t in the cache, this method creates the image from the system symbol image.

The system may purge cached image data at any time to free up memory. Purging occurs only for unused images that are in the cache.

To look up the names of system symbol images, download the SF Symbols app from [Apple Design Resources](https://developer.apple.com/design/resources/).

## See Also

### Loading and caching images

- [Providing images for different appearances](../providing-images-for-different-appearances.md) — Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md) — Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbol images for your app](../creating-custom-symbol-images-for-your-app.md) — Create, organize, and annotate symbol images using SF Symbols.
- [+ imageNamed:inBundle:compatibleWithTraitCollection:](<init(named_in_compatiblewith_).md>) — Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [+ imageNamed:inBundle:withConfiguration:](<init(named_in_with_).md>) — Creates an image by using the named image asset that’s compatible with the configuration you specify.
- [init(named:in:variableValue:configuration:)](<init(named_in_variablevalue_configuration_).md>) — Creates an image by using the name, configuration, and variable value you specify.
- [+ imageNamed:](<init(named_).md>) — Creates an image object from the specified named asset.
- [init(imageLiteralResourceName:)](<init(imageliteralresourcename_).md>) — Returns the image object for the specified resource.
- [init(systemName:variableValue:configuration:)](<init(systemname_variablevalue_configuration_).md>) — Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [+ systemImageNamed:compatibleWithTraitCollection:](<init(systemname_compatiblewith_).md>) — Creates an image object that contains a system symbol image appropriate for the specified traits.
- [+ systemImageNamed:](<init(systemname_).md>) — Creates an image object that contains a system symbol image.
- [init(resource:)](<init(resource_).md>)
- [Building high-performance lists and collection views](../building-high-performance-lists-and-collection-views.md) — Improve the performance of lists and collections in your app with prefetching and image preparation.
