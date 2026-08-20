---
title: iOS 9.0 API Diffs
apple_id: TP40016222
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS90APIDiffs/Swift/Swift.html
archived_at: '2026-07-18T02:56:59.260591Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.0 API Diffs](iOS%208.3%20to%20iOS%209.0%20API%20Differences.md)


# Swift Changes for Swift

### Swift

Removed Array.extend(_: S)Removed Array.filter(_: (T) -> Bool) -> [T]Removed Array.firstRemoved Array.flatMap(_: (T) -> [U]) -> [U]Removed Array.generate() -> IndexingGenerator<[T]>Removed Array.getMirror() -> MirrorTypeRemoved Array.init(_: _ArrayBuffer<T>)Removed Array.init(_fromCocoaArray: _NSArrayCoreType, noCopy: Bool)Removed Array.init(_uninitializedCount: Int)Removed Array.isEmptyRemoved Array.join(_: S) -> [T]Removed Array.lastRemoved Array.map(_: (T) -> U) -> [U]Removed Array.reduce(_: U, combine: (U, T) -> U) -> URemoved Array.removeRange(_: Range<Int>)Removed Array.replaceRange(_: Range<Int>, with: C)Removed Array.reverse() -> [T]Removed Array.sort(_: (T, T) -> Bool)Removed Array.sorted(_: (T, T) -> Bool) -> [T]Removed Array.splice(_: S, atIndex: Int)Removed Array.withUnsafeBufferPointer(_: (UnsafeBufferPointer<T>) -> R) -> RRemoved Array.withUnsafeMutableBufferPointer(_: (inout UnsafeMutableBufferPointer<T>) -> R) -> RRemoved ArraySlice.extend(_: S)Removed ArraySlice.filter(_: (T) -> Bool) -> ArraySlice<T>Removed ArraySlice.firstRemoved ArraySlice.flatMap(_: (T) -> ArraySlice<U>) -> ArraySlice<U>Removed ArraySlice.generate() -> IndexingGenerator<ArraySlice<T>>Removed ArraySlice.getMirror() -> MirrorTypeRemoved ArraySlice.init(_: _SliceBuffer<T>)Removed ArraySlice.init(_uninitializedCount: Int)Removed ArraySlice.isEmptyRemoved ArraySlice.join(_: S) -> ArraySlice<T>Removed ArraySlice.lastRemoved ArraySlice.map(_: (T) -> U) -> ArraySlice<U>Removed ArraySlice.reduce(_: U, combine: (U, T) -> U) -> URemoved ArraySlice.removeRange(_: Range<Int>)Removed ArraySlice.replaceRange(_: Range<Int>, with: C)Removed ArraySlice.reverse() -> ArraySlice<T>Removed ArraySlice.sort(_: (T, T) -> Bool)Removed ArraySlice.sorted(_: (T, T) -> Bool) -> ArraySlice<T>Removed ArraySlice.splice(_: S, atIndex: Int)Removed ArraySlice.withUnsafeBufferPointer(_: (UnsafeBufferPointer<T>) -> R) -> RRemoved ArraySlice.withUnsafeMutableBufferPointer(_: (inout UnsafeMutableBufferPointer<T>) -> R) -> RRemoved AutoreleasingUnsafeMutablePointer.encode() -> [Word]Removed AutoreleasingUnsafeMutablePointer.init(_: UnsafePointer<U>)Removed BidirectionalIndexType.predecessor() -> SelfRemoved BidirectionalReverseView [struct]Removed BidirectionalReverseView.endIndexRemoved BidirectionalReverseView.generate() -> IndexingGenerator<BidirectionalReverseView<T>>Removed BidirectionalReverseView.startIndexRemoved BidirectionalReverseView.subscript() -> T.Generator.ElementRemoved Bit.getMirror() -> MirrorTypeRemoved BitwiseOperationsType.&(_: Self, _: Self) -> Self [class]Removed BitwiseOperationsType.^(_: Self, _: Self) -> Self [class]Removed BitwiseOperationsType.|(_: Self, _: Self) -> Self [class]Removed BitwiseOperationsType.~(_: Self) -> Self [class]Removed Bool.getMirror() -> MirrorTypeRemoved Bool.init(_: Builtin.Int1)Removed Bool.valueRemoved CFunctionPointer [struct]Removed CFunctionPointer.debugDescriptionRemoved CFunctionPointer.encode() -> [Word]Removed CFunctionPointer.hashValueRemoved CFunctionPointer.init()Removed CFunctionPointer.init(_: COpaquePointer)Removed CFunctionPointer.init(nilLiteral: ())Removed CFunctionPointer.valueRemoved Character.getMirror() -> MirrorTypeRemoved Character.utf16Removed Character.Representation [enum]Removed Character.Representation.LargeRemoved Character.Representation.SmallRemoved CharacterLiteralConvertibleRemoved CharacterLiteralConvertible.init(characterLiteral: CharacterLiteralType)Removed ClosedInterval.getMirror() -> MirrorTypeRemoved CollectionOfOne.elementRemoved CollectionOfOne.getMirror() -> MirrorTypeRemoved CollectionType.endIndexRemoved CollectionType.startIndexRemoved CollectionType.subscript() -> Self.Generator.ElementRemoved CollectionType.subscript() -> _ElementRemoved Comparable.<(_: Self, _: Self) -> Bool [class]Removed Comparable.<=(_: Self, _: Self) -> Bool [class]Removed Comparable.>(_: Self, _: Self) -> Bool [class]Removed Comparable.>=(_: Self, _: Self) -> Bool [class]Removed ContiguousArray.extend(_: S)Removed ContiguousArray.filter(_: (T) -> Bool) -> ContiguousArray<T>Removed ContiguousArray.firstRemoved ContiguousArray.flatMap(_: (T) -> ContiguousArray<U>) -> ContiguousArray<U>Removed ContiguousArray.generate() -> IndexingGenerator<ContiguousArray<T>>Removed ContiguousArray.getMirror() -> MirrorTypeRemoved ContiguousArray.init(_: _ContiguousArrayBuffer<T>)Removed ContiguousArray.init(_uninitializedCount: Int)Removed ContiguousArray.isEmptyRemoved ContiguousArray.join(_: S) -> ContiguousArray<T>Removed ContiguousArray.lastRemoved ContiguousArray.map(_: (T) -> U) -> ContiguousArray<U>Removed ContiguousArray.reduce(_: U, combine: (U, T) -> U) -> URemoved ContiguousArray.removeRange(_: Range<Int>)Removed ContiguousArray.replaceRange(_: Range<Int>, with: C)Removed ContiguousArray.reverse() -> ContiguousArray<T>Removed ContiguousArray.sort(_: (T, T) -> Bool)Removed ContiguousArray.sorted(_: (T, T) -> Bool) -> ContiguousArray<T>Removed ContiguousArray.splice(_: S, atIndex: Int)Removed ContiguousArray.withUnsafeBufferPointer(_: (UnsafeBufferPointer<T>) -> R) -> RRemoved ContiguousArray.withUnsafeMutableBufferPointer(_: (inout UnsafeMutableBufferPointer<T>) -> R) -> RRemoved COpaquePointer.encode() -> [Word]Removed COpaquePointer.init(_: CFunctionPointer<T>)Removed COpaquePointer.init(_: Builtin.RawPointer)Removed CVaListPointer.valueRemoved CVarArgType.encode() -> [Word]Removed DebugPrintableRemoved DebugPrintable.debugDescriptionRemoved Dictionary.getMirror() -> MirrorTypeRemoved Dictionary.keysRemoved Dictionary.removeAtIndex(_: DictionaryIndex<Key, Value>)Removed Dictionary.valuesRemoved DictionaryGeneratorRepresentation [enum]Removed DictionaryIndexRepresentation [enum]Removed DictionaryMirrorRemoved DictionaryMirror.countRemoved DictionaryMirror.dispositionRemoved DictionaryMirror.init(_: [Key : Value])Removed DictionaryMirror.objectIdentifierRemoved DictionaryMirror.quickLookObjectRemoved DictionaryMirror.subscript() -> (String, MirrorType)Removed DictionaryMirror.summaryRemoved DictionaryMirror.valueRemoved DictionaryMirror.valueTypeRemoved DictionaryMirrorPosition [struct]Removed DictionaryMirrorPosition.DictionaryPosRemoved DictionaryMirrorPosition.init(_: [Key : Value])Removed DictionaryMirrorPosition.successor()Removed Double.encode() -> [Word]Removed Double.getMirror() -> MirrorTypeRemoved EmptyCollection.getMirror() -> MirrorTypeRemoved EmptyGenerator.generate() -> EmptyGenerator<T>Removed EnumerateGenerator.baseRemoved EnumerateGenerator.countRemoved EnumerateGenerator.generate() -> EnumerateGenerator<Base>Removed EnumerateSequence.baseRemoved Equatable.==(_: Self, _: Self) -> Bool [class]Removed ExtensibleCollectionTypeRemoved FilterCollectionView [struct]Removed FilterCollectionView.endIndexRemoved FilterCollectionView.generate() -> FilterGenerator<Base.Generator>Removed FilterCollectionView.init(_: Base, includeElement: (Base.Generator.Element) -> Bool)Removed FilterCollectionView.startIndexRemoved FilterCollectionView.subscript() -> Base.Generator.ElementRemoved FilterCollectionViewIndex [struct]Removed FilterCollectionViewIndex.successor() -> FilterCollectionViewIndex<Base>Removed FilterGenerator [struct]Removed FilterGenerator.generate() -> FilterGenerator<Base>Removed FilterGenerator.next() -> Base.Element?Removed FilterSequenceView [struct]Removed FilterSequenceView.generate() -> FilterGenerator<Base.Generator>Removed Float.encode() -> [Word]Removed Float.getMirror() -> MirrorTypeRemoved GeneratorOf [struct]Removed GeneratorOf.generate() -> GeneratorOf<T>Removed GeneratorOf.init(_: () -> T?)Removed GeneratorOf.init(_: G)Removed GeneratorOf.next() -> T?Removed GeneratorOfOne.elementsRemoved GeneratorOfOne.generate() -> GeneratorOfOne<T>Removed GeneratorSequence.generate() -> GeneratorSequence<G>Removed HalfOpenInterval.getMirror() -> MirrorTypeRemoved ImplicitlyUnwrappedOptional.flatMap(_: (T) -> U!) -> U!Removed ImplicitlyUnwrappedOptional.getMirror() -> MirrorTypeRemoved ImplicitlyUnwrappedOptional.map(_: (T) -> U) -> U!Removed Index.init(_: String.Index, within: String.UTF8View)Removed Index.init(_: String.Index, within: String.UTF16View)Removed Index.samePositionIn(_: String) -> String.Index?Removed Index.samePositionIn(_: String) -> String.Index?Removed IndexingGenerator.generate() -> IndexingGenerator<C>Removed IndexingGenerator.init(_: C)Removed IndexingGenerator.next() -> C._Element?Removed Int.encode() -> [Word]Removed Int.getMirror() -> MirrorTypeRemoved Int16.encode() -> [Word]Removed Int16.getMirror() -> MirrorTypeRemoved Int32.encode() -> [Word]Removed Int32.getMirror() -> MirrorTypeRemoved Int64.encode() -> [Word]Removed Int64.getMirror() -> MirrorTypeRemoved Int8.encode() -> [Word]Removed Int8.getMirror() -> MirrorTypeRemoved IntegerArithmeticType.%(_: Self, _: Self) -> Self [class]Removed IntegerArithmeticType.\*(_: Self, _: Self) -> Self [class]Removed IntegerArithmeticType.+(_: Self, _: Self) -> Self [class]Removed IntegerArithmeticType.-(_: Self, _: Self) -> Self [class]Removed IntegerArithmeticType./(_: Self, _: Self) -> Self [class]Removed LazyBidirectionalCollection [struct]Removed LazyBidirectionalCollection.arrayRemoved LazyBidirectionalCollection.endIndexRemoved LazyBidirectionalCollection.filter(_: (S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazyBidirectionalCollection.firstRemoved LazyBidirectionalCollection.generate() -> S.GeneratorRemoved LazyBidirectionalCollection.init(_: S)Removed LazyBidirectionalCollection.isEmptyRemoved LazyBidirectionalCollection.lastRemoved LazyBidirectionalCollection.map(_: (S.Generator.Element) -> U) -> LazyBidirectionalCollection<MapCollectionView<S, U>>Removed LazyBidirectionalCollection.reverse() -> LazyBidirectionalCollection<BidirectionalReverseView<S>>Removed LazyBidirectionalCollection.startIndexRemoved LazyBidirectionalCollection.subscript() -> S.Generator.ElementRemoved LazyForwardCollection [struct]Removed LazyForwardCollection.arrayRemoved LazyForwardCollection.endIndexRemoved LazyForwardCollection.filter(_: (S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazyForwardCollection.firstRemoved LazyForwardCollection.generate() -> S.GeneratorRemoved LazyForwardCollection.init(_: S)Removed LazyForwardCollection.isEmptyRemoved LazyForwardCollection.map(_: (S.Generator.Element) -> U) -> LazyForwardCollection<MapCollectionView<S, U>>Removed LazyForwardCollection.startIndexRemoved LazyForwardCollection.subscript() -> S.Generator.ElementRemoved LazyRandomAccessCollection [struct]Removed LazyRandomAccessCollection.arrayRemoved LazyRandomAccessCollection.endIndexRemoved LazyRandomAccessCollection.filter(_: (S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazyRandomAccessCollection.firstRemoved LazyRandomAccessCollection.generate() -> S.GeneratorRemoved LazyRandomAccessCollection.init(_: S)Removed LazyRandomAccessCollection.isEmptyRemoved LazyRandomAccessCollection.lastRemoved LazyRandomAccessCollection.map(_: (S.Generator.Element) -> U) -> LazyRandomAccessCollection<MapCollectionView<S, U>>Removed LazyRandomAccessCollection.reverse() -> LazyBidirectionalCollection<RandomAccessReverseView<S>>Removed LazyRandomAccessCollection.startIndexRemoved LazyRandomAccessCollection.subscript() -> S.Generator.ElementRemoved LazySequence.arrayRemoved LazySequence.filter(_: (S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazySequence.generate() -> S.GeneratorRemoved LazySequence.map(_: (S.Generator.Element) -> U) -> LazySequence<MapSequenceView<S, U>>Removed ManagedBuffer.deinitRemoved ManagedBufferPointer.init(_: ManagedProtoBuffer<Value, Element>)Removed ManagedBufferPointer.init(_uncheckedUnsafeBufferObject: AnyObject)Removed ManagedBufferPointer.init(bufferClass: AnyClass, minimumCapacity: Int)Removed MapCollectionView [struct]Removed MapCollectionView.endIndexRemoved MapCollectionView.generate() -> MapSequenceGenerator<Base.Generator, T>Removed MapCollectionView.startIndexRemoved MapCollectionView.subscript() -> TRemoved MapSequenceGenerator [struct]Removed MapSequenceGenerator.generate() -> MapSequenceGenerator<Base, T>Removed MapSequenceGenerator.next() -> T?Removed MapSequenceView [struct]Removed MapSequenceView.generate() -> MapSequenceGenerator<Base.Generator, T>Removed MirrorDisposition [enum]Removed MirrorDisposition.AggregateRemoved MirrorDisposition.ClassRemoved MirrorDisposition.ContainerRemoved MirrorDisposition.EnumRemoved MirrorDisposition.IndexContainerRemoved MirrorDisposition.KeyContainerRemoved MirrorDisposition.MembershipContainerRemoved MirrorDisposition.ObjCObjectRemoved MirrorDisposition.OptionalRemoved MirrorDisposition.StructRemoved MirrorDisposition.TupleRemoved MirrorTypeRemoved MirrorType.countRemoved MirrorType.dispositionRemoved MirrorType.objectIdentifierRemoved MirrorType.quickLookObjectRemoved MirrorType.subscript() -> (String, MirrorType)Removed MirrorType.summaryRemoved MirrorType.valueRemoved MirrorType.valueTypeRemoved MutableCollectionType.subscript() -> Self.Generator.ElementRemoved MutableSliceable.subscript() -> Self.SubSliceRemoved ObjectIdentifier.valueRemoved Optional.flatMap(_: (T) -> U?) -> U?Removed Optional.getMirror() -> MirrorTypeRemoved Optional.map(_: (T) -> U) -> U?Removed PermutationGenerator.generate() -> PermutationGenerator<C, Indices>Removed PermutationGenerator.indicesRemoved PermutationGenerator.init(elements: C, indices: Indices)Removed PermutationGenerator.next() -> Element?Removed PermutationGenerator.seqRemoved PrintableRemoved Printable.descriptionRemoved QuickLookObject [enum]Removed QuickLookObject.AttributedStringRemoved QuickLookObject.BezierPathRemoved QuickLookObject.ColorRemoved QuickLookObject.DoubleRemoved QuickLookObject.FloatRemoved QuickLookObject.ImageRemoved QuickLookObject.IntRemoved QuickLookObject.LogicalRemoved QuickLookObject.PointRemoved QuickLookObject.RangeRemoved QuickLookObject.RectangleRemoved QuickLookObject.SizeRemoved QuickLookObject.SoundRemoved QuickLookObject.SpriteRemoved QuickLookObject.TextRemoved QuickLookObject.UIntRemoved QuickLookObject.URLRemoved QuickLookObject.ViewRemoved RandomAccessReverseView [struct]Removed RandomAccessReverseView.endIndexRemoved RandomAccessReverseView.generate() -> IndexingGenerator<RandomAccessReverseView<T>>Removed RandomAccessReverseView.startIndexRemoved RandomAccessReverseView.subscript() -> T.Generator.ElementRemoved Range.getMirror() -> MirrorTypeRemoved Range.isEmptyRemoved Range.map(_: (T) -> U) -> [U]Removed RangeGenerator.generate() -> RangeGenerator<T>Removed RangeReplaceableCollectionType.insert(_: Self.Generator.Element, atIndex: Self.Index)Removed RangeReplaceableCollectionType.removeAtIndex(_: Self.Index) -> Self.Generator.ElementRemoved RangeReplaceableCollectionType.removeRange(_: Range<Self.Index>)Removed RangeReplaceableCollectionType.replaceRange(_: Range<Self.Index>, with: C)Removed RangeReplaceableCollectionType.splice(_: S, atIndex: Self.Index)Removed RawOptionSetTypeRemoved RawOptionSetType.init(rawValue: RawValue)Removed ReflectableRemoved Reflectable.getMirror() -> MirrorTypeRemoved Repeat.generate() -> IndexingGenerator<Repeat<T>>Removed ReverseBidirectionalIndex [struct]Removed ReverseBidirectionalIndex.predecessor() -> ReverseBidirectionalIndex<I>Removed ReverseBidirectionalIndex.successor() -> ReverseBidirectionalIndex<I>Removed ReverseRandomAccessIndex.predecessor() -> ReverseRandomAccessIndex<I>Removed ReverseRandomAccessIndex.successor() -> ReverseRandomAccessIndex<I>Removed SequenceOf [struct]Removed SequenceOf.generate() -> GeneratorOf<T>Removed SequenceOf.init(_: S)Removed SequenceOf.init(_: () -> G)Removed SequenceType.generate() -> GeneratorRemoved Set.getMirror() -> MirrorTypeRemoved Set.makeDescription(isDebug: Bool) -> StringRemoved Set.removeAtIndex(_: SetIndex<T>)Removed SetGeneratorRepresentation [enum]Removed SetIndexRepresentation [enum]Removed SetMirrorRemoved SetMirror.countRemoved SetMirror.dispositionRemoved SetMirror.init(_: Set<T>)Removed SetMirror.objectIdentifierRemoved SetMirror.quickLookObjectRemoved SetMirror.subscript() -> (String, MirrorType)Removed SetMirror.summaryRemoved SetMirror.valueRemoved SetMirror.valueTypeRemoved SetMirrorPosition [struct]Removed SetMirrorPosition.init(_: Set<T>)Removed SetMirrorPosition.SetPosRemoved SetMirrorPosition.successor()Removed SignedNumberType.-(_: Self) -> Self [class]Removed SinkOf [struct]Removed SinkOf.init(_: S)Removed SinkOf.init(_: (T) -> ())Removed SinkOf.put(_: T)Removed SinkTypeRemoved SinkType.put(_: Element)Removed SliceableRemoved Sliceable.subscript() -> SubSliceRemoved StaticString.init(start: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Removed StaticString.init(unicodeScalar: Builtin.Int32)Removed Strideable.advancedBy(_: Stride) -> SelfRemoved Strideable.distanceTo(_: Self) -> StrideRemoved StrideThrough.endRemoved StrideThrough.getMirror() -> MirrorTypeRemoved StrideThrough.init(start: T, end: T, stride: T.Stride)Removed StrideThrough.startRemoved StrideThrough.strideRemoved StrideThroughGenerator.currentRemoved StrideThroughGenerator.doneRemoved StrideThroughGenerator.endRemoved StrideThroughGenerator.strideRemoved StrideTo.endRemoved StrideTo.getMirror() -> MirrorTypeRemoved StrideTo.init(start: T, end: T, stride: T.Stride)Removed StrideTo.startRemoved StrideTo.strideRemoved StrideToGenerator.currentRemoved StrideToGenerator.endRemoved StrideToGenerator.strideRemoved String.extend(_: S)Removed String.extend(_: String)Removed String.generate() -> IndexingGenerator<String>Removed String.getMirror() -> MirrorTypeRemoved String.init(_: T)Removed String.init(_: T, radix: Int, uppercase: Bool)Removed String.insert(_: Character, atIndex: String.Index)Removed String.join(_: S) -> StringRemoved String.removeAtIndex(_: String.Index) -> CharacterRemoved String.removeRange(_: Range<String.Index>)Removed String.replaceRange(_: Range<String.Index>, with: C)Removed String.splice(_: S, atIndex: String.Index)Removed String.subscript() -> CharacterRemoved String.subscript() -> StringRemoved String.toInt() -> Int?Removed String.withCString(_: UnsafePointer<Int8> -> Result) -> ResultRemoved String.Index [struct]Removed String.Index.getMirror() -> MirrorTypeRemoved String.Index.predecessor() -> String.IndexRemoved String.Index.successor() -> String.IndexRemoved String.UnicodeScalarView.getMirror() -> MirrorTypeRemoved String.UTF16View.generate() -> GeneratorRemoved String.UTF16View.getMirror() -> MirrorTypeRemoved String.UTF8View.generate() -> IndexingGenerator<String.UTF8View>Removed String.UTF8View.getMirror() -> MirrorTypeRemoved UInt.encode() -> [Word]Removed UInt.getMirror() -> MirrorTypeRemoved UInt16.encode() -> [Word]Removed UInt16.getMirror() -> MirrorTypeRemoved UInt32.encode() -> [Word]Removed UInt32.getMirror() -> MirrorTypeRemoved UInt64.encode() -> [Word]Removed UInt64.getMirror() -> MirrorTypeRemoved UInt8.encode() -> [Word]Removed UInt8.getMirror() -> MirrorTypeRemoved UnicodeCodecType.encode(_: UnicodeScalar, output: S) [class]Removed UnicodeScalar.getMirror() -> MirrorTypeRemoved UnicodeScalar.init(_: Builtin.Int32)Removed UnicodeScalar.utf16Removed UnicodeScalar.UTF16View [struct]Removed UnicodeScalar.UTF16View.valueRemoved UnicodeScalarIndex.init(_: String.Index, within: String.UnicodeScalarView)Removed UnicodeScalarIndex.samePositionIn(_: String) -> String.Index?Removed UnicodeScalarView.extend(_: S)Removed UnicodeScalarView.insert(_: UnicodeScalar, atIndex: String.UnicodeScalarView.Index)Removed UnicodeScalarView.removeAll(keepCapacity: Bool)Removed UnicodeScalarView.removeAtIndex(_: String.UnicodeScalarView.Index) -> UnicodeScalarRemoved UnicodeScalarView.removeRange(_: Range<String.UnicodeScalarView.Index>)Removed UnicodeScalarView.replaceRange(_: Range<String.UnicodeScalarView.Index>, with: C)Removed UnicodeScalarView.splice(_: S, atIndex: String.UnicodeScalarView.Index)Removed UnsafeBufferPointerGenerator.endRemoved UnsafeBufferPointerGenerator.generate() -> UnsafeBufferPointerGenerator<T>Removed UnsafeBufferPointerGenerator.positionRemoved UnsafeMutablePointer.encode() -> [Word]Removed UnsafeMutablePointer.getMirror() -> MirrorTypeRemoved UnsafeMutablePointer.initializeFrom(_: C)Removed UnsafeMutablePointer.put(_: T)Removed UnsafePointer.encode() -> [Word]Removed UnsafePointer.getMirror() -> MirrorTypeRemoved UTF16.encode(_: UnicodeScalar, output: S) [static]Removed UTF16View.endIndexRemoved UTF16View.generate() -> IndexingGenerator<UnicodeScalar.UTF16View>Removed UTF16View.startIndexRemoved UTF16View.subscript() -> CodeUnitRemoved UTF32.encode(_: UnicodeScalar, output: S) [static]Removed UTF8.encode(_: UnicodeScalar, output: S) [static]Removed VaListBuilder.append(_: CVarArgType)Removed VaListBuilder.storageRemoved VaListBuilder.va_list() -> CVaListPointerRemoved Zip2 [struct]Removed Zip2.generate() -> GeneratorRemoved Zip2.init(_: S0, _: S1)Removed Zip2.sequencesRemoved ZipGenerator2 [struct]Removed ZipGenerator2.baseStreamsRemoved ZipGenerator2.init(_: E0, _: E1)Removed ZipGenerator2.next() -> Element?Removed !=(_: Builtin.NativeObject, _: Builtin.NativeObject) -> BoolRemoved !=(_: _UnitTestArray<T>, _: _UnitTestArray<T>) -> BoolRemoved !=(_: Builtin.RawPointer, _: Builtin.RawPointer) -> BoolRemoved !==(_: _UnitTestArrayBuffer<T>, _: _UnitTestArrayBuffer<T>) -> BoolRemoved &&(_: T, _: () -> U) -> BoolRemoved &&(_: T, _: () -> Bool) -> BoolRemoved &(_: T, _: T) -> TRemoved +(_: C, _: S) -> CRemoved +(_: T.Stride, _: T) -> TRemoved +(_: C, _: S) -> CRemoved +(_: EC1, _: EC2) -> EC1Removed +(_: S, _: C) -> CRemoved +(_: T, _: T.Stride) -> TRemoved ++(_: T) -> TRemoved ++(_: T) -> TRemoved +=(_: _UnitTestArrayBuffer<T>, _: C)Removed +=(_: _UnitTestArray<T>, _: S)Removed +=(_: _UnitTestArrayBuffer<T>, _: T)Removed +=(_: ContiguousArray<T>, _: C)Removed +=(_: ArraySlice<T>, _: C)Removed +=(_: T, _: T.Stride)Removed +=(_: [T], _: C)Removed +=(_: _ContiguousArrayBuffer<T>, _: C)Removed +=(_: _UnitTestArray<T>, _: C)Removed -(_: T, _: T.Stride) -> TRemoved -(_: T, _: T) -> T.StrideRemoved --(_: T) -> TRemoved --(_: T) -> TRemoved -=(_: T, _: T.Stride)Removed ...(_: Pos, _: Pos) -> Range<Pos>Removed ...(_: Pos, _: Pos) -> Range<Pos>Removed ..<(_: Pos, _: Pos) -> Range<Pos>Removed ..<(_: Pos, _: Pos) -> Range<Pos>Removed <(_: SetMirrorPosition<T>, _: Int) -> BoolRemoved <(_: _NativeDictionaryIndex<Key, Value>, _: _NativeDictionaryIndex<Key, Value>) -> BoolRemoved <(_: DictionaryMirrorPosition<Key, Value>, _: Int) -> BoolRemoved <(_: _CocoaDictionaryIndex, _: _CocoaDictionaryIndex) -> BoolRemoved <(_: _NativeSetIndex<T>, _: _NativeSetIndex<T>) -> BoolRemoved <(_: String.Index, _: String.Index) -> BoolRemoved <(_: _CocoaSetIndex, _: _CocoaSetIndex) -> BoolRemoved ==(_: _CocoaSetIndex, _: _CocoaSetIndex) -> BoolRemoved ==(_: DictionaryMirrorPosition<Key, Value>, _: Int) -> BoolRemoved ==(_: Builtin.NativeObject, _: Builtin.NativeObject) -> BoolRemoved ==(_: CFunctionPointer<T>, _: CFunctionPointer<T>) -> BoolRemoved ==(_: ReverseRandomAccessIndex<I>, _: ReverseRandomAccessIndex<I>) -> BoolRemoved ==(_: _NativeSetIndex<T>, _: _NativeSetIndex<T>) -> BoolRemoved ==(_: Builtin.RawPointer, _: Builtin.RawPointer) -> BoolRemoved ==(_: String.Index, _: String.Index) -> BoolRemoved ==(_: _ConcatenateBidirectionalIndex<I>, _: _ConcatenateBidirectionalIndex<I>) -> BoolRemoved ==(_: _HeapBuffer<Value, Element>, _: _HeapBuffer<Value, Element>) -> BoolRemoved ==(_: T, _: T) -> BoolRemoved ==(_: SetMirrorPosition<T>, _: Int) -> BoolRemoved ==(_: _UnitTestArray<T>, _: _UnitTestArray<T>) -> BoolRemoved ==(_: _ConcatenateForwardIndex<I>, _: _ConcatenateForwardIndex<I>) -> BoolRemoved ==(_: _CocoaDictionaryIndex, _: _CocoaDictionaryIndex) -> BoolRemoved ==(_: T, _: T) -> BoolRemoved ==(_: ReverseBidirectionalIndex<I>, _: ReverseBidirectionalIndex<I>) -> BoolRemoved ==(_: _NativeDictionaryIndex<Key, Value>, _: _NativeDictionaryIndex<Key, Value>) -> BoolRemoved ==(_: FilterCollectionViewIndex<Base>, _: FilterCollectionViewIndex<Base>) -> BoolRemoved ===(_: _UnitTestArrayBuffer<T>, _: _UnitTestArrayBuffer<T>) -> BoolRemoved >(_: DictionaryMirrorPosition<Key, Value>, _: Int) -> BoolRemoved >(_: SetMirrorPosition<T>, _: Int) -> BoolRemoved ??(_: T?, _: () -> T) -> TRemoved ??(_: T?, _: () -> T?) -> T?Removed ^(_: T, _: T) -> TRemoved advance(_: T, _: T.Distance) -> TRemoved advance(_: T, _: T.Distance, _: T) -> TRemoved Array.ElementRemoved Array.SubSliceRemoved ArraySlice.ElementRemoved ArraySlice.SubSliceRemoved BidirectionalReverseView.GeneratorRemoved BidirectionalReverseView.IndexRemoved Character.UTF16ViewRemoved CharacterLiteralConvertible.CharacterLiteralTypeRemoved ClosedInterval.BoundRemoved CollectionType.IndexRemoved contains(_: S, _: (S.Generator.Element) -> L) -> BoolRemoved contains(_: S, _: S.Generator.Element) -> BoolRemoved ContiguousArray.ElementRemoved ContiguousArray.SubSliceRemoved count(_: T) -> T.Index.DistanceRemoved debugPrint(_: T)Removed debugPrint(_: T, _: TargetStream)Removed debugPrintln(_: T)Removed debugPrintln(_: T, _: TargetStream)Removed DictionaryIndex.IndexRemoved DictionaryMirror.MirroredTypeRemoved DictionaryMirrorPosition.MirroredTypeRemoved distance(_: T, _: T) -> T.DistanceRemoved dropFirst(_: Seq) -> Seq.SubSliceRemoved dropLast(_: S) -> S.SubSliceRemoved enumerate(_: Seq) -> EnumerateSequence<Seq>Removed EnumerateGenerator.GeneratorRemoved equal(_: S1, _: S2) -> BoolRemoved equal(_: S1, _: S2, _: (S1.Generator.Element, S1.Generator.Element) -> Bool) -> BoolRemoved extend(_: C, _: S)Removed filter(_: S, _: (S.Generator.Element) -> Bool) -> [S.Generator.Element]Removed FilterCollectionView.IndexRemoved find(_: C, _: C.Generator.Element) -> C.Index?Removed first(_: C) -> C.Generator.Element?Removed flatMap(_: T?, _: (T) -> U?) -> U?Removed flatMap(_: S, _: (S.Generator.Element) -> [T]) -> [T]Removed flatMap(_: C, _: (C.Generator.Element) -> [T]) -> [T]Removed HalfOpenInterval.BoundRemoved indices(_: C) -> Range<C.Index>Removed insert(_: C, _: C.Generator.Element, atIndex: C.Index)Removed isEmpty(_: C) -> BoolRemoved isUniquelyReferencedOrPinnedNonObjC(_: T) -> BoolRemoved join(_: C, _: S) -> CRemoved kCFStringEncodingASCIIRemoved last(_: C) -> C.Generator.Element?Removed lazy(_: S) -> LazyRandomAccessCollection<S>Removed lazy(_: S) -> LazySequence<S>Removed lazy(_: S) -> LazyForwardCollection<S>Removed lazy(_: S) -> LazyBidirectionalCollection<S>Removed lexicographicalCompare(_: S1, _: S2) -> BoolRemoved lexicographicalCompare(_: S1, _: S2, isOrderedBefore: (S1.Generator.Element, S1.Generator.Element) -> Bool) -> BoolRemoved map(_: C, _: (C.Generator.Element) -> T) -> [T]Removed map(_: S, _: (S.Generator.Element) -> T) -> [T]Removed map(_: T?, _: (T) -> U) -> U?Removed maxElement(_: R) -> R.Generator.ElementRemoved minElement(_: R) -> R.Generator.ElementRemoved numericCast(_: T) -> URemoved numericCast(_: T) -> URemoved numericCast(_: T) -> URemoved overlaps(_: I0, _: I1) -> BoolRemoved partition(_: C, _: Range<C.Index>) -> C.IndexRemoved partition(_: C, _: Range<C.Index>, _: (C.Generator.Element, C.Generator.Element) -> Bool) -> C.IndexRemoved PermutationGenerator.GeneratorRemoved prefix(_: S, _: Int) -> S.SubSliceRemoved print(_: T)Removed print(_: T, _: TargetStream)Removed println()Removed println(_: T)Removed println(_: T, _: TargetStream)Removed RandomAccessReverseView.GeneratorRemoved RandomAccessReverseView.IndexRemoved Range.ArraySliceRemoved Range.GeneratorRemoved Range.IndexRemoved RangeGenerator.ElementRemoved RangeGenerator.GeneratorRemoved RawOptionSetType.RawValueRemoved reduce(_: S, _: U, _: (U, S.Generator.Element) -> U) -> URemoved reflect(_: T) -> MirrorTypeRemoved removeAll(_: C, keepCapacity: Bool)Removed removeAtIndex(_: C, _: C.Index) -> C.Generator.ElementRemoved removeLast(_: C) -> C.Generator.ElementRemoved removeRange(_: C, _: Range<C.Index>)Removed reverse(_: C) -> [C.Generator.Element]Removed ReverseBidirectionalIndex.DistanceRemoved SequenceType.GeneratorRemoved Set.ElementRemoved Set.GeneratorTypeRemoved SetIndex.IndexRemoved SetIndex.KeyRemoved SetIndex.ValueRemoved SetMirror.MirroredTypeRemoved SetMirrorPosition.MirroredTypeRemoved SinkType.ElementRemoved Sliceable.SubSliceRemoved sort(_: ContiguousArray<T>)Removed sort(_: C)Removed sort(_: [T])Removed sort(_: ContiguousArray<T>, _: (T, T) -> Bool)Removed sort(_: [T], _: (T, T) -> Bool)Removed sort(_: C, _: (C.Generator.Element, C.Generator.Element) -> Bool)Removed sorted(_: C) -> [C.Generator.Element]Removed sorted(_: C, _: (C.Generator.Element, C.Generator.Element) -> Bool) -> [C.Generator.Element]Removed splice(_: C, _: S, atIndex: C.Index)Removed split(_: S, maxSplit: Int, allowEmptySlices: Bool, isSeparator: (S.Generator.Element) -> R) -> [S.SubSlice]Removed startsWith(_: S0, _: S1) -> BoolRemoved startsWith(_: S0, _: S1, _: (S0.Generator.Element, S0.Generator.Element) -> Bool) -> BoolRemoved stride(from: T, through: T, by: T.Stride) -> StrideThrough<T>Removed stride(from: T, to: T, by: T.Stride) -> StrideTo<T>Removed String.UTF16View.GeneratorRemoved String.UTF8View.Index.BufferRemoved suffix(_: S, _: Int) -> S.SubSliceRemoved toDebugString(_: T) -> StringRemoved toString(_: T) -> StringRemoved transcode(_: InputEncoding.Type, _: OutputEncoding.Type, _: Input, _: Output, stopOnError: Bool) -> BoolRemoved underestimateCount(_: T) -> IntRemoved unsafeReflect(_: Builtin.NativeObject, _: UnsafeMutablePointer<T>) -> MirrorTypeRemoved UWordRemoved withExtendedLifetime(_: T, _: () -> Result) -> ResultRemoved withExtendedLifetime(_: T, _: T -> Result) -> ResultRemoved withUnsafeMutablePointer(_: T, _: UnsafeMutablePointer<T> -> Result) -> ResultRemoved withUnsafeMutablePointers(_: A0, _: A1, _: (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>) -> Result) -> ResultRemoved withUnsafeMutablePointers(_: A0, _: A1, _: A2, _: (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>, UnsafeMutablePointer<A2>) -> Result) -> ResultRemoved withUnsafePointer(_: T, _: UnsafePointer<T> -> Result) -> ResultRemoved withUnsafePointers(_: A0, _: A1, _: (UnsafePointer<A0>, UnsafePointer<A1>) -> Result) -> ResultRemoved withUnsafePointers(_: A0, _: A1, _: A2, _: (UnsafePointer<A0>, UnsafePointer<A1>, UnsafePointer<A2>) -> Result) -> ResultRemoved WordRemoved zip(_: S0, _: S1) -> Zip2<S0, S1>Removed Zip2.GeneratorRemoved Zip2.Stream1Removed Zip2.Stream2Removed ZipGenerator2.ElementRemoved |(_: T, _: T) -> TRemoved ||(_: T, _: () -> U) -> BoolRemoved ||(_: T, _: () -> Bool) -> BoolRemoved ~(_: T) -> TAdded _IncrementableAdded _Incrementable.successor() -> SelfAdded AnyBidirectionalCollection [struct]Added AnyBidirectionalCollection.countAdded AnyBidirectionalCollection.endIndexAdded AnyBidirectionalCollection.generate() -> AnyGenerator<Element>Added AnyBidirectionalCollection.init<C : CollectionType where C.Index : BidirectionalIndexType, C.Generator.Element == Element>(_: C)Added AnyBidirectionalCollection.init(_: AnyRandomAccessCollection<Element>)Added AnyBidirectionalCollection.init(_: AnyBidirectionalCollection<Element>)Added AnyBidirectionalCollection.init<C : CollectionType where C.Index : RandomAccessIndexType, C.Generator.Element == Element>(_: C)Added AnyBidirectionalCollection.init(_: AnyForwardCollection<Element>)Added AnyBidirectionalCollection.startIndexAdded AnyBidirectionalCollection.subscript(_: AnyBidirectionalIndex) -> ElementAdded AnyBidirectionalCollection.underestimateCount() -> IntAdded AnyBidirectionalIndex [struct]Added AnyBidirectionalIndex.init<BaseIndex : BidirectionalIndexType>(_: BaseIndex)Added AnyBidirectionalIndex.predecessor() -> AnyBidirectionalIndexAdded AnyBidirectionalIndex.successor() -> AnyBidirectionalIndexAdded AnyCollectionTypeAdded AnyForwardCollection [struct]Added AnyForwardCollection.countAdded AnyForwardCollection.endIndexAdded AnyForwardCollection.generate() -> AnyGenerator<Element>Added AnyForwardCollection.init<C : CollectionType where C.Index : ForwardIndexType, C.Generator.Element == Element>(_: C)Added AnyForwardCollection.init(_: AnyForwardCollection<Element>)Added AnyForwardCollection.init<C : CollectionType where C.Index : BidirectionalIndexType, C.Generator.Element == Element>(_: C)Added AnyForwardCollection.init<C : CollectionType where C.Index : RandomAccessIndexType, C.Generator.Element == Element>(_: C)Added AnyForwardCollection.init(_: AnyRandomAccessCollection<Element>)Added AnyForwardCollection.init(_: AnyBidirectionalCollection<Element>)Added AnyForwardCollection.startIndexAdded AnyForwardCollection.subscript(_: AnyForwardIndex) -> ElementAdded AnyForwardCollection.underestimateCount() -> IntAdded AnyForwardIndex [struct]Added AnyForwardIndex.init<BaseIndex : ForwardIndexType>(_: BaseIndex)Added AnyForwardIndex.successor() -> AnyForwardIndexAdded AnyGeneratorAdded AnyGenerator.init()Added AnyGenerator.next() -> Element?Added AnyRandomAccessCollection [struct]Added AnyRandomAccessCollection.countAdded AnyRandomAccessCollection.endIndexAdded AnyRandomAccessCollection.generate() -> AnyGenerator<Element>Added AnyRandomAccessCollection.init(_: AnyForwardCollection<Element>)Added AnyRandomAccessCollection.init<C : CollectionType where C.Index : RandomAccessIndexType, C.Generator.Element == Element>(_: C)Added AnyRandomAccessCollection.init(_: AnyRandomAccessCollection<Element>)Added AnyRandomAccessCollection.init(_: AnyBidirectionalCollection<Element>)Added AnyRandomAccessCollection.startIndexAdded AnyRandomAccessCollection.subscript(_: AnyRandomAccessIndex) -> ElementAdded AnyRandomAccessCollection.underestimateCount() -> IntAdded AnyRandomAccessIndex [struct]Added AnyRandomAccessIndex.advancedBy(_: Distance) -> AnyRandomAccessIndexAdded AnyRandomAccessIndex.advancedBy(_: Distance, limit: AnyRandomAccessIndex) -> AnyRandomAccessIndexAdded AnyRandomAccessIndex.distanceTo(_: AnyRandomAccessIndex) -> DistanceAdded AnyRandomAccessIndex.init<BaseIndex : RandomAccessIndexType>(_: BaseIndex)Added AnyRandomAccessIndex.predecessor() -> AnyRandomAccessIndexAdded AnyRandomAccessIndex.successor() -> AnyRandomAccessIndexAdded AnySequence [struct]Added AnySequence.generate() -> AnyGenerator<Element>Added AnySequence.init<G : GeneratorType where G.Element == Element>(_: () -> G)Added AnySequence.init<S : SequenceType where S.Generator.Element == Element>(_: S)Added AnySequence.underestimateCount() -> IntAdded Array.appendContentsOf<C : CollectionType where C.Generator.Element == Element>(_: C)Added Array.appendContentsOf<S : SequenceType where S.Generator.Element == Element>(_: S)Added Array.popLast() -> Element?Added Array.replaceRange<C : CollectionType where C.Generator.Element == _Buffer.Element>(_: Range<Int>, with: C)Added Array.withUnsafeBufferPointer<R>(_: (UnsafeBufferPointer<Element>) throws -> R) rethrows -> RAdded Array.withUnsafeMutableBufferPointer<R>(_: (inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> RAdded ArraySlice.appendContentsOf<S : SequenceType where S.Generator.Element == Element>(_: S)Added ArraySlice.appendContentsOf<C : CollectionType where C.Generator.Element == Element>(_: C)Added ArraySlice.replaceRange<C : CollectionType where C.Generator.Element == _Buffer.Element>(_: Range<Int>, with: C)Added ArraySlice.withUnsafeBufferPointer<R>(_: (UnsafeBufferPointer<Element>) throws -> R) rethrows -> RAdded ArraySlice.withUnsafeMutableBufferPointer<R>(_: (inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> RAdded BidirectionalIndexType.advancedBy(_: Self.Distance) -> SelfAdded BidirectionalIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded BidirectionalIndexType.predecessor() -> SelfAdded BidirectionalIndexType.successor() -> SelfAdded BitwiseOperationsType.&(_: Self, _: Self) -> SelfAdded BitwiseOperationsType.^(_: Self, _: Self) -> SelfAdded BitwiseOperationsType.|(_: Self, _: Self) -> SelfAdded BitwiseOperationsType.~(_: Self) -> SelfAdded CollectionOfOne.countAdded CollectionType.countAdded CollectionType.dropFirst(_: Int) -> Self.SubSequenceAdded CollectionType.dropLast(_: Int) -> Self.SubSequenceAdded CollectionType.endIndexAdded CollectionType.filter(_: (Self.Base.Generator.Element) -> Bool) -> [Self.Base.Generator.Element]Added CollectionType.firstAdded CollectionType.flatten() -> FlattenCollection<Self>Added CollectionType.flatten() -> FlattenBidirectionalCollection<Self>Added CollectionType.generate() -> Self.GeneratorAdded CollectionType.generate() -> IndexingGenerator<Self>Added CollectionType.indexOf(_: Self.Generator.Element) -> Self.Index?Added CollectionType.indexOf(_: (Self.Generator.Element) throws -> Bool) rethrows -> Self.Index?Added CollectionType.indicesAdded CollectionType.isEmptyAdded CollectionType.lastAdded CollectionType.lazyAdded CollectionType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Added CollectionType.map<T>(_: (Self.Base.Generator.Element) -> T) -> [T]Added CollectionType.popFirst() -> Self.Generator.Element?Added CollectionType.popLast() -> Self.Generator.Element?Added CollectionType.prefix(_: Int) -> Self.SubSequenceAdded CollectionType.prefixThrough(_: Self.Index) -> Self.SubSequenceAdded CollectionType.prefixUpTo(_: Self.Index) -> Self.SubSequenceAdded CollectionType.removeFirst() -> Self.Generator.ElementAdded CollectionType.reverse() -> ReverseRandomAccessCollection<Self>Added CollectionType.reverse() -> ReverseCollection<Self>Added CollectionType.split(_: Int, allowEmptySlices: Bool, isSeparator: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.SubSequence]Added CollectionType.split(_: Self.Generator.Element, maxSplit: Int, allowEmptySlices: Bool) -> [Self.SubSequence]Added CollectionType.startIndexAdded CollectionType.subscript(_: Self.Index) -> Self.Generator.ElementAdded CollectionType.subscript(_: Self.Index) -> Self.Base.Generator.ElementAdded CollectionType.subscript(_: Range<Self.Index>) -> Slice<Self>Added CollectionType.subscript(_: Range<Self.Index>) -> Self.SubSequenceAdded CollectionType.suffix(_: Int) -> Self.SubSequenceAdded CollectionType.suffixFrom(_: Self.Index) -> Self.SubSequenceAdded CollectionType.underestimateCount() -> IntAdded Comparable.<(_: Self, _: Self) -> BoolAdded Comparable.<=(_: Self, _: Self) -> BoolAdded Comparable.>(_: Self, _: Self) -> BoolAdded Comparable.>=(_: Self, _: Self) -> BoolAdded ContiguousArray.appendContentsOf<S : SequenceType where S.Generator.Element == Element>(_: S)Added ContiguousArray.appendContentsOf<C : CollectionType where C.Generator.Element == Element>(_: C)Added ContiguousArray.popLast() -> Element?Added ContiguousArray.replaceRange<C : CollectionType where C.Generator.Element == _Buffer.Element>(_: Range<Int>, with: C)Added ContiguousArray.withUnsafeBufferPointer<R>(_: (UnsafeBufferPointer<Element>) throws -> R) rethrows -> RAdded ContiguousArray.withUnsafeMutableBufferPointer<R>(_: (inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> RAdded CustomDebugStringConvertibleAdded CustomDebugStringConvertible.debugDescriptionAdded CustomLeafReflectableAdded CustomPlaygroundQuickLookableAdded CustomPlaygroundQuickLookable.customPlaygroundQuickLook() -> PlaygroundQuickLookAdded CustomReflectableAdded CustomReflectable.customMirror() -> MirrorAdded CustomStringConvertibleAdded CustomStringConvertible.descriptionAdded Dictionary.keysAdded Dictionary.popFirst() -> (Key, Value)?Added Dictionary.removeAtIndex(_: DictionaryIndex<Key, Value>) -> (Key, Value)Added Dictionary.valuesAdded DictionaryLiteral [struct]Added DictionaryLiteral.endIndexAdded DictionaryLiteral.init(dictionaryLiteral: (Key, Value))Added DictionaryLiteral.startIndexAdded DictionaryLiteral.subscript(_: Int) -> (Key, Value)Added Double.init(_: String)Added EmptyCollection.countAdded Equatable.==(_: Self, _: Self) -> BoolAdded ErrorTypeAdded FlattenBidirectionalCollection [struct]Added FlattenBidirectionalCollection.endIndexAdded FlattenBidirectionalCollection.generate() -> FlattenGenerator<Base.Generator>Added FlattenBidirectionalCollection.init(_: Base)Added FlattenBidirectionalCollection.startIndexAdded FlattenBidirectionalCollection.subscript(_: FlattenBidirectionalCollectionIndex<Base>) -> Base.Generator.Element.Generator.ElementAdded FlattenBidirectionalCollection.underestimateCount() -> IntAdded FlattenBidirectionalCollectionIndex [struct]Added FlattenBidirectionalCollectionIndex.predecessor() -> FlattenBidirectionalCollectionIndex<BaseElements>Added FlattenBidirectionalCollectionIndex.successor() -> FlattenBidirectionalCollectionIndex<BaseElements>Added FlattenCollection [struct]Added FlattenCollection.endIndexAdded FlattenCollection.generate() -> FlattenGenerator<Base.Generator>Added FlattenCollection.init(_: Base)Added FlattenCollection.startIndexAdded FlattenCollection.subscript(_: FlattenCollectionIndex<Base>) -> Base.Generator.Element.Generator.ElementAdded FlattenCollection.underestimateCount() -> IntAdded FlattenCollectionIndex [struct]Added FlattenCollectionIndex.successor() -> FlattenCollectionIndex<BaseElements>Added FlattenGenerator [struct]Added FlattenGenerator.init(_: Base)Added FlattenGenerator.next() -> Base.Element.Generator.Element?Added FlattenSequence [struct]Added FlattenSequence.generate() -> FlattenGenerator<Base.Generator>Added FlattenSequence.init(_: Base)Added Float.init(_: String)Added ForwardIndexType.advancedBy(_: Self.Distance) -> SelfAdded ForwardIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded ForwardIndexType.distanceTo(_: Self) -> Self.DistanceAdded ImplicitlyUnwrappedOptional.flatMap<U>(_: (Wrapped) throws -> U!) rethrows -> U!Added ImplicitlyUnwrappedOptional.map<U>(_: (Wrapped) throws -> U) rethrows -> U!Added IndexableAdded Indexable.endIndexAdded Indexable.startIndexAdded Indexable.subscript(_: Self.Index) -> Self._ElementAdded IndexingGenerator.init(_: Elements)Added IndexingGenerator.next() -> Elements._Element?Added Int.init(_: String, radix: Int)Added Int16.init(_: String, radix: Int)Added Int32.init(_: String, radix: Int)Added Int64.init(_: String, radix: Int)Added Int8.init(_: String, radix: Int)Added IntegerArithmeticType.%(_: Self, _: Self) -> SelfAdded IntegerArithmeticType.\*(_: Self, _: Self) -> SelfAdded IntegerArithmeticType.+(_: Self, _: Self) -> SelfAdded IntegerArithmeticType.-(_: Self, _: Self) -> SelfAdded IntegerArithmeticType./(_: Self, _: Self) -> SelfAdded IntervalType.overlaps<I : IntervalType where I.Bound == Bound>(_: I) -> BoolAdded JoinGenerator [struct]Added JoinGenerator.init<Separator : SequenceType where Separator.Generator.Element == Base.Element.Generator.Element>(base: Base, separator: Separator)Added JoinGenerator.next() -> Base.Element.Generator.Element?Added JoinSequence [struct]Added JoinSequence.generate() -> JoinGenerator<Base.Generator>Added JoinSequence.init<Separator : SequenceType where Separator.Generator.Element == Base.Generator.Element.Generator.Element>(base: Base, separator: Separator)Added LazyCollection [struct]Added LazyCollection.countAdded LazyCollection.elementsAdded LazyCollection.endIndexAdded LazyCollection.firstAdded LazyCollection.generate() -> Base.GeneratorAdded LazyCollection.init(_: Base)Added LazyCollection.isEmptyAdded LazyCollection.startIndexAdded LazyCollection.subscript(_: Range<Base.Index>) -> LazyCollection<Slice<Base>>Added LazyCollection.subscript(_: Base.Index) -> Base.Generator.ElementAdded LazyCollection.underestimateCount() -> IntAdded LazyCollectionTypeAdded LazyCollectionType.elementsAdded LazyCollectionType.filter(_: (Self.Elements.Generator.Element) -> Bool) -> LazyFilterCollection<Self.Elements>Added LazyCollectionType.flatMap<Intermediate : CollectionType where Intermediate.Index : BidirectionalIndexType>(_: (Self.Elements.Generator.Element) -> Intermediate) -> LazyCollection<FlattenBidirectionalCollection<LazyMapCollection<Self.Elements, Intermediate>>>Added LazyCollectionType.flatMap<Intermediate : CollectionType>(_: (Self.Elements.Generator.Element) -> Intermediate) -> LazyCollection<FlattenCollection<LazyMapCollection<Self.Elements, Intermediate>>>Added LazyCollectionType.flatten() -> LazyCollection<FlattenBidirectionalCollection<Self.Elements>>Added LazyCollectionType.flatten() -> LazyCollection<FlattenCollection<Self.Elements>>Added LazyCollectionType.lazyAdded LazyCollectionType.map<U>(_: (Self.Elements.Generator.Element) -> U) -> LazyMapCollection<Self.Elements, U>Added LazyCollectionType.reverse() -> LazyCollection<ReverseCollection<Self.Elements>>Added LazyCollectionType.reverse() -> LazyCollection<ReverseRandomAccessCollection<Self.Elements>>Added LazyFilterCollection [struct]Added LazyFilterCollection.endIndexAdded LazyFilterCollection.generate() -> LazyFilterGenerator<Base.Generator>Added LazyFilterCollection.init(_: Base, whereElementsSatisfy: (Base.Generator.Element) -> Bool)Added LazyFilterCollection.startIndexAdded LazyFilterCollection.subscript(_: LazyFilterIndex<Base>) -> Base.Generator.ElementAdded LazyFilterGenerator [struct]Added LazyFilterGenerator.baseAdded LazyFilterGenerator.init(_: Base, whereElementsSatisfy: (Base.Element) -> Bool)Added LazyFilterGenerator.next() -> Base.Element?Added LazyFilterIndex [struct]Added LazyFilterIndex.baseAdded LazyFilterIndex.successor() -> LazyFilterIndex<BaseElements>Added LazyFilterSequence [struct]Added LazyFilterSequence.baseAdded LazyFilterSequence.generate() -> LazyFilterGenerator<Base.Generator>Added LazyFilterSequence.init(_: Base, whereElementsSatisfy: (Base.Generator.Element) -> Bool)Added LazyMapCollection [struct]Added LazyMapCollection.countAdded LazyMapCollection.endIndexAdded LazyMapCollection.firstAdded LazyMapCollection.generate() -> LazyMapGenerator<Base.Generator, Element>Added LazyMapCollection.init(_: Base, transform: (Base.Generator.Element) -> Element)Added LazyMapCollection.isEmptyAdded LazyMapCollection.startIndexAdded LazyMapCollection.subscript(_: Base.Index) -> ElementAdded LazyMapCollection.underestimateCount() -> IntAdded LazyMapGenerator [struct]Added LazyMapGenerator.baseAdded LazyMapGenerator.next() -> Element?Added LazyMapSequence [struct]Added LazyMapSequence.generate() -> LazyMapGenerator<Base.Generator, Element>Added LazyMapSequence.init(_: Base, transform: (Base.Generator.Element) -> Element)Added LazyMapSequence.underestimateCount() -> IntAdded LazySequence.elementsAdded LazySequenceTypeAdded LazySequenceType.arrayAdded LazySequenceType.elementsAdded LazySequenceType.elementsAdded LazySequenceType.filter(_: (Self.Elements.Generator.Element) -> Bool) -> LazyFilterSequence<Self.Elements>Added LazySequenceType.flatMap<Intermediate : SequenceType>(_: (Self.Elements.Generator.Element) -> Intermediate) -> LazySequence<FlattenSequence<LazyMapSequence<Self.Elements, Intermediate>>>Added LazySequenceType.flatten() -> LazySequence<FlattenSequence<Self.Elements>>Added LazySequenceType.lazyAdded LazySequenceType.map<U>(_: (Self.Elements.Generator.Element) -> U) -> LazyMapSequence<Self.Elements, U>Added Mirror [struct]Added Mirror.childrenAdded Mirror.customMirror() -> MirrorAdded Mirror.descendant(_: MirrorPathType, _: MirrorPathType) -> Any?Added Mirror.descriptionAdded Mirror.displayStyleAdded Mirror.init<T, C : CollectionType where C.Generator.Element == Child>(_: T, children: C, displayStyle: Mirror.DisplayStyle?, ancestorRepresentation: Mirror.AncestorRepresentation)Added Mirror.init<T>(_: T, children: DictionaryLiteral<String, Any>, displayStyle: Mirror.DisplayStyle?, ancestorRepresentation: Mirror.AncestorRepresentation)Added Mirror.init<T, C : CollectionType>(_: T, unlabeledChildren: C, displayStyle: Mirror.DisplayStyle?, ancestorRepresentation: Mirror.AncestorRepresentation)Added Mirror.init(reflecting: Any)Added Mirror.subjectTypeAdded Mirror.superclassMirror() -> Mirror?Added Mirror.AncestorRepresentation [enum]Added Mirror.AncestorRepresentation.CustomizedAdded Mirror.AncestorRepresentation.GeneratedAdded Mirror.AncestorRepresentation.SuppressedAdded Mirror.DisplayStyle [enum]Added Mirror.DisplayStyle.ClassAdded Mirror.DisplayStyle.CollectionAdded Mirror.DisplayStyle.DictionaryAdded Mirror.DisplayStyle.EnumAdded Mirror.DisplayStyle.OptionalAdded Mirror.DisplayStyle.SetAdded Mirror.DisplayStyle.StructAdded Mirror.DisplayStyle.TupleAdded MirrorPathTypeAdded MutableCollectionType.partition(_: Range<Self.Index>) -> Self.IndexAdded MutableCollectionType.partition(_: Range<Self.Index>, isOrderedBefore: (Self.Generator.Element, Self.Generator.Element) -> Bool) -> Self.IndexAdded MutableCollectionType.sort() -> [Self.Generator.Element]Added MutableCollectionType.sort(_: (Self.Generator.Element, Self.Generator.Element) -> Bool) -> [Self.Generator.Element]Added MutableCollectionType.sortInPlace()Added MutableCollectionType.sortInPlace(_: (Self.Generator.Element, Self.Generator.Element) -> Bool)Added MutableCollectionType.subscript(_: Range<Self.Index>) -> Self.SubSequenceAdded MutableCollectionType.subscript(_: Range<Self.Index>) -> MutableSlice<Self>Added MutableCollectionType.subscript(_: Self.Index) -> Self.Generator.ElementAdded MutableIndexableAdded MutableIndexable.endIndexAdded MutableIndexable.startIndexAdded MutableIndexable.subscript(_: Self.Index) -> Self._ElementAdded MutableSlice [struct]Added MutableSlice.endIndexAdded MutableSlice.init(base: Base, bounds: Range<Base.Index>)Added MutableSlice.startIndexAdded MutableSlice.subscript(_: Range<Base.Index>) -> MutableSlice<Base>Added MutableSlice.subscript(_: Base.Index) -> Base._ElementAdded MutableSliceable.subscript(_: Range<Self.Index>) -> Self.SubSequenceAdded NonObjectiveCBase.init()Added Optional.flatMap<U>(_: (Wrapped) throws -> U?) rethrows -> U?Added Optional.map<U>(_: (Wrapped) throws -> U) rethrows -> U?Added OptionSetTypeAdded OptionSetType.contains(_: Self) -> BoolAdded OptionSetType.exclusiveOr(_: Self) -> SelfAdded OptionSetType.exclusiveOrInPlace(_: Self)Added OptionSetType.init()Added OptionSetType.init(rawValue: Self.RawValue)Added OptionSetType.insert(_: Self)Added OptionSetType.intersect(_: Self) -> SelfAdded OptionSetType.intersectInPlace(_: Self)Added OptionSetType.remove(_: Self) -> Self?Added OptionSetType.union(_: Self) -> SelfAdded OptionSetType.unionInPlace(_: Self)Added PermutationGenerator.init(elements: C, indices: Indices)Added PermutationGenerator.next() -> C.Generator.Element?Added PlaygroundQuickLook [enum]Added PlaygroundQuickLook.AttributedStringAdded PlaygroundQuickLook.BezierPathAdded PlaygroundQuickLook.ColorAdded PlaygroundQuickLook.DoubleAdded PlaygroundQuickLook.FloatAdded PlaygroundQuickLook.ImageAdded PlaygroundQuickLook.init(reflecting: Any)Added PlaygroundQuickLook.IntAdded PlaygroundQuickLook.LogicalAdded PlaygroundQuickLook.PointAdded PlaygroundQuickLook.RangeAdded PlaygroundQuickLook.RectangleAdded PlaygroundQuickLook.SizeAdded PlaygroundQuickLook.SoundAdded PlaygroundQuickLook.SpriteAdded PlaygroundQuickLook.TextAdded PlaygroundQuickLook.UIntAdded PlaygroundQuickLook.URLAdded PlaygroundQuickLook.ViewAdded RandomAccessIndexType.advancedBy(_: Self.Distance) -> SelfAdded RandomAccessIndexType.advancedBy(_: Self.Distance, limit: Self) -> SelfAdded RandomAccessIndexType.distanceTo(_: Self) -> Self.DistanceAdded RangeReplaceableCollectionType.append(_: Self.Generator.Element)Added RangeReplaceableCollectionType.appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_: S)Added RangeReplaceableCollectionType.init()Added RangeReplaceableCollectionType.insert(_: Self.Generator.Element, atIndex: Self.Index)Added RangeReplaceableCollectionType.insertContentsOf<S : CollectionType where S.Generator.Element == Generator.Element>(_: S, at: Self.Index)Added RangeReplaceableCollectionType.insertContentsOf<C : CollectionType where C.Generator.Element == Generator.Element>(_: C, at: Self.Index)Added RangeReplaceableCollectionType.removeAtIndex(_: Self.Index) -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst() -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeFirst(_: Int)Added RangeReplaceableCollectionType.removeLast() -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeRange(_: Range<Self.Index>)Added RangeReplaceableCollectionType.replaceRange<C : CollectionType where C.Generator.Element == Generator.Element>(_: Range<Self.Index>, with: C)Added RangeReplaceableCollectionType.reserveCapacity(_: Self.Index.Distance)Added ReverseCollection [struct]Added ReverseCollection.init(_: Base)Added ReverseIndex [struct]Added ReverseIndex.baseAdded ReverseIndex.init(_: Base)Added ReverseIndexTypeAdded ReverseIndexType.baseAdded ReverseIndexType.init(_: Self.Base)Added ReverseRandomAccessCollection [struct]Added ReverseRandomAccessCollection.init(_: Base)Added ReverseRandomAccessIndex.baseAdded ReverseRandomAccessIndex.init(_: Base)Added SequenceType.contains(_: Self.Generator.Element) -> BoolAdded SequenceType.contains(_: (Self.Generator.Element) throws -> Bool) rethrows -> BoolAdded SequenceType.dropFirst() -> Self.SubSequenceAdded SequenceType.dropFirst(_: Int) -> AnySequence<Self.Generator.Element>Added SequenceType.dropFirst(_: Int) -> Self.SubSequenceAdded SequenceType.dropLast() -> Self.SubSequenceAdded SequenceType.dropLast(_: Int) -> AnySequence<Self.Generator.Element>Added SequenceType.dropLast(_: Int) -> Self.SubSequenceAdded SequenceType.elementsEqual<OtherSequence : SequenceType where OtherSequence.Generator.Element == Generator.Element>(_: OtherSequence) -> BoolAdded SequenceType.elementsEqual<OtherSequence : SequenceType where OtherSequence.Generator.Element == Generator.Element>(_: OtherSequence, isEquivalent: (Self.Generator.Element, Self.Generator.Element) throws -> Bool) rethrows -> BoolAdded SequenceType.enumerate() -> EnumerateSequence<Self>Added SequenceType.filter(_: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]Added SequenceType.flatMap<S : SequenceType>(_: (Self.Generator.Element) throws -> S) rethrows -> [S.Generator.Element]Added SequenceType.flatMap<T>(_: (Self.Generator.Element) throws -> T?) rethrows -> [T]Added SequenceType.flatten() -> FlattenSequence<Self>Added SequenceType.forEach(_: (Self.Generator.Element) throws -> ()) rethrowsAdded SequenceType.generate() -> SelfAdded SequenceType.joinWithSeparator<Separator : SequenceType where Separator.Generator.Element == Generator.Element.Generator.Element>(_: Separator) -> JoinSequence<Self>Added SequenceType.joinWithSeparator(_: String) -> StringAdded SequenceType.lazyAdded SequenceType.lexicographicalCompare<OtherSequence : SequenceType where OtherSequence.Generator.Element == Generator.Element>(_: OtherSequence) -> BoolAdded SequenceType.lexicographicalCompare<OtherSequence : SequenceType where OtherSequence.Generator.Element == Generator.Element>(_: OtherSequence, isOrderedBefore: (Self.Generator.Element, Self.Generator.Element) throws -> Bool) rethrows -> BoolAdded SequenceType.map<T>(_: (Self.Generator.Element) throws -> T) rethrows -> [T]Added SequenceType.maxElement() -> Self.Generator.Element?Added SequenceType.maxElement(_: (Self.Generator.Element, Self.Generator.Element) throws -> Bool) rethrows -> Self.Generator.Element?Added SequenceType.minElement() -> Self.Generator.Element?Added SequenceType.minElement(_: (Self.Generator.Element, Self.Generator.Element) throws -> Bool) rethrows -> Self.Generator.Element?Added SequenceType.prefix(_: Int) -> AnySequence<Self.Generator.Element>Added SequenceType.prefix(_: Int) -> Self.SubSequenceAdded SequenceType.reduce<T>(_: T, combine: (T, Self.Generator.Element) throws -> T) rethrows -> TAdded SequenceType.reverse() -> [Self.Generator.Element]Added SequenceType.sort() -> [Self.Generator.Element]Added SequenceType.sort(_: (Self.Generator.Element, Self.Generator.Element) -> Bool) -> [Self.Generator.Element]Added SequenceType.split(_: Int, allowEmptySlices: Bool, isSeparator: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.SubSequence]Added SequenceType.split(_: Int, allowEmptySlices: Bool, isSeparator: (Self.Generator.Element) throws -> Bool) rethrows -> [AnySequence<Self.Generator.Element>]Added SequenceType.split(_: Self.Generator.Element, maxSplit: Int, allowEmptySlices: Bool) -> [AnySequence<Self.Generator.Element>]Added SequenceType.startsWith<OtherSequence : SequenceType where OtherSequence.Generator.Element == Generator.Element>(_: OtherSequence) -> BoolAdded SequenceType.startsWith<OtherSequence : SequenceType where OtherSequence.Generator.Element == Generator.Element>(_: OtherSequence, isEquivalent: (Self.Generator.Element, Self.Generator.Element) throws -> Bool) rethrows -> BoolAdded SequenceType.suffix(_: Int) -> Self.SubSequenceAdded SequenceType.suffix(_: Int) -> AnySequence<Self.Generator.Element>Added SequenceType.underestimateCount() -> IntAdded Set.popFirst() -> Element?Added Set.removeAtIndex(_: SetIndex<Element>) -> ElementAdded SetAlgebraTypeAdded SetAlgebraType.contains(_: Self.Element) -> BoolAdded SetAlgebraType.element(_: Self.Element, isDisjointWith: Self.Element) -> Bool [class]Added SetAlgebraType.element(_: Self.Element, isDisjointWith: Self.Element) -> Bool [class]Added SetAlgebraType.element(_: Self.Element, subsumes: Self.Element) -> Bool [class]Added SetAlgebraType.element(_: Self.Element, subsumes: Self.Element) -> Bool [class]Added SetAlgebraType.exclusiveOr(_: Self) -> SelfAdded SetAlgebraType.exclusiveOrInPlace(_: Self)Added SetAlgebraType.init()Added SetAlgebraType.init<S : SequenceType where S.Generator.Element == Element>(_: S)Added SetAlgebraType.init<S : SequenceType where S.Generator.Element == Element>(_: S)Added SetAlgebraType.init(arrayLiteral: Self.Element)Added SetAlgebraType.insert(_: Self.Element)Added SetAlgebraType.intersect(_: Self) -> SelfAdded SetAlgebraType.intersectInPlace(_: Self)Added SetAlgebraType.isDisjointWith(_: Self) -> BoolAdded SetAlgebraType.isDisjointWith(_: Self) -> BoolAdded SetAlgebraType.isEmptyAdded SetAlgebraType.isEmptyAdded SetAlgebraType.isStrictSubsetOf(_: Self) -> BoolAdded SetAlgebraType.isStrictSupersetOf(_: Self) -> BoolAdded SetAlgebraType.isSubsetOf(_: Self) -> BoolAdded SetAlgebraType.isSubsetOf(_: Self) -> BoolAdded SetAlgebraType.isSupersetOf(_: Self) -> BoolAdded SetAlgebraType.isSupersetOf(_: Self) -> BoolAdded SetAlgebraType.remove(_: Self.Element) -> Self.Element?Added SetAlgebraType.subtract(_: Self) -> SelfAdded SetAlgebraType.subtract(_: Self) -> SelfAdded SetAlgebraType.subtractInPlace(_: Self)Added SetAlgebraType.subtractInPlace(_: Self)Added SetAlgebraType.union(_: Self) -> SelfAdded SetAlgebraType.unionInPlace(_: Self)Added SignedIntegerType.init(_: IntMax)Added SignedIntegerType.toIntMax() -> IntMaxAdded SignedNumberType.-(_: Self) -> SelfAdded SignedNumberType.-(_: Self, _: Self) -> SelfAdded Slice [struct]Added Slice.endIndexAdded Slice.init(base: Base, bounds: Range<Base.Index>)Added Slice.startIndexAdded Slice.subscript(_: Range<Base.Index>) -> Slice<Base>Added Slice.subscript(_: Base.Index) -> Base._ElementAdded Strideable.advancedBy(_: Self.Stride) -> SelfAdded Strideable.distanceTo(_: Self) -> Self.StrideAdded Strideable.stride(through: Self, by: Self.Stride) -> StrideThrough<Self>Added Strideable.stride(to: Self, by: Self.Stride) -> StrideTo<Self>Added String.appendContentsOf(_: String)Added String.appendContentsOf<S : SequenceType where S.Generator.Element == Character>(_: S)Added [String.characters](https://developer.apple.com/documentation/swift/string/1540072-characters)Added String.init<T>(_: T)Added String.init(_: String.CharacterView)Added String.init<T : UnsignedIntegerType>(_: T)Added String.init<T : UnsignedIntegerType>(_: T, radix: Int, uppercase: Bool)Added String.init<T>(reflecting: T)Added String.insert(_: Character, atIndex: Index)Added String.insertContentsOf<S : CollectionType where S.Generator.Element == Character>(_: S, at: Index)Added String.removeAtIndex(_: Index) -> CharacterAdded String.removeRange(_: Range<Index>)Added String.replaceRange<C : CollectionType where C.Generator.Element == Character>(_: Range<Index>, with: C)Added String.replaceRange(_: Range<Index>, with: String)Added String.subscript(_: Range<Index>) -> StringAdded String.subscript(_: Index) -> CharacterAdded String.withCString<Result>(_: UnsafePointer<Int8> throws -> Result) rethrows -> ResultAdded String.withMutableCharacters<R>(_: (inout String.CharacterView) -> R) -> RAdded String.CharacterView [struct]Added String.CharacterView.append(_: Character)Added String.CharacterView.appendContentsOf<S : SequenceType where S.Generator.Element == Character>(_: S)Added String.CharacterView.endIndexAdded String.CharacterView.init()Added String.CharacterView.init(_: String)Added String.CharacterView.init<S : SequenceType where S.Generator.Element == Character>(_: S)Added String.CharacterView.replaceRange<C : CollectionType where C.Generator.Element == Character>(_: Range<String.CharacterView.Index>, with: C)Added String.CharacterView.reserveCapacity(_: Int)Added String.CharacterView.startIndexAdded String.CharacterView.subscript(_: String.CharacterView.Index) -> CharacterAdded String.CharacterView.subscript(_: Range<String.CharacterView.Index>) -> String.CharacterViewAdded String.CharacterView.Index [struct]Added String.CharacterView.Index.predecessor() -> String.CharacterView.IndexAdded String.CharacterView.Index.successor() -> String.CharacterView.IndexAdded String.UnicodeScalarView.appendContentsOf<S : SequenceType where S.Generator.Element == UnicodeScalar>(_: S)Added String.UnicodeScalarView.replaceRange<C : CollectionType where C.Generator.Element == UnicodeScalar>(_: Range<String.UnicodeScalarView.Index>, with: C)Added String.UTF16View.Index.advancedBy(_: Distance) -> String.UTF16View.IndexAdded String.UTF16View.Index.advancedBy(_: Distance, limit: String.UTF16View.Index) -> String.UTF16View.IndexAdded String.UTF16View.Index.distanceTo(_: String.UTF16View.Index) -> DistanceAdded String.UTF16View.Index.init(_: Index, within: String.UTF16View)Added String.UTF16View.Index.samePositionIn(_: String) -> Index?Added String.UTF8View.Index.init(_: Index, within: String.UTF8View)Added String.UTF8View.Index.samePositionIn(_: String) -> Index?Added UInt.init(_: String, radix: Int)Added UInt16.init(_: String, radix: Int)Added UInt32.init(_: String, radix: Int)Added UInt64.init(_: String, radix: Int)Added UInt8.init(_: String, radix: Int)Added UnicodeCodecType.encode(_: UnicodeScalar, output: (Self.CodeUnit) -> ()) [class]Added UnicodeScalarIndex.init(_: Index, within: String.UnicodeScalarView)Added UnicodeScalarIndex.samePositionIn(_: String) -> Index?Added UnsafeMutablePointer.initializeFrom<C : CollectionType where C.Generator.Element == Memory>(_: C)Added UTF16.encode(_: UnicodeScalar, output: (CodeUnit) -> ()) [static]Added UTF32.encode(_: UnicodeScalar, output: (CodeUnit) -> ()) [static]Added UTF8.encode(_: UnicodeScalar, output: (CodeUnit) -> ()) [static]Added Zip2Generator [struct]Added Zip2Generator.init(_: Generator1, _: Generator2)Added Zip2Generator.next() -> (Generator1.Element, Generator2.Element)?Added Zip2Sequence [struct]Added Zip2Sequence.generate() -> Zip2Generator<Sequence1.Generator, Sequence2.Generator>Added Zip2Sequence.init(_: Sequence1, _: Sequence2)Added !=(_: T, _: T) -> BoolAdded !=(_: T, _: T) -> BoolAdded !=(_: Any.Type?, _: Any.Type?) -> BoolAdded !==(_: L, _: R) -> BoolAdded &&(_: T, _: () throws -> Bool) rethrows -> BoolAdded &&(_: T, _: () throws -> U) rethrows -> BoolAdded +(_: S, _: C) -> CAdded +(_: C, _: S) -> CAdded +(_: T, _: T.Stride) -> TAdded +(_: T.Stride, _: T) -> TAdded +(_: C, _: S) -> CAdded +(_: RRC1, _: RRC2) -> RRC1Added ++(_: T) -> TAdded ++(_: T) -> TAdded +=(_: [Element], _: C)Added +=(_: ContiguousArray<Element>, _: C)Added +=(_: T, _: T.Stride)Added +=(_: _ContiguousArrayBuffer<Element>, _: C)Added +=(_: ArraySlice<Element>, _: C)Added -(_: T, _: T.Stride) -> TAdded -(_: T, _: T) -> T.StrideAdded --(_: T) -> TAdded --(_: T) -> TAdded -=(_: T, _: T.Stride)Added ...(_: Pos, _: Pos) -> Range<Pos>Added ...(_: Pos, _: Pos) -> Range<Pos>Added ..<(_: Pos, _: Pos) -> Range<Pos>Added ..<(_: Pos, _: Pos) -> Range<Pos>Added <(_: Index, _: Index) -> BoolAdded ==(_: T, _: T) -> BoolAdded ==(_: _SwiftNSOperatingSystemVersion, _: _SwiftNSOperatingSystemVersion) -> BoolAdded ==(_: LazyFilterIndex<Base>, _: LazyFilterIndex<Base>) -> BoolAdded ==(_: T, _: T) -> BoolAdded ==(_: AnyBidirectionalIndex, _: AnyBidirectionalIndex) -> BoolAdded ==(_: _HeapBuffer<Value, Element>, _: _HeapBuffer<Value, Element>) -> BoolAdded ==(_: AnyForwardIndex, _: AnyForwardIndex) -> BoolAdded ==(_: FlattenCollectionIndex<BaseElements>, _: FlattenCollectionIndex<BaseElements>) -> BoolAdded ==(_: Index, _: Index) -> BoolAdded ==(_: AnyRandomAccessIndex, _: AnyRandomAccessIndex) -> BoolAdded ==(_: ReverseIndex<Base>, _: ReverseIndex<Base>) -> BoolAdded ==(_: Any.Type?, _: Any.Type?) -> BoolAdded ==(_: FlattenBidirectionalCollectionIndex<BaseElements>, _: FlattenBidirectionalCollectionIndex<BaseElements>) -> BoolAdded ===(_: L, _: R) -> BoolAdded ??(_: T?, _: () throws -> T?) rethrows -> T?Added ??(_: T?, _: () throws -> T) rethrows -> TAdded AnyBidirectionalIndex.DistanceAdded AnyForwardIndex.DistanceAdded anyGenerator<G : GeneratorType>(_: G) -> AnyGenerator<G.Element>Added anyGenerator<Element>(_: () -> Element?) -> AnyGenerator<Element>Added AnyRandomAccessIndex.DistanceAdded Bit.DistanceAdded CollectionType.GeneratorAdded CollectionType.SubSequenceAdded debugPrint(_: Any, separator: String, terminator: String)Added debugPrint<Target : OutputStreamType>(_: Any, separator: String, terminator: String, toStream: Target)Added DictionaryLiteral.ElementAdded FlattenBidirectionalCollection.IndexAdded FlattenCollection.IndexAdded Indexable.IndexAdded LazyCollection.ElementsAdded LazyCollection.IndexAdded LazyCollectionType.ElementsAdded LazyFilterCollection.IndexAdded LazyMapCollection.IndexAdded LazyMapSequence.ElementsAdded LazySequenceType.ElementsAdded Mirror.ChildAdded Mirror.ChildrenAdded MutableCollectionType.SubSequenceAdded MutableIndexable.IndexAdded MutableSlice.IndexAdded numericCast<T : _SignedIntegerType, U : UnsignedIntegerType>(_: T) -> UAdded numericCast<T : UnsignedIntegerType, U : _SignedIntegerType>(_: T) -> UAdded numericCast<T : UnsignedIntegerType, U : UnsignedIntegerType>(_: T) -> UAdded OptionSetType.ElementAdded print(_: Any, separator: String, terminator: String)Added print<Target : OutputStreamType>(_: Any, separator: String, terminator: String, toStream: Target)Added readLine(stripNewline: Bool) -> String?Added ReverseCollection.GeneratorAdded ReverseCollection.IndexAdded ReverseIndex.DistanceAdded ReverseIndexType.BaseAdded ReverseIndexType.DistanceAdded ReverseRandomAccessCollection.GeneratorAdded ReverseRandomAccessCollection.IndexAdded SequenceType.SubSequenceAdded SetAlgebraType.ElementAdded Slice.IndexAdded String.IndexAdded transcode<Input : GeneratorType, InputEncoding : UnicodeCodecType, OutputEncoding : UnicodeCodecType where InputEncoding.CodeUnit == Input.Element>(_: InputEncoding.Type, _: OutputEncoding.Type, _: Input, _: (OutputEncoding.CodeUnit) -> (), stopOnError: Bool) -> BoolAdded UnsafeMutablePointer.DistanceAdded UnsafePointer.DistanceAdded withExtendedLifetime<T, Result>(_: T, _: T throws -> Result) rethrows -> ResultAdded withExtendedLifetime<T, Result>(_: T, _: () throws -> Result) rethrows -> ResultAdded withUnsafeMutablePointer<T, Result>(_: T, _: UnsafeMutablePointer<T> throws -> Result) rethrows -> ResultAdded withUnsafeMutablePointers<A0, A1, Result>(_: A0, _: A1, _: (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>) throws -> Result) rethrows -> ResultAdded withUnsafeMutablePointers<A0, A1, A2, Result>(_: A0, _: A1, _: A2, _: (UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>, UnsafeMutablePointer<A2>) throws -> Result) rethrows -> ResultAdded withUnsafePointer<T, Result>(_: T, _: UnsafePointer<T> throws -> Result) rethrows -> ResultAdded withUnsafePointers<A0, A1, Result>(_: A0, _: A1, _: (UnsafePointer<A0>, UnsafePointer<A1>) throws -> Result) rethrows -> ResultAdded withUnsafePointers<A0, A1, A2, Result>(_: A0, _: A1, _: A2, _: (UnsafePointer<A0>, UnsafePointer<A1>, UnsafePointer<A2>) throws -> Result) rethrows -> ResultAdded zip<Sequence1 : SequenceType, Sequence2 : SequenceType>(_: Sequence1, _: Sequence2) -> Zip2Sequence<Sequence1, Sequence2>Added Zip2Generator.ElementAdded Zip2Sequence.GeneratorAdded Zip2Sequence.Stream1Added Zip2Sequence.Stream2Added ||(_: T, _: () throws -> Bool) rethrows -> BoolAdded ||(_: T, _: () throws -> U) rethrows -> BoolModified AbsoluteValuable

|  | Declaration |
| --- | --- |
| From | ``` protocol AbsoluteValuable : SignedNumberType {     static func abs(_ x: Self) -> Self } ``` |
| To | ``` protocol AbsoluteValuable : SignedNumberType {     @warn_unused_result     static func abs(_ x: Self) -> Self } ``` |

Modified AbsoluteValuable.abs(_: Self) -> Self [class]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` static func abs(_ x: Self) -> Self ``` | iOS 8.3 |
| To | ``` @warn_unused_result     static func abs(_ x: Self) -> Self ``` | iOS 9.0 |

Modified [Array [struct]](https://developer.apple.com/documentation/swift/array)

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct Array<T> : MutableCollectionType, Sliceable, _DestructorSafeContainer {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<[T]>     typealias SubSlice = ArraySlice<T>     subscript (subRange: Range<Int>) -> ArraySlice<T>     init(_ buffer: _ArrayBuffer<T>) } extension Array : _ObjectiveCBridgeable {     init(_fromNSArray source: NSArray, noCopy noCopy: Bool = default) } extension Array : __ArrayType { } extension Array : ArrayLiteralConvertible {     init(arrayLiteral elements: T...) } extension Array : _ArrayType {     init()     init<S : SequenceType where T == T>(_ s: S)     init(count count: Int, repeatedValue repeatedValue: T)     init(_uninitializedCount count: Int)     var count: Int { get }     var capacity: Int { get }     var isEmpty: Bool { get }     var first: T? { get }     var last: T? { get }     mutating func reserveCapacity(_ minimumCapacity: Int)     mutating func append(_ newElement: T)     mutating func extend<S : SequenceType where T == T>(_ newElements: S)     mutating func removeLast() -> T     mutating func insert(_ newElement: T, atIndex i: Int)     mutating func removeAtIndex(_ index: Int) -> T     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     func join<S : SequenceType where [T] == [T]>(_ elements: S) -> [T]     func reduce<U>(_ initial: U, combine combine: @noescape (U, T) -> U) -> U     mutating func sort(_ isOrderedBefore: (T, T) -> Bool)     func sorted(_ isOrderedBefore: (T, T) -> Bool) -> [T]     func map<U>(_ transform: (T) -> U) -> [U]     func flatMap<U>(_ transform: @noescape (T) -> [U]) -> [U]     func reverse() -> [T]     func filter(_ includeElement: (T) -> Bool) -> [T] } extension Array : Reflectable {     func getMirror() -> MirrorType } extension Array : Printable, DebugPrintable {     var description: String { get }     var debugDescription: String { get } } extension Array {     func withUnsafeBufferPointer<R>(_ body: @noescape (UnsafeBufferPointer<T>) -> R) -> R     mutating func withUnsafeMutableBufferPointer<R>(_ body: @noescape (inout UnsafeMutableBufferPointer<T>) -> R) -> R } extension Array {     mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C)     mutating func splice<S : CollectionType where T == T>(_ newElements: S, atIndex i: Int)     mutating func removeRange(_ subRange: Range<Int>) } extension Array {     init(_fromCocoaArray source: _NSArrayCoreType, noCopy noCopy: Bool = default) } ``` | ArrayLiteralConvertible, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable | -- |
| To | ``` struct Array<Element> : CollectionType, Indexable, SequenceType, MutableCollectionType, MutableIndexable, _DestructorSafeContainer {     typealias T = Element     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ index: Int) -> Element     subscript (_ subRange: Range<Int>) -> ArraySlice<Element> } extension Array : _ObjectiveCBridgeable { } extension Array : ArrayLiteralConvertible {     init(arrayLiteral elements: Element...) } extension Array : _ArrayType, MutableSliceable, RangeReplaceableCollectionType {     init()     init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_ s: S)     init(count count: Int, repeatedValue repeatedValue: Element)     var count: Int { get }     var capacity: Int { get }     mutating func reserveCapacity(_ minimumCapacity: Int)     mutating func append(_ newElement: Element)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == Element>(_ newElements: S)     mutating func appendContentsOf<C : CollectionType where C.Generator.Element == Element>(_ newElements: C)     mutating func removeLast() -> Element     mutating func insert(_ newElement: Element, atIndex i: Int)     mutating func removeAtIndex(_ index: Int) -> Element     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     func sorted(_ isOrderedBefore: (Element, Element) -> Bool) -> [Element] } extension Array : _Reflectable { } extension Array : CustomStringConvertible, CustomDebugStringConvertible {     var description: String { get }     var debugDescription: String { get } } extension Array {     @rethrows func withUnsafeBufferPointer<R>(@noescape _ body: (UnsafeBufferPointer<Element>) throws -> R) rethrows -> R     @rethrows mutating func withUnsafeMutableBufferPointer<R>(@noescape _ body: (inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R } extension Array {     mutating func replaceRange<C : CollectionType where C.Generator.Element == _Buffer.Element>(_ subRange: Range<Int>, with newElements: C) } extension Array {     mutating func popLast() -> Element? } ``` | ArrayLiteralConvertible, CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Indexable, MutableCollectionType, MutableIndexable, MutableSliceable, RangeReplaceableCollectionType, SequenceType | Element |

Modified Array.append(_: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func append(_ newElement: T) ``` | iOS 8.0 |
| To | ``` mutating func append(_ newElement: Element) ``` | iOS 9.0 |

Modified Array.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Array.init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` init<S : SequenceType where T == T>(_ s: S) ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_ s: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == _Buffer.Element ``` | S |

Modified Array.init(arrayLiteral: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(arrayLiteral elements: T...) ``` | iOS 8.1 |
| To | ``` init(arrayLiteral elements: Element...) ``` | iOS 9.0 |

Modified Array.init(count: Int, repeatedValue: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(count count: Int, repeatedValue repeatedValue: T) ``` | iOS 8.0 |
| To | ``` init(count count: Int, repeatedValue repeatedValue: Element) ``` | iOS 9.0 |

Modified Array.insert(_: Element, atIndex: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func insert(_ newElement: T, atIndex i: Int) ``` | iOS 8.0 |
| To | ``` mutating func insert(_ newElement: Element, atIndex i: Int) ``` | iOS 9.0 |

Modified Array.removeAll(keepCapacity: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Array.removeAtIndex(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func removeAtIndex(_ index: Int) -> T ``` | iOS 8.0 |
| To | ``` mutating func removeAtIndex(_ index: Int) -> Element ``` | iOS 9.0 |

Modified Array.removeLast() -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func removeLast() -> T ``` | iOS 8.0 |
| To | ``` mutating func removeLast() -> Element ``` | iOS 9.0 |

Modified Array.reserveCapacity(_: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Array.subscript(_: Range<Int>) -> ArraySlice<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (subRange: Range<Int>) -> ArraySlice<T> ``` | iOS 8.3 |
| To | ``` subscript (_ subRange: Range<Int>) -> ArraySlice<Element> ``` | iOS 9.0 |

Modified Array.subscript(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (index: Int) -> T ``` | iOS 8.0 |
| To | ``` subscript (_ index: Int) -> Element ``` | iOS 9.0 |

Modified ArrayLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol ArrayLiteralConvertible {     typealias Element     init(arrayLiteral elements: Element...) } ``` |
| To | ``` protocol ArrayLiteralConvertible {     typealias Element     init(arrayLiteral elements: Self.Element...) } ``` |

Modified ArrayLiteralConvertible.init(arrayLiteral: Self.Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(arrayLiteral elements: Element...) ``` | iOS 8.1 |
| To | ``` init(arrayLiteral elements: Self.Element...) ``` | iOS 9.0 |

Modified ArraySlice [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct ArraySlice<T> : MutableCollectionType, Sliceable, _DestructorSafeContainer {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<ArraySlice<T>>     typealias SubSlice = ArraySlice<T>     subscript (subRange: Range<Int>) -> ArraySlice<T>     init(_ buffer: _SliceBuffer<T>) } extension ArraySlice : __ArrayType { } extension ArraySlice : ArrayLiteralConvertible {     init(arrayLiteral elements: T...) } extension ArraySlice : _ArrayType {     init()     init<S : SequenceType where T == T>(_ s: S)     init(count count: Int, repeatedValue repeatedValue: T)     init(_uninitializedCount count: Int)     var count: Int { get }     var capacity: Int { get }     var isEmpty: Bool { get }     var first: T? { get }     var last: T? { get }     mutating func reserveCapacity(_ minimumCapacity: Int)     mutating func append(_ newElement: T)     mutating func extend<S : SequenceType where T == T>(_ newElements: S)     mutating func removeLast() -> T     mutating func insert(_ newElement: T, atIndex i: Int)     mutating func removeAtIndex(_ index: Int) -> T     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     func join<S : SequenceType where ArraySlice<T> == ArraySlice<T>>(_ elements: S) -> ArraySlice<T>     func reduce<U>(_ initial: U, combine combine: @noescape (U, T) -> U) -> U     mutating func sort(_ isOrderedBefore: (T, T) -> Bool)     func sorted(_ isOrderedBefore: (T, T) -> Bool) -> ArraySlice<T>     func map<U>(_ transform: (T) -> U) -> ArraySlice<U>     func flatMap<U>(_ transform: @noescape (T) -> ArraySlice<U>) -> ArraySlice<U>     func reverse() -> ArraySlice<T>     func filter(_ includeElement: (T) -> Bool) -> ArraySlice<T> } extension ArraySlice : Reflectable {     func getMirror() -> MirrorType } extension ArraySlice : Printable, DebugPrintable {     var description: String { get }     var debugDescription: String { get } } extension ArraySlice {     func withUnsafeBufferPointer<R>(_ body: @noescape (UnsafeBufferPointer<T>) -> R) -> R     mutating func withUnsafeMutableBufferPointer<R>(_ body: @noescape (inout UnsafeMutableBufferPointer<T>) -> R) -> R } extension ArraySlice {     mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C)     mutating func splice<S : CollectionType where T == T>(_ newElements: S, atIndex i: Int)     mutating func removeRange(_ subRange: Range<Int>) } ``` | ArrayLiteralConvertible, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable | -- |
| To | ``` struct ArraySlice<Element> : Indexable, SequenceType, CollectionType, MutableCollectionType, MutableIndexable, _DestructorSafeContainer {     typealias T = Element     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ index: Int) -> Element     subscript (_ subRange: Range<Int>) -> ArraySlice<Element> } extension ArraySlice : ArrayLiteralConvertible {     init(arrayLiteral elements: Element...) } extension ArraySlice : _ArrayType, MutableSliceable, RangeReplaceableCollectionType {     init()     init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_ s: S)     init(count count: Int, repeatedValue repeatedValue: Element)     var count: Int { get }     var capacity: Int { get }     mutating func reserveCapacity(_ minimumCapacity: Int)     mutating func append(_ newElement: Element)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == Element>(_ newElements: S)     mutating func appendContentsOf<C : CollectionType where C.Generator.Element == Element>(_ newElements: C)     mutating func removeLast() -> Element     mutating func insert(_ newElement: Element, atIndex i: Int)     mutating func removeAtIndex(_ index: Int) -> Element     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     func sorted(_ isOrderedBefore: (Element, Element) -> Bool) -> ArraySlice<Element> } extension ArraySlice : _Reflectable { } extension ArraySlice : CustomStringConvertible, CustomDebugStringConvertible {     var description: String { get }     var debugDescription: String { get } } extension ArraySlice {     @rethrows func withUnsafeBufferPointer<R>(@noescape _ body: (UnsafeBufferPointer<Element>) throws -> R) rethrows -> R     @rethrows mutating func withUnsafeMutableBufferPointer<R>(@noescape _ body: (inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R } extension ArraySlice {     mutating func replaceRange<C : CollectionType where C.Generator.Element == _Buffer.Element>(_ subRange: Range<Int>, with newElements: C) } ``` | ArrayLiteralConvertible, CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Indexable, MutableCollectionType, MutableIndexable, MutableSliceable, RangeReplaceableCollectionType, SequenceType | Element |

Modified ArraySlice.append(_: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func append(_ newElement: T) ``` | iOS 8.3 |
| To | ``` mutating func append(_ newElement: Element) ``` | iOS 9.0 |

Modified ArraySlice.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ArraySlice.init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` init<S : SequenceType where T == T>(_ s: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_ s: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == _Buffer.Element ``` | S |

Modified ArraySlice.init(arrayLiteral: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(arrayLiteral elements: T...) ``` | iOS 8.3 |
| To | ``` init(arrayLiteral elements: Element...) ``` | iOS 9.0 |

Modified ArraySlice.init(count: Int, repeatedValue: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(count count: Int, repeatedValue repeatedValue: T) ``` | iOS 8.3 |
| To | ``` init(count count: Int, repeatedValue repeatedValue: Element) ``` | iOS 9.0 |

Modified ArraySlice.insert(_: Element, atIndex: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func insert(_ newElement: T, atIndex i: Int) ``` | iOS 8.3 |
| To | ``` mutating func insert(_ newElement: Element, atIndex i: Int) ``` | iOS 9.0 |

Modified ArraySlice.removeAll(keepCapacity: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ArraySlice.removeAtIndex(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func removeAtIndex(_ index: Int) -> T ``` | iOS 8.3 |
| To | ``` mutating func removeAtIndex(_ index: Int) -> Element ``` | iOS 9.0 |

Modified ArraySlice.removeLast() -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func removeLast() -> T ``` | iOS 8.3 |
| To | ``` mutating func removeLast() -> Element ``` | iOS 9.0 |

Modified ArraySlice.reserveCapacity(_: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ArraySlice.subscript(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (index: Int) -> T ``` | iOS 8.3 |
| To | ``` subscript (_ index: Int) -> Element ``` | iOS 9.0 |

Modified ArraySlice.subscript(_: Range<Int>) -> ArraySlice<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (subRange: Range<Int>) -> ArraySlice<T> ``` | iOS 8.3 |
| To | ``` subscript (_ subRange: Range<Int>) -> ArraySlice<Element> ``` | iOS 9.0 |

Modified AutoreleasingUnsafeMutablePointer [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct AutoreleasingUnsafeMutablePointer<T> : Equatable, NilLiteralConvertible, _PointerType {     var memory: T { get nonmutating set }     subscript (i: Int) -> T { get }     init(nilLiteral nilLiteral: ())     static func null() -> AutoreleasingUnsafeMutablePointer<T>     init()     init<U>(_ ptr: UnsafeMutablePointer<U>)     init<U>(_ ptr: UnsafePointer<U>) } extension AutoreleasingUnsafeMutablePointer : DebugPrintable {     var debugDescription: String { get } } extension AutoreleasingUnsafeMutablePointer : CVarArgType {     func encode() -> [Word] } ``` | CVarArgType, DebugPrintable, Equatable, NilLiteralConvertible | -- |
| To | ``` struct AutoreleasingUnsafeMutablePointer<Memory> : Equatable, NilLiteralConvertible, _PointerType {     typealias T = Memory     var memory: Memory { get nonmutating set }     subscript (_ i: Int) -> Memory { get }     init(nilLiteral nilLiteral: ())     init()     init<U>(_ ptr: UnsafeMutablePointer<U>) } extension AutoreleasingUnsafeMutablePointer : CustomDebugStringConvertible {     var debugDescription: String { get } } extension AutoreleasingUnsafeMutablePointer : CVarArgType { } ``` | CVarArgType, CustomDebugStringConvertible, Equatable, NilLiteralConvertible | Memory |

Modified AutoreleasingUnsafeMutablePointer.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified AutoreleasingUnsafeMutablePointer.init<U>(_: UnsafeMutablePointer<U>)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | U |

Modified AutoreleasingUnsafeMutablePointer.init(nilLiteral: ())

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified AutoreleasingUnsafeMutablePointer.memory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var memory: T { get nonmutating set } ``` | iOS 8.0 |
| To | ``` var memory: Memory { get nonmutating set } ``` | iOS 9.0 |

Modified AutoreleasingUnsafeMutablePointer.subscript(_: Int) -> Memory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (i: Int) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ i: Int) -> Memory { get } ``` | iOS 9.0 |

Modified BidirectionalIndexType

|  | Declaration |
| --- | --- |
| From | ``` protocol BidirectionalIndexType : ForwardIndexType, _BidirectionalIndexType { } ``` |
| To | ``` protocol BidirectionalIndexType : ForwardIndexType {     @warn_unused_result     func predecessor() -> Self } ``` |

Modified Bit [enum]

|  | Declaration | Protocols | Raw Value Type |
| --- | --- | --- | --- |
| From | ``` enum Bit : Int, RandomAccessIndexType, Reflectable {     case Zero     case One     func successor() -> Bit     func predecessor() -> Bit     func distanceTo(_ other: Bit) -> Int     func advancedBy(_ distance: Int) -> Bit     func getMirror() -> MirrorType } extension Bit : IntegerArithmeticType {     static func addWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func subtractWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func divideWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func remainderWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     func toIntMax() -> IntMax } ``` | Equatable, Hashable, IntegerArithmeticType, RandomAccessIndexType, RawRepresentable, Reflectable | -- |
| To | ``` enum Bit : Int, _Incrementable, Comparable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity, _Reflectable {     typealias Distance = Int     case Zero     case One     func successor() -> Bit     func predecessor() -> Bit     func distanceTo(_ other: Bit) -> Int     func advancedBy(_ n: Distance) -> Bit } extension Bit : IntegerArithmeticType, _IntegerArithmeticType {     static func addWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func subtractWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func divideWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     static func remainderWithOverflow(_ lhs: Bit, _ rhs: Bit) -> (Bit, overflow: Bool)     func toIntMax() -> IntMax } ``` | BidirectionalIndexType, Comparable, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, RandomAccessIndexType, RawRepresentable, Strideable | Int |

Modified Bit.advancedBy(_: Distance) -> Bit

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ distance: Int) -> Bit ``` |
| To | ``` func advancedBy(_ n: Distance) -> Bit ``` |

Modified BitwiseOperationsType

|  | Declaration |
| --- | --- |
| From | ``` protocol BitwiseOperationsType {     func &(_ lhs: Self, _ rhs: Self) -> Self     func |(_ lhs: Self, _ rhs: Self) -> Self     func ^(_ lhs: Self, _ rhs: Self) -> Self     prefix func ~(_ x: Self) -> Self     static var allZeros: Self { get } } ``` |
| To | ``` protocol BitwiseOperationsType {     @warn_unused_result     func &(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     func |(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     func ^(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     prefix func ~(_ x: Self) -> Self     static var allZeros: Self { get } } ``` |

Modified BitwiseOperationsType.allZeros

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified [Bool [struct]](https://developer.apple.com/documentation/swift/bool)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Bool {     var value: Builtin.Int1     init()     init(_ v: Builtin.Int1) } extension Bool : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Bool : BooleanLiteralConvertible {     init(_builtinBooleanLiteral value: Builtin.Int1)     init(booleanLiteral value: Bool) } extension Bool : BooleanType {     var boolValue: Bool { get }     init<T : BooleanType>(_ value: T) } extension Bool : Printable {     var description: String { get } } extension Bool : Equatable, Hashable {     var hashValue: Int { get } } extension Bool : Reflectable {     func getMirror() -> MirrorType } ``` | BooleanLiteralConvertible, BooleanType, Equatable, Hashable, Printable, Reflectable |
| To | ``` struct Bool {     init() } extension Bool : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Bool : BooleanLiteralConvertible {     init(_builtinBooleanLiteral value: Builtin.Int1)     init(booleanLiteral value: Bool) } extension Bool : BooleanType {     var boolValue: Bool { get }     init<T : BooleanType>(_ value: T) } extension Bool : CustomStringConvertible {     var description: String { get } } extension Bool : Equatable, Hashable {     var hashValue: Int { get } } extension Bool : _Reflectable { } ``` | BooleanLiteralConvertible, BooleanType, CustomStringConvertible, Equatable, Hashable |

Modified Bool.init<T : BooleanType>(_: T)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.0 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : BooleanType ``` | T |

Modified BooleanLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol BooleanLiteralConvertible {     typealias BooleanLiteralType     init(booleanLiteral value: BooleanLiteralType) } ``` |
| To | ``` protocol BooleanLiteralConvertible {     typealias BooleanLiteralType     init(booleanLiteral value: Self.BooleanLiteralType) } ``` |

Modified BooleanLiteralConvertible.init(booleanLiteral: Self.BooleanLiteralType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(booleanLiteral value: BooleanLiteralType) ``` | iOS 8.1 |
| To | ``` init(booleanLiteral value: Self.BooleanLiteralType) ``` | iOS 9.0 |

Modified Character [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Character : ExtendedGraphemeClusterLiteralConvertible, Equatable, Hashable, Comparable {     enum Representation {         case Large         case Small     }     init(_ scalar: UnicodeScalar)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: Character)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: Character)     init(_ s: String)     var hashValue: Int { get }     typealias UTF16View = String.UTF16View     var utf16: UTF16View { get } } extension Character : DebugPrintable {     var debugDescription: String { get } } extension Character : Reflectable {     func getMirror() -> MirrorType } extension Character : Streamable {     func writeTo<Target : OutputStreamType>(inout _ target: Target) } ``` | Comparable, DebugPrintable, Equatable, ExtendedGraphemeClusterLiteralConvertible, Hashable, Reflectable, Streamable |
| To | ``` struct Character : Hashable, Equatable, ExtendedGraphemeClusterLiteralConvertible, UnicodeScalarLiteralConvertible, Comparable {     init(_ scalar: UnicodeScalar)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: Character)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: Character)     init(_ s: String)     var hashValue: Int { get } } extension Character : CustomDebugStringConvertible {     var debugDescription: String { get } } extension Character : _Reflectable { } extension Character : Streamable {     func writeTo<Target : OutputStreamType>(inout _ target: Target) } ``` | Comparable, CustomDebugStringConvertible, Equatable, ExtendedGraphemeClusterLiteralConvertible, Hashable, Streamable, UnicodeScalarLiteralConvertible |

Modified Character.writeTo<Target : OutputStreamType>(_: Target)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` Target : OutputStreamType ``` | Target |

Modified ClosedInterval [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct ClosedInterval<T : Comparable> : IntervalType, Equatable, Printable, DebugPrintable, Reflectable {     typealias Bound = T     init(_ x: ClosedInterval<T>)     init(_ start: T, _ end: T)     var start: T { get }     var end: T { get }     var description: String { get }     var debugDescription: String { get }     func contains(_ x: T) -> Bool     func clamp(_ intervalToClamp: ClosedInterval<T>) -> ClosedInterval<T>     func getMirror() -> MirrorType } extension ClosedInterval {     var isEmpty: Bool { get } } ``` | DebugPrintable, Equatable, IntervalType, Printable, Reflectable | ```  ``` | -- |
| To | ``` struct ClosedInterval<Bound : Comparable> : IntervalType, Equatable, CustomStringConvertible, CustomDebugStringConvertible, _Reflectable {     typealias T = Bound     init(_ x: ClosedInterval<Bound>)     init(_ start: Bound, _ end: Bound)     var start: Bound { get }     var end: Bound { get }     var description: String { get }     var debugDescription: String { get }     @warn_unused_result     func contains(_ x: Bound) -> Bool     @warn_unused_result     func clamp(_ intervalToClamp: ClosedInterval<Bound>) -> ClosedInterval<Bound> } extension ClosedInterval {     var isEmpty: Bool { get } } ``` | CustomDebugStringConvertible, CustomStringConvertible, Equatable, IntervalType | ``` Bound : Comparable ``` | Bound |

Modified ClosedInterval.clamp(_: ClosedInterval<Bound>) -> ClosedInterval<Bound>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clamp(_ intervalToClamp: ClosedInterval<T>) -> ClosedInterval<T> ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func clamp(_ intervalToClamp: ClosedInterval<Bound>) -> ClosedInterval<Bound> ``` | iOS 9.0 |

Modified ClosedInterval.contains(_: Bound) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contains(_ x: T) -> Bool ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func contains(_ x: Bound) -> Bool ``` | iOS 9.0 |

Modified ClosedInterval.end

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var end: T { get } ``` | iOS 8.0 |
| To | ``` var end: Bound { get } ``` | iOS 9.0 |

Modified ClosedInterval.init(_: ClosedInterval<Bound>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ x: ClosedInterval<T>) ``` | iOS 8.0 |
| To | ``` init(_ x: ClosedInterval<Bound>) ``` | iOS 9.0 |

Modified ClosedInterval.init(_: Bound, _: Bound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ start: T, _ end: T) ``` | iOS 8.0 |
| To | ``` init(_ start: Bound, _ end: Bound) ``` | iOS 9.0 |

Modified ClosedInterval.start

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var start: T { get } ``` | iOS 8.0 |
| To | ``` var start: Bound { get } ``` | iOS 9.0 |

Modified CollectionOfOne [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct CollectionOfOne<T> : CollectionType {     typealias Index = Bit     init(_ element: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> GeneratorOfOne<T>     subscript (position: Index) -> T { get }     let element: T } extension CollectionOfOne : Reflectable {     func getMirror() -> MirrorType } ``` | CollectionType, Reflectable | -- |
| To | ``` struct CollectionOfOne<Element> : CollectionType, Indexable, SequenceType {     typealias T = Element     typealias Index = Bit     init(_ element: Element)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> GeneratorOfOne<Element>     subscript (_ position: Index) -> Element { get }     var count: Int { get } } extension CollectionOfOne : _Reflectable { } ``` | CollectionType, Indexable, SequenceType | Element |

Modified CollectionOfOne.generate() -> GeneratorOfOne<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> GeneratorOfOne<T> ``` | iOS 8.0 |
| To | ``` func generate() -> GeneratorOfOne<Element> ``` | iOS 9.0 |

Modified CollectionOfOne.init(_: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ element: T) ``` | iOS 8.0 |
| To | ``` init(_ element: Element) ``` | iOS 9.0 |

Modified CollectionOfOne.subscript(_: Index) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (position: Index) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ position: Index) -> Element { get } ``` | iOS 9.0 |

Modified CollectionType

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol CollectionType : _CollectionType, SequenceType {     subscript (position: Self.Index) -> Self.Generator.Element { get } } ``` | SequenceType |
| To | ``` protocol CollectionType : Indexable, SequenceType {     typealias Generator : GeneratorType = IndexingGenerator<Self>     func generate() -> Self.Generator     typealias SubSequence : Indexable, SequenceType = Slice<Self>     subscript (_ position: Self.Index) -> Self.Generator.Element { get }     subscript (_ bounds: Range<Self.Index>) -> Self.SubSequence { get }     @warn_unused_result     func prefixUpTo(_ end: Self.Index) -> Self.SubSequence     @warn_unused_result     func suffixFrom(_ start: Self.Index) -> Self.SubSequence     @warn_unused_result     func prefixThrough(_ position: Self.Index) -> Self.SubSequence     var isEmpty: Bool { get }     var count: Self.Index.Distance { get }     var first: Self.Generator.Element? { get } } ``` | Indexable, SequenceType |

Modified Comparable

|  | Declaration |
| --- | --- |
| From | ``` protocol Comparable : _Comparable, Equatable {     func <=(_ lhs: Self, _ rhs: Self) -> Bool     func >=(_ lhs: Self, _ rhs: Self) -> Bool     func >(_ lhs: Self, _ rhs: Self) -> Bool } ``` |
| To | ``` protocol Comparable : Equatable {     @warn_unused_result     func <(_ lhs: Self, _ rhs: Self) -> Bool     @warn_unused_result     func <=(_ lhs: Self, _ rhs: Self) -> Bool     @warn_unused_result     func >=(_ lhs: Self, _ rhs: Self) -> Bool     @warn_unused_result     func >(_ lhs: Self, _ rhs: Self) -> Bool } ``` |

Modified ContiguousArray [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct ContiguousArray<T> : MutableCollectionType, Sliceable, _DestructorSafeContainer {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<ContiguousArray<T>>     typealias SubSlice = ArraySlice<T>     subscript (subRange: Range<Int>) -> ArraySlice<T>     init(_ buffer: _ContiguousArrayBuffer<T>) } extension ContiguousArray : __ArrayType { } extension ContiguousArray : ArrayLiteralConvertible {     init(arrayLiteral elements: T...) } extension ContiguousArray : _ArrayType {     init()     init<S : SequenceType where T == T>(_ s: S)     init(count count: Int, repeatedValue repeatedValue: T)     init(_uninitializedCount count: Int)     var count: Int { get }     var capacity: Int { get }     var isEmpty: Bool { get }     var first: T? { get }     var last: T? { get }     mutating func reserveCapacity(_ minimumCapacity: Int)     mutating func append(_ newElement: T)     mutating func extend<S : SequenceType where T == T>(_ newElements: S)     mutating func removeLast() -> T     mutating func insert(_ newElement: T, atIndex i: Int)     mutating func removeAtIndex(_ index: Int) -> T     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     func join<S : SequenceType where ContiguousArray<T> == ContiguousArray<T>>(_ elements: S) -> ContiguousArray<T>     func reduce<U>(_ initial: U, combine combine: @noescape (U, T) -> U) -> U     mutating func sort(_ isOrderedBefore: (T, T) -> Bool)     func sorted(_ isOrderedBefore: (T, T) -> Bool) -> ContiguousArray<T>     func map<U>(_ transform: (T) -> U) -> ContiguousArray<U>     func flatMap<U>(_ transform: @noescape (T) -> ContiguousArray<U>) -> ContiguousArray<U>     func reverse() -> ContiguousArray<T>     func filter(_ includeElement: (T) -> Bool) -> ContiguousArray<T> } extension ContiguousArray : Reflectable {     func getMirror() -> MirrorType } extension ContiguousArray : Printable, DebugPrintable {     var description: String { get }     var debugDescription: String { get } } extension ContiguousArray {     func withUnsafeBufferPointer<R>(_ body: @noescape (UnsafeBufferPointer<T>) -> R) -> R     mutating func withUnsafeMutableBufferPointer<R>(_ body: @noescape (inout UnsafeMutableBufferPointer<T>) -> R) -> R } extension ContiguousArray {     mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C)     mutating func splice<S : CollectionType where T == T>(_ newElements: S, atIndex i: Int)     mutating func removeRange(_ subRange: Range<Int>) } ``` | ArrayLiteralConvertible, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable | -- |
| To | ``` struct ContiguousArray<Element> : CollectionType, Indexable, SequenceType, MutableCollectionType, MutableIndexable, _DestructorSafeContainer {     typealias T = Element     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ index: Int) -> Element     subscript (_ subRange: Range<Int>) -> ArraySlice<Element> } extension ContiguousArray : ArrayLiteralConvertible {     init(arrayLiteral elements: Element...) } extension ContiguousArray : _ArrayType, MutableSliceable, RangeReplaceableCollectionType {     init()     init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_ s: S)     init(count count: Int, repeatedValue repeatedValue: Element)     var count: Int { get }     var capacity: Int { get }     mutating func reserveCapacity(_ minimumCapacity: Int)     mutating func append(_ newElement: Element)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == Element>(_ newElements: S)     mutating func appendContentsOf<C : CollectionType where C.Generator.Element == Element>(_ newElements: C)     mutating func removeLast() -> Element     mutating func insert(_ newElement: Element, atIndex i: Int)     mutating func removeAtIndex(_ index: Int) -> Element     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     func sorted(_ isOrderedBefore: (Element, Element) -> Bool) -> ContiguousArray<Element> } extension ContiguousArray : _Reflectable { } extension ContiguousArray : CustomStringConvertible, CustomDebugStringConvertible {     var description: String { get }     var debugDescription: String { get } } extension ContiguousArray {     @rethrows func withUnsafeBufferPointer<R>(@noescape _ body: (UnsafeBufferPointer<Element>) throws -> R) rethrows -> R     @rethrows mutating func withUnsafeMutableBufferPointer<R>(@noescape _ body: (inout UnsafeMutableBufferPointer<Element>) throws -> R) rethrows -> R } extension ContiguousArray {     mutating func replaceRange<C : CollectionType where C.Generator.Element == _Buffer.Element>(_ subRange: Range<Int>, with newElements: C) } extension ContiguousArray {     mutating func popLast() -> Element? } ``` | ArrayLiteralConvertible, CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Indexable, MutableCollectionType, MutableIndexable, MutableSliceable, RangeReplaceableCollectionType, SequenceType | Element |

Modified ContiguousArray.append(_: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func append(_ newElement: T) ``` | iOS 8.0 |
| To | ``` mutating func append(_ newElement: Element) ``` | iOS 9.0 |

Modified ContiguousArray.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified ContiguousArray.init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` init<S : SequenceType where T == T>(_ s: S) ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` init<S : SequenceType where S.Generator.Element == _Buffer.Element>(_ s: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == _Buffer.Element ``` | S |

Modified ContiguousArray.init(arrayLiteral: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(arrayLiteral elements: T...) ``` | iOS 8.1 |
| To | ``` init(arrayLiteral elements: Element...) ``` | iOS 9.0 |

Modified ContiguousArray.init(count: Int, repeatedValue: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(count count: Int, repeatedValue repeatedValue: T) ``` | iOS 8.0 |
| To | ``` init(count count: Int, repeatedValue repeatedValue: Element) ``` | iOS 9.0 |

Modified ContiguousArray.insert(_: Element, atIndex: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func insert(_ newElement: T, atIndex i: Int) ``` | iOS 8.0 |
| To | ``` mutating func insert(_ newElement: Element, atIndex i: Int) ``` | iOS 9.0 |

Modified ContiguousArray.removeAll(keepCapacity: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified ContiguousArray.removeAtIndex(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func removeAtIndex(_ index: Int) -> T ``` | iOS 8.0 |
| To | ``` mutating func removeAtIndex(_ index: Int) -> Element ``` | iOS 9.0 |

Modified ContiguousArray.removeLast() -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func removeLast() -> T ``` | iOS 8.0 |
| To | ``` mutating func removeLast() -> Element ``` | iOS 9.0 |

Modified ContiguousArray.reserveCapacity(_: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified ContiguousArray.subscript(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (index: Int) -> T ``` | iOS 8.0 |
| To | ``` subscript (_ index: Int) -> Element ``` | iOS 9.0 |

Modified ContiguousArray.subscript(_: Range<Int>) -> ArraySlice<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (subRange: Range<Int>) -> ArraySlice<T> ``` | iOS 8.3 |
| To | ``` subscript (_ subRange: Range<Int>) -> ArraySlice<Element> ``` | iOS 9.0 |

Modified COpaquePointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct COpaquePointer : Equatable, Hashable, NilLiteralConvertible {     init()     init(_ v: Builtin.RawPointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<T>(_ source: UnsafePointer<T>)     init<T>(_ source: UnsafeMutablePointer<T>)     static func null() -> COpaquePointer     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } extension COpaquePointer : DebugPrintable {     var debugDescription: String { get } } extension COpaquePointer {     init<T>(_ value: CFunctionPointer<T>) } extension COpaquePointer : CVarArgType {     func encode() -> [Word] } ``` | CVarArgType, DebugPrintable, Equatable, Hashable, NilLiteralConvertible |
| To | ``` struct COpaquePointer : Equatable, Hashable, NilLiteralConvertible {     init()     init(bitPattern bitPattern: Int)     init(bitPattern bitPattern: UInt)     init<T>(_ source: UnsafePointer<T>)     init<T>(_ source: UnsafeMutablePointer<T>)     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } extension COpaquePointer : CustomDebugStringConvertible {     var debugDescription: String { get } } extension COpaquePointer : CVarArgType { } ``` | CVarArgType, CustomDebugStringConvertible, Equatable, Hashable, NilLiteralConvertible |

Modified COpaquePointer.init<T>(_: UnsafePointer<T>)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | T |

Modified COpaquePointer.init<T>(_: UnsafeMutablePointer<T>)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | T |

Modified COpaquePointer.init(bitPattern: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(bitPattern bitPattern: Word) ``` |
| To | ``` init(bitPattern bitPattern: Int) ``` |

Modified COpaquePointer.init(bitPattern: UInt)

|  | Declaration |
| --- | --- |
| From | ``` init(bitPattern bitPattern: UWord) ``` |
| To | ``` init(bitPattern bitPattern: UInt) ``` |

Modified CVaListPointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CVaListPointer {     var value: UnsafeMutablePointer<Void>     init(_fromUnsafeMutablePointer from: UnsafeMutablePointer<Void>) } extension CVaListPointer : DebugPrintable {     var debugDescription: String { get } } ``` | DebugPrintable |
| To | ``` struct CVaListPointer {     init(_fromUnsafeMutablePointer from: UnsafeMutablePointer<Void>) } extension CVaListPointer : CustomDebugStringConvertible {     var debugDescription: String { get } } ``` | CustomDebugStringConvertible |

Modified CVarArgType

|  | Declaration |
| --- | --- |
| From | ``` protocol CVarArgType {     func encode() -> [Word] } ``` |
| To | ``` protocol CVarArgType { } ``` |

Modified Dictionary [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct Dictionary<Key : Hashable, Value> : CollectionType, DictionaryLiteralConvertible {     typealias Element = (Key, Value)     typealias Index = DictionaryIndex<Key, Value>     init()     init(minimumCapacity minimumCapacity: Int)     var startIndex: DictionaryIndex<Key, Value> { get }     var endIndex: DictionaryIndex<Key, Value> { get }     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>?     subscript (position: DictionaryIndex<Key, Value>) -> (Key, Value) { get }     subscript (key: Key) -> Value?     mutating func updateValue(_ value: Value, forKey key: Key) -> Value?     mutating func removeAtIndex(_ index: DictionaryIndex<Key, Value>)     mutating func removeValueForKey(_ key: Key) -> Value?     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<Key, Value>     init(dictionaryLiteral elements: (Key, Value)...)     var isEmpty: Bool { get }     var keys: LazyForwardCollection<MapCollectionView<[Key : Value], Key>> { get }     var values: LazyForwardCollection<MapCollectionView<[Key : Value], Value>> { get } } extension Dictionary : _ObjectiveCBridgeable { } extension Dictionary : Printable, DebugPrintable {     var description: String { get }     var debugDescription: String { get } } extension Dictionary : Reflectable {     func getMirror() -> MirrorType } ``` | CollectionType, DebugPrintable, DictionaryLiteralConvertible, Printable, Reflectable | ```  ``` | -- |
| To | ``` struct Dictionary<Key : Hashable, Value> : CollectionType, Indexable, SequenceType, DictionaryLiteralConvertible {     typealias Element = (Key, Value)     typealias Index = DictionaryIndex<Key, Value>     init()     init(minimumCapacity minimumCapacity: Int)     var startIndex: DictionaryIndex<Key, Value> { get }     var endIndex: DictionaryIndex<Key, Value> { get }     @warn_unused_result     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>?     subscript (_ position: DictionaryIndex<Key, Value>) -> (Key, Value) { get }     subscript (_ key: Key) -> Value?     mutating func updateValue(_ value: Value, forKey key: Key) -> Value?     mutating func removeAtIndex(_ index: DictionaryIndex<Key, Value>) -> (Key, Value)     mutating func removeValueForKey(_ key: Key) -> Value?     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<Key, Value>     init(dictionaryLiteral elements: (Key, Value)...)     var keys: LazyMapCollection<[Key : Value], Key> { get }     var values: LazyMapCollection<[Key : Value], Value> { get }     var isEmpty: Bool { get } } extension Dictionary : _ObjectiveCBridgeable { } extension Dictionary : CustomStringConvertible, CustomDebugStringConvertible {     var description: String { get }     var debugDescription: String { get } } extension Dictionary : _Reflectable { } extension Dictionary {     mutating func popFirst() -> (Key, Value)? } ``` | CollectionType, CustomDebugStringConvertible, CustomStringConvertible, DictionaryLiteralConvertible, Indexable, SequenceType | ``` Key : Hashable ``` | Key, Value |

Modified Dictionary.endIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Dictionary.generate() -> DictionaryGenerator<Key, Value>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Dictionary.indexForKey(_: Key) -> DictionaryIndex<Key, Value>?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>? ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>? ``` | iOS 9.0 |

Modified Dictionary.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified Dictionary.init(dictionaryLiteral: (Key, Value))

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified Dictionary.init(minimumCapacity: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Dictionary.removeAll(keepCapacity: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Dictionary.removeValueForKey(_: Key) -> Value?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Dictionary.startIndex

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Dictionary.subscript(_: DictionaryIndex<Key, Value>) -> (Key, Value)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (position: DictionaryIndex<Key, Value>) -> (Key, Value) { get } ``` | iOS 8.0 |
| To | ``` subscript (_ position: DictionaryIndex<Key, Value>) -> (Key, Value) { get } ``` | iOS 9.0 |

Modified Dictionary.subscript(_: Key) -> Value?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (key: Key) -> Value? ``` | iOS 8.0 |
| To | ``` subscript (_ key: Key) -> Value? ``` | iOS 9.0 |

Modified Dictionary.updateValue(_: Value, forKey: Key) -> Value?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified DictionaryGenerator [struct]

|  | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- |
| From | ```  ``` | -- |
| To | ``` Key : Hashable ``` | Key, Value |

Modified DictionaryGenerator.next() -> (Key, Value)?

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified DictionaryIndex [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct DictionaryIndex<Key : Hashable, Value> : ForwardIndexType, Comparable {     typealias Index = DictionaryIndex<Key, Value>     func successor() -> DictionaryIndex<Key, Value> } ``` | Comparable, ForwardIndexType | ```  ``` | -- |
| To | ``` struct DictionaryIndex<Key : Hashable, Value> : ForwardIndexType, _Incrementable, Equatable, Comparable {     func successor() -> DictionaryIndex<Key, Value> } ``` | Comparable, Equatable, ForwardIndexType | ``` Key : Hashable ``` | Key, Value |

Modified DictionaryIndex.successor() -> DictionaryIndex<Key, Value>

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified DictionaryLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol DictionaryLiteralConvertible {     typealias Key     typealias Value     init(dictionaryLiteral elements: (Key, Value)...) } ``` |
| To | ``` protocol DictionaryLiteralConvertible {     typealias Key     typealias Value     init(dictionaryLiteral elements: (Self.Key, Self.Value)...) } ``` |

Modified DictionaryLiteralConvertible.init(dictionaryLiteral: (Self.Key, Self.Value))

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(dictionaryLiteral elements: (Key, Value)...) ``` | iOS 8.1 |
| To | ``` init(dictionaryLiteral elements: (Self.Key, Self.Value)...) ``` | iOS 9.0 |

Modified [Double [struct]](https://developer.apple.com/documentation/swift/double)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Double {     var value: Builtin.FPIEEE64     init()     init(_bits v: Builtin.FPIEEE64)     init(_ value: Double) } extension Double {     init(_ value: CGFloat) } extension Double : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Double : Printable {     var description: String { get } } extension Double : FloatingPointType {     static var infinity: Double { get }     static var NaN: Double { get }     static var quietNaN: Double { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Double {     var floatingPointClass: FloatingPointClassification { get } } extension Double : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Double {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Double : FloatLiteralConvertible {     init(floatLiteral value: Double) } extension Double : Comparable { } extension Double : Hashable {     var hashValue: Int { get } } extension Double : AbsoluteValuable {     static func abs(_ x: Double) -> Double } extension Double {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Double {     init(_ other: Float) } extension Double : Strideable {     func distanceTo(_ other: Double) -> Double     func advancedBy(_ amount: Double) -> Double } extension Double : Reflectable {     func getMirror() -> MirrorType } extension Double : _CVarArgPassedAsDouble {     func encode() -> [Word] } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |
| To | ``` struct Double {     var value: Builtin.FPIEEE64     init()     init(_bits v: Builtin.FPIEEE64)     init(_ value: Double) } extension Double {     init(_ value: CGFloat) } extension Double : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Double : CustomStringConvertible {     var description: String { get } } extension Double : FloatingPointType {     static var infinity: Double { get }     static var NaN: Double { get }     static var quietNaN: Double { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Double {     var floatingPointClass: FloatingPointClassification { get } } extension Double : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Double {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Double : FloatLiteralConvertible {     init(floatLiteral value: Double) } extension Double : Comparable, Equatable { } extension Double : Hashable {     var hashValue: Int { get } } extension Double : SignedNumberType, AbsoluteValuable {     @warn_unused_result     static func abs(_ x: Double) -> Double } extension Double {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Double {     init(_ other: Float) } extension Double : Strideable, _Strideable {     func distanceTo(_ other: Double) -> Double     func advancedBy(_ amount: Double) -> Double } extension Double {     init?(_ text: String) } extension Double : _Reflectable { } extension Double : _CVarArgPassedAsDouble, CVarArgType, _CVarArgAlignedType { } ``` | AbsoluteValuable, CVarArgType, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, SignedNumberType, Strideable |

Modified Double.abs(_: Double) -> Double [static]

|  | Declaration |
| --- | --- |
| From | ``` static func abs(_ x: Double) -> Double ``` |
| To | ``` @warn_unused_result     static func abs(_ x: Double) -> Double ``` |

Modified EmptyCollection [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct EmptyCollection<T> : CollectionType {     typealias Index = Int     init()     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> EmptyGenerator<T>     subscript (position: Index) -> T { get } } extension EmptyCollection : Reflectable {     func getMirror() -> MirrorType } ``` | CollectionType, Reflectable | -- |
| To | ``` struct EmptyCollection<Element> : CollectionType, Indexable, SequenceType {     typealias T = Element     typealias Index = Int     init()     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> EmptyGenerator<Element>     subscript (_ position: Index) -> Element { get }     var count: Int { get } } extension EmptyCollection : _Reflectable { } ``` | CollectionType, Indexable, SequenceType | Element |

Modified EmptyCollection.generate() -> EmptyGenerator<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> EmptyGenerator<T> ``` | iOS 8.0 |
| To | ``` func generate() -> EmptyGenerator<Element> ``` | iOS 9.0 |

Modified EmptyCollection.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified EmptyCollection.subscript(_: Index) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (position: Index) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ position: Index) -> Element { get } ``` | iOS 9.0 |

Modified EmptyGenerator [struct]

|  | Declaration | Generics[Parameters] |
| --- | --- | --- |
| From | ``` struct EmptyGenerator<T> : GeneratorType, SequenceType {     init()     func generate() -> EmptyGenerator<T>     mutating func next() -> T? } ``` | -- |
| To | ``` struct EmptyGenerator<Element> : GeneratorType, SequenceType {     typealias T = Element     init()     mutating func next() -> Element? } ``` | Element |

Modified EmptyGenerator.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified EmptyGenerator.next() -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> T? ``` | iOS 8.0 |
| To | ``` mutating func next() -> Element? ``` | iOS 9.0 |

Modified EnumerateGenerator [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct EnumerateGenerator<Base : GeneratorType> : GeneratorType, SequenceType {     typealias Element = (index: Int, element: Base.Element)     var base: Base     var count: Int     init(_ base: Base)     mutating func next() -> Element?     typealias Generator = EnumerateGenerator<Base>     func generate() -> EnumerateGenerator<Base> } ``` | ```  ``` | -- |
| To | ``` struct EnumerateGenerator<Base : GeneratorType> : GeneratorType, SequenceType {     typealias Element = (index: Int, element: Base.Element)     init(_ base: Base)     mutating func next() -> (index: Int, element: Base.Element)? } ``` | ``` Base : GeneratorType ``` | Base |

Modified EnumerateGenerator.init(_: Base)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified EnumerateGenerator.next() -> (index: Int, element: Base.Element)?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> Element? ``` | iOS 8.0 |
| To | ``` mutating func next() -> (index: Int, element: Base.Element)? ``` | iOS 9.0 |

Modified EnumerateSequence [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct EnumerateSequence<Base : SequenceType> : SequenceType {     var base: Base     init(_ base: Base)     func generate() -> EnumerateGenerator<Base.Generator> } ``` | ```  ``` | -- |
| To | ``` struct EnumerateSequence<Base : SequenceType> : SequenceType {     init(_ base: Base)     func generate() -> EnumerateGenerator<Base.Generator> } ``` | ``` Base : SequenceType ``` | Base |

Modified EnumerateSequence.generate() -> EnumerateGenerator<Base.Generator>

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified EnumerateSequence.init(_: Base)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified Equatable

|  | Declaration |
| --- | --- |
| From | ``` protocol Equatable {     func ==(_ lhs: Self, _ rhs: Self) -> Bool } ``` |
| To | ``` protocol Equatable {     @warn_unused_result     func ==(_ lhs: Self, _ rhs: Self) -> Bool } ``` |

Modified ExtendedGraphemeClusterLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol ExtendedGraphemeClusterLiteralConvertible : UnicodeScalarLiteralConvertible {     typealias ExtendedGraphemeClusterLiteralType     init(extendedGraphemeClusterLiteral value: ExtendedGraphemeClusterLiteralType) } ``` |
| To | ``` protocol ExtendedGraphemeClusterLiteralConvertible : UnicodeScalarLiteralConvertible {     typealias ExtendedGraphemeClusterLiteralType     init(extendedGraphemeClusterLiteral value: Self.ExtendedGraphemeClusterLiteralType) } ``` |

Modified ExtendedGraphemeClusterLiteralConvertible.init(extendedGraphemeClusterLiteral: Self.ExtendedGraphemeClusterLiteralType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(extendedGraphemeClusterLiteral value: ExtendedGraphemeClusterLiteralType) ``` | iOS 8.1 |
| To | ``` init(extendedGraphemeClusterLiteral value: Self.ExtendedGraphemeClusterLiteralType) ``` | iOS 9.0 |

Modified [Float [struct]](https://developer.apple.com/documentation/swift/float)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Float {     var value: Builtin.FPIEEE32     init()     init(_bits v: Builtin.FPIEEE32)     init(_ value: Float) } extension Float {     init(_ value: CGFloat) } extension Float : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Float : Printable {     var description: String { get } } extension Float : FloatingPointType {     static var infinity: Float { get }     static var NaN: Float { get }     static var quietNaN: Float { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Float {     var floatingPointClass: FloatingPointClassification { get } } extension Float : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Float {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Float : FloatLiteralConvertible {     init(floatLiteral value: Float) } extension Float : Comparable { } extension Float : Hashable {     var hashValue: Int { get } } extension Float : AbsoluteValuable {     static func abs(_ x: Float) -> Float } extension Float {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Float {     init(_ other: Double) } extension Float : Strideable {     func distanceTo(_ other: Float) -> Float     func advancedBy(_ amount: Float) -> Float } extension Float : Reflectable {     func getMirror() -> MirrorType } extension Float : _CVarArgPassedAsDouble {     func encode() -> [Word] } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |
| To | ``` struct Float {     var value: Builtin.FPIEEE32     init()     init(_bits v: Builtin.FPIEEE32)     init(_ value: Float) } extension Float {     init(_ value: CGFloat) } extension Float : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Float : CustomStringConvertible {     var description: String { get } } extension Float : FloatingPointType {     static var infinity: Float { get }     static var NaN: Float { get }     static var quietNaN: Float { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } extension Float {     var floatingPointClass: FloatingPointClassification { get } } extension Float : IntegerLiteralConvertible {     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64) } extension Float {     init(_builtinFloatLiteral value: Builtin.FPIEEE64) } extension Float : FloatLiteralConvertible {     init(floatLiteral value: Float) } extension Float : Comparable, Equatable { } extension Float : Hashable {     var hashValue: Int { get } } extension Float : SignedNumberType, AbsoluteValuable {     @warn_unused_result     static func abs(_ x: Float) -> Float } extension Float {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int) } extension Float {     init(_ other: Double) } extension Float : Strideable, _Strideable {     func distanceTo(_ other: Float) -> Float     func advancedBy(_ amount: Float) -> Float } extension Float {     init?(_ text: String) } extension Float : _Reflectable { } extension Float : _CVarArgPassedAsDouble, CVarArgType, _CVarArgAlignedType { } ``` | AbsoluteValuable, CVarArgType, Comparable, CustomStringConvertible, Equatable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, SignedNumberType, Strideable |

Modified Float.abs(_: Float) -> Float [static]

|  | Declaration |
| --- | --- |
| From | ``` static func abs(_ x: Float) -> Float ``` |
| To | ``` @warn_unused_result     static func abs(_ x: Float) -> Float ``` |

Modified FloatingPointType

|  | Declaration |
| --- | --- |
| From | ``` protocol FloatingPointType : Strideable {     typealias _BitsType     static func _fromBitPattern(_ bits: _BitsType) -> Self     func _toBitPattern() -> _BitsType     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     static var infinity: Self { get }     static var NaN: Self { get }     static var quietNaN: Self { get }     var floatingPointClass: FloatingPointClassification { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } ``` |
| To | ``` protocol FloatingPointType : Strideable {     init(_ value: UInt8)     init(_ value: Int8)     init(_ value: UInt16)     init(_ value: Int16)     init(_ value: UInt32)     init(_ value: Int32)     init(_ value: UInt64)     init(_ value: Int64)     init(_ value: UInt)     init(_ value: Int)     static var infinity: Self { get }     static var NaN: Self { get }     static var quietNaN: Self { get }     var floatingPointClass: FloatingPointClassification { get }     var isSignMinus: Bool { get }     var isNormal: Bool { get }     var isFinite: Bool { get }     var isZero: Bool { get }     var isSubnormal: Bool { get }     var isInfinite: Bool { get }     var isNaN: Bool { get }     var isSignaling: Bool { get } } ``` |

Modified FloatingPointType.infinity

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: Int64)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: UInt32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: Int16)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: UInt64)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: UInt8)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: Int8)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: UInt)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: Int32)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.init(_: UInt16)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified FloatingPointType.NaN

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified FloatingPointType.quietNaN

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified FloatLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol FloatLiteralConvertible {     typealias FloatLiteralType     init(floatLiteral value: FloatLiteralType) } ``` |
| To | ``` protocol FloatLiteralConvertible {     typealias FloatLiteralType     init(floatLiteral value: Self.FloatLiteralType) } ``` |

Modified FloatLiteralConvertible.init(floatLiteral: Self.FloatLiteralType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(floatLiteral value: FloatLiteralType) ``` | iOS 8.1 |
| To | ``` init(floatLiteral value: Self.FloatLiteralType) ``` | iOS 9.0 |

Modified ForwardIndexType

|  | Declaration |
| --- | --- |
| From | ``` protocol ForwardIndexType : _ForwardIndexType { } ``` |
| To | ``` protocol ForwardIndexType : _Incrementable {     typealias Distance : _SignedIntegerType = Int     @warn_unused_result     func advancedBy(_ n: Self.Distance) -> Self     @warn_unused_result     func advancedBy(_ n: Self.Distance, limit limit: Self) -> Self     @warn_unused_result     func distanceTo(_ end: Self) -> Self.Distance } ``` |

Modified GeneratorOfOne [struct]

|  | Declaration | Generics[Parameters] |
| --- | --- | --- |
| From | ``` struct GeneratorOfOne<T> : GeneratorType, SequenceType {     init(_ element: T?)     func generate() -> GeneratorOfOne<T>     mutating func next() -> T?     var elements: T? } ``` | -- |
| To | ``` struct GeneratorOfOne<Element> : GeneratorType, SequenceType {     typealias T = Element     init(_ element: Element?)     mutating func next() -> Element? } ``` | Element |

Modified GeneratorOfOne.init(_: Element?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ element: T?) ``` | iOS 8.0 |
| To | ``` init(_ element: Element?) ``` | iOS 9.0 |

Modified GeneratorOfOne.next() -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> T? ``` | iOS 8.0 |
| To | ``` mutating func next() -> Element? ``` | iOS 9.0 |

Modified GeneratorSequence [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct GeneratorSequence<G : GeneratorType> : GeneratorType, SequenceType {     init(_ base: G)     mutating func next() -> G.Element?     func generate() -> GeneratorSequence<G> } ``` | ```  ``` | -- |
| To | ``` struct GeneratorSequence<Base : GeneratorType> : GeneratorType, SequenceType {     typealias G = Base     init(_ base: Base)     mutating func next() -> Base.Element? } ``` | ``` Base : GeneratorType ``` | Base |

Modified GeneratorSequence.init(_: Base)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ base: G) ``` | iOS 8.0 |
| To | ``` init(_ base: Base) ``` | iOS 9.0 |

Modified GeneratorSequence.next() -> Base.Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> G.Element? ``` | iOS 8.0 |
| To | ``` mutating func next() -> Base.Element? ``` | iOS 9.0 |

Modified GeneratorType

|  | Declaration |
| --- | --- |
| From | ``` protocol GeneratorType {     typealias Element     mutating func next() -> Element? } ``` |
| To | ``` protocol GeneratorType {     typealias Element     @warn_unused_result     mutating func next() -> Self.Element? } ``` |

Modified GeneratorType.next() -> Self.Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> Element? ``` | iOS 8.0 |
| To | ``` @warn_unused_result     mutating func next() -> Self.Element? ``` | iOS 9.0 |

Modified HalfOpenInterval [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct HalfOpenInterval<T : Comparable> : IntervalType, Equatable, Printable, DebugPrintable, Reflectable {     typealias Bound = T     init(_ x: HalfOpenInterval<T>)     init(_ start: T, _ end: T)     var start: T { get }     var end: T { get }     var description: String { get }     var debugDescription: String { get }     func contains(_ x: T) -> Bool     func clamp(_ intervalToClamp: HalfOpenInterval<T>) -> HalfOpenInterval<T>     func getMirror() -> MirrorType } extension HalfOpenInterval {     var isEmpty: Bool { get } } ``` | DebugPrintable, Equatable, IntervalType, Printable, Reflectable | ```  ``` | -- |
| To | ``` struct HalfOpenInterval<Bound : Comparable> : IntervalType, Equatable, CustomStringConvertible, CustomDebugStringConvertible, _Reflectable {     typealias T = Bound     init(_ x: HalfOpenInterval<Bound>)     init(_ start: Bound, _ end: Bound)     var start: Bound { get }     var end: Bound { get }     var description: String { get }     var debugDescription: String { get }     @warn_unused_result     func contains(_ x: Bound) -> Bool     @warn_unused_result     func clamp(_ intervalToClamp: HalfOpenInterval<Bound>) -> HalfOpenInterval<Bound> } extension HalfOpenInterval {     var isEmpty: Bool { get } } ``` | CustomDebugStringConvertible, CustomStringConvertible, Equatable, IntervalType | ``` Bound : Comparable ``` | Bound |

Modified HalfOpenInterval.clamp(_: HalfOpenInterval<Bound>) -> HalfOpenInterval<Bound>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clamp(_ intervalToClamp: HalfOpenInterval<T>) -> HalfOpenInterval<T> ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func clamp(_ intervalToClamp: HalfOpenInterval<Bound>) -> HalfOpenInterval<Bound> ``` | iOS 9.0 |

Modified HalfOpenInterval.contains(_: Bound) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contains(_ x: T) -> Bool ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func contains(_ x: Bound) -> Bool ``` | iOS 9.0 |

Modified HalfOpenInterval.end

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var end: T { get } ``` | iOS 8.0 |
| To | ``` var end: Bound { get } ``` | iOS 9.0 |

Modified HalfOpenInterval.init(_: HalfOpenInterval<Bound>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ x: HalfOpenInterval<T>) ``` | iOS 8.0 |
| To | ``` init(_ x: HalfOpenInterval<Bound>) ``` | iOS 9.0 |

Modified HalfOpenInterval.init(_: Bound, _: Bound)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ start: T, _ end: T) ``` | iOS 8.0 |
| To | ``` init(_ start: Bound, _ end: Bound) ``` | iOS 9.0 |

Modified HalfOpenInterval.start

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var start: T { get } ``` | iOS 8.0 |
| To | ``` var start: Bound { get } ``` | iOS 9.0 |

Modified ImplicitlyUnwrappedOptional [enum]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` enum ImplicitlyUnwrappedOptional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     init(_ v: T?)     init(nilLiteral nilLiteral: ())     func map<U>(_ f: @noescape (T) -> U) -> U!     func flatMap<U>(_ f: @noescape (T) -> U!) -> U!     func getMirror() -> MirrorType } extension ImplicitlyUnwrappedOptional : Printable {     var description: String { get } } extension ImplicitlyUnwrappedOptional : _ObjectiveCBridgeable { } ``` | NilLiteralConvertible, Printable, Reflectable | -- |
| To | ``` enum ImplicitlyUnwrappedOptional<Wrapped> : _Reflectable, NilLiteralConvertible {     case None     case Some(Wrapped)     typealias T = Wrapped     init()     init(_ some: Wrapped)     init(_ v: Wrapped?)     init(nilLiteral nilLiteral: ())     @warn_unused_result     @rethrows func map<U>(@noescape _ f: (Wrapped) throws -> U) rethrows -> U!     @warn_unused_result     @rethrows func flatMap<U>(@noescape _ f: (Wrapped) throws -> U!) rethrows -> U! } extension ImplicitlyUnwrappedOptional : CustomStringConvertible {     var description: String { get } } extension ImplicitlyUnwrappedOptional : _ObjectiveCBridgeable { } ``` | CustomStringConvertible, NilLiteralConvertible | Wrapped |

Modified ImplicitlyUnwrappedOptional.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified ImplicitlyUnwrappedOptional.init(_: Wrapped?)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ v: T?) ``` | iOS 8.0 |
| To | ``` init(_ v: Wrapped?) ``` | iOS 9.0 |

Modified ImplicitlyUnwrappedOptional.init(_: Wrapped)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ some: T) ``` | iOS 8.0 |
| To | ``` init(_ some: Wrapped) ``` | iOS 9.0 |

Modified ImplicitlyUnwrappedOptional.init(nilLiteral: ())

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified ImplicitlyUnwrappedOptional.None

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified ImplicitlyUnwrappedOptional.Some

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Some(T) ``` | iOS 8.0 |
| To | ``` case Some(Wrapped) ``` | iOS 9.0 |

Modified Index.init(_: UTF8Index, within: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified Index.init(_: UTF16Index, within: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified Index.init(_: UnicodeScalarIndex, within: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified Index.samePositionIn(_: String.UTF16View) -> String.UTF16View.Index

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index ``` | iOS 9.0 |

Modified Index.samePositionIn(_: String.UnicodeScalarView) -> String.UnicodeScalarView.Index

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> String.UnicodeScalarView.Index ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> String.UnicodeScalarView.Index ``` | iOS 9.0 |

Modified Index.samePositionIn(_: String.UTF8View) -> String.UTF8View.Index

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index ``` | iOS 9.0 |

Modified IndexingGenerator [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct IndexingGenerator<C : _CollectionType> : GeneratorType, SequenceType {     init(_ seq: C)     func generate() -> IndexingGenerator<C>     mutating func next() -> C._Element? } ``` | ```  ``` | -- |
| To | ``` struct IndexingGenerator<Elements : Indexable> : GeneratorType, SequenceType {     init(_ elements: Elements)     mutating func next() -> Elements._Element? } ``` | ``` Elements : Indexable ``` | Elements |

Modified [Int [struct]](https://developer.apple.com/documentation/swift/int)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int : SignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } extension Int {     init(_ value: CGFloat) } extension Int : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Int : Hashable {     var hashValue: Int { get } } extension Int : Printable {     var description: String { get } } extension Int : RandomAccessIndexType {     func successor() -> Int     func predecessor() -> Int     func distanceTo(_ other: Int) -> Distance     func advancedBy(_ amount: Distance) -> Int } extension Int {     static func addWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func divideWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     func toIntMax() -> IntMax } extension Int : SignedNumberType { } extension Int {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(bitPattern bitPattern: UInt) } extension Int : BitwiseOperationsType {     static var allZeros: Int { get } } extension Int {     init(_ other: Float)     init(_ other: Double) } extension Int : Reflectable {     func getMirror() -> MirrorType } extension Int : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |
| To | ``` struct Int : Equatable, _SignedIntegerType, Comparable, _IntegerType, IntegerArithmeticType, _IntegerArithmeticType, IntegerType, SignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } extension Int {     init(_ value: CGFloat) } extension Int : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension Int : ForwardIndexType, _Incrementable, RandomAccessIndexType, BidirectionalIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> Int     func predecessor() -> Int     func distanceTo(_ other: Int) -> Distance     func advancedBy(_ n: Distance) -> Int } extension Int : Hashable {     var hashValue: Int { get } } extension Int : CustomStringConvertible {     var description: String { get } } extension Int {     static func addWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func divideWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int, _ rhs: Int) -> (Int, overflow: Bool)     func toIntMax() -> IntMax } extension Int : SignedNumberType, IntegerLiteralConvertible { } extension Int {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(bitPattern bitPattern: UInt) } extension Int : BitwiseOperationsType {     static var allZeros: Int { get } } extension Int {     init(_ other: Float)     init(_ other: Double) } extension Int {     init?(_ text: String, radix radix: Int = default) } extension Int : _Reflectable { } extension Int : MirrorPathType { } extension Int : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, MirrorPathType, RandomAccessIndexType, SignedIntegerType, SignedNumberType, Strideable |

Modified Int16 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int16 : SignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int16)     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } extension Int16 {     init(_ value: CGFloat) } extension Int16 : Hashable {     var hashValue: Int { get } } extension Int16 : Printable {     var description: String { get } } extension Int16 : RandomAccessIndexType {     func successor() -> Int16     func predecessor() -> Int16     func distanceTo(_ other: Int16) -> Distance     func advancedBy(_ amount: Distance) -> Int16 } extension Int16 {     static func addWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func divideWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     func toIntMax() -> IntMax } extension Int16 : SignedNumberType { } extension Int16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt16) } extension Int16 : BitwiseOperationsType {     static var allZeros: Int16 { get } } extension Int16 {     init(_ other: Float)     init(_ other: Double) } extension Int16 : Reflectable {     func getMirror() -> MirrorType } extension Int16 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |
| To | ``` struct Int16 : _IntegerArithmeticType, Comparable, Equatable, _SignedIntegerType, _IntegerType, IntegerArithmeticType, IntegerType, SignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int16)     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } extension Int16 {     init(_ value: CGFloat) } extension Int16 : Hashable {     var hashValue: Int { get } } extension Int16 : CustomStringConvertible {     var description: String { get } } extension Int16 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> Int16     func predecessor() -> Int16     func distanceTo(_ other: Int16) -> Distance     func advancedBy(_ n: Distance) -> Int16 } extension Int16 {     static func addWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func divideWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int16, _ rhs: Int16) -> (Int16, overflow: Bool)     func toIntMax() -> IntMax } extension Int16 : SignedNumberType, IntegerLiteralConvertible { } extension Int16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt16) } extension Int16 : BitwiseOperationsType {     static var allZeros: Int16 { get } } extension Int16 {     init(_ other: Float)     init(_ other: Double) } extension Int16 {     init?(_ text: String, radix radix: Int = default) } extension Int16 : _Reflectable { } extension Int16 : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, SignedIntegerType, SignedNumberType, Strideable |

Modified Int32 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int32 : SignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int32)     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } extension Int32 {     init(_ value: CGFloat) } extension Int32 : Hashable {     var hashValue: Int { get } } extension Int32 : Printable {     var description: String { get } } extension Int32 : RandomAccessIndexType {     func successor() -> Int32     func predecessor() -> Int32     func distanceTo(_ other: Int32) -> Distance     func advancedBy(_ amount: Distance) -> Int32 } extension Int32 {     static func addWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func divideWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     func toIntMax() -> IntMax } extension Int32 : SignedNumberType { } extension Int32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt32) } extension Int32 : BitwiseOperationsType {     static var allZeros: Int32 { get } } extension Int32 {     init(_ other: Float)     init(_ other: Double) } extension Int32 : Reflectable {     func getMirror() -> MirrorType } extension Int32 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |
| To | ``` struct Int32 : _IntegerArithmeticType, Comparable, Equatable, _SignedIntegerType, _IntegerType, IntegerArithmeticType, IntegerType, SignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int32)     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } extension Int32 {     init(_ value: CGFloat) } extension Int32 : Hashable {     var hashValue: Int { get } } extension Int32 : CustomStringConvertible {     var description: String { get } } extension Int32 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> Int32     func predecessor() -> Int32     func distanceTo(_ other: Int32) -> Distance     func advancedBy(_ n: Distance) -> Int32 } extension Int32 {     static func addWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func divideWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int32, _ rhs: Int32) -> (Int32, overflow: Bool)     func toIntMax() -> IntMax } extension Int32 : SignedNumberType, IntegerLiteralConvertible { } extension Int32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt32) } extension Int32 : BitwiseOperationsType {     static var allZeros: Int32 { get } } extension Int32 {     init(_ other: Float)     init(_ other: Double) } extension Int32 {     init?(_ text: String, radix radix: Int = default) } extension Int32 : _Reflectable { } extension Int32 : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, SignedIntegerType, SignedNumberType, Strideable |

Modified Int64 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int64 : SignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64)     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } extension Int64 {     init(_ value: CGFloat) } extension Int64 : Hashable {     var hashValue: Int { get } } extension Int64 : Printable {     var description: String { get } } extension Int64 : RandomAccessIndexType {     func successor() -> Int64     func predecessor() -> Int64     func distanceTo(_ other: Int64) -> Distance     func advancedBy(_ amount: Distance) -> Int64 } extension Int64 {     static func addWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func divideWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     func toIntMax() -> IntMax } extension Int64 : SignedNumberType { } extension Int64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: UInt64) } extension Int64 : BitwiseOperationsType {     static var allZeros: Int64 { get } } extension Int64 {     init(_ other: Float)     init(_ other: Double) } extension Int64 : Reflectable {     func getMirror() -> MirrorType } extension Int64 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |
| To | ``` struct Int64 : _SignedIntegerType, Comparable, Equatable, _IntegerType, IntegerArithmeticType, _IntegerArithmeticType, IntegerType, SignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64)     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } extension Int64 {     init(_ value: CGFloat) } extension Int64 : Hashable {     var hashValue: Int { get } } extension Int64 : CustomStringConvertible {     var description: String { get } } extension Int64 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> Int64     func predecessor() -> Int64     func distanceTo(_ other: Int64) -> Distance     func advancedBy(_ n: Distance) -> Int64 } extension Int64 {     static func addWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func divideWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int64, _ rhs: Int64) -> (Int64, overflow: Bool)     func toIntMax() -> IntMax } extension Int64 : SignedNumberType, IntegerLiteralConvertible { } extension Int64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: UInt64) } extension Int64 : BitwiseOperationsType {     static var allZeros: Int64 { get } } extension Int64 {     init(_ other: Float)     init(_ other: Double) } extension Int64 {     init?(_ text: String, radix radix: Int = default) } extension Int64 : _Reflectable { } extension Int64 : CVarArgType, _CVarArgAlignedType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, SignedIntegerType, SignedNumberType, Strideable |

Modified Int8 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int8 : SignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: Int8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int8)     static var max: Int8 { get }     static var min: Int8 { get } } extension Int8 {     init(_ value: CGFloat) } extension Int8 : Hashable {     var hashValue: Int { get } } extension Int8 : Printable {     var description: String { get } } extension Int8 : RandomAccessIndexType {     func successor() -> Int8     func predecessor() -> Int8     func distanceTo(_ other: Int8) -> Distance     func advancedBy(_ amount: Distance) -> Int8 } extension Int8 {     static func addWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func divideWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     func toIntMax() -> IntMax } extension Int8 : SignedNumberType { } extension Int8 {     init(_ v: UInt8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt8) } extension Int8 : BitwiseOperationsType {     static var allZeros: Int8 { get } } extension Int8 {     init(_ other: Float)     init(_ other: Double) } extension Int8 : Reflectable {     func getMirror() -> MirrorType } extension Int8 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |
| To | ``` struct Int8 : _IntegerArithmeticType, Comparable, Equatable, _SignedIntegerType, _IntegerType, IntegerArithmeticType, IntegerType, SignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: Int8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int8)     static var max: Int8 { get }     static var min: Int8 { get } } extension Int8 {     init(_ value: CGFloat) } extension Int8 : Hashable {     var hashValue: Int { get } } extension Int8 : CustomStringConvertible {     var description: String { get } } extension Int8 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> Int8     func predecessor() -> Int8     func distanceTo(_ other: Int8) -> Distance     func advancedBy(_ n: Distance) -> Int8 } extension Int8 {     static func addWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func subtractWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func divideWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     static func remainderWithOverflow(_ lhs: Int8, _ rhs: Int8) -> (Int8, overflow: Bool)     func toIntMax() -> IntMax } extension Int8 : SignedNumberType, IntegerLiteralConvertible { } extension Int8 {     init(_ v: UInt8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: UInt8) } extension Int8 : BitwiseOperationsType {     static var allZeros: Int8 { get } } extension Int8 {     init(_ other: Float)     init(_ other: Double) } extension Int8 {     init?(_ text: String, radix radix: Int = default) } extension Int8 : _Reflectable { } extension Int8 : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, SignedIntegerType, SignedNumberType, Strideable |

Modified IntegerArithmeticType

|  | Declaration |
| --- | --- |
| From | ``` protocol IntegerArithmeticType : _IntegerArithmeticType, Comparable {     func +(_ lhs: Self, _ rhs: Self) -> Self     func -(_ lhs: Self, _ rhs: Self) -> Self     func *(_ lhs: Self, _ rhs: Self) -> Self     func /(_ lhs: Self, _ rhs: Self) -> Self     func %(_ lhs: Self, _ rhs: Self) -> Self     func toIntMax() -> IntMax } ``` |
| To | ``` protocol IntegerArithmeticType : _IntegerArithmeticType, Comparable {     @warn_unused_result     func +(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     func -(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     func *(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     func /(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     func %(_ lhs: Self, _ rhs: Self) -> Self     @warn_unused_result     func toIntMax() -> IntMax } ``` |

Modified IntegerArithmeticType.addWithOverflow(_: Self, _: Self) -> (Self, overflow: Bool) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified IntegerArithmeticType.divideWithOverflow(_: Self, _: Self) -> (Self, overflow: Bool) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified IntegerArithmeticType.multiplyWithOverflow(_: Self, _: Self) -> (Self, overflow: Bool) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified IntegerArithmeticType.remainderWithOverflow(_: Self, _: Self) -> (Self, overflow: Bool) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified IntegerArithmeticType.subtractWithOverflow(_: Self, _: Self) -> (Self, overflow: Bool) [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified IntegerArithmeticType.toIntMax() -> IntMax

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func toIntMax() -> IntMax ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func toIntMax() -> IntMax ``` | iOS 9.0 |

Modified IntegerLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol IntegerLiteralConvertible {     typealias IntegerLiteralType     init(integerLiteral value: IntegerLiteralType) } ``` |
| To | ``` protocol IntegerLiteralConvertible {     typealias IntegerLiteralType     init(integerLiteral value: Self.IntegerLiteralType) } ``` |

Modified IntegerLiteralConvertible.init(integerLiteral: Self.IntegerLiteralType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(integerLiteral value: IntegerLiteralType) ``` | iOS 8.1 |
| To | ``` init(integerLiteral value: Self.IntegerLiteralType) ``` | iOS 9.0 |

Modified IntervalType

|  | Declaration |
| --- | --- |
| From | ``` protocol IntervalType {     typealias Bound : Comparable     func contains(_ value: Bound) -> Bool     func clamp(_ intervalToClamp: Self) -> Self     var isEmpty: Bool { get }     var start: Bound { get }     var end: Bound { get } } ``` |
| To | ``` protocol IntervalType {     typealias Bound : Comparable     @warn_unused_result     func contains(_ value: Self.Bound) -> Bool     @warn_unused_result     func clamp(_ intervalToClamp: Self) -> Self     var isEmpty: Bool { get }     var start: Self.Bound { get }     var end: Self.Bound { get } } ``` |

Modified IntervalType.clamp(_: Self) -> Self

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func clamp(_ intervalToClamp: Self) -> Self ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func clamp(_ intervalToClamp: Self) -> Self ``` | iOS 9.0 |

Modified IntervalType.contains(_: Self.Bound) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contains(_ value: Bound) -> Bool ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func contains(_ value: Self.Bound) -> Bool ``` | iOS 9.0 |

Modified IntervalType.end

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var end: Bound { get } ``` | iOS 8.0 |
| To | ``` var end: Self.Bound { get } ``` | iOS 9.0 |

Modified IntervalType.start

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var start: Bound { get } ``` | iOS 8.0 |
| To | ``` var start: Self.Bound { get } ``` | iOS 9.0 |

Modified LazySequence [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct LazySequence<S : SequenceType> : SequenceType {     init(_ base: S)     func generate() -> S.Generator     var array: [S.Generator.Element] { get } } extension LazySequence {     func filter(_ includeElement: (S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>> } extension LazySequence {     func map<U>(_ transform: (S.Generator.Element) -> U) -> LazySequence<MapSequenceView<S, U>> } ``` | SequenceType | ```  ``` | -- |
| To | ``` struct LazySequence<Base : SequenceType> : LazySequenceType, SequenceType, _SequenceWrapperType {     init(_ base: Base)     var elements: Base { get }     typealias S = Void } ``` | LazySequenceType, SequenceType | ``` Base : SequenceType ``` | Base |

Modified LazySequence.init(_: Base)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ base: S) ``` | iOS 8.0 |
| To | ``` init(_ base: Base) ``` | iOS 9.0 |

Modified ManagedBuffer

|  | Declaration | Generics[Parameters] |
| --- | --- | --- |
| From | ``` class ManagedBuffer<Value, Element> : ManagedProtoBuffer<Value, Element> {     final class func create(_ minimumCapacity: Int, initialValue initialValue: (ManagedProtoBuffer<Value, Element>) -> Value) -> ManagedBuffer<Value, Element>     deinit      final var value: Value } ``` | -- |
| To | ``` class ManagedBuffer<Value, Element> : ManagedProtoBuffer<Value, Element> {     final class func create(_ minimumCapacity: Int, initialValue initialValue: (ManagedProtoBuffer<Value, Element>) -> Value) -> ManagedBuffer<Value, Element>     final var value: Value } ``` | Value, Element |

Modified ManagedBuffer.create(_: Int, initialValue: (ManagedProtoBuffer<Value, Element>) -> Value) -> ManagedBuffer<Value, Element> [class]

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ManagedBuffer.value

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ManagedBufferPointer [struct]

|  | Declaration | Generics[Parameters] |
| --- | --- | --- |
| From | ``` struct ManagedBufferPointer<Value, Element> : Equatable {     init(bufferClass bufferClass: AnyClass, minimumCapacity minimumCapacity: Int, initialValue initialValue: (buffer: AnyObject, allocatedCount: (AnyObject) -> Int) -> Value)     init(unsafeBufferObject buffer: AnyObject)     init(_uncheckedUnsafeBufferObject buffer: AnyObject)     var value: Value     var buffer: AnyObject { get }     var allocatedElementCount: Int { get }     func withUnsafeMutablePointerToValue<R>(_ body: (UnsafeMutablePointer<Value>) -> R) -> R     func withUnsafeMutablePointerToElements<R>(_ body: (UnsafeMutablePointer<Element>) -> R) -> R     func withUnsafeMutablePointers<R>(_ body: (UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> R     mutating func holdsUniqueReference() -> Bool     mutating func holdsUniqueOrPinnedReference() -> Bool     init(bufferClass bufferClass: AnyClass, minimumCapacity minimumCapacity: Int)     init(_ buffer: ManagedProtoBuffer<Value, Element>) } ``` | -- |
| To | ``` struct ManagedBufferPointer<Value, Element> : Equatable {     init(bufferClass bufferClass: AnyClass, minimumCapacity minimumCapacity: Int, initialValue initialValue: (buffer: AnyObject, allocatedCount: (AnyObject) -> Int) -> Value)     init(unsafeBufferObject buffer: AnyObject)     var value: Value     var buffer: AnyObject { get }     var allocatedElementCount: Int { get }     func withUnsafeMutablePointerToValue<R>(_ body: (UnsafeMutablePointer<Value>) -> R) -> R     func withUnsafeMutablePointerToElements<R>(_ body: (UnsafeMutablePointer<Element>) -> R) -> R     func withUnsafeMutablePointers<R>(_ body: (UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> R     mutating func holdsUniqueReference() -> Bool     mutating func holdsUniqueOrPinnedReference() -> Bool } ``` | Value, Element |

Modified ManagedBufferPointer.holdsUniqueOrPinnedReference() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ManagedBufferPointer.holdsUniqueReference() -> Bool

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ManagedBufferPointer.init(bufferClass: AnyClass, minimumCapacity: Int, initialValue: (buffer: AnyObject, allocatedCount: (AnyObject) -> Int) -> Value)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ManagedBufferPointer.init(unsafeBufferObject: AnyObject)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ManagedBufferPointer.value

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified ManagedBufferPointer.withUnsafeMutablePointers<R>(_: (UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> R

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | R |

Modified ManagedBufferPointer.withUnsafeMutablePointerToElements<R>(_: (UnsafeMutablePointer<Element>) -> R) -> R

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | R |

Modified ManagedBufferPointer.withUnsafeMutablePointerToValue<R>(_: (UnsafeMutablePointer<Value>) -> R) -> R

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | R |

Modified ManagedProtoBuffer

|  | Generics[Parameters] |
| --- | --- |
| From | -- |
| To | Value, Element |

Modified ManagedProtoBuffer.withUnsafeMutablePointers<R>(_: (UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> R

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | R |

Modified ManagedProtoBuffer.withUnsafeMutablePointerToElements<R>(_: (UnsafeMutablePointer<Element>) -> R) -> R

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | R |

Modified ManagedProtoBuffer.withUnsafeMutablePointerToValue<R>(_: (UnsafeMutablePointer<Value>) -> R) -> R

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | R |

Modified MutableCollectionType

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MutableCollectionType : CollectionType {     subscript (position: Self.Index) -> Self.Generator.Element { get set } } ``` | CollectionType |
| To | ``` protocol MutableCollectionType : MutableIndexable, CollectionType {     typealias SubSequence : Indexable, SequenceType = MutableSlice<Self>     subscript (_ position: Self.Index) -> Self.Generator.Element { get set }     subscript (_ bounds: Range<Self.Index>) -> Self.SubSequence { get set } } ``` | CollectionType, MutableIndexable |

Modified MutableSliceable

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol MutableSliceable : Sliceable, MutableCollectionType {     subscript (_: Range<Self.Index>) -> Self.SubSlice { get set } } ``` | MutableCollectionType, Sliceable |
| To | ``` protocol MutableSliceable : CollectionType, MutableCollectionType {     subscript (_ _: Range<Self.Index>) -> Self.SubSequence { get set } } ``` | CollectionType, MutableCollectionType |

Modified NilLiteralConvertible.init(nilLiteral: ())

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified NonObjectiveCBase

|  | Declaration |
| --- | --- |
| From | ``` class NonObjectiveCBase { } ``` |
| To | ``` class NonObjectiveCBase {     init() } ``` |

Modified ObjectIdentifier [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ObjectIdentifier : Hashable, Comparable {     let value: Builtin.RawPointer     var uintValue: UInt { get }     var hashValue: Int { get }     init(_ x: AnyObject)     init(_ x: Any.Type) } ``` | Comparable, Hashable |
| To | ``` struct ObjectIdentifier : Hashable, Equatable, Comparable {     var uintValue: UInt { get }     var hashValue: Int { get }     init(_ x: AnyObject)     init(_ x: Any.Type) } ``` | Comparable, Equatable, Hashable |

Modified [Optional [enum]](https://developer.apple.com/documentation/swift/optional)

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` enum Optional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     func map<U>(_ f: @noescape (T) -> U) -> U?     func flatMap<U>(_ f: @noescape (T) -> U?) -> U?     func getMirror() -> MirrorType     init(nilLiteral nilLiteral: ()) } extension Optional : DebugPrintable {     var debugDescription: String { get } } ``` | DebugPrintable, NilLiteralConvertible, Reflectable | -- |
| To | ``` enum Optional<Wrapped> : _Reflectable, NilLiteralConvertible {     case None     case Some(Wrapped)     typealias T = Wrapped     init()     init(_ some: Wrapped)     @warn_unused_result     @rethrows func map<U>(@noescape _ f: (Wrapped) throws -> U) rethrows -> U?     @warn_unused_result     @rethrows func flatMap<U>(@noescape _ f: (Wrapped) throws -> U?) rethrows -> U?     init(nilLiteral nilLiteral: ()) } extension Optional : CustomDebugStringConvertible {     var debugDescription: String { get } } ``` | CustomDebugStringConvertible, NilLiteralConvertible | Wrapped |

Modified Optional.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Optional.init(_: Wrapped)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ some: T) ``` | iOS 8.0 |
| To | ``` init(_ some: Wrapped) ``` | iOS 9.0 |

Modified Optional.init(nilLiteral: ())

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified Optional.None

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Optional.Some

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` case Some(T) ``` | iOS 8.0 |
| To | ``` case Some(Wrapped) ``` | iOS 9.0 |

Modified OutputStreamType.write(_: String)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified PermutationGenerator [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct PermutationGenerator<C : CollectionType, Indices : SequenceType where C.Index == C.Index> : GeneratorType, SequenceType {     var seq: C     var indices: Indices.Generator     typealias Element = C.Generator.Element     mutating func next() -> Element?     typealias Generator = PermutationGenerator<C, Indices>     func generate() -> PermutationGenerator<C, Indices>     init(elements elements: C, indices indices: Indices) } ``` | ```  ``` | -- |
| To | ``` struct PermutationGenerator<C : CollectionType, Indices : SequenceType where C.Index == Indices.Generator.Element> : GeneratorType, SequenceType {     typealias Element = C.Generator.Element     mutating func next() -> C.Generator.Element?     init(elements elements: C, indices indices: Indices) } ``` | ``` C : CollectionType, Indices : SequenceType, C.Index == Indices.Generator.Element ``` | C, Indices |

Modified RandomAccessIndexType

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol RandomAccessIndexType : BidirectionalIndexType, _RandomAccessIndexType { } ``` | BidirectionalIndexType |
| To | ``` protocol RandomAccessIndexType : BidirectionalIndexType, Strideable, _RandomAccessAmbiguity {     @warn_unused_result     func distanceTo(_ other: Self) -> Self.Distance     @warn_unused_result     func advancedBy(_ n: Self.Distance) -> Self     @warn_unused_result     func advancedBy(_ n: Self.Distance, limit limit: Self) -> Self } ``` | BidirectionalIndexType, Strideable |

Modified Range [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct Range<T : ForwardIndexType> : Equatable, CollectionType, Printable, DebugPrintable {     init(_ x: Range<T>)     init(start start: T, end end: T)     var isEmpty: Bool { get }     typealias Index = T     typealias ArraySlice = Range<T>     subscript (position: T) -> T { get }     subscript (_: T._DisabledRangeIndex) -> T { get }     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T     var description: String { get }     var debugDescription: String { get } } extension Range {     func map<U>(_ transform: (T) -> U) -> [U] } extension Range : Reflectable {     func getMirror() -> MirrorType } ``` | CollectionType, DebugPrintable, Equatable, Printable, Reflectable | ```  ``` | -- |
| To | ``` struct Range<Element : ForwardIndexType> : Equatable, CollectionType, Indexable, SequenceType, CustomStringConvertible, CustomDebugStringConvertible {     typealias T = Element     init(_ x: Range<Element>)     init(start start: Element, end end: Element)     subscript (_ position: Element) -> Element { get }     subscript (_ _: Element._DisabledRangeIndex) -> Element { get }     func generate() -> RangeGenerator<Element>     var startIndex: Element     var endIndex: Element     var description: String { get }     var debugDescription: String { get } } extension Range : _Reflectable { } ``` | CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Equatable, Indexable, SequenceType | ``` Element : ForwardIndexType ``` | Element |

Modified Range.endIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var endIndex: T ``` | iOS 8.0 |
| To | ``` var endIndex: Element ``` | iOS 9.0 |

Modified Range.generate() -> RangeGenerator<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> RangeGenerator<T> ``` | iOS 8.1 |
| To | ``` func generate() -> RangeGenerator<Element> ``` | iOS 9.0 |

Modified Range.init(_: Range<Element>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ x: Range<T>) ``` | iOS 8.1 |
| To | ``` init(_ x: Range<Element>) ``` | iOS 9.0 |

Modified Range.init(start: Element, end: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(start start: T, end end: T) ``` | iOS 8.1 |
| To | ``` init(start start: Element, end end: Element) ``` | iOS 9.0 |

Modified Range.startIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var startIndex: T ``` | iOS 8.0 |
| To | ``` var startIndex: Element ``` | iOS 9.0 |

Modified Range.subscript(_: Element._DisabledRangeIndex) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (_: T._DisabledRangeIndex) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ _: Element._DisabledRangeIndex) -> Element { get } ``` | iOS 9.0 |

Modified Range.subscript(_: Element) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (position: T) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ position: Element) -> Element { get } ``` | iOS 9.0 |

Modified RangeGenerator [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct RangeGenerator<T : ForwardIndexType> : GeneratorType, SequenceType {     typealias Element = T     init(_ bounds: Range<T>)     mutating func next() -> T?     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T } ``` | ```  ``` | -- |
| To | ``` struct RangeGenerator<Element : ForwardIndexType> : GeneratorType, SequenceType {     typealias T = Element     init(_ bounds: Range<Element>)     mutating func next() -> Element?     var startIndex: Element     var endIndex: Element } ``` | ``` Element : ForwardIndexType ``` | Element |

Modified RangeGenerator.endIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var endIndex: T ``` | iOS 8.0 |
| To | ``` var endIndex: Element ``` | iOS 9.0 |

Modified RangeGenerator.init(_: Range<Element>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(_ bounds: Range<T>) ``` | iOS 8.1 |
| To | ``` init(_ bounds: Range<Element>) ``` | iOS 9.0 |

Modified RangeGenerator.next() -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> T? ``` | iOS 8.1 |
| To | ``` mutating func next() -> Element? ``` | iOS 9.0 |

Modified RangeGenerator.startIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var startIndex: T ``` | iOS 8.0 |
| To | ``` var startIndex: Element ``` | iOS 9.0 |

Modified RangeReplaceableCollectionType

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol RangeReplaceableCollectionType : ExtensibleCollectionType {     mutating func replaceRange<C : CollectionType where Self.Generator.Element == Self.Generator.Element>(_ subRange: Range<Self.Index>, with newElements: C)     mutating func insert(_ newElement: Self.Generator.Element, atIndex i: Self.Index)     mutating func splice<S : CollectionType where Self.Generator.Element == Self.Generator.Element>(_ newElements: S, atIndex i: Self.Index)     mutating func removeAtIndex(_ i: Self.Index) -> Self.Generator.Element     mutating func removeRange(_ subRange: Range<Self.Index>)     mutating func removeAll(keepCapacity keepCapacity: Bool) } ``` | ExtensibleCollectionType |
| To | ``` protocol RangeReplaceableCollectionType : CollectionType {     init()     mutating func replaceRange<C : CollectionType where C.Generator.Element == Generator.Element>(_ subRange: Range<Self.Index>, with newElements: C)     mutating func reserveCapacity(_ n: Self.Index.Distance)     mutating func append(_ x: Self.Generator.Element)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == Generator.Element>(_ newElements: S)     mutating func insert(_ newElement: Self.Generator.Element, atIndex i: Self.Index)     mutating func insertContentsOf<S : CollectionType where S.Generator.Element == Generator.Element>(_ newElements: S, at i: Self.Index)     mutating func removeAtIndex(_ i: Self.Index) -> Self.Generator.Element     mutating func removeFirst() -> Self.Generator.Element     mutating func removeFirst(_ n: Int)     mutating func removeRange(_ subRange: Range<Self.Index>)     mutating func removeAll(keepCapacity keepCapacity: Bool) } ``` | CollectionType |

Modified RangeReplaceableCollectionType.removeAll(keepCapacity: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified RawRepresentable

|  | Declaration |
| --- | --- |
| From | ``` protocol RawRepresentable {     typealias RawValue     init?(rawValue rawValue: RawValue)     var rawValue: RawValue { get } } ``` |
| To | ``` protocol RawRepresentable {     typealias RawValue     init?(rawValue rawValue: Self.RawValue)     var rawValue: Self.RawValue { get } } ``` |

Modified RawRepresentable.init(rawValue: Self.RawValue)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init?(rawValue rawValue: RawValue) ``` | iOS 8.1 |
| To | ``` init?(rawValue rawValue: Self.RawValue) ``` | iOS 9.0 |

Modified RawRepresentable.rawValue

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var rawValue: RawValue { get } ``` | iOS 8.1 |
| To | ``` var rawValue: Self.RawValue { get } ``` | iOS 9.0 |

Modified Repeat [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct Repeat<T> : CollectionType {     typealias Index = Int     init(count count: Int, repeatedValue repeatedValue: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> IndexingGenerator<Repeat<T>>     subscript (position: Int) -> T { get }     var count: Int     let repeatedValue: T } ``` | CollectionType | -- |
| To | ``` struct Repeat<Element> : CollectionType, Indexable, SequenceType {     typealias T = Element     typealias Index = Int     init(count count: Int, repeatedValue repeatedValue: Element)     var startIndex: Index { get }     var endIndex: Index { get }     subscript (_ position: Int) -> Element { get }     var count: Int     let repeatedValue: Element } ``` | CollectionType, Indexable, SequenceType | Element |

Modified Repeat.init(count: Int, repeatedValue: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(count count: Int, repeatedValue repeatedValue: T) ``` | iOS 8.0 |
| To | ``` init(count count: Int, repeatedValue repeatedValue: Element) ``` | iOS 9.0 |

Modified Repeat.repeatedValue

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` let repeatedValue: T ``` | iOS 8.0 |
| To | ``` let repeatedValue: Element ``` | iOS 9.0 |

Modified Repeat.subscript(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (position: Int) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ position: Int) -> Element { get } ``` | iOS 9.0 |

Modified ReverseRandomAccessIndex [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct ReverseRandomAccessIndex<I : RandomAccessIndexType> : RandomAccessIndexType {     func successor() -> ReverseRandomAccessIndex<I>     func predecessor() -> ReverseRandomAccessIndex<I>     typealias Distance = I.Distance     func distanceTo(_ other: ReverseRandomAccessIndex<I>) -> I.Distance     func advancedBy(_ amount: I.Distance) -> ReverseRandomAccessIndex<I> } ``` | RandomAccessIndexType | ```  ``` | -- |
| To | ``` struct ReverseRandomAccessIndex<Base : RandomAccessIndexType> : ForwardIndexType, _Incrementable, Equatable, _Strideable, ReverseIndexType, BidirectionalIndexType, RandomAccessIndexType, Strideable, Comparable, _RandomAccessAmbiguity {     typealias Distance = Base.Distance     init(_ base: Base)     let base: Base     func distanceTo(_ other: ReverseRandomAccessIndex<Base>) -> Base.Distance     func advancedBy(_ n: Base.Distance) -> ReverseRandomAccessIndex<Base>     typealias I = Base } ``` | BidirectionalIndexType, Comparable, Equatable, ForwardIndexType, RandomAccessIndexType, ReverseIndexType, Strideable | ``` Base : RandomAccessIndexType ``` | Base |

Modified ReverseRandomAccessIndex.advancedBy(_: Base.Distance) -> ReverseRandomAccessIndex<Base>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ amount: I.Distance) -> ReverseRandomAccessIndex<I> ``` | iOS 8.1 |
| To | ``` func advancedBy(_ n: Base.Distance) -> ReverseRandomAccessIndex<Base> ``` | iOS 9.0 |

Modified ReverseRandomAccessIndex.distanceTo(_: ReverseRandomAccessIndex<Base>) -> Base.Distance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ other: ReverseRandomAccessIndex<I>) -> I.Distance ``` | iOS 8.1 |
| To | ``` func distanceTo(_ other: ReverseRandomAccessIndex<Base>) -> Base.Distance ``` | iOS 9.0 |

Modified SequenceType

|  | Declaration |
| --- | --- |
| From | ``` protocol SequenceType : _Sequence_Type {     typealias Generator : GeneratorType     func generate() -> Generator } ``` |
| To | ``` protocol SequenceType {     typealias Generator : GeneratorType     typealias SubSequence     @warn_unused_result     func generate() -> Self.Generator     @warn_unused_result     func underestimateCount() -> Int     @warn_unused_result     @rethrows func map<T>(@noescape _ transform: (Self.Generator.Element) throws -> T) rethrows -> [T]     @warn_unused_result     @rethrows func filter(@noescape _ includeElement: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.Generator.Element]     @rethrows func forEach(@noescape _ body: (Self.Generator.Element) throws -> ()) rethrows     @warn_unused_result     func dropFirst(_ n: Int) -> Self.SubSequence     @warn_unused_result     func dropLast(_ n: Int) -> Self.SubSequence     @warn_unused_result     func prefix(_ maxLength: Int) -> Self.SubSequence     @warn_unused_result     func suffix(_ maxLength: Int) -> Self.SubSequence     @warn_unused_result     @rethrows func split(_ maxSplit: Int, allowEmptySlices allowEmptySlices: Bool, @noescape isSeparator isSeparator: (Self.Generator.Element) throws -> Bool) rethrows -> [Self.SubSequence] } ``` |

Modified SequenceType.generate() -> Self.Generator

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> Generator ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func generate() -> Self.Generator ``` | iOS 9.0 |

Modified Set [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct Set<T : Hashable> : Hashable, CollectionType, ArrayLiteralConvertible {     typealias Element = T     typealias Index = SetIndex<T>     typealias GeneratorType = SetGenerator<T>     init(minimumCapacity minimumCapacity: Int)     var startIndex: SetIndex<T> { get }     var endIndex: SetIndex<T> { get }     func contains(_ member: T) -> Bool     func indexOf(_ member: T) -> SetIndex<T>?     mutating func insert(_ member: T)     mutating func remove(_ member: T) -> T?     mutating func removeAtIndex(_ index: SetIndex<T>)     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     mutating func removeFirst() -> T     var count: Int { get }     subscript (position: SetIndex<T>) -> T { get }     func generate() -> SetGenerator<T>     init(arrayLiteral elements: T...)     init()     init<S : SequenceType where T == T>(_ sequence: S)     var first: T? { get }     func isSubsetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool     func isStrictSubsetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool     func isSupersetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool     func isStrictSupersetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool     func isDisjointWith<S : SequenceType where T == T>(_ sequence: S) -> Bool     func union<S : SequenceType where T == T>(_ sequence: S) -> Set<T>     mutating func unionInPlace<S : SequenceType where T == T>(_ sequence: S)     func subtract<S : SequenceType where T == T>(_ sequence: S) -> Set<T>     mutating func subtractInPlace<S : SequenceType where T == T>(_ sequence: S)     func intersect<S : SequenceType where T == T>(_ sequence: S) -> Set<T>     mutating func intersectInPlace<S : SequenceType where T == T>(_ sequence: S)     func exclusiveOr<S : SequenceType where T == T>(_ sequence: S) -> Set<T>     mutating func exclusiveOrInPlace<S : SequenceType where T == T>(_ sequence: S)     var isEmpty: Bool { get }     var hashValue: Int { get } } extension Set : _ObjectiveCBridgeable { } extension Set : Printable, DebugPrintable {     func makeDescription(isDebug isDebug: Bool) -> String     var description: String { get }     var debugDescription: String { get } } extension Set : Reflectable {     func getMirror() -> MirrorType } ``` | ArrayLiteralConvertible, CollectionType, DebugPrintable, Hashable, Printable, Reflectable | ```  ``` | -- |
| To | ``` struct Set<Element : Hashable> : Hashable, Equatable, CollectionType, Indexable, SequenceType, ArrayLiteralConvertible {     typealias T = Element     typealias Index = SetIndex<Element>     init(minimumCapacity minimumCapacity: Int)     var startIndex: SetIndex<Element> { get }     var endIndex: SetIndex<Element> { get }     @warn_unused_result     func contains(_ member: Element) -> Bool     @warn_unused_result     func indexOf(_ member: Element) -> SetIndex<Element>?     mutating func insert(_ member: Element)     mutating func remove(_ member: Element) -> Element?     mutating func removeAtIndex(_ index: SetIndex<Element>) -> Element     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     mutating func removeFirst() -> Element     var count: Int { get }     subscript (_ position: SetIndex<Element>) -> Element { get }     func generate() -> SetGenerator<Element>     init(arrayLiteral elements: Element...)     init()     init<S : SequenceType where S.Generator.Element == Element>(_ sequence: S)     @warn_unused_result     func isSubsetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool     @warn_unused_result     func isStrictSubsetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool     @warn_unused_result     func isSupersetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool     @warn_unused_result     func isStrictSupersetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool     @warn_unused_result     func isDisjointWith<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool     @warn_unused_result     func union<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element>     mutating func unionInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S)     @warn_unused_result     func subtract<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element>     mutating func subtractInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S)     @warn_unused_result     func intersect<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element>     mutating func intersectInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S)     @warn_unused_result     func exclusiveOr<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element>     mutating func exclusiveOrInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S)     var hashValue: Int { get }     var isEmpty: Bool { get }     var first: Element? { get } } extension Set : _ObjectiveCBridgeable { } extension Set : CustomStringConvertible, CustomDebugStringConvertible {     var description: String { get }     var debugDescription: String { get } } extension Set : _Reflectable { } extension Set {     mutating func popFirst() -> Element? } ``` | ArrayLiteralConvertible, CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Equatable, Hashable, Indexable, SequenceType | ``` Element : Hashable ``` | Element |

Modified Set.contains(_: Element) -> Bool

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func contains(_ member: T) -> Bool ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func contains(_ member: Element) -> Bool ``` | iOS 9.0 |

Modified Set.endIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var endIndex: SetIndex<T> { get } ``` | iOS 8.3 |
| To | ``` var endIndex: SetIndex<Element> { get } ``` | iOS 9.0 |

Modified Set.exclusiveOr<S : SequenceType where S.Generator.Element == Element>(_: S) -> Set<Element>

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func exclusiveOr<S : SequenceType where T == T>(_ sequence: S) -> Set<T> ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func exclusiveOr<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element> ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.exclusiveOrInPlace<S : SequenceType where S.Generator.Element == Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func exclusiveOrInPlace<S : SequenceType where T == T>(_ sequence: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` mutating func exclusiveOrInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.first

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var first: T? { get } ``` | iOS 8.3 |
| To | ``` var first: Element? { get } ``` | iOS 9.0 |

Modified Set.generate() -> SetGenerator<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> SetGenerator<T> ``` | iOS 8.3 |
| To | ``` func generate() -> SetGenerator<Element> ``` | iOS 9.0 |

Modified Set.indexOf(_: Element) -> SetIndex<Element>?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func indexOf(_ member: T) -> SetIndex<T>? ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func indexOf(_ member: Element) -> SetIndex<Element>? ``` | iOS 9.0 |

Modified Set.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified Set.init<S : SequenceType where S.Generator.Element == Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` init<S : SequenceType where T == T>(_ sequence: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` init<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.init(arrayLiteral: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(arrayLiteral elements: T...) ``` | iOS 8.3 |
| To | ``` init(arrayLiteral elements: Element...) ``` | iOS 9.0 |

Modified Set.init(minimumCapacity: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified Set.insert(_: Element)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func insert(_ member: T) ``` | iOS 8.3 |
| To | ``` mutating func insert(_ member: Element) ``` | iOS 9.0 |

Modified Set.intersect<S : SequenceType where S.Generator.Element == Element>(_: S) -> Set<Element>

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func intersect<S : SequenceType where T == T>(_ sequence: S) -> Set<T> ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func intersect<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element> ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.intersectInPlace<S : SequenceType where S.Generator.Element == Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func intersectInPlace<S : SequenceType where T == T>(_ sequence: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` mutating func intersectInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.isDisjointWith<S : SequenceType where S.Generator.Element == Element>(_: S) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func isDisjointWith<S : SequenceType where T == T>(_ sequence: S) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func isDisjointWith<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.isStrictSubsetOf<S : SequenceType where S.Generator.Element == Element>(_: S) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func isStrictSubsetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func isStrictSubsetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.isStrictSupersetOf<S : SequenceType where S.Generator.Element == Element>(_: S) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func isStrictSupersetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func isStrictSupersetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.isSubsetOf<S : SequenceType where S.Generator.Element == Element>(_: S) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func isSubsetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func isSubsetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.isSupersetOf<S : SequenceType where S.Generator.Element == Element>(_: S) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func isSupersetOf<S : SequenceType where T == T>(_ sequence: S) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func isSupersetOf<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Bool ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.remove(_: Element) -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func remove(_ member: T) -> T? ``` | iOS 8.3 |
| To | ``` mutating func remove(_ member: Element) -> Element? ``` | iOS 9.0 |

Modified Set.removeAll(keepCapacity: Bool)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified Set.removeFirst() -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func removeFirst() -> T ``` | iOS 8.3 |
| To | ``` mutating func removeFirst() -> Element ``` | iOS 9.0 |

Modified Set.startIndex

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var startIndex: SetIndex<T> { get } ``` | iOS 8.3 |
| To | ``` var startIndex: SetIndex<Element> { get } ``` | iOS 9.0 |

Modified Set.subscript(_: SetIndex<Element>) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (position: SetIndex<T>) -> T { get } ``` | iOS 8.3 |
| To | ``` subscript (_ position: SetIndex<Element>) -> Element { get } ``` | iOS 9.0 |

Modified Set.subtract<S : SequenceType where S.Generator.Element == Element>(_: S) -> Set<Element>

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func subtract<S : SequenceType where T == T>(_ sequence: S) -> Set<T> ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func subtract<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element> ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.subtractInPlace<S : SequenceType where S.Generator.Element == Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func subtractInPlace<S : SequenceType where T == T>(_ sequence: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` mutating func subtractInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.union<S : SequenceType where S.Generator.Element == Element>(_: S) -> Set<Element>

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func union<S : SequenceType where T == T>(_ sequence: S) -> Set<T> ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     func union<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) -> Set<Element> ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified Set.unionInPlace<S : SequenceType where S.Generator.Element == Element>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func unionInPlace<S : SequenceType where T == T>(_ sequence: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` mutating func unionInPlace<S : SequenceType where S.Generator.Element == Element>(_ sequence: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | S |

Modified SetGenerator [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct SetGenerator<T : Hashable> : GeneratorType {     mutating func next() -> T? } ``` | ```  ``` | -- |
| To | ``` struct SetGenerator<Element : Hashable> : GeneratorType {     typealias T = Element     mutating func next() -> Element? } ``` | ``` Element : Hashable ``` | Element |

Modified SetGenerator.next() -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> T? ``` | iOS 8.3 |
| To | ``` mutating func next() -> Element? ``` | iOS 9.0 |

Modified SetIndex [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct SetIndex<T : Hashable> : ForwardIndexType, Comparable {     typealias Key = T     typealias Value = T     typealias Index = SetIndex<T>     func successor() -> SetIndex<T> } ``` | Comparable, ForwardIndexType | ```  ``` | -- |
| To | ``` struct SetIndex<Element : Hashable> : ForwardIndexType, _Incrementable, Equatable, Comparable {     typealias T = Element     func successor() -> SetIndex<Element> } ``` | Comparable, Equatable, ForwardIndexType | ``` Element : Hashable ``` | Element |

Modified SetIndex.successor() -> SetIndex<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func successor() -> SetIndex<T> ``` | iOS 8.3 |
| To | ``` func successor() -> SetIndex<Element> ``` | iOS 9.0 |

Modified SignedIntegerType

|  | Declaration |
| --- | --- |
| From | ``` protocol SignedIntegerType : _SignedIntegerType, IntegerType { } ``` |
| To | ``` protocol SignedIntegerType : _SignedIntegerType, IntegerType {     func toIntMax() -> IntMax     init(_ _: IntMax) } ``` |

Modified SignedNumberType

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` protocol SignedNumberType : _SignedNumberType {     prefix func -(_ x: Self) -> Self } ``` | -- |
| To | ``` protocol SignedNumberType : Comparable, IntegerLiteralConvertible {     @warn_unused_result     prefix func -(_ x: Self) -> Self     @warn_unused_result     func -(_ lhs: Self, _ rhs: Self) -> Self } ``` | Comparable, IntegerLiteralConvertible |

Modified StaticString [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct StaticString : UnicodeScalarLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible, Printable, DebugPrintable {     var utf8Start: UnsafePointer<UInt8> { get }     var unicodeScalar: UnicodeScalar { get }     var byteSize: Word { get }     var hasPointerRepresentation: Bool { get }     var isASCII: Bool { get }     func withUTF8Buffer<R>(_ body: @noescape (UnsafeBufferPointer<UInt8>) -> R) -> R     var stringValue: String { get }     init()     init(start start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(unicodeScalar unicodeScalar: Builtin.Int32)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: StaticString)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: StaticString)     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(stringLiteral value: StaticString)     var description: String { get }     var debugDescription: String { get } } ``` | DebugPrintable, ExtendedGraphemeClusterLiteralConvertible, Printable, StringLiteralConvertible, UnicodeScalarLiteralConvertible |
| To | ``` struct StaticString : _Reflectable, UnicodeScalarLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible, CustomStringConvertible, CustomDebugStringConvertible {     var utf8Start: UnsafePointer<UInt8> { get }     var unicodeScalar: UnicodeScalar { get }     var byteSize: Int { get }     var hasPointerRepresentation: Bool { get }     var isASCII: Bool { get }     func withUTF8Buffer<R>(@noescape _ body: (UnsafeBufferPointer<UInt8>) -> R) -> R     var stringValue: String { get }     init()     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: StaticString)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: StaticString)     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(stringLiteral value: StaticString)     var description: String { get }     var debugDescription: String { get } } ``` | CustomDebugStringConvertible, CustomStringConvertible, ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

Modified StaticString.byteSize

|  | Declaration |
| --- | --- |
| From | ``` var byteSize: Word { get } ``` |
| To | ``` var byteSize: Int { get } ``` |

Modified StaticString.withUTF8Buffer<R>(_: (UnsafeBufferPointer<UInt8>) -> R) -> R

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func withUTF8Buffer<R>(_ body: @noescape (UnsafeBufferPointer<UInt8>) -> R) -> R ``` | iOS 8.1 | -- |
| To | ``` func withUTF8Buffer<R>(@noescape _ body: (UnsafeBufferPointer<UInt8>) -> R) -> R ``` | iOS 9.0 | R |

Modified Streamable.writeTo<Target : OutputStreamType>(_: Target)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` Target : OutputStreamType ``` | Target |

Modified Strideable

|  | Declaration |
| --- | --- |
| From | ``` protocol Strideable : Comparable, _Strideable { } ``` |
| To | ``` protocol Strideable : Comparable, _Strideable {     typealias Stride : SignedNumberType     @warn_unused_result     func distanceTo(_ other: Self) -> Self.Stride     @warn_unused_result     func advancedBy(_ n: Self.Stride) -> Self } ``` |

Modified StrideThrough [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct StrideThrough<T : Strideable> : SequenceType {     func generate() -> StrideThroughGenerator<T>     init(start start: T, end end: T, stride stride: T.Stride)     let start: T     let end: T     let stride: T.Stride } extension StrideThrough : Reflectable {     func getMirror() -> MirrorType } ``` | Reflectable, SequenceType | ```  ``` | -- |
| To | ``` struct StrideThrough<Element : Strideable> : SequenceType {     typealias T = Element     func generate() -> StrideThroughGenerator<Element> } extension StrideThrough : _Reflectable { } ``` | SequenceType | ``` Element : Strideable ``` | Element |

Modified StrideThrough.generate() -> StrideThroughGenerator<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> StrideThroughGenerator<T> ``` | iOS 8.0 |
| To | ``` func generate() -> StrideThroughGenerator<Element> ``` | iOS 9.0 |

Modified StrideThroughGenerator [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct StrideThroughGenerator<T : Strideable> : GeneratorType {     var current: T     let end: T     let stride: T.Stride     var done: Bool     mutating func next() -> T? } ``` | ```  ``` | -- |
| To | ``` struct StrideThroughGenerator<Element : Strideable> : GeneratorType {     typealias T = Element     mutating func next() -> Element? } ``` | ``` Element : Strideable ``` | Element |

Modified StrideThroughGenerator.next() -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> T? ``` | iOS 8.0 |
| To | ``` mutating func next() -> Element? ``` | iOS 9.0 |

Modified StrideTo [struct]

|  | Declaration | Protocols | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` struct StrideTo<T : Strideable> : SequenceType {     func generate() -> StrideToGenerator<T>     init(start start: T, end end: T, stride stride: T.Stride)     let start: T     let end: T     let stride: T.Stride } extension StrideTo : Reflectable {     func getMirror() -> MirrorType } ``` | Reflectable, SequenceType | ```  ``` | -- |
| To | ``` struct StrideTo<Element : Strideable> : SequenceType {     typealias T = Element     func generate() -> StrideToGenerator<Element> } extension StrideTo : _Reflectable { } ``` | SequenceType | ``` Element : Strideable ``` | Element |

Modified StrideTo.generate() -> StrideToGenerator<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> StrideToGenerator<T> ``` | iOS 8.0 |
| To | ``` func generate() -> StrideToGenerator<Element> ``` | iOS 9.0 |

Modified StrideToGenerator [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct StrideToGenerator<T : Strideable> : GeneratorType {     var current: T     let end: T     let stride: T.Stride     mutating func next() -> T? } ``` | ```  ``` | -- |
| To | ``` struct StrideToGenerator<Element : Strideable> : GeneratorType {     typealias T = Element     mutating func next() -> Element? } ``` | ``` Element : Strideable ``` | Element |

Modified StrideToGenerator.next() -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> T? ``` | iOS 8.0 |
| To | ``` mutating func next() -> Element? ``` | iOS 9.0 |

Modified [String [struct]](https://developer.apple.com/documentation/swift/string)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct String {     init() } extension String {     static func availableStringEncodings() -> [NSStringEncoding]     static func defaultCStringEncoding() -> NSStringEncoding     static func localizedNameOfStringEncoding(_ encoding: NSStringEncoding) -> String     static func localizedStringWithFormat(_ format: String, _ arguments: CVarArgType...) -> String     static func pathWithComponents(_ components: [String]) -> String     init?(contentsOfFile path: String, encoding enc: NSStringEncoding, error error: NSErrorPointer = default)     init?(contentsOfFile path: String, usedEncoding usedEncoding: UnsafeMutablePointer<NSStringEncoding> = default, error error: NSErrorPointer = default)     init?(contentsOfURL url: NSURL, encoding enc: NSStringEncoding, error error: NSErrorPointer = default)     init?(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<NSStringEncoding> = default, error error: NSErrorPointer = default)     init?(CString CString: UnsafePointer<CChar>, encoding enc: NSStringEncoding)     init?(UTF8String bytes: UnsafePointer<CChar>)     func canBeConvertedToEncoding(_ encoding: NSStringEncoding) -> Bool     var capitalizedString: String { get }     func capitalizedStringWithLocale(_ locale: NSLocale?) -> String     func caseInsensitiveCompare(_ aString: String) -> NSComparisonResult     func commonPrefixWithString(_ aString: String, options options: NSStringCompareOptions) -> String     func compare(_ aString: String, options mask: NSStringCompareOptions = default, range range: Range<String.Index>? = default, locale locale: NSLocale? = default) -> NSComparisonResult     func completePathIntoString(_ outputName: UnsafeMutablePointer<String> = default, caseSensitive caseSensitive: Bool, matchesIntoArray matchesIntoArray: UnsafeMutablePointer<[String]> = default, filterTypes filterTypes: [String]? = default) -> Int     func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String]     func componentsSeparatedByString(_ separator: String) -> [String]     func cStringUsingEncoding(_ encoding: NSStringEncoding) -> [CChar]?     func dataUsingEncoding(_ encoding: NSStringEncoding, allowLossyConversion allowLossyConversion: Bool = default) -> NSData?     var decomposedStringWithCanonicalMapping: String { get }     var decomposedStringWithCompatibilityMapping: String { get }     func enumerateLines(_ body: (line: String, inout stop: Bool) -> ())     func enumerateLinguisticTagsInRange(_ range: Range<String.Index>, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, _ body: (String, Range<String.Index>, Range<String.Index>, inout Bool) -> ())     func enumerateSubstringsInRange(_ range: Range<String.Index>, options opts: NSStringEnumerationOptions, _ body: (substring: String, substringRange: Range<String.Index>, enclosingRange: Range<String.Index>, inout Bool) -> ())     var fastestEncoding: NSStringEncoding { get }     func fileSystemRepresentation() -> [CChar]     func getBytes(inout _ buffer: [UInt8], maxLength maxLength: Int, usedLength usedLength: UnsafeMutablePointer<Int>, encoding encoding: NSStringEncoding, options options: NSStringEncodingConversionOptions, range range: Range<String.Index>, remainingRange remainingRange: UnsafeMutablePointer<Range<String.Index>>) -> Bool     func getCString(inout _ buffer: [CChar], maxLength maxLength: Int, encoding encoding: NSStringEncoding) -> Bool     func getFileSystemRepresentation(inout _ buffer: [CChar], maxLength maxLength: Int) -> Bool     func getLineStart(_ start: UnsafeMutablePointer<String.Index>, end end: UnsafeMutablePointer<String.Index>, contentsEnd contentsEnd: UnsafeMutablePointer<String.Index>, forRange forRange: Range<String.Index>)     func getParagraphStart(_ start: UnsafeMutablePointer<String.Index>, end end: UnsafeMutablePointer<String.Index>, contentsEnd contentsEnd: UnsafeMutablePointer<String.Index>, forRange forRange: Range<String.Index>)     var hash: Int { get }     init?<S : SequenceType where UInt8 == UInt8>(bytes bytes: S, encoding encoding: NSStringEncoding)     init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, encoding encoding: NSStringEncoding, freeWhenDone flag: Bool)     init(utf16CodeUnits utf16CodeUnits: UnsafePointer<unichar>, count count: Int)     init(utf16CodeUnitsNoCopy utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count count: Int, freeWhenDone flag: Bool)     init(format format: String, _ arguments: CVarArgType...)     init(format format: String, arguments arguments: [CVarArgType])     init(format format: String, locale locale: NSLocale?, _ args: CVarArgType...)     init(format format: String, locale locale: NSLocale?, arguments arguments: [CVarArgType])     var lastPathComponent: String { get }     var utf16Count: Int { get }     func lengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int     func lineRangeForRange(_ aRange: Range<String.Index>) -> Range<String.Index>     func linguisticTagsInRange(_ range: Range<String.Index>, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions = default, orthography orthography: NSOrthography? = default, tokenRanges tokenRanges: UnsafeMutablePointer<[Range<String.Index>]> = default) -> [String]     func localizedCaseInsensitiveCompare(_ aString: String) -> NSComparisonResult     func localizedCompare(_ aString: String) -> NSComparisonResult     func localizedStandardCompare(_ string: String) -> NSComparisonResult     func lowercaseStringWithLocale(_ locale: NSLocale) -> String     func maximumLengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int     func paragraphRangeForRange(_ aRange: Range<String.Index>) -> Range<String.Index>     var pathComponents: [String] { get }     var pathExtension: String { get }     var precomposedStringWithCanonicalMapping: String { get }     var precomposedStringWithCompatibilityMapping: String { get }     func propertyList() -> AnyObject     func propertyListFromStringsFileFormat() -> [String : String]     func rangeOfCharacterFromSet(_ aSet: NSCharacterSet, options mask: NSStringCompareOptions = default, range aRange: Range<String.Index>? = default) -> Range<String.Index>?     func rangeOfComposedCharacterSequenceAtIndex(_ anIndex: String.Index) -> Range<String.Index>     func rangeOfComposedCharacterSequencesForRange(_ range: Range<String.Index>) -> Range<String.Index>     func rangeOfString(_ aString: String, options mask: NSStringCompareOptions = default, range searchRange: Range<String.Index>? = default, locale locale: NSLocale? = default) -> Range<String.Index>?     var smallestEncoding: NSStringEncoding { get }     var stringByAbbreviatingWithTildeInPath: String { get }     func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String?     func stringByAddingPercentEscapesUsingEncoding(_ encoding: NSStringEncoding) -> String?     func stringByAppendingFormat(_ format: String, _ arguments: CVarArgType...) -> String     func stringByAppendingPathComponent(_ aString: String) -> String     func stringByAppendingPathExtension(_ ext: String) -> String?     func stringByAppendingString(_ aString: String) -> String     var stringByDeletingLastPathComponent: String { get }     var stringByDeletingPathExtension: String { get }     var stringByExpandingTildeInPath: String { get }     func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale) -> String     func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String     var stringByRemovingPercentEncoding: String? { get }     func stringByReplacingCharactersInRange(_ range: Range<String.Index>, withString replacement: String) -> String     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions = default, range searchRange: Range<String.Index>? = default) -> String     func stringByReplacingPercentEscapesUsingEncoding(_ encoding: NSStringEncoding) -> String?     var stringByResolvingSymlinksInPath: String { get }     var stringByStandardizingPath: String { get }     func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String     func stringsByAppendingPaths(_ paths: [String]) -> [String]     func substringFromIndex(_ index: String.Index) -> String     func substringToIndex(_ index: String.Index) -> String     func substringWithRange(_ aRange: Range<String.Index>) -> String     func uppercaseStringWithLocale(_ locale: NSLocale) -> String     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: NSStringEncoding, error error: NSErrorPointer = default) -> Bool     func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: NSStringEncoding, error error: NSErrorPointer = default) -> Bool } extension String : _ObjectiveCBridgeable { } extension String {     init(_ cocoaString: NSString) } extension String : CollectionType {     struct Index : BidirectionalIndexType, Comparable, Reflectable {         func successor() -> String.Index         func predecessor() -> String.Index         func getMirror() -> MirrorType     }     var startIndex: String.Index { get }     var endIndex: String.Index { get }     subscript (i: String.Index) -> Character { get }     subscript (i: Int) -> Character { get }     func generate() -> IndexingGenerator<String> } extension String {     struct UTF16View : Sliceable, Reflectable, Printable, DebugPrintable {         struct Index {         }         var startIndex: String.UTF16View.Index { get }         var endIndex: String.UTF16View.Index { get }         typealias Generator         func generate() -> Generator         subscript (i: String.UTF16View.Index) -> UInt16 { get }         subscript (i: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         subscript (subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get }         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     }     var utf16: String.UTF16View { get }     init?(_ utf16: String.UTF16View)     typealias UTF16Index = String.UTF16View.Index } extension String {     struct UTF8View : CollectionType, Reflectable, Printable, DebugPrintable {         struct Index : ForwardIndexType {             typealias Buffer = UTF8Chunk             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (position: String.UTF8View.Index) -> CodeUnit { get }         subscript (subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     }     var utf8: String.UTF8View { get }     var nulTerminatedUTF8: ContiguousArray<CodeUnit> { get }     init?(_ utf8: String.UTF8View)     typealias UTF8Index = String.UTF8View.Index } extension String {     struct UnicodeScalarView : Sliceable, SequenceType, Reflectable, Printable, DebugPrintable {         struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.Generator         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     }     init(_ unicodeScalars: String.UnicodeScalarView)     typealias UnicodeScalarIndex = String.UnicodeScalarView.Index } extension String {     static func fromCString(_ cs: UnsafePointer<CChar>) -> String?     static func fromCStringRepairingIllFormedUTF8(_ cs: UnsafePointer<CChar>) -> (String?, hadError: Bool) } extension String {     init(_ c: Character) } extension String {     func withCString<Result>(_ f: @noescape UnsafePointer<Int8> -> Result) -> Result } extension String : Reflectable {     func getMirror() -> MirrorType } extension String : OutputStreamType {     mutating func write(_ other: String) } extension String : Streamable {     func writeTo<Target : OutputStreamType>(inout _ target: Target) } extension String {     init(_builtinUnicodeScalarLiteral value: Builtin.Int32) } extension String : UnicodeScalarLiteralConvertible {     init(unicodeScalarLiteral value: String) } extension String {     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1) } extension String : ExtendedGraphemeClusterLiteralConvertible {     init(extendedGraphemeClusterLiteral value: String) } extension String {     init(_builtinUTF16StringLiteral start: Builtin.RawPointer, numberOfCodeUnits numberOfCodeUnits: Builtin.Word) } extension String {     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1) } extension String : StringLiteralConvertible {     init(stringLiteral value: String) } extension String : DebugPrintable {     var debugDescription: String { get } } extension String : Equatable { } extension String : Comparable { } extension String {     mutating func extend(_ other: String)     mutating func append(_ x: UnicodeScalar) } extension String : Hashable {     var hashValue: Int { get } } extension String : StringInterpolationConvertible {     init(stringInterpolation strings: String...)     init<T>(stringInterpolationSegment expr: T) } extension String : Sliceable {     subscript (subRange: Range<String.Index>) -> String { get }     subscript (subRange: Range<Int>) -> String { get } } extension String : ExtensibleCollectionType {     mutating func reserveCapacity(_ n: Int)     mutating func append(_ c: Character)     mutating func extend<S : SequenceType where Character == Character>(_ newElements: S)     init<S : SequenceType where Character == Character>(_ characters: S) } extension String {     func join<S : SequenceType where String == String>(_ elements: S) -> String } extension String : RangeReplaceableCollectionType {     mutating func replaceRange<C : CollectionType where Character == Character>(_ subRange: Range<String.Index>, with newElements: C)     mutating func insert(_ newElement: Character, atIndex i: String.Index)     mutating func splice<S : CollectionType where Character == Character>(_ newElements: S, atIndex i: String.Index)     mutating func removeAtIndex(_ i: String.Index) -> Character     mutating func removeRange(_ subRange: Range<String.Index>)     mutating func removeAll(keepCapacity keepCapacity: Bool = default) } extension String {     var lowercaseString: String { get }     var uppercaseString: String { get } } extension String : StringInterpolationConvertible {     init(stringInterpolationSegment expr: String)     init(stringInterpolationSegment expr: Character)     init(stringInterpolationSegment expr: UnicodeScalar)     init(stringInterpolationSegment expr: Bool)     init(stringInterpolationSegment expr: Float32)     init(stringInterpolationSegment expr: Float64)     init(stringInterpolationSegment expr: UInt8)     init(stringInterpolationSegment expr: Int8)     init(stringInterpolationSegment expr: UInt16)     init(stringInterpolationSegment expr: Int16)     init(stringInterpolationSegment expr: UInt32)     init(stringInterpolationSegment expr: Int32)     init(stringInterpolationSegment expr: UInt64)     init(stringInterpolationSegment expr: Int64)     init(stringInterpolationSegment expr: UInt)     init(stringInterpolationSegment expr: Int) } extension String {     init(count count: Int, repeatedValue c: Character)     init(count count: Int, repeatedValue c: UnicodeScalar)     var isEmpty: Bool { get } } extension String {     func hasPrefix(_ prefix: String) -> Bool     func hasSuffix(_ suffix: String) -> Bool } extension String {     init<T : _SignedIntegerType>(_ v: T)     init<T : _UnsignedIntegerType>(_ v: T)     init<T : _SignedIntegerType>(_ v: T, radix radix: Int, uppercase uppercase: Bool = default)     init<T : _UnsignedIntegerType>(_ v: T, radix radix: Int, uppercase uppercase: Bool = default) } extension String {     func toInt() -> Int? } extension String {     var unicodeScalars: String.UnicodeScalarView } ``` | CollectionType, Comparable, DebugPrintable, Equatable, ExtendedGraphemeClusterLiteralConvertible, ExtensibleCollectionType, Hashable, OutputStreamType, RangeReplaceableCollectionType, Reflectable, Sliceable, Streamable, StringInterpolationConvertible, StringLiteralConvertible, UnicodeScalarLiteralConvertible |
| To | ``` struct String {     init() } extension String {     @warn_unused_result     static func availableStringEncodings() -> [NSStringEncoding]     @warn_unused_result     static func defaultCStringEncoding() -> NSStringEncoding     @warn_unused_result     static func localizedNameOfStringEncoding(_ encoding: NSStringEncoding) -> String     @warn_unused_result     static func localizedStringWithFormat(_ format: String, _ arguments: CVarArgType...) -> String     static func pathWithComponents(_ components: [String]) -> String     init?(UTF8String bytes: UnsafePointer<CChar>)     @warn_unused_result     func canBeConvertedToEncoding(_ encoding: NSStringEncoding) -> Bool     var capitalizedString: String { get }     var localizedCapitalizedString: String { get }     @warn_unused_result     func capitalizedStringWithLocale(_ locale: NSLocale?) -> String     @warn_unused_result     func caseInsensitiveCompare(_ aString: String) -> NSComparisonResult     @warn_unused_result     func commonPrefixWithString(_ aString: String, options options: NSStringCompareOptions) -> String     @warn_unused_result     func compare(_ aString: String, options mask: NSStringCompareOptions = default, range range: Range<Index>? = default, locale locale: NSLocale? = default) -> NSComparisonResult     @warn_unused_result     func completePathIntoString(_ outputName: UnsafeMutablePointer<String> = default, caseSensitive caseSensitive: Bool, matchesIntoArray matchesIntoArray: UnsafeMutablePointer<[String]> = default, filterTypes filterTypes: [String]? = default) -> Int     @warn_unused_result     func componentsSeparatedByCharactersInSet(_ separator: NSCharacterSet) -> [String]     func componentsSeparatedByString(_ separator: String) -> [String]     @warn_unused_result     func cStringUsingEncoding(_ encoding: NSStringEncoding) -> [CChar]?     @warn_unused_result     func dataUsingEncoding(_ encoding: NSStringEncoding, allowLossyConversion allowLossyConversion: Bool = default) -> NSData?     var decomposedStringWithCanonicalMapping: String { get }     var decomposedStringWithCompatibilityMapping: String { get }     func enumerateLines(_ body: (line: String, inout stop: Bool) -> ())     func enumerateLinguisticTagsInRange(_ range: Range<Index>, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions, orthography orthography: NSOrthography?, _ body: (String, Range<Index>, Range<Index>, inout Bool) -> ())     func enumerateSubstringsInRange(_ range: Range<Index>, options opts: NSStringEnumerationOptions, _ body: (substring: String?, substringRange: Range<Index>, enclosingRange: Range<Index>, inout Bool) -> ())     var fastestEncoding: NSStringEncoding { get }     func fileSystemRepresentation() -> [CChar]     func getBytes(inout _ buffer: [UInt8], maxLength maxBufferCount: Int, usedLength usedBufferCount: UnsafeMutablePointer<Int>, encoding encoding: NSStringEncoding, options options: NSStringEncodingConversionOptions, range range: Range<Index>, remainingRange leftover: UnsafeMutablePointer<Range<Index>>) -> Bool     func getCString(inout _ buffer: [CChar], maxLength maxLength: Int, encoding encoding: NSStringEncoding) -> Bool     func getFileSystemRepresentation(inout _ buffer: [CChar], maxLength maxLength: Int) -> Bool     func getLineStart(_ start: UnsafeMutablePointer<Index>, end end: UnsafeMutablePointer<Index>, contentsEnd contentsEnd: UnsafeMutablePointer<Index>, forRange forRange: Range<Index>)     func getParagraphStart(_ start: UnsafeMutablePointer<Index>, end end: UnsafeMutablePointer<Index>, contentsEnd contentsEnd: UnsafeMutablePointer<Index>, forRange forRange: Range<Index>)     var hash: Int { get }     init?<S : SequenceType where S.Generator.Element == UInt8>(bytes bytes: S, encoding encoding: NSStringEncoding)     init?(bytesNoCopy bytes: UnsafeMutablePointer<Void>, length length: Int, encoding encoding: NSStringEncoding, freeWhenDone flag: Bool)     init(utf16CodeUnits utf16CodeUnits: UnsafePointer<unichar>, count count: Int)     init(utf16CodeUnitsNoCopy utf16CodeUnitsNoCopy: UnsafePointer<unichar>, count count: Int, freeWhenDone flag: Bool)     init(contentsOfFile path: String, encoding enc: NSStringEncoding) throws     init(contentsOfFile path: String, usedEncoding usedEncoding: UnsafeMutablePointer<NSStringEncoding> = default) throws     init(contentsOfURL url: NSURL, encoding enc: NSStringEncoding) throws     init(contentsOfURL url: NSURL, usedEncoding enc: UnsafeMutablePointer<NSStringEncoding> = default) throws     init?(CString CString: UnsafePointer<CChar>, encoding enc: NSStringEncoding)     init?(data data: NSData, encoding encoding: NSStringEncoding)     init(format format: String, _ arguments: CVarArgType...)     init(format format: String, arguments arguments: [CVarArgType])     init(format format: String, locale locale: NSLocale?, _ args: CVarArgType...)     init(format format: String, locale locale: NSLocale?, arguments arguments: [CVarArgType])     var lastPathComponent: String { get }     var utf16Count: Int { get }     @warn_unused_result     func lengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int     @warn_unused_result     func lineRangeForRange(_ aRange: Range<Index>) -> Range<Index>     @warn_unused_result     func linguisticTagsInRange(_ range: Range<Index>, scheme tagScheme: String, options opts: NSLinguisticTaggerOptions = default, orthography orthography: NSOrthography? = default, tokenRanges tokenRanges: UnsafeMutablePointer<[Range<Index>]> = default) -> [String]     @warn_unused_result     func localizedCaseInsensitiveCompare(_ aString: String) -> NSComparisonResult     @warn_unused_result     func localizedCompare(_ aString: String) -> NSComparisonResult     @warn_unused_result     func localizedStandardCompare(_ string: String) -> NSComparisonResult     var localizedLowercaseString: String { get }     @warn_unused_result     func lowercaseStringWithLocale(_ locale: NSLocale?) -> String     @warn_unused_result     func maximumLengthOfBytesUsingEncoding(_ encoding: NSStringEncoding) -> Int     @warn_unused_result     func paragraphRangeForRange(_ aRange: Range<Index>) -> Range<Index>     var pathComponents: [String] { get }     var pathExtension: String { get }     var precomposedStringWithCanonicalMapping: String { get }     var precomposedStringWithCompatibilityMapping: String { get }     @warn_unused_result     func propertyList() -> AnyObject     @warn_unused_result     func propertyListFromStringsFileFormat() -> [String : String]     @warn_unused_result     func rangeOfCharacterFromSet(_ aSet: NSCharacterSet, options mask: NSStringCompareOptions = default, range aRange: Range<Index>? = default) -> Range<Index>?     @warn_unused_result     func rangeOfComposedCharacterSequenceAtIndex(_ anIndex: Index) -> Range<Index>     @warn_unused_result     func rangeOfComposedCharacterSequencesForRange(_ range: Range<Index>) -> Range<Index>     @warn_unused_result     func rangeOfString(_ aString: String, options mask: NSStringCompareOptions = default, range searchRange: Range<Index>? = default, locale locale: NSLocale? = default) -> Range<Index>?     @warn_unused_result     func localizedStandardContainsString(_ string: String) -> Bool     @warn_unused_result     func localizedStandardRangeOfString(_ string: String) -> Range<Index>?     var smallestEncoding: NSStringEncoding { get }     var stringByAbbreviatingWithTildeInPath: String { get }     @warn_unused_result     func stringByAddingPercentEncodingWithAllowedCharacters(_ allowedCharacters: NSCharacterSet) -> String?     func stringByAddingPercentEscapesUsingEncoding(_ encoding: NSStringEncoding) -> String?     @warn_unused_result     func stringByAppendingFormat(_ format: String, _ arguments: CVarArgType...) -> String     func stringByAppendingPathComponent(_ aString: String) -> String     func stringByAppendingPathExtension(_ ext: String) -> String?     @warn_unused_result     func stringByAppendingString(_ aString: String) -> String     var stringByDeletingLastPathComponent: String { get }     var stringByDeletingPathExtension: String { get }     var stringByExpandingTildeInPath: String { get }     @warn_unused_result     func stringByFoldingWithOptions(_ options: NSStringCompareOptions, locale locale: NSLocale?) -> String     @warn_unused_result     func stringByPaddingToLength(_ newLength: Int, withString padString: String, startingAtIndex padIndex: Int) -> String     var stringByRemovingPercentEncoding: String? { get }     @warn_unused_result     func stringByReplacingCharactersInRange(_ range: Range<Index>, withString replacement: String) -> String     @warn_unused_result     func stringByReplacingOccurrencesOfString(_ target: String, withString replacement: String, options options: NSStringCompareOptions = default, range searchRange: Range<Index>? = default) -> String     func stringByReplacingPercentEscapesUsingEncoding(_ encoding: NSStringEncoding) -> String?     var stringByResolvingSymlinksInPath: String { get }     var stringByStandardizingPath: String { get }     @warn_unused_result     func stringByTrimmingCharactersInSet(_ set: NSCharacterSet) -> String     func stringsByAppendingPaths(_ paths: [String]) -> [String]     @warn_unused_result     func substringFromIndex(_ index: Index) -> String     @warn_unused_result     func substringToIndex(_ index: Index) -> String     @warn_unused_result     func substringWithRange(_ aRange: Range<Index>) -> String     var localizedUppercaseString: String { get }     @warn_unused_result     func uppercaseStringWithLocale(_ locale: NSLocale?) -> String     func writeToFile(_ path: String, atomically useAuxiliaryFile: Bool, encoding enc: NSStringEncoding) throws     func writeToURL(_ url: NSURL, atomically useAuxiliaryFile: Bool, encoding enc: NSStringEncoding) throws     @warn_unused_result     func stringByApplyingTransform(_ transform: String, reverse reverse: Bool) -> String?     @warn_unused_result     func containsString(_ other: String) -> Bool     @warn_unused_result     func localizedCaseInsensitiveContainsString(_ other: String) -> Bool } extension String : _ObjectiveCBridgeable { } extension String {     init(_ cocoaString: NSString) } extension String {     typealias Index = String.CharacterView.Index     var startIndex: Index { get }     var endIndex: Index { get }     subscript (_ i: Index) -> Character { get } } extension String {     struct CharacterView {         init(_ text: String)     }     var characters: String.CharacterView { get }     mutating func withMutableCharacters<R>(_ body: (inout String.CharacterView) -> R) -> R     init(_ characters: String.CharacterView) } extension String {     struct UnicodeScalarView : CollectionType, Indexable, SequenceType, _Reflectable, CustomStringConvertible, CustomDebugStringConvertible {         struct Index : ForwardIndexType, _Incrementable, Equatable, BidirectionalIndexType, Comparable {             @warn_unused_result             func successor() -> String.UnicodeScalarView.Index             @warn_unused_result             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (_ position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (_ r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         @warn_unused_result         func generate() -> String.UnicodeScalarView.Generator         var description: String { get }         var debugDescription: String { get }     }     init(_ unicodeScalars: String.UnicodeScalarView)     typealias UnicodeScalarIndex = String.UnicodeScalarView.Index } extension String {     struct UTF16View : CollectionType, Indexable, SequenceType, _Reflectable, CustomStringConvertible, CustomDebugStringConvertible {         struct Index {         }         var startIndex: String.UTF16View.Index { get }         var endIndex: String.UTF16View.Index { get }         subscript (_ i: String.UTF16View.Index) -> CodeUnit { get }         subscript (_ i: Int) -> CodeUnit { get }         subscript (_ subRange: Range<Int>) -> String.UTF16View { get }         subscript (_ subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get }         var description: String { get }         var debugDescription: String { get }     }     var utf16: String.UTF16View { get }     init?(_ utf16: String.UTF16View)     typealias UTF16Index = String.UTF16View.Index } extension String {     struct UTF8View : CollectionType, Indexable, SequenceType, _Reflectable, CustomStringConvertible, CustomDebugStringConvertible {         struct Index : ForwardIndexType, _Incrementable, Equatable {             @warn_unused_result             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (_ position: String.UTF8View.Index) -> CodeUnit { get }         subscript (_ subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get }         var description: String { get }         var debugDescription: String { get }     }     var utf8: String.UTF8View { get }     var nulTerminatedUTF8: ContiguousArray<CodeUnit> { get }     init?(_ utf8: String.UTF8View)     typealias UTF8Index = String.UTF8View.Index } extension String {     @warn_unused_result     static func fromCString(_ cs: UnsafePointer<CChar>) -> String?     @warn_unused_result     static func fromCStringRepairingIllFormedUTF8(_ cs: UnsafePointer<CChar>) -> (String?, hadError: Bool) } extension String {     init(_ c: Character) } extension String {     @rethrows func withCString<Result>(@noescape _ f: UnsafePointer<Int8> throws -> Result) rethrows -> Result } extension String : _Reflectable { } extension String : OutputStreamType {     mutating func write(_ other: String) } extension String : Streamable {     func writeTo<Target : OutputStreamType>(inout _ target: Target) } extension String {     init(_builtinUnicodeScalarLiteral value: Builtin.Int32) } extension String : UnicodeScalarLiteralConvertible {     init(unicodeScalarLiteral value: String) } extension String {     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1) } extension String : ExtendedGraphemeClusterLiteralConvertible {     init(extendedGraphemeClusterLiteral value: String) } extension String {     init(_builtinUTF16StringLiteral start: Builtin.RawPointer, numberOfCodeUnits numberOfCodeUnits: Builtin.Word) } extension String {     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1) } extension String : StringLiteralConvertible {     init(stringLiteral value: String) } extension String : CustomDebugStringConvertible {     var debugDescription: String { get } } extension String : Equatable { } extension String : Comparable { } extension String {     mutating func appendContentsOf(_ other: String)     mutating func append(_ x: UnicodeScalar) } extension String : Hashable {     var hashValue: Int { get } } extension String {     subscript (_ subRange: Range<Index>) -> String { get } } extension String {     mutating func reserveCapacity(_ n: Int)     mutating func append(_ c: Character)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == Character>(_ newElements: S)     init<S : SequenceType where S.Generator.Element == Character>(_ characters: S) } extension String {     func join<S : SequenceType where S.Generator.Element == String>(_ elements: S) -> String } extension String {     mutating func replaceRange<C : CollectionType where C.Generator.Element == Character>(_ subRange: Range<Index>, with newElements: C)     mutating func replaceRange(_ subRange: Range<Index>, with newElements: String)     mutating func insert(_ newElement: Character, atIndex i: Index)     mutating func insertContentsOf<S : CollectionType where S.Generator.Element == Character>(_ newElements: S, at i: Index)     mutating func removeAtIndex(_ i: Index) -> Character     mutating func removeRange(_ subRange: Range<Index>)     mutating func removeAll(keepCapacity keepCapacity: Bool = default) } extension String {     var lowercaseString: String { get }     var uppercaseString: String { get } } extension String : StringInterpolationConvertible {     init(stringInterpolation strings: String...)     init<T>(stringInterpolationSegment expr: T)     init(stringInterpolationSegment expr: String)     init(stringInterpolationSegment expr: Character)     init(stringInterpolationSegment expr: UnicodeScalar)     init(stringInterpolationSegment expr: Bool)     init(stringInterpolationSegment expr: Float32)     init(stringInterpolationSegment expr: Float64)     init(stringInterpolationSegment expr: UInt8)     init(stringInterpolationSegment expr: Int8)     init(stringInterpolationSegment expr: UInt16)     init(stringInterpolationSegment expr: Int16)     init(stringInterpolationSegment expr: UInt32)     init(stringInterpolationSegment expr: Int32)     init(stringInterpolationSegment expr: UInt64)     init(stringInterpolationSegment expr: Int64)     init(stringInterpolationSegment expr: UInt)     init(stringInterpolationSegment expr: Int) } extension String {     init(count count: Int, repeatedValue c: Character)     init(count count: Int, repeatedValue c: UnicodeScalar)     var isEmpty: Bool { get } } extension String {     func hasPrefix(_ prefix: String) -> Bool     func hasSuffix(_ suffix: String) -> Bool } extension String {     init<T : _SignedIntegerType>(_ v: T)     init<T : UnsignedIntegerType>(_ v: T)     init<T : _SignedIntegerType>(_ v: T, radix radix: Int, uppercase uppercase: Bool = default)     init<T : UnsignedIntegerType>(_ v: T, radix radix: Int, uppercase uppercase: Bool = default) } extension String {     func toInt() -> Int? } extension String {     var unicodeScalars: String.UnicodeScalarView } extension String {     subscript (_ i: Int) -> Character { get }     subscript (_ subRange: Range<Int>) -> String { get }     var count: Int { get } } extension String : MirrorPathType { } extension String {     init<T>(_ instance: T)     init<T>(reflecting subject: T) } ``` | Comparable, CustomDebugStringConvertible, Equatable, ExtendedGraphemeClusterLiteralConvertible, Hashable, MirrorPathType, OutputStreamType, Streamable, StringInterpolationConvertible, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

Modified [String.endIndex](https://developer.apple.com/documentation/swift/string/1539571-endindex)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var endIndex: String.Index { get } ``` | iOS 8.0 |
| To | ``` var endIndex: Index { get } ``` | iOS 9.0 |

Modified String.fromCString(_: UnsafePointer<CChar>) -> String? [static]

|  | Declaration |
| --- | --- |
| From | ``` static func fromCString(_ cs: UnsafePointer<CChar>) -> String? ``` |
| To | ``` @warn_unused_result     static func fromCString(_ cs: UnsafePointer<CChar>) -> String? ``` |

Modified String.fromCStringRepairingIllFormedUTF8(_: UnsafePointer<CChar>) -> (String?, hadError: Bool) [static]

|  | Declaration |
| --- | --- |
| From | ``` static func fromCStringRepairingIllFormedUTF8(_ cs: UnsafePointer<CChar>) -> (String?, hadError: Bool) ``` |
| To | ``` @warn_unused_result     static func fromCStringRepairingIllFormedUTF8(_ cs: UnsafePointer<CChar>) -> (String?, hadError: Bool) ``` |

Modified String.init<T : _SignedIntegerType>(_: T)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.1 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _SignedIntegerType ``` | T |

Modified String.init<S : SequenceType where S.Generator.Element == Character>(_: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` init<S : SequenceType where Character == Character>(_ characters: S) ``` | iOS 8.1 | ```  ``` | -- |
| To | ``` init<S : SequenceType where S.Generator.Element == Character>(_ characters: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Character ``` | S |

Modified String.init<T : _SignedIntegerType>(_: T, radix: Int, uppercase: Bool)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.1 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _SignedIntegerType ``` | T |

Modified String.init<T>(stringInterpolationSegment: T)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | T |

Modified [String.startIndex](https://developer.apple.com/documentation/swift/string/1540930-startindex)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var startIndex: String.Index { get } ``` | iOS 8.0 |
| To | ``` var startIndex: Index { get } ``` | iOS 9.0 |

Modified String.writeTo<Target : OutputStreamType>(_: Target)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.0 | ```  ``` | -- |
| To | iOS 9.0 | ``` Target : OutputStreamType ``` | Target |

Modified [String.UnicodeScalarView [struct]](https://developer.apple.com/documentation/swift/string/unicodescalarview)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnicodeScalarView : Sliceable, SequenceType, Reflectable, Printable, DebugPrintable {         struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.Generator         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } extension String.UnicodeScalarView : ExtensibleCollectionType {     init()     mutating func reserveCapacity(_ n: Int)     mutating func append(_ x: UnicodeScalar)     mutating func extend<S : SequenceType where UnicodeScalar == UnicodeScalar>(_ newElements: S) } extension String.UnicodeScalarView : RangeReplaceableCollectionType {     mutating func replaceRange<C : CollectionType where UnicodeScalar == UnicodeScalar>(_ subRange: Range<String.UnicodeScalarView.Index>, with newElements: C)     mutating func insert(_ newElement: UnicodeScalar, atIndex i: String.UnicodeScalarView.Index)     mutating func splice<S : CollectionType where UnicodeScalar == UnicodeScalar>(_ newElements: S, atIndex i: String.UnicodeScalarView.Index)     mutating func removeAtIndex(_ i: String.UnicodeScalarView.Index) -> UnicodeScalar     mutating func removeRange(_ subRange: Range<String.UnicodeScalarView.Index>)     mutating func removeAll(keepCapacity keepCapacity: Bool = default) } ``` | DebugPrintable, ExtensibleCollectionType, Printable, RangeReplaceableCollectionType, Reflectable, SequenceType, Sliceable |
| To | ``` struct UnicodeScalarView : CollectionType, Indexable, SequenceType, _Reflectable, CustomStringConvertible, CustomDebugStringConvertible {         struct Index : ForwardIndexType, _Incrementable, Equatable, BidirectionalIndexType, Comparable {             @warn_unused_result             func successor() -> String.UnicodeScalarView.Index             @warn_unused_result             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (_ position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (_ r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         @warn_unused_result         func generate() -> String.UnicodeScalarView.Generator         var description: String { get }         var debugDescription: String { get }     } extension String.UnicodeScalarView : RangeReplaceableCollectionType {     init()     mutating func reserveCapacity(_ n: Int)     mutating func append(_ x: UnicodeScalar)     mutating func appendContentsOf<S : SequenceType where S.Generator.Element == UnicodeScalar>(_ newElements: S)     mutating func replaceRange<C : CollectionType where C.Generator.Element == UnicodeScalar>(_ subRange: Range<String.UnicodeScalarView.Index>, with newElements: C) } ``` | CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Indexable, RangeReplaceableCollectionType, SequenceType |

Modified String.UnicodeScalarView.append(_: UnicodeScalar)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified String.UnicodeScalarView.generate() -> String.UnicodeScalarView.Generator

|  | Declaration |
| --- | --- |
| From | ``` func generate() -> String.UnicodeScalarView.Generator ``` |
| To | ``` @warn_unused_result         func generate() -> String.UnicodeScalarView.Generator ``` |

Modified String.UnicodeScalarView.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified String.UnicodeScalarView.reserveCapacity(_: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified String.UnicodeScalarView.subscript(_: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView

|  | Declaration |
| --- | --- |
| From | ``` subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get } ``` |
| To | ``` subscript (_ r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get } ``` |

Modified String.UnicodeScalarView.subscript(_: String.UnicodeScalarView.Index) -> UnicodeScalar

|  | Declaration |
| --- | --- |
| From | ``` subscript (position: String.UnicodeScalarView.Index) -> UnicodeScalar { get } ``` |
| To | ``` subscript (_ position: String.UnicodeScalarView.Index) -> UnicodeScalar { get } ``` |

Modified String.UnicodeScalarView.Index [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         } ``` | BidirectionalIndexType, Comparable |
| To | ``` struct Index : ForwardIndexType, _Incrementable, Equatable, BidirectionalIndexType, Comparable {             @warn_unused_result             func successor() -> String.UnicodeScalarView.Index             @warn_unused_result             func predecessor() -> String.UnicodeScalarView.Index         } ``` | BidirectionalIndexType, Comparable, Equatable, ForwardIndexType |

Modified String.UnicodeScalarView.Index.predecessor() -> String.UnicodeScalarView.Index

|  | Declaration |
| --- | --- |
| From | ``` func predecessor() -> String.UnicodeScalarView.Index ``` |
| To | ``` @warn_unused_result             func predecessor() -> String.UnicodeScalarView.Index ``` |

Modified String.UnicodeScalarView.Index.successor() -> String.UnicodeScalarView.Index

|  | Declaration |
| --- | --- |
| From | ``` func successor() -> String.UnicodeScalarView.Index ``` |
| To | ``` @warn_unused_result             func successor() -> String.UnicodeScalarView.Index ``` |

Modified [String.UTF16View [struct]](https://developer.apple.com/documentation/swift/string/utf16view)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF16View : Sliceable, Reflectable, Printable, DebugPrintable {         struct Index {         }         var startIndex: String.UTF16View.Index { get }         var endIndex: String.UTF16View.Index { get }         typealias Generator         func generate() -> Generator         subscript (i: String.UTF16View.Index) -> UInt16 { get }         subscript (i: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         subscript (subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get }         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | DebugPrintable, Printable, Reflectable, Sliceable |
| To | ``` struct UTF16View : CollectionType, Indexable, SequenceType, _Reflectable, CustomStringConvertible, CustomDebugStringConvertible {         struct Index {         }         var startIndex: String.UTF16View.Index { get }         var endIndex: String.UTF16View.Index { get }         subscript (_ i: String.UTF16View.Index) -> CodeUnit { get }         subscript (_ i: Int) -> CodeUnit { get }         subscript (_ subRange: Range<Int>) -> String.UTF16View { get }         subscript (_ subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get }         var description: String { get }         var debugDescription: String { get }     } ``` | CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Indexable, SequenceType |

Modified String.UTF16View.subscript(_: String.UTF16View.Index) -> CodeUnit

|  | Declaration |
| --- | --- |
| From | ``` subscript (i: String.UTF16View.Index) -> UInt16 { get } ``` |
| To | ``` subscript (_ i: String.UTF16View.Index) -> CodeUnit { get } ``` |

Modified String.UTF16View.subscript(_: Range<String.UTF16View.Index>) -> String.UTF16View

|  | Declaration |
| --- | --- |
| From | ``` subscript (subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get } ``` |
| To | ``` subscript (_ subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get } ``` |

Modified String.UTF16View.Index [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Index {         } extension String.UTF16View.Index : RandomAccessIndexType {     init(_ offset: Int)     func distanceTo(_ x: String.UTF16View.Index) -> Int     func advancedBy(_ x: Int) -> String.UTF16View.Index } extension String.UTF16View.Index : BidirectionalIndexType {     typealias Distance = Int     func successor() -> String.UTF16View.Index     func predecessor() -> String.UTF16View.Index } extension String.UTF16View.Index : Comparable { } extension String.UTF16View.Index {     init?(_ utf8Index: UTF8Index, within utf16: String.UTF16View)     init(_ unicodeScalarIndex: UnicodeScalarIndex, within utf16: String.UTF16View)     init(_ characterIndex: String.Index, within utf16: String.UTF16View)     func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index?     func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex?     func samePositionIn(_ characters: String) -> String.Index? } ``` | BidirectionalIndexType, Comparable, RandomAccessIndexType |
| To | ``` struct Index {         } extension String.UTF16View.Index : ForwardIndexType, _Incrementable, BidirectionalIndexType {     typealias Distance = Int     @warn_unused_result     func successor() -> String.UTF16View.Index     @warn_unused_result     func predecessor() -> String.UTF16View.Index } extension String.UTF16View.Index : Equatable, Comparable { } extension String.UTF16View.Index {     @warn_unused_result     func distanceTo(_ end: String.UTF16View.Index) -> Distance     @warn_unused_result     func advancedBy(_ n: Distance) -> String.UTF16View.Index     @warn_unused_result     func advancedBy(_ n: Distance, limit limit: String.UTF16View.Index) -> String.UTF16View.Index } extension String.UTF16View.Index {     init?(_ utf8Index: UTF8Index, within utf16: String.UTF16View)     init(_ unicodeScalarIndex: UnicodeScalarIndex, within utf16: String.UTF16View)     init(_ characterIndex: Index, within utf16: String.UTF16View)     @warn_unused_result     func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index?     @warn_unused_result     func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex?     @warn_unused_result     func samePositionIn(_ characters: String) -> Index? } ``` | BidirectionalIndexType, Comparable, Equatable, ForwardIndexType |

Modified String.UTF16View.Index.init(_: UTF8Index, within: String.UTF16View)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified String.UTF16View.Index.init(_: UnicodeScalarIndex, within: String.UTF16View)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified String.UTF16View.Index.predecessor() -> String.UTF16View.Index

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func predecessor() -> String.UTF16View.Index ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func predecessor() -> String.UTF16View.Index ``` | iOS 9.0 |

Modified String.UTF16View.Index.samePositionIn(_: String.UTF8View) -> String.UTF8View.Index?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index? ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index? ``` | iOS 9.0 |

Modified String.UTF16View.Index.samePositionIn(_: String.UnicodeScalarView) -> UnicodeScalarIndex?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex? ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex? ``` | iOS 9.0 |

Modified String.UTF16View.Index.successor() -> String.UTF16View.Index

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func successor() -> String.UTF16View.Index ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func successor() -> String.UTF16View.Index ``` | iOS 9.0 |

Modified [String.UTF8View [struct]](https://developer.apple.com/documentation/swift/string/utf8view)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF8View : CollectionType, Reflectable, Printable, DebugPrintable {         struct Index : ForwardIndexType {             typealias Buffer = UTF8Chunk             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (position: String.UTF8View.Index) -> CodeUnit { get }         subscript (subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | CollectionType, DebugPrintable, Printable, Reflectable |
| To | ``` struct UTF8View : CollectionType, Indexable, SequenceType, _Reflectable, CustomStringConvertible, CustomDebugStringConvertible {         struct Index : ForwardIndexType, _Incrementable, Equatable {             @warn_unused_result             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (_ position: String.UTF8View.Index) -> CodeUnit { get }         subscript (_ subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get }         var description: String { get }         var debugDescription: String { get }     } ``` | CollectionType, CustomDebugStringConvertible, CustomStringConvertible, Indexable, SequenceType |

Modified String.UTF8View.subscript(_: String.UTF8View.Index) -> CodeUnit

|  | Declaration |
| --- | --- |
| From | ``` subscript (position: String.UTF8View.Index) -> CodeUnit { get } ``` |
| To | ``` subscript (_ position: String.UTF8View.Index) -> CodeUnit { get } ``` |

Modified String.UTF8View.subscript(_: Range<String.UTF8View.Index>) -> String.UTF8View

|  | Declaration |
| --- | --- |
| From | ``` subscript (subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get } ``` |
| To | ``` subscript (_ subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get } ``` |

Modified String.UTF8View.Index [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Index : ForwardIndexType {             typealias Buffer = UTF8Chunk             func successor() -> String.UTF8View.Index         } extension String.UTF8View.Index {     init?(_ utf16Index: UTF16Index, within utf8: String.UTF8View)     init(_ unicodeScalarIndex: UnicodeScalarIndex, within utf8: String.UTF8View)     init(_ characterIndex: String.Index, within utf8: String.UTF8View)     func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index?     func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex?     func samePositionIn(_ characters: String) -> String.Index? } ``` | ForwardIndexType |
| To | ``` struct Index : ForwardIndexType, _Incrementable, Equatable {             @warn_unused_result             func successor() -> String.UTF8View.Index         } extension String.UTF8View.Index {     init?(_ utf16Index: UTF16Index, within utf8: String.UTF8View)     init(_ unicodeScalarIndex: UnicodeScalarIndex, within utf8: String.UTF8View)     init(_ characterIndex: Index, within utf8: String.UTF8View)     @warn_unused_result     func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index?     @warn_unused_result     func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex?     @warn_unused_result     func samePositionIn(_ characters: String) -> Index? } ``` | Equatable, ForwardIndexType |

Modified String.UTF8View.Index.init(_: UTF16Index, within: String.UTF8View)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified String.UTF8View.Index.init(_: UnicodeScalarIndex, within: String.UTF8View)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified String.UTF8View.Index.samePositionIn(_: String.UTF16View) -> String.UTF16View.Index?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index? ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index? ``` | iOS 9.0 |

Modified String.UTF8View.Index.samePositionIn(_: String.UnicodeScalarView) -> UnicodeScalarIndex?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex? ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func samePositionIn(_ unicodeScalars: String.UnicodeScalarView) -> UnicodeScalarIndex? ``` | iOS 9.0 |

Modified String.UTF8View.Index.successor() -> String.UTF8View.Index

|  | Declaration |
| --- | --- |
| From | ``` func successor() -> String.UTF8View.Index ``` |
| To | ``` @warn_unused_result             func successor() -> String.UTF8View.Index ``` |

Modified StringInterpolationConvertible.init(stringInterpolation: Self)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified StringInterpolationConvertible.init<T>(stringInterpolationSegment: T)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | T |

Modified StringLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol StringLiteralConvertible : ExtendedGraphemeClusterLiteralConvertible {     typealias StringLiteralType     init(stringLiteral value: StringLiteralType) } ``` |
| To | ``` protocol StringLiteralConvertible : ExtendedGraphemeClusterLiteralConvertible {     typealias StringLiteralType     init(stringLiteral value: Self.StringLiteralType) } ``` |

Modified StringLiteralConvertible.init(stringLiteral: Self.StringLiteralType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(stringLiteral value: StringLiteralType) ``` | iOS 8.1 |
| To | ``` init(stringLiteral value: Self.StringLiteralType) ``` | iOS 9.0 |

Modified [UInt [struct]](https://developer.apple.com/documentation/swift/uint)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt : UnsignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } extension UInt {     init(_ value: CGFloat) } extension UInt : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension UInt : Hashable {     var hashValue: Int { get } } extension UInt : Printable {     var description: String { get } } extension UInt : RandomAccessIndexType {     func successor() -> UInt     func predecessor() -> UInt     func distanceTo(_ other: UInt) -> Distance     func advancedBy(_ amount: Distance) -> UInt } extension UInt {     static func addWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: Int)     init(bitPattern bitPattern: Int) } extension UInt : BitwiseOperationsType {     static var allZeros: UInt { get } } extension UInt {     init(_ other: Float)     init(_ other: Double) } extension UInt : Reflectable {     func getMirror() -> MirrorType } extension UInt : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |
| To | ``` struct UInt : _IntegerArithmeticType, Comparable, Equatable, _DisallowMixedSignArithmetic, _IntegerType, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, UnsignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } extension UInt {     init(_ value: CGFloat) } extension UInt : _ObjectiveCBridgeable {     init(_ number: NSNumber) } extension UInt : Hashable {     var hashValue: Int { get } } extension UInt : CustomStringConvertible {     var description: String { get } } extension UInt : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> UInt     func predecessor() -> UInt     func distanceTo(_ other: UInt) -> Distance     func advancedBy(_ n: Distance) -> UInt } extension UInt {     static func addWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt, _ rhs: UInt) -> (UInt, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: Int)     init(bitPattern bitPattern: Int) } extension UInt : BitwiseOperationsType {     static var allZeros: UInt { get } } extension UInt {     init(_ other: Float)     init(_ other: Double) } extension UInt {     init?(_ text: String, radix radix: Int = default) } extension UInt : _Reflectable { } extension UInt : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, Strideable, UnsignedIntegerType |

Modified UInt16 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt16 : UnsignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt16)     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } extension UInt16 {     init(_ value: CGFloat) } extension UInt16 : Hashable {     var hashValue: Int { get } } extension UInt16 : Printable {     var description: String { get } } extension UInt16 : RandomAccessIndexType {     func successor() -> UInt16     func predecessor() -> UInt16     func distanceTo(_ other: UInt16) -> Distance     func advancedBy(_ amount: Distance) -> UInt16 } extension UInt16 {     static func addWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int16) } extension UInt16 : BitwiseOperationsType {     static var allZeros: UInt16 { get } } extension UInt16 {     init(_ other: Float)     init(_ other: Double) } extension UInt16 : Reflectable {     func getMirror() -> MirrorType } extension UInt16 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |
| To | ``` struct UInt16 : _IntegerArithmeticType, Comparable, Equatable, _DisallowMixedSignArithmetic, _IntegerType, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, UnsignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt16)     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } extension UInt16 {     init(_ value: CGFloat) } extension UInt16 : Hashable {     var hashValue: Int { get } } extension UInt16 : CustomStringConvertible {     var description: String { get } } extension UInt16 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> UInt16     func predecessor() -> UInt16     func distanceTo(_ other: UInt16) -> Distance     func advancedBy(_ n: Distance) -> UInt16 } extension UInt16 {     static func addWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt16, _ rhs: UInt16) -> (UInt16, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt16 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int16) } extension UInt16 : BitwiseOperationsType {     static var allZeros: UInt16 { get } } extension UInt16 {     init(_ other: Float)     init(_ other: Double) } extension UInt16 {     init?(_ text: String, radix radix: Int = default) } extension UInt16 : _Reflectable { } extension UInt16 : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, Strideable, UnsignedIntegerType |

Modified UInt32 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt32 : UnsignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt32)     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } extension UInt32 {     init(_ value: CGFloat) } extension UInt32 : Hashable {     var hashValue: Int { get } } extension UInt32 : Printable {     var description: String { get } } extension UInt32 : RandomAccessIndexType {     func successor() -> UInt32     func predecessor() -> UInt32     func distanceTo(_ other: UInt32) -> Distance     func advancedBy(_ amount: Distance) -> UInt32 } extension UInt32 {     static func addWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int32) } extension UInt32 : BitwiseOperationsType {     static var allZeros: UInt32 { get } } extension UInt32 {     init(_ other: Float)     init(_ other: Double) } extension UInt32 : Reflectable {     func getMirror() -> MirrorType } extension UInt32 {     init(_ v: UnicodeScalar) } extension UInt32 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |
| To | ``` struct UInt32 : _IntegerArithmeticType, Comparable, Equatable, _DisallowMixedSignArithmetic, _IntegerType, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, UnsignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt32)     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } extension UInt32 {     init(_ value: CGFloat) } extension UInt32 : Hashable {     var hashValue: Int { get } } extension UInt32 : CustomStringConvertible {     var description: String { get } } extension UInt32 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> UInt32     func predecessor() -> UInt32     func distanceTo(_ other: UInt32) -> Distance     func advancedBy(_ n: Distance) -> UInt32 } extension UInt32 {     static func addWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt32, _ rhs: UInt32) -> (UInt32, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt32 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int32) } extension UInt32 : BitwiseOperationsType {     static var allZeros: UInt32 { get } } extension UInt32 {     init(_ other: Float)     init(_ other: Double) } extension UInt32 {     init?(_ text: String, radix radix: Int = default) } extension UInt32 : _Reflectable { } extension UInt32 {     init(_ v: UnicodeScalar) } extension UInt32 : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, Strideable, UnsignedIntegerType |

Modified UInt64 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt64 : UnsignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt64)     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } extension UInt64 {     init(_ value: CGFloat) } extension UInt64 : Hashable {     var hashValue: Int { get } } extension UInt64 : Printable {     var description: String { get } } extension UInt64 : RandomAccessIndexType {     func successor() -> UInt64     func predecessor() -> UInt64     func distanceTo(_ other: UInt64) -> Distance     func advancedBy(_ amount: Distance) -> UInt64 } extension UInt64 {     static func addWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: Int64) } extension UInt64 : BitwiseOperationsType {     static var allZeros: UInt64 { get } } extension UInt64 {     init(_ other: Float)     init(_ other: Double) } extension UInt64 : Reflectable {     func getMirror() -> MirrorType } extension UInt64 {     init(_ v: UnicodeScalar) } extension UInt64 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |
| To | ``` struct UInt64 : _IntegerArithmeticType, Comparable, Equatable, _DisallowMixedSignArithmetic, _IntegerType, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, UnsignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt64)     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } extension UInt64 {     init(_ value: CGFloat) } extension UInt64 : Hashable {     var hashValue: Int { get } } extension UInt64 : CustomStringConvertible {     var description: String { get } } extension UInt64 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> UInt64     func predecessor() -> UInt64     func distanceTo(_ other: UInt64) -> Distance     func advancedBy(_ n: Distance) -> UInt64 } extension UInt64 {     static func addWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt64, _ rhs: UInt64) -> (UInt64, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt64 {     init(_ v: UInt8)     init(_ v: Int8)     init(_ v: UInt16)     init(_ v: Int16)     init(_ v: UInt32)     init(_ v: Int32)     init(_ v: Int64)     init(_ v: UInt)     init(_ v: Int)     init(bitPattern bitPattern: Int64) } extension UInt64 : BitwiseOperationsType {     static var allZeros: UInt64 { get } } extension UInt64 {     init(_ other: Float)     init(_ other: Double) } extension UInt64 {     init?(_ text: String, radix radix: Int = default) } extension UInt64 : _Reflectable { } extension UInt64 {     init(_ v: UnicodeScalar) } extension UInt64 : CVarArgType, _CVarArgAlignedType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, Strideable, UnsignedIntegerType |

Modified UInt8 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt8 : UnsignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: UInt8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt8)     static var max: UInt8 { get }     static var min: UInt8 { get } } extension UInt8 {     init(_ value: CGFloat) } extension UInt8 : Hashable {     var hashValue: Int { get } } extension UInt8 : Printable {     var description: String { get } } extension UInt8 : RandomAccessIndexType {     func successor() -> UInt8     func predecessor() -> UInt8     func distanceTo(_ other: UInt8) -> Distance     func advancedBy(_ amount: Distance) -> UInt8 } extension UInt8 {     static func addWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt8 {     init(_ v: Int8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int8) } extension UInt8 : BitwiseOperationsType {     static var allZeros: UInt8 { get } } extension UInt8 {     init(_ other: Float)     init(_ other: Double) } extension UInt8 : Reflectable {     func getMirror() -> MirrorType } extension UInt8 {     init(ascii v: UnicodeScalar) } extension UInt8 : CVarArgType {     func encode() -> [Word] } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |
| To | ``` struct UInt8 : _IntegerArithmeticType, Comparable, Equatable, _DisallowMixedSignArithmetic, _IntegerType, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, UnsignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: UInt8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt8)     static var max: UInt8 { get }     static var min: UInt8 { get } } extension UInt8 {     init(_ value: CGFloat) } extension UInt8 : Hashable {     var hashValue: Int { get } } extension UInt8 : CustomStringConvertible {     var description: String { get } } extension UInt8 : _Incrementable, RandomAccessIndexType, BidirectionalIndexType, ForwardIndexType, Strideable, _Strideable, _RandomAccessAmbiguity {     func successor() -> UInt8     func predecessor() -> UInt8     func distanceTo(_ other: UInt8) -> Distance     func advancedBy(_ n: Distance) -> UInt8 } extension UInt8 {     static func addWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func subtractWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func multiplyWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func divideWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     static func remainderWithOverflow(_ lhs: UInt8, _ rhs: UInt8) -> (UInt8, overflow: Bool)     func toUIntMax() -> UIntMax     func toIntMax() -> IntMax } extension UInt8 {     init(_ v: Int8)     init(_ v: UInt16)     init(truncatingBitPattern truncatingBitPattern: UInt16)     init(_ v: Int16)     init(truncatingBitPattern truncatingBitPattern: Int16)     init(_ v: UInt32)     init(truncatingBitPattern truncatingBitPattern: UInt32)     init(_ v: Int32)     init(truncatingBitPattern truncatingBitPattern: Int32)     init(_ v: UInt64)     init(truncatingBitPattern truncatingBitPattern: UInt64)     init(_ v: Int64)     init(truncatingBitPattern truncatingBitPattern: Int64)     init(_ v: UInt)     init(truncatingBitPattern truncatingBitPattern: UInt)     init(_ v: Int)     init(truncatingBitPattern truncatingBitPattern: Int)     init(bitPattern bitPattern: Int8) } extension UInt8 : BitwiseOperationsType {     static var allZeros: UInt8 { get } } extension UInt8 {     init(_ other: Float)     init(_ other: Double) } extension UInt8 {     init?(_ text: String, radix radix: Int = default) } extension UInt8 : _Reflectable { } extension UInt8 {     init(ascii v: UnicodeScalar) } extension UInt8 : CVarArgType { } ``` | BidirectionalIndexType, BitwiseOperationsType, CVarArgType, Comparable, CustomStringConvertible, Equatable, ForwardIndexType, Hashable, IntegerArithmeticType, IntegerLiteralConvertible, IntegerType, RandomAccessIndexType, Strideable, UnsignedIntegerType |

Modified UnicodeCodecType

|  | Declaration |
| --- | --- |
| From | ``` protocol UnicodeCodecType {     typealias CodeUnit     init()     mutating func decode<G : GeneratorType where Self.CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode<S : SinkType where Self.CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` |
| To | ``` protocol UnicodeCodecType {     typealias CodeUnit     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output output: (Self.CodeUnit) -> ()) } ``` |

Modified UnicodeCodecType.decode<G : GeneratorType where G.Element == CodeUnit>(_: G) -> UnicodeDecodingResult

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func decode<G : GeneratorType where Self.CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` | iOS 9.0 | ``` G : GeneratorType, G.Element == CodeUnit ``` | G |

Modified UnicodeCodecType.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnicodeDecodingResult [enum]

|  | Declaration |
| --- | --- |
| From | ``` enum UnicodeDecodingResult {     case Result(UnicodeScalar)     case EmptyInput     case Error     func isEmptyInput() -> Bool } ``` |
| To | ``` enum UnicodeDecodingResult {     case Result(UnicodeScalar)     case EmptyInput     case Error     @warn_unused_result     func isEmptyInput() -> Bool } ``` |

Modified UnicodeDecodingResult.isEmptyInput() -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isEmptyInput() -> Bool ``` |
| To | ``` @warn_unused_result     func isEmptyInput() -> Bool ``` |

Modified [UnicodeScalar [struct]](https://developer.apple.com/documentation/swift/unicodescalar)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnicodeScalar : UnicodeScalarLiteralConvertible {     var value: UInt32 { get }     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: UnicodeScalar)     init()     init(_ value: Builtin.Int32)     init(_ v: UInt32)     init(_ v: UInt16)     init(_ v: UInt8)     init(_ v: UnicodeScalar)     func escape(asASCII asASCII: Bool) -> String     func isASCII() -> Bool } extension UnicodeScalar : Reflectable {     func getMirror() -> MirrorType } extension UnicodeScalar : Streamable {     func writeTo<Target : OutputStreamType>(inout _ target: Target) } extension UnicodeScalar : Printable, DebugPrintable {     var description: String { get }     var debugDescription: String { get } } extension UnicodeScalar : Hashable {     var hashValue: Int { get } } extension UnicodeScalar {     init(_ v: Int) } extension UnicodeScalar : Comparable { } extension UnicodeScalar {     struct UTF16View {         var value: UnicodeScalar     }     var utf16: UnicodeScalar.UTF16View { get } } ``` | Comparable, DebugPrintable, Hashable, Printable, Reflectable, Streamable, UnicodeScalarLiteralConvertible |
| To | ``` struct UnicodeScalar : UnicodeScalarLiteralConvertible {     var value: UInt32 { get }     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: UnicodeScalar)     init()     init(_ v: UInt32)     init(_ v: UInt16)     init(_ v: UInt8)     init(_ v: UnicodeScalar)     @warn_unused_result     func escape(asASCII forceASCII: Bool) -> String     @warn_unused_result     func isASCII() -> Bool } extension UnicodeScalar : _Reflectable { } extension UnicodeScalar : Streamable {     func writeTo<Target : OutputStreamType>(inout _ target: Target) } extension UnicodeScalar : CustomStringConvertible, CustomDebugStringConvertible {     var description: String { get }     var debugDescription: String { get } } extension UnicodeScalar : Hashable {     var hashValue: Int { get } } extension UnicodeScalar {     init(_ v: Int) } extension UnicodeScalar : Equatable, Comparable { } ``` | Comparable, CustomDebugStringConvertible, CustomStringConvertible, Equatable, Hashable, Streamable, UnicodeScalarLiteralConvertible |

Modified UnicodeScalar.escape(asASCII: Bool) -> String

|  | Declaration |
| --- | --- |
| From | ``` func escape(asASCII asASCII: Bool) -> String ``` |
| To | ``` @warn_unused_result     func escape(asASCII forceASCII: Bool) -> String ``` |

Modified UnicodeScalar.isASCII() -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func isASCII() -> Bool ``` |
| To | ``` @warn_unused_result     func isASCII() -> Bool ``` |

Modified UnicodeScalar.writeTo<Target : OutputStreamType>(_: Target)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.0 | ```  ``` | -- |
| To | iOS 9.0 | ``` Target : OutputStreamType ``` | Target |

Modified UnicodeScalarIndex.samePositionIn(_: String.UTF16View) -> String.UTF16View.Index

|  | Declaration |
| --- | --- |
| From | ``` func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index ``` |
| To | ``` @warn_unused_result     func samePositionIn(_ utf16: String.UTF16View) -> String.UTF16View.Index ``` |

Modified UnicodeScalarIndex.samePositionIn(_: String.UTF8View) -> String.UTF8View.Index

|  | Declaration |
| --- | --- |
| From | ``` func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index ``` |
| To | ``` @warn_unused_result     func samePositionIn(_ utf8: String.UTF8View) -> String.UTF8View.Index ``` |

Modified UnicodeScalarLiteralConvertible

|  | Declaration |
| --- | --- |
| From | ``` protocol UnicodeScalarLiteralConvertible {     typealias UnicodeScalarLiteralType     init(unicodeScalarLiteral value: UnicodeScalarLiteralType) } ``` |
| To | ``` protocol UnicodeScalarLiteralConvertible {     typealias UnicodeScalarLiteralType     init(unicodeScalarLiteral value: Self.UnicodeScalarLiteralType) } ``` |

Modified UnicodeScalarLiteralConvertible.init(unicodeScalarLiteral: Self.UnicodeScalarLiteralType)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(unicodeScalarLiteral value: UnicodeScalarLiteralType) ``` | iOS 8.1 |
| To | ``` init(unicodeScalarLiteral value: Self.UnicodeScalarLiteralType) ``` | iOS 9.0 |

Modified Unmanaged [struct]

|  | Declaration | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct Unmanaged<T> {     static func fromOpaque(_ value: COpaquePointer) -> Unmanaged<T>     func toOpaque() -> COpaquePointer     static func passRetained(_ value: T) -> Unmanaged<T>     static func passUnretained(_ value: T) -> Unmanaged<T>     func takeUnretainedValue() -> T     func takeRetainedValue() -> T     func retain() -> Unmanaged<T>     func release()     func autorelease() -> Unmanaged<T> } ``` | ```  ``` | -- |
| To | ``` struct Unmanaged<Instance> {     typealias T = Instance     @warn_unused_result     static func fromOpaque(_ value: COpaquePointer) -> Unmanaged<Instance>     @warn_unused_result     func toOpaque() -> COpaquePointer     @warn_unused_result     static func passRetained(_ value: Instance) -> Unmanaged<Instance>     @warn_unused_result     static func passUnretained(_ value: Instance) -> Unmanaged<Instance>     @warn_unused_result     func takeUnretainedValue() -> Instance     @warn_unused_result     func takeRetainedValue() -> Instance     func retain() -> Unmanaged<Instance>     func release()     func autorelease() -> Unmanaged<Instance> } ``` | ``` Instance : AnyObject ``` | Instance |

Modified Unmanaged.autorelease() -> Unmanaged<Instance>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func autorelease() -> Unmanaged<T> ``` | iOS 8.0 |
| To | ``` func autorelease() -> Unmanaged<Instance> ``` | iOS 9.0 |

Modified Unmanaged.fromOpaque(_: COpaquePointer) -> Unmanaged<Instance> [static]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` static func fromOpaque(_ value: COpaquePointer) -> Unmanaged<T> ``` | iOS 8.3 |
| To | ``` @warn_unused_result     static func fromOpaque(_ value: COpaquePointer) -> Unmanaged<Instance> ``` | iOS 9.0 |

Modified Unmanaged.passRetained(_: Instance) -> Unmanaged<Instance> [static]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` static func passRetained(_ value: T) -> Unmanaged<T> ``` | iOS 8.3 |
| To | ``` @warn_unused_result     static func passRetained(_ value: Instance) -> Unmanaged<Instance> ``` | iOS 9.0 |

Modified Unmanaged.passUnretained(_: Instance) -> Unmanaged<Instance> [static]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` static func passUnretained(_ value: T) -> Unmanaged<T> ``` | iOS 8.3 |
| To | ``` @warn_unused_result     static func passUnretained(_ value: Instance) -> Unmanaged<Instance> ``` | iOS 9.0 |

Modified Unmanaged.release()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified Unmanaged.retain() -> Unmanaged<Instance>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func retain() -> Unmanaged<T> ``` | iOS 8.0 |
| To | ``` func retain() -> Unmanaged<Instance> ``` | iOS 9.0 |

Modified Unmanaged.takeRetainedValue() -> Instance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func takeRetainedValue() -> T ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func takeRetainedValue() -> Instance ``` | iOS 9.0 |

Modified Unmanaged.takeUnretainedValue() -> Instance

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func takeUnretainedValue() -> T ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func takeUnretainedValue() -> Instance ``` | iOS 9.0 |

Modified Unmanaged.toOpaque() -> COpaquePointer

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func toOpaque() -> COpaquePointer ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func toOpaque() -> COpaquePointer ``` | iOS 9.0 |

Modified UnsafeBufferPointer [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct UnsafeBufferPointer<T> : CollectionType {     var startIndex: Int { get }     var endIndex: Int { get }     subscript (i: Int) -> T { get }     init(start start: UnsafePointer<T>, count count: Int)     func generate() -> UnsafeBufferPointerGenerator<T>     var baseAddress: UnsafePointer<T> { get }     var count: Int { get } } extension UnsafeBufferPointer {     init(_ audioBuffer: AudioBuffer) } extension UnsafeBufferPointer : DebugPrintable {     var debugDescription: String { get } } ``` | CollectionType, DebugPrintable | -- |
| To | ``` struct UnsafeBufferPointer<Element> : CollectionType, Indexable, SequenceType {     typealias T = Element     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ i: Int) -> Element { get }     init(start start: UnsafePointer<Element>, count count: Int)     func generate() -> UnsafeBufferPointerGenerator<Element>     var baseAddress: UnsafePointer<Element> { get }     var count: Int { get } } extension UnsafeBufferPointer {     init(_ audioBuffer: AudioBuffer) } extension UnsafeBufferPointer : CustomDebugStringConvertible {     var debugDescription: String { get } } ``` | CollectionType, CustomDebugStringConvertible, Indexable, SequenceType | Element |

Modified UnsafeBufferPointer.baseAddress

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var baseAddress: UnsafePointer<T> { get } ``` | iOS 8.0 |
| To | ``` var baseAddress: UnsafePointer<Element> { get } ``` | iOS 9.0 |

Modified UnsafeBufferPointer.generate() -> UnsafeBufferPointerGenerator<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> UnsafeBufferPointerGenerator<T> ``` | iOS 8.0 |
| To | ``` func generate() -> UnsafeBufferPointerGenerator<Element> ``` | iOS 9.0 |

Modified UnsafeBufferPointer.init(start: UnsafePointer<Element>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(start start: UnsafePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` init(start start: UnsafePointer<Element>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeBufferPointer.subscript(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (i: Int) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ i: Int) -> Element { get } ``` | iOS 9.0 |

Modified UnsafeBufferPointerGenerator [struct]

|  | Declaration | Generics[Parameters] |
| --- | --- | --- |
| From | ``` struct UnsafeBufferPointerGenerator<T> : GeneratorType, SequenceType {     mutating func next() -> T?     func generate() -> UnsafeBufferPointerGenerator<T>     var position: UnsafePointer<T>     var end: UnsafePointer<T> } ``` | -- |
| To | ``` struct UnsafeBufferPointerGenerator<Element> : GeneratorType, SequenceType {     typealias T = Element     mutating func next() -> Element? } ``` | Element |

Modified UnsafeBufferPointerGenerator.next() -> Element?

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` mutating func next() -> T? ``` | iOS 8.0 |
| To | ``` mutating func next() -> Element? ``` | iOS 9.0 |

Modified UnsafeMutableBufferPointer [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct UnsafeMutableBufferPointer<T> : MutableCollectionType {     var startIndex: Int { get }     var endIndex: Int { get }     subscript (i: Int) -> T { get nonmutating set }     init(start start: UnsafeMutablePointer<T>, count count: Int)     func generate() -> UnsafeBufferPointerGenerator<T>     var baseAddress: UnsafeMutablePointer<T> { get }     var count: Int { get } } extension UnsafeMutableBufferPointer {     init(_ audioBuffer: AudioBuffer) } extension UnsafeMutableBufferPointer : DebugPrintable {     var debugDescription: String { get } } ``` | DebugPrintable, MutableCollectionType | -- |
| To | ``` struct UnsafeMutableBufferPointer<Element> : MutableCollectionType, CollectionType, Indexable, SequenceType, MutableIndexable {     typealias T = Element     var startIndex: Int { get }     var endIndex: Int { get }     subscript (_ i: Int) -> Element { get nonmutating set }     init(start start: UnsafeMutablePointer<Element>, count count: Int)     func generate() -> UnsafeBufferPointerGenerator<Element>     var baseAddress: UnsafeMutablePointer<Element> { get }     var count: Int { get } } extension UnsafeMutableBufferPointer {     init(_ audioBuffer: AudioBuffer) } extension UnsafeMutableBufferPointer : CustomDebugStringConvertible {     var debugDescription: String { get } } ``` | CollectionType, CustomDebugStringConvertible, Indexable, MutableCollectionType, MutableIndexable, SequenceType | Element |

Modified UnsafeMutableBufferPointer.baseAddress

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var baseAddress: UnsafeMutablePointer<T> { get } ``` | iOS 8.0 |
| To | ``` var baseAddress: UnsafeMutablePointer<Element> { get } ``` | iOS 9.0 |

Modified UnsafeMutableBufferPointer.generate() -> UnsafeBufferPointerGenerator<Element>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func generate() -> UnsafeBufferPointerGenerator<T> ``` | iOS 8.0 |
| To | ``` func generate() -> UnsafeBufferPointerGenerator<Element> ``` | iOS 9.0 |

Modified UnsafeMutableBufferPointer.init(start: UnsafeMutablePointer<Element>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(start start: UnsafeMutablePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` init(start start: UnsafeMutablePointer<Element>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeMutableBufferPointer.subscript(_: Int) -> Element

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (i: Int) -> T { get nonmutating set } ``` | iOS 8.0 |
| To | ``` subscript (_ i: Int) -> Element { get nonmutating set } ``` | iOS 9.0 |

Modified UnsafeMutablePointer [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct UnsafeMutablePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     init()     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafeMutablePointer<T>     static func alloc(_ num: Int) -> UnsafeMutablePointer<T>     func dealloc(_ num: Int)     var memory: T { get nonmutating set }     func initialize(_ newvalue: T)     func move() -> T     func assignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func assignBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveInitializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func initializeFrom<C : CollectionType where T == T>(_ source: C)     func moveAssignFrom(_ source: UnsafeMutablePointer<T>, count count: Int)     func destroy()     func destroy(_ count: Int)     subscript (i: Int) -> T { get nonmutating set }     var hashValue: Int { get }     func successor() -> UnsafeMutablePointer<T>     func predecessor() -> UnsafeMutablePointer<T>     func distanceTo(_ x: UnsafeMutablePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafeMutablePointer<T> } extension UnsafeMutablePointer : DebugPrintable {     var debugDescription: String { get } } extension UnsafeMutablePointer : Reflectable {     func getMirror() -> MirrorType } extension UnsafeMutablePointer : SinkType {     mutating func put(_ x: T) } extension UnsafeMutablePointer : CVarArgType {     func encode() -> [Word] } ``` | CVarArgType, DebugPrintable, Hashable, NilLiteralConvertible, RandomAccessIndexType, Reflectable, SinkType | -- |
| To | ``` struct UnsafeMutablePointer<Memory> : Equatable, Hashable, NilLiteralConvertible, _PointerType, BidirectionalIndexType, ForwardIndexType, _Incrementable, RandomAccessIndexType, Strideable, Comparable, _Strideable, _RandomAccessAmbiguity {     typealias T = Memory     typealias Distance = Int     init()     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Int)     init(bitPattern bitPattern: UInt)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     @warn_unused_result     static func alloc(_ num: Int) -> UnsafeMutablePointer<Memory>     func dealloc(_ num: Int)     var memory: Memory { get nonmutating set }     func initialize(_ newvalue: Memory)     @warn_unused_result     func move() -> Memory     func assignFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int)     func assignBackwardFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int)     func moveInitializeFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int)     func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int)     func initializeFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int)     func initializeFrom<C : CollectionType where C.Generator.Element == Memory>(_ source: C)     func moveAssignFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int)     func destroy()     func destroy(_ count: Int)     subscript (_ i: Int) -> Memory { get nonmutating set }     var hashValue: Int { get }     func successor() -> UnsafeMutablePointer<Memory>     func predecessor() -> UnsafeMutablePointer<Memory>     func distanceTo(_ x: UnsafeMutablePointer<Memory>) -> Int     func advancedBy(_ n: Int) -> UnsafeMutablePointer<Memory> } extension UnsafeMutablePointer : CustomDebugStringConvertible {     var debugDescription: String { get } } extension UnsafeMutablePointer : _Reflectable { } extension UnsafeMutablePointer : CVarArgType { } ``` | BidirectionalIndexType, CVarArgType, Comparable, CustomDebugStringConvertible, Equatable, ForwardIndexType, Hashable, NilLiteralConvertible, RandomAccessIndexType, Strideable | Memory |

Modified UnsafeMutablePointer.advancedBy(_: Int) -> UnsafeMutablePointer<Memory>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ n: Int) -> UnsafeMutablePointer<T> ``` | iOS 8.0 |
| To | ``` func advancedBy(_ n: Int) -> UnsafeMutablePointer<Memory> ``` | iOS 9.0 |

Modified UnsafeMutablePointer.alloc(_: Int) -> UnsafeMutablePointer<Memory> [static]

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` static func alloc(_ num: Int) -> UnsafeMutablePointer<T> ``` | iOS 8.3 |
| To | ``` @warn_unused_result     static func alloc(_ num: Int) -> UnsafeMutablePointer<Memory> ``` | iOS 9.0 |

Modified UnsafeMutablePointer.assignBackwardFrom(_: UnsafeMutablePointer<Memory>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func assignBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` func assignBackwardFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.assignFrom(_: UnsafeMutablePointer<Memory>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func assignFrom(_ source: UnsafeMutablePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` func assignFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.dealloc(_: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnsafeMutablePointer.destroy()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnsafeMutablePointer.destroy(_: Int)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnsafeMutablePointer.distanceTo(_: UnsafeMutablePointer<Memory>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ x: UnsafeMutablePointer<T>) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ x: UnsafeMutablePointer<Memory>) -> Int ``` | iOS 9.0 |

Modified UnsafeMutablePointer.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnsafeMutablePointer.init(_: COpaquePointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnsafeMutablePointer.init<U>(_: UnsafeMutablePointer<U>)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | U |

Modified UnsafeMutablePointer.init<U>(_: UnsafePointer<U>)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | U |

Modified UnsafeMutablePointer.init(bitPattern: UInt)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(bitPattern bitPattern: UWord) ``` | iOS 8.0 |
| To | ``` init(bitPattern bitPattern: UInt) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.init(bitPattern: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(bitPattern bitPattern: Word) ``` | iOS 8.0 |
| To | ``` init(bitPattern bitPattern: Int) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.init(nilLiteral: ())

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified UnsafeMutablePointer.initialize(_: Memory)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func initialize(_ newvalue: T) ``` | iOS 8.0 |
| To | ``` func initialize(_ newvalue: Memory) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.initializeFrom(_: UnsafeMutablePointer<Memory>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func initializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` func initializeFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.memory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var memory: T { get nonmutating set } ``` | iOS 8.0 |
| To | ``` var memory: Memory { get nonmutating set } ``` | iOS 9.0 |

Modified UnsafeMutablePointer.move() -> Memory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func move() -> T ``` | iOS 8.0 |
| To | ``` @warn_unused_result     func move() -> Memory ``` | iOS 9.0 |

Modified UnsafeMutablePointer.moveAssignFrom(_: UnsafeMutablePointer<Memory>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func moveAssignFrom(_ source: UnsafeMutablePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` func moveAssignFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.moveInitializeBackwardFrom(_: UnsafeMutablePointer<Memory>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` func moveInitializeBackwardFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.moveInitializeFrom(_: UnsafeMutablePointer<Memory>, count: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func moveInitializeFrom(_ source: UnsafeMutablePointer<T>, count count: Int) ``` | iOS 8.0 |
| To | ``` func moveInitializeFrom(_ source: UnsafeMutablePointer<Memory>, count count: Int) ``` | iOS 9.0 |

Modified UnsafeMutablePointer.predecessor() -> UnsafeMutablePointer<Memory>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func predecessor() -> UnsafeMutablePointer<T> ``` | iOS 8.0 |
| To | ``` func predecessor() -> UnsafeMutablePointer<Memory> ``` | iOS 9.0 |

Modified UnsafeMutablePointer.subscript(_: Int) -> Memory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (i: Int) -> T { get nonmutating set } ``` | iOS 8.0 |
| To | ``` subscript (_ i: Int) -> Memory { get nonmutating set } ``` | iOS 9.0 |

Modified UnsafeMutablePointer.successor() -> UnsafeMutablePointer<Memory>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func successor() -> UnsafeMutablePointer<T> ``` | iOS 8.0 |
| To | ``` func successor() -> UnsafeMutablePointer<Memory> ``` | iOS 9.0 |

Modified UnsafePointer [struct]

|  | Declaration | Protocols | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` struct UnsafePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     init()     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafePointer<T>     var memory: T { get }     subscript (i: Int) -> T { get }     var hashValue: Int { get }     func successor() -> UnsafePointer<T>     func predecessor() -> UnsafePointer<T>     func distanceTo(_ x: UnsafePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafePointer<T> } extension UnsafePointer : DebugPrintable {     var debugDescription: String { get } } extension UnsafePointer : Reflectable {     func getMirror() -> MirrorType } extension UnsafePointer : CVarArgType {     func encode() -> [Word] } ``` | CVarArgType, DebugPrintable, Hashable, NilLiteralConvertible, RandomAccessIndexType, Reflectable | -- |
| To | ``` struct UnsafePointer<Memory> : Equatable, Hashable, NilLiteralConvertible, _PointerType, BidirectionalIndexType, ForwardIndexType, _Incrementable, RandomAccessIndexType, Strideable, Comparable, _Strideable, _RandomAccessAmbiguity {     typealias T = Memory     typealias Distance = Int     init()     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Int)     init(bitPattern bitPattern: UInt)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     var memory: Memory { get }     subscript (_ i: Int) -> Memory { get }     var hashValue: Int { get }     func successor() -> UnsafePointer<Memory>     func predecessor() -> UnsafePointer<Memory>     func distanceTo(_ x: UnsafePointer<Memory>) -> Int     func advancedBy(_ n: Int) -> UnsafePointer<Memory> } extension UnsafePointer : CustomDebugStringConvertible {     var debugDescription: String { get } } extension UnsafePointer : _Reflectable { } extension UnsafePointer : CVarArgType { } ``` | BidirectionalIndexType, CVarArgType, Comparable, CustomDebugStringConvertible, Equatable, ForwardIndexType, Hashable, NilLiteralConvertible, RandomAccessIndexType, Strideable | Memory |

Modified UnsafePointer.advancedBy(_: Int) -> UnsafePointer<Memory>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func advancedBy(_ n: Int) -> UnsafePointer<T> ``` | iOS 8.0 |
| To | ``` func advancedBy(_ n: Int) -> UnsafePointer<Memory> ``` | iOS 9.0 |

Modified UnsafePointer.distanceTo(_: UnsafePointer<Memory>) -> Int

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func distanceTo(_ x: UnsafePointer<T>) -> Int ``` | iOS 8.0 |
| To | ``` func distanceTo(_ x: UnsafePointer<Memory>) -> Int ``` | iOS 9.0 |

Modified UnsafePointer.init()

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnsafePointer.init<U>(_: UnsafeMutablePointer<U>)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | U |

Modified UnsafePointer.init<U>(_: UnsafePointer<U>)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | U |

Modified UnsafePointer.init(_: COpaquePointer)

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified UnsafePointer.init(bitPattern: UInt)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(bitPattern bitPattern: UWord) ``` | iOS 8.0 |
| To | ``` init(bitPattern bitPattern: UInt) ``` | iOS 9.0 |

Modified UnsafePointer.init(bitPattern: Int)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` init(bitPattern bitPattern: Word) ``` | iOS 8.0 |
| To | ``` init(bitPattern bitPattern: Int) ``` | iOS 9.0 |

Modified UnsafePointer.init(nilLiteral: ())

|  | Introduction |
| --- | --- |
| From | iOS 8.1 |
| To | iOS 9.0 |

Modified UnsafePointer.memory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` var memory: T { get } ``` | iOS 8.0 |
| To | ``` var memory: Memory { get } ``` | iOS 9.0 |

Modified UnsafePointer.predecessor() -> UnsafePointer<Memory>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func predecessor() -> UnsafePointer<T> ``` | iOS 8.0 |
| To | ``` func predecessor() -> UnsafePointer<Memory> ``` | iOS 9.0 |

Modified UnsafePointer.subscript(_: Int) -> Memory

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` subscript (i: Int) -> T { get } ``` | iOS 8.0 |
| To | ``` subscript (_ i: Int) -> Memory { get } ``` | iOS 9.0 |

Modified UnsafePointer.successor() -> UnsafePointer<Memory>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func successor() -> UnsafePointer<T> ``` | iOS 8.0 |
| To | ``` func successor() -> UnsafePointer<Memory> ``` | iOS 9.0 |

Modified UnsignedIntegerType

|  | Declaration |
| --- | --- |
| From | ``` protocol UnsignedIntegerType : _UnsignedIntegerType, IntegerType { } ``` |
| To | ``` protocol UnsignedIntegerType : _DisallowMixedSignArithmetic, IntegerType {     @warn_unused_result     func toUIntMax() -> UIntMax     init(_ _: UIntMax) } ``` |

Modified UnsignedIntegerType.init(_: UIntMax)

|  | Introduction |
| --- | --- |
| From | iOS 8.3 |
| To | iOS 9.0 |

Modified UnsignedIntegerType.toUIntMax() -> UIntMax

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func toUIntMax() -> UIntMax ``` | iOS 8.3 |
| To | ``` @warn_unused_result     func toUIntMax() -> UIntMax ``` | iOS 9.0 |

Modified UTF16 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF16 : UnicodeCodecType {     typealias CodeUnit = UInt16     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } extension UTF16 {     static func width(_ x: UnicodeScalar) -> Int     static func leadSurrogate(_ x: UnicodeScalar) -> CodeUnit     static func trailSurrogate(_ x: UnicodeScalar) -> CodeUnit     static func isLeadSurrogate(_ x: CodeUnit) -> Bool     static func isTrailSurrogate(_ x: CodeUnit) -> Bool     static func measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Encoding.CodeUnit>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? } ``` |
| To | ``` struct UTF16 : UnicodeCodecType {     typealias CodeUnit = UInt16     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> ()) } extension UTF16 {     @warn_unused_result     static func width(_ x: UnicodeScalar) -> Int     @warn_unused_result     static func leadSurrogate(_ x: UnicodeScalar) -> CodeUnit     @warn_unused_result     static func trailSurrogate(_ x: UnicodeScalar) -> CodeUnit     @warn_unused_result     static func isLeadSurrogate(_ x: CodeUnit) -> Bool     @warn_unused_result     static func isTrailSurrogate(_ x: CodeUnit) -> Bool     @warn_unused_result     static func measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Input.Element>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? } ``` |

Modified UTF16.decode<G : GeneratorType where G.Element == CodeUnit>(_: G) -> UnicodeDecodingResult

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` | iOS 9.0 | ``` G : GeneratorType, G.Element == CodeUnit ``` | G |

Modified UTF16.isLeadSurrogate(_: CodeUnit) -> Bool [static]

|  | Declaration |
| --- | --- |
| From | ``` static func isLeadSurrogate(_ x: CodeUnit) -> Bool ``` |
| To | ``` @warn_unused_result     static func isLeadSurrogate(_ x: CodeUnit) -> Bool ``` |

Modified UTF16.isTrailSurrogate(_: CodeUnit) -> Bool [static]

|  | Declaration |
| --- | --- |
| From | ``` static func isTrailSurrogate(_ x: CodeUnit) -> Bool ``` |
| To | ``` @warn_unused_result     static func isTrailSurrogate(_ x: CodeUnit) -> Bool ``` |

Modified UTF16.leadSurrogate(_: UnicodeScalar) -> CodeUnit [static]

|  | Declaration |
| --- | --- |
| From | ``` static func leadSurrogate(_ x: UnicodeScalar) -> CodeUnit ``` |
| To | ``` @warn_unused_result     static func leadSurrogate(_ x: UnicodeScalar) -> CodeUnit ``` |

Modified UTF16.measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Input.Element>(_: Encoding.Type, input: Input, repairIllFormedSequences: Bool) -> (Int, Bool)? [static]

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` static func measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Encoding.CodeUnit>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result     static func measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Input.Element>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? ``` | iOS 9.0 | ``` Encoding : UnicodeCodecType, Input : GeneratorType, Encoding.CodeUnit == Input.Element ``` | Encoding, Input |

Modified UTF16.trailSurrogate(_: UnicodeScalar) -> CodeUnit [static]

|  | Declaration |
| --- | --- |
| From | ``` static func trailSurrogate(_ x: UnicodeScalar) -> CodeUnit ``` |
| To | ``` @warn_unused_result     static func trailSurrogate(_ x: UnicodeScalar) -> CodeUnit ``` |

Modified UTF16.width(_: UnicodeScalar) -> Int [static]

|  | Declaration |
| --- | --- |
| From | ``` static func width(_ x: UnicodeScalar) -> Int ``` |
| To | ``` @warn_unused_result     static func width(_ x: UnicodeScalar) -> Int ``` |

Modified UTF32 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF32 : UnicodeCodecType {     typealias CodeUnit = UInt32     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` |
| To | ``` struct UTF32 : UnicodeCodecType {     typealias CodeUnit = UInt32     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> ()) } ``` |

Modified UTF32.decode<G : GeneratorType where G.Element == CodeUnit>(_: G) -> UnicodeDecodingResult

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` | iOS 9.0 | ``` G : GeneratorType, G.Element == CodeUnit ``` | G |

Modified UTF8 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct UTF8 : UnicodeCodecType {     typealias CodeUnit = UInt8     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S)     static func isContinuation(_ byte: CodeUnit) -> Bool } ``` |
| To | ``` struct UTF8 : UnicodeCodecType {     typealias CodeUnit = UInt8     init()     mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode(_ input: UnicodeScalar, output put: (CodeUnit) -> ())     @warn_unused_result     static func isContinuation(_ byte: CodeUnit) -> Bool } ``` |

Modified UTF8.decode<G : GeneratorType where G.Element == CodeUnit>(_: G) -> UnicodeDecodingResult

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` mutating func decode<G : GeneratorType where G.Element == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` | iOS 9.0 | ``` G : GeneratorType, G.Element == CodeUnit ``` | G |

Modified UTF8.isContinuation(_: CodeUnit) -> Bool [static]

|  | Declaration |
| --- | --- |
| From | ``` static func isContinuation(_ byte: CodeUnit) -> Bool ``` |
| To | ``` @warn_unused_result     static func isContinuation(_ byte: CodeUnit) -> Bool ``` |

Modified VaListBuilder

|  | Declaration |
| --- | --- |
| From | ``` final class VaListBuilder {     func append(_ arg: CVarArgType)     func va_list() -> CVaListPointer     var storage: [(Word)] } ``` |
| To | ``` final class VaListBuilder { } ``` |

Modified !(_: Bool) -> Bool

|  | Declaration | Operator Fixity |
| --- | --- | --- |
| From | ``` prefix func !(_ a: Bool) -> Bool ``` | -- |
| To | ``` @warn_unused_result prefix func !(_ a: Bool) -> Bool ``` | prefix |

Modified !(_: T) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] | Operator Fixity |
| --- | --- | --- | --- | --- | --- |
| From | ``` prefix func !<T : BooleanType>(_ a: T) -> Bool ``` | iOS 8.3 | ```  ``` | -- | -- |
| To | ``` @warn_unused_result prefix func !<T : BooleanType>(_ a: T) -> Bool ``` | iOS 9.0 | ``` T : BooleanType ``` | T | prefix |

Modified !=(_: Float, _: Float) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func !=(_ lhs: Float, _ rhs: Float) -> Bool ``` |
| To | ``` @warn_unused_result func !=(_ lhs: Float, _ rhs: Float) -> Bool ``` |

Modified !=(_: T?, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func !=<T : Equatable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func !=<T : Equatable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 9.0 | ``` T : Equatable ``` | T |

Modified !=(_: [Element], _: [Element]) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func !=<T : Equatable>(_ lhs: [T], _ rhs: [T]) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func !=<Element : Equatable>(_ lhs: [Element], _ rhs: [Element]) -> Bool ``` | iOS 9.0 | ``` Element : Equatable ``` | Element |

Modified !=(_: ArraySlice<Element>, _: ArraySlice<Element>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func !=<T : Equatable>(_ lhs: ArraySlice<T>, _ rhs: ArraySlice<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func !=<Element : Equatable>(_ lhs: ArraySlice<Element>, _ rhs: ArraySlice<Element>) -> Bool ``` | iOS 9.0 | ``` Element : Equatable ``` | Element |

Modified !=(_: T?, _: _OptionalNilComparisonType) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func !=<T>(_ lhs: T?, _ rhs: _OptionalNilComparisonType) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func !=<T>(_ lhs: T?, _ rhs: _OptionalNilComparisonType) -> Bool ``` | iOS 9.0 | T |

Modified !=(_: ContiguousArray<Element>, _: ContiguousArray<Element>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func !=<T : Equatable>(_ lhs: ContiguousArray<T>, _ rhs: ContiguousArray<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func !=<Element : Equatable>(_ lhs: ContiguousArray<Element>, _ rhs: ContiguousArray<Element>) -> Bool ``` | iOS 9.0 | ``` Element : Equatable ``` | Element |

Modified !=(_: _OptionalNilComparisonType, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func !=<T>(_ lhs: _OptionalNilComparisonType, _ rhs: T?) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func !=<T>(_ lhs: _OptionalNilComparisonType, _ rhs: T?) -> Bool ``` | iOS 9.0 | T |

Modified !=(_: [Key : Value], _: [Key : Value]) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func !=<Key : Equatable, Value : Equatable>(_ lhs: [Key : Value], _ rhs: [Key : Value]) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func !=<Key : Equatable, Value : Equatable>(_ lhs: [Key : Value], _ rhs: [Key : Value]) -> Bool ``` | iOS 9.0 | ``` Key : Equatable, Value : Equatable ``` | Key, Value |

Modified !=(_: Double, _: Double) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func !=(_ lhs: Double, _ rhs: Double) -> Bool ``` |
| To | ``` @warn_unused_result func !=(_ lhs: Double, _ rhs: Double) -> Bool ``` |

Modified !=(_: T, _: T) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func !=<T : Equatable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func !=<T : RawRepresentable where T.RawValue : Equatable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 9.0 | ``` T : RawRepresentable, T.RawValue : Equatable ``` | T |

Modified !==(_: AnyObject?, _: AnyObject?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func !==(_ lhs: AnyObject?, _ rhs: AnyObject?) -> Bool ``` |
| To | ``` @warn_unused_result func !==(_ lhs: AnyObject?, _ rhs: AnyObject?) -> Bool ``` |

Modified %(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func %<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func %<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified %(_: Double, _: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func %(_ lhs: Double, _ rhs: Double) -> Double ``` |
| To | ``` @warn_unused_result func %(_ lhs: Double, _ rhs: Double) -> Double ``` |

Modified %(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func %(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` @warn_unused_result func %(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified %=(_: T, _: T)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified &\*(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func &*<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func &*<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified &+(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func &+<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func &+<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified &-(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func &-<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func &-<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified &=(_: T, _: T)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func &=<T : BitwiseOperationsType>(inout _ lhs: T, _ rhs: T) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func &=<T : BitwiseOperationsType>(inout _ lhs: T, _ rhs: T) ``` | iOS 9.0 | ``` T : BitwiseOperationsType ``` | T |

Modified \*(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func *(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` @warn_unused_result func *(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified \*(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func *<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func *<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified \*(_: Double, _: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func *(_ lhs: Double, _ rhs: Double) -> Double ``` |
| To | ``` @warn_unused_result func *(_ lhs: Double, _ rhs: Double) -> Double ``` |

Modified \*=(_: T, _: T)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified +(_: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] | Operator Fixity |
| --- | --- | --- | --- | --- | --- |
| From | ``` prefix func +<T : _SignedNumberType>(_ x: T) -> T ``` | iOS 8.3 | ```  ``` | -- | -- |
| To | ``` prefix func +<T : SignedNumberType>(_ x: T) -> T ``` | iOS 9.0 | ``` T : SignedNumberType ``` | T | prefix |

Modified +(_: Double) -> Double

|  | Declaration | Operator Fixity |
| --- | --- | --- |
| From | ``` prefix func +(_ x: Double) -> Double ``` | -- |
| To | ``` @warn_unused_result prefix func +(_ x: Double) -> Double ``` | prefix |

Modified +(_: Float) -> Float

|  | Declaration | Operator Fixity |
| --- | --- | --- |
| From | ``` prefix func +(_ x: Float) -> Float ``` | -- |
| To | ``` @warn_unused_result prefix func +(_ x: Float) -> Float ``` | prefix |

Modified +(_: String, _: String) -> String

|  | Declaration |
| --- | --- |
| From | ``` func +(_ lhs: String, _ rhs: String) -> String ``` |
| To | ``` @warn_unused_result func +(_ lhs: String, _ rhs: String) -> String ``` |

Modified +(_: T, _: T._DisallowMixedSignArithmetic) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func +<T : _UnsignedIntegerType>(_ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func +<T : UnsignedIntegerType>(_ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) -> T ``` | iOS 9.0 | ``` T : UnsignedIntegerType ``` | T |

Modified +(_: UnsafeMutablePointer<Memory>, _: Int) -> UnsafeMutablePointer<Memory>

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func +<T>(_ lhs: UnsafeMutablePointer<T>, _ rhs: Int) -> UnsafeMutablePointer<T> ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func +<Memory>(_ lhs: UnsafeMutablePointer<Memory>, _ rhs: Int) -> UnsafeMutablePointer<Memory> ``` | iOS 9.0 | Memory |

Modified +(_: Int, _: UnsafePointer<Memory>) -> UnsafePointer<Memory>

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func +<T>(_ lhs: Int, _ rhs: UnsafePointer<T>) -> UnsafePointer<T> ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func +<Memory>(_ lhs: Int, _ rhs: UnsafePointer<Memory>) -> UnsafePointer<Memory> ``` | iOS 9.0 | Memory |

Modified +(_: Double, _: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func +(_ lhs: Double, _ rhs: Double) -> Double ``` |
| To | ``` @warn_unused_result func +(_ lhs: Double, _ rhs: Double) -> Double ``` |

Modified +(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func +<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func +<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified +(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func +(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` @warn_unused_result func +(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified +(_: Int, _: UnsafeMutablePointer<Memory>) -> UnsafeMutablePointer<Memory>

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func +<T>(_ lhs: Int, _ rhs: UnsafeMutablePointer<T>) -> UnsafeMutablePointer<T> ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func +<Memory>(_ lhs: Int, _ rhs: UnsafeMutablePointer<Memory>) -> UnsafeMutablePointer<Memory> ``` | iOS 9.0 | Memory |

Modified +(_: T._DisallowMixedSignArithmetic, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func +<T : _UnsignedIntegerType>(_ lhs: T._DisallowMixedSignArithmetic, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func +<T : UnsignedIntegerType>(_ lhs: T._DisallowMixedSignArithmetic, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : UnsignedIntegerType ``` | T |

Modified +(_: UnsafePointer<Memory>, _: Int) -> UnsafePointer<Memory>

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func +<T>(_ lhs: UnsafePointer<T>, _ rhs: Int) -> UnsafePointer<T> ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func +<Memory>(_ lhs: UnsafePointer<Memory>, _ rhs: Int) -> UnsafePointer<Memory> ``` | iOS 9.0 | Memory |

Modified ++(_: Int32) -> Int32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: UInt16) -> UInt16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: Double) -> Double

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: UInt32) -> UInt32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: UInt8) -> UInt8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: Float) -> Float

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: UInt64) -> UInt64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: Int16) -> Int16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: UInt8) -> UInt8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: Int8) -> Int8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: UInt) -> UInt

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: UInt64) -> UInt64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: Int64) -> Int64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: Int16) -> Int16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: Float) -> Float

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: Int) -> Int

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: Int32) -> Int32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: Int) -> Int

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: Double) -> Double

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: Int8) -> Int8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: UInt) -> UInt

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: UInt16) -> UInt16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified ++(_: Int64) -> Int64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ++(_: UInt32) -> UInt32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified +=(_: [Element], _: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func +=<T, S : SequenceType where T == T>(inout _ lhs: [T], _ rhs: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func +=<Element, S : SequenceType where S.Generator.Element == Element>(inout _ lhs: [Element], _ rhs: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | Element, S |

Modified +=(_: UnsafePointer<Memory>, _: Int)

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func +=<T>(inout _ lhs: UnsafePointer<T>, _ rhs: Int) ``` | iOS 8.3 | -- |
| To | ``` func +=<Memory>(inout _ lhs: UnsafePointer<Memory>, _ rhs: Int) ``` | iOS 9.0 | Memory |

Modified +=(_: T, _: T)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified +=(_: UnsafeMutablePointer<Memory>, _: Int)

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func +=<T>(inout _ lhs: UnsafeMutablePointer<T>, _ rhs: Int) ``` | iOS 8.3 | -- |
| To | ``` func +=<Memory>(inout _ lhs: UnsafeMutablePointer<Memory>, _ rhs: Int) ``` | iOS 9.0 | Memory |

Modified +=(_: ArraySlice<Element>, _: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func +=<T, S : SequenceType where T == T>(inout _ lhs: ArraySlice<T>, _ rhs: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func +=<Element, S : SequenceType where S.Generator.Element == Element>(inout _ lhs: ArraySlice<Element>, _ rhs: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | Element, S |

Modified +=(_: ContiguousArray<Element>, _: S)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func +=<T, S : SequenceType where T == T>(inout _ lhs: ContiguousArray<T>, _ rhs: S) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func +=<Element, S : SequenceType where S.Generator.Element == Element>(inout _ lhs: ContiguousArray<Element>, _ rhs: S) ``` | iOS 9.0 | ``` S : SequenceType, S.Generator.Element == Element ``` | Element, S |

Modified +=(_: T, _: T._DisallowMixedSignArithmetic)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func +=<T : _UnsignedIntegerType>(inout _ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func +=<T : UnsignedIntegerType>(inout _ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) ``` | iOS 9.0 | ``` T : UnsignedIntegerType ``` | T |

Modified -(_: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] | Operator Fixity |
| --- | --- | --- | --- | --- | --- |
| From | ``` prefix func -<T : _SignedNumberType>(_ x: T) -> T ``` | iOS 8.3 | ```  ``` | -- | -- |
| To | ``` prefix func -<T : SignedNumberType>(_ x: T) -> T ``` | iOS 9.0 | ``` T : SignedNumberType ``` | T | prefix |

Modified -(_: Double) -> Double

|  | Declaration | Operator Fixity |
| --- | --- | --- |
| From | ``` prefix func -(_ x: Double) -> Double ``` | -- |
| To | ``` @warn_unused_result prefix func -(_ x: Double) -> Double ``` | prefix |

Modified -(_: Float) -> Float

|  | Declaration | Operator Fixity |
| --- | --- | --- |
| From | ``` prefix func -(_ x: Float) -> Float ``` | -- |
| To | ``` @warn_unused_result prefix func -(_ x: Float) -> Float ``` | prefix |

Modified -(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func -<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func -<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified -(_: T, _: T._DisallowMixedSignArithmetic) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func -<T : _UnsignedIntegerType>(_ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func -<T : _DisallowMixedSignArithmetic>(_ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) -> T ``` | iOS 9.0 | ``` T : _DisallowMixedSignArithmetic ``` | T |

Modified -(_: UnsafePointer<Memory>, _: UnsafePointer<Memory>) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func -<T>(_ lhs: UnsafePointer<T>, _ rhs: UnsafePointer<T>) -> Int ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func -<Memory>(_ lhs: UnsafePointer<Memory>, _ rhs: UnsafePointer<Memory>) -> Int ``` | iOS 9.0 | Memory |

Modified -(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func -(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` @warn_unused_result func -(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified -(_: UnsafeMutablePointer<Memory>, _: Int) -> UnsafeMutablePointer<Memory>

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func -<T>(_ lhs: UnsafeMutablePointer<T>, _ rhs: Int) -> UnsafeMutablePointer<T> ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func -<Memory>(_ lhs: UnsafeMutablePointer<Memory>, _ rhs: Int) -> UnsafeMutablePointer<Memory> ``` | iOS 9.0 | Memory |

Modified -(_: UnsafeMutablePointer<Memory>, _: UnsafeMutablePointer<Memory>) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func -<T>(_ lhs: UnsafeMutablePointer<T>, _ rhs: UnsafeMutablePointer<T>) -> Int ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func -<Memory>(_ lhs: UnsafeMutablePointer<Memory>, _ rhs: UnsafeMutablePointer<Memory>) -> Int ``` | iOS 9.0 | Memory |

Modified -(_: UnsafePointer<Memory>, _: Int) -> UnsafePointer<Memory>

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func -<T>(_ lhs: UnsafePointer<T>, _ rhs: Int) -> UnsafePointer<T> ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func -<Memory>(_ lhs: UnsafePointer<Memory>, _ rhs: Int) -> UnsafePointer<Memory> ``` | iOS 9.0 | Memory |

Modified -(_: Double, _: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func -(_ lhs: Double, _ rhs: Double) -> Double ``` |
| To | ``` @warn_unused_result func -(_ lhs: Double, _ rhs: Double) -> Double ``` |

Modified -(_: T, _: T) -> T._DisallowMixedSignArithmetic

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func -<T : _UnsignedIntegerType>(_ lhs: T, _ rhs: T) -> T._DisallowMixedSignArithmetic ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func -<T : _DisallowMixedSignArithmetic>(_ lhs: T, _ rhs: T) -> T._DisallowMixedSignArithmetic ``` | iOS 9.0 | ``` T : _DisallowMixedSignArithmetic ``` | T |

Modified --(_: Int16) -> Int16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: UInt32) -> UInt32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: Int) -> Int

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: Int32) -> Int32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: Float) -> Float

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: Double) -> Double

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: UInt64) -> UInt64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: Int16) -> Int16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: UInt8) -> UInt8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: Int32) -> Int32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: UInt64) -> UInt64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: Double) -> Double

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: UInt16) -> UInt16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: Int8) -> Int8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: Int) -> Int

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: UInt32) -> UInt32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: Float) -> Float

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: UInt) -> UInt

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: Int64) -> Int64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: UInt16) -> UInt16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified --(_: UInt8) -> UInt8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: UInt) -> UInt

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: Int8) -> Int8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified --(_: Int64) -> Int64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | postfix |

Modified -=(_: UnsafeMutablePointer<Memory>, _: Int)

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func -=<T>(inout _ lhs: UnsafeMutablePointer<T>, _ rhs: Int) ``` | iOS 8.3 | -- |
| To | ``` func -=<Memory>(inout _ lhs: UnsafeMutablePointer<Memory>, _ rhs: Int) ``` | iOS 9.0 | Memory |

Modified -=(_: T, _: T)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified -=(_: UnsafePointer<Memory>, _: Int)

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func -=<T>(inout _ lhs: UnsafePointer<T>, _ rhs: Int) ``` | iOS 8.3 | -- |
| To | ``` func -=<Memory>(inout _ lhs: UnsafePointer<Memory>, _ rhs: Int) ``` | iOS 9.0 | Memory |

Modified -=(_: T, _: T._DisallowMixedSignArithmetic)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func -=<T : _UnsignedIntegerType>(inout _ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` func -=<T : UnsignedIntegerType>(inout _ lhs: T, _ rhs: T._DisallowMixedSignArithmetic) ``` | iOS 9.0 | ``` T : UnsignedIntegerType ``` | T |

Modified ...(_: Bound, _: Bound) -> ClosedInterval<Bound>

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ...<T : Comparable>(_ start: T, _ end: T) -> ClosedInterval<T> ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ...<Bound : Comparable>(_ start: Bound, _ end: Bound) -> ClosedInterval<Bound> ``` | iOS 9.0 | ``` Bound : Comparable ``` | Bound |

Modified ..<(_: Bound, _: Bound) -> HalfOpenInterval<Bound>

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ..<<T : Comparable>(_ start: T, _ end: T) -> HalfOpenInterval<T> ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ..<<Bound : Comparable>(_ start: Bound, _ end: Bound) -> HalfOpenInterval<Bound> ``` | iOS 9.0 | ``` Bound : Comparable ``` | Bound |

Modified /(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func /<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func /<T : _IntegerArithmeticType>(_ lhs: T, _ rhs: T) -> T ``` | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified /(_: Float, _: Float) -> Float

|  | Declaration |
| --- | --- |
| From | ``` func /(_ lhs: Float, _ rhs: Float) -> Float ``` |
| To | ``` @warn_unused_result func /(_ lhs: Float, _ rhs: Float) -> Float ``` |

Modified /(_: Double, _: Double) -> Double

|  | Declaration |
| --- | --- |
| From | ``` func /(_ lhs: Double, _ rhs: Double) -> Double ``` |
| To | ``` @warn_unused_result func /(_ lhs: Double, _ rhs: Double) -> Double ``` |

Modified /=(_: T, _: T)

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _IntegerArithmeticType ``` | T |

Modified <(_: T, _: T) -> Bool

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : _Strideable ``` | T |

Modified <(_: UnsafeMutablePointer<Memory>, _: UnsafeMutablePointer<Memory>) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func <<T>(_ lhs: UnsafeMutablePointer<T>, _ rhs: UnsafeMutablePointer<T>) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func <<Memory>(_ lhs: UnsafeMutablePointer<Memory>, _ rhs: UnsafeMutablePointer<Memory>) -> Bool ``` | iOS 9.0 | Memory |

Modified <(_: ObjectIdentifier, _: ObjectIdentifier) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: ObjectIdentifier, _ rhs: ObjectIdentifier) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: ObjectIdentifier, _ rhs: ObjectIdentifier) -> Bool ``` |

Modified <(_: UnicodeScalar, _: UnicodeScalar) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: UnicodeScalar, _ rhs: UnicodeScalar) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: UnicodeScalar, _ rhs: UnicodeScalar) -> Bool ``` |

Modified <(_: String.UTF16View.Index, _: String.UTF16View.Index) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: String.UTF16View.Index, _ rhs: String.UTF16View.Index) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: String.UTF16View.Index, _ rhs: String.UTF16View.Index) -> Bool ``` |

Modified <(_: String, _: String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: String, _ rhs: String) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: String, _ rhs: String) -> Bool ``` |

Modified <(_: DictionaryIndex<Key, Value>, _: DictionaryIndex<Key, Value>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func <<Key : Hashable, Value>(_ lhs: DictionaryIndex<Key, Value>, _ rhs: DictionaryIndex<Key, Value>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func <<Key : Hashable, Value>(_ lhs: DictionaryIndex<Key, Value>, _ rhs: DictionaryIndex<Key, Value>) -> Bool ``` | iOS 9.0 | ``` Key : Hashable ``` | Key, Value |

Modified <(_: UnsafePointer<Memory>, _: UnsafePointer<Memory>) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func <<T>(_ lhs: UnsafePointer<T>, _ rhs: UnsafePointer<T>) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func <<Memory>(_ lhs: UnsafePointer<Memory>, _ rhs: UnsafePointer<Memory>) -> Bool ``` | iOS 9.0 | Memory |

Modified <(_: Bit, _: Bit) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: Bit, _ rhs: Bit) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: Bit, _ rhs: Bit) -> Bool ``` |

Modified <(_: T?, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func <<T : _Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func <<T : Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified <(_: SetIndex<Element>, _: SetIndex<Element>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func <<T : Hashable>(_ lhs: SetIndex<T>, _ rhs: SetIndex<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func <<Element : Hashable>(_ lhs: SetIndex<Element>, _ rhs: SetIndex<Element>) -> Bool ``` | iOS 9.0 | ``` Element : Hashable ``` | Element |

Modified <(_: Character, _: Character) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: Character, _ rhs: Character) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: Character, _ rhs: Character) -> Bool ``` |

Modified <(_: Float, _: Float) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: Float, _ rhs: Float) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: Float, _ rhs: Float) -> Bool ``` |

Modified <(_: String.UnicodeScalarView.Index, _: String.UnicodeScalarView.Index) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: String.UnicodeScalarView.Index, _ rhs: String.UnicodeScalarView.Index) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: String.UnicodeScalarView.Index, _ rhs: String.UnicodeScalarView.Index) -> Bool ``` |

Modified <(_: Double, _: Double) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <(_ lhs: Double, _ rhs: Double) -> Bool ``` |
| To | ``` @warn_unused_result func <(_ lhs: Double, _ rhs: Double) -> Bool ``` |

Modified <=(_: T, _: T) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func <=<T : _Comparable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func <=<T : Comparable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified <=(_: T?, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func <=<T : _Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func <=<T : Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified <=(_: Float, _: Float) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <=(_ lhs: Float, _ rhs: Float) -> Bool ``` |
| To | ``` @warn_unused_result func <=(_ lhs: Float, _ rhs: Float) -> Bool ``` |

Modified <=(_: Double, _: Double) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func <=(_ lhs: Double, _ rhs: Double) -> Bool ``` |
| To | ``` @warn_unused_result func <=(_ lhs: Double, _ rhs: Double) -> Bool ``` |

Modified ==(_: String, _: String) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: String, _ rhs: String) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: String, _ rhs: String) -> Bool ``` |

Modified ==(_: [Element], _: [Element]) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Equatable>(_ lhs: [T], _ rhs: [T]) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Element : Equatable>(_ lhs: [Element], _ rhs: [Element]) -> Bool ``` | iOS 9.0 | ``` Element : Equatable ``` | Element |

Modified ==(_: Float, _: Float) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: Float, _ rhs: Float) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: Float, _ rhs: Float) -> Bool ``` |

Modified ==(_: Range<Element>, _: Range<Element>) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func ==<T>(_ lhs: Range<T>, _ rhs: Range<T>) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func ==<Element>(_ lhs: Range<Element>, _ rhs: Range<Element>) -> Bool ``` | iOS 9.0 | Element |

Modified ==(_: ClosedInterval<Bound>, _: ClosedInterval<Bound>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Comparable>(_ lhs: ClosedInterval<T>, _ rhs: ClosedInterval<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Bound : Comparable>(_ lhs: ClosedInterval<Bound>, _ rhs: ClosedInterval<Bound>) -> Bool ``` | iOS 9.0 | ``` Bound : Comparable ``` | Bound |

Modified ==(_: T?, _: _OptionalNilComparisonType) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func ==<T>(_ lhs: T?, _ rhs: _OptionalNilComparisonType) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func ==<T>(_ lhs: T?, _ rhs: _OptionalNilComparisonType) -> Bool ``` | iOS 9.0 | T |

Modified ==(_: String.UnicodeScalarView.Index, _: String.UnicodeScalarView.Index) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: String.UnicodeScalarView.Index, _ rhs: String.UnicodeScalarView.Index) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: String.UnicodeScalarView.Index, _ rhs: String.UnicodeScalarView.Index) -> Bool ``` |

Modified ==(_: SetIndex<Element>, _: SetIndex<Element>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Hashable>(_ lhs: SetIndex<T>, _ rhs: SetIndex<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Element : Hashable>(_ lhs: SetIndex<Element>, _ rhs: SetIndex<Element>) -> Bool ``` | iOS 9.0 | ``` Element : Hashable ``` | Element |

Modified ==(_: ContiguousArray<Element>, _: ContiguousArray<Element>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Equatable>(_ lhs: ContiguousArray<T>, _ rhs: ContiguousArray<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Element : Equatable>(_ lhs: ContiguousArray<Element>, _ rhs: ContiguousArray<Element>) -> Bool ``` | iOS 9.0 | ``` Element : Equatable ``` | Element |

Modified ==(_: HalfOpenInterval<Bound>, _: HalfOpenInterval<Bound>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Comparable>(_ lhs: HalfOpenInterval<T>, _ rhs: HalfOpenInterval<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Bound : Comparable>(_ lhs: HalfOpenInterval<Bound>, _ rhs: HalfOpenInterval<Bound>) -> Bool ``` | iOS 9.0 | ``` Bound : Comparable ``` | Bound |

Modified ==(_: Bool, _: Bool) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: Bool, _ rhs: Bool) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: Bool, _ rhs: Bool) -> Bool ``` |

Modified ==(_: String.UTF8View.Index, _: String.UTF8View.Index) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: String.UTF8View.Index, _ rhs: String.UTF8View.Index) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: String.UTF8View.Index, _ rhs: String.UTF8View.Index) -> Bool ``` |

Modified ==(_: T?, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Equatable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<T : Equatable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 9.0 | ``` T : Equatable ``` | T |

Modified ==(_: Character, _: Character) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: Character, _ rhs: Character) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: Character, _ rhs: Character) -> Bool ``` |

Modified ==(_: ArraySlice<Element>, _: ArraySlice<Element>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Equatable>(_ lhs: ArraySlice<T>, _ rhs: ArraySlice<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Element : Equatable>(_ lhs: ArraySlice<Element>, _ rhs: ArraySlice<Element>) -> Bool ``` | iOS 9.0 | ``` Element : Equatable ``` | Element |

Modified ==(_: DictionaryIndex<Key, Value>, _: DictionaryIndex<Key, Value>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<Key : Hashable, Value>(_ lhs: DictionaryIndex<Key, Value>, _ rhs: DictionaryIndex<Key, Value>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Key : Hashable, Value>(_ lhs: DictionaryIndex<Key, Value>, _ rhs: DictionaryIndex<Key, Value>) -> Bool ``` | iOS 9.0 | ``` Key : Hashable ``` | Key, Value |

Modified ==(_: UnsafePointer<Memory>, _: UnsafePointer<Memory>) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func ==<T>(_ lhs: UnsafePointer<T>, _ rhs: UnsafePointer<T>) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func ==<Memory>(_ lhs: UnsafePointer<Memory>, _ rhs: UnsafePointer<Memory>) -> Bool ``` | iOS 9.0 | Memory |

Modified ==(_: String.UTF16View.Index, _: String.UTF16View.Index) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: String.UTF16View.Index, _ rhs: String.UTF16View.Index) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: String.UTF16View.Index, _ rhs: String.UTF16View.Index) -> Bool ``` |

Modified ==(_: Double, _: Double) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: Double, _ rhs: Double) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: Double, _ rhs: Double) -> Bool ``` |

Modified ==(_: ObjectIdentifier, _: ObjectIdentifier) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ x: ObjectIdentifier, _ y: ObjectIdentifier) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ x: ObjectIdentifier, _ y: ObjectIdentifier) -> Bool ``` |

Modified ==(_: ManagedBufferPointer<Value, Element>, _: ManagedBufferPointer<Value, Element>) -> Bool

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.3 | -- |
| To | iOS 9.0 | Value, Element |

Modified ==(_: UnicodeScalar, _: UnicodeScalar) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: UnicodeScalar, _ rhs: UnicodeScalar) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: UnicodeScalar, _ rhs: UnicodeScalar) -> Bool ``` |

Modified ==(_: Set<Element>, _: Set<Element>) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<T : Hashable>(_ lhs: Set<T>, _ rhs: Set<T>) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Element : Hashable>(_ lhs: Set<Element>, _ rhs: Set<Element>) -> Bool ``` | iOS 9.0 | ``` Element : Hashable ``` | Element |

Modified ==(_: COpaquePointer, _: COpaquePointer) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: COpaquePointer, _ rhs: COpaquePointer) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: COpaquePointer, _ rhs: COpaquePointer) -> Bool ``` |

Modified ==(_: Bit, _: Bit) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ==(_ lhs: Bit, _ rhs: Bit) -> Bool ``` |
| To | ``` @warn_unused_result func ==(_ lhs: Bit, _ rhs: Bit) -> Bool ``` |

Modified ==(_: [Key : Value], _: [Key : Value]) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ==<Key : Equatable, Value : Equatable>(_ lhs: [Key : Value], _ rhs: [Key : Value]) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ==<Key : Equatable, Value : Equatable>(_ lhs: [Key : Value], _ rhs: [Key : Value]) -> Bool ``` | iOS 9.0 | ``` Key : Equatable, Value : Equatable ``` | Key, Value |

Modified ==(_: AutoreleasingUnsafeMutablePointer<Memory>, _: AutoreleasingUnsafeMutablePointer<Memory>) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func ==<T>(_ lhs: AutoreleasingUnsafeMutablePointer<T>, _ rhs: AutoreleasingUnsafeMutablePointer<T>) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func ==<Memory>(_ lhs: AutoreleasingUnsafeMutablePointer<Memory>, _ rhs: AutoreleasingUnsafeMutablePointer<Memory>) -> Bool ``` | iOS 9.0 | Memory |

Modified ==(_: UnsafeMutablePointer<Memory>, _: UnsafeMutablePointer<Memory>) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func ==<T>(_ lhs: UnsafeMutablePointer<T>, _ rhs: UnsafeMutablePointer<T>) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func ==<Memory>(_ lhs: UnsafeMutablePointer<Memory>, _ rhs: UnsafeMutablePointer<Memory>) -> Bool ``` | iOS 9.0 | Memory |

Modified ==(_: _OptionalNilComparisonType, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func ==<T>(_ lhs: _OptionalNilComparisonType, _ rhs: T?) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func ==<T>(_ lhs: _OptionalNilComparisonType, _ rhs: T?) -> Bool ``` | iOS 9.0 | T |

Modified ===(_: AnyObject?, _: AnyObject?) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func ===(_ lhs: AnyObject?, _ rhs: AnyObject?) -> Bool ``` |
| To | ``` @warn_unused_result func ===(_ lhs: AnyObject?, _ rhs: AnyObject?) -> Bool ``` |

Modified >(_: Float, _: Float) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func >(_ lhs: Float, _ rhs: Float) -> Bool ``` |
| To | ``` @warn_unused_result func >(_ lhs: Float, _ rhs: Float) -> Bool ``` |

Modified >(_: T?, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ><T : _Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ><T : Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified >(_: Double, _: Double) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func >(_ lhs: Double, _ rhs: Double) -> Bool ``` |
| To | ``` @warn_unused_result func >(_ lhs: Double, _ rhs: Double) -> Bool ``` |

Modified >(_: T, _: T) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ><T : _Comparable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ><T : Comparable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified >=(_: Double, _: Double) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func >=(_ lhs: Double, _ rhs: Double) -> Bool ``` |
| To | ``` @warn_unused_result func >=(_ lhs: Double, _ rhs: Double) -> Bool ``` |

Modified >=(_: T, _: T) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func >=<T : _Comparable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func >=<T : Comparable>(_ lhs: T, _ rhs: T) -> Bool ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified >=(_: Float, _: Float) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func >=(_ lhs: Float, _ rhs: Float) -> Bool ``` |
| To | ``` @warn_unused_result func >=(_ lhs: Float, _ rhs: Float) -> Bool ``` |

Modified >=(_: T?, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func >=<T : _Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func >=<T : Comparable>(_ lhs: T?, _ rhs: T?) -> Bool ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified ^=(_: T, _: T)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ^=<T : BitwiseOperationsType>(inout _ lhs: T, _ rhs: T) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ^=<T : BitwiseOperationsType>(inout _ lhs: T, _ rhs: T) ``` | iOS 9.0 | ``` T : BitwiseOperationsType ``` | T |

Modified abs<T : SignedNumberType>(_: T) -> T

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.0 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : SignedNumberType ``` | T |

Modified alignof<T>(_: T.Type) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func alignof<T>(_ _: T.Type) -> Int ``` | iOS 8.0 | -- |
| To | ``` @warn_unused_result func alignof<T>(_ _: T.Type) -> Int ``` | iOS 9.0 | T |

Modified alignofValue<T>(_: T) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func alignofValue<T>(_ _: T) -> Int ``` | iOS 8.0 | -- |
| To | ``` @warn_unused_result func alignofValue<T>(_ _: T) -> Int ``` | iOS 9.0 | T |

Modified assert(_: () -> Bool, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func assert(_ condition: @autoclosure_ condition: @autoclosure () -> Bool, _ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` func assert(@autoclosure _ condition: () -> Bool, @autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |

Modified assertionFailure(_: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` @inline(__always) func assertionFailure(_ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` func assertionFailure(@autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |

Modified dump<T, TargetStream : OutputStreamType>(_: T, _: TargetStream, name: String?, indent: Int, maxDepth: Int, maxItems: Int) -> T

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.0 | ```  ``` | -- |
| To | iOS 9.0 | ``` TargetStream : OutputStreamType ``` | T, TargetStream |

Modified dump<T>(_: T, name: String?, indent: Int, maxDepth: Int, maxItems: Int) -> T

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | T |

Modified fatalError(_: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func fatalError(_ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` @noreturn func fatalError(@autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |

Modified ForwardIndexType.Distance

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified getVaList(_: [CVarArgType]) -> CVaListPointer

|  | Declaration |
| --- | --- |
| From | ``` func getVaList(_ args: [CVarArgType]) -> CVaListPointer ``` |
| To | ``` @warn_unused_result func getVaList(_ args: [CVarArgType]) -> CVaListPointer ``` |

Modified isUniquelyReferenced<T : NonObjectiveCBase>(_: T) -> Bool

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : NonObjectiveCBase ``` | T |

Modified isUniquelyReferencedNonObjC<T>(_: T) -> Bool

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : AnyObject ``` | T |

Modified isUniquelyReferencedNonObjC<T>(_: T?) -> Bool

|  | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- |
| From | iOS 8.3 | ```  ``` | -- |
| To | iOS 9.0 | ``` T : AnyObject ``` | T |

Modified max<T : Comparable>(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func max<T : Comparable>(_ x: T, _ y: T) -> T ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` @warn_unused_result func max<T : Comparable>(_ x: T, _ y: T) -> T ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified max<T : Comparable>(_: T, _: T, _: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func max<T : Comparable>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` @warn_unused_result func max<T : Comparable>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified min<T : Comparable>(_: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func min<T : Comparable>(_ x: T, _ y: T) -> T ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` @warn_unused_result func min<T : Comparable>(_ x: T, _ y: T) -> T ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified min<T : Comparable>(_: T, _: T, _: T, _: T) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func min<T : Comparable>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T ``` | iOS 8.0 | ```  ``` | -- |
| To | ``` @warn_unused_result func min<T : Comparable>(_ x: T, _ y: T, _ z: T, _ rest: T...) -> T ``` | iOS 9.0 | ``` T : Comparable ``` | T |

Modified numericCast<T : _SignedIntegerType, U : _SignedIntegerType>(_: T) -> U

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func numericCast<T : _SignedIntegerType, U : _SignedIntegerType>(_ x: T) -> U ``` | iOS 8.1 | ```  ``` | -- |
| To | ``` @warn_unused_result func numericCast<T : _SignedIntegerType, U : _SignedIntegerType>(_ x: T) -> U ``` | iOS 9.0 | ``` T : _SignedIntegerType, U : _SignedIntegerType ``` | T, U |

Modified precondition(_: () -> Bool, _: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` func precondition(_ condition: @autoclosure_ condition: @autoclosure () -> Bool, _ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` func precondition(@autoclosure _ condition: () -> Bool, @autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |

Modified preconditionFailure(_: () -> String, file: StaticString, line: UInt)

|  | Declaration |
| --- | --- |
| From | ``` @noreturn func preconditionFailure(_ message: @autoclosure_ message: @autoclosure () -> String = default, file file: StaticString = default, line line: UWord = default) ``` |
| To | ``` @noreturn func preconditionFailure(@autoclosure _ message: () -> String = default, file file: StaticString = default, line line: UInt = default) ``` |

Modified ReverseRandomAccessIndex.Distance

|  | Declaration |
| --- | --- |
| From | ``` typealias Distance = I.Distance ``` |
| To | ``` typealias Distance = Base.Distance ``` |

Modified Set.Index

|  | Declaration |
| --- | --- |
| From | ``` typealias Index = SetIndex<T> ``` |
| To | ``` typealias Index = SetIndex<Element> ``` |

Modified sizeof<T>(_: T.Type) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func sizeof<T>(_ _: T.Type) -> Int ``` | iOS 8.0 | -- |
| To | ``` @warn_unused_result func sizeof<T>(_ _: T.Type) -> Int ``` | iOS 9.0 | T |

Modified sizeofValue<T>(_: T) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func sizeofValue<T>(_ _: T) -> Int ``` | iOS 8.0 | -- |
| To | ``` @warn_unused_result func sizeofValue<T>(_ _: T) -> Int ``` | iOS 9.0 | T |

Modified Strideable.Stride

|  | Introduction |
| --- | --- |
| From | iOS 8.0 |
| To | iOS 9.0 |

Modified strideof<T>(_: T.Type) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func strideof<T>(_ _: T.Type) -> Int ``` | iOS 8.0 | -- |
| To | ``` @warn_unused_result func strideof<T>(_ _: T.Type) -> Int ``` | iOS 9.0 | T |

Modified strideofValue<T>(_: T) -> Int

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func strideofValue<T>(_ _: T) -> Int ``` | iOS 8.0 | -- |
| To | ``` @warn_unused_result func strideofValue<T>(_ _: T) -> Int ``` | iOS 9.0 | T |

Modified swap<T>(_: T, _: T)

|  | Introduction | Generics[Parameters] |
| --- | --- | --- |
| From | iOS 8.0 | -- |
| To | iOS 9.0 | T |

Modified unsafeAddressOf(_: AnyObject) -> UnsafePointer<Void>

|  | Declaration |
| --- | --- |
| From | ``` func unsafeAddressOf(_ object: AnyObject) -> UnsafePointer<Void> ``` |
| To | ``` @warn_unused_result func unsafeAddressOf(_ object: AnyObject) -> UnsafePointer<Void> ``` |

Modified unsafeBitCast<T, U>(_: T, _: U.Type) -> U

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func unsafeBitCast<T, U>(_ x: T, _ _: U.Type) -> U ``` | iOS 8.0 | -- |
| To | ``` @warn_unused_result func unsafeBitCast<T, U>(_ x: T, _ _: U.Type) -> U ``` | iOS 9.0 | T, U |

Modified unsafeDowncast<T>(_: AnyObject) -> T

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func unsafeDowncast<T>(_ x: AnyObject) -> T ``` | iOS 8.1 | ```  ``` | -- |
| To | ``` @warn_unused_result func unsafeDowncast<T>(_ x: AnyObject) -> T ``` | iOS 9.0 | ``` T : AnyObject ``` | T |

Modified unsafeUnwrap<T>(_: T?) -> T

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` @inline(__always) func unsafeUnwrap<T>(_ nonEmpty: T?) -> T ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func unsafeUnwrap<T>(_ nonEmpty: T?) -> T ``` | iOS 9.0 | T |

Modified withVaList<R>(_: VaListBuilder, _: CVaListPointer -> R) -> R

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func withVaList<R>(_ builder: VaListBuilder, _ f: @noescape CVaListPointer -> R) -> R ``` | iOS 8.0 | -- |
| To | ``` func withVaList<R>(_ builder: VaListBuilder, @noescape _ f: CVaListPointer -> R) -> R ``` | iOS 9.0 | R |

Modified withVaList<R>(_: [CVarArgType], _: CVaListPointer -> R) -> R

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func withVaList<R>(_ args: [CVarArgType], _ f: @noescape CVaListPointer -> R) -> R ``` | iOS 8.0 | -- |
| To | ``` func withVaList<R>(_ args: [CVarArgType], @noescape _ f: CVaListPointer -> R) -> R ``` | iOS 9.0 | R |

Modified |=(_: T, _: T)

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func |=<T : BitwiseOperationsType>(inout _ lhs: T, _ rhs: T) ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func |=<T : BitwiseOperationsType>(inout _ lhs: T, _ rhs: T) ``` | iOS 9.0 | ``` T : BitwiseOperationsType ``` | T |

Modified ~(_: UInt64) -> UInt64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: UInt32) -> UInt32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: Int64) -> Int64

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: UInt16) -> UInt16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: Int32) -> Int32

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: UInt8) -> UInt8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: Int) -> Int

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: UInt) -> UInt

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: Int16) -> Int16

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~(_: Int8) -> Int8

|  | Operator Fixity |
| --- | --- |
| From | -- |
| To | prefix |

Modified ~=(_: Range<I>, _: I) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ~=<I : ForwardIndexType where I : Comparable>(_ pattern: Range<I>, _ value: I) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ~=<I : ForwardIndexType where I : Comparable>(_ pattern: Range<I>, _ value: I) -> Bool ``` | iOS 9.0 | ``` I : ForwardIndexType, I : Comparable ``` | I |

Modified ~=(_: _OptionalNilComparisonType, _: T?) -> Bool

|  | Declaration | Introduction | Generics[Parameters] |
| --- | --- | --- | --- |
| From | ``` func ~=<T>(_ lhs: _OptionalNilComparisonType, _ rhs: T?) -> Bool ``` | iOS 8.3 | -- |
| To | ``` @warn_unused_result func ~=<T>(_ lhs: _OptionalNilComparisonType, _ rhs: T?) -> Bool ``` | iOS 9.0 | T |

Modified ~=(_: T, _: T) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ~=<T : Equatable>(_ a: T, _ b: T) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ~=<T : Equatable>(_ a: T, _ b: T) -> Bool ``` | iOS 9.0 | ``` T : Equatable ``` | T |

Modified ~=(_: I, _: I.Bound) -> Bool

|  | Declaration | Introduction | Generics[Constraints] | Generics[Parameters] |
| --- | --- | --- | --- | --- |
| From | ``` func ~=<I : IntervalType>(_ pattern: I, _ value: I.Bound) -> Bool ``` | iOS 8.3 | ```  ``` | -- |
| To | ``` @warn_unused_result func ~=<I : IntervalType>(_ pattern: I, _ value: I.Bound) -> Bool ``` | iOS 9.0 | ``` I : IntervalType ``` | I |

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
