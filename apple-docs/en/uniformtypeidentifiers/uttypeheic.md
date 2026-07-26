---
title: UTTypeHEIC
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeheic
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeheic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeheic.json'
content_hash: 'sha256:55384028c7e00a6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeHEIC

<sub>Global Variable</sub>

A type that represents High Efficiency Image Coding images.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeHEIC;
```

## Discussion

The identifier for this type is `public.heic`.

This type conforms to a base type identified by `public.heif-standard`, which in turn conforms to [UTTypeImage](uttypeimage.md).

## See Also

### Apple image formats

- [UTTypeHEIF](uttypeheif.md) — A type that represents High Efficiency Image File Format images.
- [UTTypeLivePhoto](uttypelivephoto.md) — A type that represents Live Photos.
