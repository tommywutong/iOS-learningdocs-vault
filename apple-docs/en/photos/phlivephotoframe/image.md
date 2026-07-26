---
title: image
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotoframe/image
source_url: 'https://developer.apple.com/documentation/photos/phlivephotoframe/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotoframe/image.json'
content_hash: 'sha256:dd362968f73cd7aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHLivePhotoFrame](../phlivephotoframe.md)

# image

<sub>Instance Property</sub>

The image content of the frame to be processed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var image: CIImage { get }
```

## Discussion

Core Image provides several ways to perform your adjustments to this image:

- Create a single [CIFilter](../../coreimage/cifilter-swift.class.md) object, or a chain of filters. Set this image as the [kCIInputImageKey](../../coreimage/kciinputimagekey.md) parameter of the first filter in the chain, and use the last filter’s [outputImage](../../coreimage/cifilter-swift.class/outputimage.md) property to access the result. Each [CIFilter](../../coreimage/cifilter-swift.class.md) object can be a built-in filter or a custom filter subclass that you create.
- Use the [applyingFilter(_:parameters:)](<../../coreimage/ciimage/applyingfilter(__parameters_).md>) method to conveniently apply one of the many built-in Core Image filters.
- Access pixel buffers directly and apply custom image processing using a custom [CIImageProcessorKernel](../../coreimage/ciimageprocessorkernel.md) subclass.

In all cases, you obtain another [CIImage](../../coreimage/ciimage.md) object representing the result of your adjustments. Return that image from your [frameProcessor](../phlivephotoeditingcontext/frameprocessor.md) block. (See the [frameProcessor](../phlivephotoeditingcontext/frameprocessor.md) description for example code.)
