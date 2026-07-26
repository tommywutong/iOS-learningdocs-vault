---
title: 'CFDateGetAbsoluteTime(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdategetabsolutetime(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdategetabsolutetime(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdategetabsolutetime%28_%3A%29.json'
content_hash: 'sha256:04b909c5fc43e254'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateGetAbsoluteTime(_:)

<sub>Function</sub>

Returns a `CFDate` object’s absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateGetAbsoluteTime(_ theDate: CFDate!) -> CFAbsoluteTime
```

## Parameters

- `theDate` — The date to examine.

## Return Value

The absolute time of `theDate`.

## Discussion

Absolute time is measured in seconds relative to the absolute reference date of Jan 1 2001 00:00:00 GMT. A positive value represents a date after the reference date, a negative value represents a date before it. For example, the absolute time -32940326 is equivalent to December 16th, 1999 at 17:54:34.

## See Also

### CFDate Miscellaneous Functions

- [CFDateCompare](<cfdatecompare(______).md>) — Compares two `CFDate` objects and returns a comparison result.
- [CFDateCreate](<cfdatecreate(____).md>) — Creates a `CFDate` object given an absolute time.
- [CFDateGetTimeIntervalSinceDate](<cfdategettimeintervalsincedate(____).md>) — Returns the number of elapsed seconds between the given `CFDate` objects.
- [CFDateGetTypeID](<cfdategettypeid().md>) — Returns the type identifier for the `CFDate` opaque type.
