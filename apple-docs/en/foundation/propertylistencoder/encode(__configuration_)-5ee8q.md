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
doc_path: '/documentation/foundation/propertylistencoder/encode(_:configuration:)-5ee8q'
source_url: 'https://developer.apple.com/documentation/foundation/propertylistencoder/encode(_:configuration:)-5ee8q'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/propertylistencoder/encode%28_%3Aconfiguration%3A%29-5ee8q.json'
content_hash: 'sha256:07bf545a73b1d4fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PropertyListEncoder](../propertylistencoder.md)

# encode(_:configuration:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func encode<T>(_ value: T, configuration: T.EncodingConfiguration) throws -> Data where T : EncodableWithConfiguration
```

## See Also

### Encoding

- [init()](<init().md>) — Creates a new, reusable property list encoder with the default formatting settings.
- [encode(_:)](<encode(__).md>) — Returns a property list that represents an encoded version of the value you supply.
- [encode(_:configuration:)](<encode(__configuration_)-4biuh.md>)
