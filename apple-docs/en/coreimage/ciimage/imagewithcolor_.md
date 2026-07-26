---
title: 'imageWithColor:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/ciimage/imagewithcolor:'
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/imagewithcolor:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/imagewithcolor%3A.json'
content_hash: 'sha256:fe9fe6bc0c7a047e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# imageWithColor:

<sub>Type Method</sub>

Creates and returns an image of infinite extent whose entire content is the specified color.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIImage *) imageWithColor:(CIColor *) color;
```

## Parameters

- `color` — A color object.

## Return Value

The image object initialized with the color represented by the [CIColor](../cicolor.md) object.

## See Also

### Creating Solid Colors

- [- initWithColor:](<init(color_).md>) — Initializes an image of infinite extent whose entire content is the specified color.
- [blackImage](black.md)
- [blueImage](blue.md)
- [clearImage](clear.md)
- [cyanImage](cyan.md)
- [grayImage](gray.md)
- [greenImage](green.md)
- [magentaImage](magenta.md)
- [redImage](red.md)
- [whiteImage](white.md)
- [yellowImage](yellow.md)
