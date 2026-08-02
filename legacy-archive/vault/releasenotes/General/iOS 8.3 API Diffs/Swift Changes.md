---
title: iOS 8.3 API Diffs
apple_id: TP40015150
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-04-08'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS83APIDiffs/modules/Swift.html
archived_at: '2026-07-18T02:56:28.000405Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 8.3 API Diffs](iOS%208.2%20to%20iOS%208.3%20API%20Differences.md)


# Swift Changes

## Swift

Removed Array.init(_fromCocoaArray: _SwiftNSArrayRequiredOverridesType, noCopy: Bool)Removed Array.convertFromHeapArray(Builtin.RawPointer, owner: Builtin.NativeObject, count: Builtin.Word) -> [T] [static]Removed ArrayTypeRemoved ArrayType.init()Removed ArrayType.+=(Self, _: S) [class]Removed ArrayType.init(_: _Buffer)Removed ArrayType.append(Self.Generator.Element)Removed ArrayType.capacityRemoved ArrayType.countRemoved ArrayType.init(count: Int, repeatedValue: Self.Generator.Element)Removed ArrayType.extend(S)Removed ArrayType.insert(Self.Generator.Element, atIndex: Int)Removed ArrayType.isEmptyRemoved ArrayType.join(S) -> SelfRemoved ArrayType.reduce(U, combine:(U, Self.Generator.Element) -> U) -> URemoved ArrayType.removeAll(Bool)Removed ArrayType.removeAtIndex(Int) -> Self.Generator.ElementRemoved ArrayType.removeLast() -> Self.Generator.ElementRemoved ArrayType.reserveCapacity(Int)Removed ArrayType.sort((Self.Generator.Element, Self.Generator.Element) -> Bool)Removed AutoreleasingUnsafeMutablePointer.init(_: Builtin.RawPointer)Removed AutoreleasingUnsafeMutablePointer.null() -> AutoreleasingUnsafeMutablePointer<T> [static]Removed AutoreleasingUnsafeMutablePointer.valueRemoved CFunctionPointer.null() -> CFunctionPointer<T> [static]Removed COpaquePointer.null() -> COpaquePointer [static]Removed COpaquePointer.valueRemoved CVaListPointer.init(fromUnsafeMutablePointer: UnsafeMutablePointer<Void>)Removed Character [enum]Removed Character.LargeRepresentationRemoved Character.SmallRepresentationRemoved Character.init(_: String)Removed Character.init(_: UnicodeScalar)Removed Character.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Removed Character.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Removed Character.init(extendedGraphemeClusterLiteral: Character)Removed Character.getMirror() -> MirrorTypeRemoved Character.hashValueRemoved Character.init(unicodeScalarLiteral: Character)Removed Character.utf16Removed Character.writeTo(Target)Removed DictionaryIndex.predecessor() -> DictionaryIndex<Key, Value>Removed Double.init(_: Builtin.FPIEEE64)Removed Float.init(_: Builtin.FPIEEE32)Removed HeapBuffer [struct]Removed HeapBuffer.init()Removed HeapBuffer.init(_: AnyClass, _: Value, _: Int)Removed HeapBuffer.init(_: HeapBufferStorage<Value, Element>)Removed HeapBuffer.baseAddressRemoved HeapBuffer.fromNativeObject(Builtin.NativeObject) -> HeapBuffer<Value, Element> [static]Removed HeapBuffer.hasStorageRemoved HeapBuffer.isUniquelyReferenced() -> BoolRemoved HeapBuffer.storageRemoved HeapBuffer.valueRemoved HeapBufferStorageRemoved HeapBufferStorage.deinitRemoved IntEncoder [struct]Removed IntEncoder.asIntRemoved IntEncoder.put(CodeUnit)Removed IntEncoder.shiftRemoved ObjectIdentifier.uintValue() -> UIntRemoved OnHeap [struct]Removed OnHeap.init(_: T)Removed Slice [struct]Removed Slice.init()Removed Slice.init(_: S)Removed Slice.init(_: _SliceBuffer<T>)Removed Slice.init(_uninitializedCount: Int)Removed Slice.append(T)Removed Slice.init(arrayLiteral: T)Removed Slice.capacityRemoved Slice.countRemoved Slice.init(count: Int, repeatedValue: T)Removed Slice.debugDescriptionRemoved Slice.descriptionRemoved Slice.endIndexRemoved Slice.extend(S)Removed Slice.filter((T) -> Bool) -> Slice<T>Removed Slice.firstRemoved Slice.generate() -> IndexingGenerator<Slice<T>>Removed Slice.getMirror() -> MirrorTypeRemoved Slice.insert(T, atIndex: Int)Removed Slice.isEmptyRemoved Slice.join(S) -> Slice<T>Removed Slice.lastRemoved Slice.map((T) -> U) -> Slice<U>Removed Slice.reduce(U, combine:(U, T) -> U) -> URemoved Slice.removeAll(Bool)Removed Slice.removeAtIndex(Int) -> TRemoved Slice.removeLast() -> TRemoved Slice.removeRange(Range<Int>)Removed Slice.replaceRange(Range<Int>, with: C)Removed Slice.reserveCapacity(Int)Removed Slice.reverse() -> Slice<T>Removed Slice.sort((T, T) -> Bool)Removed Slice.sorted((T, T) -> Bool) -> Slice<T>Removed Slice.splice(S, atIndex: Int)Removed Slice.startIndexRemoved Slice.withUnsafeBufferPointer((UnsafeBufferPointer<T>) -> R) -> RRemoved Slice.withUnsafeMutableBufferPointer((inoutUnsafeMutableBufferPointer<T>) -> R) -> RRemoved String.convertFromStringInterpolation(String) -> String [static]Removed String.convertFromStringInterpolationSegment(Bool) -> String [static]Removed String.convertFromStringInterpolationSegment(Character) -> String [static]Removed String.convertFromStringInterpolationSegment(Float32) -> String [static]Removed String.convertFromStringInterpolationSegment(Float64) -> String [static]Removed String.convertFromStringInterpolationSegment(Int) -> String [static]Removed String.convertFromStringInterpolationSegment(Int16) -> String [static]Removed String.convertFromStringInterpolationSegment(Int32) -> String [static]Removed String.convertFromStringInterpolationSegment(Int64) -> String [static]Removed String.convertFromStringInterpolationSegment(Int8) -> String [static]Removed String.convertFromStringInterpolationSegment(String) -> String [static]Removed String.convertFromStringInterpolationSegment(T) -> String [static]Removed String.convertFromStringInterpolationSegment(UInt) -> String [static]Removed String.convertFromStringInterpolationSegment(UInt16) -> String [static]Removed String.convertFromStringInterpolationSegment(UInt32) -> String [static]Removed String.convertFromStringInterpolationSegment(UInt64) -> String [static]Removed String.convertFromStringInterpolationSegment(UInt8) -> String [static]Removed String.convertFromStringInterpolationSegment(UnicodeScalar) -> String [static]Removed StringInterpolationConvertible.convertFromStringInterpolation(Self) -> Self [class]Removed StringInterpolationConvertible.convertFromStringInterpolationSegment(T) -> Self [class]Removed UInt8.init(_: UnicodeScalar)Removed UTF16.copy(UnsafeMutablePointer<T>, destination: UnsafeMutablePointer<U>, count: Int) [static]Removed UnsafeMutablePointer.init(_: Builtin.RawPointer)Removed UnsafeMutablePointer.null() -> UnsafeMutablePointer<T> [static]Removed UnsafeMutablePointer.valueRemoved UnsafePointer.init(_: Builtin.RawPointer)Removed UnsafePointer.null() -> UnsafePointer<T> [static]Removed UnsafePointer.valueRemoved C_ARGCRemoved C_ARGVRemoved HeapBuffer.StorageRemoved HeapBufferStorage.BufferRemoved OnHeap.BufferRemoved ProcessRemoved Range.SliceRemoved Slice.ElementRemoved Slice.SubSliceRemoved count(Range<I>) -> I.DistanceRemoved countElements(T) -> T.Index.DistanceRemoved split(S,(S.Generator.Element) -> R, Int, Bool) -> [S.SubSlice]Removed transcode(InputEncoding.Type, OutputEncoding.Type, Input, Output, Bool) -> (Bool)Added Array.init(_fromCocoaArray: _NSArrayCoreType, noCopy: Bool)Added Array.flatMap((T) -> [U]) -> [U]Added ArraySlice [struct]Added ArraySlice.init()Added ArraySlice.init(_: S)Added ArraySlice.init(_: _SliceBuffer<T>)Added ArraySlice.init(_uninitializedCount: Int)Added ArraySlice.append(T)Added ArraySlice.init(arrayLiteral: T)Added ArraySlice.capacityAdded ArraySlice.countAdded ArraySlice.init(count: Int, repeatedValue: T)Added ArraySlice.debugDescriptionAdded ArraySlice.descriptionAdded ArraySlice.endIndexAdded ArraySlice.extend(S)Added ArraySlice.filter((T) -> Bool) -> ArraySlice<T>Added ArraySlice.firstAdded ArraySlice.flatMap((T) -> ArraySlice<U>) -> ArraySlice<U>Added ArraySlice.generate() -> IndexingGenerator<ArraySlice<T>>Added ArraySlice.getMirror() -> MirrorTypeAdded ArraySlice.insert(T, atIndex: Int)Added ArraySlice.isEmptyAdded ArraySlice.join(S) -> ArraySlice<T>Added ArraySlice.lastAdded ArraySlice.map((T) -> U) -> ArraySlice<U>Added ArraySlice.reduce(U, combine:(U, T) -> U) -> UAdded ArraySlice.removeAll(Bool)Added ArraySlice.removeAtIndex(Int) -> TAdded ArraySlice.removeLast() -> TAdded ArraySlice.removeRange(Range<Int>)Added ArraySlice.replaceRange(Range<Int>, with: C)Added ArraySlice.reserveCapacity(Int)Added ArraySlice.reverse() -> ArraySlice<T>Added ArraySlice.sort((T, T) -> Bool)Added ArraySlice.sorted((T, T) -> Bool) -> ArraySlice<T>Added ArraySlice.splice(S, atIndex: Int)Added ArraySlice.startIndexAdded ArraySlice.withUnsafeBufferPointer((UnsafeBufferPointer<T>) -> R) -> RAdded ArraySlice.withUnsafeMutableBufferPointer((inoutUnsafeMutableBufferPointer<T>) -> R) -> RAdded AutoreleasingUnsafeMutablePointer.encode() -> [Word]Added CFunctionPointer.encode() -> [Word]Added CVaListPointer.init(_fromUnsafeMutablePointer: UnsafeMutablePointer<Void>)Added Character [struct]Added Character.init(_: String)Added Character.init(_: UnicodeScalar)Added Character.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added Character.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added Character.debugDescriptionAdded Character.init(extendedGraphemeClusterLiteral: Character)Added Character.getMirror() -> MirrorTypeAdded Character.hashValueAdded Character.init(unicodeScalarLiteral: Character)Added Character.utf16Added Character.writeTo(Target)Added Character.Representation [enum]Added Character.Representation.LargeAdded Character.Representation.SmallAdded ContiguousArray.flatMap((T) -> ContiguousArray<U>) -> ContiguousArray<U>Added DictionaryGeneratorRepresentation [enum]Added DictionaryIndexRepresentation [enum]Added DictionaryMirrorAdded DictionaryMirror.init(_: [Key: Value])Added DictionaryMirror.countAdded DictionaryMirror.dispositionAdded DictionaryMirror.objectIdentifierAdded DictionaryMirror.quickLookObjectAdded DictionaryMirror.summaryAdded DictionaryMirror.valueAdded DictionaryMirror.valueTypeAdded DictionaryMirrorPosition [struct]Added DictionaryMirrorPosition.DictionaryPosAdded DictionaryMirrorPosition.init(_: [Key: Value])Added DictionaryMirrorPosition.successor()Added Double.init(_bits: Builtin.FPIEEE64)Added EmptyGenerator.init()Added Float.init(_bits: Builtin.FPIEEE32)Added ImplicitlyUnwrappedOptional.flatMap((T) -> U!) -> U!Added Index.init(_: String.Index, within: String.UTF16View)Added Index.init(_: String.Index, within: String.UTF8View)Added Index.init(_: UTF16Index, within: String)Added Index.init(_: UTF16Index, within: String.UTF8View)Added Index.init(_: UTF8Index, within: String)Added Index.init(_: UTF8Index, within: String.UTF16View)Added Index.init(_: UnicodeScalarIndex, within: String)Added Index.init(_: UnicodeScalarIndex, within: String.UTF16View)Added Index.init(_: UnicodeScalarIndex, within: String.UTF8View)Added Index.predecessor() -> String.UTF16View.IndexAdded Index.samePositionIn(String) -> String.Index?Added Index.samePositionIn(String.UTF16View) -> String.UTF16View.IndexAdded Index.samePositionIn(String.UTF16View) -> String.UTF16View.Index?Added Index.samePositionIn(String.UTF8View) -> String.UTF8View.IndexAdded Index.samePositionIn(String.UTF8View) -> String.UTF8View.Index?Added Index.samePositionIn(String.UnicodeScalarView) -> String.UnicodeScalarView.IndexAdded Index.samePositionIn(String.UnicodeScalarView) -> UnicodeScalarIndex?Added Index.successor() -> String.UTF16View.IndexAdded Int.init(_: Builtin.Word)Added ManagedBufferAdded ManagedBuffer.deinitAdded ManagedBuffer.create(Int, initialValue:(ManagedProtoBuffer<Value, Element>) -> Value) -> ManagedBuffer<Value, Element> [class]Added ManagedBuffer.valueAdded ManagedBufferPointer [struct]Added ManagedBufferPointer.init(_: ManagedProtoBuffer<Value, Element>)Added ManagedBufferPointer.init(_uncheckedUnsafeBufferObject: AnyObject)Added ManagedBufferPointer.allocatedElementCountAdded ManagedBufferPointer.bufferAdded ManagedBufferPointer.init(bufferClass: AnyClass, minimumCapacity: Int)Added ManagedBufferPointer.init(bufferClass: AnyClass, minimumCapacity: Int, initialValue:(buffer: AnyObject, allocatedCount:(AnyObject) -> Int) -> Value)Added ManagedBufferPointer.holdsUniqueOrPinnedReference() -> BoolAdded ManagedBufferPointer.holdsUniqueReference() -> BoolAdded ManagedBufferPointer.init(unsafeBufferObject: AnyObject)Added ManagedBufferPointer.valueAdded ManagedBufferPointer.withUnsafeMutablePointerToElements((UnsafeMutablePointer<Element>) -> R) -> RAdded ManagedBufferPointer.withUnsafeMutablePointerToValue((UnsafeMutablePointer<Value>) -> R) -> RAdded ManagedBufferPointer.withUnsafeMutablePointers((UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> RAdded ManagedProtoBufferAdded ManagedProtoBuffer.allocatedElementCountAdded ManagedProtoBuffer.withUnsafeMutablePointerToElements((UnsafeMutablePointer<Element>) -> R) -> RAdded ManagedProtoBuffer.withUnsafeMutablePointerToValue((UnsafeMutablePointer<Value>) -> R) -> RAdded ManagedProtoBuffer.withUnsafeMutablePointers((UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> RAdded NonObjectiveCBaseAdded ObjectIdentifier.init(_: Any.Type)Added ObjectIdentifier.uintValueAdded Optional.flatMap((T) -> U?) -> U?Added Process [enum]Added Process.argcAdded Process.argumentsAdded Process.unsafeArgvAdded QuickLookObject.DoubleAdded Set [struct]Added Set.init()Added Set.init(_: S)Added Set.init(arrayLiteral: T)Added Set.contains(T) -> BoolAdded Set.countAdded Set.debugDescriptionAdded Set.descriptionAdded Set.endIndexAdded Set.exclusiveOr(S) -> Set<T>Added Set.exclusiveOrInPlace(S)Added Set.firstAdded Set.generate() -> SetGenerator<T>Added Set.getMirror() -> MirrorTypeAdded Set.hashValueAdded Set.indexOf(T) -> SetIndex<T>?Added Set.insert(T)Added Set.intersect(S) -> Set<T>Added Set.intersectInPlace(S)Added Set.isDisjointWith(S) -> BoolAdded Set.isEmptyAdded Set.isStrictSubsetOf(S) -> BoolAdded Set.isStrictSupersetOf(S) -> BoolAdded Set.isSubsetOf(S) -> BoolAdded Set.isSupersetOf(S) -> BoolAdded Set.makeDescription(Bool) -> StringAdded Set.init(minimumCapacity: Int)Added Set.remove(T) -> T?Added Set.removeAll(Bool)Added Set.removeAtIndex(SetIndex<T>)Added Set.removeFirst() -> TAdded Set.startIndexAdded Set.subtract(S) -> Set<T>Added Set.subtractInPlace(S)Added Set.union(S) -> Set<T>Added Set.unionInPlace(S)Added SetGenerator [struct]Added SetGenerator.next() -> T?Added SetGeneratorRepresentation [enum]Added SetIndex [struct]Added SetIndex.successor() -> SetIndex<T>Added SetIndexRepresentation [enum]Added SetMirrorAdded SetMirror.init(_: Set<T>)Added SetMirror.countAdded SetMirror.dispositionAdded SetMirror.objectIdentifierAdded SetMirror.quickLookObjectAdded SetMirror.summaryAdded SetMirror.valueAdded SetMirror.valueTypeAdded SetMirrorPosition [struct]Added SetMirrorPosition.SetPosAdded SetMirrorPosition.init(_: Set<T>)Added SetMirrorPosition.successor()Added String.init(_: String.UTF16View)Added String.init(_: String.UTF8View)Added String.init(stringInterpolation: String)Added String.init(stringInterpolationSegment: Bool)Added String.init(stringInterpolationSegment: Character)Added String.init(stringInterpolationSegment: Float32)Added String.init(stringInterpolationSegment: Float64)Added String.init(stringInterpolationSegment: Int)Added String.init(stringInterpolationSegment: Int16)Added String.init(stringInterpolationSegment: Int32)Added String.init(stringInterpolationSegment: Int64)Added String.init(stringInterpolationSegment: Int8)Added String.init(stringInterpolationSegment: String)Added String.init(stringInterpolationSegment: T)Added String.init(stringInterpolationSegment: UInt)Added String.init(stringInterpolationSegment: UInt16)Added String.init(stringInterpolationSegment: UInt32)Added String.init(stringInterpolationSegment: UInt64)Added String.init(stringInterpolationSegment: UInt8)Added String.init(stringInterpolationSegment: UnicodeScalar)Added String.UTF16View.debugDescriptionAdded String.UTF16View.descriptionAdded String.UTF16View.Index [struct]Added String.UTF8View.debugDescriptionAdded String.UTF8View.descriptionAdded String.UnicodeScalarView.debugDescriptionAdded String.UnicodeScalarView.descriptionAdded StringInterpolationConvertible.init(stringInterpolation: Self)Added StringInterpolationConvertible.init(stringInterpolationSegment: T)Added UInt.init(_: Builtin.Word)Added UInt8.init(ascii: UnicodeScalar)Added UTF16.isLeadSurrogate(CodeUnit) -> Bool [static]Added UTF16.isTrailSurrogate(CodeUnit) -> Bool [static]Added UTF16View.endIndexAdded UTF16View.generate() -> IndexingGenerator<UnicodeScalar.UTF16View>Added UTF16View.startIndexAdded UTF8.isContinuation(CodeUnit) -> Bool [static]Added UnicodeScalarIndex.init(_: String.Index, within: String.UnicodeScalarView)Added UnicodeScalarIndex.init(_: UTF16Index, within: String.UnicodeScalarView)Added UnicodeScalarIndex.init(_: UTF8Index, within: String.UnicodeScalarView)Added UnicodeScalarIndex.samePositionIn(String) -> String.Index?Added UnicodeScalarIndex.samePositionIn(String.UTF16View) -> String.UTF16View.IndexAdded UnicodeScalarIndex.samePositionIn(String.UTF8View) -> String.UTF8View.IndexAdded UnicodeScalarView.init()Added UnicodeScalarView.append(UnicodeScalar)Added UnicodeScalarView.extend(S)Added UnicodeScalarView.insert(UnicodeScalar, atIndex: String.UnicodeScalarView.Index)Added UnicodeScalarView.removeAll(Bool)Added UnicodeScalarView.removeAtIndex(String.UnicodeScalarView.Index) -> UnicodeScalarAdded UnicodeScalarView.removeRange(Range<String.UnicodeScalarView.Index>)Added UnicodeScalarView.replaceRange(Range<String.UnicodeScalarView.Index>, with: C)Added UnicodeScalarView.reserveCapacity(Int)Added UnicodeScalarView.splice(S, atIndex: String.UnicodeScalarView.Index)Added UnsafeMutablePointer.encode() -> [Word]Added UnsafePointer.encode() -> [Word]Added ArraySlice.ElementAdded ArraySlice.SubSliceAdded DictionaryMirror.MirroredTypeAdded DictionaryMirrorPosition.MirroredTypeAdded Index.DistanceAdded Range.ArraySliceAdded Set.ElementAdded Set.GeneratorTypeAdded Set.IndexAdded SetIndex.IndexAdded SetIndex.KeyAdded SetIndex.ValueAdded SetMirror.MirroredTypeAdded SetMirrorPosition.MirroredTypeAdded String.UTF16IndexAdded String.UTF8IndexAdded String.UTF8View.Index.BufferAdded String.UnicodeScalarIndexAdded count(T) -> T.Index.DistanceAdded flatMap(C,(C.Generator.Element) -> [T]) -> [T]Added flatMap(S,(S.Generator.Element) -> [T]) -> [T]Added flatMap(T?,(T) -> U?) -> U?Added isUniquelyReferenced(T) -> BoolAdded isUniquelyReferencedNonObjC(T) -> BoolAdded isUniquelyReferencedNonObjC(T?) -> BoolAdded isUniquelyReferencedOrPinnedNonObjC(T) -> BoolAdded kCFStringEncodingASCIIAdded split(S, Int, Bool,(S.Generator.Element) -> R) -> [S.SubSlice]Added transcode(InputEncoding.Type, OutputEncoding.Type, Input, Output, Bool) -> BoolAdded unsafeUnwrap(T?) -> TAdded zip(S0, S1) -> Zip2<S0, S1>Modified AbsoluteValuable.abs(Self) -> Self [class]

|  | Declaration |
| --- | --- |
| From | ``` class func abs(_ x: Self) -> Self ``` |
| To | ``` static func abs(_ x: Self) -> Self ``` |

Modified Array [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Array<T> : MutableCollectionType, Sliceable {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<[T]>     typealias SubSlice = Slice<T>     subscript (subRange: Range<Int>) -> Slice<T>     init(_ buffer: _ArrayBuffer<T>) } ``` | ArrayLiteralConvertible, ArrayType, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable |
| To | ``` struct Array<T> : MutableCollectionType, Sliceable, _DestructorSafeContainer {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<[T]>     typealias SubSlice = ArraySlice<T>     subscript (subRange: Range<Int>) -> ArraySlice<T>     init(_ buffer: _ArrayBuffer<T>) } ``` | ArrayLiteralConvertible, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable |

Modified Array.reduce(U, combine:(U, T) -> U) -> U

|  | Declaration |
| --- | --- |
| From | ``` func reduce<U>(_ initial: U, combine combine: (U, T) -> U) -> U ``` |
| To | ``` func reduce<U>(_ initial: U, combine combine: @noescape (U, T) -> U) -> U ``` |

Modified Array.withUnsafeBufferPointer((UnsafeBufferPointer<T>) -> R) -> R

|  | Declaration |
| --- | --- |
| From | ``` func withUnsafeBufferPointer<R>(_ body: (UnsafeBufferPointer<T>) -> R) -> R ``` |
| To | ``` func withUnsafeBufferPointer<R>(_ body: @noescape (UnsafeBufferPointer<T>) -> R) -> R ``` |

Modified Array.withUnsafeMutableBufferPointer((inoutUnsafeMutableBufferPointer<T>) -> R) -> R

|  | Declaration |
| --- | --- |
| From | ``` mutating func withUnsafeMutableBufferPointer<R>(_ body: (inout UnsafeMutableBufferPointer<T>) -> R) -> R ``` |
| To | ``` mutating func withUnsafeMutableBufferPointer<R>(_ body: @noescape (inout UnsafeMutableBufferPointer<T>) -> R) -> R ``` |

Modified AutoreleasingUnsafeMutablePointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct AutoreleasingUnsafeMutablePointer<T> : Equatable, NilLiteralConvertible, _PointerType {     let value: Builtin.RawPointer     init(_ value: Builtin.RawPointer)     var memory: T { get nonmutating set }     subscript (i: Int) -> T { get }     init(nilLiteral nilLiteral: ())     static func null() -> AutoreleasingUnsafeMutablePointer<T>     init()     init<U>(_ ptr: UnsafeMutablePointer<U>)     init<U>(_ ptr: UnsafePointer<U>) } ``` | DebugPrintable, Equatable, NilLiteralConvertible |
| To | ``` struct AutoreleasingUnsafeMutablePointer<T> : Equatable, NilLiteralConvertible, _PointerType {     var memory: T { get nonmutating set }     subscript (i: Int) -> T { get }     init(nilLiteral nilLiteral: ())     static func null() -> AutoreleasingUnsafeMutablePointer<T>     init()     init<U>(_ ptr: UnsafeMutablePointer<U>)     init<U>(_ ptr: UnsafePointer<U>) } ``` | CVarArgType, DebugPrintable, Equatable, NilLiteralConvertible |

Modified BitwiseOperationsType.allZeros

|  | Declaration |
| --- | --- |
| From | ``` class var allZeros: Self { get } ``` |
| To | ``` static var allZeros: Self { get } ``` |

Modified CFunctionPointer [struct]

|  | Protocols |
| --- | --- |
| From | DebugPrintable, Equatable, Hashable, NilLiteralConvertible |
| To | CVarArgType, DebugPrintable, Equatable, Hashable, NilLiteralConvertible |

Modified COpaquePointer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct COpaquePointer : Equatable, Hashable, NilLiteralConvertible {     var value: Builtin.RawPointer     init()     init(_ v: Builtin.RawPointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<T>(_ value: UnsafePointer<T>)     init<T>(_ value: UnsafeMutablePointer<T>)     static func null() -> COpaquePointer     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } ``` |
| To | ``` struct COpaquePointer : Equatable, Hashable, NilLiteralConvertible {     init()     init(_ v: Builtin.RawPointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<T>(_ source: UnsafePointer<T>)     init<T>(_ source: UnsafeMutablePointer<T>)     static func null() -> COpaquePointer     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } ``` |

Modified COpaquePointer.init(_: UnsafeMutablePointer<T>)

|  | Declaration |
| --- | --- |
| From | ``` init<T>(_ value: UnsafeMutablePointer<T>) ``` |
| To | ``` init<T>(_ source: UnsafeMutablePointer<T>) ``` |

Modified COpaquePointer.init(_: UnsafePointer<T>)

|  | Declaration |
| --- | --- |
| From | ``` init<T>(_ value: UnsafePointer<T>) ``` |
| To | ``` init<T>(_ source: UnsafePointer<T>) ``` |

Modified CVaListPointer [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct CVaListPointer {     var value: UnsafeMutablePointer<Void>     init(fromUnsafeMutablePointer from: UnsafeMutablePointer<Void>) } ``` |
| To | ``` struct CVaListPointer {     var value: UnsafeMutablePointer<Void>     init(_fromUnsafeMutablePointer from: UnsafeMutablePointer<Void>) } ``` |

Modified ContiguousArray [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ContiguousArray<T> : MutableCollectionType, Sliceable {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<ContiguousArray<T>>     typealias SubSlice = Slice<T>     subscript (subRange: Range<Int>) -> Slice<T>     init(_ buffer: _ContiguousArrayBuffer<T>) } ``` | ArrayLiteralConvertible, ArrayType, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable |
| To | ``` struct ContiguousArray<T> : MutableCollectionType, Sliceable, _DestructorSafeContainer {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<ContiguousArray<T>>     typealias SubSlice = ArraySlice<T>     subscript (subRange: Range<Int>) -> ArraySlice<T>     init(_ buffer: _ContiguousArrayBuffer<T>) } ``` | ArrayLiteralConvertible, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable |

Modified ContiguousArray.reduce(U, combine:(U, T) -> U) -> U

|  | Declaration |
| --- | --- |
| From | ``` func reduce<U>(_ initial: U, combine combine: (U, T) -> U) -> U ``` |
| To | ``` func reduce<U>(_ initial: U, combine combine: @noescape (U, T) -> U) -> U ``` |

Modified ContiguousArray.withUnsafeBufferPointer((UnsafeBufferPointer<T>) -> R) -> R

|  | Declaration |
| --- | --- |
| From | ``` func withUnsafeBufferPointer<R>(_ body: (UnsafeBufferPointer<T>) -> R) -> R ``` |
| To | ``` func withUnsafeBufferPointer<R>(_ body: @noescape (UnsafeBufferPointer<T>) -> R) -> R ``` |

Modified ContiguousArray.withUnsafeMutableBufferPointer((inoutUnsafeMutableBufferPointer<T>) -> R) -> R

|  | Declaration |
| --- | --- |
| From | ``` mutating func withUnsafeMutableBufferPointer<R>(_ body: (inout UnsafeMutableBufferPointer<T>) -> R) -> R ``` |
| To | ``` mutating func withUnsafeMutableBufferPointer<R>(_ body: @noescape (inout UnsafeMutableBufferPointer<T>) -> R) -> R ``` |

Modified Dictionary [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Dictionary<Key : Hashable, Value> : CollectionType, DictionaryLiteralConvertible {     typealias Element = (Key, Value)     typealias Index = DictionaryIndex<Key, Value>     init()     init(minimumCapacity minimumCapacity: Int)     var startIndex: DictionaryIndex<Key, Value> { get }     var endIndex: DictionaryIndex<Key, Value> { get }     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>?     subscript (position: DictionaryIndex<Key, Value>) -> (Key, Value) { get }     subscript (key: Key) -> Value?     mutating func updateValue(_ value: Value, forKey key: Key) -> Value?     mutating func removeAtIndex(_ index: DictionaryIndex<Key, Value>)     mutating func removeValueForKey(_ key: Key) -> Value?     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<Key, Value>     init(dictionaryLiteral elements: (Key, Value)...)     var isEmpty: Bool { get }     var keys: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Key>> { get }     var values: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Value>> { get } } ``` |
| To | ``` struct Dictionary<Key : Hashable, Value> : CollectionType, DictionaryLiteralConvertible {     typealias Element = (Key, Value)     typealias Index = DictionaryIndex<Key, Value>     init()     init(minimumCapacity minimumCapacity: Int)     var startIndex: DictionaryIndex<Key, Value> { get }     var endIndex: DictionaryIndex<Key, Value> { get }     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>?     subscript (position: DictionaryIndex<Key, Value>) -> (Key, Value) { get }     subscript (key: Key) -> Value?     mutating func updateValue(_ value: Value, forKey key: Key) -> Value?     mutating func removeAtIndex(_ index: DictionaryIndex<Key, Value>)     mutating func removeValueForKey(_ key: Key) -> Value?     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<Key, Value>     init(dictionaryLiteral elements: (Key, Value)...)     var isEmpty: Bool { get }     var keys: LazyForwardCollection<MapCollectionView<[Key : Value], Key>> { get }     var values: LazyForwardCollection<MapCollectionView<[Key : Value], Value>> { get } } ``` |

Modified Dictionary.keys

|  | Declaration |
| --- | --- |
| From | ``` var keys: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Key>> { get } ``` |
| To | ``` var keys: LazyForwardCollection<MapCollectionView<[Key : Value], Key>> { get } ``` |

Modified Dictionary.values

|  | Declaration |
| --- | --- |
| From | ``` var values: LazyBidirectionalCollection<MapCollectionView<[Key : Value], Value>> { get } ``` |
| To | ``` var values: LazyForwardCollection<MapCollectionView<[Key : Value], Value>> { get } ``` |

Modified DictionaryIndex [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct DictionaryIndex<Key : Hashable, Value> : BidirectionalIndexType, Comparable {     typealias Index = DictionaryIndex<Key, Value>     func predecessor() -> DictionaryIndex<Key, Value>     func successor() -> DictionaryIndex<Key, Value> } ``` | BidirectionalIndexType, Comparable |
| To | ``` struct DictionaryIndex<Key : Hashable, Value> : ForwardIndexType, Comparable {     typealias Index = DictionaryIndex<Key, Value>     func successor() -> DictionaryIndex<Key, Value> } ``` | Comparable, ForwardIndexType |

Modified Double [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Double {     var value: Builtin.FPIEEE64     init()     init(_ v: Builtin.FPIEEE64)     init(_ value: Double) } ``` | AbsoluteValuable, CVarArgType, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Strideable |
| To | ``` struct Double {     var value: Builtin.FPIEEE64     init()     init(_bits v: Builtin.FPIEEE64)     init(_ value: Double) } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |

Modified Double.getMirror() -> MirrorType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified EmptyGenerator [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct EmptyGenerator<T> : GeneratorType, SequenceType {     func generate() -> EmptyGenerator<T>     mutating func next() -> T? } ``` |
| To | ``` struct EmptyGenerator<T> : GeneratorType, SequenceType {     init()     func generate() -> EmptyGenerator<T>     mutating func next() -> T? } ``` |

Modified Float [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Float {     var value: Builtin.FPIEEE32     init()     init(_ v: Builtin.FPIEEE32)     init(_ value: Float) } ``` | AbsoluteValuable, CVarArgType, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Strideable |
| To | ``` struct Float {     var value: Builtin.FPIEEE32     init()     init(_bits v: Builtin.FPIEEE32)     init(_ value: Float) } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |

Modified Float.getMirror() -> MirrorType

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 8.3 |

Modified FloatingPointType.NaN

|  | Declaration |
| --- | --- |
| From | ``` class var NaN: Self { get } ``` |
| To | ``` static var NaN: Self { get } ``` |

Modified FloatingPointType.infinity

|  | Declaration |
| --- | --- |
| From | ``` class var infinity: Self { get } ``` |
| To | ``` static var infinity: Self { get } ``` |

Modified FloatingPointType.quietNaN

|  | Declaration |
| --- | --- |
| From | ``` class var quietNaN: Self { get } ``` |
| To | ``` static var quietNaN: Self { get } ``` |

Modified ImplicitlyUnwrappedOptional [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum ImplicitlyUnwrappedOptional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     init(_ v: T?)     init(nilLiteral nilLiteral: ())     func map<U>(_ f: (T) -> U) -> U!     func getMirror() -> MirrorType } ``` |
| To | ``` enum ImplicitlyUnwrappedOptional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     init(_ v: T?)     init(nilLiteral nilLiteral: ())     func map<U>(_ f: @noescape (T) -> U) -> U!     func flatMap<U>(_ f: @noescape (T) -> U!) -> U!     func getMirror() -> MirrorType } ``` |

Modified ImplicitlyUnwrappedOptional.map((T) -> U) -> U!

|  | Declaration |
| --- | --- |
| From | ``` func map<U>(_ f: (T) -> U) -> U! ``` |
| To | ``` func map<U>(_ f: @noescape (T) -> U) -> U! ``` |

Modified Int [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Int : SignedIntegerType {     var value: Builtin.Word     typealias Distance = Int     init()     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } ``` |
| To | ``` struct Int : SignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } ``` |

Modified Int.value

|  | Declaration |
| --- | --- |
| From | ``` var value: Builtin.Word ``` |
| To | ``` var value: Builtin.Int32 ``` |

Modified ObjectIdentifier [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ObjectIdentifier : Hashable {     let value: Builtin.RawPointer     func uintValue() -> UInt     var hashValue: Int { get }     init(_ x: AnyObject) } ``` | Hashable |
| To | ``` struct ObjectIdentifier : Hashable, Comparable {     let value: Builtin.RawPointer     var uintValue: UInt { get }     var hashValue: Int { get }     init(_ x: AnyObject)     init(_ x: Any.Type) } ``` | Comparable, Hashable |

Modified Optional [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum Optional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     func map<U>(_ f: (T) -> U) -> U?     func getMirror() -> MirrorType     init(nilLiteral nilLiteral: ()) } ``` |
| To | ``` enum Optional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     func map<U>(_ f: @noescape (T) -> U) -> U?     func flatMap<U>(_ f: @noescape (T) -> U?) -> U?     func getMirror() -> MirrorType     init(nilLiteral nilLiteral: ()) } ``` |

Modified Optional.map((T) -> U) -> U?

|  | Declaration |
| --- | --- |
| From | ``` func map<U>(_ f: (T) -> U) -> U? ``` |
| To | ``` func map<U>(_ f: @noescape (T) -> U) -> U? ``` |

Modified QuickLookObject [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum QuickLookObject {     case Text(String)     case Int(Int64)     case UInt(UInt64)     case Float(Double)     case Image(Any)     case Sound(Any)     case Color(Any)     case BezierPath(Any)     case AttributedString(Any)     case Rectangle(Double, Double, Double, Double)     case Point(Double, Double)     case Size(Double, Double)     case Logical(Bool)     case Range(UInt64, UInt64)     case View(Any)     case Sprite(Any)     case URL(String) } ``` |
| To | ``` enum QuickLookObject {     case Text(String)     case Int(Int64)     case UInt(UInt64)     case Float(Float32)     case Double(Float64)     case Image(Any)     case Sound(Any)     case Color(Any)     case BezierPath(Any)     case AttributedString(Any)     case Rectangle(Float64, Float64, Float64, Float64)     case Point(Float64, Float64)     case Size(Float64, Float64)     case Logical(Bool)     case Range(UInt64, UInt64)     case View(Any)     case Sprite(Any)     case URL(String) } ``` |

Modified QuickLookObject.Float

|  | Declaration |
| --- | --- |
| From | ``` case Float(Double) ``` |
| To | ``` case Float(Float32) ``` |

Modified QuickLookObject.Point

|  | Declaration |
| --- | --- |
| From | ``` case Point(Double, Double) ``` |
| To | ``` case Point(Float64, Float64) ``` |

Modified QuickLookObject.Rectangle

|  | Declaration |
| --- | --- |
| From | ``` case Rectangle(Double, Double, Double, Double) ``` |
| To | ``` case Rectangle(Float64, Float64, Float64, Float64) ``` |

Modified QuickLookObject.Size

|  | Declaration |
| --- | --- |
| From | ``` case Size(Double, Double) ``` |
| To | ``` case Size(Float64, Float64) ``` |

Modified Range [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Range<T : ForwardIndexType> : Equatable, CollectionType, Printable, DebugPrintable {     init(_ x: Range<T>)     init(start start: T, end end: T)     var isEmpty: Bool { get }     typealias Index = T     typealias Slice = Range<T>     subscript (position: T) -> T { get }     subscript (_: T._DisabledRangeIndex) -> T { get }     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T     var description: String { get }     var debugDescription: String { get } } ``` |
| To | ``` struct Range<T : ForwardIndexType> : Equatable, CollectionType, Printable, DebugPrintable {     init(_ x: Range<T>)     init(start start: T, end end: T)     var isEmpty: Bool { get }     typealias Index = T     typealias ArraySlice = Range<T>     subscript (position: T) -> T { get }     subscript (_: T._DisabledRangeIndex) -> T { get }     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T     var description: String { get }     var debugDescription: String { get } } ``` |

Modified RangeReplaceableCollectionType.replaceRange(Range<Self.Index>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` mutating func replaceRange<C : CollectionType where `Self`.Generator.Element == Self.Generator.Element>(_ subRange: Range<Self.Index>, with newElements: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where Self.Generator.Element == Self.Generator.Element>(_ subRange: Range<Self.Index>, with newElements: C) ``` |

Modified RangeReplaceableCollectionType.splice(S, atIndex: Self.Index)

|  | Declaration |
| --- | --- |
| From | ``` mutating func splice<S : CollectionType where `Self`.Generator.Element == Self.Generator.Element>(_ newElements: S, atIndex i: Self.Index) ``` |
| To | ``` mutating func splice<S : CollectionType where Self.Generator.Element == Self.Generator.Element>(_ newElements: S, atIndex i: Self.Index) ``` |

Modified StaticString [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct StaticString : UnicodeScalarLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible, Printable, DebugPrintable {     var utf8Start: UnsafePointer<UInt8> { get }     var unicodeScalar: UnicodeScalar { get }     var byteSize: Word { get }     var hasPointerRepresentation: Bool { get }     var isASCII: Bool { get }     func withUTF8Buffer<R>(_ body: (UnsafeBufferPointer<UInt8>) -> R) -> R     var stringValue: String { get }     init()     init(start start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(unicodeScalar unicodeScalar: Builtin.Int32)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: StaticString)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: StaticString)     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(stringLiteral value: StaticString)     var description: String { get }     var debugDescription: String { get } } ``` |
| To | ``` struct StaticString : UnicodeScalarLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible, Printable, DebugPrintable {     var utf8Start: UnsafePointer<UInt8> { get }     var unicodeScalar: UnicodeScalar { get }     var byteSize: Word { get }     var hasPointerRepresentation: Bool { get }     var isASCII: Bool { get }     func withUTF8Buffer<R>(_ body: @noescape (UnsafeBufferPointer<UInt8>) -> R) -> R     var stringValue: String { get }     init()     init(start start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(unicodeScalar unicodeScalar: Builtin.Int32)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: StaticString)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: StaticString)     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(stringLiteral value: StaticString)     var description: String { get }     var debugDescription: String { get } } ``` |

Modified StaticString.withUTF8Buffer((UnsafeBufferPointer<UInt8>) -> R) -> R

|  | Declaration |
| --- | --- |
| From | ``` func withUTF8Buffer<R>(_ body: (UnsafeBufferPointer<UInt8>) -> R) -> R ``` |
| To | ``` func withUTF8Buffer<R>(_ body: @noescape (UnsafeBufferPointer<UInt8>) -> R) -> R ``` |

Modified String.init(_: String.UnicodeScalarView)

|  | Declaration |
| --- | --- |
| From | ``` init(_ view: String.UnicodeScalarView) ``` |
| To | ``` init(_ unicodeScalars: String.UnicodeScalarView) ``` |

Modified String.init(count: Int, repeatedValue: Character)

|  | Declaration |
| --- | --- |
| From | ``` init(count sz: Int, repeatedValue c: Character) ``` |
| To | ``` init(count count: Int, repeatedValue c: Character) ``` |

Modified String.lowercaseString

|  | Module |
| --- | --- |
| From | Foundation |
| To | Swift |

Modified String.uppercaseString

|  | Module |
| --- | --- |
| From | Foundation |
| To | Swift |

Modified String.withCString(UnsafePointer<Int8> -> Result) -> Result

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withCString<Result>(_ f: (UnsafePointer<Int8>) -> Result) -> Result ``` | iOS 8.0 |
| To | ``` func withCString<Result>(_ f: @noescape UnsafePointer<Int8> -> Result) -> Result ``` | iOS 8.3 |

Modified String.UTF16View [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF16View : Sliceable, Reflectable {         var startIndex: Int { get }         var endIndex: Int { get }         typealias Generator         func generate() -> Generator         subscript (position: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         func getMirror() -> MirrorType     } ``` | Reflectable, Sliceable |
| To | ``` struct UTF16View : Sliceable, Reflectable, Printable, DebugPrintable {         struct Index {         }         var startIndex: String.UTF16View.Index { get }         var endIndex: String.UTF16View.Index { get }         typealias Generator         func generate() -> Generator         subscript (i: String.UTF16View.Index) -> UInt16 { get }         subscript (i: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         subscript (subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get }         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | DebugPrintable, Printable, Reflectable, Sliceable |

Modified String.UTF16View.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: Int { get } ``` |
| To | ``` var endIndex: String.UTF16View.Index { get } ``` |

Modified String.UTF16View.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: Int { get } ``` |
| To | ``` var startIndex: String.UTF16View.Index { get } ``` |

Modified String.UTF8View [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF8View : CollectionType, Reflectable {         struct Index : ForwardIndexType {             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (position: String.UTF8View.Index) -> CodeUnit { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> MirrorType     } ``` | CollectionType, Reflectable |
| To | ``` struct UTF8View : CollectionType, Reflectable, Printable, DebugPrintable {         struct Index : ForwardIndexType {             typealias Buffer = UTF8Chunk             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (position: String.UTF8View.Index) -> CodeUnit { get }         subscript (subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | CollectionType, DebugPrintable, Printable, Reflectable |

Modified String.UTF8View.Index [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Index : ForwardIndexType {             func successor() -> String.UTF8View.Index         } ``` |
| To | ``` struct Index : ForwardIndexType {             typealias Buffer = UTF8Chunk             func successor() -> String.UTF8View.Index         } ``` |

Modified String.UnicodeScalarView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnicodeScalarView : Sliceable, SequenceType, Reflectable {         struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.Generator         func getMirror() -> MirrorType     } ``` | Reflectable, SequenceType, Sliceable |
| To | ``` struct UnicodeScalarView : Sliceable, SequenceType, Reflectable, Printable, DebugPrintable {         struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.Generator         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | DebugPrintable, Printable, Reflectable, SequenceType, Sliceable |

Modified UInt [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UInt : UnsignedIntegerType {     var value: Builtin.Word     typealias Distance = Int     init()     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } ``` |
| To | ``` struct UInt : UnsignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } ``` |

Modified UInt.value

|  | Declaration |
| --- | --- |
| From | ``` var value: Builtin.Word ``` |
| To | ``` var value: Builtin.Int32 ``` |

Modified UTF8 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF8 : UnicodeCodecType {     typealias CodeUnit = UInt8     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` |
| To | ``` struct UTF8 : UnicodeCodecType {     typealias CodeUnit = UInt8     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S)     static func isContinuation(_ byte: CodeUnit) -> Bool } ``` |

Modified UnicodeCodecType.decode(G) -> UnicodeDecodingResult

|  | Declaration |
| --- | --- |
| From | ``` mutating func decode<G : GeneratorType where `Self`.CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` |
| To | ``` mutating func decode<G : GeneratorType where Self.CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` |

Modified UnicodeCodecType.encode(UnicodeScalar, output: S) [class]

|  | Declaration |
| --- | --- |
| From | ``` class func encode<S : SinkType where `Self`.CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |
| To | ``` static func encode<S : SinkType where Self.CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |

Modified UnsafeMutablePointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnsafeMutablePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     var value: Builtin.RawPointer     init()     init(_ value: Builtin.RawPointer)     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafeMutablePointer<T>     static func alloc(_ num: Int) -> UnsafeMutablePointer<T>     func dealloc(_ num: Int)     var memory: T { get nonmutating set }     func initialize(_ newvalue: T)     func move() -> T     func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveAssignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveInitializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom<C : CollectionType where T == T>(_ source: C)     func destroy()     func destroy(_ count: Int)     subscript (i: Int) -> T { get nonmutating set }     var hashValue: Int { get }     func successor() -> UnsafeMutablePointer<T>     func predecessor() -> UnsafeMutablePointer<T>     func distanceTo(_ x: UnsafeMutablePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafeMutablePointer<T> } ``` | DebugPrintable, Hashable, NilLiteralConvertible, RandomAccessIndexType, Reflectable, SinkType |
| To | ``` struct UnsafeMutablePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     init()     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafeMutablePointer<T>     static func alloc(_ num: Int) -> UnsafeMutablePointer<T>     func dealloc(_ num: Int)     var memory: T { get nonmutating set }     func initialize(_ newvalue: T)     func move() -> T     func assignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveInitializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom<C : CollectionType where T == T>(_ source: C)     func moveAssignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func destroy()     func destroy(_ count: Int)     subscript (i: Int) -> T { get nonmutating set }     var hashValue: Int { get }     func successor() -> UnsafeMutablePointer<T>     func predecessor() -> UnsafeMutablePointer<T>     func distanceTo(_ x: UnsafeMutablePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafeMutablePointer<T> } ``` | CVarArgType, DebugPrintable, Hashable, NilLiteralConvertible, RandomAccessIndexType, Reflectable, SinkType |

Modified UnsafePointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnsafePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     var value: Builtin.RawPointer     init()     init(_ value: Builtin.RawPointer)     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafePointer<T>     var memory: T { get }     subscript (i: Int) -> T { get }     var hashValue: Int { get }     func successor() -> UnsafePointer<T>     func predecessor() -> UnsafePointer<T>     func distanceTo(_ x: UnsafePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafePointer<T> } ``` | DebugPrintable, Hashable, NilLiteralConvertible, RandomAccessIndexType, Reflectable |
| To | ``` struct UnsafePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     init()     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafePointer<T>     var memory: T { get }     subscript (i: Int) -> T { get }     var hashValue: Int { get }     func successor() -> UnsafePointer<T>     func predecessor() -> UnsafePointer<T>     func distanceTo(_ x: UnsafePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafePointer<T> } ``` | CVarArgType, DebugPrintable, Hashable, NilLiteralConvertible, RandomAccessIndexType, Reflectable |

Modified Array.SubSlice

|  | Declaration |
| --- | --- |
| From | ``` typealias SubSlice = Slice<T> ``` |
| To | ``` typealias SubSlice = ArraySlice<T> ``` |

Modified ContiguousArray.SubSlice

|  | Declaration |
| --- | --- |
| From | ``` typealias SubSlice = Slice<T> ``` |
| To | ``` typealias SubSlice = ArraySlice<T> ``` |

Modified assert(() -> Bool,() -> String, StaticString, UWord)

|  | Declaration |
| --- | --- |
| From | ``` func assert(_ condition: @autoclosure () -> Bool, _ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` func assert(_ condition: @autoclosure_ condition: @autoclosure () -> Bool, _ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |

Modified assertionFailure(() -> String, StaticString, UWord)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func assertionFailure(_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` @inline(__always) func assertionFailure(_ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |

Modified contains(S,(S.Generator.Element) -> L) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func contains<S : SequenceType, L : BooleanType>(_ seq: S, _ predicate: (S.Generator.Element) -> L) -> Bool ``` |
| To | ``` func contains<S : SequenceType, L : BooleanType>(_ seq: S, _ predicate: @noescape (S.Generator.Element) -> L) -> Bool ``` |

Modified debugPrint(T)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrint<T>(_ x: T) ``` |
| To | ``` @inline(never) func debugPrint<T>(_ x: T) ``` |

Modified debugPrint(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrint<T, TargetStream : OutputStreamType>(_ x: T, inout _ target: TargetStream) ``` |
| To | ``` @inline(never) func debugPrint<T, TargetStream : OutputStreamType>(_ value: T, inout _ target: TargetStream) ``` |

Modified debugPrintln(T)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrintln<T>(_ x: T) ``` |
| To | ``` @inline(never) func debugPrintln<T>(_ x: T) ``` |

Modified debugPrintln(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrintln<T, TargetStream : OutputStreamType>(_ x: T, inout _ target: TargetStream) ``` |
| To | ``` @inline(never) func debugPrintln<T, TargetStream : OutputStreamType>(_ x: T, inout _ target: TargetStream) ``` |

Modified equal(S1, S2,(S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func equal<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element>(_ a1: S1, _ a2: S2, _ isEquivalent: (S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool ``` |
| To | ``` func equal<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element>(_ a1: S1, _ a2: S2, _ isEquivalent: @noescape (S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool ``` |

Modified extend(C, S)

|  | Declaration |
| --- | --- |
| From | ``` func extend<C : RangeReplaceableCollectionType, S : CollectionType where S.Generator.Element == S.Generator.Element>(inout _ x: C, _ newElements: S) ``` |
| To | ``` func extend<C : RangeReplaceableCollectionType, S : CollectionType where C.Generator.Element == C.Generator.Element>(inout _ x: C, _ newElements: S) ``` |

Modified fatalError(() -> String, StaticString, UWord)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func fatalError(_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` @noreturn func fatalError(_ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |

Modified lexicographicalCompare(S1, S2,(S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func lexicographicalCompare<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element>(_ a1: S1, _ a2: S2, _ less: (S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool ``` |
| To | ``` func lexicographicalCompare<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element>(_ a1: S1, _ a2: S2, isOrderedBefore less: @noescape (S1.Generator.Element, S1.Generator.Element) -> Bool) -> Bool ``` |

Modified map(T?,(T) -> U) -> U?

|  | Declaration |
| --- | --- |
| From | ``` func map<T, U>(_ x: T?, _ f: (T) -> U) -> U? ``` |
| To | ``` func map<T, U>(_ x: T?, _ f: @noescape (T) -> U) -> U? ``` |

Modified numericCast(T) -> U

|  | Declaration |
| --- | --- |
| From | ``` func numericCast<T : _SignedIntegerType, U : _SignedIntegerType>(_ x: T) -> U ``` |
| To | ``` func numericCast<T : _UnsignedIntegerType, U : _SignedIntegerType>(_ x: T) -> U ``` |

Modified precondition(() -> Bool,() -> String, StaticString, UWord)

|  | Declaration |
| --- | --- |
| From | ``` func precondition(_ condition: @autoclosure () -> Bool, _ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` func precondition(_ condition: @autoclosure_ condition: @autoclosure () -> Bool, _ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |

Modified preconditionFailure(() -> String, StaticString, UWord)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func preconditionFailure(_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` @noreturn func preconditionFailure(_ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |

Modified print(T)

|  | Declaration |
| --- | --- |
| From | ``` func print<T>(_ object: T) ``` |
| To | ``` @inline(never) func print<T>(_ value: T) ``` |

Modified print(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func print<T, TargetStream : OutputStreamType>(_ object: T, inout _ target: TargetStream) ``` |
| To | ``` @inline(never) func print<T, TargetStream : OutputStreamType>(_ value: T, inout _ target: TargetStream) ``` |

Modified println()

|  | Declaration |
| --- | --- |
| From | ``` func println() ``` |
| To | ``` @inline(never) func println() ``` |

Modified println(T)

|  | Declaration |
| --- | --- |
| From | ``` func println<T>(_ object: T) ``` |
| To | ``` @inline(never) func println<T>(_ value: T) ``` |

Modified println(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func println<T, TargetStream : OutputStreamType>(_ object: T, inout _ target: TargetStream) ``` |
| To | ``` @inline(never) func println<T, TargetStream : OutputStreamType>(_ value: T, inout _ target: TargetStream) ``` |

Modified reduce(S, U,(U, S.Generator.Element) -> U) -> U

|  | Declaration |
| --- | --- |
| From | ``` func reduce<S : SequenceType, U>(_ sequence: S, _ initial: U, _ combine: (U, S.Generator.Element) -> U) -> U ``` |
| To | ``` func reduce<S : SequenceType, U>(_ sequence: S, _ initial: U, _ combine: @noescape (U, S.Generator.Element) -> U) -> U ``` |

Modified splice(C, S, C.Index)

|  | Declaration |
| --- | --- |
| From | ``` func splice<C : RangeReplaceableCollectionType, S : CollectionType where S.Generator.Element == S.Generator.Element>(inout _ x: C, _ newElements: S, atIndex i: C.Index) ``` |
| To | ``` func splice<C : RangeReplaceableCollectionType, S : CollectionType where C.Generator.Element == C.Generator.Element>(inout _ x: C, _ newElements: S, atIndex i: C.Index) ``` |

Modified startsWith(S0, S1,(S0.Generator.Element, S0.Generator.Element) -> Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func startsWith<S0 : SequenceType, S1 : SequenceType where S0.Generator.Element == S0.Generator.Element>(_ s: S0, _ prefix: S1, _ isEquivalent: (S0.Generator.Element, S0.Generator.Element) -> Bool) -> Bool ``` |
| To | ``` func startsWith<S0 : SequenceType, S1 : SequenceType where S0.Generator.Element == S0.Generator.Element>(_ s: S0, _ prefix: S1, _ isEquivalent: @noescape (S0.Generator.Element, S0.Generator.Element) -> Bool) -> Bool ``` |

Modified toString(T) -> String

|  | Declaration |
| --- | --- |
| From | ``` func toString<T>(_ x: T) -> String ``` |
| To | ``` @inline(never) func toString<T>(_ x: T) -> String ``` |

Modified withExtendedLifetime(T,() -> Result) -> Result

|  | Declaration |
| --- | --- |
| From | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: () -> Result) -> Result ``` |
| To | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: @noescape () -> Result) -> Result ``` |

Modified withExtendedLifetime(T, T -> Result) -> Result

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: (T) -> Result) -> Result ``` | iOS 8.0 |
| To | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: @noescape T -> Result) -> Result ``` | iOS 8.3 |

Modified withUnsafeMutablePointer(T, UnsafeMutablePointer<T> -> Result) -> Result

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withUnsafeMutablePointer<T, Result>(inout _ arg: T, _ body: (UnsafeMutablePointer<T>) -> Result) -> Result ``` | iOS 8.0 |
| To | ``` func withUnsafeMutablePointer<T, Result>(inout _ arg: T, _ body: @noescape UnsafeMutablePointer<T> -> Result) -> Result ``` | iOS 8.3 |

Modified withUnsafeMutablePointers(A0, A1,(UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>) -> Result) -> Result

|  | Declaration |
| --- | --- |
| From | ``` func withUnsafeMutablePointers<A0, A1, Result>(inout _ arg0: A0, inout _ arg1: A1, _ body: (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>) -> Result) -> Result ``` |
| To | ``` func withUnsafeMutablePointers<A0, A1, Result>(inout _ arg0: A0, inout _ arg1: A1, _ body: @noescape (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>) -> Result) -> Result ``` |

Modified withUnsafeMutablePointers(A0, A1, A2,(UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>, UnsafeMutablePointer<A2>) -> Result) -> Result

|  | Declaration |
| --- | --- |
| From | ``` func withUnsafeMutablePointers<A0, A1, A2, Result>(inout _ arg0: A0, inout _ arg1: A1, inout _ arg2: A2, _ body: (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>, UnsafeMutablePointer<A2>) -> Result) -> Result ``` |
| To | ``` func withUnsafeMutablePointers<A0, A1, A2, Result>(inout _ arg0: A0, inout _ arg1: A1, inout _ arg2: A2, _ body: @noescape (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>, UnsafeMutablePointer<A2>) -> Result) -> Result ``` |

Modified withUnsafePointer(T, UnsafePointer<T> -> Result) -> Result

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withUnsafePointer<T, Result>(inout _ arg: T, _ body: (UnsafePointer<T>) -> Result) -> Result ``` | iOS 8.0 |
| To | ``` func withUnsafePointer<T, Result>(inout _ arg: T, _ body: @noescape UnsafePointer<T> -> Result) -> Result ``` | iOS 8.3 |

Modified withUnsafePointers(A0, A1,(UnsafePointer<A0>, UnsafePointer<A1>) -> Result) -> Result

|  | Declaration |
| --- | --- |
| From | ``` func withUnsafePointers<A0, A1, Result>(inout _ arg0: A0, inout _ arg1: A1, _ body: (UnsafePointer<A0>, UnsafePointer<A1>) -> Result) -> Result ``` |
| To | ``` func withUnsafePointers<A0, A1, Result>(inout _ arg0: A0, inout _ arg1: A1, _ body: @noescape (UnsafePointer<A0>, UnsafePointer<A1>) -> Result) -> Result ``` |

Modified withUnsafePointers(A0, A1, A2,(UnsafePointer<A0>, UnsafePointer<A1>, UnsafePointer<A2>) -> Result) -> Result

|  | Declaration |
| --- | --- |
| From | ``` func withUnsafePointers<A0, A1, A2, Result>(inout _ arg0: A0, inout _ arg1: A1, inout _ arg2: A2, _ body: (UnsafePointer<A0>, UnsafePointer<A1>, UnsafePointer<A2>) -> Result) -> Result ``` |
| To | ``` func withUnsafePointers<A0, A1, A2, Result>(inout _ arg0: A0, inout _ arg1: A1, inout _ arg2: A2, _ body: @noescape (UnsafePointer<A0>, UnsafePointer<A1>, UnsafePointer<A2>) -> Result) -> Result ``` |

Modified withVaList(VaListBuilder, CVaListPointer -> R) -> R

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withVaList<R>(_ builder: VaListBuilder, _ f: (CVaListPointer) -> R) -> R ``` | iOS 8.0 |
| To | ``` func withVaList<R>(_ builder: VaListBuilder, _ f: @noescape CVaListPointer -> R) -> R ``` | iOS 8.3 |

Modified withVaList([CVarArgType], CVaListPointer -> R) -> R

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withVaList<R>(_ args: [CVarArgType], _ f: (CVaListPointer) -> R) -> R ``` | iOS 8.0 |
| To | ``` func withVaList<R>(_ args: [CVarArgType], _ f: @noescape CVaListPointer -> R) -> R ``` | iOS 8.3 |

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
