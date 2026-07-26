---
title: 'CFDateFormatterCreateDateFromString(_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattercreatedatefromstring(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattercreatedatefromstring(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattercreatedatefromstring%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:99fc67dfdb134b34'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterCreateDateFromString(_:_:_:_:)

<sub>Function</sub>

Returns a date object representing a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterCreateDateFromString(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ string: CFString!, _ rangep: UnsafeMutablePointer<CFRange>!) -> CFDate!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `formatter` — The date formatter object to use to parse `string`.

- `string` — The string that contains the date.

- `rangep` — A reference to the range within the string specifying the substring to be parsed. If `NULL`, the whole string is parsed. Upon return, contains the range that defines the extent of the parse (may be less than the given range).

## Return Value

A new date that represents `string`, or `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Parsing Strings

- [CFDateFormatterGetAbsoluteTimeFromString](<cfdateformattergetabsolutetimefromstring(________).md>) — Returns an absolute time object representing a given string.
