---
title: 'string(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponentsformatter/string(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/string(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/string%28from%3A%29.json'
content_hash: 'sha256:17ece6f4697c9be0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# string(from:)

<sub>Instance Method</sub>

Returns a string formatted for a given `NSPersonNameComponents` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(from components: PersonNameComponents) -> String
```

## Parameters

- `components` — The name components to be formatted.

## Return Value

A formatted string representation of the given name components.

## See Also

### Converting Between Person Name Components and Strings

- [+ localizedStringFromPersonNameComponents:style:options:](<localizedstring(from_style_options_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [- annotatedStringFromPersonNameComponents:](<annotatedstring(from_).md>) — Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [- personNameComponentsFromString:](<personnamecomponents(from_).md>) — Returns a person name components object from a given string.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — Returns by reference a person name components object after creating it from a given string.
