---
title: AnyClass
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/anyclass
source_url: 'https://developer.apple.com/documentation/swift/anyclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyclass.json'
content_hash: 'sha256:e5422f457cfd0a54'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# AnyClass

<sub>Type Alias</sub>

The protocol to which all class types implicitly conform.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias AnyClass = any AnyObject.Type
```

## Discussion

You can use the `AnyClass` protocol as the concrete type for an instance of any class. When you do, all known `@objc` class methods and properties are available as implicitly unwrapped optional methods and properties, respectively. For example:

```swift
class IntegerRef {
    @objc class func getDefaultValue() -> Int {
        return 42
    }
}

func getDefaultValue(_ c: AnyClass) -> Int? {
    return c.getDefaultValue?()
}
```

The `getDefaultValue(_:)` function uses optional chaining to safely call the implicitly unwrapped class method on `c`. Calling the function with different class types shows how the `getDefaultValue()` class method is only conditionally available.

```swift
print(getDefaultValue(IntegerRef.self))
// Prints "Optional(42)"

print(getDefaultValue(NSString.self))
// Prints "nil"
```

## See Also

### Existential Types

- [AnyObject](anyobject.md) — The protocol to which all classes implicitly conform.
