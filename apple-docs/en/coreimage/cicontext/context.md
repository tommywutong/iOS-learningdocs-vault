---
title: context
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cicontext/context
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/context.json'
content_hash: 'sha256:15dac560f1bf3f42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# context

<sub>Type Method</sub>

Creates a context without a specific rendering destination, using default options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIContext *) context;
```

## Return Value

A new Core Image context.

## Discussion

If you create a context without specifying a rendering destination, Core Image automatically chooses and internally manages a rendering destination based on the current device’s capabilities. You cannot use a context without an explicit destination for the methods listed in Drawing Images. Instead, use the methods listed in Rendering Images.

To specify additional options for the context, use the [contextWithOptions:](contextwithoptions_.md) method instead.

## See Also

### Related Documentation

- [Image Unit Tutorial](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)

### Creating a Context Without Specifying a Destination

- [- init](<init().md>) — Initializes a context without a specific rendering destination, using default options.
- [contextWithOptions:](contextwithoptions_.md) — Initializes a context without a specific rendering destination, using the specified options.
