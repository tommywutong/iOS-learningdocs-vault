---
title: package
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/package
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/package'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/package.json'
content_hash: 'sha256:561f5c73dfe0c463'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# package

<sub>Type Property</sub>

A base type that represents a packaged directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var package: UTType { get }
```

## Discussion

Bundles differ from packages in that a bundle has an internal file hierarchy that [CFBundle](../../corefoundation/cfbundle.md) can read, while packages display to the user as if they were regular files. A single file system object can be a package and a bundle.

The identifier for this type is `com.apple.package`.

This type conforms to [UTTypeDirectory](../uttypedirectory.md).

## See Also

### Apple system base types

- [item](item.md) — A generic base type for most objects, such as files or directories.
- [content](content.md) — A base type that represents anything containing user-viewable content.
- [compositeContent](compositecontent.md) — A base type that represents a content format supporting mixed embedded content.
- [data](data.md) — A base type that represents any sort of byte stream, including files and in-memory data.
- [resolvable](resolvable.md) — A base type that represents a resolvable reference, including symbolic links and aliases.
- [bundle](bundle.md) — A base type that represents a directory that conforms to one of the bundle layouts.
- [pluginBundle](pluginbundle.md) — A base type that represents a bundle-based plug-in.
- [application](application.md) — A base type that represents a macOS, iOS, iPadOS, watchOS, and tvOS app.
- [sourceCode](sourcecode.md) — A base type that represents source code of any programming language.
- [bookmark](bookmark.md) — A base type that represents bookmark data.
- [log](log.md) — A base type that represents console log data.
