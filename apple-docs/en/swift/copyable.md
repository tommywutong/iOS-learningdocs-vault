---
title: Copyable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/copyable
source_url: 'https://developer.apple.com/documentation/swift/copyable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/copyable.json'
content_hash: 'sha256:f9acd4b95c194b90'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Copyable

<sub>Protocol</sub>

A type whose values can be implicitly or explicitly copied.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Copyable
```

## Overview

Conforming to this protocol indicates that a type’s value can be copied; this protocol doesn’t have any required methods or properties. You don’t generally need to write an explicit conformance to `Copyable`. The following places implicitly include `Copyable` conformance:

- Structure declarations, unless it has a noncopyable stored property
- Enumeration declarations, unless it has a case whose associated value isn’t copyable
- Class declarations
- Actor declarations
- Protocol declarations
- Associated type declarations
- The `Self` type in a protocol extension
- In an extension, the generic parameters of the type being extended

A class or actor can contain noncopyable stored properties, while still being copyable itself — classes and actors are copied by retaining and releasing references.

In a declaration that includes generic type parameters, each generic type parameter implicitly includes `Copyable` in its list of requirements. Metatypes and tuples of copyable types are also implicitly copyable, as are boxed protocol types. For example, all of the following pairs of declarations are equivalent:

```swift
struct MyStructure { }
struct MyStructere: Copyable { }

protocol MyProtocol { }
protocol MyProtocol: Copyable { }

protocol AnotherProtocol {
    associatedtype MyType
    associatedtype MyType: Copyable
}

func genericFunction<T>(t: T) { }
func genericFunction<T>(t: T) where T: Copyable { }

let x: any MyProtocol
let x: any MyProtocol & Copyable
```

To suppress an implicit conformance to `Copyable` you write `~Copyable`. For example, only copyable types can conform to `MyProtocol` in the example above, but both copyable and noncopyable types can conform `NoRequirements` in the example below:

```swift
protocol NoRequirements: ~Copyable { }
```

Extensions to the `Copyable` protocol are not allowed.

## Relationships

- **Conforming Types**: [Anchor](../regexbuilder/anchor.md), [AnyBidirectionalCollection](anybidirectionalcollection.md), [AnyCollection](anycollection.md), [AnyHashable](anyhashable.md), [AnyIterator](anyiterator.md), [AnyKeyPath](anykeypath.md), [AnyRandomAccessCollection](anyrandomaccesscollection.md), [AnyRegexOutput](anyregexoutput.md), [AnySequence](anysequence.md), [Array](array.md), [ArraySlice](arrayslice.md), [AsyncCompactMapSequence](asynccompactmapsequence.md), [AsyncDropFirstSequence](asyncdropfirstsequence.md), [AsyncDropWhileSequence](asyncdropwhilesequence.md), [AsyncFilterSequence](asyncfiltersequence.md), [AsyncFlatMapSequence](asyncflatmapsequence.md), [AsyncMapSequence](asyncmapsequence.md), [AsyncPrefixSequence](asyncprefixsequence.md), [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md), [AsyncStream](asyncstream.md), [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md), [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md), [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md), [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md), [AsyncThrowingMapSequence](asyncthrowingmapsequence.md), [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md), [AsyncThrowingStream](asyncthrowingstream.md), [AtomicLoadOrdering](../synchronization/atomicloadordering.md), [AtomicStoreOrdering](../synchronization/atomicstoreordering.md), [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [Bool](bool.md), [ByteOrder](byteorder.md), [CVaListPointer](cvalistpointer.md), [Capture](../regexbuilder/capture.md), [Character](character.md), [CharacterClass](../regexbuilder/characterclass.md), [ChoiceOf](../regexbuilder/choiceof.md), [ClosedRange](closedrange.md), [CollectionDifference](collectiondifference.md), [Change](collectiondifference/change.md), [Index](collectiondifference/index.md), [CollectionOfOne](collectionofone.md), [Iterator](collectionofone/iterator.md), [ContiguousArray](contiguousarray.md), [ContinuousClock](continuousclock.md), [Instant](continuousclock/instant.md), [DecodingError](decodingerror.md), [DefaultIndices](defaultindices.md), [DefaultStringInterpolation](defaultstringinterpolation.md), [Dictionary](dictionary.md), [Iterator](dictionary/iterator.md), [Keys](dictionary/keys-swift.struct.md), [Values](dictionary/values-swift.struct.md), [DiscardingTaskGroup](discardingtaskgroup.md), [DiscontiguousSlice](discontiguousslice.md), [Index](discontiguousslice/index.md), [Double](double.md), [DropFirstSequence](dropfirstsequence.md), [DropWhileSequence](dropwhilesequence.md), [Iterator](dropwhilesequence/iterator.md), [Duration](duration.md), [TimeFormatStyle](duration/timeformatstyle.md), [Attributed](duration/timeformatstyle/attributed-swift.struct.md), [UnitsFormatStyle](duration/unitsformatstyle.md), [Attributed](duration/unitsformatstyle/attributed-swift.struct.md), [EmptyCollection](emptycollection.md), [Iterator](emptycollection/iterator.md), [EncodingError](encodingerror.md), [EnumeratedSequence](enumeratedsequence.md), [Iterator](enumeratedsequence/iterator.md), [FlattenSequence](flattensequence.md), [Iterator](flattensequence/iterator.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [FloatingPointClassification](floatingpointclassification.md), [FloatingPointSign](floatingpointsign.md), [Hasher](hasher.md), [IndexingIterator](indexingiterator.md), [InlineArray](inlinearray.md), [Int](int.md), [Words](int/words-swift.struct.md), [Int128](int128.md), [Int16](int16.md), [Words](int16/words-swift.struct.md), [Int32](int32.md), [Words](int32/words-swift.struct.md), [Int64](int64.md), [Words](int64/words-swift.struct.md), [Int8](int8.md), [Words](int8/words-swift.struct.md), [IteratorSequence](iteratorsequence.md), [JobPriority](jobpriority.md), [JoinedSequence](joinedsequence.md), [Iterator](joinedsequence/iterator.md), [KeyValuePairs](keyvaluepairs.md), [LazyDropWhileSequence](lazydropwhilesequence.md), [Iterator](lazydropwhilesequence/iterator.md), [LazyFilterSequence](lazyfiltersequence.md), [Iterator](lazyfiltersequence/iterator.md), [LazyMapSequence](lazymapsequence.md), [Iterator](lazymapsequence/iterator.md), [LazyPrefixWhileSequence](lazyprefixwhilesequence.md), [Iterator](lazyprefixwhilesequence/iterator.md), [LazySequence](lazysequence.md), [Local](../regexbuilder/local.md), [Lookahead](../regexbuilder/lookahead.md), [Mirror](mirror.md), [NegativeLookahead](../regexbuilder/negativelookahead.md), [Never](never.md), [ObjectIdentifier](objectidentifier.md), [ObservationRegistrar](../observation/observationregistrar.md), [Options](../observation/observationtracking/options.md), [OneOrMore](../regexbuilder/oneormore.md), [OpaquePointer](opaquepointer.md), [Optional](optional.md), [Optionally](../regexbuilder/optionally.md), [PartialRangeFrom](partialrangefrom.md), [Iterator](partialrangefrom/iterator.md), [PartialRangeThrough](partialrangethrough.md), [PartialRangeUpTo](partialrangeupto.md), [PrefixSequence](prefixsequence.md), [Iterator](prefixsequence/iterator.md), [Range](range.md), [RangeSet](rangeset.md), [Ranges](rangeset/ranges-swift.struct.md), [Ref](ref.md), [Repeat](../regexbuilder/repeat.md), [Repeated](repeated.md), [Result](result.md), [ReversedCollection](reversedcollection.md), [Iterator](reversedcollection/iterator.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [Set](set.md), [Iterator](set/iterator.md), [Slice](slice.md), [StaticBigInt](staticbigint.md), [StaticString](staticstring.md), [StrideThrough](stridethrough.md), [StrideThroughIterator](stridethroughiterator.md), [StrideTo](strideto.md), [StrideToIterator](stridetoiterator.md), [String](string.md), [Encoding](string/encoding.md), [Index](string/index.md), [LocalizationValue](string/localizationvalue.md), [UTF16View](string/utf16view.md), [UTF8View](string/utf8view.md), [UnicodeScalarView](string/unicodescalarview.md), [Substring](substring.md), [UTF16View](substring/utf16view.md), [UTF8View](substring/utf8view.md), [UnicodeScalarView](substring/unicodescalarview.md), [SuspendingClock](suspendingclock.md), [Instant](suspendingclock/instant.md), [SystemRandomNumberGenerator](systemrandomnumbergenerator.md), [TaskGroup](taskgroup.md), [TaskPriority](taskpriority.md), [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md), [ThrowingTaskGroup](throwingtaskgroup.md), [TryCapture](../regexbuilder/trycapture.md), [UInt](uint.md), [Words](uint/words-swift.struct.md), [UInt128](uint128.md), [Words](uint128/words-swift.struct.md), [UInt16](uint16.md), [Words](uint16/words-swift.struct.md), [UInt32](uint32.md), [Words](uint32/words-swift.struct.md), [UInt64](uint64.md), [Words](uint64/words-swift.struct.md), [UInt8](uint8.md), [Words](uint8/words-swift.struct.md), [UnicodeScalarIterator](utf8span/unicodescalariterator.md), [UnboundedRange_](unboundedrange_.md), [ASCII](unicode/ascii.md), [Parser](unicode/ascii/parser.md), [Scalar](unicode/scalar.md), [UTF16View](unicode/scalar/utf16view.md), [UTF8View](unicode/scalar/utf8view.md), [UTF16](unicode/utf16.md), [ForwardParser](unicode/utf16/forwardparser.md), [ReverseParser](unicode/utf16/reverseparser.md), [UTF32](unicode/utf32.md), [Parser](unicode/utf32/parser.md), [UTF8](unicode/utf8.md), [ForwardParser](unicode/utf8/forwardparser.md), [ReverseParser](unicode/utf8/reverseparser.md), [ValidationError](unicode/utf8/validationerror.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md), [UnicodeDecodingResult](unicodedecodingresult.md), [Unmanaged](unmanaged.md), [UnownedJob](unownedjob.md), [UnownedSerialExecutor](unownedserialexecutor.md), [UnownedTaskExecutor](unownedtaskexecutor.md), [UnsafeBufferPointer](unsafebufferpointer.md), [Iterator](unsafebufferpointer/iterator.md), [UnsafeContinuation](unsafecontinuation.md), [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawBufferPointer](unsaferawbufferpointer.md), [Iterator](unsaferawbufferpointer/iterator.md), [UnsafeRawPointer](unsaferawpointer.md), [WordPair](../synchronization/wordpair.md), [ZeroOrMore](../regexbuilder/zeroormore.md), [Zip2Sequence](zip2sequence.md), [Iterator](zip2sequence/iterator.md)

## See Also

### Copying

- [BitwiseCopyable](bitwisecopyable.md)
- [Escapable](escapable.md) — A type whose values can persist beyond their immediate local scope.
