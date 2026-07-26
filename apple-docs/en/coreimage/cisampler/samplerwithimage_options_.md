---
title: 'samplerWithImage:options:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cisampler/samplerwithimage:options:'
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler/samplerwithimage:options:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler/samplerwithimage%3Aoptions%3A.json'
content_hash: 'sha256:162f65e2b41e427b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISampler](../cisampler.md)

# samplerWithImage:options:

<sub>Type Method</sub>

Creates and returns a sampler that references an image using options specified in a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) samplerWithImage:(CIImage *) im options:(NSDictionary *) dict;
```

## Parameters

- `im` — The image that you want the sampler to reference.

- `dict` — A dictionary that contains options specified as key-value pairs. See [Sampler Option Keys](../sampler-option-keys.md).

## Return Value

A sampler that references the image specified by the `im` argument and uses the options specified in the dictionary.

## See Also

### Creating a Sampler

- [samplerWithImage:](samplerwithimage_.md) — Creates and returns a sampler that references an image.
- [samplerWithImage:keysAndValues:](samplerwithimage_keysandvalues_.md) — Creates and returns a sampler that references an image using options specified as key-value pairs.
