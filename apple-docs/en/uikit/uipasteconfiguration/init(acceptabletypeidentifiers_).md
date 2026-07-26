---
title: 'init(acceptableTypeIdentifiers:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfiguration/init(acceptabletypeidentifiers:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration/init(acceptabletypeidentifiers:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration/init%28acceptabletypeidentifiers%3A%29.json'
content_hash: 'sha256:0928655bc72cc8fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfiguration](../uipasteconfiguration.md)

# init(acceptableTypeIdentifiers:)

<sub>Initializer</sub>

Initializes a new paste configuration with a specified array of acceptable UTIs.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(acceptableTypeIdentifiers: [String])
```

## Parameters

- `acceptableTypeIdentifiers` — An array of uniform type identifier (UTI) strings.

## Return Value

A paste configuration that is initialized with the specified UTI strings.

## Discussion

Specify the acceptable UTIs in descending order of fidelity. The UTI that provides the richest data representation should be first in the list. For instance, if the data to paste is contact information, list the vCard UTI first, followed by the plain text UTI.

## See Also

### Initializing a paste configuration

- [- init](<init().md>) — Initializes a new paste configuration.
- [- initWithTypeIdentifiersForAcceptingClass:](<init(foraccepting_)-6is3h.md>) — Initializes a new paste configuration with the UTIs declared as supported by a specified class.
- [init(forAccepting:)](<init(foraccepting_)-84r2r.md>)
