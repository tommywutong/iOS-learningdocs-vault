---
title: 'CFNumberFormatterSetFormat(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumberformattersetformat(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformattersetformat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformattersetformat%28_%3A_%3A%29.json'
content_hash: 'sha256:69f3d21225efcb63'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatterSetFormat(_:_:)

<sub>Function</sub>

Sets the format string of a number formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberFormatterSetFormat(_ formatter: CFNumberFormatter!, _ formatString: CFString!)
```

## Parameters

- `formatter` — The number formatter to modify.

- `formatString` — The format string to be used by `formatter`. See [Creating and Using CFNumberFormatter Objects](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/dfCreatingCFNumberFormatters.html#//apple_ref/doc/uid/TP40002342) for more information.

## Discussion

The format string may override other properties previously set using other functions. If this function is not called, the default value of the format string is derived from the number formatter’s style.

## See Also

### Configuring a Number Formatter

- [CFNumberFormatterSetProperty](<cfnumberformattersetproperty(______).md>) — Sets a number formatter property using a key-value pair.
