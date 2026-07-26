---
title: 'initWithDateFormat:allowNaturalLanguage:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.9 起废弃）]
languages: [occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsdateformatter/initwithdateformat:allownaturallanguage:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdateformatter/initwithdateformat:allownaturallanguage:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdateformatter/initwithdateformat%3Aallownaturallanguage%3A.json'
content_hash: 'sha256:2a0ebdd7fc8b903c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# initWithDateFormat:allowNaturalLanguage:

<sub>Instance Method</sub>

Initializes and returns an `NSDateFormatter` instance that uses the OS X 10.0 formatting behavior and the given date format string in its conversions.

<sub>macOS</sub>

```objc
- (id) initWithDateFormat:(NSString *) format allowNaturalLanguage:(BOOL) flag;
```

## Parameters

- `format` — The format for the receiver. See [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i) for a list of conversion specifiers permitted in date format strings.

- `flag` — A flag that specifies whether the receiver should process dates entered as expressions in the vernacular (for example, “tomorrow”)—[true](../../swift/true.md) means that it should.

## Return Value

An initialized `NSDateFormatter` instance that uses `format` in its conversions and that _uses the OS X 10.0 formatting behavior_.

## Discussion

`NSDateFormatter` attempts natural-language processing only after it fails to interpret an entered string according to `format`. Natural-language processing supports only a limited set of colloquial phrases, primarily in English. It may give unexpected results, and its use is strongly discouraged.

The following example creates a date formatter with the format string (for example) “Mar 15 1994” and then associates the formatter with the cells of a form (`contactsForm`):

```objc
NSDateFormatter *dateFormat = [[NSDateFormatter alloc]
    initWithDateFormat:@"%b %d %Y" allowNaturalLanguage:NO];
[[contactsForm cells] makeObjectsPerformSelector:@selector(setFormatter:)
     withObject:dateFormat];
```

### Special Considerations

You cannot use this method to initialize a formatter with the OS X 10.4 formatting behavior, you must use `init`.

## See Also

### Related Documentation

- [doesRelativeDateFormatting](../dateformatter/doesrelativedateformatting.md) — A Boolean value that indicates whether the receiver uses phrases such as “today” and “tomorrow” for the date component.
- [Data Formatting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DataFormatting/DataFormatting.html#//apple_ref/doc/uid/10000029i)

### Deprecated

- [generatesCalendarDates](../dateformatter/generatescalendardates.md) — Indicates whether the formatter generates the deprecated calendar date type.
