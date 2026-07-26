---
title: 'isPartialStringValid(_:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:)'
source_url: 'https://developer.apple.com/documentation/foundation/formatter/ispartialstringvalid(_:proposedselectedrange:originalstring:originalselectedrange:errordescription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/formatter/ispartialstringvalid%28_%3Aproposedselectedrange%3Aoriginalstring%3Aoriginalselectedrange%3Aerrordescription%3A%29.json'
content_hash: 'sha256:a9a0b10238a1a030'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Formatter](../formatter.md)

# isPartialStringValid(_:proposedSelectedRange:originalString:originalSelectedRange:errorDescription:)

<sub>Instance Method</sub>

This method should be implemented in subclasses that want to validate user changes to a string in a field, where the user changes are not necessarily at the end of the string, and preserve the selection (or set a different one, such as selecting the erroneous part of the string the user has typed).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isPartialStringValid(_ partialStringPtr: AutoreleasingUnsafeMutablePointer<NSString>, proposedSelectedRange proposedSelRangePtr: NSRangePointer?, originalString origString: String, originalSelectedRange origSelRange: NSRange, errorDescription error: AutoreleasingUnsafeMutablePointer<NSString?>?) -> Bool
```

## Parameters

- `partialStringPtr` — The new string to validate.

- `proposedSelRangePtr` — The selection range that will be used if the string is accepted or replaced.

- `origString` — The original string, before the proposed change.

- `origSelRange` — The selection range over which the change is to take place. If the user change is a deletion, `origSelRange` contains the range of the deleted characters.

- `error` — If non-`nil`, if validation fails contains an `NSString` object that describes the problem.

## Return Value

[true](../../swift/true.md) if `partialStringPtr` is acceptable, otherwise [false](../../swift/false.md).

## Discussion

In a subclass implementation, evaluate `partialString` according to the context. Return [true](../../swift/true.md) if `partialStringPtr` is acceptable and [false](../../swift/false.md) if `partialStringPtr` is unacceptable. If you return [false](../../swift/false.md) and assign a new string to `partialStringPtr` and a new range to `proposedSelRangePtr`, the string and selection range are changed, otherwise, if no values are assigned to `partialStringPtr` or `proposedSelRangePtr`, the change is rejected. If you return [false](../../swift/false.md), you can also return by indirection an `NSString` object (in `error`) that explains the reason why the validation failed; the delegate (if any) of the `NSControl` object managing the cell can then respond to the failure in control:didFailToValidatePartialString:errorDescription:.

## See Also

### Validating Partial Strings

- [- isPartialStringValid:newEditingString:errorDescription:](<ispartialstringvalid(__neweditingstring_errordescription_).md>) — Returns a Boolean value that indicates whether a partial string is valid.
