---
title: 'itemProviderVisibilityForRepresentation(withTypeIdentifier:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier:)-swift.type.method'
source_url: 'https://developer.apple.com/documentation/foundation/nsitemproviderwriting/itemprovidervisibilityforrepresentation(withtypeidentifier:)-swift.type.method'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsitemproviderwriting/itemprovidervisibilityforrepresentation%28withtypeidentifier%3A%29-swift.type.method.json'
content_hash: 'sha256:4f7052aa2a5b9b6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSItemProviderWriting](../nsitemproviderwriting.md)

# itemProviderVisibilityForRepresentation(withTypeIdentifier:)

<sub>Type Method</sub>

Asks the item provider for the default representation visibility specification for the given UTI.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional static func itemProviderVisibilityForRepresentation(withTypeIdentifier typeIdentifier: String) -> NSItemProviderRepresentationVisibility
```

## Parameters

- `typeIdentifier` — A uniform type identifier (UTI).

## Return Value

A representation visibility specification for the given UTI.

## See Also

### Getting the representation visibility specification

- [- itemProviderVisibilityForRepresentationWithTypeIdentifier:](<itemprovidervisibilityforrepresentation(withtypeidentifier_)-swift.method.md>) — Asks the item provider for the representation visibility specification for the given UTI.
