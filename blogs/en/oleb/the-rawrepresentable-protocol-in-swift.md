---
title: The RawRepresentable Protocol in Swift
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2016/11/rawrepresentable/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:2ceb9794e17e7210'
translated: false
---

> 原文：[The RawRepresentable Protocol in Swift](https://oleb.net/blog/2016/11/rawrepresentable/)　·　Ole Begemann

# The RawRepresentable Protocol in Swift

**The raw value syntax for enums in Swift is “just” a shorthand for conformance to the `RawRepresentable` protocol. It’s easy to add this manually if you want to use otherwise unsupported types as raw values.**

When you define an enum in Swift, you can choose to have each enum case [“backed” by a _raw value_](https://developer.apple.com/library/content/documentation/Swift/Conceptual/Swift_Programming_Language/Enumerations.html#//apple_ref/doc/uid/TP40014097-CH12-ID149). For example, here’s an enum that models the terrain type of a map tile in a game, and each case has a raw value of type [`String`](https://developer.apple.com/reference/swift/string) (perhaps because these values are used to encode the information on disk):

```
enum Terrain: String {
    case forest = "F"
    case mountain = "M"
    case water = "W"
}
```

You can access an instance’s raw value through the [`rawValue`](https://developer.apple.com/reference/swift/rawrepresentable/1540698-rawvalue) property, and there’s a failable initializer to construct an enum value from a raw value (the initializer returns `nil` if you pass in an invalid raw value).

# Raw values don’t change how enums are stored

Note that adding raw values to an enum doesn’t affect how the enum [is laid out in memory](https://github.com/apple/swift/blob/master/docs/ABI.rst#fragile-enum-layout). The compiler always determines how many bits it needs to discriminate between all enum cases and then assigns a unique integer tag value to each case. Even for enums with integer raw values, this tag is not the same as the raw value — they are completely different things. This also means you don’t have to worry that an enum with strings as raw values will take up more memory than a “plain” enum — the constant strings are only stored once in the binary, not for each instance.

We can test this by checking the size in memory of a `Terrain` value: it’s 1 byte. (Theoretically, an enum with three cases requires only 2 _bits_ of storage, but every value occupies a multiple of 1 byte.) In contrast, a `String` containing the corresponding raw value takes up 24 bytes (plus the actual storage for the string’s contents, but that’s statically located in the binary in both cases):^[1](#fn:1)

```
MemoryLayout.size(ofValue: Terrain.forest) // → 1 (byte)
MemoryLayout.size(ofValue: "F") // → 24 (bytes)
```

# Syntactic sugar for RawRepresentable conformance

In fact, the raw value syntax is simply shorthand for conforming the enum to the [`RawRepresentable`](https://developer.apple.com/reference/swift/rawrepresentable) protocol, which defines the `rawValue` property and initializer. When you define the above enum, the compiler generates code equivalent to this:

```
enum Terrain {
    case forest
    case mountain
    case water
}

extension Terrain: RawRepresentable {
    typealias RawValue = String

    init?(rawValue: RawValue) {
        switch rawValue {
        case "F": self = .forest
        case "M": self = .mountain
        case "W": self = .water
        default: return nil
        }
    }

    var rawValue: RawValue {
        switch self {
        case .forest: return "F"
        case .mountain: return "M"
        case .water: return "W"
        }
    }
}
```

This does exactly the same as the shorthand syntax and should make clear that the raw values don’t affect the enum’s storage.

# More options with manual conformance

Once you realize that there’s no magic behind enums with raw values, it opens up the possibility to use all kinds of types as raw values. In the shorthand syntax, raw values can only be `String`, `Character`, or any integer or floating-point number type. Moreover, the values you provide must be literals, i.e. they must be statically known at compile time.

The `RawRepresentable` protocol has no such limitation — its [`RawValue`](https://developer.apple.com/reference/swift/rawrepresentable/rawvalue) associated type can be anything, and the actual raw values can be created dynamically at runtime. Take this example of an enum for modeling colors, backed by their correspoding [`UIColor`](https://developer.apple.com/reference/uikit/uicolor) values:

```
import UIKit

// Can’t use the shorthand syntax for UIColor raw values
enum Color {
    case red
    case green
    case blue
}

// But it’s no problem with manual RawRepresentable conformance
extension Color: RawRepresentable {
    typealias RawValue = UIColor

    init?(rawValue: RawValue) {
        switch rawValue {
        case UIColor.red: self = .red
        case UIColor.green: self = .green
        case UIColor.blue: self = .blue
        default: return nil
        }
    }

    var rawValue: RawValue {
        switch self {
        case .red: return UIColor.red
        case .green: return UIColor.green
        case .blue: return UIColor.blue
        }
    }
}

// Access a color's rawValue
Color.blue.rawValue is UIColor
// → true
```

# RawRepresentable is more than just enums

`RawRepresentable` isn’t limited to enums. It can also make sense for structs and classes to add conformance. [Option sets](https://oleb.net/blog/2016/09/swift-option-sets/) also make use of the protocol (`OptionSet` inherits from `RawRepresentable`).

1. In our case, since the string value is statically known at compile time, we could use a [`StaticString`](https://developer.apple.com/reference/swift/staticstring), which is only 17 bytes big and not 24. Or we could use a [`Character`](https://developer.apple.com/reference/swift/character) (9 bytes) since our string contains only a single character. In any case, it’s still much bigger than the enum. You get the idea. [↩︎](#fnref:1)
