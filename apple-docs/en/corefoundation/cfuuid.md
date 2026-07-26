---
title: CFUUID
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfuuid
source_url: 'https://developer.apple.com/documentation/corefoundation/cfuuid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfuuid.json'
content_hash: 'sha256:e2b7106bddaacf90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFUUID

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFUUID
```

## Overview

CFUUID objects are used by plug-ins to uniquely identify types, interfaces, and factories. When creating a new type, host developers must generate UUIDs to identify the type as well as its interfaces and factories.

UUIDs (Universally Unique Identifiers), also known as GUIDs (Globally Unique Identifiers) or IIDs (Interface Identifiers), are 128-bit values designed to be unique.

The standard format for UUIDs represented in ASCII is a string punctuated by hyphens, for example `68753A44-4D6F-1226-9C60-0050E4C00067`. The hex representation looks, as you might expect, like a list of numerical values preceded by `0x`. For example, `0x68, 0x75, 0x3A, 0x44, 0x4D, 0x6F, 0x12, 0x26, 0x9C, 0x60, 0x00, 0x50, 0xE4, 0xC0, 0x00, 0x67` . To use a UUID, you create it and then copy the resulting strings into your header and C language source files. Because a UUID is expressed as an array of bytes, there are no endianness considerations for different platforms.

You can create a CFUUID object using any one of the `CFUUIDCreate...` functions. Use the [CFUUIDGetConstantUUIDWithBytes](<cfuuidgetconstantuuidwithbytes(__________________________________).md>) function if you want to declare a UUID constant in a `#define` statement. You can get the raw bytes of an existing CFUUID object using the [CFUUIDGetUUIDBytes](<cfuuidgetuuidbytes(__).md>) function.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating CFUUID Objects

- [CFUUIDCreate](<cfuuidcreate(__).md>) — Creates a Universally Unique Identifier (UUID) object.
- [CFUUIDCreateFromString](<cfuuidcreatefromstring(____).md>) — Creates a CFUUID object for a specified string.
- [CFUUIDCreateFromUUIDBytes](<cfuuidcreatefromuuidbytes(____).md>) — Creates a CFUUID object from raw UUID bytes.
- [CFUUIDCreateWithBytes](<cfuuidcreatewithbytes(__________________________________).md>) — Creates a CFUUID object from raw UUID bytes.

### Getting Information About CFUUID Objects

- [CFUUIDCreateString](<cfuuidcreatestring(____).md>) — Returns the string representation of a specified CFUUID object.
- [CFUUIDGetConstantUUIDWithBytes](<cfuuidgetconstantuuidwithbytes(__________________________________).md>) — Returns a CFUUID object from raw UUID bytes.
- [CFUUIDGetUUIDBytes](<cfuuidgetuuidbytes(__).md>) — Returns the value of a UUID object as raw bytes.

### Getting the CFUUID Type Identifier

- [CFUUIDGetTypeID](<cfuuidgettypeid().md>) — Returns the type identifier for all CFUUID objects.

### Data Types

- [CFUUIDBytes](cfuuidbytes.md) — A 128-bit struct that represents a UUID as raw bytes.

## See Also

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
