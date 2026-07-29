---
title: 'Friday Q&A 2017-07-28：一个针对 Swift 的二进制编码器'
source: 'mikeash.com Friday Q&A'
source_key: mikeash
source_url: 'https://www.mikeash.com/pyblog/friday-qa-2017-07-28-a-binary-coder-for-swift.html'
original_language: en
published: ''
status: frozen
license: 未声明 → 仅私有归档
archived_at: 2026-07-27
content_hash: 'sha256:f88d07b2d76a504d'
translated: true
---

> 原文：[Friday Q&A 2017-07-28: A Binary Coder for Swift](https://www.mikeash.com/pyblog/friday-qa-2017-07-28-a-binary-coder-for-swift.html)　·　mikeash.com Friday Q&A

发布于 2017-07-28 12:44 | [RSS Feed](https://www.mikeash.com/pyblog/rss.py) ([全文 Feed](https://www.mikeash.com/pyblog/rss.py?mode=fulltext)) | [博客索引](https://www.mikeash.com/pyblog/)  
下一篇文章：[Friday Q&A 2017-08-11: Swift.Unmanaged](https://www.mikeash.com/pyblog/friday-qa-2017-08-11-swiftunmanaged.html)  
上一篇文章：[Friday Q&A 2017-07-14: Swift.Codable](https://www.mikeash.com/pyblog/friday-qa-2017-07-14-swiftcodable.html)  
标签：[fridayqna](https://www.mikeash.com/pyblog/?tag=fridayqna) [serialization](https://www.mikeash.com/pyblog/?tag=serialization) [swift](https://www.mikeash.com/pyblog/?tag=swift)

Friday Q&A 2017-07-28：一个针对 Swift 的二进制编码器

作者：[Mike Ash](https://www.mikeash.com/)

本文也提供[匈牙利语版本（由 Zsolt Boros 翻译）](http://www.forallworld.com/binaris-coder-valo-swift/)。

**源代码**  
像往常一样，源代码可以在 GitHub 上找到：

[https://github.com/mikeash/BinaryCoder/tree/887cecd70c070d86f338065f59ed027c13952c83](https://github.com/mikeash/BinaryCoder/tree/887cecd70c070d86f338065f59ed027c13952c83)

**概念与方法**  
这个编码器通过顺序地将字段写为原始字节来进行序列化，不包含元数据。例如：

```
    struct S {
        var a: Int16
        var b: Int32
        var c: Int64
    }
```

对 `S` 的一个实例进行编码的结果是 14 字节长，其中 `a` 占 2 字节，`b` 占 4 字节，`c` 占 8 字节。其结果*几乎*与直接写出 `S` 的原始底层内存相同，差别在于没有填充（padding），数字经过字节交换以实现字节序（endian）无关性，并且它能够智能地追踪引用并在需要时执行自定义编码。

这种直接的二进制编码方式是我的一个小爱好。我之前曾尝试过在 Swift 中使用其他方法来实现它，但都不令人满意。当 Swift 4 beta 版带着 `Codable` 发布时，我研究了它是否适用于此，结果发现是可行的！

我对 `Codable` 的使用方式有些滥用。我想利用编译器生成的 `Encodable` 和 `Decodable` 实现，但那些实现使用的是键控编码（keyed coding），而直接的、无元数据的二进制格式却与键控编码截然相反。解决方案很简单：忽略键，并依赖编码和解码顺序的一致性。这很丑陋，通常也不是个好主意，但确实有效，甚至[得到了 Swift 核心团队成员的推文](https://twitter.com/jckarter/status/874079604612505601)暗示这可能没问题。显然，这种方法对你字段布局或字段类型的更改*不*具有弹性（resilient），但只要你意识到这一点并理解它，就是可以接受的。

这的确意味着，任意 `Codable` 的实现都不能保证能与此编码器配合工作。我们知道编译器生成的实现是可行的（尽管有局限性），但标准库中可能有一些实现（例如 `Array` 的实现）依赖于此编码器不支持的语义。为了确保类型在未经审查的情况下不会参与二进制编码，我创建了自己的用于二进制编码的协议（protocol）：

```
    public protocol BinaryEncodable: Encodable {
        func binaryEncode(to encoder: BinaryEncoder) throws
    }

    public protocol BinaryDecodable: Decodable {
        init(fromBinary decoder: BinaryDecoder) throws
    }

    public typealias BinaryCodable = BinaryEncodable & BinaryDecodable
```

我编写了一些扩展来简化只想使用编译器 `Codable` 实现的常见情况：

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

这样，你自己的类型只需符合 `BinaryCodable`，只要满足要求，它们就能获得所需实现的默认实现。要求是所有字段都必须是 `Codable`，但我们不能要求所有字段都是 `BinaryCodable`。这种类型检查必须在运行时进行，这不太理想，但可以接受。

编码器和解码器的实现都很直接：它们按顺序对所有内容进行编码/解码，忽略键。编码器生成与编码值对应的字节，解码器则从其存储的字节生成值。

**`BinaryEncoder` 基础**  
编码器是一个公有类（class）：

```
    public class BinaryEncoder {
```

它有一个字段，即到目前为止已编码的数据：

```
    fileprivate var data: [UInt8] = []
```

该数据最初为空，随着值的编码，字节被追加到其中。

一个便捷方法封装了创建编码器实例、将对象编码到其中并返回实例数据的过程：

```
    static func encode(_ value: BinaryEncodable) throws -> [UInt8] {
        let encoder = BinaryEncoder()
        try value.binaryEncode(to: encoder)
        return encoder.data
    }
```

编码过程可能抛出运行时错误，因此编码器需要一个错误类型：

```
    enum Error: Swift.Error {
        case typeNotConformingToBinaryEncodable(Encodable.Type)
        case typeNotConformingToEncodable(Any.Type)
    }
```

接下来我们看低级编码方法。从一个通用的方法开始，它将编码一个值的原始字节：

```
    func appendBytes<T>(of: T) {
        var target = of
        withUnsafeBytes(of: &target) {
            data.append(contentsOf: $0)
        }
    }
```

这将构成其他编码方法的基础。

接下来快速看一下用于编码 `Float` 和 `Double` 的方法。CoreFoundation 提供了辅助函数，负责处理它们所需的任何字节交换，因此这些方法会调用这些函数，然后使用结果调用 `appendBytes`：

```
    func encode(_ value: Float) {
        appendBytes(of: CFConvertFloatHostToSwapped(value))
    }

    func encode(_ value: Double) {
        appendBytes(of: CFConvertDoubleHostToSwapped(value))
    }
```

顺便，这里是用于编码 `Bool` 的方法。它将 `Bool` 转换为包含 `0` 或 `1` 的 `UInt8`，然后对其进行编码：

```
    func encode(_ value: Bool) throws {
        try encode(value ? 1 as UInt8 : 0 as UInt8)
    }
```

`BinaryEncoder` 还有另一个 `encode` 方法，负责编码所有其他 `Encodable` 类型：

```
    func encode(_ encodable: Encodable) throws {
```

此方法对各种类型有特殊处理，因此它对参数进行 switch：

```
        switch encodable {
```

`Int` 和 `UInt` 需要特殊处理，因为它们的大小不一致。根据目标平台，它们可能是 32 位或 64 位。为了解决这个问题，我们将它们转换为 `Int64` 或 `UInt64`，然后对该值进行编码：

```
        case let v as Int:
            try encode(Int64(v))
        case let v as UInt:
            try encode(UInt64(v))
```

所有其他整数类型都通过 `FixedWidthInteger` 协议处理，该协议暴露了足够的功能来完成编码值所需的字节交换。由于 `FixedWidthInteger` 在某些返回类型中使用了 `Self`，我无法直接在这里完成工作。相反，我使用一个 `binaryEncode` 方法扩展了 `FixedWidthInteger` 来处理这个工作：

```
        case let v as FixedWidthInteger:
            v.binaryEncode(to: self)
```

`Float`、`Double` 和 `Bool` 调用上面的类型特定方法：

```
        case let v as Float:
            encode(v)
        case let v as Double:
            encode(v)
        case let v as Bool:
            try encode(v)
```

任何符合 `BinaryEncodable` 的类型都通过调用其 `binaryEncode` 方法并将 `self` 传给它来进行编码：

```
        case let binary as BinaryEncodable:
            try binary.binaryEncode(to: self)
```

还有一个要处理的情况。任何走到这一步的值，都不是我们原生知道如何编码的类型，也不是 `BinaryEncodable`。在这种情况下，我们抛出一个错误来告知调用方此值不符合该协议：

```
        default:
            throw Error.typeNotConformingToBinaryEncodable(type(of: encodable))
        }
    }
```

最后，让我们看看 `FixedWidthInteger` 扩展。它只需要调用 `self.bigEndian` 来获得整数类型的可移植表示，然后在编码器上调用 `appendBytes` 来对该表示进行编码：

```
    private extension FixedWidthInteger {
        func binaryEncode(to encoder: BinaryEncoder) {
            encoder.appendBytes(of: self.bigEndian)
        }
    }
```

我们现在已经有了二进制编码的所有重要部分，但仍然缺少 `Encoder` 实现。为了实现它，我们将创建容器协议（container protocol）的实现，这些实现会回调 `BinaryEncoder` 来完成工作。

**`BinaryEncoder` 的 `Encoder` 实现**  
让我们从查看容器的实现开始。先从 `KeyedEncodingContainerProtocol` 实现开始：

```
    private struct KeyedContainer<Key: CodingKey>: KeyedEncodingContainerProtocol {
```

该实现需要引用它所操作的二进制编码器：

```
        var encoder: BinaryEncoder
```

`Encoder` 需要一个 `codingPath` 属性，该属性返回一个 `CodingKey` 值的数组，指示进入编码器的当前路径。由于此编码器一开始并不真正支持键，我们始终返回一个空数组：

```
        public var codingPath: [CodingKey] { return [] }
```

使用此类的代码必须被实现为不需要这个值有意义。

然后该协议有一大堆用于编码其支持的各种类型的方法：

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

我们必须逐个实现所有这些方法。先从最后一个开始，它处理泛型 `Encodable` 值。它只需要调用 `BinaryEncoder` 的 `encode` 方法：

```
        func encode<T>(_ value: T, forKey key: Key) throws where T : Encodable {
            try encoder.encode(value)
        }
```

我们可以使用类似的技术来实现其他方法，然后……咦？关于协议一致性的编译器错误都消失了？

事实证明，这一个 `encode` 实现满足了协议中*所有*的 `encode` 方法，因为所有其他类型都是 `Encodable`。一个合适的泛型方法可以满足任何匹配的协议要求。事后看来很明显，但在我写这段代码写到一半，看到当我删除类型特定方法时错误并没有出现之前，我并没有意识到这一点。

现在我们可以看到为什么我使用一个大的 `switch` 语句来实现 `BinaryEncoder` 的 `encode` 方法，而不是为所有支持的类型使用单独的实现。重载方法在编译时根据调用点可用的静态类型解析。上面调用 `encoder.encode(value)` 总会调用 `func encode(_ encodable: Encodable)`，即使传入的实际值是一个 `Double` 或 `Bool`。为了允许这个简单的包装器，`BinaryEncoder` 中的实现必须通过一个单一的入口点工作，这意味着它需要一个大的 `switch` 语句。

`KeyedEncodingContainerProtocol` 还需要其他一些方法。有一个用于编码 nil 的方法，我们将其实现为什么都不做：

```
        func encodeNil(forKey key: Key) throws {}
```

然后是四个用于返回嵌套容器或超类编码器的方法。我们这里不做任何聪明的事，只是委托回编码器：

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

我们还需要 `UnkeyedEncodingContainer` 和 `SingleValueEncodingContainer` 的实现。事实证明，这些协议足够相似，我们可以为两者使用同一个实现。实际的实现几乎与 `KeyedEncodingContainerProtocol` 相同，只是多了一个虚拟的 `count` 属性：

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

使用这些容器，我们将让 `BinaryEncoder` 符合 `Encoder`。

`Encoder` 需要一个 `codingPath` 属性，就像容器一样：

```
    public var codingPath: [CodingKey] { return [] }
```

它还需要一个 `userInfo` 属性。我们也不支持这个，所以它返回一个空字典：

```
    public var userInfo: [CodingUserInfoKey : Any] { return [:] }
```

然后是三个返回容器的方法：

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

`BinaryEncoder` 到此结束。

**`BinaryDecoder` 基础**  
解码器也是一个公有类：

```
    public class BinaryDecoder {
```

像编码器一样，它有一些数据：

```
    fileprivate let data: [UInt8]
```

与编码器不同，解码器的数据在对象创建时被加载进来。调用者提供解码器将从其中进行解码的数据：

```
    public init(data: [UInt8]) {
        self.data = data
    }
```

解码器还需要跟踪它在要解码的数据中的位置。它通过一个 `cursor` 属性来做到这一点，该属性从数据的开头开始：

```
    fileprivate var cursor = 0
```

一个便捷方法封装了创建解码器并解码一个值的过程：

```
    static func decode<T: BinaryDecodable>(_ type: T.Type, data: [UInt8]) throws -> T {
        return try BinaryDecoder(data: data).decode(T.self)
    }
```

解码器在解码过程中可能有自己的错误可以抛出。解码失败的方式比编码要多得多，因此 `BinaryDecoder` 的 `Error` 类型有更多的 case：

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

现在我们可以开始实际的解码了。最低级别的方法从 `data` 中读取一定数量的字节到一个指针中，推进 `cursor`，如果 `data` 中没有足够的字节则抛出 `prematureEndOfData`：

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

还有一个小的泛型包装器，它接受一个 `inout T` 并读取到该值中，使用 `MemoryLayout` 来确定要读取多少字节。

```
    func read<T>(into: inout T) throws {
        try read(MemoryLayout<T>.size, into: &into)
    }
```

与 `BinaryEncoder` 类似，`BinaryDecoder` 有用于解码浮点类型的方法。对于这些，它创建一个空的 `CFSwappedFloat` 值，读取数据进去，然后调用适当的 CF 函数将其转换为所讨论的浮点类型：

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

用于解码 `Bool` 的方法解码一个 `UInt8`，然后如果它是 `0` 则返回 false，如果是 `1` 则返回 true，否则抛出一个错误：

```
    func decode(_ type: Bool.Type) throws -> Bool {
        switch try decode(UInt8.self) {
        case 0: return false
        case 1: return true
        case let x: throw Error.boolOutOfRange(x)
        }
    }
```

用于 `Decodable` 的通用 `decode` 方法使用一个大的 `switch` 语句来解码各种特定类型：

```
    func decode<T: Decodable>(_ type: T.Type) throws -> T {
        switch type {
```

对于 `Int` 和 `UInt`，它解码一个 `Int64` 或 `UInt64`，然后转换为 `Int` 或 `UInt`，或者抛出一个错误：

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

编译器不会意识到 `T` 的类型必须与生成的值匹配，所以 `as! T` 让它编译此代码。

其他整数通过 `FixedWidthInteger` 使用一个扩展方法处理：

```
        case let intT as FixedWidthInteger.Type:
            return try intT.from(binaryDecoder: self) as! T
```

`Float`、`Double` 和 `Bool` 都调用它们类型特定的解码方法：

```
        case is Float.Type:
            return try decode(Float.self) as! T
        case is Double.Type:
            return try decode(Double.self) as! T
        case is Bool.Type:
            return try decode(Bool.self) as! T
```

`BinaryDecodable` 类型使用该协议中定义的初始化方法（initializer），传递 `self`：

```
        case let binaryT as BinaryDecodable.Type:
            return try binaryT.init(fromBinary: self) as! T
```

如果没有匹配到任何 case，则抛出一个错误：

```
        default:
            throw Error.typeNotConformingToBinaryDecodable(type)
        }
    }
```

`FixedWidthInteger` 方法使用 `Self.init()` 创建一个值，将字节读取进去，然后使用 `bigEndian:` 初始化方法来执行字节交换：

```
    private extension FixedWidthInteger {
        static func from(binaryDecoder: BinaryDecoder) throws -> Self {
            var v = Self.init()
            try binaryDecoder.read(into: &v)
            return self.init(bigEndian: v)
        }
    }
```

基础部分就这些了。现在来实现 `Decoder`。

**`BinaryDecoder` 的 `Decoder` 实现**  
和之前一样，我们实现三个容器协议。先看键控容器：

```
    private struct KeyedContainer<Key: CodingKey>: KeyedDecodingContainerProtocol {
```

它将所有内容委托给解码器，所以它需要引用解码器：

```
        var decoder: BinaryDecoder
```

协议要求 `codingPath`：

```
        var codingPath: [CodingKey] { return [] }
```

它还需要 `allKeys`，该属性返回容器知道的所有键。由于我们一开始并不真正支持键，这里返回一个空数组：

```
        var allKeys: [Key] { return [] }
```

还有一个方法用于查看容器是否包含给定的键。对于所有此类问题，我们盲目地回答“是”：

```
        func contains(_ key: Key) -> Bool {
            return true
        }
```

和之前一样，`KeyedDecodingContainerProtocol` 有大量不同的 `decode` 方法，所有这些都可以通过一个用于 `Decodable` 的泛型方法来满足：

```
        func decode<T>(_ type: T.Type, forKey key: Key) throws -> T where T : Decodable {
            return try decoder.decode(T.self)
        }
```

还有一个 `decodeNil`，我们将实现为什么都不做并始终成功：

```
        func decodeNil(forKey key: Key) throws -> Bool {
            return true
        }
```

嵌套容器和超类解码委托回解码器：

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

像之前一样，一个类型可以实现另外两个容器协议：

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

现在 `BinaryDecoder` 本身可以提供 `Decoder` 所需属性的虚拟实现，并实现方法来返回容器的实例：

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

`BinaryDecoder` 到此结束。

**`Array` 和 `String` 扩展**  
为了使编码器更有用，我为 `Array` 和 `String` 实现了 `BinaryCodable`。理论上，我可以调用它们的 `Codable` 实现，但我不能指望该实现能在二进制编码器的限制下工作，而且我也无法控制序列化的表示形式。相反，我手动实现了它。

计划是让 `Array` 编码其 count，然后编码其元素。解码时，它可以解码 count，然后解码那么多元素。`String` 会将自己转换为 UTF-8 形式的 `Array`，然后使用 `Array` 的实现来完成实际工作。

总有一天，当 Swift 具备[条件一致性（conditional conformances）](https://github.com/apple/swift-evolution/blob/master/proposals/0143-conditional-conformances.md)时，我们将能够编写 `extension Array: BinaryCodable where Element: BinaryCodable` 来表明 `Array` 仅在其元素也可编码时才是可编码的。目前，Swift 还无法表达这个概念。相反，我们必须说 `Array` 始终是 `BinaryCodable`，然后进行运行时类型检查以确保其内容是合适的。

编码就是检查 `Element` 的类型，编码 `self.count`，然后编码所有元素：

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

解码是相反的过程。检查类型，解码 count，然后解码那么多元素：

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

然后 `String` 可以通过从其 `utf8` 属性创建一个 `Array` 并对其进行编码来编码自身：

```
    extension String: BinaryCodable {
        public func binaryEncode(to encoder: BinaryEncoder) throws {
            try Array(self.utf8).binaryEncode(to: encoder)
        }
```

解码先解码 UTF-8 `Array`，然后从中创建一个 `String`。如果解码后的 `Array` 不是有效的 UTF-8，则会失败，因此这里有一些额外的代码来检查并抛出一个错误：

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

**使用示例**  
以上就完成了二进制编码和解码。使用很简单。声明符合 `BinaryCodable`，然后在你的类型上使用 `BinaryEncoder` 和 `BinaryDecoder`：

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
    // roundtrippedCompany 包含与 company 相同的数据
```

**结论**  
Swift 新的 `Codable` 协议是该语言受欢迎的补充，能够消除大量样板代码。它具有足够的灵活性，可以轻松地将其用于超远 JSON 和属性列表解析之外的事物，甚至“滥用”之。像这样简单的二进制格式通常并不需要，但它们有其用途，并且看到 `Codable` 如何用于与内置设施如此不同的目标，是很有趣的。`Encoder` 和 `Decoder` 协议很大，但明智地使用泛型可以减少大量重复代码，并且最终实现起来相对简单。

`BinaryCoder` 是为探索和教育目的而编写的，它可能不适合在你自己的程序中使用。然而，只要你理解所涉及的权衡，在某些情况下它可能是合适的。

今天就到这里！欢迎再次回来，了解更多令人兴奋的字节相关冒险。一如既往，Friday Q&A 由读者的想法驱动，所以如果你有想要看到涵盖的主题，请[发过来](mailto:mike@mikeash.com)！

喜欢这篇文章吗？我正在销售整本包含这些文章的书！第 II 卷和第 III 卷现已出版！它们提供 ePub、PDF、印刷版，并在 iBooks 和 Kindle 上有售。[点击此处了解更多信息](https://www.mikeash.com/book.html)。

---

评论：

---

[此页面的评论 RSS Feed](https://www.mikeash.com/commentsrss.py?page=pyblog/friday-qa-2017-07-28-a-binary-coder-for-swift.html)

添加你的想法，发表评论：

垃圾邮件和离题帖子将被删除，恕不另行通知。违规者可能会由我自行决定公开羞辱。

代码语法高亮感谢 [Pygments](http://pygments.org/)。
