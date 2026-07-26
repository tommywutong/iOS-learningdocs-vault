---
title: init()
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteconfiguration/init()
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration/init%28%29.json'
content_hash: 'sha256:ebe7628ccca99265'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfiguration](../uipasteconfiguration.md)

# init()

<sub>Initializer</sub>

Initializes a new paste configuration.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init()
```

## Return Value

A paste configuration that has no acceptable uniform type identifiers (UTIs).

## Discussion

Use this initializer to create a paste configuration that has an empty [acceptableTypeIdentifiers](acceptabletypeidentifiers.md) array. After you create the paste configuration, you can use its [- addAcceptableTypeIdentifiers:](<addacceptabletypeidentifiers(__).md>) method or [- addTypeIdentifiersForAcceptingClass:](<addtypeidentifiers(foraccepting_)-4fvd6.md>) method to add acceptable UTIs to the array.

## See Also

### Initializing a paste configuration

- [- initWithAcceptableTypeIdentifiers:](<init(acceptabletypeidentifiers_).md>) — Initializes a new paste configuration with a specified array of acceptable UTIs.
- [- initWithTypeIdentifiersForAcceptingClass:](<init(foraccepting_)-6is3h.md>) — Initializes a new paste configuration with the UTIs declared as supported by a specified class.
- [init(forAccepting:)](<init(foraccepting_)-84r2r.md>)
