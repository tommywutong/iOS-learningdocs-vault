---
title: 'random(in:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/int/random(in:)-8zzqh'
source_url: 'https://developer.apple.com/documentation/swift/int/random(in:)-8zzqh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/int/random%28in%3A%29-8zzqh.json'
content_hash: 'sha256:085475b5f1d083e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Int](../int.md)

# random(in:)

<sub>Type Method</sub>

Returns a random value within the specified range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func random(in range: ClosedRange<Self>) -> Self
```

## Parameters

- `range` — The range in which to create a random value.

## Return Value

A random value within the bounds of `range`.

## Discussion

Use this method to generate an integer within a specific range. This example creates three new values in the range `1...100`.

```swift
for _ in 1...3 {
    print(Int.random(in: 1...100))
}
// Prints "53"
// Prints "64"
// Prints "5"
```

This method is equivalent to calling `random(in:using:)`, passing in the system’s default random generator.

## See Also

### Creating a Random Integer

- [random(in:)](<random(in_)-9mjpw.md>) — Returns a random value within the specified range.
- [random(in:using:)](<random(in_using_)-4lsb5.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
- [random(in:using:)](<random(in_using_)-3dwv4.md>) — Returns a random value within the specified range, using the given generator as a source for randomness.
