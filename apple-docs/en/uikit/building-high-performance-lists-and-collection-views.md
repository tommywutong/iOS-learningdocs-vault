---
title: Building high-performance lists and collection views
framework: UIKit
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, Xcode 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/building-high-performance-lists-and-collection-views
source_url: 'https://developer.apple.com/documentation/uikit/building-high-performance-lists-and-collection-views'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/building-high-performance-lists-and-collection-views.json'
content_hash: 'sha256:aef3e0e250d6496b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [Images and PDF](images-and-pdf.md) · [UIImage](uiimage.md)

# Building high-performance lists and collection views

<sub>Sample Code</sub>

Improve the performance of lists and collections in your app with prefetching and image preparation.

## Overview

> [!note] Note
> This sample code project is associated with WWDC21 session [10252: Make Blazing Fast Lists and Collection Views](https://developer.apple.com/wwdc21/10252/).

## See Also

### Loading and caching images

- [Providing images for different appearances](providing-images-for-different-appearances.md) — Supply image resources appropriate for light and dark appearances and for high-contrast environments.
- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md) — Create scalable images that integrate with your app’s text, and adjust the appearance of those images dynamically.
- [Creating custom symbol images for your app](creating-custom-symbol-images-for-your-app.md) — Create, organize, and annotate symbol images using SF Symbols.
- [+ imageNamed:inBundle:compatibleWithTraitCollection:](<uiimage/init(named_in_compatiblewith_).md>) — Creates an image object using the named image asset that’s compatible with the specified trait collection.
- [+ imageNamed:inBundle:withConfiguration:](<uiimage/init(named_in_with_).md>) — Creates an image by using the named image asset that’s compatible with the configuration you specify.
- [init(named:in:variableValue:configuration:)](<uiimage/init(named_in_variablevalue_configuration_).md>) — Creates an image by using the name, configuration, and variable value you specify.
- [+ imageNamed:](<uiimage/init(named_).md>) — Creates an image object from the specified named asset.
- [init(imageLiteralResourceName:)](<uiimage/init(imageliteralresourcename_).md>) — Returns the image object for the specified resource.
- [+ systemImageNamed:withConfiguration:](<uiimage/init(systemname_withconfiguration_).md>) — Creates an image object that contains a system symbol image with the specified configuration.
- [init(systemName:variableValue:configuration:)](<uiimage/init(systemname_variablevalue_configuration_).md>) — Creates an image object that contains a system symbol image with the configuration and variable value you specify.
- [+ systemImageNamed:compatibleWithTraitCollection:](<uiimage/init(systemname_compatiblewith_).md>) — Creates an image object that contains a system symbol image appropriate for the specified traits.
- [+ systemImageNamed:](<uiimage/init(systemname_).md>) — Creates an image object that contains a system symbol image.
- [init(resource:)](<uiimage/init(resource_).md>)

## Download

- [BuildingHighPerformanceListsAndCollectionViews.zip](https://docs-assets.developer.apple.com/published/7f5574e912c4/BuildingHighPerformanceListsAndCollectionViews.zip)
