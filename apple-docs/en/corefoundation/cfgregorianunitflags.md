---
title: CFGregorianUnitFlags
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfgregorianunitflags
source_url: 'https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfgregorianunitflags.json'
content_hash: 'sha256:005464a995d43d4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFGregorianUnitFlags

<sub>Structure</sub>

These option flags are used as a mask to indicate a specific set of fields in the CFGregorianDate or CFGregorianUnits structures.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFGregorianUnitFlags
```

## Overview

These flags are used with functions such as [CFGregorianDateIsValid](<cfgregoriandateisvalid(____).md>) and [CFAbsoluteTimeGetDifferenceAsGregorianUnits](<cfabsolutetimegetdifferenceasgregorianunits(________).md>) which operate on a CFGregorianDate or CFGregorianUnits structure. For more details, see the discussion of those functions.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFGregorianUnitsYears](cfgregorianunitflags/unitsyears.md) — Specifies the year field. _(deprecated)_
- [kCFGregorianUnitsMonths](cfgregorianunitflags/unitsmonths.md) — Specifies the month field. _(deprecated)_
- [kCFGregorianUnitsDays](cfgregorianunitflags/unitsdays.md) — Specifies the day field. _(deprecated)_
- [kCFGregorianUnitsHours](cfgregorianunitflags/unitshours.md) — Specifies the hours field. _(deprecated)_
- [kCFGregorianUnitsMinutes](cfgregorianunitflags/unitsminutes.md) — Specifies the minutes field. _(deprecated)_
- [kCFGregorianUnitsSeconds](cfgregorianunitflags/unitsseconds.md) — Specifies the seconds field. _(deprecated)_
- [kCFGregorianAllUnits](cfgregorianunitflags/allunits.md) — Specifies all fields. _(deprecated)_

### Initializers

- [init(rawValue:)](<cfgregorianunitflags/init(rawvalue_).md>)

## See Also

### Constants

- [Predefined Time Interval Values](predefined-time-interval-values.md) — Time intervals between the absolute reference date and certain other dates.
