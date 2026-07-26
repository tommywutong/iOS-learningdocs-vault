---
title: name
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cikernel/name
source_url: 'https://developer.apple.com/documentation/coreimage/cikernel/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cikernel/name.json'
content_hash: 'sha256:fdd8f76a5221b135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIKernel](../cikernel.md)

# name

<sub>Instance Property</sub>

The name of the kernel routine.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var name: String { get }
```

## Discussion

The name of a kernel routine is the identifier used to declare it in the Core Image Kernel Language source code. For example, if you use the [+ kernelWithString:](<init(source_).md>) method to create a kernel from the source code below, the name of the returned [CIKernel](../cikernel.md) object is “moveUpTwoPixels”.

```objc
kernel vec4 moveUpTwoPixels (sampler image) {
    vec2 dc = destCoord();
    vec2 offset = vec2(0.0, 2.0);
    return sample (image, samplerTransform (image, dc + offset));
}
```
