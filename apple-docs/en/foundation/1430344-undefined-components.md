---
title: Undefined Components
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/1430344-undefined-components
source_url: 'https://developer.apple.com/documentation/foundation/1430344-undefined-components'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/1430344-undefined-components.json'
content_hash: 'sha256:6c63ab037dba00a4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Dates and Times](dates-and-times.md) · [NSDateComponents](nsdatecomponents.md)

# Undefined Components

<sub>API Collection</sub>

Constants that denote that the value of a date component is undefined.

## Overview

For example, when an [NSDateComponents](nsdatecomponents.md) object is created as the result of calculating the distance in time between two dates represented by a particular calendar, the value for the [NSCalendarUnitWeekOfYear](nscalendar/unit/weekofyear.md) component would be set to [NSDateComponentUndefined](nsdatecomponentundefined.md).

## Topics

### Constants

- [NSDateComponentUndefined](nsdatecomponentundefined.md) — Specifies a date component without a value.
- [NSUndefinedDateComponent](nsundefineddatecomponent.md) — Specifies a date component without a value. _(deprecated)_

## See Also

### Validating a Date

- [validDate](nsdatecomponents/isvaliddate.md) — A Boolean value that indicates whether the current combination of properties represents a date which exists in the current calendar.
- [- isValidDateInCalendar:](<nsdatecomponents/isvaliddate(in_).md>) — Returns a Boolean value that indicates whether the current combination of properties represents a date which exists in the specified calendar.
- [date](nsdatecomponents/date.md) — The date calculated from the current components using the stored calendar.
