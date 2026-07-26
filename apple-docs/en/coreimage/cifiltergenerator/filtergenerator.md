---
title: filterGenerator
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [macOS 10.5+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cifiltergenerator/filtergenerator
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/filtergenerator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/filtergenerator.json'
content_hash: 'sha256:5b4de60045e5eceb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# filterGenerator

<sub>Type Method</sub>

Creates and returns an empty filter generator object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIFilterGenerator *) filterGenerator;
```

## Return Value

A [CIFilterGenerator](../cifiltergenerator.md) object.

## Discussion

You use the returned object to connect two or more [CIFilter](../cifilter-swift.class.md) objects and input images. It is also valid to have only one [CIFilter](../cifilter-swift.class.md) object in a filter generator.

## See Also

### Related Documentation

- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
- [Core Image Filter Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CoreImageFilterReference/index.html#//apple_ref/doc/uid/TP40004346)

### Creating Filter Generator Objects

- [filterGeneratorWithContentsOfURL:](filtergeneratorwithcontentsofurl_.md) — Creates and returns a filter generator object and initializes it with the contents of a filter generator file.
