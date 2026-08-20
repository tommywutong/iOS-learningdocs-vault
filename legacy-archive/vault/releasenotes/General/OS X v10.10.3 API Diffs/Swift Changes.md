---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/Swift.html
archived_at: '2026-07-18T02:52:41.372256Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Swift Changes

## Swift

Removed AbsoluteValuable.abs() -> Self [class]Removed Array.convertFromArrayLiteral(T) -> [T] [static]Removed Array.getMirror() -> MirrorRemoved Array.withUnsafeMutableStorage((inoutUnsafeMutableArray<T>) -> R) -> RRemoved Array.withUnsafePointerToElements((UnsafePointer<T>) -> R) -> RRemoved ArrayBoundRemoved ArrayBound.getArrayBoundValue() -> ArrayBoundTypeRemoved ArrayLiteralConvertible.convertFromArrayLiteral(Element) -> Self [class]Removed ArrayTypeRemoved ArrayType.init()Removed ArrayType.+=(Self, _: S) [class]Removed ArrayType.+=(Self, _: Self.GeneratorType.Element) [class]Removed ArrayType.init(_: _Buffer)Removed ArrayType.append(Self.GeneratorType.Element)Removed ArrayType.capacityRemoved ArrayType.countRemoved ArrayType.init(count: Int, repeatedValue: Self.GeneratorType.Element)Removed ArrayType.extend(S)Removed ArrayType.insert(Self.GeneratorType.Element, atIndex: Int)Removed ArrayType.isEmptyRemoved ArrayType.join(S) -> SelfRemoved ArrayType.reduce(U, combine:(U, Self.GeneratorType.Element) -> U) -> URemoved ArrayType.removeAll(Bool)Removed ArrayType.removeAtIndex(Int) -> Self.GeneratorType.ElementRemoved ArrayType.removeLast() -> Self.GeneratorType.ElementRemoved ArrayType.reserveCapacity(Int)Removed ArrayType.sort((Self.GeneratorType.Element, Self.GeneratorType.Element) -> Bool)Removed AutoreleasingUnsafePointer [struct]Removed AutoreleasingUnsafePointer.init()Removed AutoreleasingUnsafePointer.init(_: ConstUnsafePointer<U>)Removed AutoreleasingUnsafePointer.init(_: UnsafePointer<U>)Removed AutoreleasingUnsafePointer.convertFromNilLiteral() -> AutoreleasingUnsafePointer<T> [static]Removed AutoreleasingUnsafePointer.getLogicValue() -> BoolRemoved AutoreleasingUnsafePointer.memoryRemoved AutoreleasingUnsafePointer.null() -> AutoreleasingUnsafePointer<T> [static]Removed BidirectionalIndexRemoved Bit.getMirror() -> MirrorRemoved Bit.oneRemoved Bit.zeroRemoved BitwiseOperationsRemoved BitwiseOperations.&(Self, _: Self) -> Self [class]Removed BitwiseOperations.^(Self, _: Self) -> Self [class]Removed BitwiseOperations.allZerosRemoved BitwiseOperations.|(Self, _: Self) -> Self [class]Removed BitwiseOperations.~() -> Self [class]Removed Bool.init(_: LogicValue)Removed Bool.convertFromBooleanLiteral(Bool) -> Bool [static]Removed Bool.getLogicValue() -> BoolRemoved Bool.getMirror() -> MirrorRemoved BooleanLiteralConvertible.convertFromBooleanLiteral(BooleanLiteralType) -> Self [class]Removed CFunctionPointer.convertFromNilLiteral() -> CFunctionPointer<T> [static]Removed CFunctionPointer.getLogicValue() -> BoolRemoved CFunctionPointer.null() -> CFunctionPointer<T> [static]Removed COpaquePointer.convertFromNilLiteral() -> COpaquePointer [static]Removed COpaquePointer.getLogicValue() -> BoolRemoved COpaquePointer.null() -> COpaquePointer [static]Removed CVaListPointer.init(fromUnsafePointer: UnsafePointer<Void>)Removed CVarArgRemoved CVarArg.encode() -> [Word]Removed Character [enum]Removed Character.LargeRepresentationRemoved Character.SmallRepresentationRemoved Character.init(_: String)Removed Character.init(_: UnicodeScalar)Removed Character.convertFromExtendedGraphemeClusterLiteral(Character) -> Character [static]Removed Character.getMirror() -> MirrorRemoved Character.writeTo(Target)Removed CharacterLiteralConvertible.convertFromCharacterLiteral(CharacterLiteralType) -> Self [class]Removed CodeUnit.fromUTF16CodeUnit(CodeUnit) -> CodeUnit [static]Removed CodeUnit.toUTF16CodeUnit(CodeUnit) -> CodeUnit [static]Removed CollectionRemoved CollectionOfOne.getMirror() -> MirrorRemoved ConstUnsafePointer [struct]Removed ConstUnsafePointer.init()Removed ConstUnsafePointer.init(_: COpaquePointer)Removed ConstUnsafePointer.init(_: ConstUnsafePointer<U>)Removed ConstUnsafePointer.init(_: Int)Removed ConstUnsafePointer.init(_: UnsafePointer<U>)Removed ConstUnsafePointer.convertFromNilLiteral() -> ConstUnsafePointer<T> [static]Removed ConstUnsafePointer.descriptionRemoved ConstUnsafePointer.getLogicValue() -> BoolRemoved ConstUnsafePointer.getMirror() -> MirrorRemoved ConstUnsafePointer.hashValueRemoved ConstUnsafePointer.memoryRemoved ConstUnsafePointer.null() -> ConstUnsafePointer<T> [static]Removed ConstUnsafePointer.predecessor() -> ConstUnsafePointer<T>Removed ConstUnsafePointer.successor() -> ConstUnsafePointer<T>Removed ContiguousArray.convertFromArrayLiteral(T) -> ContiguousArray<T> [static]Removed ContiguousArray.getMirror() -> MirrorRemoved ContiguousArray.withUnsafeMutableStorage((inoutUnsafeMutableArray<T>) -> R) -> RRemoved ContiguousArray.withUnsafePointerToElements((UnsafePointer<T>) -> R) -> RRemoved Dictionary.convertFromDictionaryLiteral((KeyType, ValueType)) -> [KeyType: ValueType] [static]Removed Dictionary.generate() -> DictionaryGenerator<KeyType, ValueType>Removed Dictionary.getMirror() -> MirrorRemoved Dictionary.indexForKey(KeyType) -> DictionaryIndex<KeyType, ValueType>?Removed Dictionary.removeAtIndex(DictionaryIndex<KeyType, ValueType>)Removed DictionaryIndex.predecessor() -> DictionaryIndex<KeyType, ValueType>Removed DictionaryLiteralConvertible.convertFromDictionaryLiteral((Key, Value)) -> Self [class]Removed Double.convertFromFloatLiteral(Double) -> Double [static]Removed Double.convertFromIntegerLiteral(Int64) -> Double [static]Removed EmptyCollection.getMirror() -> MirrorRemoved ExtendedGraphemeClusterLiteralConvertible.convertFromExtendedGraphemeClusterLiteral(ExtendedGraphemeClusterLiteralType) -> Self [class]Removed ExtensibleCollectionRemoved FilterCollectionView.init(_: Base, includeElement:(Base.GeneratorType.Element) -> Bool)Removed FilterCollectionView.generate() -> FilterGenerator<Base.GeneratorType>Removed FilterSequenceView.generate() -> FilterGenerator<Base.GeneratorType>Removed Float.convertFromFloatLiteral(Float) -> Float [static]Removed Float.convertFromIntegerLiteral(Int64) -> Float [static]Removed Float32.getMirror() -> MirrorRemoved Float64.getMirror() -> MirrorRemoved Float80.convertFromFloatLiteral(Float80) -> Float80 [static]Removed Float80.convertFromIntegerLiteral(Int64) -> Float80 [static]Removed FloatLiteralConvertible.convertFromFloatLiteral(FloatLiteralType) -> Self [class]Removed FloatingPointNumberRemoved FloatingPointNumber.NaNRemoved FloatingPointNumber.floatingPointClassRemoved FloatingPointNumber.infinityRemoved FloatingPointNumber.isFiniteRemoved FloatingPointNumber.isInfiniteRemoved FloatingPointNumber.isNaNRemoved FloatingPointNumber.isNormalRemoved FloatingPointNumber.isSignMinusRemoved FloatingPointNumber.isSignalingRemoved FloatingPointNumber.isSubnormalRemoved FloatingPointNumber.isZeroRemoved FloatingPointNumber.quietNaNRemoved ForwardIndexRemoved GeneratorRemoved Generator.next() -> Element?Removed HeapBuffer [struct]Removed HeapBuffer.init()Removed HeapBuffer.init(_: HeapBufferStorage<Value, Element>)Removed HeapBuffer.init(_: HeapBufferStorageBase.Type, _: Value, _: Int)Removed HeapBuffer.elementStorageRemoved HeapBuffer.getLogicValue() -> BoolRemoved HeapBuffer.isUniquelyReferenced() -> BoolRemoved HeapBuffer.storageRemoved HeapBuffer.valueRemoved HeapBufferStorageRemoved HeapBufferStorage.deinitRemoved HeapBufferStorageBaseRemoved ImplicitlyUnwrappedOptional.bridgeFromObjectiveC(AnyObject) -> T! [static]Removed ImplicitlyUnwrappedOptional.bridgeFromObjectiveCConditional(AnyObject) -> T!? [static]Removed ImplicitlyUnwrappedOptional.bridgeToObjectiveC() -> AnyObjectRemoved ImplicitlyUnwrappedOptional.convertFromNilLiteral() -> T! [static]Removed ImplicitlyUnwrappedOptional.getLogicValue() -> BoolRemoved ImplicitlyUnwrappedOptional.getMirror() -> MirrorRemoved ImplicitlyUnwrappedOptional.getObjectiveCType() -> Any.Type [static]Removed ImplicitlyUnwrappedOptional.isBridgedToObjectiveC() -> Bool [static]Removed Int.asUnsigned() -> UIntRemoved Int.convertFromIntegerLiteral(Int) -> Int [static]Removed Int.from(IntMax) -> Int [static]Removed Int.getArrayBoundValue() -> IntRemoved Int.getMirror() -> MirrorRemoved Int16.asUnsigned() -> UInt16Removed Int16.convertFromIntegerLiteral(Int16) -> Int16 [static]Removed Int16.from(IntMax) -> Int16 [static]Removed Int16.getArrayBoundValue() -> Int16Removed Int16.getMirror() -> MirrorRemoved Int32.asUnsigned() -> UInt32Removed Int32.convertFromIntegerLiteral(Int32) -> Int32 [static]Removed Int32.from(IntMax) -> Int32 [static]Removed Int32.getArrayBoundValue() -> Int32Removed Int32.getMirror() -> MirrorRemoved Int64.asUnsigned() -> UInt64Removed Int64.convertFromIntegerLiteral(Int64) -> Int64 [static]Removed Int64.from(IntMax) -> Int64 [static]Removed Int64.getArrayBoundValue() -> Int64Removed Int64.getMirror() -> MirrorRemoved Int8.asUnsigned() -> UInt8Removed Int8.convertFromIntegerLiteral(Int8) -> Int8 [static]Removed Int8.from(IntMax) -> Int8 [static]Removed Int8.getArrayBoundValue() -> Int8Removed Int8.getMirror() -> MirrorRemoved IntEncoder [struct]Removed IntEncoder.asIntRemoved IntEncoder.put(CodeUnit)Removed IntEncoder.shiftRemoved IntegerRemoved IntegerArithmeticRemoved IntegerArithmetic.%(Self, _: Self) -> Self [class]Removed IntegerArithmetic.\*(Self, _: Self) -> Self [class]Removed IntegerArithmetic.+(Self, _: Self) -> Self [class]Removed IntegerArithmetic.-(Self, _: Self) -> Self [class]Removed IntegerArithmetic.\ [class]Removed IntegerArithmetic.toIntMax() -> IntMaxRemoved IntegerLiteralConvertible.convertFromIntegerLiteral(IntegerLiteralType) -> Self [class]Removed LazyBidirectionalCollection.filter((S.GeneratorType.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazyBidirectionalCollection.generate() -> S.GeneratorTypeRemoved LazyBidirectionalCollection.map((S.GeneratorType.Element) -> U) -> LazyBidirectionalCollection<MapCollectionView<S, U>>Removed LazyForwardCollection.filter((S.GeneratorType.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazyForwardCollection.generate() -> S.GeneratorTypeRemoved LazyForwardCollection.map((S.GeneratorType.Element) -> U) -> LazyForwardCollection<MapCollectionView<S, U>>Removed LazyRandomAccessCollection.filter((S.GeneratorType.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazyRandomAccessCollection.generate() -> S.GeneratorTypeRemoved LazyRandomAccessCollection.map((S.GeneratorType.Element) -> U) -> LazyRandomAccessCollection<MapCollectionView<S, U>>Removed LazySequence.filter((S.GeneratorType.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Removed LazySequence.generate() -> S.GeneratorTypeRemoved LazySequence.map((S.GeneratorType.Element) -> U) -> LazySequence<MapSequenceView<S, U>>Removed Less [struct]Removed Less.compare(T, _: T) -> Bool [static]Removed LogicValueRemoved LogicValue.getLogicValue() -> BoolRemoved MapCollectionView.generate() -> MapSequenceGenerator<Base.GeneratorType, T>Removed MapSequenceView.generate() -> MapSequenceGenerator<Base.GeneratorType, T>Removed MirrorRemoved Mirror.countRemoved Mirror.dispositionRemoved Mirror.objectIdentifierRemoved Mirror.quickLookObjectRemoved Mirror.summaryRemoved Mirror.valueRemoved Mirror.valueTypeRemoved MutableCollectionRemoved NilLiteralConvertible.convertFromNilLiteral() -> Self [class]Removed ObjectIdentifier.uintValue() -> UIntRemoved OnHeap [struct]Removed OnHeap.init(_: T)Removed Optional.convertFromNilLiteral() -> T? [static]Removed Optional.getLogicValue() -> BoolRemoved Optional.getMirror() -> MirrorRemoved OutputStreamRemoved OutputStream.write(String)Removed RandomAccessIndexRemoved Range.getLogicValue() -> BoolRemoved Range.getMirror() -> MirrorRemoved RawOptionSetRemoved RawOptionSet.fromMask(Self.RawType) -> Self [class]Removed RawRepresentable.fromRaw(RawType) -> Self? [class]Removed RawRepresentable.toRaw() -> RawTypeRemoved Reflectable.getMirror() -> MirrorRemoved ReverseRandomAccessIndex.advancedBy(I.DistanceType) -> ReverseRandomAccessIndex<I>Removed ReverseRandomAccessIndex.distanceTo(ReverseRandomAccessIndex<I>) -> I.DistanceTypeRemoved SequenceRemoved Sequence.generate() -> GeneratorTypeRemoved SignedIntegerRemoved SignedNumberRemoved SignedNumber.-(Self) -> Self [class]Removed SinkRemoved Sink.put(Element)Removed Slice [struct]Removed Slice.init()Removed Slice.init(_: S)Removed Slice.append(T)Removed Slice.capacityRemoved Slice.convertFromArrayLiteral(T) -> Slice<T> [static]Removed Slice.countRemoved Slice.init(count: Int, repeatedValue: T)Removed Slice.debugDescriptionRemoved Slice.descriptionRemoved Slice.endIndexRemoved Slice.extend(S)Removed Slice.filter((T) -> Bool) -> Slice<T>Removed Slice.generate() -> IndexingGenerator<Slice<T>>Removed Slice.getMirror() -> MirrorRemoved Slice.insert(T, atIndex: Int)Removed Slice.isEmptyRemoved Slice.join(S) -> Slice<T>Removed Slice.map((T) -> U) -> Slice<U>Removed Slice.reduce(U, combine:(U, T) -> U) -> URemoved Slice.removeAll(Bool)Removed Slice.removeAtIndex(Int) -> TRemoved Slice.removeLast() -> TRemoved Slice.replaceRange(Range<Int>, with: C)Removed Slice.reserveCapacity(Int)Removed Slice.reverse() -> Slice<T>Removed Slice.sort((T, T) -> Bool)Removed Slice.sorted((T, T) -> Bool) -> Slice<T>Removed Slice.startIndexRemoved Slice.withUnsafeMutableStorage((inoutUnsafeMutableArray<T>) -> R) -> RRemoved Slice.withUnsafePointerToElements((UnsafePointer<T>) -> R) -> RRemoved StaticString.convertFromExtendedGraphemeClusterLiteral(StaticString) -> StaticString [static]Removed StaticString.convertFromStringLiteral(StaticString) -> StaticString [static]Removed String.compare(String) -> IntRemoved String.convertFromExtendedGraphemeClusterLiteral(String) -> String [static]Removed String.convertFromStringInterpolation(String) -> String [static]Removed String.convertFromStringInterpolationSegment(T) -> String [static]Removed String.convertFromStringLiteral(String) -> String [static]Removed String.fromCString(ConstUnsafePointer<CChar>) -> String? [static]Removed String.fromCStringRepairingIllFormedUTF8(ConstUnsafePointer<CChar>) -> (String?, hadError: Bool) [static]Removed String.getMirror() -> MirrorRemoved String.withCString((ConstUnsafePointer<Int8>) -> Result) -> ResultRemoved String.Index.getMirror() -> MirrorRemoved String.UTF16View.getMirror() -> MirrorRemoved String.UTF8View.getMirror() -> MirrorRemoved String.UnicodeScalarView.compare(String.UnicodeScalarView) -> IntRemoved String.UnicodeScalarView.generate() -> String.UnicodeScalarView.GeneratorTypeRemoved String.UnicodeScalarView.GeneratorType [struct]Removed String.UnicodeScalarView.GeneratorType.next() -> UnicodeScalar?Removed String.UnicodeScalarView.IndexType [struct]Removed String.UnicodeScalarView.IndexType.predecessor() -> String.UnicodeScalarView.IndexTypeRemoved String.UnicodeScalarView.IndexType.successor() -> String.UnicodeScalarView.IndexTypeRemoved StringElementRemoved StringElement.fromUTF16CodeUnit(CodeUnit) -> Self [class]Removed StringElement.toUTF16CodeUnit() -> CodeUnit [class]Removed StringInterpolationConvertible.convertFromStringInterpolation(Self) -> Self [class]Removed StringInterpolationConvertible.convertFromStringInterpolationSegment(T) -> Self [class]Removed StringLiteralConvertible.convertFromStringLiteral(StringLiteralType) -> Self [class]Removed UInt.asSigned() -> IntRemoved UInt.convertFromIntegerLiteral(UInt) -> UInt [static]Removed UInt.from(UIntMax) -> UInt [static]Removed UInt.getArrayBoundValue() -> UIntRemoved UInt.getMirror() -> MirrorRemoved UInt16.asSigned() -> Int16Removed UInt16.convertFromIntegerLiteral(UInt16) -> UInt16 [static]Removed UInt16.from(UIntMax) -> UInt16 [static]Removed UInt16.getArrayBoundValue() -> UInt16Removed UInt16.getMirror() -> MirrorRemoved UInt32.asSigned() -> Int32Removed UInt32.convertFromIntegerLiteral(UInt32) -> UInt32 [static]Removed UInt32.from(UIntMax) -> UInt32 [static]Removed UInt32.getArrayBoundValue() -> UInt32Removed UInt32.getMirror() -> MirrorRemoved UInt64.asSigned() -> Int64Removed UInt64.convertFromIntegerLiteral(UInt64) -> UInt64 [static]Removed UInt64.from(UIntMax) -> UInt64 [static]Removed UInt64.getArrayBoundValue() -> UInt64Removed UInt64.getMirror() -> MirrorRemoved UInt8.init(_: UnicodeScalar)Removed UInt8.asSigned() -> Int8Removed UInt8.convertFromIntegerLiteral(UInt8) -> UInt8 [static]Removed UInt8.from(UIntMax) -> UInt8 [static]Removed UInt8.getArrayBoundValue() -> UInt8Removed UInt8.getMirror() -> MirrorRemoved UTF16.copy(UnsafePointer<T>, destination: UnsafePointer<U>, count: Int) [static]Removed UnicodeCodecRemoved UnicodeCodec.init()Removed UnicodeCodec.decode(G) -> UnicodeDecodingResultRemoved UnicodeCodec.encode(UnicodeScalar, output: S) [class]Removed UnicodeScalar.convertFromExtendedGraphemeClusterLiteral(String) -> UnicodeScalar [static]Removed UnicodeScalar.getMirror() -> MirrorRemoved UnsafeArray [struct]Removed UnsafeArray.endIndexRemoved UnsafeArray.generate() -> UnsafeArrayGenerator<T>Removed UnsafeArray.init(start: UnsafePointer<T>, length: Int)Removed UnsafeArray.startIndexRemoved UnsafeArrayGenerator [struct]Removed UnsafeArrayGenerator.endRemoved UnsafeArrayGenerator.generate() -> UnsafeArrayGenerator<T>Removed UnsafeArrayGenerator.next() -> T?Removed UnsafeArrayGenerator.positionRemoved UnsafeMutableArray [struct]Removed UnsafeMutableArray.endIndexRemoved UnsafeMutableArray.generate() -> UnsafeArrayGenerator<T>Removed UnsafeMutableArray.init(start: UnsafePointer<T>, length: Int)Removed UnsafeMutableArray.startIndexRemoved UnsafePointer.init(_: ConstUnsafePointer<U>)Removed UnsafePointer.init(_: Int)Removed UnsafePointer.alloc(Int) -> UnsafePointer<T> [static]Removed UnsafePointer.convertFromNilLiteral() -> UnsafePointer<T> [static]Removed UnsafePointer.dealloc(Int)Removed UnsafePointer.descriptionRemoved UnsafePointer.destroy()Removed UnsafePointer.destroy(Int)Removed UnsafePointer.getLogicValue() -> BoolRemoved UnsafePointer.getMirror() -> MirrorRemoved UnsafePointer.initialize(T)Removed UnsafePointer.initializeFrom(C)Removed UnsafePointer.initializeFrom(UnsafePointer<T>, count: Int)Removed UnsafePointer.move() -> TRemoved UnsafePointer.moveAssignFrom(UnsafePointer<T>, count: Int)Removed UnsafePointer.moveInitializeBackwardFrom(UnsafePointer<T>, count: Int)Removed UnsafePointer.moveInitializeFrom(UnsafePointer<T>, count: Int)Removed UnsafePointer.null() -> UnsafePointer<T> [static]Removed UnsignedIntegerRemoved VaListBuilder.append(CVarArg)Removed Zip2.generate() -> GeneratorTypeRemoved Array.SliceTypeRemoved ArrayBound.ArrayBoundTypeRemoved BidirectionalReverseView.GeneratorTypeRemoved BidirectionalReverseView.IndexTypeRemoved C_ARGCRemoved C_ARGVRemoved CollectionOfOne.IndexTypeRemoved ContiguousArray.SliceTypeRemoved EmptyCollection.IndexTypeRemoved EnumerateGenerator.GeneratorTypeRemoved FilterCollectionView.IndexTypeRemoved Generator.ElementRemoved HeapBuffer.StorageRemoved HeapBufferStorage.BufferRemoved ImplicitlyUnwrappedOptional.ObjectiveCTypeRemoved Int.ArrayBoundTypeRemoved Int16.ArrayBoundTypeRemoved Int32.ArrayBoundTypeRemoved Int64.ArrayBoundTypeRemoved Int8.ArrayBoundTypeRemoved MaxBuiltinFloatTypeRemoved MaxBuiltinIntegerTypeRemoved OnHeap.BufferRemoved PermutationGenerator.GeneratorTypeRemoved RandomAccessReverseView.GeneratorTypeRemoved RandomAccessReverseView.IndexTypeRemoved Range.GeneratorTypeRemoved Range.IndexTypeRemoved Range.SliceTypeRemoved RangeGenerator.GeneratorTypeRemoved RawRepresentable.RawTypeRemoved Repeat.IndexTypeRemoved ReverseBidirectionalIndex.DistanceTypeRemoved ReverseRandomAccessIndex.DistanceTypeRemoved Sequence.GeneratorTypeRemoved Sink.ElementRemoved Slice.ElementRemoved Slice.SliceTypeRemoved Sliceable.SliceTypeRemoved String.UTF16View.GeneratorTypeRemoved UInt.ArrayBoundTypeRemoved UInt16.ArrayBoundTypeRemoved UInt32.ArrayBoundTypeRemoved UInt64.ArrayBoundTypeRemoved UInt8.ArrayBoundTypeRemoved UnicodeCodec.CodeUnitRemoved Zip2.GeneratorTypeRemoved advance(T, T.DistanceType) -> TRemoved advance(T, T.DistanceType, T) -> TRemoved assert(() -> Bool, StaticString, StaticString, UWord)Removed assert(() -> T, StaticString, StaticString, UWord)Removed contains(S,(S.GeneratorType.Element) -> L) -> BoolRemoved contains(S, S.GeneratorType.Element) -> BoolRemoved count(Range<I>) -> I.DistanceTypeRemoved countElements(T) -> T.IndexType.DistanceTypeRemoved distance(T, T) -> T.DistanceTypeRemoved dropFirst(Seq) -> Seq.SliceTypeRemoved dropLast(Seq) -> Seq.SliceTypeRemoved dump(T, String?, Int, Int, Int, TargetStream) -> TRemoved enumerate(Seq) -> EnumerateGenerator<Seq.GeneratorType>Removed equal(S1, S2,(S1.GeneratorType.Element, S1.GeneratorType.Element) -> Bool) -> BoolRemoved fatalError(StaticString, StaticString, UWord)Removed filter(S,(S.GeneratorType.Element) -> Bool) -> [S.GeneratorType.Element]Removed find(C, C.GeneratorType.Element) -> C.IndexType?Removed getVaList([CVarArg]) -> CVaListPointerRemoved indices(Seq) -> Range<Seq.IndexType>Removed lexicographicalCompare(S1, S2,(S1.GeneratorType.Element, S1.GeneratorType.Element) -> Bool) -> BoolRemoved map(C,(C.GeneratorType.Element) -> T) -> [T]Removed map(S,(S.GeneratorType.Element) -> T) -> [T]Removed maxElement(R) -> R.GeneratorType.ElementRemoved minElement(R) -> R.GeneratorType.ElementRemoved partition(C, Range<C.IndexType>) -> C.IndexTypeRemoved partition(C, Range<C.IndexType>,(C.GeneratorType.Element, C.GeneratorType.Element) -> Bool) -> C.IndexTypeRemoved reduce(S, U,(U, S.GeneratorType.Element) -> U) -> URemoved reflect(T) -> MirrorRemoved reinterpretCast(T) -> URemoved reverse(C) -> [C.GeneratorType.Element]Removed sort(C,(C.GeneratorType.Element, C.GeneratorType.Element) -> Bool)Removed sorted(C) -> CRemoved sorted(C,(C.GeneratorType.Element, C.GeneratorType.Element) -> Bool) -> CRemoved sorted(S) -> [S.GeneratorType.Element]Removed sorted(S,(S.GeneratorType.Element, S.GeneratorType.Element) -> Bool) -> [S.GeneratorType.Element]Removed split(Seq,(Seq.GeneratorType.Element) -> R, Int, Bool) -> [Seq.SliceType]Removed transcode(InputEncoding.Type, OutputEncoding.Type, Input, Output, Bool) -> (hadError: Bool)Removed withVaList([CVarArg],(CVaListPointer) -> R) -> RAdded AbsoluteValuable.abs(Self) -> Self [class]Added Array.init(_: _ArrayBuffer<T>)Added Array.init(_fromCocoaArray: _NSArrayCoreType, noCopy: Bool)Added Array.init(_uninitializedCount: Int)Added Array.init(arrayLiteral: T)Added Array.firstAdded Array.flatMap((T) -> [U]) -> [U]Added Array.getMirror() -> MirrorTypeAdded Array.lastAdded Array.removeRange(Range<Int>)Added Array.splice(S, atIndex: Int)Added Array.withUnsafeBufferPointer((UnsafeBufferPointer<T>) -> R) -> RAdded Array.withUnsafeMutableBufferPointer((inoutUnsafeMutableBufferPointer<T>) -> R) -> RAdded ArrayLiteralConvertible.init(arrayLiteral: Element)Added ArraySlice [struct]Added ArraySlice.init()Added ArraySlice.init(_: S)Added ArraySlice.init(_: _SliceBuffer<T>)Added ArraySlice.init(_uninitializedCount: Int)Added ArraySlice.append(T)Added ArraySlice.init(arrayLiteral: T)Added ArraySlice.capacityAdded ArraySlice.countAdded ArraySlice.init(count: Int, repeatedValue: T)Added ArraySlice.debugDescriptionAdded ArraySlice.descriptionAdded ArraySlice.endIndexAdded ArraySlice.extend(S)Added ArraySlice.filter((T) -> Bool) -> ArraySlice<T>Added ArraySlice.firstAdded ArraySlice.flatMap((T) -> ArraySlice<U>) -> ArraySlice<U>Added ArraySlice.generate() -> IndexingGenerator<ArraySlice<T>>Added ArraySlice.getMirror() -> MirrorTypeAdded ArraySlice.insert(T, atIndex: Int)Added ArraySlice.isEmptyAdded ArraySlice.join(S) -> ArraySlice<T>Added ArraySlice.lastAdded ArraySlice.map((T) -> U) -> ArraySlice<U>Added ArraySlice.reduce(U, combine:(U, T) -> U) -> UAdded ArraySlice.removeAll(Bool)Added ArraySlice.removeAtIndex(Int) -> TAdded ArraySlice.removeLast() -> TAdded ArraySlice.removeRange(Range<Int>)Added ArraySlice.replaceRange(Range<Int>, with: C)Added ArraySlice.reserveCapacity(Int)Added ArraySlice.reverse() -> ArraySlice<T>Added ArraySlice.sort((T, T) -> Bool)Added ArraySlice.sorted((T, T) -> Bool) -> ArraySlice<T>Added ArraySlice.splice(S, atIndex: Int)Added ArraySlice.startIndexAdded ArraySlice.withUnsafeBufferPointer((UnsafeBufferPointer<T>) -> R) -> RAdded ArraySlice.withUnsafeMutableBufferPointer((inoutUnsafeMutableBufferPointer<T>) -> R) -> RAdded AutoreleasingUnsafeMutablePointer [struct]Added AutoreleasingUnsafeMutablePointer.init()Added AutoreleasingUnsafeMutablePointer.init(_: UnsafeMutablePointer<U>)Added AutoreleasingUnsafeMutablePointer.init(_: UnsafePointer<U>)Added AutoreleasingUnsafeMutablePointer.debugDescriptionAdded AutoreleasingUnsafeMutablePointer.encode() -> [Word]Added AutoreleasingUnsafeMutablePointer.memoryAdded AutoreleasingUnsafeMutablePointer.init(nilLiteral: ())Added BidirectionalIndexTypeAdded Bit.OneAdded Bit.ZeroAdded Bit.getMirror() -> MirrorTypeAdded BitwiseOperationsTypeAdded BitwiseOperationsType.&(Self, _: Self) -> Self [class]Added BitwiseOperationsType.^(Self, _: Self) -> Self [class]Added BitwiseOperationsType.allZerosAdded BitwiseOperationsType.|(Self, _: Self) -> Self [class]Added BitwiseOperationsType.~(Self) -> Self [class]Added Bool.init(_: Builtin.Int1)Added Bool.init(_: T)Added Bool.init(_builtinBooleanLiteral: Builtin.Int1)Added Bool.boolValueAdded Bool.init(booleanLiteral: Bool)Added Bool.getMirror() -> MirrorTypeAdded Bool.valueAdded BooleanLiteralConvertible.init(booleanLiteral: BooleanLiteralType)Added BooleanTypeAdded BooleanType.boolValueAdded CFunctionPointer.debugDescriptionAdded CFunctionPointer.encode() -> [Word]Added CFunctionPointer.init(nilLiteral: ())Added COpaquePointer.init(_: Builtin.RawPointer)Added COpaquePointer.init(_: UnsafeMutablePointer<T>)Added COpaquePointer.init(bitPattern: UWord)Added COpaquePointer.init(bitPattern: Word)Added COpaquePointer.debugDescriptionAdded COpaquePointer.init(nilLiteral: ())Added CVaListPointer.init(_fromUnsafeMutablePointer: UnsafeMutablePointer<Void>)Added CVaListPointer.debugDescriptionAdded CVarArgTypeAdded CVarArgType.encode() -> [Word]Added Character [struct]Added Character.init(_: String)Added Character.init(_: UnicodeScalar)Added Character.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added Character.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added Character.debugDescriptionAdded Character.init(extendedGraphemeClusterLiteral: Character)Added Character.getMirror() -> MirrorTypeAdded Character.hashValueAdded Character.init(unicodeScalarLiteral: Character)Added Character.utf16Added Character.writeTo(Target)Added Character.Representation [enum]Added Character.Representation.LargeAdded Character.Representation.SmallAdded CharacterLiteralConvertible.init(characterLiteral: CharacterLiteralType)Added ClosedInterval [struct]Added ClosedInterval.init(_: ClosedInterval<T>)Added ClosedInterval.init(_: T, _: T)Added ClosedInterval.clamp(ClosedInterval<T>) -> ClosedInterval<T>Added ClosedInterval.contains(T) -> BoolAdded ClosedInterval.debugDescriptionAdded ClosedInterval.descriptionAdded ClosedInterval.endAdded ClosedInterval.getMirror() -> MirrorTypeAdded ClosedInterval.isEmptyAdded ClosedInterval.startAdded CollectionOfOne.getMirror() -> MirrorTypeAdded CollectionTypeAdded ContiguousArray.init(_: _ContiguousArrayBuffer<T>)Added ContiguousArray.init(_uninitializedCount: Int)Added ContiguousArray.init(arrayLiteral: T)Added ContiguousArray.firstAdded ContiguousArray.flatMap((T) -> ContiguousArray<U>) -> ContiguousArray<U>Added ContiguousArray.getMirror() -> MirrorTypeAdded ContiguousArray.lastAdded ContiguousArray.removeRange(Range<Int>)Added ContiguousArray.splice(S, atIndex: Int)Added ContiguousArray.withUnsafeBufferPointer((UnsafeBufferPointer<T>) -> R) -> RAdded ContiguousArray.withUnsafeMutableBufferPointer((inoutUnsafeMutableBufferPointer<T>) -> R) -> RAdded Dictionary.init()Added Dictionary.init(dictionaryLiteral: (Key, Value))Added Dictionary.generate() -> DictionaryGenerator<Key, Value>Added Dictionary.getMirror() -> MirrorTypeAdded Dictionary.indexForKey(Key) -> DictionaryIndex<Key, Value>?Added Dictionary.removeAtIndex(DictionaryIndex<Key, Value>)Added DictionaryGeneratorRepresentation [enum]Added DictionaryIndexRepresentation [enum]Added DictionaryLiteralConvertible.init(dictionaryLiteral: (Key, Value))Added DictionaryMirrorAdded DictionaryMirror.init(_: [Key: Value])Added DictionaryMirror.countAdded DictionaryMirror.dispositionAdded DictionaryMirror.objectIdentifierAdded DictionaryMirror.quickLookObjectAdded DictionaryMirror.summaryAdded DictionaryMirror.valueAdded DictionaryMirror.valueTypeAdded DictionaryMirrorPosition [struct]Added DictionaryMirrorPosition.DictionaryPosAdded DictionaryMirrorPosition.init(_: [Key: Value])Added DictionaryMirrorPosition.successor()Added Double.init(_bits: Builtin.FPIEEE64)Added Double.init(_builtinFloatLiteral: Builtin.FPIEEE80)Added Double.init(_builtinIntegerLiteral: Builtin.Int2048)Added Double.init(floatLiteral: Double)Added Double.getMirror() -> MirrorTypeAdded Double.init(integerLiteral: Int64)Added Double.valueAdded EmptyCollection.getMirror() -> MirrorTypeAdded EmptyGenerator.init()Added EnumerateSequence [struct]Added EnumerateSequence.init(_: Base)Added EnumerateSequence.baseAdded EnumerateSequence.generate() -> EnumerateGenerator<Base.Generator>Added ExtendedGraphemeClusterLiteralConvertible.init(extendedGraphemeClusterLiteral: ExtendedGraphemeClusterLiteralType)Added ExtensibleCollectionTypeAdded FilterCollectionView.init(_: Base, includeElement:(Base.Generator.Element) -> Bool)Added FilterCollectionView.generate() -> FilterGenerator<Base.Generator>Added FilterSequenceView.generate() -> FilterGenerator<Base.Generator>Added Float.init(_bits: Builtin.FPIEEE32)Added Float.init(_builtinFloatLiteral: Builtin.FPIEEE80)Added Float.init(_builtinIntegerLiteral: Builtin.Int2048)Added Float.init(floatLiteral: Float)Added Float.getMirror() -> MirrorTypeAdded Float.init(integerLiteral: Int64)Added Float.valueAdded Float80.init(_bits: Builtin.FPIEEE80)Added Float80.init(_builtinFloatLiteral: Builtin.FPIEEE80)Added Float80.init(_builtinIntegerLiteral: Builtin.Int2048)Added Float80.init(floatLiteral: Float80)Added Float80.init(integerLiteral: Int64)Added Float80.valueAdded FloatLiteralConvertible.init(floatLiteral: FloatLiteralType)Added FloatingPointTypeAdded FloatingPointType.NaNAdded FloatingPointType.init(_: Int)Added FloatingPointType.init(_: Int16)Added FloatingPointType.init(_: Int32)Added FloatingPointType.init(_: Int64)Added FloatingPointType.init(_: Int8)Added FloatingPointType.init(_: UInt)Added FloatingPointType.init(_: UInt16)Added FloatingPointType.init(_: UInt32)Added FloatingPointType.init(_: UInt64)Added FloatingPointType.init(_: UInt8)Added FloatingPointType.floatingPointClassAdded FloatingPointType.infinityAdded FloatingPointType.isFiniteAdded FloatingPointType.isInfiniteAdded FloatingPointType.isNaNAdded FloatingPointType.isNormalAdded FloatingPointType.isSignMinusAdded FloatingPointType.isSignalingAdded FloatingPointType.isSubnormalAdded FloatingPointType.isZeroAdded FloatingPointType.quietNaNAdded ForwardIndexTypeAdded GeneratorTypeAdded GeneratorType.next() -> Element?Added HalfOpenInterval [struct]Added HalfOpenInterval.init(_: HalfOpenInterval<T>)Added HalfOpenInterval.init(_: T, _: T)Added HalfOpenInterval.clamp(HalfOpenInterval<T>) -> HalfOpenInterval<T>Added HalfOpenInterval.contains(T) -> BoolAdded HalfOpenInterval.debugDescriptionAdded HalfOpenInterval.descriptionAdded HalfOpenInterval.endAdded HalfOpenInterval.getMirror() -> MirrorTypeAdded HalfOpenInterval.isEmptyAdded HalfOpenInterval.startAdded ImplicitlyUnwrappedOptional.flatMap((T) -> U!) -> U!Added ImplicitlyUnwrappedOptional.getMirror() -> MirrorTypeAdded ImplicitlyUnwrappedOptional.init(nilLiteral: ())Added Index.init(_: String.Index, within: String.UTF16View)Added Index.init(_: String.Index, within: String.UTF8View)Added Index.init(_: UTF16Index, within: String)Added Index.init(_: UTF16Index, within: String.UTF8View)Added Index.init(_: UTF8Index, within: String)Added Index.init(_: UTF8Index, within: String.UTF16View)Added Index.init(_: UnicodeScalarIndex, within: String)Added Index.init(_: UnicodeScalarIndex, within: String.UTF16View)Added Index.init(_: UnicodeScalarIndex, within: String.UTF8View)Added Index.predecessor() -> String.UTF16View.IndexAdded Index.samePositionIn(String) -> String.Index?Added Index.samePositionIn(String.UTF16View) -> String.UTF16View.IndexAdded Index.samePositionIn(String.UTF16View) -> String.UTF16View.Index?Added Index.samePositionIn(String.UTF8View) -> String.UTF8View.IndexAdded Index.samePositionIn(String.UTF8View) -> String.UTF8View.Index?Added Index.samePositionIn(String.UnicodeScalarView) -> String.UnicodeScalarView.IndexAdded Index.samePositionIn(String.UnicodeScalarView) -> UnicodeScalarIndex?Added Index.successor() -> String.UTF16View.IndexAdded Int.init(_: Builtin.Word)Added Int.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int.init(bitPattern: UInt)Added Int.getMirror() -> MirrorTypeAdded Int.init(integerLiteral: Int)Added Int.init(truncatingBitPattern: Int64)Added Int.init(truncatingBitPattern: UInt64)Added Int.valueAdded Int16.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int16.init(bitPattern: UInt16)Added Int16.getMirror() -> MirrorTypeAdded Int16.init(integerLiteral: Int16)Added Int16.init(truncatingBitPattern: Int)Added Int16.init(truncatingBitPattern: Int32)Added Int16.init(truncatingBitPattern: Int64)Added Int16.init(truncatingBitPattern: UInt)Added Int16.init(truncatingBitPattern: UInt32)Added Int16.init(truncatingBitPattern: UInt64)Added Int16.valueAdded Int32.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int32.init(bitPattern: UInt32)Added Int32.getMirror() -> MirrorTypeAdded Int32.init(integerLiteral: Int32)Added Int32.init(truncatingBitPattern: Int)Added Int32.init(truncatingBitPattern: Int64)Added Int32.init(truncatingBitPattern: UInt)Added Int32.init(truncatingBitPattern: UInt64)Added Int32.valueAdded Int64.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int64.init(bitPattern: UInt64)Added Int64.getMirror() -> MirrorTypeAdded Int64.init(integerLiteral: Int64)Added Int64.valueAdded Int8.init(_builtinIntegerLiteral: Builtin.Int2048)Added Int8.init(bitPattern: UInt8)Added Int8.getMirror() -> MirrorTypeAdded Int8.init(integerLiteral: Int8)Added Int8.init(truncatingBitPattern: Int)Added Int8.init(truncatingBitPattern: Int16)Added Int8.init(truncatingBitPattern: Int32)Added Int8.init(truncatingBitPattern: Int64)Added Int8.init(truncatingBitPattern: UInt)Added Int8.init(truncatingBitPattern: UInt16)Added Int8.init(truncatingBitPattern: UInt32)Added Int8.init(truncatingBitPattern: UInt64)Added Int8.valueAdded IntegerArithmeticTypeAdded IntegerArithmeticType.%(Self, _: Self) -> Self [class]Added IntegerArithmeticType.\*(Self, _: Self) -> Self [class]Added IntegerArithmeticType.+(Self, _: Self) -> Self [class]Added IntegerArithmeticType.-(Self, _: Self) -> Self [class]Added IntegerArithmeticType.\ [class]Added IntegerArithmeticType.toIntMax() -> IntMaxAdded IntegerLiteralConvertible.init(integerLiteral: IntegerLiteralType)Added IntegerTypeAdded IntervalTypeAdded IntervalType.clamp(Self) -> SelfAdded IntervalType.contains(Bound) -> BoolAdded IntervalType.endAdded IntervalType.isEmptyAdded IntervalType.startAdded LazyBidirectionalCollection.filter((S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Added LazyBidirectionalCollection.firstAdded LazyBidirectionalCollection.generate() -> S.GeneratorAdded LazyBidirectionalCollection.isEmptyAdded LazyBidirectionalCollection.lastAdded LazyBidirectionalCollection.map((S.Generator.Element) -> U) -> LazyBidirectionalCollection<MapCollectionView<S, U>>Added LazyForwardCollection.filter((S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Added LazyForwardCollection.firstAdded LazyForwardCollection.generate() -> S.GeneratorAdded LazyForwardCollection.isEmptyAdded LazyForwardCollection.map((S.Generator.Element) -> U) -> LazyForwardCollection<MapCollectionView<S, U>>Added LazyRandomAccessCollection.filter((S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Added LazyRandomAccessCollection.firstAdded LazyRandomAccessCollection.generate() -> S.GeneratorAdded LazyRandomAccessCollection.isEmptyAdded LazyRandomAccessCollection.lastAdded LazyRandomAccessCollection.map((S.Generator.Element) -> U) -> LazyRandomAccessCollection<MapCollectionView<S, U>>Added LazySequence.filter((S.Generator.Element) -> Bool) -> LazySequence<FilterSequenceView<S>>Added LazySequence.generate() -> S.GeneratorAdded LazySequence.map((S.Generator.Element) -> U) -> LazySequence<MapSequenceView<S, U>>Added ManagedBufferAdded ManagedBuffer.deinitAdded ManagedBuffer.create(Int, initialValue:(ManagedProtoBuffer<Value, Element>) -> Value) -> ManagedBuffer<Value, Element> [class]Added ManagedBuffer.valueAdded ManagedBufferPointer [struct]Added ManagedBufferPointer.init(_: ManagedProtoBuffer<Value, Element>)Added ManagedBufferPointer.init(_uncheckedUnsafeBufferObject: AnyObject)Added ManagedBufferPointer.allocatedElementCountAdded ManagedBufferPointer.bufferAdded ManagedBufferPointer.init(bufferClass: AnyClass, minimumCapacity: Int)Added ManagedBufferPointer.init(bufferClass: AnyClass, minimumCapacity: Int, initialValue:(buffer: AnyObject, allocatedCount:(AnyObject) -> Int) -> Value)Added ManagedBufferPointer.holdsUniqueOrPinnedReference() -> BoolAdded ManagedBufferPointer.holdsUniqueReference() -> BoolAdded ManagedBufferPointer.init(unsafeBufferObject: AnyObject)Added ManagedBufferPointer.valueAdded ManagedBufferPointer.withUnsafeMutablePointerToElements((UnsafeMutablePointer<Element>) -> R) -> RAdded ManagedBufferPointer.withUnsafeMutablePointerToValue((UnsafeMutablePointer<Value>) -> R) -> RAdded ManagedBufferPointer.withUnsafeMutablePointers((UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> RAdded ManagedProtoBufferAdded ManagedProtoBuffer.allocatedElementCountAdded ManagedProtoBuffer.withUnsafeMutablePointerToElements((UnsafeMutablePointer<Element>) -> R) -> RAdded ManagedProtoBuffer.withUnsafeMutablePointerToValue((UnsafeMutablePointer<Value>) -> R) -> RAdded ManagedProtoBuffer.withUnsafeMutablePointers((UnsafeMutablePointer<Value>, UnsafeMutablePointer<Element>) -> R) -> RAdded MapCollectionView.generate() -> MapSequenceGenerator<Base.Generator, T>Added MapSequenceView.generate() -> MapSequenceGenerator<Base.Generator, T>Added MirrorTypeAdded MirrorType.countAdded MirrorType.dispositionAdded MirrorType.objectIdentifierAdded MirrorType.quickLookObjectAdded MirrorType.summaryAdded MirrorType.valueAdded MirrorType.valueTypeAdded MutableCollectionTypeAdded NilLiteralConvertible.init(nilLiteral: ())Added NonObjectiveCBaseAdded ObjectIdentifier.init(_: Any.Type)Added ObjectIdentifier.uintValueAdded ObjectIdentifier.valueAdded Optional.flatMap((T) -> U?) -> U?Added Optional.getMirror() -> MirrorTypeAdded Optional.init(nilLiteral: ())Added OutputStreamTypeAdded OutputStreamType.write(String)Added Process [enum]Added Process.argcAdded Process.argumentsAdded Process.unsafeArgvAdded QuickLookObject.DoubleAdded RandomAccessIndexTypeAdded Range.init(_: Range<T>)Added Range.debugDescriptionAdded Range.descriptionAdded Range.getMirror() -> MirrorTypeAdded RangeReplaceableCollectionTypeAdded RangeReplaceableCollectionType.insert(Self.Generator.Element, atIndex: Self.Index)Added RangeReplaceableCollectionType.removeAll(Bool)Added RangeReplaceableCollectionType.removeAtIndex(Self.Index) -> Self.Generator.ElementAdded RangeReplaceableCollectionType.removeRange(Range<Self.Index>)Added RangeReplaceableCollectionType.replaceRange(Range<Self.Index>, with: C)Added RangeReplaceableCollectionType.splice(S, atIndex: Self.Index)Added RawOptionSetTypeAdded RawRepresentable.rawValueAdded RawRepresentable.init(rawValue: RawValue)Added Reflectable.getMirror() -> MirrorTypeAdded ReverseRandomAccessIndex.advancedBy(I.Distance) -> ReverseRandomAccessIndex<I>Added ReverseRandomAccessIndex.distanceTo(ReverseRandomAccessIndex<I>) -> I.DistanceAdded SequenceTypeAdded SequenceType.generate() -> GeneratorAdded Set [struct]Added Set.init()Added Set.init(_: S)Added Set.init(arrayLiteral: T)Added Set.contains(T) -> BoolAdded Set.countAdded Set.debugDescriptionAdded Set.descriptionAdded Set.endIndexAdded Set.exclusiveOr(S) -> Set<T>Added Set.exclusiveOrInPlace(S)Added Set.firstAdded Set.generate() -> SetGenerator<T>Added Set.getMirror() -> MirrorTypeAdded Set.hashValueAdded Set.indexOf(T) -> SetIndex<T>?Added Set.insert(T)Added Set.intersect(S) -> Set<T>Added Set.intersectInPlace(S)Added Set.isDisjointWith(S) -> BoolAdded Set.isEmptyAdded Set.isStrictSubsetOf(S) -> BoolAdded Set.isStrictSupersetOf(S) -> BoolAdded Set.isSubsetOf(S) -> BoolAdded Set.isSupersetOf(S) -> BoolAdded Set.makeDescription(Bool) -> StringAdded Set.init(minimumCapacity: Int)Added Set.remove(T) -> T?Added Set.removeAll(Bool)Added Set.removeAtIndex(SetIndex<T>)Added Set.removeFirst() -> TAdded Set.startIndexAdded Set.subtract(S) -> Set<T>Added Set.subtractInPlace(S)Added Set.union(S) -> Set<T>Added Set.unionInPlace(S)Added SetGenerator [struct]Added SetGenerator.next() -> T?Added SetGeneratorRepresentation [enum]Added SetIndex [struct]Added SetIndex.successor() -> SetIndex<T>Added SetIndexRepresentation [enum]Added SetMirrorAdded SetMirror.init(_: Set<T>)Added SetMirror.countAdded SetMirror.dispositionAdded SetMirror.objectIdentifierAdded SetMirror.quickLookObjectAdded SetMirror.summaryAdded SetMirror.valueAdded SetMirror.valueTypeAdded SetMirrorPosition [struct]Added SetMirrorPosition.SetPosAdded SetMirrorPosition.init(_: Set<T>)Added SetMirrorPosition.successor()Added SignedIntegerTypeAdded SignedNumberTypeAdded SignedNumberType.-(Self) -> Self [class]Added SinkTypeAdded SinkType.put(Element)Added StaticString.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added StaticString.init(_builtinStringLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added StaticString.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added StaticString.byteSizeAdded StaticString.debugDescriptionAdded StaticString.descriptionAdded StaticString.init(extendedGraphemeClusterLiteral: StaticString)Added StaticString.hasPointerRepresentationAdded StaticString.isASCIIAdded StaticString.init(start: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added StaticString.init(stringLiteral: StaticString)Added StaticString.stringValueAdded StaticString.unicodeScalarAdded StaticString.init(unicodeScalar: Builtin.Int32)Added StaticString.init(unicodeScalarLiteral: StaticString)Added StaticString.utf8StartAdded StaticString.withUTF8Buffer((UnsafeBufferPointer<UInt8>) -> R) -> RAdded StrideThrough.getMirror() -> MirrorTypeAdded StrideTo.getMirror() -> MirrorTypeAdded String.init(_: S)Added String.init(_: String.UTF16View)Added String.init(_: String.UTF8View)Added String.init(_: T)Added String.init(_: T, radix: Int, uppercase: Bool)Added String.init(_builtinExtendedGraphemeClusterLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added String.init(_builtinStringLiteral: Builtin.RawPointer, byteSize: Builtin.Word, isASCII: Builtin.Int1)Added String.init(_builtinUTF16StringLiteral: Builtin.RawPointer, numberOfCodeUnits: Builtin.Word)Added String.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added String.append(Character)Added String.append(UnicodeScalar)Added String.extend(String)Added String.init(extendedGraphemeClusterLiteral: String)Added String.fromCString(UnsafePointer<CChar>) -> String? [static]Added String.fromCStringRepairingIllFormedUTF8(UnsafePointer<CChar>) -> (String?, hadError: Bool) [static]Added String.getMirror() -> MirrorTypeAdded String.insert(Character, atIndex: String.Index)Added String.lowercaseStringAdded String.removeAll(Bool)Added String.removeAtIndex(String.Index) -> CharacterAdded String.removeRange(Range<String.Index>)Added String.replaceRange(Range<String.Index>, with: C)Added String.splice(S, atIndex: String.Index)Added String.init(stringInterpolation: String)Added String.init(stringInterpolationSegment: Bool)Added String.init(stringInterpolationSegment: Character)Added String.init(stringInterpolationSegment: Float32)Added String.init(stringInterpolationSegment: Float64)Added String.init(stringInterpolationSegment: Int)Added String.init(stringInterpolationSegment: Int16)Added String.init(stringInterpolationSegment: Int32)Added String.init(stringInterpolationSegment: Int64)Added String.init(stringInterpolationSegment: Int8)Added String.init(stringInterpolationSegment: String)Added String.init(stringInterpolationSegment: T)Added String.init(stringInterpolationSegment: UInt)Added String.init(stringInterpolationSegment: UInt16)Added String.init(stringInterpolationSegment: UInt32)Added String.init(stringInterpolationSegment: UInt64)Added String.init(stringInterpolationSegment: UInt8)Added String.init(stringInterpolationSegment: UnicodeScalar)Added String.init(stringLiteral: String)Added String.init(unicodeScalarLiteral: String)Added String.uppercaseStringAdded String.Index.getMirror() -> MirrorTypeAdded String.UTF16View.debugDescriptionAdded String.UTF16View.descriptionAdded String.UTF16View.getMirror() -> MirrorTypeAdded String.UTF16View.Index [struct]Added String.UTF8View.debugDescriptionAdded String.UTF8View.descriptionAdded String.UTF8View.getMirror() -> MirrorTypeAdded String.UnicodeScalarView.debugDescriptionAdded String.UnicodeScalarView.descriptionAdded String.UnicodeScalarView.generate() -> String.UnicodeScalarView.GeneratorAdded String.UnicodeScalarView.getMirror() -> MirrorTypeAdded String.UnicodeScalarView.Generator [struct]Added String.UnicodeScalarView.Generator.next() -> UnicodeScalar?Added String.UnicodeScalarView.Index [struct]Added String.UnicodeScalarView.Index.predecessor() -> String.UnicodeScalarView.IndexAdded String.UnicodeScalarView.Index.successor() -> String.UnicodeScalarView.IndexAdded StringInterpolationConvertible.init(stringInterpolation: Self)Added StringInterpolationConvertible.init(stringInterpolationSegment: T)Added StringLiteralConvertible.init(stringLiteral: StringLiteralType)Added UInt.init(_: Builtin.Word)Added UInt.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt.init(bitPattern: Int)Added UInt.getMirror() -> MirrorTypeAdded UInt.init(integerLiteral: UInt)Added UInt.init(truncatingBitPattern: Int64)Added UInt.init(truncatingBitPattern: UInt64)Added UInt.valueAdded UInt16.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt16.init(bitPattern: Int16)Added UInt16.getMirror() -> MirrorTypeAdded UInt16.init(integerLiteral: UInt16)Added UInt16.init(truncatingBitPattern: Int)Added UInt16.init(truncatingBitPattern: Int32)Added UInt16.init(truncatingBitPattern: Int64)Added UInt16.init(truncatingBitPattern: UInt)Added UInt16.init(truncatingBitPattern: UInt32)Added UInt16.init(truncatingBitPattern: UInt64)Added UInt16.valueAdded UInt32.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt32.init(bitPattern: Int32)Added UInt32.getMirror() -> MirrorTypeAdded UInt32.init(integerLiteral: UInt32)Added UInt32.init(truncatingBitPattern: Int)Added UInt32.init(truncatingBitPattern: Int64)Added UInt32.init(truncatingBitPattern: UInt)Added UInt32.init(truncatingBitPattern: UInt64)Added UInt32.valueAdded UInt64.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt64.init(bitPattern: Int64)Added UInt64.getMirror() -> MirrorTypeAdded UInt64.init(integerLiteral: UInt64)Added UInt64.valueAdded UInt8.init(_builtinIntegerLiteral: Builtin.Int2048)Added UInt8.init(ascii: UnicodeScalar)Added UInt8.init(bitPattern: Int8)Added UInt8.getMirror() -> MirrorTypeAdded UInt8.init(integerLiteral: UInt8)Added UInt8.init(truncatingBitPattern: Int)Added UInt8.init(truncatingBitPattern: Int16)Added UInt8.init(truncatingBitPattern: Int32)Added UInt8.init(truncatingBitPattern: Int64)Added UInt8.init(truncatingBitPattern: UInt)Added UInt8.init(truncatingBitPattern: UInt16)Added UInt8.init(truncatingBitPattern: UInt32)Added UInt8.init(truncatingBitPattern: UInt64)Added UInt8.valueAdded UTF16.isLeadSurrogate(CodeUnit) -> Bool [static]Added UTF16.isTrailSurrogate(CodeUnit) -> Bool [static]Added UTF16View.endIndexAdded UTF16View.generate() -> IndexingGenerator<UnicodeScalar.UTF16View>Added UTF16View.startIndexAdded UTF8.isContinuation(CodeUnit) -> Bool [static]Added UnicodeCodecTypeAdded UnicodeCodecType.init()Added UnicodeCodecType.decode(G) -> UnicodeDecodingResultAdded UnicodeCodecType.encode(UnicodeScalar, output: S) [class]Added UnicodeScalar.init(_: Builtin.Int32)Added UnicodeScalar.init(_: UInt16)Added UnicodeScalar.init(_: UInt8)Added UnicodeScalar.init(_builtinUnicodeScalarLiteral: Builtin.Int32)Added UnicodeScalar.getMirror() -> MirrorTypeAdded UnicodeScalar.init(unicodeScalarLiteral: UnicodeScalar)Added UnicodeScalar.utf16Added UnicodeScalar.UTF16View [struct]Added UnicodeScalar.UTF16View.valueAdded UnicodeScalarIndex.init(_: String.Index, within: String.UnicodeScalarView)Added UnicodeScalarIndex.init(_: UTF16Index, within: String.UnicodeScalarView)Added UnicodeScalarIndex.init(_: UTF8Index, within: String.UnicodeScalarView)Added UnicodeScalarIndex.samePositionIn(String) -> String.Index?Added UnicodeScalarIndex.samePositionIn(String.UTF16View) -> String.UTF16View.IndexAdded UnicodeScalarIndex.samePositionIn(String.UTF8View) -> String.UTF8View.IndexAdded UnicodeScalarLiteralConvertibleAdded UnicodeScalarLiteralConvertible.init(unicodeScalarLiteral: UnicodeScalarLiteralType)Added UnicodeScalarView.init()Added UnicodeScalarView.append(UnicodeScalar)Added UnicodeScalarView.extend(S)Added UnicodeScalarView.insert(UnicodeScalar, atIndex: String.UnicodeScalarView.Index)Added UnicodeScalarView.removeAll(Bool)Added UnicodeScalarView.removeAtIndex(String.UnicodeScalarView.Index) -> UnicodeScalarAdded UnicodeScalarView.removeRange(Range<String.UnicodeScalarView.Index>)Added UnicodeScalarView.replaceRange(Range<String.UnicodeScalarView.Index>, with: C)Added UnicodeScalarView.reserveCapacity(Int)Added UnicodeScalarView.splice(S, atIndex: String.UnicodeScalarView.Index)Added UnsafeBufferPointer [struct]Added UnsafeBufferPointer.baseAddressAdded UnsafeBufferPointer.countAdded UnsafeBufferPointer.debugDescriptionAdded UnsafeBufferPointer.endIndexAdded UnsafeBufferPointer.generate() -> UnsafeBufferPointerGenerator<T>Added UnsafeBufferPointer.init(start: UnsafePointer<T>, count: Int)Added UnsafeBufferPointer.startIndexAdded UnsafeBufferPointerGenerator [struct]Added UnsafeBufferPointerGenerator.endAdded UnsafeBufferPointerGenerator.generate() -> UnsafeBufferPointerGenerator<T>Added UnsafeBufferPointerGenerator.next() -> T?Added UnsafeBufferPointerGenerator.positionAdded UnsafeMutableBufferPointer [struct]Added UnsafeMutableBufferPointer.baseAddressAdded UnsafeMutableBufferPointer.countAdded UnsafeMutableBufferPointer.debugDescriptionAdded UnsafeMutableBufferPointer.endIndexAdded UnsafeMutableBufferPointer.generate() -> UnsafeBufferPointerGenerator<T>Added UnsafeMutableBufferPointer.init(start: UnsafeMutablePointer<T>, count: Int)Added UnsafeMutableBufferPointer.startIndexAdded UnsafeMutablePointer [struct]Added UnsafeMutablePointer.init()Added UnsafeMutablePointer.init(_: COpaquePointer)Added UnsafeMutablePointer.init(_: UnsafeMutablePointer<U>)Added UnsafeMutablePointer.init(_: UnsafePointer<U>)Added UnsafeMutablePointer.advancedBy(Int) -> UnsafeMutablePointer<T>Added UnsafeMutablePointer.alloc(Int) -> UnsafeMutablePointer<T> [static]Added UnsafeMutablePointer.assignBackwardFrom(UnsafeMutablePointer<T>, count: Int)Added UnsafeMutablePointer.assignFrom(UnsafeMutablePointer<T>, count: Int)Added UnsafeMutablePointer.init(bitPattern: UWord)Added UnsafeMutablePointer.init(bitPattern: Word)Added UnsafeMutablePointer.dealloc(Int)Added UnsafeMutablePointer.debugDescriptionAdded UnsafeMutablePointer.destroy()Added UnsafeMutablePointer.destroy(Int)Added UnsafeMutablePointer.distanceTo(UnsafeMutablePointer<T>) -> IntAdded UnsafeMutablePointer.encode() -> [Word]Added UnsafeMutablePointer.getMirror() -> MirrorTypeAdded UnsafeMutablePointer.hashValueAdded UnsafeMutablePointer.initialize(T)Added UnsafeMutablePointer.initializeFrom(C)Added UnsafeMutablePointer.initializeFrom(UnsafeMutablePointer<T>, count: Int)Added UnsafeMutablePointer.memoryAdded UnsafeMutablePointer.move() -> TAdded UnsafeMutablePointer.moveAssignFrom(UnsafeMutablePointer<T>, count: Int)Added UnsafeMutablePointer.moveInitializeBackwardFrom(UnsafeMutablePointer<T>, count: Int)Added UnsafeMutablePointer.moveInitializeFrom(UnsafeMutablePointer<T>, count: Int)Added UnsafeMutablePointer.init(nilLiteral: ())Added UnsafeMutablePointer.predecessor() -> UnsafeMutablePointer<T>Added UnsafeMutablePointer.put(T)Added UnsafeMutablePointer.successor() -> UnsafeMutablePointer<T>Added UnsafePointer.init(_: UnsafeMutablePointer<U>)Added UnsafePointer.advancedBy(Int) -> UnsafePointer<T>Added UnsafePointer.init(bitPattern: UWord)Added UnsafePointer.init(bitPattern: Word)Added UnsafePointer.debugDescriptionAdded UnsafePointer.distanceTo(UnsafePointer<T>) -> IntAdded UnsafePointer.encode() -> [Word]Added UnsafePointer.getMirror() -> MirrorTypeAdded UnsafePointer.init(nilLiteral: ())Added UnsignedIntegerTypeAdded VaListBuilder.append(CVarArgType)Added Zip2.generate() -> GeneratorAdded Array.SubSliceAdded ArraySlice.ElementAdded ArraySlice.SubSliceAdded BidirectionalReverseView.GeneratorAdded BidirectionalReverseView.IndexAdded Character.UTF16ViewAdded ClosedInterval.BoundAdded CollectionOfOne.IndexAdded ContiguousArray.SubSliceAdded DictionaryMirror.MirroredTypeAdded DictionaryMirrorPosition.MirroredTypeAdded EmptyCollection.IndexAdded EnumerateGenerator.GeneratorAdded FilterCollectionView.IndexAdded GeneratorType.ElementAdded HalfOpenInterval.BoundAdded Index.DistanceAdded Int.DistanceAdded Int16.DistanceAdded Int32.DistanceAdded Int64.DistanceAdded Int8.DistanceAdded IntervalType.BoundAdded PermutationGenerator.GeneratorAdded RandomAccessReverseView.GeneratorAdded RandomAccessReverseView.IndexAdded Range.ArraySliceAdded Range.GeneratorAdded Range.IndexAdded RangeGenerator.GeneratorAdded RawRepresentable.RawValueAdded Repeat.IndexAdded ReverseBidirectionalIndex.DistanceAdded ReverseRandomAccessIndex.DistanceAdded SequenceType.GeneratorAdded Set.ElementAdded Set.GeneratorTypeAdded Set.IndexAdded SetIndex.IndexAdded SetIndex.KeyAdded SetIndex.ValueAdded SetMirror.MirroredTypeAdded SetMirrorPosition.MirroredTypeAdded SinkType.ElementAdded Sliceable.SubSliceAdded String.UTF16IndexAdded String.UTF16View.GeneratorAdded String.UTF8IndexAdded String.UTF8View.Index.BufferAdded String.UnicodeScalarIndexAdded UInt.DistanceAdded UInt16.DistanceAdded UInt32.DistanceAdded UInt64.DistanceAdded UInt8.DistanceAdded UnicodeCodecType.CodeUnitAdded UnicodeScalarLiteralConvertible.UnicodeScalarLiteralTypeAdded UnicodeScalarTypeAdded Zip2.GeneratorAdded advance(T, T.Distance) -> TAdded advance(T, T.Distance, T) -> TAdded assert(() -> Bool,() -> String, StaticString, UWord)Added assertionFailure(() -> String, StaticString, UWord)Added contains(S,(S.Generator.Element) -> L) -> BoolAdded contains(S, S.Generator.Element) -> BoolAdded count(T) -> T.Index.DistanceAdded distance(T, T) -> T.DistanceAdded dropFirst(Seq) -> Seq.SubSliceAdded dropLast(S) -> S.SubSliceAdded dump(T, TargetStream, String?, Int, Int, Int) -> TAdded enumerate(Seq) -> EnumerateSequence<Seq>Added equal(S1, S2,(S1.Generator.Element, S1.Generator.Element) -> Bool) -> BoolAdded extend(C, S)Added fatalError(() -> String, StaticString, UWord)Added filter(S,(S.Generator.Element) -> Bool) -> [S.Generator.Element]Added find(C, C.Generator.Element) -> C.Index?Added first(C) -> C.Generator.Element?Added flatMap(C,(C.Generator.Element) -> [T]) -> [T]Added flatMap(S,(S.Generator.Element) -> [T]) -> [T]Added flatMap(T?,(T) -> U?) -> U?Added getVaList([CVarArgType]) -> CVaListPointerAdded indices(C) -> Range<C.Index>Added insert(C, C.Generator.Element, C.Index)Added isEmpty(C) -> BoolAdded isUniquelyReferenced(T) -> BoolAdded isUniquelyReferencedNonObjC(T) -> BoolAdded isUniquelyReferencedNonObjC(T?) -> BoolAdded isUniquelyReferencedOrPinnedNonObjC(T) -> BoolAdded kCFStringEncodingASCIIAdded last(C) -> C.Generator.Element?Added lexicographicalCompare(S1, S2,(S1.Generator.Element, S1.Generator.Element) -> Bool) -> BoolAdded map(C,(C.Generator.Element) -> T) -> [T]Added map(S,(S.Generator.Element) -> T) -> [T]Added maxElement(R) -> R.Generator.ElementAdded minElement(R) -> R.Generator.ElementAdded overlaps(I0, I1) -> BoolAdded partition(C, Range<C.Index>) -> C.IndexAdded partition(C, Range<C.Index>,(C.Generator.Element, C.Generator.Element) -> Bool) -> C.IndexAdded precondition(() -> Bool,() -> String, StaticString, UWord)Added preconditionFailure(() -> String, StaticString, UWord)Added prefix(S, Int) -> S.SubSliceAdded reduce(S, U,(U, S.Generator.Element) -> U) -> UAdded reflect(T) -> MirrorTypeAdded removeAll(C, Bool)Added removeAtIndex(C, C.Index) -> C.Generator.ElementAdded removeLast(C) -> C.Generator.ElementAdded removeRange(C, Range<C.Index>)Added reverse(C) -> [C.Generator.Element]Added sort(C,(C.Generator.Element, C.Generator.Element) -> Bool)Added sort(ContiguousArray<T>)Added sort(ContiguousArray<T>,(T, T) -> Bool)Added sorted(C) -> [C.Generator.Element]Added sorted(C,(C.Generator.Element, C.Generator.Element) -> Bool) -> [C.Generator.Element]Added splice(C, S, C.Index)Added split(S, Int, Bool,(S.Generator.Element) -> R) -> [S.SubSlice]Added startsWith(S0, S1,(S0.Generator.Element, S0.Generator.Element) -> Bool) -> BoolAdded suffix(S, Int) -> S.SubSliceAdded toDebugString(T) -> StringAdded transcode(InputEncoding.Type, OutputEncoding.Type, Input, Output, Bool) -> BoolAdded unsafeAddressOf(AnyObject) -> UnsafePointer<Void>Added unsafeBitCast(T, U.Type) -> UAdded unsafeDowncast(AnyObject) -> TAdded unsafeReflect(Builtin.NativeObject, UnsafeMutablePointer<T>) -> MirrorTypeAdded unsafeUnwrap(T?) -> TAdded withUnsafeMutablePointer(T, UnsafeMutablePointer<T> -> Result) -> ResultAdded withUnsafeMutablePointers(A0, A1,(UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>) -> Result) -> ResultAdded withUnsafeMutablePointers(A0, A1, A2,(UnsafeMutablePointer<A0>, UnsafeMutablePointer<A1>, UnsafeMutablePointer<A2>) -> Result) -> ResultAdded withVaList([CVarArgType], CVaListPointer -> R) -> RAdded zip(S0, S1) -> Zip2<S0, S1>Modified AbsoluteValuable

|  | Protocols |
| --- | --- |
| From | SignedNumber |
| To | SignedNumberType |

Modified Array [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Array<T> : MutableCollection, Sliceable {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<[T]>     typealias SliceType = Slice<T>     subscript (subRange: Range<Int>) -> Slice<T> } ``` | ArrayLiteralConvertible, ArrayType, DebugPrintable, MutableCollection, Printable, Reflectable, Sliceable |
| To | ``` struct Array<T> : MutableCollectionType, Sliceable, _DestructorSafeContainer {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<[T]>     typealias SubSlice = ArraySlice<T>     subscript (subRange: Range<Int>) -> ArraySlice<T>     init(_ buffer: _ArrayBuffer<T>) } ``` | ArrayLiteralConvertible, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable |

Modified Array.init(_: S)

|  | Declaration |
| --- | --- |
| From | ``` init<S : Sequence where T == T>(_ s: S) ``` |
| To | ``` init<S : SequenceType where T == T>(_ s: S) ``` |

Modified Array.append(T)

|  | Declaration |
| --- | --- |
| From | ``` func append(_ newElement: T) ``` |
| To | ``` mutating func append(_ newElement: T) ``` |

Modified Array.extend(S)

|  | Declaration |
| --- | --- |
| From | ``` func extend<S : Sequence where T == T>(_ sequence: S) ``` |
| To | ``` mutating func extend<S : SequenceType where T == T>(_ newElements: S) ``` |

Modified Array.insert(T, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insert(_ newElement: T, atIndex atIndex: Int) ``` |
| To | ``` mutating func insert(_ newElement: T, atIndex i: Int) ``` |

Modified Array.join(S) -> [T]

|  | Declaration |
| --- | --- |
| From | ``` func join<S : Sequence where [T] == [T]>(_ elements: S) -> [T] ``` |
| To | ``` func join<S : SequenceType where [T] == [T]>(_ elements: S) -> [T] ``` |

Modified Array.reduce(U, combine:(U, T) -> U) -> U

|  | Declaration |
| --- | --- |
| From | ``` func reduce<U>(_ initial: U, combine combine: (U, T) -> U) -> U ``` |
| To | ``` func reduce<U>(_ initial: U, combine combine: @noescape (U, T) -> U) -> U ``` |

Modified Array.removeAll(Bool)

|  | Declaration |
| --- | --- |
| From | ``` func removeAll(keepCapacity keepCapacity: Bool = default) ``` |
| To | ``` mutating func removeAll(keepCapacity keepCapacity: Bool = default) ``` |

Modified Array.removeAtIndex(Int) -> T

|  | Declaration |
| --- | --- |
| From | ``` func removeAtIndex(_ index: Int) -> T ``` |
| To | ``` mutating func removeAtIndex(_ index: Int) -> T ``` |

Modified Array.removeLast() -> T

|  | Declaration |
| --- | --- |
| From | ``` func removeLast() -> T ``` |
| To | ``` mutating func removeLast() -> T ``` |

Modified Array.replaceRange(Range<Int>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` func replaceRange<C : Collection where T == T>(_ subRange: Range<Int>, with newValues: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C) ``` |

Modified Array.reserveCapacity(Int)

|  | Declaration |
| --- | --- |
| From | ``` func reserveCapacity(_ minimumCapacity: Int) ``` |
| To | ``` mutating func reserveCapacity(_ minimumCapacity: Int) ``` |

Modified Array.sort((T, T) -> Bool)

|  | Declaration |
| --- | --- |
| From | ``` func sort(_ isOrderedBefore: (T, T) -> Bool) ``` |
| To | ``` mutating func sort(_ isOrderedBefore: (T, T) -> Bool) ``` |

Modified BidirectionalReverseView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct BidirectionalReverseView<T : Collection where T.IndexType : BidirectionalIndex> : Collection {     typealias IndexType = ReverseBidirectionalIndex<T.IndexType>     typealias GeneratorType = IndexingGenerator<BidirectionalReverseView<T>>     func generate() -> IndexingGenerator<BidirectionalReverseView<T>>     var startIndex: IndexType { get }     var endIndex: IndexType { get }     subscript (i: IndexType) -> T.GeneratorType.Element { get } } ``` | Collection |
| To | ``` struct BidirectionalReverseView<T : CollectionType where T.Index : BidirectionalIndexType> : CollectionType {     typealias Index = ReverseBidirectionalIndex<T.Index>     typealias Generator = IndexingGenerator<BidirectionalReverseView<T>>     func generate() -> IndexingGenerator<BidirectionalReverseView<T>>     var startIndex: Index { get }     var endIndex: Index { get }     subscript (position: Index) -> T.Generator.Element { get } } ``` | CollectionType |

Modified BidirectionalReverseView.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: IndexType { get } ``` |
| To | ``` var endIndex: Index { get } ``` |

Modified BidirectionalReverseView.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: IndexType { get } ``` |
| To | ``` var startIndex: Index { get } ``` |

Modified Bit [enum]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum Bit : Int, RandomAccessIndex, Reflectable {     case zero     case one     func successor() -> Bit     func predecessor() -> Bit     func distanceTo(_ other: Bit) -> Int     func advancedBy(_ distance: Int) -> Bit     func getMirror() -> Mirror } ``` | Equatable, Hashable, IntegerArithmetic, RandomAccessIndex, RawRepresentable, Reflectable |
| To | ``` enum Bit : Int, RandomAccessIndexType, Reflectable {     case Zero     case One     func successor() -> Bit     func predecessor() -> Bit     func distanceTo(_ other: Bit) -> Int     func advancedBy(_ distance: Int) -> Bit     func getMirror() -> MirrorType } ``` | Equatable, Hashable, IntegerArithmeticType, RandomAccessIndexType, RawRepresentable, Reflectable |

Modified Bool [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Bool {     init() } ``` | BooleanLiteralConvertible, Equatable, Hashable, LogicValue, Printable, Reflectable |
| To | ``` struct Bool {     var value: Builtin.Int1     init()     init(_ v: Builtin.Int1) } ``` | BooleanLiteralConvertible, BooleanType, Equatable, Hashable, Printable, Reflectable |

Modified CFunctionPointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CFunctionPointer<T> : Equatable, Hashable, LogicValue, NilLiteralConvertible {     var value: COpaquePointer     init()     init(_ value: COpaquePointer)     static func null() -> CFunctionPointer<T>     func getLogicValue() -> Bool     var hashValue: Int { get }     static func convertFromNilLiteral() -> CFunctionPointer<T> } ``` | Equatable, Hashable, LogicValue, NilLiteralConvertible |
| To | ``` struct CFunctionPointer<T> : Equatable, Hashable, NilLiteralConvertible {     var value: COpaquePointer     init()     init(_ value: COpaquePointer)     static func null() -> CFunctionPointer<T>     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } ``` | CVarArgType, DebugPrintable, Equatable, Hashable, NilLiteralConvertible |

Modified COpaquePointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct COpaquePointer : Equatable, Hashable, LogicValue, NilLiteralConvertible {     init()     static func null() -> COpaquePointer     func getLogicValue() -> Bool     var hashValue: Int { get }     static func convertFromNilLiteral() -> COpaquePointer } ``` | CVarArg, Equatable, Hashable, LogicValue, NilLiteralConvertible |
| To | ``` struct COpaquePointer : Equatable, Hashable, NilLiteralConvertible {     init()     init(_ v: Builtin.RawPointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<T>(_ source: UnsafePointer<T>)     init<T>(_ source: UnsafeMutablePointer<T>)     static func null() -> COpaquePointer     var hashValue: Int { get }     init(nilLiteral nilLiteral: ()) } ``` | CVarArgType, DebugPrintable, Equatable, Hashable, NilLiteralConvertible |

Modified COpaquePointer.init(_: CFunctionPointer<T>)

|  | Declaration |
| --- | --- |
| From | ``` init<T>(_ from: CFunctionPointer<T>) ``` |
| To | ``` init<T>(_ value: CFunctionPointer<T>) ``` |

Modified COpaquePointer.init(_: UnsafePointer<T>)

|  | Declaration |
| --- | --- |
| From | ``` init<T>(_ from: UnsafePointer<T>) ``` |
| To | ``` init<T>(_ source: UnsafePointer<T>) ``` |

Modified CVaListPointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CVaListPointer {     var value: UnsafePointer<Void>     init(fromUnsafePointer from: UnsafePointer<Void>) } ``` | -- |
| To | ``` struct CVaListPointer {     var value: UnsafeMutablePointer<Void>     init(_fromUnsafeMutablePointer from: UnsafeMutablePointer<Void>) } ``` | DebugPrintable |

Modified CVaListPointer.value

|  | Declaration |
| --- | --- |
| From | ``` var value: UnsafePointer<Void> ``` |
| To | ``` var value: UnsafeMutablePointer<Void> ``` |

Modified CollectionOfOne [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct CollectionOfOne<T> : Collection {     typealias IndexType = Bit     init(_ element: T)     var startIndex: IndexType { get }     var endIndex: IndexType { get }     func generate() -> GeneratorOfOne<T>     subscript (i: IndexType) -> T { get }     let element: T } ``` | Collection, Reflectable |
| To | ``` struct CollectionOfOne<T> : CollectionType {     typealias Index = Bit     init(_ element: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> GeneratorOfOne<T>     subscript (position: Index) -> T { get }     let element: T } ``` | CollectionType, Reflectable |

Modified CollectionOfOne.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: IndexType { get } ``` |
| To | ``` var endIndex: Index { get } ``` |

Modified CollectionOfOne.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: IndexType { get } ``` |
| To | ``` var startIndex: Index { get } ``` |

Modified ContiguousArray [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ContiguousArray<T> : MutableCollection, Sliceable {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<ContiguousArray<T>>     typealias SliceType = Slice<T>     subscript (subRange: Range<Int>) -> Slice<T> } ``` | ArrayLiteralConvertible, ArrayType, DebugPrintable, MutableCollection, Printable, Reflectable, Sliceable |
| To | ``` struct ContiguousArray<T> : MutableCollectionType, Sliceable, _DestructorSafeContainer {     typealias Element = T     var startIndex: Int { get }     var endIndex: Int { get }     subscript (index: Int) -> T     func generate() -> IndexingGenerator<ContiguousArray<T>>     typealias SubSlice = ArraySlice<T>     subscript (subRange: Range<Int>) -> ArraySlice<T>     init(_ buffer: _ContiguousArrayBuffer<T>) } ``` | ArrayLiteralConvertible, DebugPrintable, MutableCollectionType, Printable, Reflectable, Sliceable |

Modified ContiguousArray.init(_: S)

|  | Declaration |
| --- | --- |
| From | ``` init<S : Sequence where T == T>(_ s: S) ``` |
| To | ``` init<S : SequenceType where T == T>(_ s: S) ``` |

Modified ContiguousArray.append(T)

|  | Declaration |
| --- | --- |
| From | ``` func append(_ newElement: T) ``` |
| To | ``` mutating func append(_ newElement: T) ``` |

Modified ContiguousArray.extend(S)

|  | Declaration |
| --- | --- |
| From | ``` func extend<S : Sequence where T == T>(_ sequence: S) ``` |
| To | ``` mutating func extend<S : SequenceType where T == T>(_ newElements: S) ``` |

Modified ContiguousArray.insert(T, atIndex: Int)

|  | Declaration |
| --- | --- |
| From | ``` func insert(_ newElement: T, atIndex atIndex: Int) ``` |
| To | ``` mutating func insert(_ newElement: T, atIndex i: Int) ``` |

Modified ContiguousArray.join(S) -> ContiguousArray<T>

|  | Declaration |
| --- | --- |
| From | ``` func join<S : Sequence where ContiguousArray<T> == ContiguousArray<T>>(_ elements: S) -> ContiguousArray<T> ``` |
| To | ``` func join<S : SequenceType where ContiguousArray<T> == ContiguousArray<T>>(_ elements: S) -> ContiguousArray<T> ``` |

Modified ContiguousArray.reduce(U, combine:(U, T) -> U) -> U

|  | Declaration |
| --- | --- |
| From | ``` func reduce<U>(_ initial: U, combine combine: (U, T) -> U) -> U ``` |
| To | ``` func reduce<U>(_ initial: U, combine combine: @noescape (U, T) -> U) -> U ``` |

Modified ContiguousArray.removeAll(Bool)

|  | Declaration |
| --- | --- |
| From | ``` func removeAll(keepCapacity keepCapacity: Bool = default) ``` |
| To | ``` mutating func removeAll(keepCapacity keepCapacity: Bool = default) ``` |

Modified ContiguousArray.removeAtIndex(Int) -> T

|  | Declaration |
| --- | --- |
| From | ``` func removeAtIndex(_ index: Int) -> T ``` |
| To | ``` mutating func removeAtIndex(_ index: Int) -> T ``` |

Modified ContiguousArray.removeLast() -> T

|  | Declaration |
| --- | --- |
| From | ``` func removeLast() -> T ``` |
| To | ``` mutating func removeLast() -> T ``` |

Modified ContiguousArray.replaceRange(Range<Int>, with: C)

|  | Declaration |
| --- | --- |
| From | ``` func replaceRange<C : Collection where T == T>(_ subRange: Range<Int>, with newValues: C) ``` |
| To | ``` mutating func replaceRange<C : CollectionType where T == T>(_ subRange: Range<Int>, with newElements: C) ``` |

Modified ContiguousArray.reserveCapacity(Int)

|  | Declaration |
| --- | --- |
| From | ``` func reserveCapacity(_ minimumCapacity: Int) ``` |
| To | ``` mutating func reserveCapacity(_ minimumCapacity: Int) ``` |

Modified ContiguousArray.sort((T, T) -> Bool)

|  | Declaration |
| --- | --- |
| From | ``` func sort(_ isOrderedBefore: (T, T) -> Bool) ``` |
| To | ``` mutating func sort(_ isOrderedBefore: (T, T) -> Bool) ``` |

Modified Dictionary [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Dictionary<KeyType : Hashable, ValueType> : Collection, DictionaryLiteralConvertible {     typealias Element = (KeyType, ValueType)     typealias Index = DictionaryIndex<KeyType, ValueType>     init(minimumCapacity minimumCapacity: Int = default)     var startIndex: DictionaryIndex<KeyType, ValueType> { get }     var endIndex: DictionaryIndex<KeyType, ValueType> { get }     func indexForKey(_ key: KeyType) -> DictionaryIndex<KeyType, ValueType>?     subscript (i: DictionaryIndex<KeyType, ValueType>) -> (KeyType, ValueType) { get }     subscript (key: KeyType) -> ValueType?     func updateValue(_ value: ValueType, forKey key: KeyType) -> ValueType?     func removeAtIndex(_ index: DictionaryIndex<KeyType, ValueType>)     func removeValueForKey(_ key: KeyType) -> ValueType?     func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<KeyType, ValueType>     static func convertFromDictionaryLiteral(_ elements: (KeyType, ValueType)...) -> [KeyType : ValueType]     var isEmpty: Bool { get }     var keys: LazyBidirectionalCollection<MapCollectionView<[KeyType : ValueType], KeyType>> { get }     var values: LazyBidirectionalCollection<MapCollectionView<[KeyType : ValueType], ValueType>> { get } } ``` | Collection, DebugPrintable, DictionaryLiteralConvertible, Printable, Reflectable |
| To | ``` struct Dictionary<Key : Hashable, Value> : CollectionType, DictionaryLiteralConvertible {     typealias Element = (Key, Value)     typealias Index = DictionaryIndex<Key, Value>     init()     init(minimumCapacity minimumCapacity: Int)     var startIndex: DictionaryIndex<Key, Value> { get }     var endIndex: DictionaryIndex<Key, Value> { get }     func indexForKey(_ key: Key) -> DictionaryIndex<Key, Value>?     subscript (position: DictionaryIndex<Key, Value>) -> (Key, Value) { get }     subscript (key: Key) -> Value?     mutating func updateValue(_ value: Value, forKey key: Key) -> Value?     mutating func removeAtIndex(_ index: DictionaryIndex<Key, Value>)     mutating func removeValueForKey(_ key: Key) -> Value?     mutating func removeAll(keepCapacity keepCapacity: Bool = default)     var count: Int { get }     func generate() -> DictionaryGenerator<Key, Value>     init(dictionaryLiteral elements: (Key, Value)...)     var isEmpty: Bool { get }     var keys: LazyForwardCollection<MapCollectionView<[Key : Value], Key>> { get }     var values: LazyForwardCollection<MapCollectionView<[Key : Value], Value>> { get } } ``` | CollectionType, DebugPrintable, DictionaryLiteralConvertible, Printable, Reflectable |

Modified Dictionary.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: DictionaryIndex<KeyType, ValueType> { get } ``` |
| To | ``` var endIndex: DictionaryIndex<Key, Value> { get } ``` |

Modified Dictionary.keys

|  | Declaration |
| --- | --- |
| From | ``` var keys: LazyBidirectionalCollection<MapCollectionView<[KeyType : ValueType], KeyType>> { get } ``` |
| To | ``` var keys: LazyForwardCollection<MapCollectionView<[Key : Value], Key>> { get } ``` |

Modified Dictionary.init(minimumCapacity: Int)

|  | Declaration |
| --- | --- |
| From | ``` init(minimumCapacity minimumCapacity: Int = default) ``` |
| To | ``` init(minimumCapacity minimumCapacity: Int) ``` |

Modified Dictionary.removeAll(Bool)

|  | Declaration |
| --- | --- |
| From | ``` func removeAll(keepCapacity keepCapacity: Bool = default) ``` |
| To | ``` mutating func removeAll(keepCapacity keepCapacity: Bool = default) ``` |

Modified Dictionary.removeValueForKey(Key) -> Value?

|  | Declaration |
| --- | --- |
| From | ``` func removeValueForKey(_ key: KeyType) -> ValueType? ``` |
| To | ``` mutating func removeValueForKey(_ key: Key) -> Value? ``` |

Modified Dictionary.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: DictionaryIndex<KeyType, ValueType> { get } ``` |
| To | ``` var startIndex: DictionaryIndex<Key, Value> { get } ``` |

Modified Dictionary.updateValue(Value, forKey: Key) -> Value?

|  | Declaration |
| --- | --- |
| From | ``` func updateValue(_ value: ValueType, forKey key: KeyType) -> ValueType? ``` |
| To | ``` mutating func updateValue(_ value: Value, forKey key: Key) -> Value? ``` |

Modified Dictionary.values

|  | Declaration |
| --- | --- |
| From | ``` var values: LazyBidirectionalCollection<MapCollectionView<[KeyType : ValueType], ValueType>> { get } ``` |
| To | ``` var values: LazyForwardCollection<MapCollectionView<[Key : Value], Value>> { get } ``` |

Modified DictionaryGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct DictionaryGenerator<KeyType : Hashable, ValueType> : Generator {     func next() -> (KeyType, ValueType)? } ``` | Generator |
| To | ``` struct DictionaryGenerator<Key : Hashable, Value> : GeneratorType {     mutating func next() -> (Key, Value)? } ``` | GeneratorType |

Modified DictionaryGenerator.next() -> (Key, Value)?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> (KeyType, ValueType)? ``` |
| To | ``` mutating func next() -> (Key, Value)? ``` |

Modified DictionaryIndex [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct DictionaryIndex<KeyType : Hashable, ValueType> : BidirectionalIndex {     typealias Index = DictionaryIndex<KeyType, ValueType>     func predecessor() -> DictionaryIndex<KeyType, ValueType>     func successor() -> DictionaryIndex<KeyType, ValueType> } ``` | BidirectionalIndex |
| To | ``` struct DictionaryIndex<Key : Hashable, Value> : ForwardIndexType, Comparable {     typealias Index = DictionaryIndex<Key, Value>     func successor() -> DictionaryIndex<Key, Value> } ``` | Comparable, ForwardIndexType |

Modified DictionaryIndex.successor() -> DictionaryIndex<Key, Value>

|  | Declaration |
| --- | --- |
| From | ``` func successor() -> DictionaryIndex<KeyType, ValueType> ``` |
| To | ``` func successor() -> DictionaryIndex<Key, Value> ``` |

Modified Double [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Double {     init()     init(_ value: Double) } ``` | AbsoluteValuable, CVarArg, Comparable, FloatLiteralConvertible, FloatingPointNumber, Hashable, IntegerLiteralConvertible, Printable, Strideable |
| To | ``` struct Double {     var value: Builtin.FPIEEE64     init()     init(_bits v: Builtin.FPIEEE64)     init(_ value: Double) } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |

Modified Double.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified Double.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified EmptyCollection [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct EmptyCollection<T> : Collection {     typealias IndexType = Int     init()     var startIndex: IndexType { get }     var endIndex: IndexType { get }     func generate() -> EmptyGenerator<T>     subscript (i: IndexType) -> T { get } } ``` | Collection, Reflectable |
| To | ``` struct EmptyCollection<T> : CollectionType {     typealias Index = Int     init()     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> EmptyGenerator<T>     subscript (position: Index) -> T { get } } ``` | CollectionType, Reflectable |

Modified EmptyCollection.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: IndexType { get } ``` |
| To | ``` var endIndex: Index { get } ``` |

Modified EmptyCollection.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: IndexType { get } ``` |
| To | ``` var startIndex: Index { get } ``` |

Modified EmptyGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct EmptyGenerator<T> : Generator, Sequence {     func generate() -> EmptyGenerator<T>     func next() -> T? } ``` | Generator, Sequence |
| To | ``` struct EmptyGenerator<T> : GeneratorType, SequenceType {     init()     func generate() -> EmptyGenerator<T>     mutating func next() -> T? } ``` | GeneratorType, SequenceType |

Modified EmptyGenerator.next() -> T?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> T? ``` |
| To | ``` mutating func next() -> T? ``` |

Modified EnumerateGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct EnumerateGenerator<Base : Generator> : Generator, Sequence {     typealias Element = (index: Int, element: Base.Element)     var base: Base     var count: Int     init(_ base: Base)     func next() -> Element?     typealias GeneratorType = EnumerateGenerator<Base>     func generate() -> EnumerateGenerator<Base> } ``` | Generator, Sequence |
| To | ``` struct EnumerateGenerator<Base : GeneratorType> : GeneratorType, SequenceType {     typealias Element = (index: Int, element: Base.Element)     var base: Base     var count: Int     init(_ base: Base)     mutating func next() -> Element?     typealias Generator = EnumerateGenerator<Base>     func generate() -> EnumerateGenerator<Base> } ``` | GeneratorType, SequenceType |

Modified EnumerateGenerator.next() -> Element?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> Element? ``` |
| To | ``` mutating func next() -> Element? ``` |

Modified ExtendedGraphemeClusterLiteralConvertible

|  | Protocols |
| --- | --- |
| From | -- |
| To | UnicodeScalarLiteralConvertible |

Modified FilterCollectionView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct FilterCollectionView<Base : Collection> : Collection {     typealias IndexType = FilterCollectionViewIndex<Base>     init(_ base: Base, includeElement includeElement: (Base.GeneratorType.Element) -> Bool)     var startIndex: FilterCollectionViewIndex<Base> { get }     var endIndex: FilterCollectionViewIndex<Base> { get }     subscript (index: FilterCollectionViewIndex<Base>) -> Base.GeneratorType.Element { get }     func generate() -> FilterGenerator<Base.GeneratorType> } ``` | Collection |
| To | ``` struct FilterCollectionView<Base : CollectionType> : CollectionType {     typealias Index = FilterCollectionViewIndex<Base>     init(_ base: Base, includeElement predicate: (Base.Generator.Element) -> Bool)     var startIndex: FilterCollectionViewIndex<Base> { get }     var endIndex: FilterCollectionViewIndex<Base> { get }     subscript (position: FilterCollectionViewIndex<Base>) -> Base.Generator.Element { get }     func generate() -> FilterGenerator<Base.Generator> } ``` | CollectionType |

Modified FilterCollectionViewIndex [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct FilterCollectionViewIndex<Base : Collection> : ForwardIndex {     func successor() -> FilterCollectionViewIndex<Base> } ``` | ForwardIndex |
| To | ``` struct FilterCollectionViewIndex<Base : CollectionType> : ForwardIndexType {     func successor() -> FilterCollectionViewIndex<Base> } ``` | ForwardIndexType |

Modified FilterGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct FilterGenerator<Base : Generator> : Generator, Sequence {     func next() -> Base.Element?     func generate() -> FilterGenerator<Base> } ``` | Generator, Sequence |
| To | ``` struct FilterGenerator<Base : GeneratorType> : GeneratorType, SequenceType {     mutating func next() -> Base.Element?     func generate() -> FilterGenerator<Base> } ``` | GeneratorType, SequenceType |

Modified FilterGenerator.next() -> Base.Element?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> Base.Element? ``` |
| To | ``` mutating func next() -> Base.Element? ``` |

Modified FilterSequenceView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct FilterSequenceView<Base : Sequence> : Sequence {     func generate() -> FilterGenerator<Base.GeneratorType> } ``` | Sequence |
| To | ``` struct FilterSequenceView<Base : SequenceType> : SequenceType {     func generate() -> FilterGenerator<Base.Generator> } ``` | SequenceType |

Modified Float [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Float {     init()     init(_ value: Float) } ``` | AbsoluteValuable, CVarArg, Comparable, FloatLiteralConvertible, FloatingPointNumber, Hashable, IntegerLiteralConvertible, Printable, Strideable |
| To | ``` struct Float {     var value: Builtin.FPIEEE32     init()     init(_bits v: Builtin.FPIEEE32)     init(_ value: Float) } ``` | AbsoluteValuable, Comparable, FloatLiteralConvertible, FloatingPointType, Hashable, IntegerLiteralConvertible, Printable, Reflectable, Strideable |

Modified Float.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified Float.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified Float80 [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Float80 {     init()     init(_ value: Float80) } ``` |
| To | ``` struct Float80 {     var value: Builtin.FPIEEE80     init()     init(_bits v: Builtin.FPIEEE80)     init(_ value: Float80) } ``` |

Modified Float80.init(_: Double)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Double) ``` |
| To | ``` init(_ other: Double) ``` |

Modified Float80.init(_: Float)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float) ``` |
| To | ``` init(_ other: Float) ``` |

Modified GeneratorOf [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct GeneratorOf<T> : Generator, Sequence {     init(_ next: () -> T?)     init<G : Generator where T == T>(_ self_: G)     func next() -> T?     func generate() -> GeneratorOf<T> } ``` | Generator, Sequence |
| To | ``` struct GeneratorOf<T> : GeneratorType, SequenceType {     init(_ nextElement: () -> T?)     init<G : GeneratorType where T == T>(_ base: G)     mutating func next() -> T?     func generate() -> GeneratorOf<T> } ``` | GeneratorType, SequenceType |

Modified GeneratorOf.init(_: () -> T?)

|  | Declaration |
| --- | --- |
| From | ``` init(_ next: () -> T?) ``` |
| To | ``` init(_ nextElement: () -> T?) ``` |

Modified GeneratorOf.init(_: G)

|  | Declaration |
| --- | --- |
| From | ``` init<G : Generator where T == T>(_ self_: G) ``` |
| To | ``` init<G : GeneratorType where T == T>(_ base: G) ``` |

Modified GeneratorOf.next() -> T?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> T? ``` |
| To | ``` mutating func next() -> T? ``` |

Modified GeneratorOfOne [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct GeneratorOfOne<T> : Generator, Sequence {     init(_ elements: T?)     func generate() -> GeneratorOfOne<T>     func next() -> T?     var elements: T? } ``` | Generator, Sequence |
| To | ``` struct GeneratorOfOne<T> : GeneratorType, SequenceType {     init(_ element: T?)     func generate() -> GeneratorOfOne<T>     mutating func next() -> T?     var elements: T? } ``` | GeneratorType, SequenceType |

Modified GeneratorOfOne.init(_: T?)

|  | Declaration |
| --- | --- |
| From | ``` init(_ elements: T?) ``` |
| To | ``` init(_ element: T?) ``` |

Modified GeneratorOfOne.next() -> T?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> T? ``` |
| To | ``` mutating func next() -> T? ``` |

Modified GeneratorSequence [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct GeneratorSequence<G : Generator> : Generator, Sequence {     init(_ base: G)     func next() -> G.Element?     func generate() -> GeneratorSequence<G> } ``` | Generator, Sequence |
| To | ``` struct GeneratorSequence<G : GeneratorType> : GeneratorType, SequenceType {     init(_ base: G)     mutating func next() -> G.Element?     func generate() -> GeneratorSequence<G> } ``` | GeneratorType, SequenceType |

Modified GeneratorSequence.next() -> G.Element?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> G.Element? ``` |
| To | ``` mutating func next() -> G.Element? ``` |

Modified ImplicitlyUnwrappedOptional [enum]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum ImplicitlyUnwrappedOptional<T> : LogicValue, Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     init(_ v: T?)     static func convertFromNilLiteral() -> T!     func getLogicValue() -> Bool     func map<U>(_ f: (T) -> U) -> U!     func getMirror() -> Mirror } ``` | LogicValue, NilLiteralConvertible, Printable, Reflectable |
| To | ``` enum ImplicitlyUnwrappedOptional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     init(_ v: T?)     init(nilLiteral nilLiteral: ())     func map<U>(_ f: @noescape (T) -> U) -> U!     func flatMap<U>(_ f: @noescape (T) -> U!) -> U!     func getMirror() -> MirrorType } ``` | NilLiteralConvertible, Printable, Reflectable |

Modified ImplicitlyUnwrappedOptional.map((T) -> U) -> U!

|  | Declaration |
| --- | --- |
| From | ``` func map<U>(_ f: (T) -> U) -> U! ``` |
| To | ``` func map<U>(_ f: @noescape (T) -> U) -> U! ``` |

Modified IndexingGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct IndexingGenerator<C> : Generator, Sequence {     init(_ seq: C)     func generate() -> IndexingGenerator<C>     func next() -> C._Element? } ``` | Generator, Sequence |
| To | ``` struct IndexingGenerator<C : _CollectionType> : GeneratorType, SequenceType {     init(_ seq: C)     func generate() -> IndexingGenerator<C>     mutating func next() -> C._Element? } ``` | GeneratorType, SequenceType |

Modified IndexingGenerator.next() -> C._Element?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> C._Element? ``` |
| To | ``` mutating func next() -> C._Element? ``` |

Modified Int [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int : SignedInteger {     init()     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     static func convertFromIntegerLiteral(_ value: Int) -> Int     typealias ArrayBoundType = Int     func getArrayBoundValue() -> Int     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, SignedInteger, SignedNumber |
| To | ``` struct Int : SignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: Int)     init(bigEndian value: Int)     init(littleEndian value: Int)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int)     var bigEndian: Int { get }     var littleEndian: Int { get }     var byteSwapped: Int { get }     static var max: Int { get }     static var min: Int { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |

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

Modified Int.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified Int.advancedBy(Distance) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int ``` |
| To | ``` func advancedBy(_ amount: Distance) -> Int ``` |

Modified Int.distanceTo(Int) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: Int) -> Int ``` |
| To | ``` func distanceTo(_ other: Int) -> Distance ``` |

Modified Int16 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int16 : SignedInteger {     init()     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     static func convertFromIntegerLiteral(_ value: Int16) -> Int16     typealias ArrayBoundType = Int16     func getArrayBoundValue() -> Int16     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, SignedInteger, SignedNumber |
| To | ``` struct Int16 : SignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: Int16)     init(bigEndian value: Int16)     init(littleEndian value: Int16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int16)     var bigEndian: Int16 { get }     var littleEndian: Int16 { get }     var byteSwapped: Int16 { get }     static var max: Int16 { get }     static var min: Int16 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |

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

Modified Int16.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified Int16.advancedBy(Distance) -> Int16

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int16 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> Int16 ``` |

Modified Int16.distanceTo(Int16) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: Int16) -> Int ``` |
| To | ``` func distanceTo(_ other: Int16) -> Distance ``` |

Modified Int32 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int32 : SignedInteger {     init()     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     static func convertFromIntegerLiteral(_ value: Int32) -> Int32     typealias ArrayBoundType = Int32     func getArrayBoundValue() -> Int32     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, SignedInteger, SignedNumber |
| To | ``` struct Int32 : SignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: Int32)     init(bigEndian value: Int32)     init(littleEndian value: Int32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int32)     var bigEndian: Int32 { get }     var littleEndian: Int32 { get }     var byteSwapped: Int32 { get }     static var max: Int32 { get }     static var min: Int32 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |

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

Modified Int32.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified Int32.advancedBy(Distance) -> Int32

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int32 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> Int32 ``` |

Modified Int32.distanceTo(Int32) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: Int32) -> Int ``` |
| To | ``` func distanceTo(_ other: Int32) -> Distance ``` |

Modified Int64 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int64 : SignedInteger {     init()     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     static func convertFromIntegerLiteral(_ value: Int64) -> Int64     typealias ArrayBoundType = Int64     func getArrayBoundValue() -> Int64     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, SignedInteger, SignedNumber |
| To | ``` struct Int64 : SignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: Int64)     init(bigEndian value: Int64)     init(littleEndian value: Int64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int64)     var bigEndian: Int64 { get }     var littleEndian: Int64 { get }     var byteSwapped: Int64 { get }     static var max: Int64 { get }     static var min: Int64 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |

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

Modified Int64.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified Int64.advancedBy(Distance) -> Int64

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int64 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> Int64 ``` |

Modified Int64.distanceTo(Int64) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: Int64) -> Int ``` |
| To | ``` func distanceTo(_ other: Int64) -> Distance ``` |

Modified Int8 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Int8 : SignedInteger {     init()     init(_ value: Int8)     static func convertFromIntegerLiteral(_ value: Int8) -> Int8     typealias ArrayBoundType = Int8     func getArrayBoundValue() -> Int8     static var max: Int8 { get }     static var min: Int8 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, SignedInteger, SignedNumber |
| To | ``` struct Int8 : SignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: Int8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: Int8)     static var max: Int8 { get }     static var min: Int8 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, SignedIntegerType, SignedNumberType |

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

Modified Int8.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified Int8.advancedBy(Distance) -> Int8

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> Int8 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> Int8 ``` |

Modified Int8.distanceTo(Int8) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: Int8) -> Int ``` |
| To | ``` func distanceTo(_ other: Int8) -> Distance ``` |

Modified LazyBidirectionalCollection [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LazyBidirectionalCollection<S : Collection where S.IndexType : BidirectionalIndex> : Collection {     init(_ base: S)     func generate() -> S.GeneratorType     var startIndex: S.IndexType { get }     var endIndex: S.IndexType { get }     subscript (i: S.IndexType) -> S.GeneratorType.Element { get }     var array: [S.GeneratorType.Element] { get } } ``` | Collection |
| To | ``` struct LazyBidirectionalCollection<S : CollectionType where S.Index : BidirectionalIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     var last: S.Generator.Element? { get }     subscript (position: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` | CollectionType |

Modified LazyBidirectionalCollection.array

|  | Declaration |
| --- | --- |
| From | ``` var array: [S.GeneratorType.Element] { get } ``` |
| To | ``` var array: [S.Generator.Element] { get } ``` |

Modified LazyBidirectionalCollection.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: S.IndexType { get } ``` |
| To | ``` var endIndex: S.Index { get } ``` |

Modified LazyBidirectionalCollection.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: S.IndexType { get } ``` |
| To | ``` var startIndex: S.Index { get } ``` |

Modified LazyForwardCollection [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LazyForwardCollection<S : Collection where S.IndexType : ForwardIndex> : Collection {     init(_ base: S)     func generate() -> S.GeneratorType     var startIndex: S.IndexType { get }     var endIndex: S.IndexType { get }     subscript (i: S.IndexType) -> S.GeneratorType.Element { get }     var array: [S.GeneratorType.Element] { get } } ``` | Collection |
| To | ``` struct LazyForwardCollection<S : CollectionType where S.Index : ForwardIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     subscript (position: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` | CollectionType |

Modified LazyForwardCollection.array

|  | Declaration |
| --- | --- |
| From | ``` var array: [S.GeneratorType.Element] { get } ``` |
| To | ``` var array: [S.Generator.Element] { get } ``` |

Modified LazyForwardCollection.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: S.IndexType { get } ``` |
| To | ``` var endIndex: S.Index { get } ``` |

Modified LazyForwardCollection.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: S.IndexType { get } ``` |
| To | ``` var startIndex: S.Index { get } ``` |

Modified LazyRandomAccessCollection [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LazyRandomAccessCollection<S : Collection where S.IndexType : RandomAccessIndex> : Collection {     init(_ base: S)     func generate() -> S.GeneratorType     var startIndex: S.IndexType { get }     var endIndex: S.IndexType { get }     subscript (i: S.IndexType) -> S.GeneratorType.Element { get }     var array: [S.GeneratorType.Element] { get } } ``` | Collection |
| To | ``` struct LazyRandomAccessCollection<S : CollectionType where S.Index : RandomAccessIndexType> : CollectionType {     init(_ base: S)     func generate() -> S.Generator     var startIndex: S.Index { get }     var endIndex: S.Index { get }     var isEmpty: Bool { get }     var first: S.Generator.Element? { get }     var last: S.Generator.Element? { get }     subscript (position: S.Index) -> S.Generator.Element { get }     var array: [S.Generator.Element] { get } } ``` | CollectionType |

Modified LazyRandomAccessCollection.array

|  | Declaration |
| --- | --- |
| From | ``` var array: [S.GeneratorType.Element] { get } ``` |
| To | ``` var array: [S.Generator.Element] { get } ``` |

Modified LazyRandomAccessCollection.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: S.IndexType { get } ``` |
| To | ``` var endIndex: S.Index { get } ``` |

Modified LazyRandomAccessCollection.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: S.IndexType { get } ``` |
| To | ``` var startIndex: S.Index { get } ``` |

Modified LazySequence [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct LazySequence<S : Sequence> : Sequence {     init(_ base: S)     func generate() -> S.GeneratorType     var array: [S.GeneratorType.Element] { get } } ``` | Sequence |
| To | ``` struct LazySequence<S : SequenceType> : SequenceType {     init(_ base: S)     func generate() -> S.Generator     var array: [S.Generator.Element] { get } } ``` | SequenceType |

Modified LazySequence.array

|  | Declaration |
| --- | --- |
| From | ``` var array: [S.GeneratorType.Element] { get } ``` |
| To | ``` var array: [S.Generator.Element] { get } ``` |

Modified MapCollectionView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MapCollectionView<Base : Collection, T> : Collection {     var startIndex: Base.IndexType { get }     var endIndex: Base.IndexType { get }     subscript (index: Base.IndexType) -> T { get }     func generate() -> MapSequenceGenerator<Base.GeneratorType, T> } ``` | Collection |
| To | ``` struct MapCollectionView<Base : CollectionType, T> : CollectionType {     var startIndex: Base.Index { get }     var endIndex: Base.Index { get }     subscript (position: Base.Index) -> T { get }     func generate() -> MapSequenceGenerator<Base.Generator, T> } ``` | CollectionType |

Modified MapCollectionView.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: Base.IndexType { get } ``` |
| To | ``` var endIndex: Base.Index { get } ``` |

Modified MapCollectionView.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: Base.IndexType { get } ``` |
| To | ``` var startIndex: Base.Index { get } ``` |

Modified MapSequenceGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MapSequenceGenerator<Base : Generator, T> : Generator, Sequence {     func next() -> T?     func generate() -> MapSequenceGenerator<Base, T> } ``` | Generator, Sequence |
| To | ``` struct MapSequenceGenerator<Base : GeneratorType, T> : GeneratorType, SequenceType {     mutating func next() -> T?     func generate() -> MapSequenceGenerator<Base, T> } ``` | GeneratorType, SequenceType |

Modified MapSequenceGenerator.next() -> T?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> T? ``` |
| To | ``` mutating func next() -> T? ``` |

Modified MapSequenceView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct MapSequenceView<Base : Sequence, T> : Sequence {     func generate() -> MapSequenceGenerator<Base.GeneratorType, T> } ``` | Sequence |
| To | ``` struct MapSequenceView<Base : SequenceType, T> : SequenceType {     func generate() -> MapSequenceGenerator<Base.Generator, T> } ``` | SequenceType |

Modified MutableSliceable

|  | Protocols |
| --- | --- |
| From | MutableCollection, Sliceable |
| To | MutableCollectionType, Sliceable |

Modified ObjectIdentifier [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ObjectIdentifier : Hashable {     func uintValue() -> UInt     var hashValue: Int { get }     init(_ x: AnyObject) } ``` | Hashable |
| To | ``` struct ObjectIdentifier : Hashable, Comparable {     let value: Builtin.RawPointer     var uintValue: UInt { get }     var hashValue: Int { get }     init(_ x: AnyObject)     init(_ x: Any.Type) } ``` | Comparable, Hashable |

Modified Optional [enum]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` enum Optional<T> : LogicValue, Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     func getLogicValue() -> Bool     func map<U>(_ f: (T) -> U) -> U?     func getMirror() -> Mirror     static func convertFromNilLiteral() -> T? } ``` | DebugPrintable, LogicValue, NilLiteralConvertible, Reflectable |
| To | ``` enum Optional<T> : Reflectable, NilLiteralConvertible {     case None     case Some(T)     init()     init(_ some: T)     func map<U>(_ f: @noescape (T) -> U) -> U?     func flatMap<U>(_ f: @noescape (T) -> U?) -> U?     func getMirror() -> MirrorType     init(nilLiteral nilLiteral: ()) } ``` | DebugPrintable, NilLiteralConvertible, Reflectable |

Modified Optional.map((T) -> U) -> U?

|  | Declaration |
| --- | --- |
| From | ``` func map<U>(_ f: (T) -> U) -> U? ``` |
| To | ``` func map<U>(_ f: @noescape (T) -> U) -> U? ``` |

Modified PermutationGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct PermutationGenerator<C : Collection, Indices : Sequence where C.IndexType == C.IndexType> : Generator, Sequence {     var seq: C     var indices: Indices.GeneratorType     typealias Element = C.GeneratorType.Element     func next() -> Element?     typealias GeneratorType = PermutationGenerator<C, Indices>     func generate() -> PermutationGenerator<C, Indices>     init(elements seq: C, indices indices: Indices) } ``` | Generator, Sequence |
| To | ``` struct PermutationGenerator<C : CollectionType, Indices : SequenceType where C.Index == C.Index> : GeneratorType, SequenceType {     var seq: C     var indices: Indices.Generator     typealias Element = C.Generator.Element     mutating func next() -> Element?     typealias Generator = PermutationGenerator<C, Indices>     func generate() -> PermutationGenerator<C, Indices>     init(elements elements: C, indices indices: Indices) } ``` | GeneratorType, SequenceType |

Modified PermutationGenerator.init(elements: C, indices: Indices)

|  | Declaration |
| --- | --- |
| From | ``` init(elements seq: C, indices indices: Indices) ``` |
| To | ``` init(elements elements: C, indices indices: Indices) ``` |

Modified PermutationGenerator.indices

|  | Declaration |
| --- | --- |
| From | ``` var indices: Indices.GeneratorType ``` |
| To | ``` var indices: Indices.Generator ``` |

Modified PermutationGenerator.next() -> Element?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> Element? ``` |
| To | ``` mutating func next() -> Element? ``` |

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

Modified RandomAccessReverseView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct RandomAccessReverseView<T : Collection where T.IndexType : RandomAccessIndex> : Collection {     typealias IndexType = ReverseRandomAccessIndex<T.IndexType>     typealias GeneratorType = IndexingGenerator<RandomAccessReverseView<T>>     func generate() -> IndexingGenerator<RandomAccessReverseView<T>>     var startIndex: IndexType { get }     var endIndex: IndexType { get }     subscript (i: IndexType) -> T.GeneratorType.Element { get } } ``` | Collection |
| To | ``` struct RandomAccessReverseView<T : CollectionType where T.Index : RandomAccessIndexType> : CollectionType {     typealias Index = ReverseRandomAccessIndex<T.Index>     typealias Generator = IndexingGenerator<RandomAccessReverseView<T>>     func generate() -> IndexingGenerator<RandomAccessReverseView<T>>     var startIndex: Index { get }     var endIndex: Index { get }     subscript (position: Index) -> T.Generator.Element { get } } ``` | CollectionType |

Modified RandomAccessReverseView.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: IndexType { get } ``` |
| To | ``` var endIndex: Index { get } ``` |

Modified RandomAccessReverseView.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: IndexType { get } ``` |
| To | ``` var startIndex: Index { get } ``` |

Modified Range [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Range<T : ForwardIndex> : LogicValue, Equatable, Collection {     init(start start: T, end end: T)     var isEmpty: Bool { get }     func getLogicValue() -> Bool     typealias IndexType = T     typealias SliceType = Range<T>     subscript (i: T) -> T { get }     subscript (_: T._DisabledRangeIndex) -> T { get }     typealias GeneratorType = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T } ``` | Collection, Equatable, LogicValue, Reflectable |
| To | ``` struct Range<T : ForwardIndexType> : Equatable, CollectionType, Printable, DebugPrintable {     init(_ x: Range<T>)     init(start start: T, end end: T)     var isEmpty: Bool { get }     typealias Index = T     typealias ArraySlice = Range<T>     subscript (position: T) -> T { get }     subscript (_: T._DisabledRangeIndex) -> T { get }     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T     var description: String { get }     var debugDescription: String { get } } ``` | CollectionType, DebugPrintable, Equatable, Printable, Reflectable |

Modified RangeGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct RangeGenerator<T : ForwardIndex> : Generator, Sequence {     typealias Element = T     init(_ bounds: Range<T>)     func next() -> T?     typealias GeneratorType = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T } ``` | Generator, Sequence |
| To | ``` struct RangeGenerator<T : ForwardIndexType> : GeneratorType, SequenceType {     typealias Element = T     init(_ bounds: Range<T>)     mutating func next() -> T?     typealias Generator = RangeGenerator<T>     func generate() -> RangeGenerator<T>     var startIndex: T     var endIndex: T } ``` | GeneratorType, SequenceType |

Modified RangeGenerator.next() -> T?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> T? ``` |
| To | ``` mutating func next() -> T? ``` |

Modified Repeat [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Repeat<T> : Collection {     typealias IndexType = Int     init(count count: Int, repeatedValue repeatedValue: T)     var startIndex: IndexType { get }     var endIndex: IndexType { get }     func generate() -> IndexingGenerator<Repeat<T>>     subscript (i: Int) -> T { get }     var count: Int     let repeatedValue: T } ``` | Collection |
| To | ``` struct Repeat<T> : CollectionType {     typealias Index = Int     init(count count: Int, repeatedValue repeatedValue: T)     var startIndex: Index { get }     var endIndex: Index { get }     func generate() -> IndexingGenerator<Repeat<T>>     subscript (position: Int) -> T { get }     var count: Int     let repeatedValue: T } ``` | CollectionType |

Modified Repeat.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: IndexType { get } ``` |
| To | ``` var endIndex: Index { get } ``` |

Modified Repeat.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: IndexType { get } ``` |
| To | ``` var startIndex: Index { get } ``` |

Modified ReverseBidirectionalIndex [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ReverseBidirectionalIndex<I : BidirectionalIndex> : BidirectionalIndex {     func successor() -> ReverseBidirectionalIndex<I>     func predecessor() -> ReverseBidirectionalIndex<I>     typealias DistanceType = I.DistanceType } ``` | BidirectionalIndex |
| To | ``` struct ReverseBidirectionalIndex<I : BidirectionalIndexType> : BidirectionalIndexType {     func successor() -> ReverseBidirectionalIndex<I>     func predecessor() -> ReverseBidirectionalIndex<I>     typealias Distance = I.Distance } ``` | BidirectionalIndexType |

Modified ReverseRandomAccessIndex [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ReverseRandomAccessIndex<I : RandomAccessIndex> : RandomAccessIndex {     func successor() -> ReverseRandomAccessIndex<I>     func predecessor() -> ReverseRandomAccessIndex<I>     typealias DistanceType = I.DistanceType     func distanceTo(_ other: ReverseRandomAccessIndex<I>) -> I.DistanceType     func advancedBy(_ amount: I.DistanceType) -> ReverseRandomAccessIndex<I> } ``` | RandomAccessIndex |
| To | ``` struct ReverseRandomAccessIndex<I : RandomAccessIndexType> : RandomAccessIndexType {     func successor() -> ReverseRandomAccessIndex<I>     func predecessor() -> ReverseRandomAccessIndex<I>     typealias Distance = I.Distance     func distanceTo(_ other: ReverseRandomAccessIndex<I>) -> I.Distance     func advancedBy(_ amount: I.Distance) -> ReverseRandomAccessIndex<I> } ``` | RandomAccessIndexType |

Modified SequenceOf [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SequenceOf<T> : Sequence {     init<G : Generator where T == T>(_ generate: () -> G)     init<S : Sequence where T == T>(_ self_: S)     func generate() -> GeneratorOf<T> } ``` | Sequence |
| To | ``` struct SequenceOf<T> : SequenceType {     init<G : GeneratorType where T == T>(_ makeUnderlyingGenerator: () -> G)     init<S : SequenceType where T == T>(_ base: S)     func generate() -> GeneratorOf<T> } ``` | SequenceType |

Modified SequenceOf.init(_: () -> G)

|  | Declaration |
| --- | --- |
| From | ``` init<G : Generator where T == T>(_ generate: () -> G) ``` |
| To | ``` init<G : GeneratorType where T == T>(_ makeUnderlyingGenerator: () -> G) ``` |

Modified SequenceOf.init(_: S)

|  | Declaration |
| --- | --- |
| From | ``` init<S : Sequence where T == T>(_ self_: S) ``` |
| To | ``` init<S : SequenceType where T == T>(_ base: S) ``` |

Modified SinkOf [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct SinkOf<T> : Sink {     init(_ put: (T) -> ())     init<S : Sink where T == T>(_ base: S)     func put(_ x: T) } ``` | Sink |
| To | ``` struct SinkOf<T> : SinkType {     init(_ putElement: (T) -> ())     init<S : SinkType where T == T>(_ base: S)     func put(_ x: T) } ``` | SinkType |

Modified SinkOf.init(_: (T) -> ())

|  | Declaration |
| --- | --- |
| From | ``` init(_ put: (T) -> ()) ``` |
| To | ``` init(_ putElement: (T) -> ()) ``` |

Modified SinkOf.init(_: S)

|  | Declaration |
| --- | --- |
| From | ``` init<S : Sink where T == T>(_ base: S) ``` |
| To | ``` init<S : SinkType where T == T>(_ base: S) ``` |

Modified StaticString [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct StaticString : ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible {     init()     static func convertFromExtendedGraphemeClusterLiteral(_ value: StaticString) -> StaticString     static func convertFromStringLiteral(_ value: StaticString) -> StaticString } ``` | ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible |
| To | ``` struct StaticString : UnicodeScalarLiteralConvertible, ExtendedGraphemeClusterLiteralConvertible, StringLiteralConvertible, Printable, DebugPrintable {     var utf8Start: UnsafePointer<UInt8> { get }     var unicodeScalar: UnicodeScalar { get }     var byteSize: Word { get }     var hasPointerRepresentation: Bool { get }     var isASCII: Bool { get }     func withUTF8Buffer<R>(_ body: @noescape (UnsafeBufferPointer<UInt8>) -> R) -> R     var stringValue: String { get }     init()     init(start start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(unicodeScalar unicodeScalar: Builtin.Int32)     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: StaticString)     init(_builtinExtendedGraphemeClusterLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(extendedGraphemeClusterLiteral value: StaticString)     init(_builtinStringLiteral start: Builtin.RawPointer, byteSize byteSize: Builtin.Word, isASCII isASCII: Builtin.Int1)     init(stringLiteral value: StaticString)     var description: String { get }     var debugDescription: String { get } } ``` | DebugPrintable, ExtendedGraphemeClusterLiteralConvertible, Printable, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

Modified Streamable.writeTo(Target)

|  | Declaration |
| --- | --- |
| From | ``` func writeTo<Target : OutputStream>(inout _ target: Target) ``` |
| To | ``` func writeTo<Target : OutputStreamType>(inout _ target: Target) ``` |

Modified StrideThrough [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct StrideThrough<T : Strideable> : Sequence {     func generate() -> StrideThroughGenerator<T>     init(start start: T, end end: T, stride stride: T.Stride)     let start: T     let end: T     let stride: T.Stride } ``` | Sequence |
| To | ``` struct StrideThrough<T : Strideable> : SequenceType {     func generate() -> StrideThroughGenerator<T>     init(start start: T, end end: T, stride stride: T.Stride)     let start: T     let end: T     let stride: T.Stride } ``` | Reflectable, SequenceType |

Modified StrideThroughGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct StrideThroughGenerator<T : Strideable> : Generator {     var current: T     let end: T     let stride: T.Stride     var done: Bool     func next() -> T? } ``` | Generator |
| To | ``` struct StrideThroughGenerator<T : Strideable> : GeneratorType {     var current: T     let end: T     let stride: T.Stride     var done: Bool     mutating func next() -> T? } ``` | GeneratorType |

Modified StrideThroughGenerator.next() -> T?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> T? ``` |
| To | ``` mutating func next() -> T? ``` |

Modified StrideTo [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct StrideTo<T : Strideable> : Sequence {     func generate() -> StrideToGenerator<T>     init(start start: T, end end: T, stride stride: T.Stride)     let start: T     let end: T     let stride: T.Stride } ``` | Sequence |
| To | ``` struct StrideTo<T : Strideable> : SequenceType {     func generate() -> StrideToGenerator<T>     init(start start: T, end end: T, stride stride: T.Stride)     let start: T     let end: T     let stride: T.Stride } ``` | Reflectable, SequenceType |

Modified StrideToGenerator [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct StrideToGenerator<T : Strideable> : Generator {     var current: T     let end: T     let stride: T.Stride     func next() -> T? } ``` | Generator |
| To | ``` struct StrideToGenerator<T : Strideable> : GeneratorType {     var current: T     let end: T     let stride: T.Stride     mutating func next() -> T? } ``` | GeneratorType |

Modified StrideToGenerator.next() -> T?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> T? ``` |
| To | ``` mutating func next() -> T? ``` |

Modified String [struct]

|  | Protocols |
| --- | --- |
| From | Collection, Comparable, DebugPrintable, Equatable, ExtendedGraphemeClusterLiteralConvertible, ExtensibleCollection, Hashable, OutputStream, Reflectable, Sliceable, Streamable, StringInterpolationConvertible, StringLiteralConvertible |
| To | CollectionType, Comparable, DebugPrintable, Equatable, ExtendedGraphemeClusterLiteralConvertible, ExtensibleCollectionType, Hashable, OutputStreamType, RangeReplaceableCollectionType, Reflectable, Sliceable, Streamable, StringInterpolationConvertible, StringLiteralConvertible, UnicodeScalarLiteralConvertible |

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

Modified String.extend(S)

|  | Declaration |
| --- | --- |
| From | ``` func extend<S : Sequence where Character == Character>(_ seq: S) ``` |
| To | ``` mutating func extend<S : SequenceType where Character == Character>(_ newElements: S) ``` |

Modified String.join(S) -> String

|  | Declaration |
| --- | --- |
| From | ``` func join<S : Sequence where String == String>(_ elements: S) -> String ``` |
| To | ``` func join<S : SequenceType where String == String>(_ elements: S) -> String ``` |

Modified String.reserveCapacity(Int)

|  | Declaration |
| --- | --- |
| From | ``` func reserveCapacity(_ n: Int) ``` |
| To | ``` mutating func reserveCapacity(_ n: Int) ``` |

Modified String.unicodeScalars

|  | Declaration |
| --- | --- |
| From | ``` var unicodeScalars: String.UnicodeScalarView { get } ``` |
| To | ``` var unicodeScalars: String.UnicodeScalarView ``` |

Modified String.withCString(UnsafePointer<Int8> -> Result) -> Result

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withCString<Result>(_ f: (UnsafePointer<CChar>) -> Result) -> Result ``` | OS X 10.10 |
| To | ``` func withCString<Result>(_ f: @noescape UnsafePointer<Int8> -> Result) -> Result ``` | OS X 10.10.3 |

Modified String.write(String)

|  | Declaration |
| --- | --- |
| From | ``` func write(_ string: String) ``` |
| To | ``` mutating func write(_ other: String) ``` |

Modified String.writeTo(Target)

|  | Declaration |
| --- | --- |
| From | ``` func writeTo<Target : OutputStream>(inout _ target: Target) ``` |
| To | ``` func writeTo<Target : OutputStreamType>(inout _ target: Target) ``` |

Modified String.Index [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Index : BidirectionalIndex, Reflectable {         func successor() -> String.Index         func predecessor() -> String.Index         func getMirror() -> Mirror     } ``` | BidirectionalIndex, Reflectable |
| To | ``` struct Index : BidirectionalIndexType, Comparable, Reflectable {         func successor() -> String.Index         func predecessor() -> String.Index         func getMirror() -> MirrorType     } ``` | BidirectionalIndexType, Comparable, Reflectable |

Modified String.UTF16View [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF16View : Sliceable, Reflectable {         var startIndex: Int { get }         var endIndex: Int { get }         typealias GeneratorType         func generate() -> GeneratorType         subscript (i: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         func getMirror() -> Mirror     } ``` | Reflectable, Sliceable |
| To | ``` struct UTF16View : Sliceable, Reflectable, Printable, DebugPrintable {         struct Index {         }         var startIndex: String.UTF16View.Index { get }         var endIndex: String.UTF16View.Index { get }         typealias Generator         func generate() -> Generator         subscript (i: String.UTF16View.Index) -> UInt16 { get }         subscript (i: Int) -> UInt16 { get }         subscript (subRange: Range<Int>) -> String.UTF16View { get }         subscript (subRange: Range<String.UTF16View.Index>) -> String.UTF16View { get }         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | DebugPrintable, Printable, Reflectable, Sliceable |

Modified String.UTF16View.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: Int { get } ``` |
| To | ``` var endIndex: String.UTF16View.Index { get } ``` |

Modified String.UTF16View.generate() -> Generator

|  | Declaration |
| --- | --- |
| From | ``` func generate() -> GeneratorType ``` |
| To | ``` func generate() -> Generator ``` |

Modified String.UTF16View.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: Int { get } ``` |
| To | ``` var startIndex: String.UTF16View.Index { get } ``` |

Modified String.UTF8View [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF8View : Collection, Reflectable {         struct Index : ForwardIndex {             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (i: String.UTF8View.Index) -> CodeUnit { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> Mirror     } ``` | Collection, Reflectable |
| To | ``` struct UTF8View : CollectionType, Reflectable, Printable, DebugPrintable {         struct Index : ForwardIndexType {             typealias Buffer = UTF8Chunk             func successor() -> String.UTF8View.Index         }         var startIndex: String.UTF8View.Index { get }         var endIndex: String.UTF8View.Index { get }         subscript (position: String.UTF8View.Index) -> CodeUnit { get }         subscript (subRange: Range<String.UTF8View.Index>) -> String.UTF8View { get }         func generate() -> IndexingGenerator<String.UTF8View>         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | CollectionType, DebugPrintable, Printable, Reflectable |

Modified String.UTF8View.Index [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Index : ForwardIndex {             func successor() -> String.UTF8View.Index         } ``` | ForwardIndex |
| To | ``` struct Index : ForwardIndexType {             typealias Buffer = UTF8Chunk             func successor() -> String.UTF8View.Index         } ``` | ForwardIndexType |

Modified String.UnicodeScalarView [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnicodeScalarView : Sliceable, Sequence {         struct IndexType : BidirectionalIndex {             func successor() -> String.UnicodeScalarView.IndexType             func predecessor() -> String.UnicodeScalarView.IndexType         }         var startIndex: String.UnicodeScalarView.IndexType { get }         var endIndex: String.UnicodeScalarView.IndexType { get }         subscript (i: String.UnicodeScalarView.IndexType) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.IndexType>) -> String.UnicodeScalarView { get }         struct GeneratorType : Generator {             func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.GeneratorType         func compare(_ other: String.UnicodeScalarView) -> Int     } ``` | Sequence, Sliceable |
| To | ``` struct UnicodeScalarView : Sliceable, SequenceType, Reflectable, Printable, DebugPrintable {         struct Index : BidirectionalIndexType, Comparable {             func successor() -> String.UnicodeScalarView.Index             func predecessor() -> String.UnicodeScalarView.Index         }         var startIndex: String.UnicodeScalarView.Index { get }         var endIndex: String.UnicodeScalarView.Index { get }         subscript (position: String.UnicodeScalarView.Index) -> UnicodeScalar { get }         subscript (r: Range<String.UnicodeScalarView.Index>) -> String.UnicodeScalarView { get }         struct Generator : GeneratorType {             mutating func next() -> UnicodeScalar?         }         func generate() -> String.UnicodeScalarView.Generator         func getMirror() -> MirrorType         var description: String { get }         var debugDescription: String { get }     } ``` | DebugPrintable, Printable, Reflectable, SequenceType, Sliceable |

Modified String.UnicodeScalarView.endIndex

|  | Declaration |
| --- | --- |
| From | ``` var endIndex: String.UnicodeScalarView.IndexType { get } ``` |
| To | ``` var endIndex: String.UnicodeScalarView.Index { get } ``` |

Modified String.UnicodeScalarView.startIndex

|  | Declaration |
| --- | --- |
| From | ``` var startIndex: String.UnicodeScalarView.IndexType { get } ``` |
| To | ``` var startIndex: String.UnicodeScalarView.Index { get } ``` |

Modified UInt [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt : UnsignedInteger {     init()     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     static func convertFromIntegerLiteral(_ value: UInt) -> UInt     typealias ArrayBoundType = UInt     func getArrayBoundValue() -> UInt     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, UnsignedInteger |
| To | ``` struct UInt : UnsignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ v: Builtin.Word)     init(_ value: UInt)     init(bigEndian value: UInt)     init(littleEndian value: UInt)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt)     var bigEndian: UInt { get }     var littleEndian: UInt { get }     var byteSwapped: UInt { get }     static var max: UInt { get }     static var min: UInt { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |

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

Modified UInt.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified UInt.advancedBy(Distance) -> UInt

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt ``` |
| To | ``` func advancedBy(_ amount: Distance) -> UInt ``` |

Modified UInt.distanceTo(UInt) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: UInt) -> Int ``` |
| To | ``` func distanceTo(_ other: UInt) -> Distance ``` |

Modified UInt16 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt16 : UnsignedInteger {     init()     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     static func convertFromIntegerLiteral(_ value: UInt16) -> UInt16     typealias ArrayBoundType = UInt16     func getArrayBoundValue() -> UInt16     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, UnsignedInteger |
| To | ``` struct UInt16 : UnsignedIntegerType {     var value: Builtin.Int16     typealias Distance = Int     init()     init(_ value: UInt16)     init(bigEndian value: UInt16)     init(littleEndian value: UInt16)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt16)     var bigEndian: UInt16 { get }     var littleEndian: UInt16 { get }     var byteSwapped: UInt16 { get }     static var max: UInt16 { get }     static var min: UInt16 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |

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

Modified UInt16.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified UInt16.advancedBy(Distance) -> UInt16

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt16 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> UInt16 ``` |

Modified UInt16.distanceTo(UInt16) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: UInt16) -> Int ``` |
| To | ``` func distanceTo(_ other: UInt16) -> Distance ``` |

Modified UInt32 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt32 : UnsignedInteger {     init()     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     static func convertFromIntegerLiteral(_ value: UInt32) -> UInt32     typealias ArrayBoundType = UInt32     func getArrayBoundValue() -> UInt32     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, UnsignedInteger |
| To | ``` struct UInt32 : UnsignedIntegerType {     var value: Builtin.Int32     typealias Distance = Int     init()     init(_ value: UInt32)     init(bigEndian value: UInt32)     init(littleEndian value: UInt32)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt32)     var bigEndian: UInt32 { get }     var littleEndian: UInt32 { get }     var byteSwapped: UInt32 { get }     static var max: UInt32 { get }     static var min: UInt32 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |

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

Modified UInt32.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified UInt32.advancedBy(Distance) -> UInt32

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt32 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> UInt32 ``` |

Modified UInt32.distanceTo(UInt32) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: UInt32) -> Int ``` |
| To | ``` func distanceTo(_ other: UInt32) -> Distance ``` |

Modified UInt64 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt64 : UnsignedInteger {     init()     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     static func convertFromIntegerLiteral(_ value: UInt64) -> UInt64     typealias ArrayBoundType = UInt64     func getArrayBoundValue() -> UInt64     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, UnsignedInteger |
| To | ``` struct UInt64 : UnsignedIntegerType {     var value: Builtin.Int64     typealias Distance = Int     init()     init(_ value: UInt64)     init(bigEndian value: UInt64)     init(littleEndian value: UInt64)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt64)     var bigEndian: UInt64 { get }     var littleEndian: UInt64 { get }     var byteSwapped: UInt64 { get }     static var max: UInt64 { get }     static var min: UInt64 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |

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

Modified UInt64.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified UInt64.advancedBy(Distance) -> UInt64

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt64 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> UInt64 ``` |

Modified UInt64.distanceTo(UInt64) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: UInt64) -> Int ``` |
| To | ``` func distanceTo(_ other: UInt64) -> Distance ``` |

Modified UInt8 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UInt8 : UnsignedInteger {     init()     init(_ value: UInt8)     static func convertFromIntegerLiteral(_ value: UInt8) -> UInt8     typealias ArrayBoundType = UInt8     func getArrayBoundValue() -> UInt8     static var max: UInt8 { get }     static var min: UInt8 { get } } ``` | BitwiseOperations, CVarArg, Hashable, Printable, RandomAccessIndex, Reflectable, UnsignedInteger |
| To | ``` struct UInt8 : UnsignedIntegerType {     var value: Builtin.Int8     typealias Distance = Int     init()     init(_ value: UInt8)     init(_builtinIntegerLiteral value: Builtin.Int2048)     init(integerLiteral value: UInt8)     static var max: UInt8 { get }     static var min: UInt8 { get } } ``` | BitwiseOperationsType, CVarArgType, Hashable, Printable, RandomAccessIndexType, Reflectable, UnsignedIntegerType |

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

Modified UInt8.init(_: Float80)

|  | Declaration |
| --- | --- |
| From | ``` init(_ v: Float80) ``` |
| To | ``` init(_ other: Float80) ``` |

Modified UInt8.advancedBy(Distance) -> UInt8

|  | Declaration |
| --- | --- |
| From | ``` func advancedBy(_ amount: Int) -> UInt8 ``` |
| To | ``` func advancedBy(_ amount: Distance) -> UInt8 ``` |

Modified UInt8.distanceTo(UInt8) -> Distance

|  | Declaration |
| --- | --- |
| From | ``` func distanceTo(_ other: UInt8) -> Int ``` |
| To | ``` func distanceTo(_ other: UInt8) -> Distance ``` |

Modified UTF16 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF16 : UnicodeCodec {     typealias CodeUnit = UInt16     init()     func decode<G : Generator where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode<S : Sink where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` | UnicodeCodec |
| To | ``` struct UTF16 : UnicodeCodecType {     typealias CodeUnit = UInt16     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` | UnicodeCodecType |

Modified UTF16.decode(G) -> UnicodeDecodingResult

|  | Declaration |
| --- | --- |
| From | ``` func decode<G : Generator where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` |
| To | ``` mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` |

Modified UTF16.encode(UnicodeScalar, output: S) [static]

|  | Declaration |
| --- | --- |
| From | ``` static func encode<S : Sink where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |
| To | ``` static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |

Modified UTF16.measure(Encoding.Type, input: Input, repairIllFormedSequences: Bool) -> (Int, Bool)? [static]

|  | Declaration |
| --- | --- |
| From | ``` static func measure<Encoding : UnicodeCodec, Input : Generator where Encoding.CodeUnit == Encoding.CodeUnit>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? ``` |
| To | ``` static func measure<Encoding : UnicodeCodecType, Input : GeneratorType where Encoding.CodeUnit == Encoding.CodeUnit>(_ _: Encoding.Type, input input: Input, repairIllFormedSequences repairIllFormedSequences: Bool) -> (Int, Bool)? ``` |

Modified UTF32 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF32 : UnicodeCodec {     typealias CodeUnit = UInt32     init()     func decode<G : Generator where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode<S : Sink where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` | UnicodeCodec |
| To | ``` struct UTF32 : UnicodeCodecType {     typealias CodeUnit = UInt32     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` | UnicodeCodecType |

Modified UTF32.decode(G) -> UnicodeDecodingResult

|  | Declaration |
| --- | --- |
| From | ``` func decode<G : Generator where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` |
| To | ``` mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ input: G) -> UnicodeDecodingResult ``` |

Modified UTF32.encode(UnicodeScalar, output: S) [static]

|  | Declaration |
| --- | --- |
| From | ``` static func encode<S : Sink where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |
| To | ``` static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |

Modified UTF8 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UTF8 : UnicodeCodec {     typealias CodeUnit = UInt8     init()     func decode<G : Generator where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode<S : Sink where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) } ``` | UnicodeCodec |
| To | ``` struct UTF8 : UnicodeCodecType {     typealias CodeUnit = UInt8     init()     mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult     static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S)     static func isContinuation(_ byte: CodeUnit) -> Bool } ``` | UnicodeCodecType |

Modified UTF8.decode(G) -> UnicodeDecodingResult

|  | Declaration |
| --- | --- |
| From | ``` func decode<G : Generator where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` |
| To | ``` mutating func decode<G : GeneratorType where CodeUnit == CodeUnit>(inout _ next: G) -> UnicodeDecodingResult ``` |

Modified UTF8.encode(UnicodeScalar, output: S) [static]

|  | Declaration |
| --- | --- |
| From | ``` static func encode<S : Sink where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |
| To | ``` static func encode<S : SinkType where CodeUnit == CodeUnit>(_ input: UnicodeScalar, inout output output: S) ``` |

Modified UnicodeScalar [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnicodeScalar : ExtendedGraphemeClusterLiteralConvertible {     var value: UInt32 { get }     static func convertFromExtendedGraphemeClusterLiteral(_ value: String) -> UnicodeScalar     init()     init(_ v: UInt32)     init(_ v: UnicodeScalar)     func escape(asASCII asASCII: Bool) -> String     func isASCII() -> Bool } ``` | Comparable, DebugPrintable, ExtendedGraphemeClusterLiteralConvertible, Hashable, Printable, Reflectable, Streamable |
| To | ``` struct UnicodeScalar : UnicodeScalarLiteralConvertible {     var value: UInt32 { get }     init(_builtinUnicodeScalarLiteral value: Builtin.Int32)     init(unicodeScalarLiteral value: UnicodeScalar)     init()     init(_ value: Builtin.Int32)     init(_ v: UInt32)     init(_ v: UInt16)     init(_ v: UInt8)     init(_ v: UnicodeScalar)     func escape(asASCII asASCII: Bool) -> String     func isASCII() -> Bool } ``` | Comparable, DebugPrintable, Hashable, Printable, Reflectable, Streamable, UnicodeScalarLiteralConvertible |

Modified UnicodeScalar.writeTo(Target)

|  | Declaration |
| --- | --- |
| From | ``` func writeTo<Target : OutputStream>(inout _ target: Target) ``` |
| To | ``` func writeTo<Target : OutputStreamType>(inout _ target: Target) ``` |

Modified UnsafePointer [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct UnsafePointer<T> : BidirectionalIndex, Comparable, Hashable, LogicValue, NilLiteralConvertible {     init()     init(_ other: COpaquePointer)     init(_ value: Int)     init<U>(_ from: UnsafePointer<U>)     init<U>(_ from: ConstUnsafePointer<U>)     static func convertFromNilLiteral() -> UnsafePointer<T>     static func null() -> UnsafePointer<T>     static func alloc(_ num: Int) -> UnsafePointer<T>     func dealloc(_ num: Int)     var memory: T     func initialize(_ newvalue: T)     func move() -> T     func moveInitializeBackwardFrom(_ source: UnsafePointer<T>, count count: Int)     func moveAssignFrom(_ source: UnsafePointer<T>, count count: Int)     func moveInitializeFrom(_ source: UnsafePointer<T>, count count: Int)     func initializeFrom(_ source: UnsafePointer<T>, count count: Int)     func initializeFrom<C : Collection where T == T>(_ source: C)     func destroy()     func destroy(_ count: Int)     func getLogicValue() -> Bool     subscript (i: Int) -> T     var hashValue: Int { get }     func successor() -> UnsafePointer<T>     func predecessor() -> UnsafePointer<T> } ``` | BidirectionalIndex, Comparable, Hashable, LogicValue, NilLiteralConvertible, Printable, Reflectable |
| To | ``` struct UnsafePointer<T> : RandomAccessIndexType, Hashable, NilLiteralConvertible, _PointerType {     init()     init(_ other: COpaquePointer)     init(bitPattern bitPattern: Word)     init(bitPattern bitPattern: UWord)     init<U>(_ from: UnsafeMutablePointer<U>)     init<U>(_ from: UnsafePointer<U>)     init(nilLiteral nilLiteral: ())     static func null() -> UnsafePointer<T>     var memory: T { get }     subscript (i: Int) -> T { get }     var hashValue: Int { get }     func successor() -> UnsafePointer<T>     func predecessor() -> UnsafePointer<T>     func distanceTo(_ x: UnsafePointer<T>) -> Int     func advancedBy(_ n: Int) -> UnsafePointer<T> } ``` | CVarArgType, DebugPrintable, Hashable, NilLiteralConvertible, RandomAccessIndexType, Reflectable |

Modified UnsafePointer.memory

|  | Declaration |
| --- | --- |
| From | ``` var memory: T ``` |
| To | ``` var memory: T { get } ``` |

Modified VaListBuilder.header

|  | Declaration |
| --- | --- |
| From | ``` final final final var header: VaListBuilder.Header ``` |
| To | ``` final var header: VaListBuilder.Header ``` |

Modified VaListBuilder.Header [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct Header {         var gp_offset: UInt32         var fp_offset: UInt32         var overflow_arg_area: UnsafePointer<Word>         var reg_save_area: UnsafePointer<Word>     } ``` |
| To | ``` struct Header {         var gp_offset: UInt32         var fp_offset: UInt32         var overflow_arg_area: UnsafeMutablePointer<Word>         var reg_save_area: UnsafeMutablePointer<Word>     } ``` |

Modified VaListBuilder.Header.overflow_arg_area

|  | Declaration |
| --- | --- |
| From | ``` var overflow_arg_area: UnsafePointer<Word> ``` |
| To | ``` var overflow_arg_area: UnsafeMutablePointer<Word> ``` |

Modified VaListBuilder.Header.reg_save_area

|  | Declaration |
| --- | --- |
| From | ``` var reg_save_area: UnsafePointer<Word> ``` |
| To | ``` var reg_save_area: UnsafeMutablePointer<Word> ``` |

Modified Zip2 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct Zip2<S0 : Sequence, S1 : Sequence> : Sequence {     typealias Stream1 = S0.GeneratorType     typealias Stream2 = S1.GeneratorType     typealias GeneratorType = ZipGenerator2<S0.GeneratorType, S1.GeneratorType>     init(_ s0: S0, _ s1: S1)     func generate() -> GeneratorType     var sequences: (S0, S1) } ``` | Sequence |
| To | ``` struct Zip2<S0 : SequenceType, S1 : SequenceType> : SequenceType {     typealias Stream1 = S0.Generator     typealias Stream2 = S1.Generator     typealias Generator = ZipGenerator2<S0.Generator, S1.Generator>     init(_ s0: S0, _ s1: S1)     func generate() -> Generator     var sequences: (S0, S1) } ``` | SequenceType |

Modified ZipGenerator2 [struct]

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct ZipGenerator2<E0 : Generator, E1 : Generator> : Generator {     typealias Element = (E0.Element, E1.Element)     init(_ e0: E0, _ e1: E1)     func next() -> Element?     var baseStreams: (E0, E1) } ``` | Generator |
| To | ``` struct ZipGenerator2<E0 : GeneratorType, E1 : GeneratorType> : GeneratorType {     typealias Element = (E0.Element, E1.Element)     init(_ e0: E0, _ e1: E1)     mutating func next() -> Element?     var baseStreams: (E0, E1) } ``` | GeneratorType |

Modified ZipGenerator2.next() -> Element?

|  | Declaration |
| --- | --- |
| From | ``` func next() -> Element? ``` |
| To | ``` mutating func next() -> Element? ``` |

Modified Dictionary.Element

|  | Declaration |
| --- | --- |
| From | ``` typealias Element = (KeyType, ValueType) ``` |
| To | ``` typealias Element = (Key, Value) ``` |

Modified Dictionary.Index

|  | Declaration |
| --- | --- |
| From | ``` typealias Index = DictionaryIndex<KeyType, ValueType> ``` |
| To | ``` typealias Index = DictionaryIndex<Key, Value> ``` |

Modified DictionaryIndex.Index

|  | Declaration |
| --- | --- |
| From | ``` typealias Index = DictionaryIndex<KeyType, ValueType> ``` |
| To | ``` typealias Index = DictionaryIndex<Key, Value> ``` |

Modified PermutationGenerator.Element

|  | Declaration |
| --- | --- |
| From | ``` typealias Element = C.GeneratorType.Element ``` |
| To | ``` typealias Element = C.Generator.Element ``` |

Modified Zip2.Stream1

|  | Declaration |
| --- | --- |
| From | ``` typealias Stream1 = S0.GeneratorType ``` |
| To | ``` typealias Stream1 = S0.Generator ``` |

Modified Zip2.Stream2

|  | Declaration |
| --- | --- |
| From | ``` typealias Stream2 = S1.GeneratorType ``` |
| To | ``` typealias Stream2 = S1.Generator ``` |

Modified abs(T) -> T

|  | Declaration |
| --- | --- |
| From | ``` func abs<T : SignedNumber>(_ x: T) -> T ``` |
| To | ``` func abs<T : SignedNumberType>(_ x: T) -> T ``` |

Modified debugPrint(T)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrint<T>(_ object: T) ``` |
| To | ``` @inline(never) func debugPrint<T>(_ x: T) ``` |

Modified debugPrint(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrint<T, TargetStream : OutputStream>(_ object: T, inout _ target: TargetStream) ``` |
| To | ``` @inline(never) func debugPrint<T, TargetStream : OutputStreamType>(_ value: T, inout _ target: TargetStream) ``` |

Modified debugPrintln(T)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrintln<T>(_ object: T) ``` |
| To | ``` @inline(never) func debugPrintln<T>(_ x: T) ``` |

Modified debugPrintln(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func debugPrintln<T, TargetStream : OutputStream>(_ object: T, inout _ target: TargetStream) ``` |
| To | ``` @inline(never) func debugPrintln<T, TargetStream : OutputStreamType>(_ x: T, inout _ target: TargetStream) ``` |

Modified equal(S1, S2) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func equal<S1 : Sequence, S2 : Sequence where S1.GeneratorType.Element == S1.GeneratorType.Element, S1.GeneratorType.Element : Equatable>(_ a1: S1, _ a2: S2) -> Bool ``` |
| To | ``` func equal<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element, S1.Generator.Element : Equatable>(_ a1: S1, _ a2: S2) -> Bool ``` |

Modified join(C, S) -> C

|  | Declaration |
| --- | --- |
| From | ``` func join<C : ExtensibleCollection, S : Sequence where C == C>(_ separator: C, _ elements: S) -> C ``` |
| To | ``` func join<C : ExtensibleCollectionType, S : SequenceType where C == C>(_ separator: C, _ elements: S) -> C ``` |

Modified lazy(S) -> LazyBidirectionalCollection<S>

|  | Declaration |
| --- | --- |
| From | ``` func lazy<S : Collection where S.IndexType : BidirectionalIndex>(_ s: S) -> LazyBidirectionalCollection<S> ``` |
| To | ``` func lazy<S : CollectionType where S.Index : BidirectionalIndexType>(_ s: S) -> LazyBidirectionalCollection<S> ``` |

Modified lazy(S) -> LazyForwardCollection<S>

|  | Declaration |
| --- | --- |
| From | ``` func lazy<S : Collection where S.IndexType : ForwardIndex>(_ s: S) -> LazyForwardCollection<S> ``` |
| To | ``` func lazy<S : CollectionType where S.Index : ForwardIndexType>(_ s: S) -> LazyForwardCollection<S> ``` |

Modified lazy(S) -> LazyRandomAccessCollection<S>

|  | Declaration |
| --- | --- |
| From | ``` func lazy<S : Collection where S.IndexType : RandomAccessIndex>(_ s: S) -> LazyRandomAccessCollection<S> ``` |
| To | ``` func lazy<S : CollectionType where S.Index : RandomAccessIndexType>(_ s: S) -> LazyRandomAccessCollection<S> ``` |

Modified lazy(S) -> LazySequence<S>

|  | Declaration |
| --- | --- |
| From | ``` func lazy<S : Sequence>(_ s: S) -> LazySequence<S> ``` |
| To | ``` func lazy<S : SequenceType>(_ s: S) -> LazySequence<S> ``` |

Modified lexicographicalCompare(S1, S2) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func lexicographicalCompare<S1 : Sequence, S2 : Sequence where S1.GeneratorType.Element == S1.GeneratorType.Element, S1.GeneratorType.Element : Comparable>(_ a1: S1, _ a2: S2) -> Bool ``` |
| To | ``` func lexicographicalCompare<S1 : SequenceType, S2 : SequenceType where S1.Generator.Element == S1.Generator.Element, S1.Generator.Element : Comparable>(_ a1: S1, _ a2: S2) -> Bool ``` |

Modified map(T?,(T) -> U) -> U?

|  | Declaration |
| --- | --- |
| From | ``` func map<T, U>(_ x: T?, _ f: (T) -> U) -> U? ``` |
| To | ``` func map<T, U>(_ x: T?, _ f: @noescape (T) -> U) -> U? ``` |

Modified numericCast(T) -> U

|  | Declaration |
| --- | --- |
| From | ``` func numericCast<T, U>(_ x: T) -> U ``` |
| To | ``` func numericCast<T : _UnsignedIntegerType, U : _UnsignedIntegerType>(_ x: T) -> U ``` |

Modified print(T)

|  | Declaration |
| --- | --- |
| From | ``` func print<T>(_ object: T) ``` |
| To | ``` @inline(never) func print<T>(_ value: T) ``` |

Modified print(T, TargetStream)

|  | Declaration |
| --- | --- |
| From | ``` func print<T, TargetStream : OutputStream>(_ object: T, inout _ target: TargetStream) ``` |
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
| From | ``` func println<T, TargetStream : OutputStream>(_ object: T, inout _ target: TargetStream) ``` |
| To | ``` @inline(never) func println<T, TargetStream : OutputStreamType>(_ value: T, inout _ target: TargetStream) ``` |

Modified sort(C)

|  | Declaration |
| --- | --- |
| From | ``` func sort<C : MutableCollection where C.IndexType : RandomAccessIndex, C.GeneratorType.Element : Comparable>(inout _ collection: C) ``` |
| To | ``` func sort<C : MutableCollectionType where C.Index : RandomAccessIndexType, C.Generator.Element : Comparable>(inout _ collection: C) ``` |

Modified sort([T],(T, T) -> Bool)

|  | Declaration |
| --- | --- |
| From | ``` func sort<T>(inout _ array: [T], _ predicate: (T, T) -> Bool) ``` |
| To | ``` func sort<T>(inout _ array: [T], _ isOrderedBefore: (T, T) -> Bool) ``` |

Modified startsWith(S0, S1) -> Bool

|  | Declaration |
| --- | --- |
| From | ``` func startsWith<S0 : Sequence, S1 : Sequence where S0.GeneratorType.Element == S0.GeneratorType.Element, S0.GeneratorType.Element : Equatable>(_ s: S0, _ prefix: S1) -> Bool ``` |
| To | ``` func startsWith<S0 : SequenceType, S1 : SequenceType where S0.Generator.Element == S0.Generator.Element, S0.Generator.Element : Equatable>(_ s: S0, _ prefix: S1) -> Bool ``` |

Modified toString(T) -> String

|  | Declaration |
| --- | --- |
| From | ``` func toString<T>(_ object: T) -> String ``` |
| To | ``` @inline(never) func toString<T>(_ x: T) -> String ``` |

Modified underestimateCount(T) -> Int

|  | Declaration |
| --- | --- |
| From | ``` func underestimateCount<T : Sequence>(_ x: T) -> Int ``` |
| To | ``` func underestimateCount<T : SequenceType>(_ x: T) -> Int ``` |

Modified withExtendedLifetime(T,() -> Result) -> Result

|  | Declaration |
| --- | --- |
| From | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: () -> Result) -> Result ``` |
| To | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: @noescape () -> Result) -> Result ``` |

Modified withExtendedLifetime(T, T -> Result) -> Result

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: (T) -> Result) -> Result ``` | OS X 10.10 |
| To | ``` func withExtendedLifetime<T, Result>(_ x: T, _ f: @noescape T -> Result) -> Result ``` | OS X 10.10.3 |

Modified withUnsafePointer(T, UnsafePointer<T> -> Result) -> Result

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func withUnsafePointer<T, Result>(inout _ arg: T, _ body: (UnsafePointer<T>) -> Result) -> Result ``` | OS X 10.10 |
| To | ``` func withUnsafePointer<T, Result>(inout _ arg: T, _ body: @noescape UnsafePointer<T> -> Result) -> Result ``` | OS X 10.10.3 |

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
| From | ``` func withVaList<R>(_ builder: VaListBuilder, _ f: (CVaListPointer) -> R) -> R ``` | OS X 10.10 |
| To | ``` func withVaList<R>(_ builder: VaListBuilder, _ f: @noescape CVaListPointer -> R) -> R ``` | OS X 10.10.3 |

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
