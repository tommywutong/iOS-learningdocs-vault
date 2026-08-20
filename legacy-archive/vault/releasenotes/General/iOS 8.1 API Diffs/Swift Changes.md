---
title: iOS 8.1 API Diffs
apple_id: TP40014994
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2014-10-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS81APIDiffs/modules/Swift.html
archived_at: '2026-07-18T02:56:16.668028Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.1 API Diffs](iOS%208.0%20to%208.1%20API%20Differences.md)


# Swift Changes

## Swift

Removed Array.init(_fromCocoaArray: _CocoaArrayType, noCopy: Bool)Removed Array.convertFromArrayLiteral(T) -> [T] [static]Removed ArrayBoundTypeRemoved ArrayBoundType.arrayBoundValueRemoved ArrayLiteralConvertible.convertFromArrayLiteral(Element) -> Self [class]Removed AssertString [struct]Removed AssertString.init()Removed AssertString.init(_: String)Removed AssertString.convertFromExtendedGraphemeClusterLiteral(String) -> AssertString [static]Removed AssertString.convertFromStringInterpolation(AssertString) -> AssertString [static]Removed AssertString.convertFromStringInterpolationSegment(T) -> AssertString [static]Removed AssertString.convertFromStringLiteral(String) -> AssertString [static]Removed AssertString.stringValueRemoved AssertStringTypeRemoved AssertStringType.stringValueRemoved AutoreleasingUnsafeMutablePointer.convertFromNilLiteral() -> AutoreleasingUnsafeMutablePointer<T> [static]Removed Bool.convertFromBooleanLiteral(Bool) -> Bool [static]Removed BooleanLiteralConvertible.convertFromBooleanLiteral(BooleanLiteralType) -> Self [class]Removed CFunctionPointer.convertFromNilLiteral() -> CFunctionPointer<T> [static]Removed COpaquePointer.convertFromNilLiteral() -> COpaquePointer [static]Removed Character.convertFromExtendedGraphemeClusterLiteral(Character) -> Character [static]Removed Character.SmallUTF16 [struct]Removed Character.SmallUTF16.init(_: UInt64)Removed Character.SmallUTF16.countRemoved Character.SmallUTF16.dataRemoved Character.SmallUTF16.endIndexRemoved Character.SmallUTF16.generate() -> IndexingGenerator<Character.SmallUTF16>Removed Character.SmallUTF16.startIndexRemoved CharacterLiteralConvertible.convertFromCharacterLiteral(CharacterLiteralType) -> Self [class]Removed CodeUnit.fromUTF16CodeUnit(CodeUnit) -> CodeUnit [static]Removed CodeUnit.toUTF16CodeUnit(CodeUnit) -> CodeUnit [static]Removed ContiguousArray.convertFromArrayLiteral(T) -> ContiguousArray<T> [static]Removed Dictionary.convertFromDictionaryLiteral((Key, Value)) -> [Key: Value] [static]Removed DictionaryLiteralConvertible.convertFromDictionaryLiteral((Key, Value)) -> Self [class]Removed Double.convertFromFloatLiteral(Double) -> Double [static]Removed Double.convertFromIntegerLiteral(Int64) -> Double [static]Removed ExtendedGraphemeClusterLiteralConvertible.convertFromExtendedGraphemeClusterLiteral(ExtendedGraphemeClusterLiteralType) -> Self [class]Removed Float.convertFromFloatLiteral(Float) -> Float [static]Removed Float.convertFromIntegerLiteral(Int64) -> Float [static]Removed FloatLiteralConvertible.convertFromFloatLiteral(FloatLiteralType) -> Self [class]Removed HeapBuffer.init(_: HeapBufferStorageBase.Type, _: Value, _: Int)Removed HeapBufferStorageBaseRemoved ImplicitlyUnwrappedOptional.convertFromNilLiteral() -> T! [static]Removed Int.init(_: Builtin.Word)Removed Int.arrayBoundValueRemoved Int.convertFromIntegerLiteral(Int) -> Int [static]Removed Int.from(IntMax) -> Int [static]Removed Int16.init(_: Builtin.Int16)Removed Int16.arrayBoundValueRemoved Int16.convertFromIntegerLiteral(Int16) -> Int16 [static]Removed Int16.from(IntMax) -> Int16 [static]Removed Int32.init(_: Builtin.Int32)Removed Int32.arrayBoundValueRemoved Int32.convertFromIntegerLiteral(Int32) -> Int32 [static]Removed Int32.from(IntMax) -> Int32 [static]Removed Int64.init(_: Builtin.Int64)Removed Int64.arrayBoundValueRemoved Int64.convertFromIntegerLiteral(Int64) -> Int64 [static]Removed Int64.from(IntMax) -> Int64 [static]Removed Int8.init(_: Builtin.Int8)Removed Int8.arrayBoundValueRemoved Int8.convertFromIntegerLiteral(Int8) -> Int8 [static]Removed Int8.from(IntMax) -> Int8 [static]Removed IntegerLiteralConvertible.convertFromIntegerLiteral(IntegerLiteralType) -> Self [class]Removed NilLiteralConvertible.convertFromNilLiteral() -> Self [class]Removed Optional.convertFromNilLiteral() -> T? [static]Removed RawRepresentable.fromRaw(Raw) -> Self? [class]Removed RawRepresentable.toRaw() -> RawRemoved Slice.convertFromArrayLiteral(T) -> Slice<T> [static]Removed StaticString.convertFromExtendedGraphemeClusterLiteral(StaticString) -> StaticString [static]Removed StaticString.convertFromStringLiteral(StaticString) -> StaticString [static]Removed StaticString.startRemoved StaticStringTypeRemoved String.convertFromExtendedGraphemeClusterLiteral(String) -> String [static]Removed String.convertFromStringLiteral(String) -> String [static]Removed String.init(seq: S)Removed String.UnicodeScalarView.compare(String.UnicodeScalarView) -> IntRemoved StringElementTypeRemoved StringElementType.fromUTF16CodeUnit(CodeUnit) -> Self [class]Removed StringElementType.toUTF16CodeUnit() -> CodeUnit [class]Removed StringLiteralConvertible.convertFromStringLiteral(StringLiteralType) -> Self [class]Removed UInt.init(_: Builtin.Word)Removed UInt.arrayBoundValueRemoved UInt.convertFromIntegerLiteral(UInt) -> UInt [static]Removed UInt.from(UIntMax) -> UInt [static]Removed UInt16.init(_: Builtin.Int16)Removed UInt16.arrayBoundValueRemoved UInt16.convertFromIntegerLiteral(UInt16) -> UInt16 [static]Removed UInt16.from(UIntMax) -> UInt16 [static]Removed UInt32.init(_: Builtin.Int32)Removed UInt32.arrayBoundValueRemoved UInt32.convertFromIntegerLiteral(UInt32) -> UInt32 [static]Removed UInt32.from(UIntMax) -> UInt32 [static]Removed UInt64.init(_: Builtin.Int64)Removed UInt64.arrayBoundValueRemoved UInt64.convertFromIntegerLiteral(UInt64) -> UInt64 [static]Removed UInt64.from(UIntMax) -> UInt64 [static]Removed UInt8.init(_: Builtin.Int8)Removed UInt8.arrayBoundValueRemoved UInt8.convertFromIntegerLiteral(UInt8) -> UInt8 [static]Removed UInt8.from(UIntMax) -> UInt8 [static]Removed UnicodeScalar.convertFromExtendedGraphemeClusterLiteral(String) -> UnicodeScalar [static]Removed UnsafeMutablePointer.convertFromNilLiteral() -> UnsafeMutablePointer<T> [static]Removed UnsafePointer.convertFromNilLiteral() -> UnsafePointer<T> [static]Removed ??(T?,() -> T) -> TRemoved ??(T?,() -> T?) -> T?Removed ArrayBoundType.ArrayBoundRemoved Int.ArrayBoundRemoved Int16.ArrayBoundRemoved Int32.ArrayBoundRemoved Int64.ArrayBoundRemoved Int8.ArrayBoundRemoved RawRepresentable.RawRemoved UInt.ArrayBoundRemoved UInt16.ArrayBoundRemoved UInt32.ArrayBoundRemoved UInt64.ArrayBoundRemoved UInt8.ArrayBoundRemoved assert(() -> Bool,() -> Str, StaticString, UWord)Removed assert(() -> Bool, StaticString, StaticString, UWord)Removed assert(() -> T,() -> Str, StaticString, UWord)Removed assertionFailure(StaticString, StaticString, UWord)Removed emptyNSSwiftArrayRemoved enumerate(Seq) -> EnumerateGenerator<Seq.Generator>Removed fatalError(StaticString, StaticString, UWord)Removed indices(Seq) -> Range<Seq.Index>Removed precondition(() -> Bool,() -> Str, StaticString, UWord)Removed precondition(() -> Bool, StaticString, StaticString, UWord)Removed precondition(() -> T,() -> Str, StaticString, UWord)Removed preconditionFailure(StaticString, StaticString, UWord)Removed sorted(C) -> CRemoved sorted(C,(C.Generator.Element, C.Generator.Element) -> Bool) -> CRemoved split(Seq,(Seq.Generator.Element) -> R, Int, Bool) -> [Seq.SubSlice]Added Array.init(_fromCocoaArray: _SwiftNSArrayRequiredOverridesType, noCopy: Bool)Added Array.init(arrayLiteral: T)Added ArrayLiteralConvertible.init(arrayLiteral: Element)Added AutoreleasingUnsafeMutablePointer.init(nilLiteral: ())Added Bool.init(_builtinBooleanLiteral: Builtin.Int1)Added Bool.init(booleanLiteral: Bool)Added BooleanLiteralConvertible.init(booleanLiteral: BooleanLiteralType)Added CFunctionPointer.init(nilLiteral: ())Added COpaquePointer.init(nilLiteral: ())Added Character.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added Character.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added Character.init(extendedGraphemeClusterLiteral: Character)Added Character.init(unicodeScalarLiteral: Character)Added CharacterLiteralConvertible.init(characterLiteral: CharacterLiteralType)Added ContiguousArray.init(arrayLiteral: T)Added Dictionary.init()Added Dictionary.init(dictionaryLiteral: (Key, Value))Added DictionaryLiteralConvertible.init(dictionaryLiteral: (Key, Value))Added Double.init(_builtinFloatLiteral: Builtin.FPIEEE64)Added Double.init(_builtinIntegerLiteral: Builtin.Int2048)Added Double.init(floatLiteral: Double)Added Double.init(integerLiteral: Int64)Added EnumerateSequence [struct]Added EnumerateSequence.init(_: Base)Added EnumerateSequence.baseAdded EnumerateSequence.generate() -> EnumerateGenerator<Base.Generator>Added ExtendedGraphemeClusterLiteralConvertible.init(extendedGraphemeClusterLiteral: ExtendedGraphemeClusterLiteralType)Added Float.init(_builtinFloatLiteral: Builtin.FPIEEE64)Added Float.init(_builtinIntegerLiteral: Builtin.Int2048)Added Float.init(floatLiteral: Float)Added Float.init(integerLiteral: Int64)Added FloatLiteralConvertible.init(floatLiteral: FloatLiteralType)Added HeapBuffer.init(_: AnyClass, _: Value, _: Int)Added ImplicitlyUnwrappedOptional.init(nilLiteral: ())Added Int.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int.init(integerLiteral: Int)Added Int.init(truncatingBitPattern: Int64)Added Int.init(truncatingBitPattern: UInt64)Added Int16.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int16.init(integerLiteral: Int16)Added Int16.init(truncatingBitPattern: Int)Added Int16.init(truncatingBitPattern: Int32)Added Int16.init(truncatingBitPattern: Int64)Added Int16.init(truncatingBitPattern: UInt)Added Int16.init(truncatingBitPattern: UInt32)Added Int16.init(truncatingBitPattern: UInt64)Added Int32.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int32.init(integerLiteral: Int32)Added Int32.init(truncatingBitPattern: Int)Added Int32.init(truncatingBitPattern: Int64)Added Int32.init(truncatingBitPattern: UInt)Added Int32.init(truncatingBitPattern: UInt64)Added Int64.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int64.init(integerLiteral: Int64)Added Int8.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int8.init(integerLiteral: Int8)Added Int8.init(truncatingBitPattern: Int)Added Int8.init(truncatingBitPattern: Int16)Added Int8.init(truncatingBitPattern: Int32)Added Int8.init(truncatingBitPattern: Int64)Added Int8.init(truncatingBitPattern: UInt)Added Int8.init(truncatingBitPattern: UInt16)Added Int8.init(truncatingBitPattern: UInt32)Added Int8.init(truncatingBitPattern: UInt64)Added IntegerLiteralConvertible.init(integerLiteral: IntegerLiteralType)Added NilLiteralConvertible.init(nilLiteral: ())Added Optional.init(nilLiteral: ())Added RawRepresentable.rawValueAdded RawRepresentable.init(rawValue: RawValue)Added Slice.init(arrayLiteral: T)Added StaticString.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added StaticString.init(_builtinStringLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added StaticString.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added StaticString.debugDescriptionAdded StaticString.descriptionAdded StaticString.init(extendedGraphemeClusterLiteral: StaticString)Added StaticString.hasPointerRepresentationAdded StaticString.init(stringLiteral: StaticString)Added StaticString.unicodeScalarAdded StaticString.init(unicodeScalar: Builtin.Int32)Added StaticString.init(unicodeScalarLiteral: StaticString)Added StaticString.utf8StartAdded StaticString.withUTF8Buffer((UnsafeBufferPointer<UInt8>) -> R) -> RAdded StrideThrough.getMirror() -> MirrorTypeAdded StrideTo.getMirror() -> MirrorTypeAdded String.init(_: S)Added String.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added String.init(_builtinStringLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added String.init(_builtinUTF16StringLiteral: Builtin.RawPointer, numberOfCodeUnits: Builtin.Word)Added String.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added String.convertFromStringInterpolationSegment(Bool) -> String [static]Added String.convertFromStringInterpolationSegment(Character) -> String [static]Added String.convertFromStringInterpolationSegment(Float32) -> String [static]Added String.convertFromStringInterpolationSegment(Float64) -> String [static]Added String.convertFromStringInterpolationSegment(Int) -> String [static]Added String.convertFromStringInterpolationSegment(Int16) -> String [static]Added String.convertFromStringInterpolationSegment(Int32) -> String [static]Added String.convertFromStringInterpolationSegment(Int64) -> String [static]Added String.convertFromStringInterpolationSegment(Int8) -> String [static]Added String.convertFromStringInterpolationSegment(String) -> String [static]Added String.convertFromStringInterpolationSegment(UInt) -> String [static]Added String.convertFromStringInterpolationSegment(UInt16) -> String [static]Added String.convertFromStringInterpolationSegment(UInt32) -> String [static]Added String.convertFromStringInterpolationSegment(UInt64) -> String [static]Added String.convertFromStringInterpolationSegment(UInt8) -> String [static]Added String.convertFromStringInterpolationSegment(UnicodeScalar) -> String [static]Added String.init(extendedGraphemeClusterLiteral: String)Added String.init(stringLiteral: String)Added String.init(unicodeScalarLiteral: String)Added StringLiteralConvertible.init(stringLiteral: StringLiteralType)Added UInt.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt.init(integerLiteral: UInt)Added UInt.init(truncatingBitPattern: Int64)Added UInt.init(truncatingBitPattern: UInt64)Added UInt16.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt16.init(integerLiteral: UInt16)Added UInt16.init(truncatingBitPattern: Int)Added UInt16.init(truncatingBitPattern: Int32)Added UInt16.init(truncatingBitPattern: Int64)Added UInt16.init(truncatingBitPattern: UInt)Added UInt16.init(truncatingBitPattern: UInt32)Added UInt16.init(truncatingBitPattern: UInt64)Added UInt32.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt32.init(integerLiteral: UInt32)Added UInt32.init(truncatingBitPattern: Int)Added UInt32.init(truncatingBitPattern: Int64)Added UInt32.init(truncatingBitPattern: UInt)Added UInt32.init(truncatingBitPattern: UInt64)Added UInt64.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt64.init(integerLiteral: UInt64)Added UInt8.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt8.init(integerLiteral: UInt8)Added UInt8.init(truncatingBitPattern: Int)Added UInt8.init(truncatingBitPattern: Int16)Added UInt8.init(truncatingBitPattern: Int32)Added UInt8.init(truncatingBitPattern: Int64)Added UInt8.init(truncatingBitPattern: UInt)Added UInt8.init(truncatingBitPattern: UInt16)Added UInt8.init(truncatingBitPattern: UInt32)Added UInt8.init(truncatingBitPattern: UInt64)Added UnicodeScalar.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added UnicodeScalar.init(unicodeScalarLiteral: UnicodeScalar)Added UnicodeScalarLiteralConvertibleAdded UnicodeScalarLiteralConvertible.init(unicodeScalarLiteral: UnicodeScalarLiteralType)Added UnsafeMutablePointer.init(nilLiteral: ())Added UnsafePointer.init(nilLiteral: ())Added Int.DistanceAdded Int16.DistanceAdded Int32.DistanceAdded Int64.DistanceAdded Int8.DistanceAdded RawRepresentable.RawValueAdded UInt.DistanceAdded UInt16.DistanceAdded UInt32.DistanceAdded UInt64.DistanceAdded UInt8.DistanceAdded UnicodeScalarLiteralConvertible.UnicodeScalarLiteralTypeAdded UnicodeScalarTypeAdded assert(() -> Bool,() -> String, StaticString, UWord)Added assertionFailure(() -> String, StaticString, UWord)Added enumerate(Seq) -> EnumerateSequence<Seq>Added fatalError(() -> String, StaticString, UWord)Added indices(C) -> Range<C.Index>Added precondition(() -> Bool,() -> String, StaticString, UWord)Added preconditionFailure(() -> String, StaticString, UWord)Added sort(ContiguousArray<T>)Added sort(ContiguousArray<T>,(T, T) -> Bool)Added split(S,(S.Generator.Element) -> R, Int, Bool) -> [S.SubSlice]Added unsafeAddressOf(AnyObject) -> UnsafePointer<Void>Added unsafeDowncast(AnyObject) -> TModified AbsoluteValuable.abs(Self) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` class func abs(_ _: Self) -> Self ``` | iOS 8.0 |
| To | ``` class func abs(_ x: Self) -> Self ``` | iOS 8.1 |

Modified Array.extend(S)

|  | Declaration |
| --- | --- |
| From | ``` mutating func extend<S : SequenceType where T == T>(_ sequence: S) ``` |
| To | ``` mutating func extend<S : SequenceType where T == T>(_ newElements: S) ``` |

Modified Array.replaceRange(Range<Int>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newValues: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C) ``` |

Modified Array.splice(S, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` mutating func splice<S : CollectionType where T == T>(_ s: S, atIndex i: Int) ``` |
| To | ``` mutating func splice<S : CollectionType where T == T>(_ newElements: S, atIndex i: Int) ``` |

Modified ArrayType.insert(Self.Generator.Element, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` mutating func insert(_ newElement: Self.Generator.Element, atIndex atIndex: Int) ``` |
| To | ``` mutating func insert(_ newElement: Self.Generator.Element, atIndex i: Int) ``` |

Modified AutoreleasingUnsafeMutablePointer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct AutoreleasingUnsafeMutablePointer<T> : Equatable, NilLiteralConvertible, _PointerType {     let value: Builtin.RawPointer     init(_ value: Builtin.RawPointer)     var memory: T { get nonmutating set }     subscript (i: Int) -> T { get }     static func convertFromNilLiteral() -> AutoreleasingUnsafeMutablePointer<T>     static func null() -> AutoreleasingUnsafeMutablePointer<T>     init()     init<U>(_ ptr: UnsafeMutablePointer<U>)     init<U>(_ ptr: UnsafePointer<U>) } ``` |
| To | ``` struct AutoreleasingUnsafeMutablePointer<T> : Equatable, NilLiteralConvertible, _PointerType {     let value: Builtin.RawPointer     init(_ value: Builtin.RawPointer)     var memory: T { get nonmutating set }     subscript (i: Int) -> T { get }     init(nilLiteral nilLiteral: ())     static func null() -> AutoreleasingUnsafeMutablePointer<T>     init()     init<U>(_ ptr: UnsafeMutablePointer<U>)     init<U>(_ ptr: UnsafePointer<U>) } ``` |

Modified BidirectionalReverseView [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BidirectionalReverseView<T : CollectionType where T.Index : BidirectionalIndexType> : CollectionType {     typealias Index = ReverseBidirectionalIndex<T.Index>     typealias Generator = IndexingGenerator<BidirectionalReverseView<T>>     func generate() -> IndexingGenerator<BidirectionalReverseView<T>>     var startIndex: Index { get }     var endIndex: Index { get }     subscript (i: Index) -> T.Generator.Element { get } } ``` |
| To | ``` struct BidirectionalReverseView<T : CollectionType where T.Index : BidirectionalIndexType> : CollectionType {     typealias Index = ReverseBidirectionalIndex<T.Index>     typealias Generator = IndexingGenerator<BidirectionalReverseView<T>>     func generate() -> IndexingGenerator<BidirectionalReverseView<T>>     var startIndex: Index { get }     var endIndex: Index { get }     subscript (position: Index) -> T.Generator.Element { get } } ``` |

Modified BitwiseOperationsType.&(Self, _: Self) -> Self [class]

|  | Declaration |
| --- | --- |
| From | ``` func &(_ _: Self, _ _: Self) -> Self ``` |
| To | ``` func &(_ lhs: Self, _ rhs: Self) -> Self ``` |

Modified BitwiseOperationsType.^(Self, _: Self) -> Self [class]

|  | Declaration |
| --- | --- |
| From | ``` func ^(_ _: Self, _ _: Self) -> Self ``` |
| To | ``` func ^(_ lhs: Self, _ rhs: Self) -> Self ``` |

Modified BitwiseOperationsType.|(Self, _: Self) -> Self [class]

|  | Declaration |
| --- | --- |
| From | ``` func |(_ _: Self, _ _: Self) -> Self ``` |
| To | ``` func |(_ lhs: Self, _ rhs: Self) -> Self ``` |

Modified BitwiseOperationsType.~(Self) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` prefix func ~(_ _: Self) -> Self ``` | iOS 8.0 |
| To | ``` prefix func ~(_ x: Self) -> Self ``` | iOS 8.1 |

Modified Bool.init(_: T)

|  | Declaration |
| --- | --- |
| From | ``` init<T : BooleanType>(_ v: T) ``` |
| To | ``` init<T : BooleanType>(_ value: T) ``` |

Modified CFunctionPointer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CFunctionPointer<T> : Equatable, Hashable, NilLiteralConvertible {     var value: COpaquePointer     init()     init(_ value: COpaquePointer)     static func null() -> CFunctionPointer<T>     var hashValue: Int { get }     static func convertFromNilLiteral() -> CFunctionPointer<T> } ``` |
| To | ``` struct CFunctionPointer<T> : Equatable, Hashable, NilLiteralConvertible {     var value: COpaquePointer     init()     init(_ value: COpaquePointer)     static func null() -> CFunctionPointer<T>     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } ``` |

Modified COpaquePointer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct COpaquePointer : Equatable, Hashable, NilLiteralConvertible {     var value: Builtin.RawPointer     init()     init(_ v: Builtin.RawPointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<T>(_ value: UnsafePointer<T>)     init<T>(_ value: UnsafeMutablePointer<T>)     static func null() -> COpaquePointer     var hashValue: Int { get }     static func convertFromNilLiteral() -> COpaquePointer } ``` |
| To | ``` struct COpaquePointer : Equatable, Hashable, NilLiteralConvertible {     var value: Builtin.RawPointer     init()     init(_ v: Builtin.RawPointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<T>(_ value: UnsafePointer<T>)     init<T>(_ value: UnsafeMutablePointer<T>)     static func null() -> COpaquePointer     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } ``` |

Modified COpaquePointer.init(_: CFunctionPointer<T>)

|  | Declaration |
| --- | --- |
| From | ``` init<T>(_ from: CFunctionPointer<T>) ``` |
| To | ``` init<T>(_ value: CFunctionPointer<T>) ``` |

Modified Character [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum Character : ExtendedGraphemeClusterLiteralConvertible, Equatable, Hashable, Comparable {     case LargeRepresentation(OnHeap<String>)     case SmallRepresentation     init(_ scalar: UnicodeScalar)     static func convertFromExtendedGraphemeClusterLiteral(_ value: Character) -> Character     init(_ s: String)     struct SmallUTF16 : CollectionType {         init(_ u8: UInt64)         var startIndex: Int { get }         var endIndex: Int { get }         subscript (i: Int) -> CodeUnit { get }         func generate() -> IndexingGenerator<Character.SmallUTF16>         var count: UInt16         var data: UInt64     }     var hashValue: Int { get }     typealias UTF16View = String.UTF16View     var utf16: UTF16View { get } } ``` |
| To | ``` enum Character : ExtendedGraphemeClusterLiteralConvertible, Equatable, Hashable, Comparable {     case LargeRepresentation(OnHeap<String>)     case SmallRepresentation     init(_ scalar: UnicodeScalar)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: Character)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: Character)     init(_ s: String)     var hashValue: Int { get }     typealias UTF16View = String.UTF16View     var utf16: UTF16View { get } } ``` |

Modified CollectionOfOne [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CollectionOfOne<T> : CollectionType {     typealias Index = Bit     init(_ element: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> GeneratorOfOne<T>     subscript (i: Index) -> T { get }     let element: T } ``` |
| To | ``` struct CollectionOfOne<T> : CollectionType {     typealias Index = Bit     init(_ element: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> GeneratorOfOne<T>     subscript (position: Index) -> T { get }     let element: T } ``` |

Modified ContiguousArray.extend(S)

|  | Declaration |
| --- | --- |
| From | ``` mutating func extend<S : SequenceType where T == T>(_ sequence: S) ``` |
| To | ``` mutating func extend<S : SequenceType where T == T>(_ newElements: S) ``` |

Modified ContiguousArray.replaceRange(Range<Int>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newValues: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C) ``` |

Modified ContiguousArray.splice(S, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` mutating func splice<S : CollectionType where T == T>(_ s: S, atIndex i: Int) ``` |
| To | ``` mutating func splice<S : CollectionType where T == T>(_ newElements: S, atIndex i: Int) ``` |

Modified Dictionary [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Dictionary<Key : Hashable, Value> : CollectionType, DictionaryLiteralConvertible {     typealias Element = (Key, Value)     typealias Index = DictionaryIndex<Key, Value>     init(minimumCapacity minimumCapacity: Int = default)     var startIndex: DictionaryIndex<Key, Value> { get }     var endIndex: DictionaryIndex<Key, Value> { get }     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>?     subscript (i: DictionaryIndex<Key, Value>) -> (Key, Value) { get }     subscript (key: Key) -> Value?     mutating func updateValue(_ value: Value, forKey key: Key) -> Value?     mutating func removeAtIndex(_ index: DictionaryIndex<Key, Value>)     mutating func removeValueForKey(_ key: Key) -> Value?     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<Key, Value>     static func convertFromDictionaryLiteral(_ elements: (Key, Value)...) -> [Key : Value]     var isEmpty: Bool { get }     var keys: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Key>> { get }     var values: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Value>> { get } } ``` |
| To | ``` struct Dictionary<Key : Hashable, Value> : CollectionType, DictionaryLiteralConvertible {     typealias Element = (Key, Value)     typealias Index = DictionaryIndex<Key, Value>     init()     init(minimumCapacity minimumCapacity: Int)     var startIndex: DictionaryIndex<Key, Value> { get }     var endIndex: DictionaryIndex<Key, Value> { get }     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>?     subscript (position: DictionaryIndex<Key, Value>) -> (Key, Value) { get }     subscript (key: Key) -> Value?     mutating func updateValue(_ value: Value, forKey key: Key) -> Value?     mutating func removeAtIndex(_ index: DictionaryIndex<Key, Value>)     mutating func removeValueForKey(_ key: Key) -> Value?     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<Key, Value>     init(dictionaryLiteral elements: (Key, Value)...)     var isEmpty: Bool { get }     var keys: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Key>> { get }     var values: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Value>> { get } } ``` |

Modified Dictionary.init(minimumCapacity: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(minimumCapacity minimumCapacity: Int = default) ``` |
| To | ``` init(minimumCapacity minimumCapacity: Int) ``` |

Modified Double.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified EmptyCollection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EmptyCollection<T> : CollectionType {     typealias Index = Int     init()     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> EmptyGenerator<T>     subscript (i: Index) -> T { get } } ``` |
| To | ``` struct EmptyCollection<T> : CollectionType {     typealias Index = Int     init()     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> EmptyGenerator<T>     subscript (position: Index) -> T { get } } ``` |

Modified ExtendedGraphemeClusterLiteralConvertible

|  | Protocols |
| --- | --- |
| From | -- |
| To | UnicodeScalarLiteralConvertible |

Modified FilterCollectionView [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct FilterCollectionView<Base : CollectionType> : CollectionType {     typealias Index = FilterCollectionViewIndex<Base>     init(_ base: Base, includeElement includeElement: (Base.Generator.Element) -> Bool)     var startIndex: FilterCollectionViewIndex<Base> { get }     var endIndex: FilterCollectionViewIndex<Base> { get }     subscript (index: FilterCollectionViewIndex<Base>) -> Base.Generator.Element { get }     func generate() -> FilterGenerator<Base.Generator> } ``` |
| To | ``` struct FilterCollectionView<Base : CollectionType> : CollectionType {     typealias Index = FilterCollectionViewIndex<Base>     init(_ base: Base, includeElement predicate: (Base.Generator.Element) -> Bool)     var startIndex: FilterCollectionViewIndex<Base> { get }     var endIndex: FilterCollectionViewIndex<Base> { get }     subscript (position: FilterCollectionViewIndex<Base>) -> Base.Generator.Element { get }     func generate() -> FilterGenerator<Base.Generator> } ``` |

Modified FilterCollectionView.init(_: Base, includeElement:(Base.Generator.Element) -> Bool)

|  | Declaration |
| --- | --- |
| From | ``` init(_ base: Base, includeElement includeElement: (Base.Generator.Element) -> Bool) ``` |
| To | ``` init(_ base: Base, includeElement predicate: (Base.Generator.Element) -> Bool) ``` |

Modified Float.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified GeneratorOf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GeneratorOf<T> : GeneratorType, SequenceType {     init(_ next: () -> T?)     init<G : GeneratorType where T == T>(_ self_: G)     mutating func next() -> T?     func generate() -> GeneratorOf<T> } ``` |
| To | ``` struct GeneratorOf<T> : GeneratorType, SequenceType {     init(_ nextElement: () -> T?)     init<G : GeneratorType where T == T>(_ base: G)     mutating func next() -> T?     func generate() -> GeneratorOf<T> } ``` |

Modified GeneratorOf.init(_: () -> T?)

|  | Declaration |
| --- | --- |
| From | ``` init(_ next: () -> T?) ``` |
| To | ``` init(_ nextElement: () -> T?) ``` |

Modified GeneratorOf.init(_: G)

|  | Declaration |
| --- | --- |
| From | ``` init<G : GeneratorType where T == T>(_ self_: G) ``` |
| To | ``` init<G : GeneratorType where T == T>(_ base: G) ``` |

Modified GeneratorOfOne [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct GeneratorOfOne<T> : GeneratorType, SequenceType {     init(_ elements: T?)     func generate() -> GeneratorOfOne<T>     mutating func next() -> T?     var elements: T? } ``` |
| To | ``` struct GeneratorOfOne<T> : GeneratorType, SequenceType {     init(_ element: T?)     func generate() -> GeneratorOfOne<T>     mutating func next() -> T?     var elements: T? } ``` |

Modified GeneratorOfOne.init(_: T?)

|  | Declaration |
| --- | --- |
| From | ``` init(_ elements: T?) ``` |
| To | ``` init(_ element: T?) ``` |

Modified HeapBuffer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct HeapBuffer<Value, Element> : Equatable {     typealias Storage = HeapBufferStorage<Value, Element>     let storage: HeapBufferStorage<Value, Element>?     var baseAddress: UnsafeMutablePointer<Element> { get }     init()     init(_ storage: HeapBufferStorage<Value, Element>)     init(_ storageClass: HeapBufferStorageBase.Type, _ initializer: Value, _ capacity: Int)     var value: Value { get nonmutating set }     var hasStorage: Bool { get }     subscript (i: Int) -> Element { get nonmutating set }     static func fromNativeObject(_ x: Builtin.NativeObject) -> HeapBuffer<Value, Element>     mutating func isUniquelyReferenced() -> Bool } ``` |
| To | ``` struct HeapBuffer<Value, Element> : Equatable {     typealias Storage = HeapBufferStorage<Value, Element>     let storage: HeapBufferStorage<Value, Element>?     var baseAddress: UnsafeMutablePointer<Element> { get }     init()     init(_ storage: HeapBufferStorage<Value, Element>)     init(_ storageClass: AnyClass, _ initializer: Value, _ capacity: Int)     var value: Value { get nonmutating set }     var hasStorage: Bool { get }     subscript (i: Int) -> Element { get nonmutating set }     static func fromNativeObject(_ x: Builtin.NativeObject) -> HeapBuffer<Value, Element>     mutating func isUniquelyReferenced() -> Bool } ``` |

Modified HeapBufferStorage

|  | Superclasses |
| --- | --- |
| From | HeapBufferStorageBase |
| To | -- |

Modified ImplicitlyUnwrappedOptional [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ImplicitlyUnwrappedOptional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     init(_ v: T?)     static func convertFromNilLiteral() -> T!     func map<U>(_ f: (T) -> U) -> U!     func getMirror() -> MirrorType } ``` |
| To | ``` enum ImplicitlyUnwrappedOptional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     init(_ v: T?)     init(nilLiteral nilLiteral: ())     func map<U>(_ f: (T) -> U) -> U!     func getMirror() -> MirrorType } ``` |

Modified Int [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Int : SignedIntegerType {     var value: Builtin.Word     init()     init(_ v: Builtin.Word)     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     static func convertFromIntegerLiteral(_ value: Int) -> Int     typealias ArrayBound = Int     var arrayBoundValue: Int { get }     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } ``` |
| To | ``` struct Int : SignedIntegerType {     var value: Builtin.Word     typealias Distance = Int     init()     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } ``` |

Modified Int.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified Int.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified Int.advancedBy(Distance) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> Int ``` | iOS 8.1 |

Modified Int.distanceTo(Int) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: Int) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: Int) -> Distance ``` | iOS 8.1 |

Modified Int16 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Int16 : SignedIntegerType {     var value: Builtin.Int16     init()     init(_ v: Builtin.Int16)     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     static func convertFromIntegerLiteral(_ value: Int16) -> Int16     typealias ArrayBound = Int16     var arrayBoundValue: Int16 { get }     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } ``` |
| To | ``` struct Int16 : SignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int16)     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } ``` |

Modified Int16.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified Int16.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified Int16.advancedBy(Distance) -> Int16

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int16 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> Int16 ``` | iOS 8.1 |

Modified Int16.distanceTo(Int16) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: Int16) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: Int16) -> Distance ``` | iOS 8.1 |

Modified Int32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Int32 : SignedIntegerType {     var value: Builtin.Int32     init()     init(_ v: Builtin.Int32)     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     static func convertFromIntegerLiteral(_ value: Int32) -> Int32     typealias ArrayBound = Int32     var arrayBoundValue: Int32 { get }     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } ``` |
| To | ``` struct Int32 : SignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int32)     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } ``` |

Modified Int32.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified Int32.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified Int32.advancedBy(Distance) -> Int32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int32 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> Int32 ``` | iOS 8.1 |

Modified Int32.distanceTo(Int32) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: Int32) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: Int32) -> Distance ``` | iOS 8.1 |

Modified Int64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Int64 : SignedIntegerType {     var value: Builtin.Int64     init()     init(_ v: Builtin.Int64)     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     static func convertFromIntegerLiteral(_ value: Int64) -> Int64     typealias ArrayBound = Int64     var arrayBoundValue: Int64 { get }     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } ``` |
| To | ``` struct Int64 : SignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64)     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } ``` |

Modified Int64.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified Int64.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified Int64.advancedBy(Distance) -> Int64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int64 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> Int64 ``` | iOS 8.1 |

Modified Int64.distanceTo(Int64) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: Int64) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: Int64) -> Distance ``` | iOS 8.1 |

Modified Int8 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Int8 : SignedIntegerType {     var value: Builtin.Int8     init()     init(_ v: Builtin.Int8)     init(_ value: Int8)     static func convertFromIntegerLiteral(_ value: Int8) -> Int8     typealias ArrayBound = Int8     var arrayBoundValue: Int8 { get }     static var max: Int8 { get }     static var min: Int8 { get } } ``` |
| To | ``` struct Int8 : SignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: Int8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int8)     static var max: Int8 { get }     static var min: Int8 { get } } ``` |

Modified Int8.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified Int8.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified Int8.advancedBy(Distance) -> Int8

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int8 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> Int8 ``` | iOS 8.1 |

Modified Int8.distanceTo(Int8) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: Int8) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: Int8) -> Distance ``` | iOS 8.1 |

Modified LazyBidirectionalCollection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LazyBidirectionalCollection<S : CollectionType where S.Index : BidirectionalIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     var last: S.Generator.Element? { get }     subscript (i: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` |
| To | ``` struct LazyBidirectionalCollection<S : CollectionType where S.Index : BidirectionalIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     var last: S.Generator.Element? { get }     subscript (position: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` |

Modified LazyForwardCollection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LazyForwardCollection<S : CollectionType where S.Index : ForwardIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     subscript (i: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` |
| To | ``` struct LazyForwardCollection<S : CollectionType where S.Index : ForwardIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     subscript (position: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` |

Modified LazyRandomAccessCollection [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct LazyRandomAccessCollection<S : CollectionType where S.Index : RandomAccessIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     var last: S.Generator.Element? { get }     subscript (i: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` |
| To | ``` struct LazyRandomAccessCollection<S : CollectionType where S.Index : RandomAccessIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     var last: S.Generator.Element? { get }     subscript (position: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` |

Modified MapCollectionView [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MapCollectionView<Base : CollectionType, T> : CollectionType {     var startIndex: Base.Index { get }     var endIndex: Base.Index { get }     subscript (index: Base.Index) -> T { get }     func generate() -> MapSequenceGenerator<Base.Generator, T> } ``` |
| To | ``` struct MapCollectionView<Base : CollectionType, T> : CollectionType {     var startIndex: Base.Index { get }     var endIndex: Base.Index { get }     subscript (position: Base.Index) -> T { get }     func generate() -> MapSequenceGenerator<Base.Generator, T> } ``` |

Modified Optional [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum Optional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     func map<U>(_ f: (T) -> U) -> U?     func getMirror() -> MirrorType     static func convertFromNilLiteral() -> T? } ``` |
| To | ``` enum Optional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     func map<U>(_ f: (T) -> U) -> U?     func getMirror() -> MirrorType     init(nilLiteral nilLiteral: ()) } ``` |

Modified PermutationGenerator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct PermutationGenerator<C : CollectionType, Indices : SequenceType where C.Index == C.Index> : GeneratorType, SequenceType {     var seq: C     var indices: Indices.Generator     typealias Element = C.Generator.Element     mutating func next() -> Element?     typealias Generator = PermutationGenerator<C, Indices>     func generate() -> PermutationGenerator<C, Indices>     init(elements seq: C, indices indices: Indices) } ``` |
| To | ``` struct PermutationGenerator<C : CollectionType, Indices : SequenceType where C.Index == C.Index> : GeneratorType, SequenceType {     var seq: C     var indices: Indices.Generator     typealias Element = C.Generator.Element     mutating func next() -> Element?     typealias Generator = PermutationGenerator<C, Indices>     func generate() -> PermutationGenerator<C, Indices>     init(elements elements: C, indices indices: Indices) } ``` |

Modified PermutationGenerator.init(elements: C, indices: Indices)

|  | Declaration |
| --- | --- |
| From | ``` init(elements seq: C, indices indices: Indices) ``` |
| To | ``` init(elements elements: C, indices indices: Indices) ``` |

Modified RandomAccessReverseView [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct RandomAccessReverseView<T : CollectionType where T.Index : RandomAccessIndexType> : CollectionType {     typealias Index = ReverseRandomAccessIndex<T.Index>     typealias Generator = IndexingGenerator<RandomAccessReverseView<T>>     func generate() -> IndexingGenerator<RandomAccessReverseView<T>>     var startIndex: Index { get }     var endIndex: Index { get }     subscript (i: Index) -> T.Generator.Element { get } } ``` |
| To | ``` struct RandomAccessReverseView<T : CollectionType where T.Index : RandomAccessIndexType> : CollectionType {     typealias Index = ReverseRandomAccessIndex<T.Index>     typealias Generator = IndexingGenerator<RandomAccessReverseView<T>>     func generate() -> IndexingGenerator<RandomAccessReverseView<T>>     var startIndex: Index { get }     var endIndex: Index { get }     subscript (position: Index) -> T.Generator.Element { get } } ``` |

Modified Range [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Range<T : ForwardIndexType> : Equatable, CollectionType, Printable, DebugPrintable {     init(_ x: Range<T>)     init(start start: T, end end: T)     var isEmpty: Bool { get }     typealias Index = T     typealias Slice = Range<T>     subscript (i: T) -> T { get }     subscript (_: T._DisabledRangeIndex) -> T { get }     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T     var description: String { get }     var debugDescription: String { get } } ``` |
| To | ``` struct Range<T : ForwardIndexType> : Equatable, CollectionType, Printable, DebugPrintable {     init(_ x: Range<T>)     init(start start: T, end end: T)     var isEmpty: Bool { get }     typealias Index = T     typealias Slice = Range<T>     subscript (position: T) -> T { get }     subscript (_: T._DisabledRangeIndex) -> T { get }     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T     var description: String { get }     var debugDescription: String { get } } ``` |

Modified RangeReplaceableCollectionType.replaceRange(Range<Self.Index>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` mutating func replaceRange<C : CollectionType where `Self`.Generator.Element == Self.Generator.Element>(_ subRange: Range<Self.Index>, with newValues: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where `Self`.Generator.Element == Self.Generator.Element>(_ subRange: Range<Self.Index>, with newElements: C) ``` |

Modified RangeReplaceableCollectionType.splice(S, atIndex: Self.Index)

|  | Declaration |
| --- | --- |
| From | ``` mutating func splice<S : CollectionType where `Self`.Generator.Element == Self.Generator.Element>(_ newValues: S, atIndex i: Self.Index) ``` |
| To | ``` mutating func splice<S : CollectionType where `Self`.Generator.Element == Self.Generator.Element>(_ newElements: S, atIndex i: Self.Index) ``` |

Modified Repeat [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Repeat<T> : CollectionType {     typealias Index = Int     init(count count: Int, repeatedValue repeatedValue: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> IndexingGenerator<Repeat<T>>     subscript (i: Int) -> T { get }     var count: Int     let repeatedValue: T } ``` |
| To | ``` struct Repeat<T> : CollectionType {     typealias Index = Int     init(count count: Int, repeatedValue repeatedValue: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> IndexingGenerator<Repeat<T>>     subscript (position: Int) -> T { get }     var count: Int     let repeatedValue: T } ``` |

Modified SequenceOf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SequenceOf<T> : SequenceType {     init<G : GeneratorType where T == T>(_ generate: () -> G)     init<S : SequenceType where T == T>(_ self_: S)     func generate() -> GeneratorOf<T> } ``` |
| To | ``` struct SequenceOf<T> : SequenceType {     init<G : GeneratorType where T == T>(_ makeUnderlyingGenerator: () -> G)     init<S : SequenceType where T == T>(_ base: S)     func generate() -> GeneratorOf<T> } ``` |

Modified SequenceOf.init(_: () -> G)

|  | Declaration |
| --- | --- |
| From | ``` init<G : GeneratorType where T == T>(_ generate: () -> G) ``` |
| To | ``` init<G : GeneratorType where T == T>(_ makeUnderlyingGenerator: () -> G) ``` |

Modified SequenceOf.init(_: S)

|  | Declaration |
| --- | --- |
| From | ``` init<S : SequenceType where T == T>(_ self_: S) ``` |
| To | ``` init<S : SequenceType where T == T>(_ base: S) ``` |

Modified SinkOf [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SinkOf<T> : SinkType {     init(_ put: (T) -> ())     init<S : SinkType where T == T>(_ base: S)     func put(_ x: T) } ``` |
| To | ``` struct SinkOf<T> : SinkType {     init(_ putElement: (T) -> ())     init<S : SinkType where T == T>(_ base: S)     func put(_ x: T) } ``` |

Modified SinkOf.init(_: (T) -> ())

|  | Declaration |
| --- | --- |
| From | ``` init(_ put: (T) -> ()) ``` |
| To | ``` init(_ putElement: (T) -> ()) ``` |

Modified Slice.extend(S)

|  | Declaration |
| --- | --- |
| From | ``` mutating func extend<S : SequenceType where T == T>(_ sequence: S) ``` |
| To | ``` mutating func extend<S : SequenceType where T == T>(_ newElements: S) ``` |

Modified Slice.replaceRange(Range<Int>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newValues: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C) ``` |

Modified Slice.splice(S, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` mutating func splice<S : CollectionType where T == T>(_ s: S, atIndex i: Int) ``` |
| To | ``` mutating func splice<S : CollectionType where T == T>(_ newElements: S, atIndex i: Int) ``` |

Modified StaticString [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct StaticString : StaticStringType {     var start: UnsafePointer<UInt8> { get }     var byteSize: UWord { get }     var isASCII: Bool { get }     var stringValue: String { get }     init()     init(start start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     static func convertFromExtendedGraphemeClusterLiteral(_ value: StaticString) -> StaticString     static func convertFromStringLiteral(_ value: StaticString) -> StaticString } ``` | StaticStringType |
| To | ``` struct StaticString : UnicodeScalarLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible, Printable, DebugPrintable {     var utf8Start: UnsafePointer<UInt8> { get }     var unicodeScalar: UnicodeScalar { get }     var byteSize: Word { get }     var hasPointerRepresentation: Bool { get }     var isASCII: Bool { get }     func withUTF8Buffer<R>(_ body: (UnsafeBufferPointer<UInt8>) -> R) -> R     var stringValue: String { get }     init()     init(start start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(unicodeScalar unicodeScalar: Builtin.Int32)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: StaticString)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: StaticString)     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(stringLiteral value: StaticString)     var description: String { get }     var debugDescription: String { get } } ``` | DebugPrintable, ExtendedGraphemeClusterLiteralConvertible, Printable, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

Modified StaticString.byteSize

|  | Declaration |
| --- | --- |
| From | ``` var byteSize: UWord { get } ``` |
| To | ``` var byteSize: Word { get } ``` |

Modified StrideThrough [struct]

|  | Protocols |
| --- | --- |
| From | SequenceType |
| To | Reflectable, SequenceType |

Modified StrideTo [struct]

|  | Protocols |
| --- | --- |
| From | SequenceType |
| To | Reflectable, SequenceType |

Modified String [struct]

|  | Protocols |
| --- | --- |
| From | CollectionType, Comparable, DebugPrintable, Equatable, ExtendedGraphemeClusterLiteralConvertible, ExtensibleCollectionType, Hashable, OutputStreamType, RangeReplaceableCollectionType, Reflectable, Sliceable, Streamable, StringInterpolationConvertible, StringLiteralConvertible |
| To | CollectionType, Comparable, DebugPrintable, Equatable, ExtendedGraphemeClusterLiteralConvertible, ExtensibleCollectionType, Hashable, OutputStreamType, RangeReplaceableCollectionType, Reflectable, Sliceable, Streamable, StringInterpolationConvertible, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

Modified String.extend(S)

|  | Declaration |
| --- | --- |
| From | ``` mutating func extend<S : SequenceType where Character == Character>(_ seq: S) ``` |
| To | ``` mutating func extend<S : SequenceType where Character == Character>(_ newElements: S) ``` |

Modified String.extend(String)

|  | Declaration |
| --- | --- |
| From | ``` mutating func extend(_ rhs: String) ``` |
| To | ``` mutating func extend(_ other: String) ``` |

Modified String.replaceRange(Range<String.Index>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` mutating func replaceRange<C : CollectionType where Character == Character>(_ subRange: Range<String.Index>, with newValues: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where Character == Character>(_ subRange: Range<String.Index>, with newElements: C) ``` |

Modified String.splice(S, atIndex: String.Index)

|  | Declaration |
| --- | --- |
| From | ``` mutating func splice<S : CollectionType where Character == Character>(_ newValues: S, atIndex i: String.Index) ``` |
| To | ``` mutating func splice<S : CollectionType where Character == Character>(_ newElements: S, atIndex i: String.Index) ``` |

Modified String.write(String)

|  | Declaration |
| --- | --- |
| From | ``` mutating func write(_ string: String) ``` |
| To | ``` mutating func write(_ other: String) ``` |

Modified String.UTF16View [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF16View : Sliceable, Reflectable {         var startIndex: Int { get }         var endIndex: Int { get }         typealias Generator         func generate() -> Generator         subscript (i: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         func getMirror() -> MirrorType     } ``` |
| To | ``` struct UTF16View : Sliceable, Reflectable {         var startIndex: Int { get }         var endIndex: Int { get }         typealias Generator         func generate() -> Generator         subscript (position: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         func getMirror() -> MirrorType     } ``` |

Modified String.UTF8View [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF8View : CollectionType, Reflectable {         struct Index : ForwardIndexType {             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (i: String.UTF8View.Index) -> CodeUnit { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> MirrorType     } ``` |
| To | ``` struct UTF8View : CollectionType, Reflectable {         struct Index : ForwardIndexType {             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (position: String.UTF8View.Index) -> CodeUnit { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> MirrorType     } ``` |

Modified String.UnicodeScalarView [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UnicodeScalarView : Sliceable, SequenceType, Reflectable {         struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (i: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.Generator         func compare(_ other: String.UnicodeScalarView) -> Int         func getMirror() -> MirrorType     } ``` |
| To | ``` struct UnicodeScalarView : Sliceable, SequenceType, Reflectable {         struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.Generator         func getMirror() -> MirrorType     } ``` |

Modified UInt [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UInt : UnsignedIntegerType {     var value: Builtin.Word     init()     init(_ v: Builtin.Word)     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     static func convertFromIntegerLiteral(_ value: UInt) -> UInt     typealias ArrayBound = UInt     var arrayBoundValue: UInt { get }     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } ``` |
| To | ``` struct UInt : UnsignedIntegerType {     var value: Builtin.Word     typealias Distance = Int     init()     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } ``` |

Modified UInt.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified UInt.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified UInt.advancedBy(Distance) -> UInt

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> UInt ``` | iOS 8.1 |

Modified UInt.distanceTo(UInt) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: UInt) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: UInt) -> Distance ``` | iOS 8.1 |

Modified UInt16 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UInt16 : UnsignedIntegerType {     var value: Builtin.Int16     init()     init(_ v: Builtin.Int16)     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     static func convertFromIntegerLiteral(_ value: UInt16) -> UInt16     typealias ArrayBound = UInt16     var arrayBoundValue: UInt16 { get }     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } ``` |
| To | ``` struct UInt16 : UnsignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt16)     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } ``` |

Modified UInt16.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified UInt16.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified UInt16.advancedBy(Distance) -> UInt16

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt16 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> UInt16 ``` | iOS 8.1 |

Modified UInt16.distanceTo(UInt16) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: UInt16) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: UInt16) -> Distance ``` | iOS 8.1 |

Modified UInt32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UInt32 : UnsignedIntegerType {     var value: Builtin.Int32     init()     init(_ v: Builtin.Int32)     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     static func convertFromIntegerLiteral(_ value: UInt32) -> UInt32     typealias ArrayBound = UInt32     var arrayBoundValue: UInt32 { get }     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } ``` |
| To | ``` struct UInt32 : UnsignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt32)     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } ``` |

Modified UInt32.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified UInt32.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified UInt32.advancedBy(Distance) -> UInt32

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt32 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> UInt32 ``` | iOS 8.1 |

Modified UInt32.distanceTo(UInt32) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: UInt32) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: UInt32) -> Distance ``` | iOS 8.1 |

Modified UInt64 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UInt64 : UnsignedIntegerType {     var value: Builtin.Int64     init()     init(_ v: Builtin.Int64)     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     static func convertFromIntegerLiteral(_ value: UInt64) -> UInt64     typealias ArrayBound = UInt64     var arrayBoundValue: UInt64 { get }     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } ``` |
| To | ``` struct UInt64 : UnsignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt64)     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } ``` |

Modified UInt64.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified UInt64.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified UInt64.advancedBy(Distance) -> UInt64

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt64 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> UInt64 ``` | iOS 8.1 |

Modified UInt64.distanceTo(UInt64) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: UInt64) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: UInt64) -> Distance ``` | iOS 8.1 |

Modified UInt8 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UInt8 : UnsignedIntegerType {     var value: Builtin.Int8     init()     init(_ v: Builtin.Int8)     init(_ value: UInt8)     static func convertFromIntegerLiteral(_ value: UInt8) -> UInt8     typealias ArrayBound = UInt8     var arrayBoundValue: UInt8 { get }     static var max: UInt8 { get }     static var min: UInt8 { get } } ``` |
| To | ``` struct UInt8 : UnsignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: UInt8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt8)     static var max: UInt8 { get }     static var min: UInt8 { get } } ``` |

Modified UInt8.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified UInt8.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified UInt8.advancedBy(Distance) -> UInt8

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt8 ``` | iOS 8.0 |
| To | ``` func advancedBy(_ amount: Distance) -> UInt8 ``` | iOS 8.1 |

Modified UInt8.distanceTo(UInt8) -> Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: UInt8) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ other: UInt8) -> Distance ``` | iOS 8.1 |

Modified UTF16.copy(UnsafeMutablePointer<T>, destination: UnsafeMutablePointer<U>, count: Int) [static]

|  | Declaration |
| --- | --- |
| From | ``` static func copy<T : StringElementType, U : StringElementType>(_ source: UnsafeMutablePointer<T>, destination destination: UnsafeMutablePointer<U>, count count: Int) ``` |
| To | ``` static func copy<T : _StringElementType, U : _StringElementType>(_ source: UnsafeMutablePointer<T>, destination destination: UnsafeMutablePointer<U>, count count: Int) ``` |

Modified UnicodeScalar [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnicodeScalar : ExtendedGraphemeClusterLiteralConvertible {     var value: UInt32 { get }     static func convertFromExtendedGraphemeClusterLiteral(_ value: String) -> UnicodeScalar     init()     init(_ value: Builtin.Int32)     init(_ v: UInt32)     init(_ v: UInt16)     init(_ v: UInt8)     init(_ v: UnicodeScalar)     func escape(asASCII asASCII: Bool) -> String     func isASCII() -> Bool } ``` | Comparable, DebugPrintable, ExtendedGraphemeClusterLiteralConvertible, Hashable, Printable, Reflectable, Streamable |
| To | ``` struct UnicodeScalar : UnicodeScalarLiteralConvertible {     var value: UInt32 { get }     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: UnicodeScalar)     init()     init(_ value: Builtin.Int32)     init(_ v: UInt32)     init(_ v: UInt16)     init(_ v: UInt8)     init(_ v: UnicodeScalar)     func escape(asASCII asASCII: Bool) -> String     func isASCII() -> Bool } ``` | Comparable, DebugPrintable, Hashable, Printable, Reflectable, Streamable, UnicodeScalarLiteralConvertible |

Modified UnsafeMutablePointer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UnsafeMutablePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     var value: Builtin.RawPointer     init()     init(_ value: Builtin.RawPointer)     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     static func convertFromNilLiteral() -> UnsafeMutablePointer<T>     static func null() -> UnsafeMutablePointer<T>     static func alloc(_ num: Int) -> UnsafeMutablePointer<T>     func dealloc(_ num: Int)     var memory: T { get nonmutating set }     func initialize(_ newvalue: T)     func move() -> T     func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveAssignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveInitializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom<C : CollectionType where T == T>(_ source: C)     func destroy()     func destroy(_ count: Int)     subscript (i: Int) -> T { get nonmutating set }     var hashValue: Int { get }     func successor() -> UnsafeMutablePointer<T>     func predecessor() -> UnsafeMutablePointer<T>     func distanceTo(_ x: UnsafeMutablePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafeMutablePointer<T> } ``` |
| To | ``` struct UnsafeMutablePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     var value: Builtin.RawPointer     init()     init(_ value: Builtin.RawPointer)     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafeMutablePointer<T>     static func alloc(_ num: Int) -> UnsafeMutablePointer<T>     func dealloc(_ num: Int)     var memory: T { get nonmutating set }     func initialize(_ newvalue: T)     func move() -> T     func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveAssignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveInitializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom<C : CollectionType where T == T>(_ source: C)     func destroy()     func destroy(_ count: Int)     subscript (i: Int) -> T { get nonmutating set }     var hashValue: Int { get }     func successor() -> UnsafeMutablePointer<T>     func predecessor() -> UnsafeMutablePointer<T>     func distanceTo(_ x: UnsafeMutablePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafeMutablePointer<T> } ``` |

Modified UnsafePointer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UnsafePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     var value: Builtin.RawPointer     init()     init(_ value: Builtin.RawPointer)     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     static func convertFromNilLiteral() -> UnsafePointer<T>     static func null() -> UnsafePointer<T>     var memory: T { get }     subscript (i: Int) -> T { get }     var hashValue: Int { get }     func successor() -> UnsafePointer<T>     func predecessor() -> UnsafePointer<T>     func distanceTo(_ x: UnsafePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafePointer<T> } ``` |
| To | ``` struct UnsafePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     var value: Builtin.RawPointer     init()     init(_ value: Builtin.RawPointer)     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafePointer<T>     var memory: T { get }     subscript (i: Int) -> T { get }     var hashValue: Int { get }     func successor() -> UnsafePointer<T>     func predecessor() -> UnsafePointer<T>     func distanceTo(_ x: UnsafePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafePointer<T> } ``` |

Modified Process

|  | Declaration |
| --- | --- |
| From | ``` var Process: _Process ``` |
| To | ``` let Process: _Process ``` |

Modified debugPrint(T)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrint<T>(_ object: T) ``` |
| To | ``` func debugPrint<T>(_ x: T) ``` |

Modified debugPrint(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrint<T, TargetStream : OutputStreamType>(_ object: T, inout _ target: TargetStream) ``` |
| To | ``` func debugPrint<T, TargetStream : OutputStreamType>(_ x: T, inout _ target: TargetStream) ``` |

Modified debugPrintln(T)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrintln<T>(_ object: T) ``` |
| To | ``` func debugPrintln<T>(_ x: T) ``` |

Modified debugPrintln(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrintln<T, TargetStream : OutputStreamType>(_ object: T, inout _ target: TargetStream) ``` |
| To | ``` func debugPrintln<T, TargetStream : OutputStreamType>(_ x: T, inout _ target: TargetStream) ``` |

Modified equal(S1, S2,(S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func equal<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element>(_ a1: S1, _ a2: S2, _ predicate: (S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool ``` |
| To | ``` func equal<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element>(_ a1: S1, _ a2: S2, _ isEquivalent: (S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool ``` |

Modified extend(C, S)

|  | Declaration |
| --- | --- |
| From | ``` func extend<C : RangeReplaceableCollectionType, S : CollectionType where S.Generator.Element == S.Generator.Element>(inout _ x: C, _ newValues: S) ``` |
| To | ``` func extend<C : RangeReplaceableCollectionType, S : CollectionType where S.Generator.Element == S.Generator.Element>(inout _ x: C, _ newElements: S) ``` |

Modified maxElement(R) -> R.Generator.Element

|  | Declaration |
| --- | --- |
| From | ``` func maxElement<R : SequenceType where R.Generator.Element : Comparable>(_ range: R) -> R.Generator.Element ``` |
| To | ``` func maxElement<R : SequenceType where R.Generator.Element : Comparable>(_ elements: R) -> R.Generator.Element ``` |

Modified minElement(R) -> R.Generator.Element

|  | Declaration |
| --- | --- |
| From | ``` func minElement<R : SequenceType where R.Generator.Element : Comparable>(_ range: R) -> R.Generator.Element ``` |
| To | ``` func minElement<R : SequenceType where R.Generator.Element : Comparable>(_ elements: R) -> R.Generator.Element ``` |

Modified numericCast(T) -> U

|  | Declaration |
| --- | --- |
| From | ``` func numericCast<T : _UnsignedIntegerType, U : _UnsignedIntegerType>(_ x: T) -> U ``` |
| To | ``` func numericCast<T : _UnsignedIntegerType, U : _SignedIntegerType>(_ x: T) -> U ``` |

Modified splice(C, S, C.Index)

|  | Declaration |
| --- | --- |
| From | ``` func splice<C : RangeReplaceableCollectionType, S : CollectionType where S.Generator.Element == S.Generator.Element>(inout _ x: C, _ newValues: S, atIndex i: C.Index) ``` |
| To | ``` func splice<C : RangeReplaceableCollectionType, S : CollectionType where S.Generator.Element == S.Generator.Element>(inout _ x: C, _ newElements: S, atIndex i: C.Index) ``` |

Modified startsWith(S0, S1,(S0.Generator.Element, S0.Generator.Element) -> Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func startsWith<S0 : SequenceType, S1 : SequenceType where S0.Generator.Element == S0.Generator.Element>(_ s: S0, _ prefix: S1, _ predicate: (S0.Generator.Element, S0.Generator.Element) -> Bool) -> Bool ``` |
| To | ``` func startsWith<S0 : SequenceType, S1 : SequenceType where S0.Generator.Element == S0.Generator.Element>(_ s: S0, _ prefix: S1, _ isEquivalent: (S0.Generator.Element, S0.Generator.Element) -> Bool) -> Bool ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
