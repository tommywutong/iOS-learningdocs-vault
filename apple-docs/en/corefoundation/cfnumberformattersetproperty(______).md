---
title: 'CFNumberFormatterSetProperty(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattersetproperty(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattersetproperty(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattersetproperty%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3acaa6e1d6dbe1d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterSetProperty(_:_:_:)

<sub>Function</sub>

Sets a number formatter property using a key-value pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterSetProperty(_ formatter: CFNumberFormatter!, _ key: CFNumberFormatterKey!, _ value: CFTypeRef!)
```

## Parameters

- `formatter` — The number formatter to modify.

- `key` — The name of the property of `formatter` to set. See [Number Formatter Property Keys](number-formatter-property-keys.md) for a description of possible values.

- `value` — The value of the specified key. This must be an instance of the correct `CFType` object for the corresponding key.

## See Also

### Configuring a Number Formatter

- [CFNumberFormatterSetFormat](<cfnumberformattersetformat(____).md>) — Sets the format string of a number formatter.
