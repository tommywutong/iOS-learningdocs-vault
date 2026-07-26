---
title: OSLogInterpolation
framework: os
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/os/osloginterpolation
source_url: 'https://developer.apple.com/documentation/os/osloginterpolation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/os/osloginterpolation.json'
content_hash: 'sha256:8b30eedf7fdf0f94'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [os](../os.md)

# OSLogInterpolation

<sub>Structure</sub>

A container for the elements of a log message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct OSLogInterpolation
```

## Overview

An [OSLogInterpolation](osloginterpolation.md) structure contains a formatted string and its interpolated arguments. Don’t create [OSLogInterpolation](osloginterpolation.md) structures directly. The system creates them automatically when you log messages using the [Logger](logger.md) object.

When you craft log messages, you may incorporate content from your code’s variables directly into the message strings. When you do, the logging system creates [OSLogInterpolation](osloginterpolation.md) structures to store those values. The structure stores the provided values as-is, and the logging system formats those values as strings only in the final log message. To change the final appearance of a value, include additional parameters along with the value. Consider the following example, which logs values of several different types:

```swift
logger.log("\(taskID) \(giftCardID) \(serverID) \(seconds)")
```

For values that are variable in length, formatting them makes the log message easier to read. In the preceding example, `giftCardID` and `seconds` contain variable-length values. The following example fixes the formatting issues by making all gift card IDs the same width and aligning them to the left edge of the available space. The example also formats each seconds value as a fixed-point number with only two digits to the right of the decimal point.

```swift
logger.log("\(taskID) \(giftCardID, align: .left(columns: GiftCard.maxIDLength)) \(serverID) \(seconds, format: .fixed(precision: 2))")
```

Because strings and custom objects may contain user-sensitive information, the logging system redacts those values by default, however, it doesn’t redact numerical values. The resulting log message displays a string like `<private>` instead of the actual value. If you know the value doesn’t include sensitive data, change the privacy setting using the `privacy` parameter, as the following example shows:

```swift
logger.log("Paid with bank account \(accountNumberString)")   // Redacted by default
logger.log("Ordered smoothie \(smoothieName, privacy: .public)")  // Visible!
```

## Relationships

- **Conforms To**: [StringInterpolationProtocol](../swift/stringinterpolationprotocol.md)

## Topics

### Appending Strings

- [appendInterpolation(_:align:privacy:)](<osloginterpolation/appendinterpolation(__align_privacy_)-6tazr.md>) — Appends an interpolated string.
- [appendInterpolation(_:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__align_privacy_attributes_)-7g68v.md>) — Appends an interpolated string with the specified attributes.

### Appending Signed Integers

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-8kli1.md>) — Appends an interpolated integer.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-5ihzf.md>) — Appends an interpolated 8-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-190d0.md>) — Appends an interpolated 16-bit integer.
- [appendInterpolation(_:format:privacy:)](<osloginterpolation/appendinterpolation(__format_privacy_)-3ji02.md>) — Appends an interpolated 32-bit integer.
- [appendInterpolation(_:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_privacy_attributes_)-4i2ir.md>) — Appends an interpolated 32-bit integer with the specified attributes.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-2sb1i.md>) — Appends an interpolated 32-bit integer with the specified alignment.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-802m9.md>) — Appends an interpolated 64-bit integer.

### Appending Unsigned Integers

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-20jin.md>) — Appends an interpolated unsigned integer.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-4qvu9.md>) — Appends an interpolated unsigned 8-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-7k91g.md>) — Appends an interpolated unsigned 16-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-2i3qh.md>) — Appends an interpolated unsigned 32-bit integer.
- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-81jbm.md>) — Appends an interpolated unsigned 64-bit integer.

### Appending Doubles

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-6mu00.md>) — Appends an interpolated double.
- [appendInterpolation(_:format:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_align_privacy_attributes_)-8bi90.md>) — Appends an interpolated double with the specified attributes.

### Appending Floats

- [appendInterpolation(_:format:align:privacy:)](<osloginterpolation/appendinterpolation(__format_align_privacy_)-7z1jd.md>) — Appends an interpolated float.
- [appendInterpolation(_:format:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_align_privacy_attributes_)-78sek.md>) — Appends an interpolated float with the specified attributes.

### Appending Boolean Values

- [appendInterpolation(_:format:privacy:)](<osloginterpolation/appendinterpolation(__format_privacy_)-686xc.md>) — Adds a Boolean argument to the message.

### Appending Generic Types

- [appendInterpolation(_:align:privacy:)](<osloginterpolation/appendinterpolation(__align_privacy_)-84m60.md>) — Appends an interpolated textual representation of a type.
- [appendInterpolation(_:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__align_privacy_attributes_)-xyum.md>) — Appends an interpolated textual representation of a type using the specified attributes.
- [appendInterpolation(_:format:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_align_privacy_attributes_)-8107a.md>) — Appends an interpolated numeric type using the specified attributes.
- [appendInterpolation(_:align:privacy:)](<osloginterpolation/appendinterpolation(__align_privacy_)-8hwmt.md>) — Appends an interpolated type description.
- [appendInterpolation(_:align:privacy:attributes:)](<osloginterpolation/appendinterpolation(__align_privacy_attributes_)-9hehv.md>) — Appends an interpolated type description with the specified attributes.

### Appending Pointer Data

- [appendInterpolation(_:bytes:format:privacy:)](<osloginterpolation/appendinterpolation(__bytes_format_privacy_).md>) — Appends interpolated pointer data.
- [appendInterpolation(_:bytes:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__bytes_format_privacy_attributes_).md>) — Appends interpolated pointer data with the specified attributes.
- [appendInterpolation(_:format:privacy:)](<osloginterpolation/appendinterpolation(__format_privacy_)-5qaau.md>) — Appends an interpolated collection of raw bytes.
- [appendInterpolation(_:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_privacy_attributes_)-93lbs.md>) — Appends an interpolated collection of raw bytes with the specified attributes.

### Appending Objects

- [appendInterpolation(_:privacy:)](<osloginterpolation/appendinterpolation(__privacy_).md>) — Appends an interpolated object description.
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-3czd2.md>) — Appends an interpolated object description with the specified attributes.

### Instance Methods

- [appendInterpolation(_:format:privacy:attributes:)](<osloginterpolation/appendinterpolation(__format_privacy_attributes_)-6le5w.md>)
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-4o74h.md>)
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-6vtcc.md>)
- [appendInterpolation(_:privacy:attributes:)](<osloginterpolation/appendinterpolation(__privacy_attributes_)-9eafm.md>)

## See Also

### Value Interpolation

- [OSLogIntExtendedFormat](oslogintextendedformat.md) — Options for expanding bit rate information stored as an int during logging.
