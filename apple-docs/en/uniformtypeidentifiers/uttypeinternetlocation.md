---
title: UTTypeInternetLocation
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypeinternetlocation
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypeinternetlocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypeinternetlocation.json'
content_hash: 'sha256:a069c1cd183da84f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeInternetLocation

<sub>Global Variable</sub>

A base type that represents an Apple internet location file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeInternetLocation;
```

## Discussion

The identifier for this type is `com.apple.internet-location`.

This type conforms to [UTTypeData](uttypedata.md) and a base type identified by `public.stored-url`.

## See Also

### Internet-specific

- [UTTypeHTML](uttypehtml.md) — A type that represents any version of HTML.
- [UTTypeWebArchive](uttypewebarchive.md) — A type that represents WebKit web archive data.
- [UTTypeInternetShortcut](uttypeinternetshortcut.md) — A type that represents a Microsoft internet shortcut file.
