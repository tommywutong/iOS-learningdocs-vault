---
title: 'CFStringGetIntValue(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetintvalue(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetintvalue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetintvalue%28_%3A%29.json'
content_hash: 'sha256:f441f065ebc8669b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetIntValue(_:)

<sub>Function</sub>

Returns the integer value represented by a string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetIntValue(_ str: CFString!) -> Int32
```

## Parameters

- `str` — A string that represents a signed integer value. The only allowed characters are the ASCII digit characters (ASCII `0x30` - `0x39`), the plus sign (ASCII `0x2B`), the minus sign (ASCII `0x2D`), and the period character (ASCII `0x2E`).

## Return Value

The signed integer value represented by `str`. The result is `0` if there is a scanning error (if the string contains disallowed characters or does not represent an integer value) or `INT_MAX` or `INT_MIN` if there is an overflow error.

## Discussion

Consider the following example:

```objc
SInt32 val = CFStringGetIntValue(CFSTR("-123"));
```

The variable `val` in this example would contain the value `-123` after the function is called.

## See Also

### Getting Numeric Values

- [CFStringGetDoubleValue](<cfstringgetdoublevalue(__).md>) — Returns the primary `double` value represented by a string.
