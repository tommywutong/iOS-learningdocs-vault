---
title: 'personNameComponents(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponentsformatter/personnamecomponents(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/personnamecomponents(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/personnamecomponents%28from%3A%29.json'
content_hash: 'sha256:6fbabb2924eecdc3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# personNameComponents(from:)

<sub>Instance Method</sub>

Returns a person name components object from a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func personNameComponents(from string: String) -> PersonNameComponents?
```

## Parameters

- `string` — A string that is parsed to create a person name components object.

## Return Value

An [NSPersonNameComponents](../nspersonnamecomponents.md) object parsing string using the receiver’s format, or `nil` if no components could be parsed.

## Discussion

This method uses a combination of locale rules and heuristics to determine the most likely name components for a particular string representation. Parsing name components from a representation created for an existing name components object may not produce equivalent results.

> [!important] Important
> Currently, only names using Latin or CJK scripts are supported.

Here are some general rules that describe the name component parsing behavior:

- Names in Latin script have components delimited by whitespace.
- Names with a single delimited component are parsed into their most likely name component.
- Names in Latin script with more than two delimited components may include middle components in the `givenName`, `middleName`, or `familyName` name components.
- Names in Latin script that are inverted may be parsed into components in a different order than they appear; names in CJK script that are inverted will not typically produce the correct results.
- Names in Latin script may use a comma to indicate name inversion.
- Names in Latin script have capitalization preserved between string representation and parsed components.
- Text between parentheses or brackets, as well as extraneous characters in names is ignored.

| String | `namePrefix` | `givenName` | `middleName` | `familyName` | `nameSuffix` |
|---|---|---|---|---|---|
| Jonathan Appleseed |  | Jonathan |  | Appleseed |  |
| Jonathan Paul Appleseed |  | Jonathan | Paul | Appleseed |  |
| John Paul Appleseed |  | John Paul |  | Appleseed |  |
| Jonathan P. Appleseed |  | Jonathan | P. | Appleseed |  |
| Dr. Jonathan, Esq. | Dr. | Jonathan |  |  | Esq. |
| jonathan appleseed |  | jonathan |  | appleseed |  |
| Appleseed, Jonathan |  | Jonathan |  | Appleseed |  |
| Appleseed Jonathan |  | Jonathan |  | Appleseed |  |
| APPLESEED Jonathan |  | Jonathan |  | APPLESEED |  |
| Jonathan (a.k.a. Johnny) Appleseed 🍎 |  | Jonathan |  | Appleseed |  |
| 杨振宁 |  | 振宁 |  | 杨 |  |
| Jean-Philippe de Zélicourt |  | Jean-Philippe |  | de Zélicourt |  |
| Max Mustermann |  | Max |  | Mustermann |  |
| 木田泰夫 |  | 泰夫 |  | 木田 |  |
| José Ramiro Martín González de Rivera |  | José | Ramiro | Martín González de Rivera |  |

## See Also

### Converting Between Person Name Components and Strings

- [+ localizedStringFromPersonNameComponents:style:options:](<localizedstring(from_style_options_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [- stringFromPersonNameComponents:](<string(from_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object.
- [- annotatedStringFromPersonNameComponents:](<annotatedstring(from_).md>) — Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — Returns by reference a person name components object after creating it from a given string.
