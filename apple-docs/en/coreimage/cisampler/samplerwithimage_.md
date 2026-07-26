---
title: 'samplerWithImage:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cisampler/samplerwithimage:'
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler/samplerwithimage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler/samplerwithimage%3A.json'
content_hash: 'sha256:b146a7dfeff32797'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISampler](../cisampler.md)

# samplerWithImage:

<sub>Type Method</sub>

Creates and returns a sampler that references an image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) samplerWithImage:(CIImage *) im;
```

## Parameters

- `im` — The image that you want the sampler to reference.

## Return Value

A sampler object that references the image specified by the `im` argument.

## See Also

### Related Documentation

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)

### Creating a Sampler

- [samplerWithImage:keysAndValues:](samplerwithimage_keysandvalues_.md) — Creates and returns a sampler that references an image using options specified as key-value pairs.
- [samplerWithImage:options:](samplerwithimage_options_.md) — Creates and returns a sampler that references an image using options specified in a dictionary.
