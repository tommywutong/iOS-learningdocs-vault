---
title: 'getObjectValue(_:for:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/numberformatter/getobjectvalue(_:for:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/numberformatter/getobjectvalue(_:for:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/numberformatter/getobjectvalue%28_%3Afor%3Arange%3A%29.json'
content_hash: 'sha256:d5a8b9c243793ece'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NumberFormatter](../numberformatter.md)

# getObjectValue(_:for:range:)

<sub>Instance Method</sub>

Returns by reference a cell-content object after creating it from a range of characters in a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, range rangep: UnsafeMutablePointer<NSRange>?) throws
```

## Parameters

- `obj` — On return, contains an instance of [NSDecimalNumber](../nsdecimalnumber.md) or [NSNumber](../nsnumber.md) based on the current value of the [generatesDecimalNumbers](generatesdecimalnumbers.md) property. Returns `nil` by reference if conversion failed.

- `string` — A string object with the range of characters specified in `rangep` that is used to create `anObject`.

- `rangep` — A range of characters in `aString`. On return, contains the actual range of characters used to create the object.

## Discussion

If a string contains any characters other than numerical digits or locale-appropriate group or decimal separators, parsing will fail.

Any leading or trailing space separator characters in a string are ignored. For example, the strings “ 5”, “5 “, and “5” all produce the number `5`.

If there is an error, this method calls `control(_:didFailToFormatString:errorDescription:)` on the delegate.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Converting Between Numbers and Strings

- [- numberFromString:](<number(from_).md>) — Returns an [NSNumber](../nsnumber.md) object created by parsing a given string.
- [- stringFromNumber:](<string(from_).md>) — Returns a string containing the formatted value of the provided number object.
- [+ localizedStringFromNumber:numberStyle:](<localizedstring(from_number_).md>) — Returns a localized number string with the specified style.
