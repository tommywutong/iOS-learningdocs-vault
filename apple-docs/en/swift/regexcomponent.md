---
title: RegexComponent
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/regexcomponent
source_url: 'https://developer.apple.com/documentation/swift/regexcomponent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/regexcomponent.json'
content_hash: 'sha256:7fd9f8816432ca09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# RegexComponent

<sub>Protocol</sub>

A type that represents a regular expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol RegexComponent<RegexOutput>
```

## Overview

You can use types that conform to `RegexComponent` as parameters to string searching operations and inside `RegexBuilder` closures.

## Relationships

- **Inherited By**: [CustomConsumingRegexComponent](customconsumingregexcomponent.md)

- **Conforming Types**: [Anchor](../regexbuilder/anchor.md), [Capture](../regexbuilder/capture.md), [Character](character.md), [CharacterClass](../regexbuilder/characterclass.md), [ChoiceOf](../regexbuilder/choiceof.md), [Local](../regexbuilder/local.md), [Lookahead](../regexbuilder/lookahead.md), [NegativeLookahead](../regexbuilder/negativelookahead.md), [One](../regexbuilder/one.md), [OneOrMore](../regexbuilder/oneormore.md), [Optionally](../regexbuilder/optionally.md), [Reference](../regexbuilder/reference.md), [Regex](regex.md), [Repeat](../regexbuilder/repeat.md), [String](string.md), [Substring](substring.md), [TryCapture](../regexbuilder/trycapture.md), [Scalar](unicode/scalar.md), [ZeroOrMore](../regexbuilder/zeroormore.md)

## Topics

### Creating a regex component

- [init(_:_:)](<regexcomponent/init(____).md>) — Creates a character class that combines the given classes in a union.

### Getting a regex from a component

- [regex](regexcomponent/regex.md) — The regular expression represented by this component.

### Matching substring sequences

- [anyOf(_:)](<regexcomponent/anyof(__)-3pexl.md>) — Returns a character class that matches any Unicode scalar in the given sequence.
- [anyOf(_:)](<regexcomponent/anyof(__)-4xgea.md>) — Returns a character class that matches any character in the given string or sequence.
- [any](regexcomponent/any.md) — A character class that matches any element.
- [anyGraphemeCluster](regexcomponent/anygraphemecluster.md) — A character class that matches any single `Character`, or extended grapheme cluster, regardless of the current semantic level.
- [anyNonNewline](regexcomponent/anynonnewline.md) — A character class that matches any element that isn’t a newline.
- [digit](regexcomponent/digit.md) — A character class that matches any digit.
- [hexDigit](regexcomponent/hexdigit.md) — A character class that matches any hexadecimal digit.
- [word](regexcomponent/word.md) — A character class that matches any element that is a “word character”.

### Matching whitespace and line endings

- [horizontalWhitespace](regexcomponent/horizontalwhitespace.md) — A character class that matches any element that is classified as horizontal whitespace.
- [newlineSequence](regexcomponent/newlinesequence.md) — A character class that matches any newline sequence.
- [verticalWhitespace](regexcomponent/verticalwhitespace.md) — A character class that matches any element that is classified as vertical whitespace.
- [whitespace](regexcomponent/whitespace.md) — A character class that matches any element that is classified as whitespace.

### Matching dates and times

- [date(_:locale:timeZone:calendar:)](<regexcomponent/date(__locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a style, capturing it as a Foundation date.
- [date(format:locale:timeZone:calendar:twoDigitStartDate:)](<regexcomponent/date(format_locale_timezone_calendar_twodigitstartdate_).md>) — Creates a regex component that matches a localized date string formatted in accordance with a format string, capturing it as a Foundation date.
- [dateTime(date:time:locale:timeZone:calendar:)](<regexcomponent/datetime(date_time_locale_timezone_calendar_).md>) — Creates a regex component that matches a localized date and time string, capturing it as a Foundation date.
- [iso8601](regexcomponent/iso8601.md) — A regex component that matches a default ISO 8601-formatted date string, capturing it as a Foundation date.
- [iso8601Date(timeZone:dateSeparator:)](<regexcomponent/iso8601date(timezone_dateseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing it as a Foundation date in the specified time zone.
- [iso8601(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)](<regexcomponent/iso8601(timezone_includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string, capturing the matched substring as a Foundation date in the specified time zone.
- [iso8601WithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)](<regexcomponent/iso8601withtimezone(includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_timezoneseparator_).md>) — Creates a regex component that matches an ISO 8601-formatted date string that includes a time zone component, capturing the matched substring as a Foundation date.

### Matching numeric formats

- [localizedInteger(locale:)](<regexcomponent/localizedinteger(locale_).md>) — Creates a regex component that matches a localized numeric string, capturing it as an integer value.
- [localizedDouble(locale:)](<regexcomponent/localizeddouble(locale_).md>) — Creates a regex component that matches a localized numeric string, capturing it as a double-precision floating-point value.
- [localizedDecimal(locale:)](<regexcomponent/localizeddecimal(locale_).md>) — Creates a regex component that matches a localized decimal string, capturing it as a Foundation decimal.
- [localizedCurrency(code:locale:)](<regexcomponent/localizedcurrency(code_locale_).md>) — Creates a regex component that matches a localized currency string, capturing it as a decimal value.
- [localizedIntegerCurrency(code:locale:)](<regexcomponent/localizedintegercurrency(code_locale_).md>) — Creates a regex component that matches a localized currency string, capturing it as an integer value.
- [localizedIntegerPercentage(locale:)](<regexcomponent/localizedintegerpercentage(locale_).md>) — Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.
- [localizedDoublePercentage(locale:)](<regexcomponent/localizeddoublepercentage(locale_).md>) — Creates a regex component that matches a localized percentage string, capturing it as a double-precision floating-point value.

### Matching URLs

- [url(scheme:user:password:host:port:path:query:fragment:)](<regexcomponent/url(scheme_user_password_host_port_path_query_fragment_).md>) — Creates a regex component that matches a URL substring, capturing it as a Foundation URL.

### Supporting types

- [RegexOutput](regexcomponent/regexoutput.md) — The output type for this regular expression.
- [DateStyle](regexcomponent/datestyle.md) — A type alias to use when matching date components in a regular expression.
- [TimeStyle](regexcomponent/timestyle.md) — A type alias to use when matching time components in a regular expression.

### Type Properties

- [http](regexcomponent/http.md) — Creates a regex component to match an HTTP date and time, such as “2015-11-14’T’15:05:03’Z’”, and capture the string as a `Date` using the time zone as specified in the string.
- [httpComponents](regexcomponent/httpcomponents.md) — Creates a regex component to match an HTTP date and time, such as “2015-11-14’T’15:05:03’Z’”, and capture the string as a `DateComponents` using the time zone as specified in the string.
- [iso8601Components](regexcomponent/iso8601components.md) — Creates a regex component to match an ISO 8601 date and time, such as “2015-11-14’T’15:05:03’Z’”, and capture the string as a `DateComponents` using the time zone as specified in the string.

### Type Methods

- [iso8601Components(timeZone:includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:)](<regexcomponent/iso8601components(timezone_includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_).md>) — Creates a regex component to match an ISO 8601 date and time string without time zone, and capture the string as a `DateComponents` using the specified `timeZone`. If the string contains time zone designators, matches up until the start of time zone designators.
- [iso8601ComponentsWithTimeZone(includingFractionalSeconds:dateSeparator:dateTimeSeparator:timeSeparator:timeZoneSeparator:)](<regexcomponent/iso8601componentswithtimezone(includingfractionalseconds_dateseparator_datetimeseparator_timeseparator_timezoneseparator_).md>) — Creates a regex component to match an ISO 8601 date and time string, including time zone, and capture the string as a `DateComponents` using the time zone as specified in the string.
- [iso8601DateComponents(timeZone:dateSeparator:)](<regexcomponent/iso8601datecomponents(timezone_dateseparator_).md>) — Creates a regex component to match an ISO 8601 date string, such as “2015-11-14”, and capture the string as a `DateComponents`. The captured `DateComponents` would be at midnight in the specified `timeZone`.

## See Also

### Regular Expressions

- [Regex](regex.md) — A regular expression.
- [RegexRepetitionBehavior](regexrepetitionbehavior.md) — Specifies how much to attempt to match when using a quantifier.
- [RegexSemanticLevel](regexsemanticlevel.md) — A semantic level to use during regex matching.
- [RegexWordBoundaryKind](regexwordboundarykind.md) — A word boundary algorithm to use during regex matching.
- [AnyRegexOutput](anyregexoutput.md) — The type-erased, dynamic output of a regular expression match.
- [CustomConsumingRegexComponent](customconsumingregexcomponent.md)
