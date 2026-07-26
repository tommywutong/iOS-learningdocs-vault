---
title: 'contextWithOptions:'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cicontext/contextwithoptions:'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/contextwithoptions:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/contextwithoptions%3A.json'
content_hash: 'sha256:5ea0ca2d40bc528d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# contextWithOptions:

<sub>Type Method</sub>

Initializes a context without a specific rendering destination, using the specified options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
+ (CIContext *) contextWithOptions:(NSDictionary<NSString *,id> *) options;
```

## Parameters

- `options` — A dictionary containing options for the context. For applicable keys and values, see [CIContextOption](../cicontextoption.md).

## Return Value

An initialized Core Image context.

## Discussion

If you create a context without specifying a rendering destination, Core Image automatically chooses and internally manages a rendering destination based on the current device’s capabilities and your settings in the `options` dictionary. You cannot use a context without an explicit destination for the methods listed in Drawing Images. Instead, use the methods listed in Rendering Images.

The `options` dictionary defines behaviors for the context, such as color space and rendering quality. For example, to create a CPU-based context, use the  [kCIContextUseSoftwareRenderer](../cicontextoption/usesoftwarerenderer.md) key.

## See Also

### Creating a Context Without Specifying a Destination

- [context](context.md) — Creates a context without a specific rendering destination, using default options.
- [- init](<init().md>) — Initializes a context without a specific rendering destination, using default options.
