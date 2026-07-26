---
title: 'allowKeyPathsForPropertiesProvided(by:recursive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicatecodableconfiguration/allowkeypathsforpropertiesprovided(by:recursive:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicatecodableconfiguration/allowkeypathsforpropertiesprovided(by:recursive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicatecodableconfiguration/allowkeypathsforpropertiesprovided%28by%3Arecursive%3A%29.json'
content_hash: 'sha256:7c6d8b6bcb1cc763'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateCodableConfiguration](../predicatecodableconfiguration.md)

# allowKeyPathsForPropertiesProvided(by:recursive:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func allowKeyPathsForPropertiesProvided<T>(by type: T.Type, recursive: Bool = false) where T : PredicateCodableKeyPathProviding
```

## See Also

### Allowing types and key paths

- [allow(_:)](<allow(__).md>)
- [allowPartialType(_:identifier:)](<allowpartialtype(__identifier_).md>)
- [allowType(_:identifier:)](<allowtype(__identifier_).md>)
