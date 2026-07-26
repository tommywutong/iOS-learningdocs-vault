---
title: CFDateFormatter
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdateformatter
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdateformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdateformatter.json'
content_hash: 'sha256:fd192b05d83a951c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFDateFormatter

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFDateFormatter
```

## Overview

CFDateFormatter objects format the textual representations of CFDate and CFAbsoluteTime objects, and convert textual representations of dates and times into CFDate and CFAbsoluteTime objects. You can express the representation of dates and times very flexibly, for example “Thu 22 Dec 1994” is just as acceptable as “12/22/94.” You specify how strings are formatted and parsed by setting a format string and other properties of a CFDateFomatter object.

The format of the format string itself is defined by Unicode Technical Standard #35; the version of the standard used varies with release of the operating system, and is described in [Introduction to Data Formatting Programming Guide For Cocoa](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029).

> [!note] Note
> CFDateFormatter is not thread safe, so you must not mutate a given date formatter simultaneously from multiple threads.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Date Formatter

- [CFDateFormatterCreate](<cfdateformattercreate(________).md>) — Creates a new CFDateFormatter object, localized to the given locale, which will format dates to the given date and time styles.

### Configuring a Date Formatter

- [CFDateFormatterSetFormat](<cfdateformattersetformat(____).md>) — Sets the format string of the given date formatter to the specified value.
- [CFDateFormatterSetProperty](<cfdateformattersetproperty(______).md>) — Sets a date formatter property using a key-value pair.

### Parsing Strings

- [CFDateFormatterCreateDateFromString](<cfdateformattercreatedatefromstring(________).md>) — Returns a date object representing a given string.
- [CFDateFormatterGetAbsoluteTimeFromString](<cfdateformattergetabsolutetimefromstring(________).md>) — Returns an absolute time object representing a given string.

### Creating Strings From Data

- [CFDateFormatterCreateStringWithAbsoluteTime](<cfdateformattercreatestringwithabsolutetime(______).md>) — Returns a string representation of the given absolute time using the specified date formatter.
- [CFDateFormatterCreateStringWithDate](<cfdateformattercreatestringwithdate(______).md>) — Returns a string representation of the given date using the specified date formatter.
- [CFDateFormatterCreateDateFormatFromTemplate](<cfdateformattercreatedateformatfromtemplate(________).md>) — Returns a localized date format string representing the given date format components arranged appropriately for the specified locale.

### Getting Information About a Date Formatter

- [CFDateFormatterCopyProperty](<cfdateformattercopyproperty(____).md>) — Returns a copy of a date formatter’s value for a given key.
- [CFDateFormatterGetDateStyle](<cfdateformattergetdatestyle(__).md>) — Returns the date style used to create the given date formatter object.
- [CFDateFormatterGetFormat](<cfdateformattergetformat(__).md>) — Returns a format string for the given date formatter object.
- [CFDateFormatterGetLocale](<cfdateformattergetlocale(__).md>) — Returns the locale object used to create the given date formatter object.
- [CFDateFormatterGetTimeStyle](<cfdateformattergettimestyle(__).md>) — Returns the time style used to create the given date formatter object.

### Getting the CFDateFormatter Type ID

- [CFDateFormatterGetTypeID](<cfdateformattergettypeid().md>) — Returns the type identifier for CFDateFormatter.

### Data Types

- [CFDateFormatterStyle](cfdateformatterstyle.md) — Data type for predefined date and time format styles.

### Constants

- [Date Formatter Styles](date_formatter_styles.md) — Predefined date and time format styles.
- [Date Formatter Property Keys](date-formatter-property-keys.md) — Keys used in key-value pairs to discover and specify the value of date formatter properties—used in conjunction with [CFDateFormatterCopyProperty](<cfdateformattercopyproperty(____).md>) and [CFDateFormatterSetProperty](<cfdateformattersetproperty(______).md>).
- [Calendar Names](calendar-names.md) — Calendar names used by CFDateFormatter.

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
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)
- [CFFileDescriptor](cffiledescriptor.md)
