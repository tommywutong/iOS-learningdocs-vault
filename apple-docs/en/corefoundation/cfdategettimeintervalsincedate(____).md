---
title: 'CFDateGetTimeIntervalSinceDate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdategettimeintervalsincedate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdategettimeintervalsincedate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdategettimeintervalsincedate%28_%3A_%3A%29.json'
content_hash: 'sha256:d4eb8ca354eba9b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateGetTimeIntervalSinceDate(_:_:)

<sub>Function</sub>

Returns the number of elapsed seconds between the given `CFDate` objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateGetTimeIntervalSinceDate(_ theDate: CFDate!, _ otherDate: CFDate!) -> CFTimeInterval
```

## Parameters

- `theDate` — The date to compare to `otherDate`.

- `otherDate` — The date to compare to `theDate`.

## Return Value

The number of elapsed seconds between `theDate` and `otherDate`. The result is positive if `theDate` is later than `otherDate`.

## See Also

### CFDate Miscellaneous Functions

- [CFDateCompare](<cfdatecompare(______).md>) — Compares two `CFDate` objects and returns a comparison result.
- [CFDateCreate](<cfdatecreate(____).md>) — Creates a `CFDate` object given an absolute time.
- [CFDateGetAbsoluteTime](<cfdategetabsolutetime(__).md>) — Returns a `CFDate` object’s absolute time.
- [CFDateGetTypeID](<cfdategettypeid().md>) — Returns the type identifier for the `CFDate` opaque type.
