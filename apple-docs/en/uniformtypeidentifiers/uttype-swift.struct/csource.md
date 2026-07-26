---
title: cSource
framework: Uniform Type Identifiers
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uniformtypeidentifiers/uttype-swift.struct/csource
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/csource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttype-swift.struct/csource.json'
content_hash: 'sha256:7d1be3f818394f50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTType](../uttype-swift.struct.md)

# cSource

<sub>Type Property</sub>

A type that represents a C source code file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var cSource: UTType { get }
```

## Discussion

The identifier for this type is `public.c-source`.

This type conforms to [UTTypeSourceCode](../uttypesourcecode.md).

## See Also

### Compiled programming language sources

- [assemblyLanguageSource](assemblylanguagesource.md) — A type that represents assembly language source code.
- [cHeader](cheader.md) — A type that represents a C header file.
- [cPlusPlusHeader](cplusplusheader.md) — A type that represents a C++ header file.
- [cPlusPlusSource](cplusplussource.md) — A type that represents a C++ source code file.
- [objectiveCPlusPlusSource](objectivecplusplussource.md) — A type that represents an Objective-C++ source code file.
- [objectiveCSource](objectivecsource.md) — A type that represents an Objective-C source code file.
- [swiftSource](swiftsource.md) — A type that represents a Swift source code file.
