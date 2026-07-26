---
title: Scanner
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/scanner
source_url: 'https://developer.apple.com/documentation/foundation/scanner'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/scanner.json'
content_hash: 'sha256:a537b707018c481d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Scanner

<sub>Class</sub>

A string parser that scans for substrings or characters in a character set, and for numeric values from decimal, hexadecimal, and floating-point representations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class Scanner
```

## Overview

A [Scanner](scanner.md) object interprets and converts the characters of a [String](../swift/string.md) into number and string values. You assign the scanner’s string when you create the scanner, and the scanner progresses through the characters of that string from beginning to end as you request items.

Because of the nature of class clusters, a scanner object isn’t an actual instance of the [Scanner](scanner.md) class, but is one of its private subclasses. Although a scanner object’s class is private, its interface is public, as declared by this abstract superclass, [Scanner](scanner.md). The objects you create using this class are referred to as scanner objects (and when no confusion will result, merely as scanners).

To set a [Scanner](scanner.md) object to ignore a set of characters as it scans the string, use the [charactersToBeSkipped](scanner/characterstobeskipped.md) property. Characters in the skip set are skipped over before the target is scanned. The default set of characters to skip is the whitespace and newline character set.

To retrieve the unscanned remainder of the string, use `scanner.string.substring(from: scanner.scanLocation)`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Scanner

- [+ localizedScannerWithString:](<scanner/localizedscanner(with_).md>) — Returns an `NSScanner` object that scans a given string according to the user’s default locale.
- [- initWithString:](<scanner/init(string_).md>) — Returns an `NSScanner` object initialized to scan a given string.

### Getting a Scanner’s String

- [string](scanner/string.md) — The string the scanner will scan.

### Configuring a Scanner

- [scanLocation](scanner/scanlocation.md) — The character position at which the receiver will begin its next scanning operation. _(deprecated)_
- [caseSensitive](scanner/casesensitive.md) — Flag that indicates whether the receiver distinguishes case in the characters it scans.
- [charactersToBeSkipped](scanner/characterstobeskipped.md) — Character set containing the characters the scanner ignores when looking for a scannable element.
- [locale](scanner/locale.md) — The locale to use when scanning.

### Scanning Characters and Strings

- [- scanCharactersFromSet:intoString:](<scanner/scancharacters(from_into_).md>) — Scans the string as long as characters from a given character set are encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_
- [- scanUpToCharactersFromSet:intoString:](<scanner/scanuptocharacters(from_into_).md>) — Scans the string until a character from a given character set is encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_
- [- scanString:intoString:](<scanner/scanstring(__into_).md>) — Scans a given string, returning an equivalent string object by reference if a match is found. _(deprecated)_
- [- scanUpToString:intoString:](<scanner/scanupto(__into_).md>) — Scans the string until a given string is encountered, accumulating characters into a string that’s returned by reference. _(deprecated)_

### Scanning Numeric Values

- [- scanDecimal:](<scanner/scandecimal(__).md>) — Scans for an `NSDecimal` value, returning a found value by reference. _(deprecated)_
- [- scanDouble:](<scanner/scandouble(__).md>) — Scans for a double value, returning a found value by reference. _(deprecated)_
- [- scanFloat:](<scanner/scanfloat(__).md>) — Scans for a float value, returning a found value by reference. _(deprecated)_
- [- scanHexDouble:](<scanner/scanhexdouble(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexFloat:](<scanner/scanhexfloat(__).md>) — Scans for a double value from a hexadecimal representation, returning a found value by reference.
- [- scanHexInt:](<scanner/scanhexint32(__).md>) — Scans for an unsigned value from a hexadecimal representation, returning a found value by reference. _(deprecated)_
- [- scanHexLongLong:](<scanner/scanhexint64(__).md>) — Scans for a long long value from a hexadecimal representation, returning a found value by reference.
- [- scanInteger:](<scanner/scanint(__).md>) — Scans for an NSInteger value from a decimal representation, returning a found value by reference
- [- scanInt:](<scanner/scanint32(__).md>) — Scans for an int value from a decimal representation, returning a found value by reference. _(deprecated)_
- [- scanLongLong:](<scanner/scanint64(__).md>) — Scans for a long long value from a decimal representation, returning a found value by reference.
- [- scanUnsignedLongLong:](<scanner/scanunsignedlonglong(__).md>) — Scans for an unsigned long long value from a decimal representation, returning a found value by reference.

### Monitoring Scanner Progress

- [atEnd](scanner/isatend.md) — Flag that indicates whether the receiver has exhausted all significant characters.

### Instance Properties

- [currentIndex](scanner/currentindex.md)

### Instance Methods

- [scanCharacter()](<scanner/scancharacter().md>)
- [scanCharacters(from:)](<scanner/scancharacters(from_).md>)
- [scanDecimal()](<scanner/scandecimal().md>)
- [scanDouble(representation:)](<scanner/scandouble(representation_).md>)
- [scanFloat(representation:)](<scanner/scanfloat(representation_).md>)
- [scanInt(representation:)](<scanner/scanint(representation_).md>)
- [scanInt32(representation:)](<scanner/scanint32(representation_).md>)
- [scanInt64(representation:)](<scanner/scanint64(representation_).md>)
- [scanString(_:)](<scanner/scanstring(__).md>)
- [scanUInt64(representation:)](<scanner/scanuint64(representation_).md>)
- [scanUpToCharacters(from:)](<scanner/scanuptocharacters(from_).md>)
- [scanUpToString(_:)](<scanner/scanuptostring(__).md>)

### Enumerations

- [NumberRepresentation](scanner/numberrepresentation.md)

## See Also

### Pattern Matching

- [NSRegularExpression](nsregularexpression.md) — An immutable representation of a compiled regular expression that you apply to Unicode strings.
- [NSDataDetector](nsdatadetector.md) — A specialized regular expression object that matches natural language text for predefined data patterns.
- [NSTextCheckingResult](nstextcheckingresult.md) — An occurrence of textual content found during the analysis of a block of text, such as when matching a regular expression.
- [NSNotFound](nsnotfound-4qp9h.md) — A value indicating that a requested item couldn’t be found or doesn’t exist.
