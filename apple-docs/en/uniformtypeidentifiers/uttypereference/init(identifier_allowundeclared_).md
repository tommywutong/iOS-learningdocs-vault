---
title: 'init(identifier:allowUndeclared:)'
framework: Uniform Type Identifiers
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/uniformtypeidentifiers/uttypereference/init(identifier:allowundeclared:)'
source_url: 'https://developer.apple.com/documentation/uniformtypeidentifiers/uttypereference/init(identifier:allowundeclared:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uniformtypeidentifiers/uttypereference/init%28identifier%3Aallowundeclared%3A%29.json'
content_hash: 'sha256:4df6cef80a5df79c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Uniform Type Identifiers](../../uniformtypeidentifiers.md) · [UTTypeReference](../uttypereference.md)

# init(identifier:allowUndeclared:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(identifier: String, allowUndeclared: Bool)
```

## Parameters

- `identifier` — The type identifier.

- `allowUndeclared` — Whether to return an object if no type with the provided identifier is known to the system.

## Return Value

A type object, or \\c nil if the input \\c identifier was not a Uniform Type Identifier.

## Discussion

Create a type given a type identifier, optionally allowing identifiers that do not have an active declaration on the current system.

When `allowUndeclared` is `YES`, this initializer can be used to obtain a type object that keeps the “identity” of the input identifier even if no type with that identifier is (currently) known to the system. In that case, the type is neither dynamic nor declared, and has no conformances or tags (or any other properties).

If a type with the input identifier is known to the system, or if the input identifier is in the dynamic namespace, it returns the same type object that \\c typeWithIdentifier: would return.

If `allowUndeclared` is `NO`, this initializer behaves identically to \\c typeWithIdentifier: given the same identifier.

One may use this, for instance, to create a concrete type object using an identifier that may have been obtained from another system, and round-trip it through a subsystem without losing the identity of the type.

If the input \\c identifier is not a valid Uniform Type Identifier, the method returns \\c nil . See https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_conc/understand_utis_conc.html#//apple_ref/doc/uid/TP40001319-CH202-SW2
