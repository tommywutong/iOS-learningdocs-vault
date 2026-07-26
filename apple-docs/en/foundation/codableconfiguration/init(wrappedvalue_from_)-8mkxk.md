---
title: 'init(wrappedValue:from:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/codableconfiguration/init(wrappedvalue:from:)-8mkxk'
source_url: 'https://developer.apple.com/documentation/foundation/codableconfiguration/init(wrappedvalue:from:)-8mkxk'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/codableconfiguration/init%28wrappedvalue%3Afrom%3A%29-8mkxk.json'
content_hash: 'sha256:6c51d6006e4dd8bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CodableConfiguration](../codableconfiguration.md)

# init(wrappedValue:from:)

<sub>Initializer</sub>

Creates a codable configuration wrapper for the given value, using given configuration provider type identified by key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(wrappedValue: T, from keyPath: KeyPath<AttributeScopes, ConfigurationProvider.Type>)
```

## Parameters

- `wrappedValue` — The underlying value to make codable, using data from the configuration provider.

- `keyPath` — A key path that identifies the type of the configuration provider, which provides additional information to encode `wrappedValue`.

## See Also

### Creating a Codable Configuration

- [init(wrappedValue:)](<init(wrappedvalue_).md>) — Creates a codable configuration wrapper for the given value.
- [init(wrappedValue:from:)](<init(wrappedvalue_from_)-46oo6.md>) — Creates a codable configuration wrapper for the given value, using the given configuration provider type.
