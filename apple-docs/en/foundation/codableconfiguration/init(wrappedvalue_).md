---
title: 'init(wrappedValue:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/codableconfiguration/init(wrappedvalue:)'
source_url: 'https://developer.apple.com/documentation/foundation/codableconfiguration/init(wrappedvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/codableconfiguration/init%28wrappedvalue%3A%29.json'
content_hash: 'sha256:735fc7577977dcd9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CodableConfiguration](../codableconfiguration.md)

# init(wrappedValue:)

<sub>Initializer</sub>

Creates a codable configuration wrapper for the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(wrappedValue: T)
```

## Parameters

- `wrappedValue` — The underlying value to make codable.

## Discussion

This initializer doesn’t take a `ConfigurationProvider.Type` parameter. As a result, it won’t compile unless the compiler can imply the provider type through other means, such as a generic expression like `@CodableConfiguration<AttributedString, FoundationAttributes>`.

For clarity, use this type’s other initializers, which take the configuration provider type as an explicit parameter.

## See Also

### Creating a Codable Configuration

- [init(wrappedValue:from:)](<init(wrappedvalue_from_)-46oo6.md>) — Creates a codable configuration wrapper for the given value, using the given configuration provider type.
- [init(wrappedValue:from:)](<init(wrappedvalue_from_)-8mkxk.md>) — Creates a codable configuration wrapper for the given value, using given configuration provider type identified by key path.
