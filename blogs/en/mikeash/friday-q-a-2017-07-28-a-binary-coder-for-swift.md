---
title: 'Friday Q&A 2017-07-28: A Binary Coder for Swift'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-07-28-a-binary-coder-for-swift.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f88d07b2d76a504d'
translated: false
---

> 原文：[Friday Q&A 2017-07-28: A Binary Coder for Swift](https://www.mikeash.com/pyblog/friday-qa-2017-07-28-a-binary-coder-for-swift.html)　·　mikeash.com Friday Q&A

Posted at 2017-07-28 12:44 | [RSS feed](https://www.mikeash.com/pyblog/rss.py) ([Full text feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [Blog Index](https://www.mikeash.com/pyblog/)  
Next article: [Friday Q&A 2017-08-11: Swift.Unmanaged](https://www.mikeash.com/pyblog/friday-qa-2017-08-11-swiftunmanaged.html)  
Previous article: [Friday Q&A 2017-07-14: Swift.Codable](https://www.mikeash.com/pyblog/friday-qa-2017-07-14-swiftcodable.html)  
Tags: [fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [serialization](https://www.mikeash.com/pyblog/?tag=serialization) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-07-28: A Binary Coder for Swift

by [Mike Ash](https://www.mikeash.com/)

This article is also available in [Hungarian (translation by Zsolt Boros)](http://www.forallworld.com/binaris-coder-valo-swift/).

**Source Code**  
As usual, the source code is available on GitHub:

[https://github.com/mikeash/BinaryCoder/tree/887cecd70c070d86f338065f59ed027c13952c83](https://github.com/mikeash/BinaryCoder/tree/887cecd70c070d86f338065f59ed027c13952c83)

**Concept and Approach**  
This coder serializes fields by writing them out sequentially as raw bytes, with no metadata. For example:

```
    struct S {
        var a: Int16
        var b: Int32
        var c: Int64
    }
```

The result of encoding an instance of `S` is fourteen bytes long, with two bytes for `a`, four bytes for `b`, and eight bytes for `c`. The result is _almost_ the same as writing out the raw underlying memory of `S`, except there's no padding, the numbers are byte-swapped to be endian agnostic, and it's able to intelligently chase down references and do custom encoding when needed.

This type of straightforward binary encoding is a little hobby of mine, and I've previously experimented with other approaches to it in Swift, none of which were satisfactory. When the Swift 4 beta became available with `Codable`, I looked to see if it would work for this, and it did!

My use of `Codable` is somewhat abusive. I want to take advantage of the compiler-generated `Encodable` and `Decodable` implementations, but those use keyed coding, whereas the straight-line no-metadata binary format is pretty much the polar opposite of keyed coding. The solution is simple: ignore the keys, and rely on the encoding and decoding order to be consistent. This is ugly, and a bad idea in general, but it does work, and even got [a tweet from a member of the Swift core team](https://twitter.com/jckarter/status/874079604612505601) indicating it might be OK. This approach is obviously _not_ resilient to changes in your field layout or field types, but as long as you're aware of this and understand it, that's acceptable.

It does mean that arbitrary implementations of `Codable` can't be trusted to work with this coder. We know that the compiler-generated implementations work, with limitations, but there may be implementations in the standard library (for example, the implementation for `Array`) which rely on semantics that this coder doesn't support. In order to ensure that types don't partipate in binary coding without some vetting, I created my own protocols for binary coding:

```
    public protocol BinaryEncodable: Encodable {
        func binaryEncode(to encoder: BinaryEncoder) throws
    }

    public protocol BinaryDecodable: Decodable {
        init(fromBinary decoder: BinaryDecoder) throws
    }

    public typealias BinaryCodable = BinaryEncodable & BinaryDecodable
```

I wrote extensions to simplify the common case where you just want to use the compiler's implementation of `Codable`:

```
    public extension BinaryEncodable {
        func binaryEncode(to encoder: BinaryEncoder) throws {
            try self.encode(to: encoder)
        }
    }

    public extension BinaryDecodable {
        public init(fromBinary decoder: BinaryDecoder) throws {
            try self.init(from: decoder)
        }
    }
```

This way, your own types can just conform to `BinaryCodable`, and they'll get a default implementation of everything they need, as long as they meet the requirements. It's required that all fields must be `Codable`, but we can't require all fields to be `BinaryCodable`. That type checking has to be done at runtime, which is unfortunate, but acceptable.

The encoder and decoder implementation are straightforward: they encode/decode everything in order, ignoring the keys. The encoder produces bytes corresponding to the values that are encoded, and the decoder produces values from the bytes it has stored.

**`BinaryEncoder` Basics**  
The encoder is a public class:

```
    public class BinaryEncoder {
```

It has one field, which is the data it has encoded so far:

```
    fileprivate var data: [UInt8] = []
```

This data starts out empty, and bytes are appended to it as values are encoded.

A convenience method wraps up the process of creating an encoder instance, encoding an object into it, and returning the instance's data:

```
    static func encode(_ value: BinaryEncodable) throws -> [UInt8] {
        let encoder = BinaryEncoder()
        try value.binaryEncode(to: encoder)
        return encoder.data
    }
```

The encoding process can throw runtime errors, so the encoder needs an error type:

```
    enum Error: Swift.Error {
        case typeNotConformingToBinaryEncodable(Encodable.Type)
        case typeNotConformingToEncodable(Any.Type)
    }
```

Let's move on to the low-level encoding methods. We'll start with a generic method which will encode the raw bytes of a value:

```
    func appendBytes<T>(of: T) {
        var target = of
        withUnsafeBytes(of: &target) {
            data.append(contentsOf: $0)
        }
    }
```

This will form the basis for other encoding methods.

Let's take a quick look at the methods for encoding `Float` and `Double` next. CoreFoundation has helper functions which take care of any byte swapping that's needed for them, so these methods call those functions and then call `appendBytes` with the result:

```
    func encode(_ value: Float) {
        appendBytes(of: CFConvertFloatHostToSwapped(value))
    }

    func encode(_ value: Double) {
        appendBytes(of: CFConvertDoubleHostToSwapped(value))
    }
```

While we're at it, here's the method for encoding a `Bool`. It translates the `Bool` to a `UInt8` containing a `0` or `1` and encodes that:

```
    func encode(_ value: Bool) throws {
        try encode(value ? 1 as UInt8 : 0 as UInt8)
    }
```

`BinaryEncoder` has one more `encode` method, which takes care of encoding all other `Encodable` types:

```
    func encode(_ encodable: Encodable) throws {
```

This has special cases for various types, so it switches on the parameter:

```
        switch encodable {
```

`Int` and `UInt` need special handling, because their sizes aren't consistent. Depending on the target platform, they may be 32 bits or 64 bits. To solve this, we convert them to `Int64` or `UInt64` and then encode that value:

```
        case let v as Int:
            try encode(Int64(v))
        case let v as UInt:
            try encode(UInt64(v))
```

All other integer types are handled with the `FixedWidthInteger` protocol, which exposes enough functionality to do the necessary byte swapping for encoding values. Because `FixedWidthInteger` uses `Self` for some return types, I wasn't able to do the work directly here. Instead, I extended `FixedWidthInteger` with a `binaryEncode` method that handles the work:

```
        case let v as FixedWidthInteger:
            v.binaryEncode(to: self)
```

`Float`, `Double`, and `Bool` call the type-specific methods above:

```
        case let v as Float:
            encode(v)
        case let v as Double:
            encode(v)
        case let v as Bool:
            try encode(v)
```

Anything that's `BinaryEncodable` is encoded by calling its `binaryEncode` method and passing `self`:

```
        case let binary as BinaryEncodable:
            try binary.binaryEncode(to: self)
```

There's one more case to handle. Any value that gets this far is not a type that we know how to encode natively, nor is it `BinaryEncodable`. In this case, we throw an error to inform the caller that this value doesn't conform to the protocol:

```
        default:
            throw Error.typeNotConformingToBinaryEncodable(type(of: encodable))
        }
    }
```

Finally, let's look at the `FixedWidthInteger` extension. All this has to do is call `self.bigEndian` to get a portable representation of the integer type, and then call `appendBytes` on the encoder to encode that representation:

```
    private extension FixedWidthInteger {
        func binaryEncode(to encoder: BinaryEncoder) {
            encoder.appendBytes(of: self.bigEndian)
        }
    }
```

We now have all the important parts of binary encoding, but we still don't have an `Encoder` implementation. To accomplish that, we'll create implementations of the container protocols which call back to the `BinaryEncoder` to do the work.

**`BinaryEncoder` `Encoder` Implementation**  
Let's start by looking at the implementations of the containers. We'll start with the `KeyedEncodingContainerProtocol` implementation:

```
    private struct KeyedContainer<Key: CodingKey>: KeyedEncodingContainerProtocol {
```

The implementation needs a reference to the binary encoder that it's working in:

```
        var encoder: BinaryEncoder
```

`Encoder` requires a `codingPath` property which returns an array of `CodingKey` values indicating the current path into the encoder. Since this encoder doesn't really support keys in the first place, we always return an empty array:

```
        public var codingPath: [CodingKey] { return [] }
```

Code which uses this class will have to be implemented not to require this value to make any sense.

The protocol then has a ton of methods for encoding all of the various types that it supports:

```
    public mutating func encode(_ value: Bool, forKey key: Self.Key) throws
    public mutating func encode(_ value: Int, forKey key: Self.Key) throws
    public mutating func encode(_ value: Int8, forKey key: Self.Key) throws
    public mutating func encode(_ value: Int16, forKey key: Self.Key) throws
    public mutating func encode(_ value: Int32, forKey key: Self.Key) throws
    public mutating func encode(_ value: Int64, forKey key: Self.Key) throws
    public mutating func encode(_ value: UInt, forKey key: Self.Key) throws
    public mutating func encode(_ value: UInt8, forKey key: Self.Key) throws
    public mutating func encode(_ value: UInt16, forKey key: Self.Key) throws
    public mutating func encode(_ value: UInt32, forKey key: Self.Key) throws
    public mutating func encode(_ value: UInt64, forKey key: Self.Key) throws
    public mutating func encode(_ value: Float, forKey key: Self.Key) throws
    public mutating func encode(_ value: Double, forKey key: Self.Key) throws
    public mutating func encode(_ value: String, forKey key: Self.Key) throws
    public mutating func encode<T>(_ value: T, forKey key: Self.Key) throws where T : Encodable
```

We'll have to implement all of those one by one. Let's start with the last one, which handles generic `Encodable` values. It just needs to call through to `BinaryEncoder`'s `encode` method:

```
        func encode<T>(_ value: T, forKey key: Key) throws where T : Encodable {
            try encoder.encode(value)
        }
```

We can use a similar technique to implement the other methods, and... what's this? All of the compiler errors about protocol conformance have gone away?

It turns out that this one implementation of `encode` satisfies _all_ of the `encode` methods in the protocol, because all of the other types are `Encodable`. A suitable generic method will fulfill any matching protocol requirements. It's obvious in retrospect, but I didn't realize it until I was halfway done with this code and saw that errors didn't appear when I deleted type-specific methods.

Now we can see why I implemented `BinaryEncoder`'s `encode` method with a big `switch` statement instead of using separate implementations for all of the various supported types. Overloaded methods are resolved at compile time based on the static type that's available at the call site. The above call to `encoder.encode(value)` will always call `func encode(_ encodable: Encodable)` even if the actual value passed in is, say, a `Double` or a `Bool`. In order to allow for this simple wrapper, the implementation in `BinaryEncoder` has to work with a single entry point, which means it needs to be a big `switch` statement.

`KeyedEncodingContainerProtocol` requires a few other methods. There's one for encoding nil, which we implement to do nothing:

```
        func encodeNil(forKey key: Key) throws {}
```

Then there are four methods for returning nested containers or superclass encoders. We don't do anything clever here, so this just delegates back to the encoder:

```
        func nestedContainer<NestedKey>(keyedBy keyType: NestedKey.Type, forKey key: Key) -> KeyedEncodingContainer<NestedKey> where NestedKey : CodingKey {
            return encoder.container(keyedBy: keyType)
        }

        func nestedUnkeyedContainer(forKey key: Key) -> UnkeyedEncodingContainer {
            return encoder.unkeyedContainer()
        }

        func superEncoder() -> Encoder {
            return encoder
        }

        func superEncoder(forKey key: Key) -> Encoder {
            return encoder
        }
    }
```

We also need implementations of `UnkeyedEncodingContainer` and `SingleValueEncodingContainer`. It turns out that those protocols are similar enough that we can use a single implementation for both. The actual implementation is almost the same as it was for `KeyedEncodingContainerProtocol`, with the addition of a dummy `count` property:

```
    private struct UnkeyedContanier: UnkeyedEncodingContainer, SingleValueEncodingContainer {
        var encoder: BinaryEncoder

        var codingPath: [CodingKey] { return [] }

        var count: Int { return 0 }

        func nestedContainer<NestedKey>(keyedBy keyType: NestedKey.Type) -> KeyedEncodingContainer<NestedKey> where NestedKey : CodingKey {
            return encoder.container(keyedBy: keyType)
        }

        func nestedUnkeyedContainer() -> UnkeyedEncodingContainer {
            return self
        }

        func superEncoder() -> Encoder {
            return encoder
        }

        func encodeNil() throws {}

        func encode<T>(_ value: T) throws where T : Encodable {
            try encoder.encode(value)
        }
    }
```

Using these containers, we'll make `BinaryEncoder` conform to `Encoder`.

`Encoder` requires a `codingPath` property like the containers do:

```
    public var codingPath: [CodingKey] { return [] }
```

It also requires a `userInfo` property. We don't support that either, so it returns an empty dictionary:

```
    public var userInfo: [CodingUserInfoKey : Any] { return [:] }
```

Then there are three methods which return containers:

```
    public func container<Key>(keyedBy type: Key.Type) -> KeyedEncodingContainer<Key> where Key : CodingKey {
        return KeyedEncodingContainer(KeyedContainer<Key>(encoder: self))
    }

    public func unkeyedContainer() -> UnkeyedEncodingContainer {
        return UnkeyedContanier(encoder: self)
    }

    public func singleValueContainer() -> SingleValueEncodingContainer {
        return UnkeyedContanier(encoder: self)
    }
```

That's the end of `BinaryEncoder`.

**`BinaryDecoder` Basics**  
The decoder is a public class too:

```
    public class BinaryDecoder {
```

Like the encoder, it has some data:

```
    fileprivate let data: [UInt8]
```

Unlike the encoder, the decoder's data is loaded into the object when it's created. The caller provides the data that the decoder will decode from:

```
    public init(data: [UInt8]) {
        self.data = data
    }
```

The decoder also needs to keep track of where it is inside the data it's decoding. It does that with a `cursor` property, which starts out at the beginning of the data:

```
    fileprivate var cursor = 0
```

A convenience method wraps up the process of creating a decoder and decoding a value:

```
    static func decode<T: BinaryDecodable>(_ type: T.Type, data: [UInt8]) throws -> T {
        return try BinaryDecoder(data: data).decode(T.self)
    }
```

The decoder has its own errors it can throw during the decoding process. Decoding can fail in many more ways than encoding, so `BinaryDecoder`'s `Error` type has a lot more cases:

```
    enum Error: Swift.Error {
        case prematureEndOfData
        case typeNotConformingToBinaryDecodable(Decodable.Type)
        case typeNotConformingToDecodable(Any.Type)
        case intOutOfRange(Int64)
        case uintOutOfRange(UInt64)
        case boolOutOfRange(UInt8)
        case invalidUTF8([UInt8])
    }
```

Now we can get on to actual decoding. The lowest level method reads a certain number of bytes out of `data` into a pointer, advancing `cursor`, or throwing `prematureEndOfData` if `data` doesn't have enough bytes in it:

```
    func read(_ byteCount: Int, into: UnsafeMutableRawPointer) throws {
        if cursor + byteCount > data.count {
            throw Error.prematureEndOfData
        }

        data.withUnsafeBytes({
            let from = $0.baseAddress! + cursor
            memcpy(into, from, byteCount)
        })

        cursor += byteCount
    }
```

There's also a small generic wrapper which takes an `inout T` and reads into that value, using `MemoryLayout` to figure out how many bytes to read.

```
    func read<T>(into: inout T) throws {
        try read(MemoryLayout<T>.size, into: &into)
    }
```

Like `BinaryEncoder`, `BinaryDecoder` has methods for decoding floating-point types. For these, it creates an empty `CFSwappedFloat` value, reads into it, and then calls the appropriate CF function to convert it to the floating-point type in question:

```
    func decode(_ type: Float.Type) throws -> Float {
        var swapped = CFSwappedFloat32()
        try read(into: &swapped)
        return CFConvertFloatSwappedToHost(swapped)
    }

    func decode(_ type: Double.Type) throws -> Double {
        var swapped = CFSwappedFloat64()
        try read(into: &swapped)
        return CFConvertDoubleSwappedToHost(swapped)
    }
```

The method for decoding `Bool` decodes a `UInt8` and then returns false if it's `0`, true if it's `1`, and otherwise throws an error:

```
    func decode(_ type: Bool.Type) throws -> Bool {
        switch try decode(UInt8.self) {
        case 0: return false
        case 1: return true
        case let x: throw Error.boolOutOfRange(x)
        }
    }
```

The general `decode` method for `Decodable` uses a big `switch` statement to decode various specific types:

```
    func decode<T: Decodable>(_ type: T.Type) throws -> T {
        switch type {
```

For `Int` and `UInt`, it decodes an `Int64` or `UInt64`, then converts to an `Int` or `UInt`, or throws an error:

```
        case is Int.Type:
            let v = try decode(Int64.self)
            if let v = Int(exactly: v) {
                return v as! T
            } else {
                throw Error.intOutOfRange(v)
            }
        case is UInt.Type:
            let v = try decode(UInt64.self)
            if let v = UInt(exactly: v) {
                return v as! T
            } else {
                throw Error.uintOutOfRange(v)
            }
```

The compiler doesn't realize that `T`'s type must match the values being produced, so the `as! T` convinces it to compile this code.

Other integers are handled through `FixedWidthInteger` using an extension method:

```
        case let intT as FixedWidthInteger.Type:
            return try intT.from(binaryDecoder: self) as! T
```

`Float`, `Double`, and `Bool` all call their type-specific decoding methods:

```
        case is Float.Type:
            return try decode(Float.self) as! T
        case is Double.Type:
            return try decode(Double.self) as! T
        case is Bool.Type:
            return try decode(Bool.self) as! T
```

`BinaryDecodable` types use the initializer defined in that protocol, passing `self`:

```
        case let binaryT as BinaryDecodable.Type:
            return try binaryT.init(fromBinary: self) as! T
```

If none of the cases are hit, then throw an error:

```
        default:
            throw Error.typeNotConformingToBinaryDecodable(type)
        }
    }
```

The `FixedWidthInteger` method uses `Self.init()` to make a value, reads bytes into it, and then uses the `bigEndian:` initializer to perform byte swapping:

```
    private extension FixedWidthInteger {
        static func from(binaryDecoder: BinaryDecoder) throws -> Self {
            var v = Self.init()
            try binaryDecoder.read(into: &v)
            return self.init(bigEndian: v)
        }
    }
```

That takes care of the foundation. Now to implement `Decoder`.

**`BinaryDecoder` `Decoder` Implementation**  
As before, we implement the three container protocols. We'll start with the keyed container:

```
    private struct KeyedContainer<Key: CodingKey>: KeyedDecodingContainerProtocol {
```

It delegates everything to the decoder, so it needs a reference to that:

```
        var decoder: BinaryDecoder
```

The protocol requires `codingPath`:

```
        var codingPath: [CodingKey] { return [] }
```

It also requires `allKeys`, which returns all keys that the container knows about. Since we don't really support keys in the first place, this returns an empty array:

```
        var allKeys: [Key] { return [] }
```

There's also a method to see if the container contains a given key. We'll just blindly say "yes" to all such questions:

```
        func contains(_ key: Key) -> Bool {
            return true
        }
```

As before, `KeyedDecodingContainerProtocol` has a ton of different `decode` methods which can all be satisfied with a single generic method for `Decodable`:

```
        func decode<T>(_ type: T.Type, forKey key: Key) throws -> T where T : Decodable {
            return try decoder.decode(T.self)
        }
```

There's also a `decodeNil`, which we'll have do nothing and always succeed:

```
        func decodeNil(forKey key: Key) throws -> Bool {
            return true
        }
```

Nested containers and superclass decodes delegate back to the decoder:

```
        func nestedContainer<NestedKey>(keyedBy type: NestedKey.Type, forKey key: Key) throws -> KeyedDecodingContainer<NestedKey> where NestedKey : CodingKey {
            return try decoder.container(keyedBy: type)
        }

        func nestedUnkeyedContainer(forKey key: Key) throws -> UnkeyedDecodingContainer {
            return try decoder.unkeyedContainer()
        }

        func superDecoder() throws -> Decoder {
            return decoder
        }

        func superDecoder(forKey key: Key) throws -> Decoder {
            return decoder
        }
    }
```

Like before, one type can implement both of the other container protocols:

```
    private struct UnkeyedContainer: UnkeyedDecodingContainer, SingleValueDecodingContainer {
        var decoder: BinaryDecoder

        var codingPath: [CodingKey] { return [] }

        var count: Int? { return nil }

        var currentIndex: Int { return 0 }

        var isAtEnd: Bool { return false }

        func decode<T>(_ type: T.Type) throws -> T where T : Decodable {
            return try decoder.decode(type)
        }

        func decodeNil() -> Bool {
            return true
        }

        func nestedContainer<NestedKey>(keyedBy type: NestedKey.Type) throws -> KeyedDecodingContainer<NestedKey> where NestedKey : CodingKey {
            return try decoder.container(keyedBy: type)
        }

        func nestedUnkeyedContainer() throws -> UnkeyedDecodingContainer {
            return self
        }

        func superDecoder() throws -> Decoder {
            return decoder
        }
    }
```

Now `BinaryDecoder` itself can provide dummy implementations of the properties required by `Decoder` and implement methods to return instances of the containers:

```
    public var codingPath: [CodingKey] { return [] }

    public var userInfo: [CodingUserInfoKey : Any] { return [:] }

    public func container<Key>(keyedBy type: Key.Type) throws -> KeyedDecodingContainer<Key> where Key : CodingKey {
        return KeyedDecodingContainer(KeyedContainer<Key>(decoder: self))
    }

    public func unkeyedContainer() throws -> UnkeyedDecodingContainer {
        return UnkeyedContainer(decoder: self)
    }

    public func singleValueContainer() throws -> SingleValueDecodingContainer {
        return UnkeyedContainer(decoder: self)
    }
```

That is the end of `BinaryDecoder`.

**`Array` and `String` Extensions**  
In order to make the coders more useful, I implemented `BinaryCodable` for `Array` and `String`. In theory I could call through to their `Codable` implementation, but I can't count on that implementation to work with the limitations of the binary coders, and I wouldn't have control over the serialized representation. Instead, I manually implemented it.

The plan is to have `Array` encode its count, and then encode its elements. To decode, it can decode the count, then decode that many elements. `String` will convert itself to UTF-8 in the form of `Array` and then use `Array`'s implementation to do the real work.

Someday, when Swift gets [conditional conformances](https://github.com/apple/swift-evolution/blob/master/proposals/0143-conditional-conformances.md), we'll be able to write `extension Array: BinaryCodable where Element: BinaryCodable` to indicate that `Array` is is only codable when its contents are. For now, Swift can't express that notion. Instead, we have to say that `Array` is always `BinaryCodable`, and then do runtime type checks to ensure the content is suitable.

Encoding is a matter of checking the type of `Element`, encoding `self.count`, then encoding all of the elements:

```
    extension Array: BinaryCodable {
        public func binaryEncode(to encoder: BinaryEncoder) throws {
            guard Element.self is Encodable.Type else {
                throw BinaryEncoder.Error.typeNotConformingToEncodable(Element.self)
            }

            try encoder.encode(self.count)
            for element in self {
                try (element as! Encodable).encode(to: encoder)
            }
        }
```

Decoding is the opposite. Check the type, decode the count, then decode that many elements:

```
        public init(fromBinary decoder: BinaryDecoder) throws {
            guard let binaryElement = Element.self as? Decodable.Type else {
                throw BinaryDecoder.Error.typeNotConformingToDecodable(Element.self)
            }

            let count = try decoder.decode(Int.self)
            self.init()
            self.reserveCapacity(count)
            for _ in 0 ..< count {
                let decoded = try binaryElement.init(from: decoder)
                self.append(decoded as! Element)
            }
        }
    }
```

`String` can then encode itself by creating an `Array` from its `utf8` property and encoding that:

```
    extension String: BinaryCodable {
        public func binaryEncode(to encoder: BinaryEncoder) throws {
            try Array(self.utf8).binaryEncode(to: encoder)
        }
```

Decoding decodes the UTF-8 `Array` and then creates a `String` from it. This will fail if the decoded `Array` isn't valid UTF-8, so there's a little extra code here to check for that and throw an error:

```
        public init(fromBinary decoder: BinaryDecoder) throws {
            let utf8: [UInt8] = try Array(fromBinary: decoder)
            if let str = String(bytes: utf8, encoding: .utf8) {
                self = str
            } else {
                throw BinaryDecoder.Error.invalidUTF8(utf8)
            }
        }
    }
```

**Example Use**  
That takes care of binary encoding and decoding. Use is simple. Declare conformance to `BinaryCodable`, then use `BinaryEncoder` and `BinaryDecoder` on your types:

```
    struct Company: BinaryCodable {
        var name: String
        var employees: [Employee]
    }

    struct Employee: BinaryCodable {
        var name: String
        var jobTitle: String
        var age: Int
    }

    let company = Company(name: "Joe's Discount Airbags", employees: [
        Employee(name: "Joe Johnson", jobTitle: "CEO", age: 27),
        Employee(name: "Stan Lee", jobTitle: "Janitor", age: 87),
        Employee(name: "Dracula", jobTitle: "Dracula", age: 41),
        Employee(name: "Steve Jobs", jobTitle: "Visionary", age: 56),
    ])
    let data = try BinaryEncoder.encode(company)
    let roundtrippedCompany = try BinaryDecoder.decode(Company.self, data: data)
    // roundtrippedCompany contains the same data as company
```

**Conclusion**  
Swift's new `Codable` protocols are a welcome addition to the language to eliminate a lot of boilerplate code. It's flexible enough to make it straightforward to use/abuse it for things well beyond JSON and property list parsing. Unsophisticated binary formats such as this are not often called for, but they have their uses, and it's interesting to see how `Codable` can be used for something so different from the built-in facilities. The `Encoder` and `Decoder` protocols are large, but judicious use of generics can cut down a lot of the repetitive code, and implementation is relatively simple in the end.

`BinaryCoder` was written for exploratory and educational purposes, and it's probably not what you want to use in your own programs. However, there are cases where it could be suitable, as long as you understand the tradeoffs involved.

That's it for today! Come back again for more exciting byte-related adventures. As always, Friday Q&A is driven by reader ideas, so if you have a topic you'd like to see covered, please [send it in](mailto:mike@mikeash.com)!

Did you enjoy this article? I'm selling whole books full of them! Volumes II and III are now out! They're available as ePub, PDF, print, and on iBooks and Kindle. [Click here for more information](https://www.mikeash.com/book.html).

---

Comments:

---

Comments RSS feed for this page

Add your thoughts, post a comment:

Spam and off-topic posts will be deleted without notice. Culprits may be publicly humiliated at my sole discretion.

Code syntax highlighting thanks to [Pygments](http://pygments.org/).
