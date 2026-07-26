---
title: 'disallowKeyPathsForPropertiesProvided(by:recursive:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/predicatecodableconfiguration/disallowkeypathsforpropertiesprovided(by:recursive:)'
source_url: 'https://developer.apple.com/documentation/foundation/predicatecodableconfiguration/disallowkeypathsforpropertiesprovided(by:recursive:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/predicatecodableconfiguration/disallowkeypathsforpropertiesprovided%28by%3Arecursive%3A%29.json'
content_hash: 'sha256:f25ac142c2232a68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PredicateCodableConfiguration](../predicatecodableconfiguration.md)

# disallowKeyPathsForPropertiesProvided(by:recursive:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func disallowKeyPathsForPropertiesProvided<T>(by type: T.Type, recursive: Bool = false) where T : PredicateCodableKeyPathProviding
```

## See Also

### Disallowing types and key paths

- [disallowPartialType(_:)](<disallowpartialtype(__).md>)
- [disallowType(_:)](<disallowtype(__).md>)
