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
doc_path: '/documentation/foundation/dateformatter/getobjectvalue(_:for:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/dateformatter/getobjectvalue(_:for:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/dateformatter/getobjectvalue%28_%3Afor%3Arange%3A%29.json'
content_hash: 'sha256:a93e201a19af6629'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [DateFormatter](../dateformatter.md)

# getObjectValue(_:for:range:)

<sub>Instance Method</sub>

Returns by reference a date representation of a specified string and its date range, as well as a Boolean value that indicates whether the system can parse the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func getObjectValue(_ obj: AutoreleasingUnsafeMutablePointer<AnyObject?>?, for string: String, range rangep: UnsafeMutablePointer<NSRange>?) throws
```

## Parameters

- `obj` — If the receiver is able to parse `string`, upon return contains a date representation of `string`.

- `string` — The string to parse.

- `rangep` — If the receiver is able to parse `string`, upon return contains the range of `string` used to create the date.

## Discussion

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- stringForObjectValue:](<../formatter/string(for_).md>) — The default implementation of this method raises an exception.

### Converting Objects

- [- dateFromString:](<date(from_).md>) — Returns a date representation of a specified string that the system interprets using the receiver’s current settings.
- [- stringFromDate:](<string(from_).md>) — Returns a string representation of a specified date that the system formats using the receiver’s current settings.
- [+ localizedStringFromDate:dateStyle:timeStyle:](<localizedstring(from_datestyle_timestyle_).md>) — Returns a string representation of a specified date, that the system formats for the current locale using the specified date and time styles.
