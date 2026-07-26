---
title: 'components(separatedBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/components(separatedby:)-8gl9t'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/components(separatedby:)-8gl9t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/components%28separatedby%3A%29-8gl9t.json'
content_hash: 'sha256:4567c14cb6f510c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# components(separatedBy:)

<sub>Instance Method</sub>

Returns an array containing substrings from the string that have been divided by the given separator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func components<T>(separatedBy separator: T) -> [String] where T : StringProtocol
```

## Parameters

- `separator` — The separator string.

## Return Value

An array containing substrings that have been divided from the string using `separator`.

## Discussion

The substrings in the resulting array appear in the same order as the original string. Adjacent occurrences of the separator string produce empty strings in the result. Similarly, if the string begins or ends with the separator, the first or last substring, respectively, is empty. The following example shows this behavior:

```swift
let list1 = "Karin, Carrie, David"
let items1 = list1.components(separatedBy: ", ")
// ["Karin", "Carrie", "David"]

// Beginning with the separator:
let list2 = ", Norman, Stanley, Fletcher"
let items2 = list2.components(separatedBy: ", ")
// ["", "Norman", "Stanley", "Fletcher"
```

If the list has no separators, the array contains only the original string itself.

```swift
let name = "Karin"
let list = name.components(separatedBy: ", ")
// ["Karin"]
```
