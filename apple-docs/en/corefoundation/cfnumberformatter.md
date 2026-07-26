---
title: CFNumberFormatter
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfnumberformatter
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumberformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumberformatter.json'
content_hash: 'sha256:f1ecb420036f2172'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberFormatter

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFNumberFormatter
```

## Overview

CFNumberFormatter objects format the textual representations of CFNumber objects, and convert textual representations of numbers into CFNumber objects. The representation encompasses integers, floats, and doubles; floats and doubles can be formatted to a specified decimal position. You specify how strings are formatted and parsed by setting a format string and other properties of a CFNumberFormatter object.

The format of the format string is defined by Unicode Technical Standard #35; the version of the standard used varies with release of the operating system, and is described in [Introduction to Data Formatting Programming Guide For Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029).

> [!important] Important
> `CFNumberFormatter` is not thread-safe.  Do not use a single instance from multiple threads.

Unlike some other Core Foundation opaque types with names similar to a corresponding Cocoa Foundation class (such as CFString and `NSString`), CFNumberFormatter objects cannot be cast (“toll-free bridged”) to `NSNumberFormatter` objects.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Number Formatter

- [CFNumberFormatterCreate](<cfnumberformattercreate(______).md>) — Creates a new CFNumberFormatter object, localized to the given locale, which will format numbers to the given style.

### Configuring a Number Formatter

- [CFNumberFormatterSetFormat](<cfnumberformattersetformat(____).md>) — Sets the format string of a number formatter.
- [CFNumberFormatterSetProperty](<cfnumberformattersetproperty(______).md>) — Sets a number formatter property using a key-value pair.

### Formatting Values

- [CFNumberFormatterCreateNumberFromString](<cfnumberformattercreatenumberfromstring(__________).md>) — Returns a number object representing a given string.
- [CFNumberFormatterCreateStringWithNumber](<cfnumberformattercreatestringwithnumber(______).md>) — Returns a string representation of the given number using the specified number formatter.
- [CFNumberFormatterCreateStringWithValue](<cfnumberformattercreatestringwithvalue(________).md>) — Returns a string representation of the given number or value using the specified number formatter.
- [CFNumberFormatterGetDecimalInfoForCurrencyCode](<cfnumberformattergetdecimalinfoforcurrencycode(______).md>) — Returns the number of fraction digits that should be displayed, and the rounding increment, for a given currency.
- [CFNumberFormatterGetValueFromString](<cfnumberformattergetvaluefromstring(__________).md>) — Returns a number or value representing a given string.

### Examining a Number Formatter

- [CFNumberFormatterCopyProperty](<cfnumberformattercopyproperty(____).md>) — Returns a copy of a number formatter’s value for a given key.
- [CFNumberFormatterGetFormat](<cfnumberformattergetformat(__).md>) — Returns a format string for the given number formatter object.
- [CFNumberFormatterGetLocale](<cfnumberformattergetlocale(__).md>) — Returns the locale object used to create the given number formatter object.
- [CFNumberFormatterGetStyle](<cfnumberformattergetstyle(__).md>) — Returns the number style used to create the given number formatter object.

### Getting the CFNumberFormatter Type ID

- [CFNumberFormatterGetTypeID](<cfnumberformattergettypeid().md>) — Returns the type identifier for the `CFNumberFormatter` opaque type.

### Data Types

- [CFNumberFormatterStyle](cfnumberformatterstyle.md) — Type for constants specifying a formatter style.
- [CFNumberFormatterOptionFlags](cfnumberformatteroptionflags.md) — Type for constants specifying how numbers should be parsed.
- [CFNumberFormatterPadPosition](cfnumberformatterpadposition.md) — Type for constants specifying how numbers should be padded.

### Constants

- [Number Formatter Styles](number-formatter-styles.md) — Predefined number format styles.
- [Number Formatter Property Keys](number-formatter-property-keys.md) — The keys used in key-value pairs to specify the value of number formatter properties.
- [Number Format Options](number_format_options.md) — These constants are used to specify how numbers should be parsed.
- [CFNumberFormatterRoundingMode](cfnumberformatterroundingmode.md) — These constants are used to specify how numbers should be rounded.
- [Padding Positions](padding-positions.md) — These constants are used to specify how numbers should be padded.

## See Also

### Related Documentation

- [Data Formatting Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDataFormatting/Articles/CFDataFormatting.html#//apple_ref/doc/uid/10000176i)

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
