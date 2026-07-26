---
title: 'columnTerminators(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstexttab/columnterminators(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstexttab/columnterminators(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstexttab/columnterminators%28for%3A%29.json'
content_hash: 'sha256:cb4782a9ac5b483a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextTab](../nstexttab.md)

# columnTerminators(for:)

<sub>Type Method</sub>

Returns the column terminators for the specified locale.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
class func columnTerminators(for aLocale: Locale?) -> CharacterSet
```

## Parameters

- `aLocale` — The locale to use when determining the terminators. Specify `nil` to use the system’s current locale. You can get the user’s locale using the [current](../../foundation/nslocale/current.md) method of [NSLocale](../../foundation/nslocale.md).

## Return Value

The characters for the column terminators.

## Discussion

The returned value can be used as the value for [NSTabColumnTerminatorsAttributeName](optionkey/columnterminators.md) to make a decimal tab stop.

## See Also

### Getting text tab information

- [alignment](alignment.md) — The text alignment of the text tab.
- [options](options.md) — The dictionary of attributes for the text tab.
