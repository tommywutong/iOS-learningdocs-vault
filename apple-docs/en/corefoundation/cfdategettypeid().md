---
title: CFDateGetTypeID()
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdategettypeid()
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdategettypeid()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdategettypeid%28%29.json'
content_hash: 'sha256:36b7086cf7c281a3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateGetTypeID()

<sub>Function</sub>

Returns the type identifier for the `CFDate` opaque type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFDateGetTypeID() -> CFTypeID
```

## Return Value

The type identifier for the CFDate opaque type.

## See Also

### CFDate Miscellaneous Functions

- [CFDateCompare](<cfdatecompare(______).md>) — Compares two `CFDate` objects and returns a comparison result.
- [CFDateCreate](<cfdatecreate(____).md>) — Creates a `CFDate` object given an absolute time.
- [CFDateGetAbsoluteTime](<cfdategetabsolutetime(__).md>) — Returns a `CFDate` object’s absolute time.
- [CFDateGetTimeIntervalSinceDate](<cfdategettimeintervalsincedate(____).md>) — Returns the number of elapsed seconds between the given `CFDate` objects.
