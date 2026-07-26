---
title: Responding to changing display modes on Apple TV
framework: UIKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/responding-to-changing-display-modes-on-apple-tv
source_url: 'https://developer.apple.com/documentation/uikit/responding-to-changing-display-modes-on-apple-tv'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/responding-to-changing-display-modes-on-apple-tv.json'
content_hash: 'sha256:2a3cf749faecc927'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md) · [App and environment](app-and-environment.md)

# Responding to changing display modes on Apple TV

<sub>Article</sub>

Change images and resources dynamically when the screen gamut on your device changes.

## Overview

On Apple TV (5th generation), the assets required for an app depend on the screen gamut of the TV being used, with 4K TVs using the Display P3 gamut, and all other resolutions using the sRGB gamut. Also, the screen gamut of the TV can change at any time, switching between 4K and other resolutions. Your app needs to respond to these changes and present the appropriate assets when required.

### Create and place the image assets

In Xcode, create an image asset in an asset catalog. In the Attributes inspector, configure the asset catalog to handle Display P3 images. In the Devices pane, ensure that Apple TV is selected. From the Gamut menu, select sRGB and Display P3. The following image shows the correct settings.

![Screenshot that shows the asset catalog configuration for sRGB and Display P3 image support.](../../../attachments/15e09ea268c10122fd959747c4685fd4/responding-to-changing-display-modes-on-apple-tv-1@2x.png)

### Add images to the asset catalog

Place non-4K images in the 1x (sRGB) slot and 4K images in the 2x (Display P3) slot. The correct image is automatically loaded based on the display gamut of the TV. The following image shows assets placed in their correct containers.

![Screenshot that shows adding 1x and 2x assets to their corresponding slots in an asset catalog.](../../../attachments/ab43abfac159777900d328d49ee69e49/responding-to-changing-display-modes-on-apple-tv-2@2x.png)

### Adapt to screen changes programmatically

Implement the [- traitCollectionDidChange:](<uitraitenvironment/traitcollectiondidchange(__).md>) method to respond to changing device traits. If your app performs expensive operations related to image generation based on the current display gamut, it’s important to verify that the display gamut has changed before performing these operations. The following code shows how to test whether the display gamut changed.

```swift
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    let currentDisplayGamut = self.traitCollection.displayGamut
    if (previousTraitCollection?.displayGamut == .SRGB) && (currentDisplayGamut == .SRGB) {
        // Resolution didn't change. Your code goes here.
    } else if (previousTraitCollection?.displayGamut == .P3) && (currentDisplayGamut == .P3) {
        // Resolution didn't change. Your code goes here.
    } else {
        // Resolution changed. Your code goes here.
    }
}
```

## See Also

### Adaptivity and traits

- [Traits and the trait environment](traits-and-the-trait-environment.md) — Get information about traits and the environment in which your app runs, and share data with your view hierarchy.
