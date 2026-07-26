---
title: 'CFDateCompare(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatecompare(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatecompare(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatecompare%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a8aad2784cee83c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateCompare(_:_:_:)

<sub>Function</sub>

Compares two `CFDate` objects and returns a comparison result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateCompare(_ theDate: CFDate!, _ otherDate: CFDate!, _ context: UnsafeMutableRawPointer!) -> CFComparisonResult
```

## Parameters

- `theDate` — The date to compare to `otherDate`.

- `otherDate` — The date to compare to `theDate`.

- `context` — Unused. Pass `NULL`.

## Return Value

A [CFComparisonResult](cfcomparisonresult.md) value that indicates whether `theDate` is equal to, less than, or greater than `otherDate`.

## See Also

### CFDate Miscellaneous Functions

- [CFDateCreate](<cfdatecreate(____).md>) — Creates a `CFDate` object given an absolute time.
- [CFDateGetAbsoluteTime](<cfdategetabsolutetime(__).md>) — Returns a `CFDate` object’s absolute time.
- [CFDateGetTimeIntervalSinceDate](<cfdategettimeintervalsincedate(____).md>) — Returns the number of elapsed seconds between the given `CFDate` objects.
- [CFDateGetTypeID](<cfdategettypeid().md>) — Returns the type identifier for the `CFDate` opaque type.
