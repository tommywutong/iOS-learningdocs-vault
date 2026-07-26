---
title: 'CFDateCreate(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfdatecreate(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatecreate(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatecreate%28_%3A_%3A%29.json'
content_hash: 'sha256:da522560610b579a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateCreate(_:_:)

<sub>Function</sub>

Creates a `CFDate` object given an absolute time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateCreate(_ allocator: CFAllocator!, _ at: CFAbsoluteTime) -> CFDate!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `at` — The absolute time to convert to a CFDate object.

## Return Value

A date object that represents the absolute time `at`.  The caller is responsible for releasing the `CFDate` object using [CFRelease](cfrelease.md).

## Discussion

`CFDate` objects must always be created using absolute time. Time intervals are not supported.

## See Also

### CFDate Miscellaneous Functions

- [CFDateCompare](<cfdatecompare(______).md>) — Compares two `CFDate` objects and returns a comparison result.
- [CFDateGetAbsoluteTime](<cfdategetabsolutetime(__).md>) — Returns a `CFDate` object’s absolute time.
- [CFDateGetTimeIntervalSinceDate](<cfdategettimeintervalsincedate(____).md>) — Returns the number of elapsed seconds between the given `CFDate` objects.
- [CFDateGetTypeID](<cfdategettypeid().md>) — Returns the type identifier for the `CFDate` opaque type.
