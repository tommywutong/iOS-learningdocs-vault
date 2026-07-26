---
title: Numbers, Data, and Basic Values
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/numbers-data-and-basic-values
source_url: 'https://developer.apple.com/documentation/foundation/numbers-data-and-basic-values'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numbers-data-and-basic-values.json'
content_hash: 'sha256:5d5d8e8115094e8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# Numbers, Data, and Basic Values

<sub>API Collection</sub>

Work with primitive values and other fundamental types used throughout Cocoa.

## Topics

### Numbers

- [Int](../swift/int.md) — A signed integer value type.
- [Double](../swift/double.md) — A double-precision (64-bit), floating-point value type.
- [Decimal](decimal.md) — A structure representing a base-10 number.
- [NumberFormatter](numberformatter.md) — A formatter that converts between numeric values and their textual representations.

### Binary Data

- [Data](data.md) — A byte buffer in memory.
- [DataProtocol](dataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous data buffers.
- [MutableDataProtocol](mutabledataprotocol.md) — A protocol that provides consistent data access to the bytes underlying contiguous and noncontiguous mutable data buffers.
- [ContiguousBytes](contiguousbytes.md) — A protocol that declares the type offers direct access to the underlying raw bytes in a contiguous manner.

### URLs

- [URL](url.md) — A value that identifies the location of a resource, such as an item on a remote server or the path to a local file.
- [URLComponents](urlcomponents.md) — A structure that parses URLs into and constructs URLs from their constituent parts.
- [URLQueryItem](urlqueryitem.md) — A single name-value pair from the query portion of a URL.

### Unique Identifiers

- [UUID](uuid.md) — A universally unique value to identify types, interfaces, and other items.

### Geometry

- [CGFloat](../corefoundation/cgfloat-swift.struct.md) — The basic type for floating-point scalar values in Core Graphics and related frameworks.
- [NSPoint](nspoint.md) — A point in a Cartesian coordinate system.
- [NSSize](nssize.md) — A two-dimensional size.
- [NSRect](nsrect.md) — A rectangle.
- [AffineTransform](affinetransform.md) — A graphics coordinate transformation.
- [NSEdgeInsets](nsedgeinsets.md) — A description of the distance between the edges of two rectangles.

### Ranges

- [NSRange](nsrange-swift.typealias.md) — A structure used to describe a portion of a series, such as characters in a string or objects in an array.

## See Also

### Fundamentals

- [Strings and Text](strings-and-text.md) — Create and process strings of Unicode characters, use regular expressions to find patterns, and perform natural language analysis of text.
- [Collections](collections.md) — Use arrays, dictionaries, sets, and specialized collections to store and iterate groups of objects or values.
- [Dates and Times](dates-and-times.md) — Compare dates and times, and perform calendar and time zone calculations.
- [Units and Measurement](units-and-measurement.md) — Label numeric quantities with physical dimensions to allow locale-aware formatting and conversion between related units.
- [Data Formatting](data-formatting.md) — Convert numbers, dates, measurements, and other values to and from locale-aware string representations.
- [Filters and Sorting](filters-and-sorting.md) — Use predicates, expressions, and sort descriptors to examine elements in collections and other services.
