---
title: 'remainderReportingOverflow(dividingBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/remainderreportingoverflow(dividingby:)'
source_url: 'https://developer.apple.com/documentation/swift/int/remainderreportingoverflow(dividingby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/remainderreportingoverflow%28dividingby%3A%29.json'
content_hash: 'sha256:f07c00be594c0b9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# remainderReportingOverflow(dividingBy:)

<sub>Instance Method</sub>

Returns the remainder after dividing this value by the given value, along with a Boolean value indicating whether overflow occurred during division.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remainderReportingOverflow(dividingBy other: Int) -> (partialValue: Int, overflow: Bool)
```

## Return Value

A tuple containing the result of the operation along with a Boolean value indicating whether overflow occurred. If the `overflow` component is `false`, the `partialValue` component contains the entire remainder. If the `overflow` component is `true`, an overflow occurred during division and the `partialValue` component contains either the entire remainder or, if the remainder is undefined, the dividend.

## Discussion

Dividing by zero is not an error when using this method. For a value `x`, the result of `x.remainderReportingOverflow(dividingBy: 0)` is `(x, true)`.

## See Also

### Performing Calculations with Overflow

- [addingReportingOverflow(_:)](<addingreportingoverflow(__).md>) — Returns the sum of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [subtractingReportingOverflow(_:)](<subtractingreportingoverflow(__).md>) — Returns the difference obtained by subtracting the given value from this value, along with a Boolean value indicating whether overflow occurred in the operation.
- [multipliedReportingOverflow(by:)](<multipliedreportingoverflow(by_).md>) — Returns the product of this value and the given value, along with a Boolean value indicating whether overflow occurred in the operation.
- [dividedReportingOverflow(by:)](<dividedreportingoverflow(by_).md>) — Returns the quotient obtained by dividing this value by the given value, along with a Boolean value indicating whether overflow occurred in the operation.
