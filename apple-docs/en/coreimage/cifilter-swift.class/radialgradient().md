---
title: radialGradient()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/radialgradient()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/radialgradient()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/radialgradient%28%29.json'
content_hash: 'sha256:955865dc5c274f9d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# radialGradient()

<sub>Type Method</sub>

Generates a gradient that varies radially between two circles having the same center.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func radialGradient() -> any CIFilter & CIRadialGradient
```

## Return Value

The generated image.

## Discussion

This method generates a radial-gradient image. The effect generates a color shift between the `radius0` and `radius1` properties.

The radial-gradient filter uses the following properties:

- **`center`** — A [CGPoint](../../corefoundation/cgpoint.md) representing the center of the effect as x and y coordinates.
- **`color0`** — A [CIColor](../cicolor.md) representing the first color to use in the gradient.
- **`color1`** — A [CIColor](../cicolor.md) representing the second color to use in the gradient.
- **`radius0`** — A `float` representing the radius of the starting circle to use in the gradient as a [NSNumber](../../foundation/nsnumber.md).
- **`radius1`** — A `float` representing the radius of the ending circle to use in the gradient as a [NSNumber](../../foundation/nsnumber.md).

The following code creates a filter that generates a gradient image:

```swift
func radial() -> CIImage {
    let radialGradient = CIFilter.radialGradient()
    radialGradient.center = CGPoint(x: 150, y: 150)
    radialGradient.radius0 = 5
    radialGradient.radius1 = 100
    radialGradient.color0 = CIColor(red: 246/255, green: 145/255, blue: 181/255)
    radialGradient.color1 = CIColor(red: 110/255, green: 81/255, blue: 161/255)
    return radialGradient.outputImage!
}
```

![An image that gradually changes in color from pink in the center to purple in the periphery.](../../../../attachments/777f45cb51953b0afb3947f48465b672/media-3558800@2x.png)

## See Also

### Filters

- [+ gaussianGradientFilter](<gaussiangradient().md>) — Generates a gradient that varies from one color to another using a Gaussian distribution.
- [+ hueSaturationValueGradientFilter](<huesaturationvaluegradient().md>) — Generates a gradient representing a specified color space.
- [+ linearGradientFilter](<lineargradient().md>) — Generates a color gradient that varies along a linear axis between two defined endpoints.
- [+ smoothLinearGradientFilter](<smoothlineargradient().md>) — Generates a gradient that blends colors along a linear axis between two defined endpoints.
