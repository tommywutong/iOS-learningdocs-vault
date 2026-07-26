---
title: CFDate
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdate
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdate.json'
content_hash: 'sha256:3043d34416ba624f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDate

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFDate
```

## Overview

`CFDate` objects store dates and times that can be compared to other dates and times. `CFDate` objects are immutable—there is no mutable counterpart for this opaque type.

`CFDate` provides functions for creating dates, comparing dates, and computing intervals. You use the [CFDateCreate](<cfdatecreate(____).md>) function to create `CFDate` objects. You use the [CFDateCompare](<cfdatecompare(______).md>) function to compare two dates, and the [CFDateGetTimeIntervalSinceDate](<cfdategettimeintervalsincedate(____).md>) function to compute a time interval. Additional functions for managing dates and times are described in [Time Utilities](time-utilities.md)

`CFDate` is “toll-free bridged” with its Cocoa Foundation counterpart, [NSDate](../foundation/nsdate.md). What this means is that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. In other words, in a method where you see an `NSDate *` parameter, you can pass in a `CFDateRef`, and in a function where you see a `CFDateRef` parameter, you can pass in an `NSDate` instance. This also applies to concrete subclasses of `NSDate`. See Interchangeable Data Types for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### CFDate Miscellaneous Functions

- [CFDateCompare](<cfdatecompare(______).md>) — Compares two `CFDate` objects and returns a comparison result.
- [CFDateCreate](<cfdatecreate(____).md>) — Creates a `CFDate` object given an absolute time.
- [CFDateGetAbsoluteTime](<cfdategetabsolutetime(__).md>) — Returns a `CFDate` object’s absolute time.
- [CFDateGetTimeIntervalSinceDate](<cfdategettimeintervalsincedate(____).md>) — Returns the number of elapsed seconds between the given `CFDate` objects.
- [CFDateGetTypeID](<cfdategettypeid().md>) — Returns the type identifier for the `CFDate` opaque type.

## See Also

### Related Documentation

- [Property List Programming Topics for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFPropertyLists/CFPropertyLists.html#//apple_ref/doc/uid/10000130i)
- [Date and Time Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDatesAndTimes/CFDatesAndTimes.html#//apple_ref/doc/uid/10000125i)

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
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)
