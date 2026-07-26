---
title: CFNumberType
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnumbertype
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumbertype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumbertype.json'
content_hash: 'sha256:1a3680913d491952'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberType

<sub>Enumeration</sub>

Flags used by CFNumber to indicate the data type of a value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFNumberType
```

## Overview

The type specified in the call to [CFNumberCreate](<cfnumbercreate(______).md>) is not necessarily preserved when creating a new CFNumber object. A CFNumber object uses whatever internal storage type the creation function deems appropriate. Use the [CFNumberGetType](<cfnumbergettype(__).md>) function to find out what type the CFNumber object used to store your value.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFNumberSInt8Type](cfnumbertype/sint8type.md) — Eight-bit, signed integer. The `SInt8` data type is defined in `MacTypes.h`.
- [kCFNumberSInt16Type](cfnumbertype/sint16type.md) — Sixteen-bit, signed integer. The `SInt16` data type is defined in `MacTypes.h`.
- [kCFNumberSInt32Type](cfnumbertype/sint32type.md) — Thirty-two-bit, signed integer. The `SInt32` data type is defined in `MacTypes.h`.
- [kCFNumberSInt64Type](cfnumbertype/sint64type.md) — Sixty-four-bit, signed integer. The `SInt64` data type is defined in `MacTypes.h`.
- [kCFNumberFloat32Type](cfnumbertype/float32type.md) — Thirty-two-bit real. The `Float32` data type is defined in `MacTypes.h`.
- [kCFNumberFloat64Type](cfnumbertype/float64type.md) — Sixty-four-bit real. The `Float64` data type is defined in `MacTypes.h` and conforms to the 64-bit IEEE 754 standard.
- [kCFNumberCharType](cfnumbertype/chartype.md) — Basic C `char` type.
- [kCFNumberShortType](cfnumbertype/shorttype.md) — Basic C `short` type.
- [kCFNumberIntType](cfnumbertype/inttype.md) — Basic C `int` type.
- [kCFNumberLongType](cfnumbertype/longtype.md) — Basic C `long` type.
- [kCFNumberLongLongType](cfnumbertype/longlongtype.md) — Basic C `long long` type.
- [kCFNumberFloatType](cfnumbertype/floattype.md) — Basic C `float` type.
- [kCFNumberDoubleType](cfnumbertype/doubletype.md) — Basic C `double` type.
- [kCFNumberCFIndexType](cfnumbertype/cfindextype.md) — CFIndex value.
- [kCFNumberNSIntegerType](cfnumbertype/nsintegertype.md) — `NSInteger` value.
- [kCFNumberCGFloatType](cfnumbertype/cgfloattype.md) — `CGFloat` value.
- [kCFNumberMaxType](cfnumbertype/maxtype.md) — Same as [kCFNumberCGFloatType](cfnumbertype/cgfloattype.md).

### Initializers

- [init(rawValue:)](<cfnumbertype/init(rawvalue_).md>)

## See Also

### Constants

- [Predefined Values](predefined-values.md) — CFNumber provides some predefined number values.
