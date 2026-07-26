---
title: UTTypeHEIF
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeheif
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeheif'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeheif.json'
content_hash: 'sha256:038d0282488ab1ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeHEIF

<sub>Global Variable</sub>

A type that represents High Efficiency Image File Format images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeHEIF;
```

## Discussion

The identifier for this type is `public.heif`.

This type conforms to a base type identified by `public.heif-standard`, which in turn conforms to [UTTypeImage](uttypeimage.md).

## See Also

### Apple image formats

- [UTTypeHEIC](uttypeheic.md) — A type that represents High Efficiency Image Coding images.
- [UTTypeLivePhoto](uttypelivephoto.md) — A type that represents Live Photos.
