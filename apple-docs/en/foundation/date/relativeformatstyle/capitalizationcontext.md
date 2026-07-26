---
title: capitalizationContext
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/date/relativeformatstyle/capitalizationcontext
source_url: 'https://developer.apple.com/documentation/foundation/date/relativeformatstyle/capitalizationcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/date/relativeformatstyle/capitalizationcontext.json'
content_hash: 'sha256:13f1d663a4c33e43'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [Date](../../date.md) · [RelativeFormatStyle](../relativeformatstyle.md)

# capitalizationContext

<sub>Instance Property</sub>

The capitalization context to use when formatting the relative dates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var capitalizationContext: FormatStyleCapitalizationContext
```

## Discussion

Setting the capitalization context to [beginningOfSentence](../../formatstylecapitalizationcontext/beginningofsentence.md) sets the first word of the relative date string to upper-case. A capitalization context set to [middleOfSentence](../../formatstylecapitalizationcontext/middleofsentence.md) keeps all words in the string lower-cased.

If you set this property to `nil`, the format style resets to using `unknown`.

## See Also

### Modifying a Relative Date Format Style

- [presentation](presentation-swift.property.md) — Specifies the style to use when describing a relative date, such as “1 day ago” or “yesterday”.
- [unitsStyle](unitsstyle-swift.property.md) — The style to use when formatting the quantity or the name of the unit, such as “1 day ago” or “one day ago”.
- [calendar](calendar.md) — The calendar to use when formatting relative dates.
- [locale](locale.md) — The locale to use when formatting the relative date.
- [locale(_:)](<locale(__).md>) — Modifies the relative date format style to use the specified locale.
