---
title: titleHighlightRanges
framework: MapKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.3+, iPadOS 9.3+, Mac Catalyst 13.1+, macOS 10.11.4+, tvOS 9.2+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/mklocalsearchcompletion/titlehighlightranges
source_url: 'https://developer.apple.com/documentation/mapkit/mklocalsearchcompletion/titlehighlightranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mklocalsearchcompletion/titlehighlightranges.json'
content_hash: 'sha256:614c19e899289f87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKLocalSearchCompletion](../mklocalsearchcompletion.md)

# titleHighlightRanges

<sub>Instance Property</sub>

The ranges of characters to highlight in the title string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var titleHighlightRanges: [NSValue] { get }
```

## Discussion

This property contains an array of [NSValue](../../foundation/nsvalue.md) objects, each of which contains an [NSRange](../../foundation/nsrange-c.struct.md) type defining a range of characters in the [title](title.md) string. Use this property to identify the ranges of characters in the title string that you want to highlight. Highlighting the matching text of a search completion is optional, but it’s a best practice for providing helpful information to the user.

## See Also

### Getting the search completions

- [title](title.md) — The title string associated with the point of interest.
- [subtitle](subtitle.md) — The subtitle (if any) associated with the point of interest.
- [subtitleHighlightRanges](subtitlehighlightranges.md) — The ranges of characters to highlight in the subtitle string.
