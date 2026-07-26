---
title: Why Dictionary sometimes encodes itself as an array
source: Ole Begemann
source_key: oleb
source_url: 'https://oleb.net/blog/2017/12/dictionary-codable-array/'
original_language: en
published: ''
status: active
license: 未声明 → 仅私有归档
archived_at: 2026-07-26
content_hash: 'sha256:14356216497eef2d'
translated: false
---

> 原文：[Why Dictionary sometimes encodes itself as an array](https://oleb.net/blog/2017/12/dictionary-codable-array/)　·　Ole Begemann

# Why Dictionary sometimes encodes itself as an array

_This is a writeup of [a Twitter conversation](https://twitter.com/olebegemann/status/937744585190764546)._

You may have noticed that some [dictionaries](https://developer.apple.com/documentation/swift/dictionary) encode themselves as arrays in Swift’s [`Codable` system](https://developer.apple.com/documentation/foundation/archives_and_serialization/encoding_and_decoding_custom_types) — or more precisely, as [unkeyed containers](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer), which is `Codable` lingo for an array-like data structure. This is quite surprising; a [keyed container](https://developer.apple.com/documentation/swift/keyedencodingcontainerprotocol) sounds like a much better match for a dictionary.

Here’s an example. Note that the dictionary’s `Key` type is a `String`-backed enum:

```
enum Color: String, Codable {
    case red
    case green
    case blue
}

let dict: [Color : String] = [
    .red: "ff0000",
    .green: "00ff00",
    .blue: "0000ff"
]

import Foundation
let encoder = JSONEncoder()
encoder.outputFormatting = [.prettyPrinted, .sortedKeys]
let encoded = try! encoder.encode(dict)
let jsonText = String(decoding: encoded, as: UTF8.self)
```

This produces **a JSON array** containing both keys and values in alternating order, and **not an object/dictionary** of key-value pairs, as I would have expected:

```
[
  "blue",
  "0000ff",
  "red",
  "ff0000",
  "green",
  "00ff00"
]
```

**Not all dictionaries behave this way, though.** If we replace the enum keys with plain strings, the encoder produces a proper JSON object.

---

So `Dictionary` seems to behave differently depending on its `Key` type, even though the enum values are ultimately encoded as strings. What’s going on here? We can find the answer in [`Dictionary`’s implementation](https://github.com/apple/swift/blob/swift-4.1-branch/stdlib/public/core/Codable.swift.gyb#L1995-L2033) for the [`Encodable`](https://developer.apple.com/documentation/swift/encodable) protocol. The code looks like this:

```
extension Dictionary : Encodable where Key : Encodable, Value : Encodable {
    /// Encodes the contents of this dictionary into the given encoder.
    ///
    /// If the dictionary uses `String` or `Int` keys, the contents are encoded
    /// in a keyed container. Otherwise, the contents are encoded as alternating
    /// key-value pairs in an unkeyed container.
    ///
    /// This function throws an error if any values are invalid for the given
    /// encoder's format.
    ///
    /// - Parameter encoder: The encoder to write data to.
    public func encode(to encoder: Encoder) throws {
        if Key.self == String.self {
            // Since the keys are already Strings, we can use them as keys directly.
            var container = encoder.container(keyedBy: _DictionaryCodingKey.self)
            for (key, value) in self {
                let codingKey = _DictionaryCodingKey(stringValue: key as! String)!
                try container.encode(value, forKey: codingKey)
            }
        } else if Key.self == Int.self {
            // Since the keys are already Ints, we can use them as keys directly.
            var container = encoder.container(keyedBy: _DictionaryCodingKey.self)
            for (key, value) in self {
                let codingKey = _DictionaryCodingKey(intValue: key as! Int)!
                try container.encode(value, forKey: codingKey)
            }
        } else {
            // Keys are Encodable but not Strings or Ints, so we cannot arbitrarily
            // convert to keys. We can encode as an array of alternating key-value
            // pairs, though.
            var container = encoder.unkeyedContainer()
            for (key, value) in self {
                try container.encode(key)
                try container.encode(value)
            }
        }
    }
}
```

There are three branches: only if the dictionary’s key type is `String` or `Int` does it use a keyed container. Any other key type triggers results in an unkeyed container of alternating keys and values.

`String` and `Int` get special treatment because those are the two valid coding key types in the `Codable` world. Any other coding key is ultimately lowered to a `String` or `Int`.[1](#fn:1) Since the dictionary has no way to tell how other types encode themselves, it has no choice but to resort to an unkeyed container.

And the fact that our custom enum is backed by `String` (and thus produces `String` values when encoded) doesn’t matter. The standard library can’t use a rule like “use a keyed container if `Key: RawRepresentable, Key.RawValue == String`” because, however unlikely, the type may have overridden the default compiler-synthesized `Codable` implementation to encode itself differently — there’s no practical way for the standard library to tell.

Until Swift changes the behavior (if ever), I don’t think there’s a simple fix for this, short of manually converting any dictionary to `String` or `Int` keys before encoding. Here’s how you could do this for the example dictionary (this works for any [`RawRepresentable`](https://developer.apple.com/documentation/swift/rawrepresentable) dictionary with a `RawValue` of `String` or `Int`):

```
let stringKeyedDict = Dictionary(
    dict.map { ($0.key.rawValue, $0.value) },
    uniquingKeysWith: { $1 }
)
```

This creates a new dictionary from a sequence of key-value pairs. We create this sequence by mapping over the source dictionary and using the key’s `rawValue` property to produce the string keys.

---

**Update May 29, 2018:** Itai Ferber, one of the developers of the `Codable` system [confirmed in a post on the Swift forums](https://forums.swift.org/t/json-encoding-decoding-weird-encoding-of-dictionary-with-enum-values/12995/7) that he sees this as more a bug than a feature:

> This was an oversight in the implementation as far as I’m concerned. Something that is RawRepresentable as a String or Int encodes as a String or Int by default everywhere else, and I don’t think this should be different.
> 
> The one thing we need to figure out is how bad the regression would be if we changed behavior, as we would introduce incompatibility in the other direction.

---

**Update July 31, 2022:** Although the default coding behavior can’t be changed since it would break existing archives, Swift 5.6 ([SE-0320](https://github.com/apple/swift-evolution/blob/main/proposals/0320-codingkeyrepresentable.md)) added the ability to opt in to a more consistent coding format for non-string-keyed dictionaries. To do this in our example, all we have to do is conform our key type to the [`CodingKeyRepresentable`](https://developer.apple.com/documentation/swift/codingkeyrepresentable) protocol:

```
enum Color: String, Codable, CodingKeyRepresentable {
    case red
    case green
    case blue
}
```

`Dictionary`’s `Codable` implementation detects that the key type has this conformance and uses it convert the enum values to and from strings in a controlled manner.

1. You may wonder why `Int` is a valid key type when JSON requires string keys. But we’re on a more generic level here. The dictionary doesn’t know it’s being encoded into JSON, it only knows about the generic [`Encoder`](https://developer.apple.com/documentation/swift/encoder) interface. And all compatible encoders must be able to handle `String` and `Int` keys. It’s then the [`JSONEncoder`](https://developer.apple.com/documentation/foundation/jsonencoder)’s task to convert any integer keys it receives into strings. [↩︎](#fnref:1)
