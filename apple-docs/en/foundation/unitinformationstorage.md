---
title: UnitInformationStorage
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/unitinformationstorage
source_url: 'https://developer.apple.com/documentation/foundation/unitinformationstorage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/unitinformationstorage.json'
content_hash: 'sha256:156b56a68a0a9b95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UnitInformationStorage

<sub>Class</sub>

A unit of measure for quantities of information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UnitInformationStorage
```

## Overview

Use instances of [UnitInformationStorage](unitinformationstorage.md) to represent quantities of information using the [NSMeasurement](nsmeasurement.md) class. The base unit of measure for information is the bit, with a nibble representing four bits and a byte representing eight bits.

Larger units of information expand on bits and bytes by orders of magnitude in both decimal and binary forms.

### Information Transfer

Units of bits commonly represent the amount of transferred information.

| Decimal Bits | Coefficient | Binary Bits | Coefficient |
|---|---|---|---|
| [kilobits](unitinformationstorage/kilobits.md) | `1000` | [kibibits](unitinformationstorage/kibibits.md) | `1024` |
| [megabits](unitinformationstorage/megabits.md) | `1000e2` | [mebibits](unitinformationstorage/mebibits.md) | `1024e2` |
| [gigabits](unitinformationstorage/gigabits.md) | `1000e3` | [gibibits](unitinformationstorage/gibibits.md) | `1024e3` |
| [terabits](unitinformationstorage/terabits.md) | `1000e4` | [tebibits](unitinformationstorage/tebibits.md) | `1024e4` |
| [petabits](unitinformationstorage/petabits.md) | `1000e5` | [pebibits](unitinformationstorage/pebibits.md) | `1024e5` |
| [exabits](unitinformationstorage/exabits.md) | `1000e6` | [exbibits](unitinformationstorage/exbibits.md) | `1024e6` |
| [zettabits](unitinformationstorage/zettabits.md) | `1000e7` | [zebibits](unitinformationstorage/zebibits.md) | `1024e7` |
| [yottabits](unitinformationstorage/yottabits.md) | `1000e8` | [yobibits](unitinformationstorage/yobibits.md) | `1024e8` |

### Information Storage

Units of bytes commonly represent the amount of stored information.

| Decimal Bytes | Coefficient | Binary Bytes | Coefficient |
|---|---|---|---|
| [kilobytes](unitinformationstorage/kilobytes.md) | `1000` | [kibibytes](unitinformationstorage/kibibytes.md) | `1024` |
| [megabytes](unitinformationstorage/megabytes.md) | `1000e2` | [mebibytes](unitinformationstorage/mebibytes.md) | `1024e2` |
| [gigabytes](unitinformationstorage/gigabytes.md) | `1000e3` | [gibibytes](unitinformationstorage/gibibytes.md) | `1024e3` |
| [terabytes](unitinformationstorage/terabytes.md) | `1000e4` | [tebibytes](unitinformationstorage/tebibytes.md) | `1024e4` |
| [petabytes](unitinformationstorage/petabytes.md) | `1000e5` | [pebibytes](unitinformationstorage/pebibytes.md) | `1024e5` |
| [exabytes](unitinformationstorage/exabytes.md) | `1000e6` | [exbibytes](unitinformationstorage/exbibytes.md) | `1024e6` |
| [zettabytes](unitinformationstorage/zettabytes.md) | `1000e7` | [zebibytes](unitinformationstorage/zebibytes.md) | `1024e7` |
| [yottabytes](unitinformationstorage/yottabytes.md) | `1000e8` | [yobibytes](unitinformationstorage/yobibytes.md) | `1024e8` |

## Relationships

- **Inherits From**: [Dimension](dimension.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Accessing Predefined Common Units

- [bits](unitinformationstorage/bits.md) — The bits unit of information.
- [nibbles](unitinformationstorage/nibbles.md) — The nibbles unit of information.
- [bytes](unitinformationstorage/bytes.md) — The bytes unit of information.

### Accessing Predefined Binary Units

- [kibibits](unitinformationstorage/kibibits.md) — The kibibits unit of information.
- [kibibytes](unitinformationstorage/kibibytes.md) — The kibibytes unit of information.
- [mebibits](unitinformationstorage/mebibits.md) — The mebibits unit of information.
- [mebibytes](unitinformationstorage/mebibytes.md) — The mebibytes unit of information.
- [gibibits](unitinformationstorage/gibibits.md) — The gibibits unit of information.
- [gibibytes](unitinformationstorage/gibibytes.md) — The gibibytes unit of information.
- [tebibits](unitinformationstorage/tebibits.md) — The tebibits unit of information.
- [tebibytes](unitinformationstorage/tebibytes.md) — The tebibytes unit of information.
- [pebibits](unitinformationstorage/pebibits.md) — The pebibits unit of information.
- [pebibytes](unitinformationstorage/pebibytes.md) — The pebibytes unit of information.
- [exbibits](unitinformationstorage/exbibits.md) — The exbibits unit of information.
- [exbibytes](unitinformationstorage/exbibytes.md) — The exbibytes unit of information.
- [zebibits](unitinformationstorage/zebibits.md) — The zebibits unit of information.
- [zebibytes](unitinformationstorage/zebibytes.md) — The zebibytes unit of information.
- [yobibits](unitinformationstorage/yobibits.md) — The yobibits unit of information.
- [yobibytes](unitinformationstorage/yobibytes.md) — The yobibytes unit of information.

### Accessing Predefined Decimal Units

- [kilobits](unitinformationstorage/kilobits.md) — The kilobits unit of information.
- [kilobytes](unitinformationstorage/kilobytes.md) — The kilobytes unit of information.
- [megabits](unitinformationstorage/megabits.md) — The megabits unit of information.
- [megabytes](unitinformationstorage/megabytes.md) — The megabytes unit of information.
- [gigabits](unitinformationstorage/gigabits.md) — The gigabits unit of information.
- [gigabytes](unitinformationstorage/gigabytes.md) — The gigabytes unit of information.
- [terabits](unitinformationstorage/terabits.md) — The terabits unit of information.
- [terabytes](unitinformationstorage/terabytes.md) — The terrabytes unit of information.
- [petabits](unitinformationstorage/petabits.md) — The petabits unit of information.
- [petabytes](unitinformationstorage/petabytes.md) — The petabytes unit of information.
- [exabits](unitinformationstorage/exabits.md) — The exabits unit of information.
- [exabytes](unitinformationstorage/exabytes.md) — The exabytes unit of information.
- [zettabits](unitinformationstorage/zettabits.md) — The zettabits unit of information.
- [zettabytes](unitinformationstorage/zettabytes.md) — The zettabytes unit of information.
- [yottabits](unitinformationstorage/yottabits.md) — The yottabits unit of information.
- [yottabytes](unitinformationstorage/yottabytes.md) — The yottabytes unit of information.
