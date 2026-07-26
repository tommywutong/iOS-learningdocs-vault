---
title: 'CFStringGetDoubleValue(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetdoublevalue(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetdoublevalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetdoublevalue%28_%3A%29.json'
content_hash: 'sha256:c4b3066f4d61cc81'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetDoubleValue(_:)

<sub>Function</sub>

Returns the primary `double` value represented by a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetDoubleValue(_ str: CFString!) -> Double
```

## Parameters

- `str` — A string that represents a double value. The only allowed characters are the ASCII digit characters (ASCII `0x30` - `0x39`), the plus sign (ASCII `0x2B`), the minus sign (ASCII `0x2D`), and the period character (ASCII `0x2E`).

## Return Value

The `double` value represented by `str`, or `0.0` if there is a scanning error (if the string contains disallowed characters or does not represent a double value).

## Discussion

Consider the following example:

```objc
double val = CFStringGetDoubleValue(CFSTR("0.123"));
```

The variable `val` in this example would contain the value `0.123` after the function is called.

## See Also

### Getting Numeric Values

- [CFStringGetIntValue](<cfstringgetintvalue(__).md>) — Returns the integer value represented by a string.
