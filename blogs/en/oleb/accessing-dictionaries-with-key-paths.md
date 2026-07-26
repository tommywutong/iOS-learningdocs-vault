---
title: Accessing Dictionaries with Key Paths
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/01/dictionary-key-paths/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:fa406c2c63585d99'
translated: false
---

> 原文：[Accessing Dictionaries with Key Paths](https://oleb.net/blog/2017/01/dictionary-key-paths/)　·　Ole Begemann

# Accessing Dictionaries with Key Paths

In [Swift Talk episode 31](https://talk.objc.io/episodes/S01E31-mutating-untyped-dictionaries), Chris and Florian present a solution for mutating nested, heterogeneous dictionaries of type `[String: Any]` in Swift. It’s an interesting discussion, I encourage you to watch it or read the excellent transcript.

I helped a little in the preparation of the episode and while experimenting with this problem developed something that ultimately didn’t make it into the video, so I’d like to show it to you here.

# A heterogeneous dictionary

We start with a heterogeneous dictionary with multiple nesting levels. You would typically encounter this as JSON data you got from a web service or perhaps a configuration loaded from a [plist](https://en.wikipedia.org/wiki/Property_list) file:

```
var dict: [String: Any] = [
    "language": "de",
    "translator": "Erika Fuchs",
    "translations": [
        "characters": [
            "Scrooge McDuck": "Dagobert",
            "Huey": "Tick",
            "Dewey": "Trick",
            "Louie": "Track",
            "Gyro Gearloose": "Daniel Düsentrieb",
        ],
        "places": [
            "Duckburg": "Entenhausen",
            "Money Bin": "Geldspeicher",
        ]
    ]
]
```

Florian and Chris’s solution allows you to access (and mutate) a nested value in the dictionary with this syntax:

```
dict[jsonDict: "translations"]?[jsonDict: "characters"]?[string: "Gyro Gearloose"]
// → "Daniel Düsentrieb"
```

# Using a key path to subscript a dictionary

I’d like to introduce a syntax that is as close as possible to the key paths used in [key-value coding](https://developer.apple.com/library/content/documentation/Cocoa/Conceptual/KeyValueCoding/BasicPrinciples.html#//apple_ref/doc/uid/20002170-BAJEAIEE) in Cocoa. The end result should look like this:

```
dict[keyPath: "translations.characters.Gyro Gearloose"]
// → "Daniel Düsentrieb"
```

We can’t use Swift’s existing [`#keyPath` construct](https://github.com/apple/swift-evolution/blob/master/proposals/0062-objc-keypaths.md) for this because it performs a compile-time check that the properties the key path references exist, which is not possible with dictionaries.

## The `KeyPath` type

Let’s start by introducing a new type to represent a key path. It stores the key path as an array of path segments and has a convenience method for striping off the first path segment, which will come in handy later.

```
struct KeyPath {
    var segments: [String]

    var isEmpty: Bool { return segments.isEmpty }
    var path: String {
        return segments.joined(separator: ".")
    }

    /// Strips off the first segment and returns a pair
    /// consisting of the first segment and the remaining key path.
    /// Returns nil if the key path has no segments.
    func headAndTail() -> (head: String, tail: KeyPath)? {
        guard !isEmpty else { return nil }
        var tail = segments
        let head = tail.removeFirst()
        return (head, KeyPath(segments: tail))
    }
}
```

Putting this functionality into a custom type is not strictly necessary; after all, we’re dealing with [stringly typed](http://wiki.c2.com/?StringlyTyped) data anyway, so there isn’t much type-safety to be gained here. It’s convenient to extract the string parsing code so we don’t have to deal with it in the dictionary subscript, though.

Speaking of parsing, we need an initializer that takes a key path string and converts it into the internal array representation:

```
import Foundation

/// Initializes a KeyPath with a string of the form "this.is.a.keypath"
extension KeyPath {
    init(_ string: String) {
        segments = string.components(separatedBy: ".")
    }
}
```

The next step is adding conformance to [`ExpressibleByStringLiteral`](https://developer.apple.com/reference/swift/expressiblebystringliteral). This allows us to create a key path with a plain string literal like `"this.is.a.key.path"`. The protocol has three required initializers, all of which forward to the initializer we just wrote:

```
extension KeyPath: ExpressibleByStringLiteral {
    init(stringLiteral value: String) {
        self.init(value)
    }
    init(unicodeScalarLiteral value: String) {
        self.init(value)
    }
    init(extendedGraphemeClusterLiteral value: String) {
        self.init(value)
    }
}
```

## The `Dictionary` subscript

Now it’s time to write the extension for [`Dictionary`](https://developer.apple.com/reference/swift/dictionary). Key paths only make sense for dictionaries whose keys are strings. Unfortunately, extensions that constrain a generic type parameter to a concrete type, as in `extension Dictionary where Key == String`, are not supported in Swift 3.0. This feature [has already been implemented](https://bugs.swift.org/browse/SR-1009) and will be part of Swift 3.1, though.

Until then, we can work around the limitation by introducing a dummy protocol and conforming `String` to it:

```
// Needed because Swift 3.0 doesn't support extensions with concrete
// same-type requirements (extension Dictionary where Key == String).
protocol StringProtocol {
    init(string s: String)
}

extension String: StringProtocol {
    init(string s: String) {
        self = s
    }
}
```

Now we can constrain our extension with `where Key: StringProtocol`. We’re going to add a subscript to `Dictionary` that takes a key path and returns an optional value of type `Any`. The subscript needs a getter and setter because we want to be able to mutate the dictionary through the key path syntax:

```
extension Dictionary where Key: StringProtocol {
    subscript(keyPath keyPath: KeyPath) -> Any? {
        get {
            // ...
        }
        set {
            // ...
        }
    }
}
```

Here’s the implementation for the getter:

```
extension Dictionary where Key: StringProtocol {
    subscript(keyPath keyPath: KeyPath) -> Any? {
        get {
            switch keyPath.headAndTail() {
            case nil:
                // key path is empty.
                return nil
            case let (head, remainingKeyPath)? where remainingKeyPath.isEmpty:
                // Reached the end of the key path.
                let key = Key(string: head)
                return self[key]
            case let (head, remainingKeyPath)?:
                // Key path has a tail we need to traverse.
                let key = Key(string: head)
                switch self[key] {
                case let nestedDict as [Key: Any]:
                    // Next nest level is a dictionary.
                    // Start over with remaining key path.
                    return nestedDict[keyPath: remainingKeyPath]
                default:
                    // Next nest level isn't a dictionary.
                    // Invalid key path, abort.
                    return nil
                }
            }
        }
        // ...
```

It has to handle four cases:

1. If the key path is empty, return `nil`. This should only happen if we get called with an empty key path.
2. If the key path has only one segment, use the standard [dictionary subscript](https://developer.apple.com/reference/swift/dictionary/1540848-subscript) to return the value for this key (or `nil` if the key doesn’t exist).
3. If the key path has more than one segment, check if there is a nested dictionary we can traverse down into. If so, call the subscript recursively with the remaining path segments.
4. If there isn’t a nested dictionary, the key path is malformed. Return `nil`.

The setter has a very similar structure:

```
extension Dictionary where Key: StringProtocol {
    subscript(keyPath keyPath: KeyPath) -> Any? {
        // ...
        set {
            switch keyPath.headAndTail() {
            case nil:
                // key path is empty.
                return
            case let (head, remainingKeyPath)? where remainingKeyPath.isEmpty:
                // Reached the end of the key path.
                let key = Key(string: head)
                self[key] = newValue as? Value
            case let (head, remainingKeyPath)?:
                let key = Key(string: head)
                let value = self[key]
                switch value {
                case var nestedDict as [Key: Any]:
                    // Key path has a tail we need to traverse
                    nestedDict[keyPath: remainingKeyPath] = newValue
                    self[key] = nestedDict as? Value
                default:
                    // Invalid keyPath
                    return
                }
            }
        }
    }
}
```

This is quite a lot of code, but it’s all nicely tucked away in an extension. And the end result reads very nicely at the call site, which ultimately is [what matters](https://swift.org/documentation/api-design-guidelines/).

> Clarity at the point of use is your most important goal.

— [Swift API Design Guidelines](https://swift.org/documentation/api-design-guidelines/)

Here’s an example:

```
dict[keyPath: "translations.characters.Gyro Gearloose"]
// → "Daniel Düsentrieb"
dict[keyPath: "translations.characters.Magica De Spell"] = "Gundel Gaukeley"
dict[keyPath: "translations.characters.Magica De Spell"]
// → "Gundel Gaukeley"
```

We can access values and also assign new values.

## Mutating methods

The return type of our subscript is `Any?`. This means you’ll usually have to cast the return value before you can do anything useful with it. This is no different than the default subscript on a heterogeneous dictionary whose `Value` type is `Any`.

As Chris and Florian [show at length in the video](https://talk.objc.io/episodes/S01E31-mutating-untyped-dictionaries), one implication is that _mutating_ a value in the dictionary (as opposed to assigning a new value) becomes very difficult because you can’t mutate values through a cast. Neither of these lines compile:

```
// error: value of type 'Any' has no member 'append'
dict[keyPath: "translations.characters.Scrooge McDuck"]?.append(" Duck")

// error: cannot use mutating member on immutable value of type 'String'
(dict[keyPath: "translations.characters.Scrooge McDuck"] as? String)?.append(" Duck")
```

To make this work, we need a subscript that returns a `String?`. The best solution for this would be to make our subscript generic, but [generic subscripts are not supported](https://bugs.swift.org/browse/SR-115). The next best approach is to provide additional subscripts with different argument labels for the types we want to support. The implementation can forward to the existing subscript, but the downside is that we have to add these manually for each required type. Here are two variants for strings and dictionaries:

```
extension Dictionary where Key: StringProtocol {
    subscript(string keyPath: KeyPath) -> String? {
        get { return self[keyPath: keyPath] as? String }
        set { self[keyPath: keyPath] = newValue }
    }

    subscript(dict keyPath: KeyPath) -> [Key: Any]? {
        get { return self[keyPath: keyPath] as? [Key: Any] }
        set { self[keyPath: keyPath] = newValue }
    }
}
```

And now this works:

```
dict[string: "translations.characters.Scrooge McDuck"]?.append(" Duck")
dict[keyPath: "translations.characters.Scrooge McDuck"]
// → "Dagobert Duck"

dict[dict: "translations.places"]?.removeAll()
dict[keyPath: "translations.places"]
// → [:]
```

# Conclusion

If you routinely work with weakly typed heterogeneous dictionaries, you should question your data model. In most situations it’s probably a better idea to transform such data into custom structs or enums that match your domain model and provide more type safety.

However, in the rare case where a full data model would be overkill, I really like the flexibility and readability of the approach I presented here.
