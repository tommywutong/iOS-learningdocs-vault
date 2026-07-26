---
title: 'isPartialStringValid(_:newEditingString:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatter/ispartialstringvalid(_:neweditingstring:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatter/ispartialstringvalid(_:neweditingstring:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/ispartialstringvalid%28_%3Aneweditingstring%3Aerrordescription%3A%29.json'
content_hash: 'sha256:f8b2ba26415e2afe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# isPartialStringValid(_:newEditingString:errorDescription:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a partial string is valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isPartialStringValid(_ partialString: String, newEditingString newString: AutoreleasingUnsafeMutablePointer<NSString?>?, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `partialString` — The text currently in a cell.

- `newString` — If `partialString` needs to be modified, upon return contains the replacement string.

- `error` — If non-`nil`, if validation fails contains an `NSString` object that describes the problem.

## Return Value

[true](../../swift/true.md) if `partialString` is an acceptable value, otherwise [false](../../swift/false.md).

## Discussion

This method is invoked each time the user presses a key while the cell has the keyboard focus—it lets you verify and edit the cell text as the user types it.

In a subclass implementation, evaluate `partialString` according to the context, edit the text if necessary, and return by reference any edited string in `newString`. Return [true](../../swift/true.md) if `partialString` is acceptable and [false](../../swift/false.md) if `partialString` is unacceptable. If you return [false](../../swift/false.md) and `newString` is `nil`, the cell displays `partialString` minus the last character typed. If you return [false](../../swift/false.md), you can also return by indirection an `NSString` object (in `error`) that explains the reason why the validation failed; the delegate (if any) of the `NSControl` object managing the cell can then respond to the failure in control:didFailToValidatePartialString:errorDescription:. The selection range will always be set to the end of the text if replacement occurs.

This method is a compatibility method. If a subclass overrides this method and does not override [- isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:](<ispartialstringvalid(__proposedselectedrange_originalstring_originalselectedrange_errordescription_).md>), this method will be called as before ([- isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:](<ispartialstringvalid(__proposedselectedrange_originalstring_originalselectedrange_errordescription_).md>) just calls this one by default).

## See Also

### Validating Partial Strings

- [- isPartialStringValid:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:](<ispartialstringvalid(__proposedselectedrange_originalstring_originalselectedrange_errordescription_).md>) — This method should be implemented in subclasses that want to validate user changes to a string in a field, where the user changes are not necessarily at the end of the string, and preserve the selection (or set a different one, such as selecting the erroneous part of the string the user has typed).
