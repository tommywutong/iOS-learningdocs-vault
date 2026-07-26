---
title: 'getObjectValue(_:for:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/personnamecomponentsformatter/getobjectvalue(_:for:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/getobjectvalue(_:for:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/personnamecomponentsformatter/getobjectvalue%28_%3Afor%3Aerrordescription%3A%29.json'
content_hash: 'sha256:be638724f98a2cc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [PersonNameComponentsFormatter](../personnamecomponentsformatter.md)

# getObjectValue(_:for:errorDescription:)

<sub>Instance Method</sub>

Returns by reference a person name components object after creating it from a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `obj` — On return, contains an instance of [NSPersonNameComponents](../nspersonnamecomponents.md), or `nil` if conversion failed.

- `string` — A string that is parsed to create a person name components object.

- `error` — If an error occurs, upon return contains an [NSError](../nserror.md) object in the [NSCocoaErrorDomain](../nscocoaerrordomain.md) with code [NSFormattingError](../nsformattingerror-swift.var.md) that explains why the conversion failed. If you pass in `nil` for error, you are indicating that you are not interested in error information.

## Return Value

[true](../../swift/true.md) if conversion succeeded; otherwise [false](../../swift/false.md).

## See Also

### Converting Between Person Name Components and Strings

- [+ localizedStringFromPersonNameComponents:style:options:](<localizedstring(from_style_options_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object using the provided style and options.
- [- stringFromPersonNameComponents:](<string(from_).md>) — Returns a string formatted for a given `NSPersonNameComponents` object.
- [- annotatedStringFromPersonNameComponents:](<annotatedstring(from_).md>) — Returns an attributed string formatted for a given `NSPersonNameComponents` object, with attribute annotations for each component.
- [- personNameComponentsFromString:](<personnamecomponents(from_).md>) — Returns a person name components object from a given string.
