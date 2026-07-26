---
title: 'CFDateFormatterCreateStringWithAbsoluteTime(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdateformattercreatestringwithabsolutetime(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformattercreatestringwithabsolutetime(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformattercreatestringwithabsolutetime%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:f2bfac21cf9ab990'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatterCreateStringWithAbsoluteTime(_:_:_:)

<sub>Function</sub>

Returns a string representation of the given absolute time using the specified date formatter.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateFormatterCreateStringWithAbsoluteTime(_ allocator: CFAllocator!, _ formatter: CFDateFormatter!, _ at: CFAbsoluteTime) -> CFString!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `formatter` — The date formatter object that specifies the format of the returned string.

- `at` — The absolute time for which to generate a string representation.

## Return Value

A new string that represents `at` in the specified format. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Creating Strings From Data

- [CFDateFormatterCreateStringWithDate](<cfdateformattercreatestringwithdate(______).md>) — Returns a string representation of the given date using the specified date formatter.
- [CFDateFormatterCreateDateFormatFromTemplate](<cfdateformattercreatedateformatfromtemplate(________).md>) — Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.
