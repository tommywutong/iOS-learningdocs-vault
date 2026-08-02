---
title: tvOS 9.2 API Diffs
apple_id: TP40016673
resource_type: Release Note
platform: tvOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/tvOS92APIDiffs/Swift/Swift.html
archived_at: '2026-07-18T02:58:06.654931Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [tvOS 9.2 API Diffs](tvOS%209.1%20to%209.2%20API%20Differences.md)


# Swift Changes for Swift

### Swift

Removed AnyGeneratorRemoved AnyGenerator.init()Removed AnyGenerator.next() -> Element?Removed AnySequence.init<S : SequenceType where S.Generator.Element == Element>(_: S)Removed BidirectionalIndexType.predecessor() -> SelfRemoved BidirectionalIndexType.predecessor() -> SelfRemoved CollectionType.countRemoved CollectionType.countRemoved CollectionType.dropLast(_: Int) -> Self.SubSequenceRemoved CollectionType.dropLast(_: Int) -> Self.SubSequenceRemoved CollectionType.firstRemoved CollectionType.firstRemoved CollectionType.isEmptyRemoved CollectionType.isEmptyRemoved CollectionType.prefixThrough(_: Self.Index) -> Self.SubSequenceRemoved CollectionType.prefixThrough(_: Self.Index) -> Self.SubSequenceRemoved CollectionType.prefixUpTo(_: Self.Index) -> Self.SubSequenceRemoved CollectionType.prefixUpTo(_: Self.Index) -> Self.SubSequenceRemoved CollectionType.startIndexRemoved CollectionType.startIndexRemoved CollectionType.suffix(_: Int) -> Self.SubSequenceRemoved CollectionType.suffix(_: Int) -> Self.SubSequenceRemoved CollectionType.suffixFrom(_: Self.Index) -> Self.SubSequenceRemoved CollectionType.suffixFrom(_: Self.Index) -> Self.SubSequenceRemoved Double.valueRemoved Float.valueRemoved ForwardIndexType.advancedBy(_: Self.Distance) -> SelfRemoved ForwardIndexType.advancedBy(_: Self.Distance) -> SelfRemoved ForwardIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfRemoved ForwardIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfRemoved ForwardIndexType.distanceTo(_: Self) -> Self.DistanceRemoved ForwardIndexType.distanceTo(_: Self) -> Self.DistanceRemoved Int.valueRemoved Int16.valueRemoved Int32.valueRemoved Int64.valueRemoved Int8.valueRemoved LazySequenceType.elementsRemoved LazySequenceType.elementsRemoved RandomAccessIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfRemoved RandomAccessIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfRemoved RangeReplaceableCollectionType.append(_: Self.Generator.Element)Removed RangeReplaceableCollectionType.append(_: Self.Generator.Element)Removed RangeReplaceableCollectionType.appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Removed RangeReplaceableCollectionType.appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Removed RangeReplaceableCollectionType.insert(_: Self.Generator.Element, atIndex: Self.Index)Removed RangeReplaceableCollectionType.insert(_: Self.Generator.Element, atIndex: Self.Index)Removed RangeReplaceableCollectionType.removeAll(keepCapacity: Bool)Removed RangeReplaceableCollectionType.removeAll(keepCapacity: Bool)Removed RangeReplaceableCollectionType.removeAtIndex(_: Self.Index) -> Self.Generator.ElementRemoved RangeReplaceableCollectionType.removeAtIndex(_: Self.Index) -> Self.Generator.ElementRemoved RangeReplaceableCollectionType.removeFirst() -> Self.Generator.ElementRemoved RangeReplaceableCollectionType.removeFirst() -> Self.Generator.ElementRemoved RangeReplaceableCollectionType.removeFirst(_: Int)Removed RangeReplaceableCollectionType.removeFirst(_: Int)Removed RangeReplaceableCollectionType.removeRange(_: Range<Self.Index>)Removed RangeReplaceableCollectionType.removeRange(_: Range<Self.Index>)Removed RangeReplaceableCollectionType.reserveCapacity(_: Self.Index.Distance)Removed RangeReplaceableCollectionType.reserveCapacity(_: Self.Index.Distance)Removed SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Removed SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Removed SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Removed SequenceType.forEach(_: (Self.Generator.Element) throws -> ()) rethrowsRemoved SequenceType.forEach(_: (Self.Generator.Element) throws -> ()) rethrowsRemoved SequenceType.generate() -> Self.GeneratorRemoved SequenceType.generate() -> Self.GeneratorRemoved SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Removed SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Removed SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Removed SequenceType.underestimateCount() -> IntRemoved SequenceType.underestimateCount() -> IntRemoved SequenceType.underestimateCount() -> IntRemoved SetAlgebraType.element(_: Self.Element, isDisjointWith: Self.Element) -> Bool [class]Removed SetAlgebraType.element(_: Self.Element, isDisjointWith: Self.Element) -> Bool [class]Removed SetAlgebraType.element(_: Self.Element, subsumes: Self.Element) -> Bool [class]Removed SetAlgebraType.element(_: Self.Element, subsumes: Self.Element) -> Bool [class]Removed SetAlgebraType.init<S : SequenceType where S.Generator.Element == Element>(_: S)Removed SetAlgebraType.init<S : SequenceType where S.Generator.Element == Element>(_: S)Removed SetAlgebraType.isDisjointWith(_: Self) -> BoolRemoved SetAlgebraType.isDisjointWith(_: Self) -> BoolRemoved SetAlgebraType.isEmptyRemoved SetAlgebraType.isEmptyRemoved SetAlgebraType.isSubsetOf(_: Self) -> BoolRemoved SetAlgebraType.isSubsetOf(_: Self) -> BoolRemoved SetAlgebraType.isSupersetOf(_: Self) -> BoolRemoved SetAlgebraType.isSupersetOf(_: Self) -> BoolRemoved SetAlgebraType.subtract(_: Self) -> SelfRemoved SetAlgebraType.subtract(_: Self) -> SelfRemoved SetAlgebraType.subtractInPlace(_: Self)Removed SetAlgebraType.subtractInPlace(_: Self)Removed UInt.valueRemoved UInt16.valueRemoved UInt32.valueRemoved UInt64.valueRemoved UInt8.valueRemoved UnicodeCodecType.encode(_: UnicodeScalar, output: (Self.CodeUnit) -> ()) [class]Removed UTF16.encode(_: UnicodeScalar, output: (CodeUnit) -> ()) [static]Removed UTF32.encode(_: UnicodeScalar, output: (CodeUnit) -> ()) [static]Removed UTF8.encode(_: UnicodeScalar, output: (CodeUnit) -> ()) [static]Removed !=(_: T, _: T) -> BoolRemoved !=(_: T, _: T) -> BoolRemoved !=(_: T, _: T) -> BoolRemoved +(_: C, _: S) -> CRemoved +(_: C, _: S) -> CRemoved ++(_: Int32) -> Int32Removed ++(_: Int16) -> Int16Removed ++(_: Int) -> IntRemoved ++(_: UInt64) -> UInt64Removed ++(_: UInt) -> UIntRemoved ++(_: Int8) -> Int8Removed ++(_: Int64) -> Int64Removed ++(_: T) -> TRemoved ++(_: Int) -> IntRemoved ++(_: Int8) -> Int8Removed ++(_: Int16) -> Int16Removed ++(_: Int32) -> Int32Removed ++(_: UInt8) -> UInt8Removed ++(_: UInt8) -> UInt8Removed ++(_: UInt32) -> UInt32Removed ++(_: UInt) -> UIntRemoved ++(_: Float) -> FloatRemoved ++(_: UInt16) -> UInt16Removed ++(_: Float) -> FloatRemoved ++(_: UInt16) -> UInt16Removed ++(_: Double) -> DoubleRemoved ++(_: UInt64) -> UInt64Removed ++(_: Double) -> DoubleRemoved ++(_: UInt32) -> UInt32Removed ++(_: T) -> TRemoved ++(_: Int64) -> Int64Removed --(_: UInt16) -> UInt16Removed --(_: T) -> TRemoved --(_: Double) -> DoubleRemoved --(_: T) -> TRemoved --(_: UInt16) -> UInt16Removed --(_: Int) -> IntRemoved --(_: Int16) -> Int16Removed --(_: Int64) -> Int64Removed --(_: Int8) -> Int8Removed --(_: UInt32) -> UInt32Removed --(_: Double) -> DoubleRemoved --(_: Float) -> FloatRemoved --(_: Int32) -> Int32Removed --(_: UInt64) -> UInt64Removed --(_: Int) -> IntRemoved --(_: UInt64) -> UInt64Removed --(_: Int64) -> Int64Removed --(_: UInt32) -> UInt32Removed --(_: UInt) -> UIntRemoved --(_: UInt8) -> UInt8Removed --(_: Float) -> FloatRemoved --(_: UInt) -> UIntRemoved --(_: Int32) -> Int32Removed --(_: UInt8) -> UInt8Removed --(_: Int8) -> Int8Removed --(_: Int16) -> Int16Removed ...(_: Pos, _: Pos) -> Range<Pos>Removed ...(_: Pos, _: Pos) -> Range<Pos>Removed ..<(_: Pos, _: Pos) -> Range<Pos>Removed ..<(_: Pos, _: Pos) -> Range<Pos>Removed ==(_: T, _: T) -> BoolRemoved ==(_: FloatingPointClassification, _: FloatingPointClassification) -> BoolRemoved ==(_: T, _: T) -> BoolRemoved transcode<Input : GeneratorType, InputEncoding : UnicodeCodecType, OutputEncoding : UnicodeCodecType where InputEncoding.CodeUnit == Input.Element>(_: InputEncoding.Type, _: OutputEncoding.Type, _: Input, _: (OutputEncoding.CodeUnit) -> (), stopOnError: Bool) -> BoolAdded AnyGenerator [struct]Added AnyGenerator.init<G : GeneratorType where G.Element == Element>(_: G)Added AnyGenerator.init(body: () -> Element?)Added AnyGenerator.next() -> Element?Added [AnySequence.dropFirst(_: Int) -> AnySequence<Element>](https://developer.apple.com/documentation/swift/anysequence/1538669-dropfirst)Added AnySequence.init<S : SequenceType where S.Generator.Element == Element, S.SubSequence : SequenceType, S.SubSequence.Generator.Element == Element, S.SubSequence.SubSequence == S.SubSequence>(_: S)Added [AnySequence.prefix(_: Int) -> AnySequence<Element>](https://developer.apple.com/documentation/swift/anysequence/1540601-prefix)Added BidirectionalIndexType.predecessor() -> SelfAdded BidirectionalIndexType.predecessor() -> SelfAdded CollectionType.countAdded CollectionType.countAdded CollectionType.dropLast(_: Int) -> Self.SubSequenceAdded CollectionType.dropLast(_: Int) -> Self.SubSequenceAdded CollectionType.firstAdded CollectionType.firstAdded CollectionType.isEmptyAdded CollectionType.isEmptyAdded CollectionType.popLast() -> Self.Generator.Element?Added CollectionType.prefixThrough(_: Self.Index) -> Self.SubSequenceAdded CollectionType.prefixThrough(_: Self.Index) -> Self.SubSequenceAdded CollectionType.prefixUpTo(_: Self.Index) -> Self.SubSequenceAdded CollectionType.prefixUpTo(_: Self.Index) -> Self.SubSequenceAdded CollectionType.removeFirst(_: Int)Added CollectionType.removeLast() -> Self.Generator.ElementAdded CollectionType.removeLast(_: Int)Added CollectionType.startIndexAdded CollectionType.startIndexAdded CollectionType.suffix(_: Int) -> Self.SubSequenceAdded CollectionType.suffix(_: Int) -> Self.SubSequenceAdded CollectionType.suffixFrom(_: Self.Index) -> Self.SubSequenceAdded CollectionType.suffixFrom(_: Self.Index) -> Self.SubSequenceAdded [Double.debugDescription](https://developer.apple.com/documentation/swift/double/1539408-debugdescription)Added [Float.debugDescription](https://developer.apple.com/documentation/swift/float/1538813-debugdescription)Added ForwardIndexType.advancedBy(_: Self.Distance) -> SelfAdded ForwardIndexType.advancedBy(_: Self.Distance) -> SelfAdded ForwardIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded ForwardIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded ForwardIndexType.distanceTo(_: Self) -> Self.DistanceAdded ForwardIndexType.distanceTo(_: Self) -> Self.DistanceAdded ImplicitlyUnwrappedOptional.debugDescriptionAdded LazySequenceType.elementsAdded LazySequenceType.elementsAdded RandomAccessIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded RandomAccessIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded RangeReplaceableCollectionType.append(_: Self.Generator.Element)Added RangeReplaceableCollectionType.append(_: Self.Generator.Element)Added RangeReplaceableCollectionType.appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Added RangeReplaceableCollectionType.appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Added RangeReplaceableCollectionType.init<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Added RangeReplaceableCollectionType.init<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Added RangeReplaceableCollectionType.insert(_: Self.Generator.Element, atIndex: Self.Index)Added RangeReplaceableCollectionType.insert(_: Self.Generator.Element, atIndex: Self.Index)Added RangeReplaceableCollectionType.removeAll(keepCapacity: Bool)Added RangeReplaceableCollectionType.removeAll(keepCapacity: Bool)Added RangeReplaceableCollectionType.removeAtIndex(_: Self.Index) -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeAtIndex(_: Self.Index) -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst() -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst() -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst() -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst(_: Int)Added RangeReplaceableCollectionType.removeFirst(_: Int)Added RangeReplaceableCollectionType.removeFirst(_: Int)Added RangeReplaceableCollectionType.removeLast(_: Int)Added RangeReplaceableCollectionType.removeRange(_: Range<Self.Index>)Added RangeReplaceableCollectionType.removeRange(_: Range<Self.Index>)Added RangeReplaceableCollectionType.reserveCapacity(_: Self.Index.Distance)Added RangeReplaceableCollectionType.reserveCapacity(_: Self.Index.Distance)Added SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Added SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Added SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Added SequenceType.forEach(_: (Self.Generator.Element) throws -> Void) rethrowsAdded SequenceType.forEach(_: (Self.Generator.Element) throws -> Void) rethrowsAdded SequenceType.generate() -> Self.GeneratorAdded SequenceType.generate() -> Self.GeneratorAdded SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Added SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Added SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Added SequenceType.underestimateCount() -> IntAdded SequenceType.underestimateCount() -> IntAdded SequenceType.underestimateCount() -> IntAdded SetAlgebraType.element(_: Self.Element, isDisjointWith: Self.Element) -> Bool [class]Added SetAlgebraType.element(_: Self.Element, isDisjointWith: Self.Element) -> Bool [class]Added SetAlgebraType.element(_: Self.Element, subsumes: Self.Element) -> Bool [class]Added SetAlgebraType.element(_: Self.Element, subsumes: Self.Element) -> Bool [class]Added SetAlgebraType.init<S : SequenceType where S.Generator.Element == Element>(_: S)Added SetAlgebraType.init<S : SequenceType where S.Generator.Element == Element>(_: S)Added SetAlgebraType.isDisjointWith(_: Self) -> BoolAdded SetAlgebraType.isDisjointWith(_: Self) -> BoolAdded SetAlgebraType.isEmptyAdded SetAlgebraType.isEmptyAdded SetAlgebraType.isSubsetOf(_: Self) -> BoolAdded SetAlgebraType.isSubsetOf(_: Self) -> BoolAdded SetAlgebraType.isSupersetOf(_: Self) -> BoolAdded SetAlgebraType.isSupersetOf(_: Self) -> BoolAdded SetAlgebraType.subtract(_: Self) -> SelfAdded SetAlgebraType.subtract(_: Self) -> SelfAdded SetAlgebraType.subtractInPlace(_: Self)Added SetAlgebraType.subtractInPlace(_: Self)Added UnicodeCodecType.encode(_: UnicodeScalar, output: (Self.CodeUnit) -> Void) [class]Added UTF16.encode(_: UnicodeScalar, output: (CodeUnit) -> Void) [static]Added UTF32.encode(_: UnicodeScalar, output: (CodeUnit) -> Void) [static]Added UTF8.encode(_: UnicodeScalar, output: (CodeUnit) -> Void) [static]Added [!=(_: (A, B, C, D, E), _: (A, B, C, D, E)) -> Bool](https://developer.apple.com/documentation/swift/1539308)Added [!=(_: (A, B, C), _: (A, B, C)) -> Bool](https://developer.apple.com/documentation/swift/1540139)Added !=(_: T, _: T) -> BoolAdded [!=(_: (A, B), _: (A, B)) -> Bool](https://developer.apple.com/documentation/swift/1539195)Added [!=(_: (A, B, C, D), _: (A, B, C, D)) -> Bool](https://developer.apple.com/documentation/swift/1541104)Added [!=(_: (A, B, C, D, E, F), _: (A, B, C, D, E, F)) -> Bool](https://developer.apple.com/documentation/swift/1541222)Added !=(_: T, _: T) -> BoolAdded !=(_: T, _: T) -> BoolAdded +(_: C, _: S) -> CAdded +(_: C, _: S) -> CAdded ++(_: Int32) -> Int32Added ++(_: Int) -> IntAdded ++(_: UInt) -> UIntAdded ++(_: UInt64) -> UInt64Added ++(_: Float) -> FloatAdded ++(_: UInt64) -> UInt64Added ++(_: Float) -> FloatAdded ++(_: Int8) -> Int8Added ++(_: Int8) -> Int8Added ++(_: UInt16) -> UInt16Added ++(_: Int64) -> Int64Added ++(_: Int16) -> Int16Added ++(_: Int) -> IntAdded ++(_: UInt8) -> UInt8Added ++(_: UInt32) -> UInt32Added ++(_: Int64) -> Int64Added ++(_: UInt32) -> UInt32Added ++(_: Int16) -> Int16Added ++(_: UInt8) -> UInt8Added ++(_: UInt16) -> UInt16Added ++(_: Double) -> DoubleAdded ++(_: Int32) -> Int32Added ++(_: Double) -> DoubleAdded ++(_: UInt) -> UIntAdded ++(_: T) -> TAdded ++(_: T) -> TAdded --(_: Int) -> IntAdded --(_: UInt8) -> UInt8Added --(_: T) -> TAdded --(_: Int16) -> Int16Added --(_: Int) -> IntAdded --(_: Int8) -> Int8Added --(_: Int64) -> Int64Added --(_: UInt) -> UIntAdded --(_: Int8) -> Int8Added --(_: Float) -> FloatAdded --(_: Double) -> DoubleAdded --(_: Float) -> FloatAdded --(_: Int16) -> Int16Added --(_: T) -> TAdded --(_: UInt64) -> UInt64Added --(_: Int32) -> Int32Added --(_: Double) -> DoubleAdded --(_: UInt64) -> UInt64Added --(_: UInt32) -> UInt32Added --(_: UInt16) -> UInt16Added --(_: UInt8) -> UInt8Added --(_: UInt32) -> UInt32Added --(_: UInt) -> UIntAdded --(_: Int32) -> Int32Added --(_: UInt16) -> UInt16Added --(_: Int64) -> Int64Added ...(_: Pos, _: Pos) -> Range<Pos>Added ...(_: Pos, _: Pos) -> Range<Pos>Added ..<(_: Pos, _: Pos) -> Range<Pos>Added ..<(_: Pos, _: Pos) -> Range<Pos>Added [<(_: (A, B, C), _: (A, B, C)) -> Bool](https://developer.apple.com/documentation/swift/1541272)Added [<(_: (A, B, C, D), _: (A, B, C, D)) -> Bool](https://developer.apple.com/documentation/swift/1539564)Added <(_: _SwiftNSOperatingSystemVersion, _: _SwiftNSOperatingSystemVersion) -> BoolAdded [<(_: (A, B), _: (A, B)) -> Bool](https://developer.apple.com/documentation/swift/1541163)Added [<(_: (A, B, C, D, E), _: (A, B, C, D, E)) -> Bool](https://developer.apple.com/documentation/swift/1540710)Added [<(_: (A, B, C, D, E, F), _: (A, B, C, D, E, F)) -> Bool](https://developer.apple.com/documentation/swift/1539598)Added [<=(_: (A, B, C, D, E, F), _: (A, B, C, D, E, F)) -> Bool](https://developer.apple.com/documentation/swift/1539470)Added [<=(_: (A, B, C, D), _: (A, B, C, D)) -> Bool](https://developer.apple.com/documentation/swift/1538693)Added [<=(_: (A, B, C, D, E), _: (A, B, C, D, E)) -> Bool](https://developer.apple.com/documentation/swift/1540241)Added [<=(_: (A, B), _: (A, B)) -> Bool](https://developer.apple.com/documentation/swift/1539554)Added [<=(_: (A, B, C), _: (A, B, C)) -> Bool](https://developer.apple.com/documentation/swift/1541336)Added ==(_: T, _: T) -> BoolAdded [==(_: (A, B, C, D), _: (A, B, C, D)) -> Bool](https://developer.apple.com/documentation/swift/1538987)Added [==(_: (A, B, C, D, E), _: (A, B, C, D, E)) -> Bool](https://developer.apple.com/documentation/swift/1539448)Added [==(_: (A, B), _: (A, B)) -> Bool](https://developer.apple.com/documentation/swift/1539354)Added ==(_: T, _: T) -> BoolAdded [==(_: (A, B, C), _: (A, B, C)) -> Bool](https://developer.apple.com/documentation/swift/1538449)Added [==(_: (A, B, C, D, E, F), _: (A, B, C, D, E, F)) -> Bool](https://developer.apple.com/documentation/swift/1541073)Added [>(_: (A, B, C), _: (A, B, C)) -> Bool](https://developer.apple.com/documentation/swift/1538936)Added [>(_: (A, B, C, D, E), _: (A, B, C, D, E)) -> Bool](https://developer.apple.com/documentation/swift/1540514)Added [>(_: (A, B, C, D, E, F), _: (A, B, C, D, E, F)) -> Bool](https://developer.apple.com/documentation/swift/1540839)Added [>(_: (A, B, C, D), _: (A, B, C, D)) -> Bool](https://developer.apple.com/documentation/swift/1540224)Added [>(_: (A, B), _: (A, B)) -> Bool](https://developer.apple.com/documentation/swift/1540518)Added [>=(_: (A, B, C, D, E), _: (A, B, C, D, E)) -> Bool](https://developer.apple.com/documentation/swift/1539150)Added [>=(_: (A, B), _: (A, B)) -> Bool](https://developer.apple.com/documentation/swift/1540206)Added >=(_: _SwiftNSOperatingSystemVersion, _: _SwiftNSOperatingSystemVersion) -> BoolAdded [>=(_: (A, B, C, D, E, F), _: (A, B, C, D, E, F)) -> Bool](https://developer.apple.com/documentation/swift/1541431)Added [>=(_: (A, B, C), _: (A, B, C)) -> Bool](https://developer.apple.com/documentation/swift/1539903)Added [>=(_: (A, B, C, D), _: (A, B, C, D)) -> Bool](https://developer.apple.com/documentation/swift/1538929)Added transcode<Input : GeneratorType, InputEncoding : UnicodeCodecType, OutputEncoding : UnicodeCodecType where InputEncoding.CodeUnit == Input.Element>(_: InputEncoding.Type, _: OutputEncoding.Type, _: Input, _: (OutputEncoding.CodeUnit) -> Void, stopOnError: Bool) -> BoolModified [AnySequence [struct]](https://developer.apple.com/documentation/swift/anysequence)

|  | Declaration |
| --- | --- |
| From | ``` struct AnySequence<Element> : SequenceType {     typealias T = Element     init<S : SequenceType where S.Generator.Element == Element>(_ base: S)     init<G : GeneratorType where G.Element == Element>(_ makeUnderlyingGenerator: () -> G)     func generate() -> AnyGenerator<Element> } extension AnySequence {     func underestimateCount() -> Int } ``` |
| To | ``` struct AnySequence<Element> : SequenceType {     typealias T = Element     init<S : SequenceType where S.Generator.Element == Element, S.SubSequence : SequenceType, S.SubSequence.Generator.Element == Element, S.SubSequence.SubSequence == S.SubSequence>(_ base: S)     init<G : GeneratorType where G.Element == Element>(_ makeUnderlyingGenerator: () -> G)     func generate() -> AnyGenerator<Element> } extension AnySequence {     @warn_unused_result     func dropFirst(_ n: Int) -> AnySequence<Element>     @warn_unused_result     func prefix(_ maxLength: Int) -> AnySequence<Element> } extension AnySequence {     func underestimateCount() -> Int } ``` |

Modified ArrayLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol ArrayLiteralConvertible {     typealias Element     init(arrayLiteral elements: Self.Element...) } ``` |
| To | ``` protocol ArrayLiteralConvertible {     associatedtype Element     init(arrayLiteral elements: Self.Element...) } ``` |

Modified AutoreleasingUnsafeMutablePointer.init()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified Bit [enum]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified Bit.advancedBy(_: Distance) -> Bit

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified Bit.distanceTo(_: Bit) -> Int

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified Bit.predecessor() -> Bit

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified Bit.successor() -> Bit

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified BooleanLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol BooleanLiteralConvertible {     typealias BooleanLiteralType     init(booleanLiteral value: Self.BooleanLiteralType) } ``` |
| To | ``` protocol BooleanLiteralConvertible {     associatedtype BooleanLiteralType     init(booleanLiteral value: Self.BooleanLiteralType) } ``` |

Modified CollectionType

|  | Declaration |
| --- | --- |
| From | ``` protocol CollectionType : Indexable, SequenceType {     typealias Generator : GeneratorType = IndexingGenerator<Self>     func generate() -> Self.Generator     typealias SubSequence : Indexable, SequenceType = Slice<Self>     subscript (_ position: Self.Index) -> Self.Generator.Element { get }     subscript (_ bounds: Range<Self.Index>) -> Self.SubSequence { get }     @warn_unused_result     func prefixUpTo(_ end: Self.Index) -> Self.SubSequence     @warn_unused_result     func suffixFrom(_ start: Self.Index) -> Self.SubSequence     @warn_unused_result     func prefixThrough(_ position: Self.Index) -> Self.SubSequence     var isEmpty: Bool { get }     var count: Self.Index.Distance { get }     var first: Self.Generator.Element? { get } } ``` |
| To | ``` protocol CollectionType : Indexable, SequenceType {     associatedtype Generator : GeneratorType = IndexingGenerator<Self>     func generate() -> Self.Generator     associatedtype SubSequence : Indexable, SequenceType = Slice<Self>     subscript (_ position: Self.Index) -> Self.Generator.Element { get }     subscript (_ bounds: Range<Self.Index>) -> Self.SubSequence { get }     @warn_unused_result     func prefixUpTo(_ end: Self.Index) -> Self.SubSequence     @warn_unused_result     func suffixFrom(_ start: Self.Index) -> Self.SubSequence     @warn_unused_result     func prefixThrough(_ position: Self.Index) -> Self.SubSequence     var isEmpty: Bool { get }     var count: Self.Index.Distance { get }     var first: Self.Generator.Element? { get } } ``` |

Modified CollectionType.popLast() -> Self.Generator.Element?

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified COpaquePointer.init()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified DictionaryLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol DictionaryLiteralConvertible {     typealias Key     typealias Value     init(dictionaryLiteral elements: (Self.Key, Self.Value)...) } ``` |
| To | ``` protocol DictionaryLiteralConvertible {     associatedtype Key     associatedtype Value     init(dictionaryLiteral elements: (Self.Key, Self.Value)...) } ``` |

Modified [Double [struct]](https://developer.apple.com/documentation/swift/double)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Double {     var value: Builtin.FPIEEE64     init()     init(_bits v: Builtin.FPIEEE64)     init(_ value: Double) } extension Double {     init(_ value: CGFloat) } extension Double : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Double : CustomStringConvertible {     var description: String { get } } extension Double : FloatingPointType {     static var infinity: Double { get }     static var NaN: Double { get }     static var quietNaN: Double { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Double {     var floatingPointClass: FloatingPointClassification { get } } extension Double : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Double {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Double : FloatLiteralConvertible {     init(floatLiteral value: Double) } extension Double : Comparable, Equatable { } extension Double : Hashable {     var hashValue: Int { get } } extension Double : AbsoluteValuable {     @warn_unused_result     static func abs(_ x: Double) -> Double } extension Double {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Double {     init(_ other: Float) } extension Double : Strideable {     func distanceTo(_ other: Double) -> Double     func advancedBy(_ amount: Double) -> Double } extension Double {     init?(_ text: String) } extension Double : _Reflectable { } extension Double : _CVarArgPassedAsDouble, _CVarArgAlignedType { } ``` | AbsoluteValuable, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Strideable |
| To | ``` struct Double {     init()     init(_bits v: Builtin.FPIEEE64)     init(_ value: Double) } extension Double {     init(_ value: CGFloat) } extension Double : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Double : CustomStringConvertible {     var description: String { get } } extension Double : CustomDebugStringConvertible {     var debugDescription: String { get } } extension Double : FloatingPointType {     static var infinity: Double { get }     static var NaN: Double { get }     static var quietNaN: Double { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Double {     var floatingPointClass: FloatingPointClassification { get } } extension Double : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Double {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Double : FloatLiteralConvertible {     init(floatLiteral value: Double) } extension Double : Comparable, Equatable { } extension Double : Hashable {     var hashValue: Int { get } } extension Double : AbsoluteValuable {     @warn_unused_result     static func abs(_ x: Double) -> Double } extension Double {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Double {     init(_ other: Float) } extension Double : Strideable {     func distanceTo(_ other: Double) -> Double     func advancedBy(_ amount: Double) -> Double } extension Double {     init?(_ text: String) } extension Double : _Reflectable { } extension Double : _CVarArgPassedAsDouble, _CVarArgAlignedType { } ``` | AbsoluteValuable, Comparable, CustomDebugStringConvertible, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Strideable |

Modified EnumerateGenerator.init(_: Base)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified EnumerateSequence.init(_: Base)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified ExtendedGraphemeClusterLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol ExtendedGraphemeClusterLiteralConvertible : UnicodeScalarLiteralConvertible {     typealias ExtendedGraphemeClusterLiteralType     init(extendedGraphemeClusterLiteral value: Self.ExtendedGraphemeClusterLiteralType) } ``` |
| To | ``` protocol ExtendedGraphemeClusterLiteralConvertible : UnicodeScalarLiteralConvertible {     associatedtype ExtendedGraphemeClusterLiteralType     init(extendedGraphemeClusterLiteral value: Self.ExtendedGraphemeClusterLiteralType) } ``` |

Modified [Float [struct]](https://developer.apple.com/documentation/swift/float)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Float {     var value: Builtin.FPIEEE32     init()     init(_bits v: Builtin.FPIEEE32)     init(_ value: Float) } extension Float {     init(_ value: CGFloat) } extension Float : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Float : CustomStringConvertible {     var description: String { get } } extension Float : FloatingPointType {     static var infinity: Float { get }     static var NaN: Float { get }     static var quietNaN: Float { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Float {     var floatingPointClass: FloatingPointClassification { get } } extension Float : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Float {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Float : FloatLiteralConvertible {     init(floatLiteral value: Float) } extension Float : Comparable, Equatable { } extension Float : Hashable {     var hashValue: Int { get } } extension Float : AbsoluteValuable {     @warn_unused_result     static func abs(_ x: Float) -> Float } extension Float {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Float {     init(_ other: Double) } extension Float : Strideable {     func distanceTo(_ other: Float) -> Float     func advancedBy(_ amount: Float) -> Float } extension Float {     init?(_ text: String) } extension Float : _Reflectable { } extension Float : _CVarArgPassedAsDouble, _CVarArgAlignedType { } ``` | AbsoluteValuable, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Strideable |
| To | ``` struct Float {     init()     init(_bits v: Builtin.FPIEEE32)     init(_ value: Float) } extension Float {     init(_ value: CGFloat) } extension Float : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Float : CustomStringConvertible {     var description: String { get } } extension Float : CustomDebugStringConvertible {     var debugDescription: String { get } } extension Float : FloatingPointType {     static var infinity: Float { get }     static var NaN: Float { get }     static var quietNaN: Float { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Float {     var floatingPointClass: FloatingPointClassification { get } } extension Float : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Float {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Float : FloatLiteralConvertible {     init(floatLiteral value: Float) } extension Float : Comparable, Equatable { } extension Float : Hashable {     var hashValue: Int { get } } extension Float : AbsoluteValuable {     @warn_unused_result     static func abs(_ x: Float) -> Float } extension Float {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Float {     init(_ other: Double) } extension Float : Strideable {     func distanceTo(_ other: Float) -> Float     func advancedBy(_ amount: Float) -> Float } extension Float {     init?(_ text: String) } extension Float : _Reflectable { } extension Float : _CVarArgPassedAsDouble, _CVarArgAlignedType { } ``` | AbsoluteValuable, Comparable, CustomDebugStringConvertible, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Strideable |

Modified [FloatingPointClassification [enum]](https://developer.apple.com/documentation/swift/floatingpointclassification)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum FloatingPointClassification {     case SignalingNaN     case QuietNaN     case NegativeInfinity     case NegativeNormal     case NegativeSubnormal     case NegativeZero     case PositiveZero     case PositiveSubnormal     case PositiveNormal     case PositiveInfinity } extension FloatingPointClassification : Equatable { } ``` | Equatable |
| To | ``` enum FloatingPointClassification {     case SignalingNaN     case QuietNaN     case NegativeInfinity     case NegativeNormal     case NegativeSubnormal     case NegativeZero     case PositiveZero     case PositiveSubnormal     case PositiveNormal     case PositiveInfinity } ``` | -- |

Modified FloatLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol FloatLiteralConvertible {     typealias FloatLiteralType     init(floatLiteral value: Self.FloatLiteralType) } ``` |
| To | ``` protocol FloatLiteralConvertible {     associatedtype FloatLiteralType     init(floatLiteral value: Self.FloatLiteralType) } ``` |

Modified ForwardIndexType

|  | Declaration |
| --- | --- |
| From | ``` protocol ForwardIndexType : _Incrementable {     typealias Distance : _SignedIntegerType = Int     @warn_unused_result     func advancedBy(_ n: Self.Distance) -> Self     @warn_unused_result     func advancedBy(_ n: Self.Distance, limit limit: Self) -> Self     @warn_unused_result     func distanceTo(_ end: Self) -> Self.Distance } ``` |
| To | ``` protocol ForwardIndexType : _Incrementable {     associatedtype Distance : _SignedIntegerType = Int     @warn_unused_result     func advancedBy(_ n: Self.Distance) -> Self     @warn_unused_result     func advancedBy(_ n: Self.Distance, limit limit: Self) -> Self     @warn_unused_result     func distanceTo(_ end: Self) -> Self.Distance } ``` |

Modified GeneratorType

|  | Declaration |
| --- | --- |
| From | ``` protocol GeneratorType {     typealias Element     @warn_unused_result     mutating func next() -> Self.Element? } ``` |
| To | ``` protocol GeneratorType {     associatedtype Element     @warn_unused_result     mutating func next() -> Self.Element? } ``` |

Modified ImplicitlyUnwrappedOptional [enum]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum ImplicitlyUnwrappedOptional<Wrapped> : _Reflectable, NilLiteralConvertible {     case None     case Some(Wrapped)     typealias T = Wrapped     init()     init(_ some: Wrapped)     init(_ v: Wrapped?)     init(nilLiteral nilLiteral: ())     @warn_unused_result     func map<U>(@noescape _ f: (Wrapped) throws -> U) rethrows -> U!     @warn_unused_result     func flatMap<U>(@noescape _ f: (Wrapped) throws -> U!) rethrows -> U! } extension ImplicitlyUnwrappedOptional : CustomStringConvertible {     var description: String { get } } extension ImplicitlyUnwrappedOptional : _ObjectiveCBridgeable { } ``` | CustomStringConvertible, NilLiteralConvertible |
| To | ``` enum ImplicitlyUnwrappedOptional<Wrapped> : _Reflectable, NilLiteralConvertible {     case None     case Some(Wrapped)     typealias T = Wrapped     init()     init(_ some: Wrapped)     init(_ v: Wrapped?)     init(nilLiteral nilLiteral: ())     @warn_unused_result     func map<U>(@noescape _ f: (Wrapped) throws -> U) rethrows -> U!     @warn_unused_result     func flatMap<U>(@noescape _ f: (Wrapped) throws -> U!) rethrows -> U! } extension ImplicitlyUnwrappedOptional : CustomStringConvertible {     var description: String { get } } extension ImplicitlyUnwrappedOptional : CustomDebugStringConvertible {     var debugDescription: String { get } } extension ImplicitlyUnwrappedOptional : _ObjectiveCBridgeable { } ``` | CustomDebugStringConvertible, CustomStringConvertible, NilLiteralConvertible |

Modified ImplicitlyUnwrappedOptional.flatMap<U>(_: (Wrapped) throws -> U!) rethrows -> U!

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified ImplicitlyUnwrappedOptional.init()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified ImplicitlyUnwrappedOptional.map<U>(_: (Wrapped) throws -> U) rethrows -> U!

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified Indexable

|  | Declaration |
| --- | --- |
| From | ``` protocol Indexable {     typealias Index : ForwardIndexType     var startIndex: Self.Index { get }     var endIndex: Self.Index { get }     subscript (_ position: Self.Index) -> Self._Element { get } } ``` |
| To | ``` protocol Indexable {     associatedtype Index : ForwardIndexType     var startIndex: Self.Index { get }     var endIndex: Self.Index { get }     subscript (_ position: Self.Index) -> Self._Element { get } } ``` |

Modified [Int [struct]](https://developer.apple.com/documentation/swift/int)

|  | Declaration |
| --- | --- |
| From | ``` struct Int : SignedIntegerType, Comparable, Equatable {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } extension Int {     init(_ value: CGFloat) } extension Int : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Int : RandomAccessIndexType {     func successor() -> Int     func predecessor() -> Int     func distanceTo(_ other: Int) -> Distance     func advancedBy(_ n: Distance) -> Int } extension Int : Hashable {     var hashValue: Int { get } } extension Int : CustomStringConvertible {     var description: String { get } } extension Int {     static func addWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func divideWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     func toIntMax() -> IntMax } extension Int : SignedNumberType { } extension Int {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(bitPattern bitPattern: UInt) } extension Int : BitwiseOperationsType {     static var allZeros: Int { get } } extension Int {     init(_ other: Float)     init(_ other: Double) } extension Int {     init?(_ text: String, radix radix: Int = default) } extension Int : _Reflectable { } extension Int : MirrorPathType { } extension Int : CVarArgType { } ``` |
| To | ``` struct Int : SignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } extension Int {     init(_ value: CGFloat) } extension Int : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Int : RandomAccessIndexType {     func successor() -> Int     func predecessor() -> Int     func distanceTo(_ other: Int) -> Distance     func advancedBy(_ n: Distance) -> Int } extension Int : Hashable {     var hashValue: Int { get } } extension Int : CustomStringConvertible {     var description: String { get } } extension Int {     static func addWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func divideWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     func toIntMax() -> IntMax } extension Int : SignedNumberType { } extension Int {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(bitPattern bitPattern: UInt) } extension Int : BitwiseOperationsType {     static var allZeros: Int { get } } extension Int {     init(_ other: Float)     init(_ other: Double) } extension Int {     init?(_ text: String, radix radix: Int = default) } extension Int : _Reflectable { } extension Int : MirrorPathType { } extension Int : CVarArgType { } ``` |

Modified [Int16 [struct]](https://developer.apple.com/documentation/swift/int16)

|  | Declaration |
| --- | --- |
| From | ``` struct Int16 : SignedIntegerType, Comparable, Equatable {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int16)     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } extension Int16 {     init(_ value: CGFloat) } extension Int16 : Hashable {     var hashValue: Int { get } } extension Int16 : CustomStringConvertible {     var description: String { get } } extension Int16 : RandomAccessIndexType {     func successor() -> Int16     func predecessor() -> Int16     func distanceTo(_ other: Int16) -> Distance     func advancedBy(_ n: Distance) -> Int16 } extension Int16 {     static func addWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func divideWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     func toIntMax() -> IntMax } extension Int16 : SignedNumberType { } extension Int16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt16) } extension Int16 : BitwiseOperationsType {     static var allZeros: Int16 { get } } extension Int16 {     init(_ other: Float)     init(_ other: Double) } extension Int16 {     init?(_ text: String, radix radix: Int = default) } extension Int16 : _Reflectable { } extension Int16 : CVarArgType { } ``` |
| To | ``` struct Int16 : SignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int16)     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } extension Int16 {     init(_ value: CGFloat) } extension Int16 : Hashable {     var hashValue: Int { get } } extension Int16 : CustomStringConvertible {     var description: String { get } } extension Int16 : RandomAccessIndexType {     func successor() -> Int16     func predecessor() -> Int16     func distanceTo(_ other: Int16) -> Distance     func advancedBy(_ n: Distance) -> Int16 } extension Int16 {     static func addWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func divideWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     func toIntMax() -> IntMax } extension Int16 : SignedNumberType { } extension Int16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt16) } extension Int16 : BitwiseOperationsType {     static var allZeros: Int16 { get } } extension Int16 {     init(_ other: Float)     init(_ other: Double) } extension Int16 {     init?(_ text: String, radix radix: Int = default) } extension Int16 : _Reflectable { } extension Int16 : CVarArgType { } ``` |

Modified [Int32 [struct]](https://developer.apple.com/documentation/swift/int32)

|  | Declaration |
| --- | --- |
| From | ``` struct Int32 : SignedIntegerType, Comparable, Equatable {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int32)     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } extension Int32 {     init(_ value: CGFloat) } extension Int32 : Hashable {     var hashValue: Int { get } } extension Int32 : CustomStringConvertible {     var description: String { get } } extension Int32 : RandomAccessIndexType {     func successor() -> Int32     func predecessor() -> Int32     func distanceTo(_ other: Int32) -> Distance     func advancedBy(_ n: Distance) -> Int32 } extension Int32 {     static func addWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func divideWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     func toIntMax() -> IntMax } extension Int32 : SignedNumberType { } extension Int32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt32) } extension Int32 : BitwiseOperationsType {     static var allZeros: Int32 { get } } extension Int32 {     init(_ other: Float)     init(_ other: Double) } extension Int32 {     init?(_ text: String, radix radix: Int = default) } extension Int32 : _Reflectable { } extension Int32 : CVarArgType { } ``` |
| To | ``` struct Int32 : SignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int32)     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } extension Int32 {     init(_ value: CGFloat) } extension Int32 : Hashable {     var hashValue: Int { get } } extension Int32 : CustomStringConvertible {     var description: String { get } } extension Int32 : RandomAccessIndexType {     func successor() -> Int32     func predecessor() -> Int32     func distanceTo(_ other: Int32) -> Distance     func advancedBy(_ n: Distance) -> Int32 } extension Int32 {     static func addWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func divideWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     func toIntMax() -> IntMax } extension Int32 : SignedNumberType { } extension Int32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt32) } extension Int32 : BitwiseOperationsType {     static var allZeros: Int32 { get } } extension Int32 {     init(_ other: Float)     init(_ other: Double) } extension Int32 {     init?(_ text: String, radix radix: Int = default) } extension Int32 : _Reflectable { } extension Int32 : CVarArgType { } ``` |

Modified [Int64 [struct]](https://developer.apple.com/documentation/swift/int64)

|  | Declaration |
| --- | --- |
| From | ``` struct Int64 : SignedIntegerType, Comparable, Equatable {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64)     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } extension Int64 {     init(_ value: CGFloat) } extension Int64 : Hashable {     var hashValue: Int { get } } extension Int64 : CustomStringConvertible {     var description: String { get } } extension Int64 : RandomAccessIndexType {     func successor() -> Int64     func predecessor() -> Int64     func distanceTo(_ other: Int64) -> Distance     func advancedBy(_ n: Distance) -> Int64 } extension Int64 {     static func addWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func divideWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     func toIntMax() -> IntMax } extension Int64 : SignedNumberType { } extension Int64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: UInt64) } extension Int64 : BitwiseOperationsType {     static var allZeros: Int64 { get } } extension Int64 {     init(_ other: Float)     init(_ other: Double) } extension Int64 {     init?(_ text: String, radix radix: Int = default) } extension Int64 : _Reflectable { } extension Int64 : CVarArgType, _CVarArgAlignedType { } ``` |
| To | ``` struct Int64 : SignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64)     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } extension Int64 {     init(_ value: CGFloat) } extension Int64 : Hashable {     var hashValue: Int { get } } extension Int64 : CustomStringConvertible {     var description: String { get } } extension Int64 : RandomAccessIndexType {     func successor() -> Int64     func predecessor() -> Int64     func distanceTo(_ other: Int64) -> Distance     func advancedBy(_ n: Distance) -> Int64 } extension Int64 {     static func addWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func divideWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     func toIntMax() -> IntMax } extension Int64 : SignedNumberType { } extension Int64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: UInt64) } extension Int64 : BitwiseOperationsType {     static var allZeros: Int64 { get } } extension Int64 {     init(_ other: Float)     init(_ other: Double) } extension Int64 {     init?(_ text: String, radix radix: Int = default) } extension Int64 : _Reflectable { } extension Int64 : CVarArgType, _CVarArgAlignedType { } ``` |

Modified [Int8 [struct]](https://developer.apple.com/documentation/swift/int8)

|  | Declaration |
| --- | --- |
| From | ``` struct Int8 : SignedIntegerType, Comparable, Equatable {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: Int8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int8)     static var max: Int8 { get }     static var min: Int8 { get } } extension Int8 {     init(_ value: CGFloat) } extension Int8 : Hashable {     var hashValue: Int { get } } extension Int8 : CustomStringConvertible {     var description: String { get } } extension Int8 : RandomAccessIndexType {     func successor() -> Int8     func predecessor() -> Int8     func distanceTo(_ other: Int8) -> Distance     func advancedBy(_ n: Distance) -> Int8 } extension Int8 {     static func addWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func divideWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     func toIntMax() -> IntMax } extension Int8 : SignedNumberType { } extension Int8 {     init(_ v: UInt8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt8) } extension Int8 : BitwiseOperationsType {     static var allZeros: Int8 { get } } extension Int8 {     init(_ other: Float)     init(_ other: Double) } extension Int8 {     init?(_ text: String, radix radix: Int = default) } extension Int8 : _Reflectable { } extension Int8 : CVarArgType { } ``` |
| To | ``` struct Int8 : SignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: Int8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int8)     static var max: Int8 { get }     static var min: Int8 { get } } extension Int8 {     init(_ value: CGFloat) } extension Int8 : Hashable {     var hashValue: Int { get } } extension Int8 : CustomStringConvertible {     var description: String { get } } extension Int8 : RandomAccessIndexType {     func successor() -> Int8     func predecessor() -> Int8     func distanceTo(_ other: Int8) -> Distance     func advancedBy(_ n: Distance) -> Int8 } extension Int8 {     static func addWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func divideWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     func toIntMax() -> IntMax } extension Int8 : SignedNumberType { } extension Int8 {     init(_ v: UInt8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt8) } extension Int8 : BitwiseOperationsType {     static var allZeros: Int8 { get } } extension Int8 {     init(_ other: Float)     init(_ other: Double) } extension Int8 {     init?(_ text: String, radix radix: Int = default) } extension Int8 : _Reflectable { } extension Int8 : CVarArgType { } ``` |

Modified IntegerLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol IntegerLiteralConvertible {     typealias IntegerLiteralType     init(integerLiteral value: Self.IntegerLiteralType) } ``` |
| To | ``` protocol IntegerLiteralConvertible {     associatedtype IntegerLiteralType     init(integerLiteral value: Self.IntegerLiteralType) } ``` |

Modified IntervalType

|  | Declaration |
| --- | --- |
| From | ``` protocol IntervalType {     typealias Bound : Comparable     @warn_unused_result     func contains(_ value: Self.Bound) -> Bool     @warn_unused_result     func clamp(_ intervalToClamp: Self) -> Self     var isEmpty: Bool { get }     var start: Self.Bound { get }     var end: Self.Bound { get } } ``` |
| To | ``` protocol IntervalType {     associatedtype Bound : Comparable     @warn_unused_result     func contains(_ value: Self.Bound) -> Bool     @warn_unused_result     func clamp(_ intervalToClamp: Self) -> Self     var isEmpty: Bool { get }     var start: Self.Bound { get }     var end: Self.Bound { get } } ``` |

Modified LazyCollectionType

|  | Declaration |
| --- | --- |
| From | ``` protocol LazyCollectionType : CollectionType, LazySequenceType {     typealias Elements : CollectionType = Self } ``` |
| To | ``` protocol LazyCollectionType : CollectionType, LazySequenceType {     associatedtype Elements : CollectionType = Self } ``` |

Modified LazyFilterCollection.init(_: Base, whereElementsSatisfy: (Base.Generator.Element) -> Bool)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified LazyFilterGenerator.init(_: Base, whereElementsSatisfy: (Base.Element) -> Bool)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified LazyMapCollection.init(_: Base, transform: (Base.Generator.Element) -> Element)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified LazyMapSequence.init(_: Base, transform: (Base.Generator.Element) -> Element)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified LazySequenceType

|  | Declaration |
| --- | --- |
| From | ``` protocol LazySequenceType : SequenceType {     typealias Elements : SequenceType = Self     var elements: Self.Elements { get }     var array: [Self.Generator.Element] { get } } ``` |
| To | ``` protocol LazySequenceType : SequenceType {     associatedtype Elements : SequenceType = Self     var elements: Self.Elements { get }     var array: [Self.Generator.Element] { get } } ``` |

Modified LazySequenceType.array

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified MutableCollectionType

|  | Declaration |
| --- | --- |
| From | ``` protocol MutableCollectionType : MutableIndexable, CollectionType {     typealias SubSequence = MutableSlice<Self>     subscript (_ position: Self.Index) -> Self.Generator.Element { get set }     subscript (_ bounds: Range<Self.Index>) -> Self.SubSequence { get set } } ``` |
| To | ``` protocol MutableCollectionType : MutableIndexable, CollectionType {     associatedtype SubSequence : CollectionType = MutableSlice<Self>     subscript (_ position: Self.Index) -> Self.Generator.Element { get set }     subscript (_ bounds: Range<Self.Index>) -> Self.SubSequence { get set } } ``` |

Modified MutableIndexable

|  | Declaration |
| --- | --- |
| From | ``` protocol MutableIndexable {     typealias Index : ForwardIndexType     var startIndex: Self.Index { get }     var endIndex: Self.Index { get }     subscript (_ position: Self.Index) -> Self._Element { get set } } ``` |
| To | ``` protocol MutableIndexable {     associatedtype Index : ForwardIndexType     var startIndex: Self.Index { get }     var endIndex: Self.Index { get }     subscript (_ position: Self.Index) -> Self._Element { get set } } ``` |

Modified MutableSlice.init(base: Base, bounds: Range<Base.Index>)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified MutableSliceable

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified MutableSliceable.subscript(_: Range<Self.Index>) -> Self.SubSequence

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified OptionSetType

|  | Declaration |
| --- | --- |
| From | ``` protocol OptionSetType : SetAlgebraType, RawRepresentable {     typealias Element = Self     init(rawValue rawValue: Self.RawValue) } ``` |
| To | ``` protocol OptionSetType : SetAlgebraType, RawRepresentable {     associatedtype Element = Self     init(rawValue rawValue: Self.RawValue) } ``` |

Modified PermutationGenerator [struct]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified PermutationGenerator.init(elements: C, indices: Indices)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified PermutationGenerator.next() -> C.Generator.Element?

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified [PlaygroundQuickLook [enum]](https://developer.apple.com/documentation/swift/playgroundquicklook)

|  | Declaration |
| --- | --- |
| From | ``` enum PlaygroundQuickLook {     case Text(String)     case Int(Int64)     case UInt(UInt64)     case Float(Float32)     case Double(Float64)     case Image(Any)     case Sound(Any)     case Color(Any)     case BezierPath(Any)     case AttributedString(Any)     case Rectangle(Float64, Float64, Float64, Float64)     case Point(Float64, Float64)     case Size(Float64, Float64)     case Logical(Bool)     case Range(UInt64, UInt64)     case View(Any)     case Sprite(Any)     case URL(String) } extension PlaygroundQuickLook {     init(reflecting subject: Any) } ``` |
| To | ``` enum PlaygroundQuickLook {     case Text(String)     case Int(Int64)     case UInt(UInt64)     case Float(Float32)     case Double(Float64)     case Image(Any)     case Sound(Any)     case Color(Any)     case BezierPath(Any)     case AttributedString(Any)     case Rectangle(Float64, Float64, Float64, Float64)     case Point(Float64, Float64)     case Size(Float64, Float64)     case Logical(Bool)     case Range(Int64, Int64)     case View(Any)     case Sprite(Any)     case URL(String) } extension PlaygroundQuickLook {     init(reflecting subject: Any) } ``` |

Modified PlaygroundQuickLook.Range

|  | Declaration |
| --- | --- |
| From | ``` case Range(UInt64, UInt64) ``` |
| To | ``` case Range(Int64, Int64) ``` |

Modified Range.init(start: Element, end: Element)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified RangeGenerator.endIndex

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified RangeGenerator.init(_: Range<Element>)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified RangeGenerator.startIndex

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified RangeReplaceableCollectionType

|  | Declaration |
| --- | --- |
| From | ``` protocol RangeReplaceableCollectionType : CollectionType {     init()     mutating func replaceRange<C : CollectionType where C.Generator.Element == Generator.Element>(_ subRange: Range<Self.Index>, with newElements: C)     mutating func reserveCapacity(_ n: Self.Index.Distance)     mutating func append(_ x: Self.Generator.Element)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_ newElements: S)     mutating func insert(_ newElement: Self.Generator.Element, atIndex i: Self.Index)     mutating func insertContentsOf<S : CollectionType where S.Generator.Element == Generator.Element>(_ newElements: S, at i: Self.Index)     mutating func removeAtIndex(_ i: Self.Index) -> Self.Generator.Element     mutating func removeFirst() -> Self.Generator.Element     mutating func removeFirst(_ n: Int)     mutating func removeRange(_ subRange: Range<Self.Index>)     mutating func removeAll(keepCapacity keepCapacity: Bool) } ``` |
| To | ``` protocol RangeReplaceableCollectionType : CollectionType {     init()     mutating func replaceRange<C : CollectionType where C.Generator.Element == Generator.Element>(_ subRange: Range<Self.Index>, with newElements: C)     mutating func reserveCapacity(_ n: Self.Index.Distance)     init<S : SequenceType where S.Generator.Element == Generator.Element>(_ elements: S)     mutating func append(_ x: Self.Generator.Element)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_ newElements: S)     mutating func insert(_ newElement: Self.Generator.Element, atIndex i: Self.Index)     mutating func insertContentsOf<S : CollectionType where S.Generator.Element == Generator.Element>(_ newElements: S, at i: Self.Index)     mutating func removeAtIndex(_ i: Self.Index) -> Self.Generator.Element     mutating func removeFirst() -> Self.Generator.Element     mutating func removeFirst(_ n: Int)     mutating func removeRange(_ subRange: Range<Self.Index>)     mutating func removeAll(keepCapacity keepCapacity: Bool) } ``` |

Modified RawByte [struct]

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified [RawRepresentable](https://developer.apple.com/documentation/swift/rawrepresentable)

|  | Declaration |
| --- | --- |
| From | ``` protocol RawRepresentable {     typealias RawValue     init?(rawValue rawValue: Self.RawValue)     var rawValue: Self.RawValue { get } } ``` |
| To | ``` protocol RawRepresentable {     associatedtype RawValue     init?(rawValue rawValue: Self.RawValue)     var rawValue: Self.RawValue { get } } ``` |

Modified ReverseCollection.init(_: Base)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified ReverseIndexType

|  | Declaration |
| --- | --- |
| From | ``` protocol ReverseIndexType : BidirectionalIndexType {     typealias Base : BidirectionalIndexType     typealias Distance : _SignedIntegerType = Self.Base.Distance     var base: Self.Base { get }     init(_ base: Self.Base) } ``` |
| To | ``` protocol ReverseIndexType : BidirectionalIndexType {     associatedtype Base : BidirectionalIndexType     associatedtype Distance : _SignedIntegerType = Self.Base.Distance     var base: Self.Base { get }     init(_ base: Self.Base) } ``` |

Modified ReverseRandomAccessCollection.init(_: Base)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified SequenceType

|  | Declaration |
| --- | --- |
| From | ``` protocol SequenceType {     typealias Generator : GeneratorType     typealias SubSequence     @warn_unused_result     func generate() -> Self.Generator     @warn_unused_result     func underestimateCount() -> Int     @warn_unused_result     func map<T>(@noescape _ transform: (Self.Generator.Element) throws -> T) rethrows -> [T]     @warn_unused_result     func filter(@noescape _ includeElement: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]     func forEach(@noescape _ body: (Self.Generator.Element) throws -> ()) rethrows     @warn_unused_result     func dropFirst(_ n: Int) -> Self.SubSequence     @warn_unused_result     func dropLast(_ n: Int) -> Self.SubSequence     @warn_unused_result     func prefix(_ maxLength: Int) -> Self.SubSequence     @warn_unused_result     func suffix(_ maxLength: Int) -> Self.SubSequence     @warn_unused_result     func split(_ maxSplit: Int, allowEmptySlices allowEmptySlices: Bool, @noescape isSeparator isSeparator: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.SubSequence] } ``` |
| To | ``` protocol SequenceType {     associatedtype Generator : GeneratorType     associatedtype SubSequence     @warn_unused_result     func generate() -> Self.Generator     @warn_unused_result     func underestimateCount() -> Int     @warn_unused_result     func map<T>(@noescape _ transform: (Self.Generator.Element) throws -> T) rethrows -> [T]     @warn_unused_result     func filter(@noescape _ includeElement: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]     func forEach(@noescape _ body: (Self.Generator.Element) throws -> Void) rethrows     @warn_unused_result     func dropFirst(_ n: Int) -> Self.SubSequence     @warn_unused_result     func dropLast(_ n: Int) -> Self.SubSequence     @warn_unused_result     func prefix(_ maxLength: Int) -> Self.SubSequence     @warn_unused_result     func suffix(_ maxLength: Int) -> Self.SubSequence     @warn_unused_result     func split(_ maxSplit: Int, allowEmptySlices allowEmptySlices: Bool, @noescape isSeparator isSeparator: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.SubSequence] } ``` |

Modified SequenceType.dropFirst(_: Int) -> AnySequence<Self.Generator.Element>

|  | Generics[Extension Constraints] |
| --- | --- |
| From | -- |
| To | <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol> : <Symbol>SequenceType</Symbol></Syntax>, <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol>.<Symbol>Generator</Symbol>.<Symbol>Element</Symbol> == <Symbol>Generator</Symbol>.<Symbol>Element</Symbol></Syntax>, <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol>.<Symbol>SubSequence</Symbol> == <Symbol>SubSequence</Symbol></Syntax> |

Modified SequenceType.dropLast(_: Int) -> AnySequence<Self.Generator.Element>

|  | Generics[Extension Constraints] |
| --- | --- |
| From | -- |
| To | <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol> : <Symbol>SequenceType</Symbol></Syntax>, <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol>.<Symbol>Generator</Symbol>.<Symbol>Element</Symbol> == <Symbol>Generator</Symbol>.<Symbol>Element</Symbol></Syntax>, <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol>.<Symbol>SubSequence</Symbol> == <Symbol>SubSequence</Symbol></Syntax> |

Modified SequenceType.prefix(_: Int) -> AnySequence<Self.Generator.Element>

|  | Generics[Extension Constraints] |
| --- | --- |
| From | -- |
| To | <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol> : <Symbol>SequenceType</Symbol></Syntax>, <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol>.<Symbol>Generator</Symbol>.<Symbol>Element</Symbol> == <Symbol>Generator</Symbol>.<Symbol>Element</Symbol></Syntax>, <Syntax xml:space="preserve"><Symbol>SubSequence</Symbol>.<Symbol>SubSequence</Symbol> == <Symbol>SubSequence</Symbol></Syntax> |

Modified SetAlgebraType

|  | Declaration |
| --- | --- |
| From | ``` protocol SetAlgebraType : Equatable, ArrayLiteralConvertible {     typealias Element     init()     @warn_unused_result     func contains(_ member: Self.Element) -> Bool     @warn_unused_result     func union(_ other: Self) -> Self     @warn_unused_result     func intersect(_ other: Self) -> Self     @warn_unused_result     func exclusiveOr(_ other: Self) -> Self     mutating func insert(_ member: Self.Element)     mutating func remove(_ member: Self.Element) -> Self.Element?     mutating func unionInPlace(_ other: Self)     mutating func intersectInPlace(_ other: Self)     mutating func exclusiveOrInPlace(_ other: Self)     @warn_unused_result     func subtract(_ other: Self) -> Self     @warn_unused_result     func isSubsetOf(_ other: Self) -> Bool     @warn_unused_result     func isDisjointWith(_ other: Self) -> Bool     @warn_unused_result     func isSupersetOf(_ other: Self) -> Bool     var isEmpty: Bool { get }     init<S : SequenceType where S.Generator.Element == Element>(_ sequence: S)     mutating func subtractInPlace(_ other: Self)     @warn_unused_result     static func element(_ a: Self.Element, subsumes b: Self.Element) -> Bool     @warn_unused_result     static func element(_ a: Self.Element, isDisjointWith b: Self.Element) -> Bool } ``` |
| To | ``` protocol SetAlgebraType : Equatable, ArrayLiteralConvertible {     associatedtype Element     init()     @warn_unused_result     func contains(_ member: Self.Element) -> Bool     @warn_unused_result     func union(_ other: Self) -> Self     @warn_unused_result     func intersect(_ other: Self) -> Self     @warn_unused_result     func exclusiveOr(_ other: Self) -> Self     mutating func insert(_ member: Self.Element)     mutating func remove(_ member: Self.Element) -> Self.Element?     mutating func unionInPlace(_ other: Self)     mutating func intersectInPlace(_ other: Self)     mutating func exclusiveOrInPlace(_ other: Self)     @warn_unused_result     func subtract(_ other: Self) -> Self     @warn_unused_result     func isSubsetOf(_ other: Self) -> Bool     @warn_unused_result     func isDisjointWith(_ other: Self) -> Bool     @warn_unused_result     func isSupersetOf(_ other: Self) -> Bool     var isEmpty: Bool { get }     init<S : SequenceType where S.Generator.Element == Element>(_ sequence: S)     mutating func subtractInPlace(_ other: Self)     @warn_unused_result     static func element(_ a: Self.Element, subsumes b: Self.Element) -> Bool     @warn_unused_result     static func element(_ a: Self.Element, isDisjointWith b: Self.Element) -> Bool } ``` |

Modified [Slice.init(base: Base, bounds: Range<Base.Index>)](https://developer.apple.com/documentation/swift/slice/1540308-init)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified [Strideable](https://developer.apple.com/documentation/swift/strideable)

|  | Declaration |
| --- | --- |
| From | ``` protocol Strideable : Comparable, _Strideable {     typealias Stride : SignedNumberType     @warn_unused_result     func distanceTo(_ other: Self) -> Self.Stride     @warn_unused_result     func advancedBy(_ n: Self.Stride) -> Self } ``` |
| To | ``` protocol Strideable : Comparable {     associatedtype Stride : SignedNumberType     @warn_unused_result     func distanceTo(_ other: Self) -> Self.Stride     @warn_unused_result     func advancedBy(_ n: Self.Stride) -> Self } ``` |

Modified StringLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol StringLiteralConvertible : ExtendedGraphemeClusterLiteralConvertible {     typealias StringLiteralType     init(stringLiteral value: Self.StringLiteralType) } ``` |
| To | ``` protocol StringLiteralConvertible : ExtendedGraphemeClusterLiteralConvertible {     associatedtype StringLiteralType     init(stringLiteral value: Self.StringLiteralType) } ``` |

Modified [UInt [struct]](https://developer.apple.com/documentation/swift/uint)

|  | Declaration |
| --- | --- |
| From | ``` struct UInt : UnsignedIntegerType, Comparable, Equatable {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } extension UInt {     init(_ value: CGFloat) } extension UInt : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension UInt : Hashable {     var hashValue: Int { get } } extension UInt : CustomStringConvertible {     var description: String { get } } extension UInt : RandomAccessIndexType {     func successor() -> UInt     func predecessor() -> UInt     func distanceTo(_ other: UInt) -> Distance     func advancedBy(_ n: Distance) -> UInt } extension UInt {     static func addWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: Int)     init(bitPattern bitPattern: Int) } extension UInt : BitwiseOperationsType {     static var allZeros: UInt { get } } extension UInt {     init(_ other: Float)     init(_ other: Double) } extension UInt {     init?(_ text: String, radix radix: Int = default) } extension UInt : _Reflectable { } extension UInt : CVarArgType { } ``` |
| To | ``` struct UInt : UnsignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } extension UInt {     init(_ value: CGFloat) } extension UInt : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension UInt : Hashable {     var hashValue: Int { get } } extension UInt : CustomStringConvertible {     var description: String { get } } extension UInt : RandomAccessIndexType {     func successor() -> UInt     func predecessor() -> UInt     func distanceTo(_ other: UInt) -> Distance     func advancedBy(_ n: Distance) -> UInt } extension UInt {     static func addWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: Int)     init(bitPattern bitPattern: Int) } extension UInt : BitwiseOperationsType {     static var allZeros: UInt { get } } extension UInt {     init(_ other: Float)     init(_ other: Double) } extension UInt {     init?(_ text: String, radix radix: Int = default) } extension UInt : _Reflectable { } extension UInt : CVarArgType { } ``` |

Modified [UInt16 [struct]](https://developer.apple.com/documentation/swift/uint16)

|  | Declaration |
| --- | --- |
| From | ``` struct UInt16 : UnsignedIntegerType, Comparable, Equatable {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt16)     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } extension UInt16 {     init(_ value: CGFloat) } extension UInt16 : Hashable {     var hashValue: Int { get } } extension UInt16 : CustomStringConvertible {     var description: String { get } } extension UInt16 : RandomAccessIndexType {     func successor() -> UInt16     func predecessor() -> UInt16     func distanceTo(_ other: UInt16) -> Distance     func advancedBy(_ n: Distance) -> UInt16 } extension UInt16 {     static func addWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int16) } extension UInt16 : BitwiseOperationsType {     static var allZeros: UInt16 { get } } extension UInt16 {     init(_ other: Float)     init(_ other: Double) } extension UInt16 {     init?(_ text: String, radix radix: Int = default) } extension UInt16 : _Reflectable { } extension UInt16 : CVarArgType { } ``` |
| To | ``` struct UInt16 : UnsignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt16)     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } extension UInt16 {     init(_ value: CGFloat) } extension UInt16 : Hashable {     var hashValue: Int { get } } extension UInt16 : CustomStringConvertible {     var description: String { get } } extension UInt16 : RandomAccessIndexType {     func successor() -> UInt16     func predecessor() -> UInt16     func distanceTo(_ other: UInt16) -> Distance     func advancedBy(_ n: Distance) -> UInt16 } extension UInt16 {     static func addWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int16) } extension UInt16 : BitwiseOperationsType {     static var allZeros: UInt16 { get } } extension UInt16 {     init(_ other: Float)     init(_ other: Double) } extension UInt16 {     init?(_ text: String, radix radix: Int = default) } extension UInt16 : _Reflectable { } extension UInt16 : CVarArgType { } ``` |

Modified [UInt32 [struct]](https://developer.apple.com/documentation/swift/uint32)

|  | Declaration |
| --- | --- |
| From | ``` struct UInt32 : UnsignedIntegerType, Comparable, Equatable {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt32)     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } extension UInt32 {     init(_ value: CGFloat) } extension UInt32 : Hashable {     var hashValue: Int { get } } extension UInt32 : CustomStringConvertible {     var description: String { get } } extension UInt32 : RandomAccessIndexType {     func successor() -> UInt32     func predecessor() -> UInt32     func distanceTo(_ other: UInt32) -> Distance     func advancedBy(_ n: Distance) -> UInt32 } extension UInt32 {     static func addWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int32) } extension UInt32 : BitwiseOperationsType {     static var allZeros: UInt32 { get } } extension UInt32 {     init(_ other: Float)     init(_ other: Double) } extension UInt32 {     init?(_ text: String, radix radix: Int = default) } extension UInt32 : _Reflectable { } extension UInt32 {     init(_ v: UnicodeScalar) } extension UInt32 : CVarArgType { } ``` |
| To | ``` struct UInt32 : UnsignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt32)     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } extension UInt32 {     init(_ value: CGFloat) } extension UInt32 : Hashable {     var hashValue: Int { get } } extension UInt32 : CustomStringConvertible {     var description: String { get } } extension UInt32 : RandomAccessIndexType {     func successor() -> UInt32     func predecessor() -> UInt32     func distanceTo(_ other: UInt32) -> Distance     func advancedBy(_ n: Distance) -> UInt32 } extension UInt32 {     static func addWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int32) } extension UInt32 : BitwiseOperationsType {     static var allZeros: UInt32 { get } } extension UInt32 {     init(_ other: Float)     init(_ other: Double) } extension UInt32 {     init?(_ text: String, radix radix: Int = default) } extension UInt32 : _Reflectable { } extension UInt32 {     init(_ v: UnicodeScalar) } extension UInt32 : CVarArgType { } ``` |

Modified [UInt64 [struct]](https://developer.apple.com/documentation/swift/uint64)

|  | Declaration |
| --- | --- |
| From | ``` struct UInt64 : UnsignedIntegerType, Comparable, Equatable {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt64)     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } extension UInt64 {     init(_ value: CGFloat) } extension UInt64 : Hashable {     var hashValue: Int { get } } extension UInt64 : CustomStringConvertible {     var description: String { get } } extension UInt64 : RandomAccessIndexType {     func successor() -> UInt64     func predecessor() -> UInt64     func distanceTo(_ other: UInt64) -> Distance     func advancedBy(_ n: Distance) -> UInt64 } extension UInt64 {     static func addWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: Int64) } extension UInt64 : BitwiseOperationsType {     static var allZeros: UInt64 { get } } extension UInt64 {     init(_ other: Float)     init(_ other: Double) } extension UInt64 {     init?(_ text: String, radix radix: Int = default) } extension UInt64 : _Reflectable { } extension UInt64 {     init(_ v: UnicodeScalar) } extension UInt64 : CVarArgType, _CVarArgAlignedType { } ``` |
| To | ``` struct UInt64 : UnsignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt64)     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } extension UInt64 {     init(_ value: CGFloat) } extension UInt64 : Hashable {     var hashValue: Int { get } } extension UInt64 : CustomStringConvertible {     var description: String { get } } extension UInt64 : RandomAccessIndexType {     func successor() -> UInt64     func predecessor() -> UInt64     func distanceTo(_ other: UInt64) -> Distance     func advancedBy(_ n: Distance) -> UInt64 } extension UInt64 {     static func addWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: Int64) } extension UInt64 : BitwiseOperationsType {     static var allZeros: UInt64 { get } } extension UInt64 {     init(_ other: Float)     init(_ other: Double) } extension UInt64 {     init?(_ text: String, radix radix: Int = default) } extension UInt64 : _Reflectable { } extension UInt64 {     init(_ v: UnicodeScalar) } extension UInt64 : CVarArgType, _CVarArgAlignedType { } ``` |

Modified [UInt8 [struct]](https://developer.apple.com/documentation/swift/uint8)

|  | Declaration |
| --- | --- |
| From | ``` struct UInt8 : UnsignedIntegerType, Comparable, Equatable {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: UInt8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt8)     static var max: UInt8 { get }     static var min: UInt8 { get } } extension UInt8 {     init(_ value: CGFloat) } extension UInt8 : Hashable {     var hashValue: Int { get } } extension UInt8 : CustomStringConvertible {     var description: String { get } } extension UInt8 : RandomAccessIndexType {     func successor() -> UInt8     func predecessor() -> UInt8     func distanceTo(_ other: UInt8) -> Distance     func advancedBy(_ n: Distance) -> UInt8 } extension UInt8 {     static func addWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt8 {     init(_ v: Int8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int8) } extension UInt8 : BitwiseOperationsType {     static var allZeros: UInt8 { get } } extension UInt8 {     init(_ other: Float)     init(_ other: Double) } extension UInt8 {     init?(_ text: String, radix radix: Int = default) } extension UInt8 : _Reflectable { } extension UInt8 {     init(ascii v: UnicodeScalar) } extension UInt8 : CVarArgType { } ``` |
| To | ``` struct UInt8 : UnsignedIntegerType, Comparable, Equatable {     typealias Distance = Int     init()     init(_ value: UInt8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt8)     static var max: UInt8 { get }     static var min: UInt8 { get } } extension UInt8 {     init(_ value: CGFloat) } extension UInt8 : Hashable {     var hashValue: Int { get } } extension UInt8 : CustomStringConvertible {     var description: String { get } } extension UInt8 : RandomAccessIndexType {     func successor() -> UInt8     func predecessor() -> UInt8     func distanceTo(_ other: UInt8) -> Distance     func advancedBy(_ n: Distance) -> UInt8 } extension UInt8 {     static func addWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt8 {     init(_ v: Int8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int8) } extension UInt8 : BitwiseOperationsType {     static var allZeros: UInt8 { get } } extension UInt8 {     init(_ other: Float)     init(_ other: Double) } extension UInt8 {     init?(_ text: String, radix radix: Int = default) } extension UInt8 : _Reflectable { } extension UInt8 {     init(ascii v: UnicodeScalar) } extension UInt8 : CVarArgType { } ``` |

Modified UnicodeCodecType

|  | Declaration |
| --- | --- |
| From | ``` protocol UnicodeCodecType {     typealias CodeUnit     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output output: (Self.CodeUnit) -> ()) } ``` |
| To | ``` protocol UnicodeCodecType {     associatedtype CodeUnit     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output output: (Self.CodeUnit) -> Void) } ``` |

Modified UnicodeScalarLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol UnicodeScalarLiteralConvertible {     typealias UnicodeScalarLiteralType     init(unicodeScalarLiteral value: Self.UnicodeScalarLiteralType) } ``` |
| To | ``` protocol UnicodeScalarLiteralConvertible {     associatedtype UnicodeScalarLiteralType     init(unicodeScalarLiteral value: Self.UnicodeScalarLiteralType) } ``` |

Modified [Unmanaged.autorelease() -> Unmanaged<Instance>](https://developer.apple.com/documentation/swift/unmanaged/1538691-autorelease)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified [Unmanaged.retain() -> Unmanaged<Instance>](https://developer.apple.com/documentation/swift/unmanaged/1541092-retain)

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified UnsafeMutablePointer.init()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified UnsafePointer.init()

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified UTF16 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF16 : UnicodeCodecType {     typealias CodeUnit = UInt16     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> ()) } extension UTF16 {     @warn_unused_result     static func width(_ x: UnicodeScalar) -> Int     @warn_unused_result     static func leadSurrogate(_ x: UnicodeScalar) -> CodeUnit     @warn_unused_result     static func trailSurrogate(_ x: UnicodeScalar) -> CodeUnit     @warn_unused_result     static func isLeadSurrogate(_ x: CodeUnit) -> Bool     @warn_unused_result     static func isTrailSurrogate(_ x: CodeUnit) -> Bool     @warn_unused_result     static func measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Input.Element>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? } ``` |
| To | ``` struct UTF16 : UnicodeCodecType {     typealias CodeUnit = UInt16     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> Void) } extension UTF16 {     @warn_unused_result     static func width(_ x: UnicodeScalar) -> Int     @warn_unused_result     static func leadSurrogate(_ x: UnicodeScalar) -> CodeUnit     @warn_unused_result     static func trailSurrogate(_ x: UnicodeScalar) -> CodeUnit     @warn_unused_result     static func isLeadSurrogate(_ x: CodeUnit) -> Bool     @warn_unused_result     static func isTrailSurrogate(_ x: CodeUnit) -> Bool     @warn_unused_result     static func measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Input.Element>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? } ``` |

Modified UTF32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF32 : UnicodeCodecType {     typealias CodeUnit = UInt32     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> ()) } ``` |
| To | ``` struct UTF32 : UnicodeCodecType {     typealias CodeUnit = UInt32     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> Void) } ``` |

Modified UTF8 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF8 : UnicodeCodecType {     typealias CodeUnit = UInt8     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> ())     @warn_unused_result     static func isContinuation(_ byte: CodeUnit) -> Bool } ``` |
| To | ``` struct UTF8 : UnicodeCodecType {     typealias CodeUnit = UInt8     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> Void)     @warn_unused_result     static func isContinuation(_ byte: CodeUnit) -> Bool } ``` |

Modified VaListBuilder

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified <(_: T, _: T) -> Bool

|  | Declaration | Generics[Constraints] |
| --- | --- | --- |
| From | ``` func <<T : _Strideable>(_ x: T, _ y: T) -> Bool ``` | ``` T : _Strideable ``` |
| To | ``` func <<T : Strideable>(_ x: T, _ y: T) -> Bool ``` | ``` T : Strideable ``` |

Modified anyGenerator<G : GeneratorType>(_: G) -> AnyGenerator<G.Element>

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified anyGenerator<Element>(_: () -> Element?) -> AnyGenerator<Element>

|  | Declaration | Deprecation |
| --- | --- | --- |
| From | ``` @warn_unused_result func anyGenerator<Element>(_ body: () -> Element?) -> AnyGenerator<Element> ``` | -- |
| To | ``` func anyGenerator<Element>(_ body: () -> Element?) -> AnyGenerator<Element> ``` | tvOS 9.2 |

Modified ArrayLiteralConvertible.Element

|  | Declaration |
| --- | --- |
| From | ``` typealias Element ``` |
| To | ``` associatedtype Element ``` |

Modified [assert(_: () -> Bool, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/swift/1541112-assert)

|  | Declaration |
| --- | --- |
| From | ``` func assert(@autoclosure _ condition: () -> Bool, @autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |
| To | ``` func assert(@autoclosure _ condition: () -> Bool, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [assertionFailure(_: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/swift/1539616-assertionfailure)

|  | Declaration |
| --- | --- |
| From | ``` func assertionFailure(@autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |
| To | ``` func assertionFailure(@autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified BooleanLiteralConvertible.BooleanLiteralType

|  | Declaration |
| --- | --- |
| From | ``` typealias BooleanLiteralType ``` |
| To | ``` associatedtype BooleanLiteralType ``` |

Modified CollectionType.Generator

|  | Declaration |
| --- | --- |
| From | ``` typealias Generator : GeneratorType = IndexingGenerator<Self> ``` |
| To | ``` associatedtype Generator : GeneratorType = IndexingGenerator<Self> ``` |

Modified CollectionType.SubSequence

|  | Declaration |
| --- | --- |
| From | ``` typealias SubSequence : Indexable, SequenceType = Slice<Self> ``` |
| To | ``` associatedtype SubSequence : Indexable, SequenceType = Slice<Self> ``` |

Modified DictionaryLiteralConvertible.Key

|  | Declaration |
| --- | --- |
| From | ``` typealias Key ``` |
| To | ``` associatedtype Key ``` |

Modified DictionaryLiteralConvertible.Value

|  | Declaration |
| --- | --- |
| From | ``` typealias Value ``` |
| To | ``` associatedtype Value ``` |

Modified ExtendedGraphemeClusterLiteralConvertible.ExtendedGraphemeClusterLiteralType

|  | Declaration |
| --- | --- |
| From | ``` typealias ExtendedGraphemeClusterLiteralType ``` |
| To | ``` associatedtype ExtendedGraphemeClusterLiteralType ``` |

Modified [fatalError(_: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/swift/1538698-fatalerror)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func fatalError(@autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |
| To | ``` @noreturn func fatalError(@autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified FloatLiteralConvertible.FloatLiteralType

|  | Declaration |
| --- | --- |
| From | ``` typealias FloatLiteralType ``` |
| To | ``` associatedtype FloatLiteralType ``` |

Modified ForwardIndexType.Distance

|  | Declaration |
| --- | --- |
| From | ``` typealias Distance : _SignedIntegerType = Int ``` |
| To | ``` associatedtype Distance : _SignedIntegerType = Int ``` |

Modified GeneratorType.Element

|  | Declaration |
| --- | --- |
| From | ``` typealias Element ``` |
| To | ``` associatedtype Element ``` |

Modified Indexable.Index

|  | Declaration |
| --- | --- |
| From | ``` typealias Index : ForwardIndexType ``` |
| To | ``` associatedtype Index : ForwardIndexType ``` |

Modified IntegerLiteralConvertible.IntegerLiteralType

|  | Declaration |
| --- | --- |
| From | ``` typealias IntegerLiteralType ``` |
| To | ``` associatedtype IntegerLiteralType ``` |

Modified IntervalType.Bound

|  | Declaration |
| --- | --- |
| From | ``` typealias Bound : Comparable ``` |
| To | ``` associatedtype Bound : Comparable ``` |

Modified LazyCollectionType.Elements

|  | Declaration |
| --- | --- |
| From | ``` typealias Elements : CollectionType = Self ``` |
| To | ``` associatedtype Elements : CollectionType = Self ``` |

Modified LazySequenceType.Elements

|  | Declaration |
| --- | --- |
| From | ``` typealias Elements : SequenceType = Self ``` |
| To | ``` associatedtype Elements : SequenceType = Self ``` |

Modified MutableCollectionType.SubSequence

|  | Declaration |
| --- | --- |
| From | ``` typealias SubSequence = MutableSlice<Self> ``` |
| To | ``` associatedtype SubSequence : CollectionType = MutableSlice<Self> ``` |

Modified MutableIndexable.Index

|  | Declaration |
| --- | --- |
| From | ``` typealias Index : ForwardIndexType ``` |
| To | ``` associatedtype Index : ForwardIndexType ``` |

Modified OptionSetType.Element

|  | Declaration |
| --- | --- |
| From | ``` typealias Element = Self ``` |
| To | ``` associatedtype Element = Self ``` |

Modified [precondition(_: () -> Bool, _: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/swift/1540960-precondition)

|  | Declaration |
| --- | --- |
| From | ``` func precondition(@autoclosure _ condition: () -> Bool, @autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |
| To | ``` func precondition(@autoclosure _ condition: () -> Bool, @autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [preconditionFailure(_: () -> String, file: StaticString, line: UInt)](https://developer.apple.com/documentation/swift/1539374-preconditionfailure)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func preconditionFailure(@autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |
| To | ``` @noreturn func preconditionFailure(@autoclosure _ message: () -> String = default, file file: StaticString = #file, line line: UInt = #line) ``` |

Modified [RawRepresentable.RawValue](https://developer.apple.com/documentation/swift/rawrepresentable/1540809-rawvalue)

|  | Declaration |
| --- | --- |
| From | ``` typealias RawValue ``` |
| To | ``` associatedtype RawValue ``` |

Modified ReverseIndexType.Base

|  | Declaration |
| --- | --- |
| From | ``` typealias Base : BidirectionalIndexType ``` |
| To | ``` associatedtype Base : BidirectionalIndexType ``` |

Modified ReverseIndexType.Distance

|  | Declaration |
| --- | --- |
| From | ``` typealias Distance : _SignedIntegerType = Self.Base.Distance ``` |
| To | ``` associatedtype Distance : _SignedIntegerType = Self.Base.Distance ``` |

Modified SequenceType.Generator

|  | Declaration |
| --- | --- |
| From | ``` typealias Generator : GeneratorType ``` |
| To | ``` associatedtype Generator : GeneratorType ``` |

Modified SequenceType.SubSequence

|  | Declaration |
| --- | --- |
| From | ``` typealias SubSequence ``` |
| To | ``` associatedtype SubSequence ``` |

Modified SetAlgebraType.Element

|  | Declaration |
| --- | --- |
| From | ``` typealias Element ``` |
| To | ``` associatedtype Element ``` |

Modified [Strideable.Stride](https://developer.apple.com/documentation/swift/strideable/1541220-stride)

|  | Declaration |
| --- | --- |
| From | ``` typealias Stride : SignedNumberType ``` |
| To | ``` associatedtype Stride : SignedNumberType ``` |

Modified StringLiteralConvertible.StringLiteralType

|  | Declaration |
| --- | --- |
| From | ``` typealias StringLiteralType ``` |
| To | ``` associatedtype StringLiteralType ``` |

Modified UnicodeCodecType.CodeUnit

|  | Declaration |
| --- | --- |
| From | ``` typealias CodeUnit ``` |
| To | ``` associatedtype CodeUnit ``` |

Modified UnicodeScalarLiteralConvertible.UnicodeScalarLiteralType

|  | Declaration |
| --- | --- |
| From | ``` typealias UnicodeScalarLiteralType ``` |
| To | ``` associatedtype UnicodeScalarLiteralType ``` |

Modified unsafeUnwrap<T>(_: T?) -> T

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

Modified withVaList<R>(_: VaListBuilder, _: CVaListPointer -> R) -> R

|  | Deprecation |
| --- | --- |
| From | -- |
| To | tvOS 9.2 |

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
