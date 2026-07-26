---
title: allowsNaturalLanguage
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.9 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsdateformatter/allowsnaturallanguage
source_url: 'https://developer.apple.com/documentation/foundation/nsdateformatter/allowsnaturallanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateformatter/allowsnaturallanguage.json'
content_hash: 'sha256:cbe751c3aafedc5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# allowsNaturalLanguage

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the receiver attempts to process dates entered as a vernacular string.

<sub>macOS</sub>

```objc
- (BOOL) allowsNaturalLanguage;
```

## Return Value

[true](../../swift/true.md) if the receiver attempts to process dates entered as a vernacular string (“today,” “next week,” “dinner time,” and so on), otherwise [false](../../swift/false.md).

## Discussion

Natural-language processing supports only a limited set of colloquial phrases, primarily in English. It may give unexpected results, and its use is strongly discouraged.

### Special Considerations

This method is for use with formatters using `NSDateFormatterBehavior10_0` behavior.

## See Also

### Managing Natural Language Support

- [lenient](../dateformatter/islenient.md) — A Boolean value that indicates whether the receiver uses heuristics when parsing a string.
- [doesRelativeDateFormatting](../dateformatter/doesrelativedateformatting.md) — A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.
