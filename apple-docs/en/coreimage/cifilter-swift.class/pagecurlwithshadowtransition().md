---
title: pageCurlWithShadowTransition()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifilter-swift.class/pagecurlwithshadowtransition()
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/pagecurlwithshadowtransition()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/pagecurlwithshadowtransition%28%29.json'
content_hash: 'sha256:f9486604c8a85941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# pageCurlWithShadowTransition()

<sub>Type Method</sub>

Simulates the curl of a page, revealing the target image with added shadow.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func pageCurlWithShadowTransition() -> any CIFilter & CIPageCurlWithShadowTransition
```

## Return Value

The transition image.

## Discussion

This method applies the page curl with shadow transition filter to an image. The effect transitions from one image to another by simulating a curling page, revealing the target image as the page curls with a shadow effect from the backside image.

The page curl with shadow transition filter uses the following properties:

- **`inputImage`** — The starting image with the type [CIImage](../ciimage.md).
- **`targetImage`** — The ending image with the type [CIImage](../ciimage.md).
- **`backsideImage`** — An image used as the backside of the curl with the type [CIImage](../ciimage.md).
- **`extent`** — A [CIVector](../civector.md) representing the extent of the effect.
- **`angle`** — A `float` representing the angle of the motion, in radians as an [NSNumber](../../foundation/nsnumber.md).
- **`shadowAmount`** — A `float` representing the strength of the shadow as an [NSNumber](../../foundation/nsnumber.md).
- **`shadowExtent`** — A [CIVector](../civector.md) representing the rectangular portion of the input image that is used to create the shadow.
- **`shadowSize`** — A `float` representing the maximum amount of pixels to make up the shadow as an [NSNumber](../../foundation/nsnumber.md).
- **`time`** — A `float` representing the parametric time of the transition from start (at time 0) to end (at time 1) as an [NSNumber](../../foundation/nsnumber.md).

The following code creates a page curling back to reveal the target image with an added shadow.

```swift
func pageCurl(inputImage: CIImage, targetImage: CIImage, backsideImage: CIImage) -> CIImage {
    let pageCurlTransition = CIFilter.pageCurlWithShadowTransition()
    pageCurlTransition.inputImage = inputImage
    pageCurlTransition.targetImage = targetImage
    pageCurlTransition.backsideImage = backsideImage
    pageCurlTransition.extent = CGRect(x: 54, y: 90, width: 300, height: 300)
    pageCurlTransition.time = 0.5
    pageCurlTransition.angle = 4
    pageCurlTransition.radius = 100
    pageCurlTransition.shadowAmount = 10
    pageCurlTransition.shadowSize = 6
    pageCurlTransition.shadowExtent = CGRect(x: 32, y: 56, width: 400, height: 400)
    return pageCurlTransition.outputImage!
}
```

![](../../../../attachments/88d677ea78614c06bec80dfe35c25d48/media-3616423@2x.png)

<sub>Three photographs. In the photo on the left, there are multiple small purple flowers photographed close up with good lighting, and the background has a slight blur. In the photograph on the right is a tall building with two trees directly in front of the building. In the center photograph, a page curl with shadow filter is applied, resulting in a still photo of the moving transition. The left photograph is overlaid on the photo on the right with the left side of the overlaid image curling up to reveal more of the city image under. The curl has an added shadow to the underside.</sub>

## See Also

### Filters

- [+ accordionFoldTransitionFilter](<accordionfoldtransition().md>) — Transitions by folding and crossfading an image to reveal the target image.
- [+ barsSwipeTransitionFilter](<barsswipetransition().md>) — Transitions between two images by removing rectangular portions of an image.
- [+ copyMachineTransitionFilter](<copymachinetransition().md>) — Simulates the effect of a copy machine scanner light to transiton between two images.
- [+ disintegrateWithMaskTransitionFilter](<disintegratewithmasktransition().md>) — Transitions between two images using a mask image.
- [+ dissolveTransitionFilter](<dissolvetransition().md>) — Transitions between two images with a fade effect.
- [+ flashTransitionFilter](<flashtransition().md>) — Creates a flash of light to transition between two images.
- [+ modTransitionFilter](<modtransition().md>) — Transitions between two images by applying irregularly shaped holes.
- [+ pageCurlTransitionFilter](<pagecurltransition().md>) — Simulates the curl of a page, revealing the target image.
- [+ rippleTransitionFilter](<rippletransition().md>) — Simulates a ripple in a pond to transiton from one image to another.
- [+ swipeTransitionFilter](<swipetransition().md>) — Gradually transitions from one image to another with a swiping motion.
