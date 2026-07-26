---
title: 'componentsJoined(by:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsarray/componentsjoined(by:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsarray/componentsjoined(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsarray/componentsjoined%28by%3A%29.json'
content_hash: 'sha256:953a4ac4800435fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSArray](../nsarray.md)

# componentsJoined(by:)

<sub>Instance Method</sub>

Constructs and returns an `NSString` object that is the result of interposing a given separator between the elements of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func componentsJoined(by separator: String) -> String
```

## Parameters

- `separator` — The string to interpose between the elements of the array.

## Return Value

An `NSString` object that is the result of interposing `separator` between the elements of the array. If the array has no elements, returns an `NSString` object representing an empty string.

## Discussion

For example, this code excerpt writes “`here be dragons`” to the console:

```objc
NSArray *pathArray = [NSArray arrayWithObjects:@"here", @"be", @"dragons", nil];
NSLog(@"%@",[pathArray componentsJoinedByString:@" "]);
```

### Special Considerations

Each element in the array must handle `description`.

## See Also

### Related Documentation

- [- componentsSeparatedByString:](<../nsstring/components(separatedby_)-238fy.md>) — Returns an array containing substrings from the receiver that have been divided by a given separator.
