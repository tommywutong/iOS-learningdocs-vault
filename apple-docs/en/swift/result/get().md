---
title: get()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/result/get()
source_url: 'https://developer.apple.com/documentation/swift/result/get()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/get%28%29.json'
content_hash: 'sha256:bed86da83f241a29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# get()

<sub>Instance Method</sub>

Returns the success value as a throwing expression.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func get() throws(Failure) -> Success
```

## Return Value

The success value, if the instance represents a success.

## Discussion

Use this method to retrieve the value of this result if it represents a success, or to catch the value if it represents a failure.

```swift
let integerResult: Result<Int, Error> = .success(5)
do {
    let value = try integerResult.get()
    print("The value is \(value).")
} catch {
    print("Error retrieving the value: \(error)")
}
// Prints "The value is 5."
```

> [!danger] Throws
> The failure value, if the instance represents a failure.
