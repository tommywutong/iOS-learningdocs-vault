---
title: 'init(markerFormat:options:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nstextlist/init(markerformat:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/nstextlist/init(markerformat:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nstextlist/init%28markerformat%3Aoptions%3A%29.json'
content_hash: 'sha256:962d917f78715fc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSTextList](../nstextlist.md)

# init(markerFormat:options:)

<sub>Initializer</sub>

Returns an initialized text list.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(markerFormat: NSTextList.MarkerFormat, options: Int)
```

## Parameters

- `markerFormat` — The marker format for the text list.

- `options` — The marker options for the text list. Values for `mask` are listed in [Constants](../nstextlist.md#Constants).

## Return Value

An initialized text list.

## Discussion

The marker format is specified as a constant string, except for a numbering specifier, which takes the form `{`keyword`}`. The currently supported values for keyword include:

- `box`
- `check`
- `circle`
- `diamond`
- `disc`
- `hyphen`
- `square`
- `lower-hexadecimal`
- `upper-hexadecimal`
- `octal`
- `lower-alpha` or  `lower-latin`
- `upper-alpha` or  `upper-latin`
- `lower-roman`
- `upper-roman`
- `decimal`

Thus, for example, `@"({decimal})"` would specify the format for a list numbered (1), (2), (3), and so on, and `@"{upper-roman}"` would specify the format for a list numbered I, II, III, IV, and so on. (All of these keywords are included in the Cascading Style Sheets level 3 specification.)

## See Also

### Related Documentation

- [markerFormat](markerformat-swift.property.md) — Returns the marker format string used by the receiver.
- [listOptions](listoptions.md) — Returns the list options mask value of the receiver.

### Creating a text list

- [- initWithCoder:](<init(coder_).md>) — Initializes and returns a newly allocated text list item.
- [- initWithMarkerFormat:options:startingItemNumber:](<init(markerformat_options_startingitemnumber_).md>) — Returns a new text list with the format, options, and starting item number you provide.
