---
title: my last article
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-07-14-swiftcodable.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:d6df8ff716c58021'
translated: false
---

> 原文：[my last article](https://www.mikeash.com/pyblog/friday-qa-2017-07-14-swiftcodable.html)　·　mikeash.com Friday Q&A

Posted at 2017-07-14 13:57 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2017-07-28: A Binary Coder for Swift](https://www.mikeash.com/pyblog/friday-qa-2017-07-28-a-binary-coder-for-swift.html)  
Previous article: [Friday Q&A 2017-06-30: Dissecting objc_msgSend on ARM64](https://www.mikeash.com/pyblog/friday-qa-2017-06-30-dissecting-objc_msgsend-on-arm64.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [serialization](https://www.mikeash.com/pyblog/?tag=serialization) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-07-14: Swift.Codable

by [Mike Ash](https://www.mikeash.com/)

**Serialization**  
Serializing values to data that can be stored on disk or transmitted over a network is a common need. It's especially common in this age of always-connected mobile apps.

So far, the options for serialization in Apple's ecosystem were limited:

1. provides intelligent serialization of complex object graphs and works with your own types, but works with a poorly documented serialization format not suitable for cross-platform work, and requires writing code to manually encode and decode your types.
2. and

  can convert between standard Cocoa types like

  /

  and property lists or JSON. JSON in particular is used all over the place for server communication. Since these APIs provide low-level values, you have to write a bunch of code to extract meaning from those values. That code is often ad-hoc and handles bad data poorly.
3. and

  are the choice of masochists or people stuck working with systems that use XML. Converting between the basic parsed data and more meaningful model objects is once again up to the programmer.
4. Finally, there's always the option to build your own from scratch. This is fun, but a lot of work, and error-prone.

These approaches tend to result in a lot of boilerplate code, where you declare a property called `foo` of type `String` which is encoded by storing the `String` stored in `foo` under the key `"foo"` and is decoded by retrieving the value for the key `"foo"`, attempting to cast it to a `String`, storing it into `foo` on success, or throwing an error on failure. Then you declare a property called `bar` of type `String` which....

Naturally, programmers dislike these repetitive tasks. Repitition is what computers are for. We want to be able to just write this:

```
    struct Whatever {
        var foo: String
        var bar: String
    }
```

And have it be serializable. It ought to be possible: all the necessary information is already present.

Reflection is a common way to accomplish this. A lot of Objective-C programmers have written code to automatically read and write Objective-C objects to and from JSON objects. The Objective-C runtime provides all of the information you need to do this automatically. For Swift, we can use the Objective-C runtime, or make do with Swift's Mirror and use wacky workarounds to compensate for its inability to mutate properties.

Outside of Apple's ecosystem, this is a common approach in many languages. This has led to various [hilarious](http://blog.codeclimate.com/blog/2013/01/10/rails-remote-code-execution-vulnerability-explained/) [security](https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet) [bugs](https://www.cs.uic.edu/~s/musings/pickle/) over the years.

Reflection is not a particularly good solution to this problem. It's easy to get it wrong and create security bugs. It's less able to use static typing, so more errors happen at runtime rather than compile time. And it tends to be pretty slow, since the code has to be completely general and does lots of string lookups with type metadata.

Swift has taken the approach of compile-time code generation rather than runtime reflection. This means that some of the knowledge has to be built in to the compiler, but the result is fast and takes advantage of static typing, while still remaining easy to use.

**Overview**  
There are a few fundamental protocols that Swift's new encoding system is built around.

The `Encodable` protocol is used for types which can be encoded. If you conform to this protocol and all stored properties in your type are themselves `Encodable`, then the compiler will generate an implementation for you. If you don't meet the requirements, or you need special handling, you can implement it yourself.

The `Decodable` protocol is the companion to the `Encodable` protocol and denotes types which can be decoded. Like `Encodable`, the compiler will generate an implementation for you if your stored properties are all `Decodable`.

Because `Encodable` and `Decodable` usually go together, there's another protocol called `Codable` which is just the two protocols glued together:

```
    typealias Codable = Decodable & Encodable
```

These two protocols are really simple. Each one contains just one requirement:

```
    protocol Encodable {
        func encode(to encoder: Encoder) throws
    }

    protocol Decodable {
        init(from decoder: Decoder) throws
    }
```

The `Encoder` and `Decoder` protocols specify how objects can actually encode and decode themselves. You don't have to worry about these for basic use, since the default implementation of `Codable` handles all the details for you, but you need to use them if you write your own `Codable` implementation. These are complex and we'll look at them later.

Finally, there's a `CodingKey` protocol which is used to denote keys used for encoding and decoding. This adds an extra layer of static type checking to the process compared to using plain strings everywhere. It provides a `String`, and optionally an `Int` for positional keys:

```
    protocol CodingKey {
        var stringValue: String { get }
        init?(stringValue: String)

        var intValue: Int? { get }
        public init?(intValue: Int)
    }
```

**Encoders and Decoders**  
The basic concept of `Encoder` and `Decoder` is similar to `NSCoder`. Objects receive a coder and then call its methods to encode or decode themselves.

The API of `NSCoder` is straightforward. `NSCoder` has a bunch of methods like `encodeObject:forKey:` and `encodeInteger:forKey:` which objects call to perform their coding. Objects can also use unkeyed methods like `encodeObject:` and `encodeInteger:` to do things positionally instead of by key.

Swift's API is more indirect. `Encoder` doesn't have any methods of its own for encoding values. Instead, it provides _containers_, and those containers then have methods for encoding values. There's one container for keyed encoding, one for unkeyed encoding, and one for encoding a single value.

This helps make things more explicit and fits better with portable serialization formats. `NSCoder` only has to work with Apple's encoding format so it just needs to put the same thing out that it got in. `Encoder` has to work with things like JSON. If an object encodes values with keys, that should produce a JSON dictionary. If it uses unkeyed encoding then that should produce a JSON array. What if the object is empty and encodes no values? With the `NSCoder` approach, it would have no idea what to output. With `Encoder`, the object will still request a keyed or unkeyed container and the encoder can figure it out from that.

`Decoder` works the same way. You don't decode values from it directly, but rather ask for a container, and then decode values from the container. Like `Encoder`, `Decoder` provides keyed, unkeyed, and single value containers.

Because of this container design, the `Encoder` and `Decoder` protocols themselves are small. They contain a bit of bookkeeping info, and methods for obtaining containers:

```
    protocol Encoder {
        var codingPath: [CodingKey?] { get }
        public var userInfo: [CodingUserInfoKey : Any] { get }

        func container<Key>(keyedBy type: Key.Type)
            -> KeyedEncodingContainer<Key> where Key : CodingKey
        func unkeyedContainer() -> UnkeyedEncodingContainer
        func singleValueContainer() -> SingleValueEncodingContainer
    }

    protocol Decoder {
        var codingPath: [CodingKey?] { get }
        var userInfo: [CodingUserInfoKey : Any] { get }

        func container<Key>(keyedBy type: Key.Type) throws
            -> KeyedDecodingContainer<Key> where Key : CodingKey
        func unkeyedContainer() throws -> UnkeyedDecodingContainer
        func singleValueContainer() throws -> SingleValueDecodingContainer
    }
```

The complexity is in the container types. You can get pretty far by recursively walking through properties of `Codable` types, but at some point you need to get down to some raw encodable types which can be directly encoded and decoded. For `Codable`, those types include the various integer types, `Float`, `Double`, `Bool`, and `String`. That makes for a whole bunch of really similar encode/decode methods. Unkeyed containers also directly support encoding sequences of the raw encodable types.

Beyond those basic methods, there are a bunch of methods that support exotic use cases. KeyedDecodingContainer has methods called `decodeIfPresent` which return an optional and return `nil` for missing keys instead of throwing. The encoding containers have methods for weak encoding, which encodes an object only if something else encodes it too (useful for parent references in a complex graph). There are methods for getting nested containers, which allows you to encode hierarchies. Finally, there are methods for getting a "super" encoder or decoder, which is intended to allow subclasses and superclasses to coexist peacefully when encoding and decoding. The subclass can encode itself directly, and then ask the superclass to encode itself with a "super" encoder, which ensures keys don't conflict.

**Implementing `Codable`**  
Implementing `Codable` is easy: declare conformance and let the compiler generate it for you.

It's useful to know just what it's doing, though. Let's take a look at what it ends up generating and how you would do it yourself. We'll start with an example `Codable` type:

```
    struct Person: Codable {
        var name: String
        var age: Int
        var quest: String
    }
```

The compiler generates a `CodingKeys` type nested inside `Person`. If we did it ourselves, that nested type would look like this:

```
    private enum CodingKeys: CodingKey {
        case name
        case age
        case quest
    }
```

The case names match `Person`'s property names. Compiler magic gives each CodingKeys case a string value which matches its case name, which means that the property names are also the keys used for encoding them.

If we need different names, we can easily accomplish this by providing our own `CodingKeys` with custom raw values. For example, we might write this:

```
    private enum CodingKeys: String, CodingKey {
        case name = "person_name"
        case age
        case quest
    }
```

This will cause the `name` property to be encoded and decoded under `person_name`. And this is all we have to do. The compiler happily accepts our custom `CodingKeys` type while still providing a default implementation for the rest of `Codable`, and that default implementation uses our custom type. You can mix and match customizations with the compiler-provided code.

The compiler also generates an implementation for `encode(to:)` and `init(from:)`. The implementation of `encode(to:)` gets a keyed container and then encodes each property in turn:

```
    func encode(to encoder: Encoder) throws {
        var container = encoder.container(keyedBy: CodingKeys.self)

        try container.encode(name, forKey: .name)
        try container.encode(age, forKey: .age)
        try container.encode(quest, forKey: .quest)
    }
```

The compiler generates an implementation of `init(from:)` which mirrors this:

```
    init(from decoder: Decoder) throws {
        let container = try decoder.container(keyedBy: CodingKeys.self)

        name = try container.decode(String.self, forKey: .name)
        age = try container.decode(Int.self, forKey: .age)
        quest = try container.decode(String.self, forKey: .quest)
    }
```

That's all there is to it. Just like with `CodingKeys`, if you need custom behavior here you can implement your own version of one of these methods while letting the compiler generate the rest. Unfortunately, there's no way to specify custom behavior for an individual property, so you have to write out the whole thing even if you want the default behavior for the rest. This is not particularly terrible, though.

If you were to do it all by hand, the full implementation of `Codable` for `Person` would look like this:

```
    extension Person {
        private enum CodingKeys: CodingKey {
            case name
            case age
            case quest
        }

        func encode(to encoder: Encoder) throws {
            var container = encoder.container(keyedBy: CodingKeys.self)

            try container.encode(name, forKey: .name)
            try container.encode(age, forKey: .age)
            try container.encode(quest, forKey: .quest)
        }

        init(from decoder: Decoder) throws {
            let container = try decoder.container(keyedBy: CodingKeys.self)

            name = try container.decode(String.self, forKey: .name)
            age = try container.decode(Int.self, forKey: .age)
            quest = try container.decode(String.self, forKey: .quest)
        }
    }
```

**Implementing `Encoder` and `Decoder`**  
You may never need to implement your own `Encoder` or `Decoder`. Swift provides implementations for JSON and property lists, which take care of the common use cases.

You can implement your own in order to support a custom format. The size of the container protocols means this will take some effort. Fortunately, it's mostly a matter of size, not complexity.

To implement a custom `Encoder`, you'll need something that implements the `Encoder` protocol plus implementations of the container protocols. Implementing the three container protocols involves a lot of repetitive code to implement encoding or decoding methods for all of the various directly encodable types.

How they work is up to you. The `Encoder` will probably need to store the data being encoded, and the containers will inform the `Encoder` of the various things they're encoding.

Implementing a custom `Decoder` is similar. You'll need to implement that protocol plus the container protocols. The decoder will hold the serialized data and the containers will communicate with it to provide the requested values.

I've been experimenting with a custom binary encoder and decoder as a way to learn the protocols, and I hope to present that in a future article as an example of how to do it.

**Conclusion**  
Swift 4's `Codable` API looks great and ought to simplify a lot of common code. For typical JSON tasks, it's sufficient to declare conformance to `Codable` in your model types and let the compiler do the rest. When needed, you can implement parts of the protocol yourself in order to handle things differently, and you can implement it all if needed.

The companion `Encoder` and `Decoder` protocols are more complex, but justifiably so. Supporting a custom format by implementing your own `Encoder` and `Decoder` takes some work, but is mostly a matter of filling in a lot of similar blanks.

That's it for today! Come back again for more exciting serialization-related material, and perhaps even things not related to serialization. Until then, Friday Q&A is driven by reader ideas, so if you have a topic you'd like to see covered here, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
