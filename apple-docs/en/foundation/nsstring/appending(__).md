---
title: 'appending(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/appending(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/appending(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/appending%28_%3A%29.json'
content_hash: 'sha256:288086d6b5d119f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# appending(_:)

<sub>Instance Method</sub>

Returns a new string made by appending a given string to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func appending(_ aString: String) -> String
```

## Parameters

- `aString` — The string to append to the receiver. This value must not be `nil`. > [!important] Important > Raises an `NSInvalidArgumentException` if `aString` is `nil`.

## Return Value

A new string made by appending `aString` to the receiver.

## Discussion

This code excerpt, for example:

```objc
NSString *errorTag = @"Error: ";
NSString *errorString = @"premature end of file.";
NSString *errorMessage = [errorTag stringByAppendingString:errorString];
```

produces the string “`Error: premature end of file.`”.

## See Also

### Combining Strings

- [appendingFormat(_:_:)](<appendingformat(____).md>)
- [- stringByPaddingToLength:withString:startingAtIndex:](<padding(tolength_withpad_startingat_).md>) — Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.
