---
title: 'localizedString(from:style:options:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponentsformatter/localizedstring(from:style:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/localizedstring(from:style:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/localizedstring%28from%3Astyle%3Aoptions%3A%29.json'
content_hash: 'sha256:a376d59502a6a210'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# localizedString(from:style:options:)

<sub>Type Method</sub>

Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedString(from components: PersonNameComponents, style nameFormatStyle: PersonNameComponentsFormatter.Style, options nameOptions: PersonNameComponentsFormatter.Options = []) -> String
```

## Parameters

- `components` — The name components to be formatted.

- `nameFormatStyle` — A format style for the name components. For possible values, see [Style](style-swift.enum.md).

- `nameOptions` — The formatting options for the name components. For possible values, see [Options](options.md).

## Return Value

A formatted string representation of the given name components.

## Discussion

This method is a convenience for formatting name components without creating an instance of `NSPersonNameComponentsFormatter`. For greater customizability, you can create an instance of `NSPersonNameComponentsFormatter` and use [- stringFromPersonNameComponents:](<string(from_).md>) instead.

## See Also

### Converting Between Person Name Components and Strings

- [- stringFromPersonNameComponents:](<string(from_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object.
- [- annotatedStringFromPersonNameComponents:](<annotatedstring(from_).md>) — Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [- personNameComponentsFromString:](<personnamecomponents(from_).md>) — Returns a person name components object from a given string.
- [- getObjectValue:forString:errorDescription:](<getobjectvalue(__for_errordescription_).md>) — Returns by reference a person name components object after creating it from a given string.
