---
title: 'init(patternImage:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicolor/init(patternimage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicolor/init(patternimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicolor/init%28patternimage%3A%29.json'
content_hash: 'sha256:a45797ef3445181c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIColor](../uicolor.md)

# init(patternImage:)

<sub>Initializer</sub>

Creates a color object using the specified image object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(patternImage image: UIImage)
```

## Parameters

- `image` — The image to use when creating the pattern color.

## Return Value

The pattern color.

## Discussion

You can use pattern colors to set the fill or stroke color just as you’d a solid color. During drawing, the image in the pattern color is tiled as necessary to cover the given area.

By default, the phase of the returned color is 0, which causes the top-left corner of the image to be aligned with the drawing origin. To change the phase, make the color the current color and then use the [setPatternPhase(_:)](<../../coregraphics/cgcontext/setpatternphase(__).md>) function to change the phase.
