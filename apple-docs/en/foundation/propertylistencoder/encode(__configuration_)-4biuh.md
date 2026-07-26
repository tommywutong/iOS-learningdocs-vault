---
title: 'encode(_:configuration:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/propertylistencoder/encode(_:configuration:)-4biuh'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistencoder/encode(_:configuration:)-4biuh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistencoder/encode%28_%3Aconfiguration%3A%29-4biuh.json'
content_hash: 'sha256:99228b272f148fbc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListEncoder](../propertylistencoder.md)

# encode(_:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<T, C>(_ value: T, configuration: C.Type) throws -> Data where T : EncodableWithConfiguration, C : EncodingConfigurationProviding, T.EncodingConfiguration == C.EncodingConfiguration
```

## See Also

### Encoding

- [init()](<init().md>) — Creates a new, reusable property list encoder with the default formatting settings.
- [encode(_:)](<encode(__).md>) — Returns a property list that represents an encoded version of the value you supply.
- [encode(_:configuration:)](<encode(__configuration_)-5ee8q.md>)
