---
title: 'padding(toLength:withPad:startingAt:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/padding(tolength:withpad:startingat:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/padding(tolength:withpad:startingat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/padding%28tolength%3Awithpad%3Astartingat%3A%29.json'
content_hash: 'sha256:d1c68b121c4def24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# padding(toLength:withPad:startingAt:)

<sub>Instance Method</sub>

Returns a new string formed from the receiver by either removing characters from the end, or by appending as many occurrences as necessary of a given pad string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func padding(toLength newLength: Int, withPad padString: String, startingAt padIndex: Int) -> String
```

## Parameters

- `newLength` — The new length for the receiver.

- `padString` — The string with which to extend the receiver.

- `padIndex` — The index in `padString` from which to start padding.

## Return Value

A new string formed from the receiver by either removing characters from the end, or by appending as many occurrences of `padString` as necessary.

## Discussion

Here are some examples of usage:

```objc
[@"abc" stringByPaddingToLength: 9 withString: @"." startingAtIndex:0];
    // Results in "abc......"
 
[@"abc" stringByPaddingToLength: 2 withString: @"." startingAtIndex:0];
    // Results in "ab"
 
[@"abc" stringByPaddingToLength: 9 withString: @". " startingAtIndex:1];
    // Results in "abc . . ."
    // Notice that the first character in the padding is " "
```

## See Also

### Combining Strings

- [appendingFormat(_:_:)](<appendingformat(____).md>)
- [- stringByAppendingString:](<appending(__).md>) — Returns a new string made by appending a given string to the receiver.
