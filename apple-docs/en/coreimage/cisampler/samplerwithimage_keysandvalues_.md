---
title: 'samplerWithImage:keysAndValues:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cisampler/samplerwithimage:keysandvalues:'
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler/samplerwithimage:keysandvalues:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler/samplerwithimage%3Akeysandvalues%3A.json'
content_hash: 'sha256:e019193294bfdef7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISampler](../cisampler.md)

# samplerWithImage:keysAndValues:

<sub>Type Method</sub>

Creates and returns a sampler that references an image using options specified as key-value pairs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (instancetype) samplerWithImage:(CIImage *) im keysAndValues:(id) key0;
```

## Parameters

- `im` — The image that you want the sampler to reference.

- `key0` — A list of key-value pairs that represent options.  Each key needs to be followed by that appropriate value. You can supply one or more key-value pairs. Use `nil` to specify the end of the key-value options. See [Sampler Option Keys](../sampler-option-keys.md).

## Return Value

A sampler that references the image specified by the `im` argument and uses the specified options.

## See Also

### Creating a Sampler

- [samplerWithImage:](samplerwithimage_.md) — Creates and returns a sampler that references an image.
- [samplerWithImage:options:](samplerwithimage_options_.md) — Creates and returns a sampler that references an image using options specified in a dictionary.
