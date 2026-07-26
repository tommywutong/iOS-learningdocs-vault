---
title: UTTypeData
framework: Uniform Type Identifiers
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttypedata
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypedata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypedata.json'
content_hash: 'sha256:cd19be3796689371'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Uniform Type Identifiers](../uniformtypeidentifiers.md)

# UTTypeData

<sub>Global Variable</sub>

A base type that represents any sort of byte stream, including files and in-memory data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern UTType * const UTTypeData;
```

## Discussion

The identifier for this type is `public.data`.

This type conforms to [UTTypeItem](uttypeitem.md).

## See Also

### Apple system base types

- [UTTypeItem](uttypeitem.md) — A generic base type for most objects, such as files or directories.
- [UTTypeContent](uttypecontent.md) — A base type that represents anything containing user-viewable content.
- [UTTypeCompositeContent](uttypecompositecontent.md) — A base type that represents a content format supporting mixed embedded content.
- [UTTypeResolvable](uttyperesolvable.md) — A base type that represents a resolvable reference, including symbolic links and aliases.
- [UTTypePackage](uttypepackage.md) — A base type that represents a packaged directory.
- [UTTypeBundle](uttypebundle.md) — A base type that represents a directory that conforms to one of the bundle layouts.
- [UTTypePluginBundle](uttypepluginbundle.md) — A base type that represents a bundle-based plug-in.
- [UTTypeApplication](uttypeapplication.md) — A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.
- [UTTypeSourceCode](uttypesourcecode.md) — A base type that represents source code of any programming language.
- [UTTypeBookmark](uttypebookmark.md) — A base type that represents bookmark data.
- [UTTypeLog](uttypelog.md) — A base type that represents console log data.
