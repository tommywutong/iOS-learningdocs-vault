---
title: CFNull
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnull
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnull'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnull.json'
content_hash: 'sha256:f1bcb9056783088c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNull

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFNull
```

## Overview

The CFNull opaque type defines a unique object used to represent null values in collection objects (which don’t allow `NULL` values). CFNull objects are neither created nor destroyed. Instead, a single CFNull constant object—[kCFNull](kcfnull.md)—is defined and is used wherever a null value is needed.

The CFNull opaque type is available in macOS 10.2 and later.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### CFNull Miscellaneous Functions

- [CFNullGetTypeID](<cfnullgettypeid().md>) — Returns the type identifier for the CFNull opaque type.

### Constants

- [Predefined Value](predefined-value.md) — Predefined CFNull object.

## See Also

### Related Documentation

- [Collections Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFCollections/CFCollections.html#//apple_ref/doc/uid/10000124i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
