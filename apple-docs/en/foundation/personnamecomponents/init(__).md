---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponents/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponents/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponents/init%28_%3A%29.json'
content_hash: 'sha256:da8dc41fe188d5dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponents](../personnamecomponents.md)

# init(_:)

<sub>Initializer</sub>

Creates a person name components object from a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ value: String) throws
```

## Parameters

- `value` — A string to parse into name components.

## Discussion

This initializer uses a combination of locale rules and heuristics to determine the most likely name components for a particular string representation. Parsing name components from a representation created for an existing name components object may not produce equivalent results.

> [!important] Important
> Only names using Latin or CJK scripts are supported.

Here are some general rules that describe the name component parsing behavior:

- Names in Latin script have components delimited by whitespace.
- The format style parses names with a single delimited component into their most likely name component.
- Names in Latin script with more than two delimited components may include middle components in the `givenName`, `middleName`, or `familyName` name components.
- The format style may parse names in inverted Latin script into components in a different order than they appear. Inverted names in CJK script won’t typically produce the correct results.
- Names in Latin script may use a comma to indicate name inversion.
- Names in Latin script have capitalization preserved between string representation and parsed components.
- The format style ignores text between parentheses or brackets, as well as extraneous characters in names.

| String | Name prefix | Given name | Middle name | Family name | Name suffix |
|---|---|---|---|---|---|
| Thomas Clark |  | Thomas |  | Clark |  |
| Thomas Louis Clark |  | Thomas | Louis | Clark |  |
| Tom Louis Appleseed |  | Tom Louis |  | Clark |  |
| Thomas L. Appleseed |  | Thomas | L. | Clark |  |
| Dr. Thomas, Esq. | Dr. | Thomas |  |  | Esq. |
| thomas clark |  | thomas |  | clark |  |
| Clark, Thomas |  | Thomas |  | Clark |  |
| Clark Thomas |  | Thomas |  | Clark |  |
| CLARK Thomas |  | Thomas |  | CLARK |  |
| Thomas (a.k.a. Tom) Clark 🍎 |  | Thomas |  | Clark |  |
| 杨振宁 |  | 振宁 |  | 杨 |  |
| Jean-Philippe de Zélicourt |  | Jean-Philippe |  | de Zélicourt |  |
| Max Mustermann |  | Max |  | Mustermann |  |
| 木田泰夫 |  | 泰夫 |  | 木田 |  |
| José Ramiro Martín González de Rivera |  | José | Ramiro | Martín González de Rivera |  |

## See Also

### Parsing Person Name Components

- [init(_:strategy:)](<init(__strategy_).md>) — Creates a person name components object from a given string by applying the provided parsing strategy.
- [parseStrategy](formatstyle/parsestrategy.md) — The strategy used to parse a string into person name components.
