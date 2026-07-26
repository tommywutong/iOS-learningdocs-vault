---
title: 'annotatedString(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponentsformatter/annotatedstring(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/annotatedstring(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/annotatedstring%28from%3A%29.json'
content_hash: 'sha256:81b829d02980f938'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# annotatedString(from:)

<sub>Instance Method</sub>

Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func annotatedString(from components: PersonNameComponents) -> NSAttributedString
```

## Parameters

- `components` — A formatted string representation of the given name components.

## Return Value

An attributed string representation of the given name components. You can determine the person component corresponding to a particular range of the attributed string by querying the `NSPersonNameComponentKey` attribute, providing one of the `NSPersonNameComponent` constant values defined below as the attribute value.

## Discussion

Use this method to style individual components of a formatted name, such as a name in a label.

## See Also

### Converting Between Person Name Components and Strings

- [+ localizedStringFromPersonNameComponents:style:options:](<localizedstring(from_style_options_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [- stringFromPersonNameComponents:](<string(from_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object.
- [- personNameComponentsFromString:](<personnamecomponents(from_).md>) — Returns a person name components object from a given string.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — Returns by reference a person name components object after creating it from a given string.
