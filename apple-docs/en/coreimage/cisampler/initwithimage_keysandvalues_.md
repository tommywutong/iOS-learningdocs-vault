---
title: 'initWithImage:keysAndValues:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cisampler/initwithimage:keysandvalues:'
source_url: 'https://developer.apple.com/documentation/coreimage/cisampler/initwithimage:keysandvalues:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cisampler/initwithimage%3Akeysandvalues%3A.json'
content_hash: 'sha256:8eb82166489ffa5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CISampler](../cisampler.md)

# initWithImage:keysAndValues:

<sub>Instance Method</sub>

Initializes the sampler with an image object using options specified as key-value pairs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (instancetype) initWithImage:(CIImage *) im keysAndValues:(id) key0;
```

## Parameters

- `im` — The image object to initialize the sampler with.

- `key0` — A list of key-value pairs that represent options.  Each key needs to be followed by that appropriate value. You can supply one or more key-value pairs. Use `nil` to specify the end of the key-value options. See [Sampler Option Keys](../sampler-option-keys.md).

## See Also

### Initializing a Sampler

- [- initWithImage:](<init(image_).md>) — Initializes a sampler with an image object.
- [- initWithImage:options:](<init(image_options_).md>) — Initializes the sampler with an image object using options specified in a dictionary.
