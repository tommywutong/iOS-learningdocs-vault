---
title: 'init(image:options:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cisampler/init(image:options:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler/init(image:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler/init%28image%3Aoptions%3A%29.json'
content_hash: 'sha256:a4d46e44c8894244'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISampler](../cisampler.md)

# init(image:options:)

<sub>Initializer</sub>

Initializes the sampler with an image object using options specified in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(image im: CIImage, options dict: [AnyHashable : Any]? = nil)
```

## Parameters

- `im` — The image to initialize the sampler with.

- `dict` — A dictionary that contains options specified as key-value pairs. See [Sampler Option Keys](../sampler-option-keys.md).

## See Also

### Initializing a Sampler

- [- initWithImage:](<init(image_).md>) — Initializes a sampler with an image object.
