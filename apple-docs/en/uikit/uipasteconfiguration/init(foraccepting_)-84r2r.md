---
title: 'init(forAccepting:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipasteconfiguration/init(foraccepting:)-84r2r'
source_url: 'https://developer.apple.com/documentation/uikit/uipasteconfiguration/init(foraccepting:)-84r2r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteconfiguration/init%28foraccepting%3A%29-84r2r.json'
content_hash: 'sha256:e97d710ea7403142'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteConfiguration](../uipasteconfiguration.md)

# init(forAccepting:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init<T>(forAccepting _: T.Type) where T : _ObjectiveCBridgeable, T._ObjectiveCType : NSItemProviderReading
```

## See Also

### Initializing a paste configuration

- [- init](<init().md>) — Initializes a new paste configuration.
- [- initWithAcceptableTypeIdentifiers:](<init(acceptabletypeidentifiers_).md>) — Initializes a new paste configuration with a specified array of acceptable UTIs.
- [- initWithTypeIdentifiersForAcceptingClass:](<init(foraccepting_)-6is3h.md>) — Initializes a new paste configuration with the UTIs declared as supported by a specified class.
