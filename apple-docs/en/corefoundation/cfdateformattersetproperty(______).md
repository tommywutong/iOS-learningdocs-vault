---
title: 'CFDateFormatterSetProperty(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattersetproperty(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattersetproperty(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattersetproperty%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:cfa422cf76034fd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterSetProperty(_:_:_:)

<sub>Function</sub>

Sets a date formatter property using a key-value pair.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterSetProperty(_ formatter: CFDateFormatter!, _ key: CFString!, _ value: CFTypeRef!)
```

## Parameters

- `formatter` — The date formatter to modify.

- `key` — The name of the property to set. See [Date Formatter Property Keys](date-formatter-property-keys.md) for a description of possible values for this parameter.

- `value` — The value for `key`. This should be a CFType object corresponding to the specified key.

## See Also

### Configuring a Date Formatter

- [CFDateFormatterSetFormat](<cfdateformattersetformat(____).md>) — Sets the format string of the given date formatter to the specified value.
