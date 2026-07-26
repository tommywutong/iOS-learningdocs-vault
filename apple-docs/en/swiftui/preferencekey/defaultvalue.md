---
title: defaultValue
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/preferencekey/defaultvalue
source_url: 'https://developer.apple.com/documentation/swiftui/preferencekey/defaultvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/preferencekey/defaultvalue.json'
content_hash: 'sha256:e0af75d969e96cfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PreferenceKey](../preferencekey.md)

# defaultValue

<sub>Type Property</sub>

The default value of the preference.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var defaultValue: Self.Value { get }
```

## Discussion

Views that have no explicit value for the key produce this default value. Combining child views may remove an implicit value produced by using the default. This means that `reduce(value: &x, nextValue: {defaultValue})` shouldn’t change the meaning of `x`.

## Default Implementations

### PreferenceKey Implementations

- [defaultValue](defaultvalue-23qgw.md) — Let nil-expressible values default-initialize to nil.

## See Also

### Getting the default value

- [Value](value.md) — The type of value produced by this preference.
