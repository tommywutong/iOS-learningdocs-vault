---
title: 'CFDateFormatterGetAbsoluteTimeFromString(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattergetabsolutetimefromstring(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattergetabsolutetimefromstring(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattergetabsolutetimefromstring%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a5994f5bb3705205'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterGetAbsoluteTimeFromString(_:_:_:_:)

<sub>Function</sub>

Returns an absolute time object representing a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterGetAbsoluteTimeFromString(_ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!, _ atp: UnsafeMutablePointer<CFAbsoluteTime>!) -> Bool
```

## Parameters

- `formatter` — The date formatter object to use to parse `string`.

- `string` — The string that contains the time to be parsed.

- `rangep` — Reference to the range within the string specifying the substring to be parsed. If `NULL`, the whole string is parsed. On return, the range that defines the extent of the parse (may be less than the given range).

- `atp` — An absolute time value, returned by reference, that represents `string`. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Return Value

`true` if the string was parsed successfully, otherwise `false`.

## See Also

### Parsing Strings

- [CFDateFormatterCreateDateFromString](<cfdateformattercreatedatefromstring(________).md>) — Returns a date object representing a given string.
