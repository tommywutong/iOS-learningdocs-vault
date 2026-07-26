---
title: PersonNameComponentsFormatter
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/personnamecomponentsformatter
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter.json'
content_hash: 'sha256:e8df48ef0f03094c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# PersonNameComponentsFormatter

<sub>Class</sub>

A formatter that provides localized representations of the components of a person’s name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class PersonNameComponentsFormatter
```

## Overview

Each locale has its own set of rules and conventions for how personal names are structured and represented. These rules vary widely across different locales in a several ways, including the sort and display order of given and family names, the use of salutations and honorifics, and other concerns related to the grammar, spelling, punctuation, and formatting. About the only thing that _is_ consistent across all locales is that personal names are significant and meaningful. For this reason, names deserve careful and respectful treatment—perhaps more than any other kind of information your app interacts with.

Formatters can be configured to represent names in a variety of styles, which are described in detail below.

- Default ([NSPersonNameComponentsFormatterStyleDefault](personnamecomponentsformatter/style-swift.enum/default.md))
- Short ([NSPersonNameComponentsFormatterStyleShort](personnamecomponentsformatter/style-swift.enum/short.md))
- Long ([NSPersonNameComponentsFormatterStyleLong](personnamecomponentsformatter/style-swift.enum/long.md))
- Abbreviated ([NSPersonNameComponentsFormatterStyleAbbreviated](personnamecomponentsformatter/style-swift.enum/abbreviated.md))

When determining how to represent a name in a particular style, a formatter takes a number of factors into consideration, in order of priority:

1. **Script derived behaviors** Scripts may specify a strict sort or display order of given and family names, and the availability of styles.
2. **User specified preferences** Users can enable and configure the display of short names, as well as whether or not to display nicknames when available. Users can also override the default sort and display order of given and family names for their current locale.
3. **Locale derived defaults** Locales specify a default sort and display order for given and family names.
4. **Developer specified configuration** The style property value set for the `NSPersonNameComponentsFormatter` object.

When the behavior specified in one factor conflicts with any other factors, the behavior specified by the factor with the most precedence is used. For example, the U.S. English (`en-US`) locale specifies that names be displayed in “given name followed by the family name” (for example,“John Appleseed”). This behavior would be overridden if the user changed their system preferences to have names displayed as family name followed by given name (for example, “Appleseed, John”), because user-specified preferences take precedence over locale-derived defaults. Furthermore, if the name to be formatted were Japanese (for example, given name: “泰夫”, family name: “木田”), the behavior derived for the name’s script (CJK, for Chinese, Japanese, and Korean languages) would take precedence over any locale-derived defaults or user-specified preferences to have the name displayed as family name followed by given name (for example, “木田 泰夫”).

These considerations extend to the availability of certain formatter styles as well. Because developer-specified configurations have the lowest precedence in determining behavior, the value set for the formatter’s style property can be invalidated if it’s not supported for the locale, user preferences, or script. If the specified style is not available, the next longest valid style is used. For example, a name in Arabic script (for example, “أحمد الراجحي”) does not support the Abbreviated style, so the Short style is used instead. A name that contains more than one script (for example, given name: “John”, family name: “王”) is detected to have “Unknown” script, which has its own set of behaviors and characteristics.

> [!tip] Tip
> In Swift, you can use [FormatStyle](personnamecomponents/formatstyle.md) rather than [PersonNameComponentsFormatter](personnamecomponentsformatter.md). The [FormatStyle](formatstyle.md) API offers a declarative idiom for customizing the formatting of various types. Also, Foundation caches identical [FormatStyle](formatstyle.md) instances, so you don’t need to pass them around your app, or risk wasting memory with duplicate formatters.

### Styles

`NSPersonNameComponentsFormatter` can be configured to format names in the following styles:

- **[NSPersonNameComponentsFormatterStyleDefault](personnamecomponentsformatter/style-swift.enum/default.md)** — The minimally necessary features for differentiation in a casual setting. Equivalent to [NSPersonNameComponentsFormatterStyleMedium](personnamecomponentsformatter/style-swift.enum/medium.md).
- **[NSPersonNameComponentsFormatterStyleShort](personnamecomponentsformatter/style-swift.enum/short.md)** — Relies on user preferences and language defaults to display shortened form appropriate for display in space-constrained settings.
- **[NSPersonNameComponentsFormatterStyleLong](personnamecomponentsformatter/style-swift.enum/long.md)** — The fully qualified name complete with all known components.
- **[NSPersonNameComponentsFormatterStyleAbbreviated](personnamecomponentsformatter/style-swift.enum/abbreviated.md)** — The maximally abbreviated form of a name.

|  | `namePrefix` | `givenName` | `middleName` | `familyName` | `nameSuffix` | `nickname` |
|---|---|---|---|---|---|---|
| Arabic ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(ar-SA)` | .د | أحمد |  | محمدالمصري |  |  |
| Chinese ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(zh-Hans)` | 物理学博士 | 振宁 |  | 杨 | 先生 |  |
| English ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(en-US)` | Dr. | Jonathan | Maple | Appleseed | Esq. | Johnny |
| French ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(fr-FR)` | Père | Jean-Philippe |  | de Zélicourt |  | JP |
| German ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(de-DE)` | Dr. med. | Max |  | Mustermann | junior, M.A. |  |
| Hindi ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(hi-IN)` | डॉ. | रिय |  | साहिल |  |  |
| Japanese ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(ja-JP)` |  | 泰夫 |  | 木田 | 先生 |  |
| Spanish ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(es-ES)` | Dr. | José Ramiro |  | Martín González de Rivera | júnior, PhD | Ramiro |
| Thai ![](../../../attachments/67dc4b07a8d84366d4cc0e812eb40b4a/spacer.png) `(th-TH)` | ฯพณฯ | สมชาย | ปีเตอร์ | รัตนเรืองรองบวรทิพย์ |  |  |

#### Default

The Default, or Medium, style presents names in a way that is suitable for most contexts. It uses the given and family names, as well as a nickname, if provided and enabled by the user in System Preferences.

|  | Default style |
|---|---|
| Arabic (ar-SA) | أحمد محمﺩﺍلمصﺭﻱ |
| Chinese (zh-Hans) | 杨振宁 |
| English (en-US) | Jonathan Appleseed |
| French (fr-FR) | Jean-Philippe de Zélicourt |
| German (de-DE) | Max Mustermann |
| Hindi (hi-IN) | रिय साहिल |
| Japanese (ja-JP) | 木田泰夫 |
| Spanish (es-ES) | José Ramiro Martín González de Rivera |
| Thai (th-TH) | สมชาย รัตนเรืองรอง บวรทิพย์ |

#### Short

The Short style offers an alternative display method for names whose default representation may exceed a certain length constraint. It is only available if the user has enabled “Short Names” in System Preferences, and only for names with a script that supports Short style. Otherwise, a formatter configured to display with Short style is displayed with Medium style instead.

If a user has enabled the use of short names, the user can choose from one of four variations:

- Given Name - Family Initial
- Family Name - Given Initial
- Given Name Only
- Family Name Only

Short style is not available for names in CJK script and is restricted to Given Name Only or Family Name Only for names in Arabic or Devanagari script. If the specified Short style is unavailable, the Medium style is used instead.

|  | Given Name - Family Initial | Family Name - Given Initial | Given Name Only | Family Name Only |
|---|---|---|---|---|
| Arabic (ar-SA) | _N/A_ | _N/A_ | أحمد | محمﺩﺍلمصﺭﻱ |
| Chinese (zh-Hans) | _N/A_ | _N/A_ | _N/A_ | _N/A_ |
| English (en-US) | Jonathan A | J Appleseed | Jonathan | Appleseed |
| French (fr-FR) | Jean-Philippe d | J de Zélicourt | Jean-Philippe | de Zélicourt |
| German (de-DE) | Max M | M Mustermann | Max | Mustermann |
| Hindi (hi-IN) | _N/A_ | _N/A_ | रिय | साहिल |
| Japanese (ja-JP) | _N/A_ | _N/A_ | _N/A_ | _N/A_ |
| Spanish (es-ES) | José Ramiro M | J Martín González de Rivera | José Ramiro | Martín González de Rivera |
| Thai (th-TH) | สมชาย ร | ส รัตนเรืองรองบวรทิพย์ | สมชาย | รัตนเรืองรองบวรทิพย์ |

> [!important] Important
> `NSPersonNameComponentsFormatter` does not currently account for prepositional particles. Representations using the Short style that specify a family name initial naively use the first letter unit of the particle as the initial.

#### Long

The Long style provides the most explicit representation of names. It uses all available name components, with the exception of nickname.

|  | Long style |
|---|---|
| Arabic (ar-SA) | ﺩ. أحمد محمﺩﺍلمصﺭﻱ |
| Chinese (zh-Hans) | 物理学博士杨振宁先生 |
| English (en-US) | Dr. Jonathan Maple Appleseed Esq. |
| French (fr-FR) | Père Jean-Philippe de Zélicourt |
| German (de-DE) | Dr. med. Max Mustermann junior, M.A. |
| Hindi (hi-IN) | डॉ. रिय साहिल |
| Japanese (ja-JP) | 木田泰夫先生 |
| Spanish (es-ES) | Dr. José Ramiro Martín González de Rivera júnior, PhD |
| Thai (th-TH) | ฯพณฯ สมชาย ปีเตอร์ รัตนเรืองรอง บวรทิพย์ |

#### Abbreviated

The Abbreviated style offers the most compact representation of names, similar to a monogram.

Abbreviated style is supported for names in several scripts, with the following general characteristics:

- For names in Cyrillic, Greek, or Latin script, the first characters of `givenName`, `middleName`, and `familyName` may be used.
- For names in Chinese or Japanese script, `familyName` may be used. If `familyName` is too long, or if the family name is `nil`, the Short or Medium style may be used instead.
- For names in Korean script, `givenName` may be used. If `givenName` is too long, the first character of `givenName` may be used. If `givenName` is `nil`, the `familyName` may be used instead.
- For names in Bengali, Devanagari, Gujarati, Gurmukhi, Kannada, Malayalam, Oriya, Sinhala, Tamil, Telugu, Tibetan, or Thai script, the first character of `givenName` may be used. If `givenName` is `nil`, the first character of `familyName` may be used instead.
- For names that contain more than one script, the abbreviated style may use the `familyName`, `givenName`, or the first characters of `givenName` and/or `familyName`.

If the Abbreviated style is unavailable, the Short style is used instead—unless that too is unsupported, in which case the Medium style is used instead.

|  | Abbreviated style |
|---|---|
| Arabic (ar-SA) | _N/A_ |
| Chinese (zh-Hans) | 杨 |
| English (en-US) | JMA |
| French (fr-FR) | Jd |
| German (de-DE) | MM |
| Hindi (hi-IN) | मि |
| Japanese (ja-JP) | 木田 |
| Spanish (es-ES) | JM |
| Thai (th-TH) | ส |

> [!important] Important
> `NSPersonNameComponentsFormatter` doesn’t currently account for prepositional particles or compound names. Representations using the Abbreviated style uses the first letter unit of each name component, regardless.

## Relationships

- **Inherits From**: [Formatter](formatter.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring Formatter Behavior

- [style](personnamecomponentsformatter/style-swift.property.md) — The formatting style of the receiver.
- [phonetic](personnamecomponentsformatter/isphonetic.md) — A Boolean value that specifies whether the receiver should use only the phonetic representations of name components.

### Converting Between Person Name Components and Strings

- [+ localizedStringFromPersonNameComponents:style:options:](<personnamecomponentsformatter/localizedstring(from_style_options_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [- stringFromPersonNameComponents:](<personnamecomponentsformatter/string(from_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object.
- [- annotatedStringFromPersonNameComponents:](<personnamecomponentsformatter/annotatedstring(from_).md>) — Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [- personNameComponentsFromString:](<personnamecomponentsformatter/personnamecomponents(from_).md>) — Returns a person name components object from a given string.
- [- getObjectValue:forString:errorDescription:](<personnamecomponentsformatter/getobjectvalue(__for_errordescription_).md>) — Returns by reference a person name components object after creating it from a given string.

### Constants

- [Style](personnamecomponentsformatter/style-swift.enum.md) — The formatting styles for person name components.
- [Options](personnamecomponentsformatter/options.md) — Options for formatting person name components.
- [Attributed String Key](attributed-string-key.md) — This constant is used as a key for person name component attributes in attributed strings returned by the [- annotatedStringFromPersonNameComponents:](<personnamecomponentsformatter/annotatedstring(from_).md>) method
- [Attributed String Components](attributed-string-components.md) — These constants are used to identify individual components of attributed strings returned by the [- annotatedStringFromPersonNameComponents:](<personnamecomponentsformatter/annotatedstring(from_).md>) method.
- [Component Delimiter](component-delimiter.md) — This constant defines the delimiter used to separate name components.

### Instance Properties

- [locale](personnamecomponentsformatter/locale.md) — Specifies the locale to format names.

## See Also

### Names

- [PersonNameComponents](personnamecomponents.md) — The separate parts of a person’s name, allowing locale-aware formatting.
