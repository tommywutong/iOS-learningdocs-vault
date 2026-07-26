---
title: Escapable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/escapable
source_url: 'https://developer.apple.com/documentation/swift/escapable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/escapable.json'
content_hash: 'sha256:4c00cc28c151646a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Escapable

<sub>Protocol</sub>

A type whose values can persist beyond their immediate local scope.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Escapable
```

## Overview

Escapable values can be assigned to global or static variables, returned from functions, captured by escaping closures, and so on. All Swift types implicitly conform to this protocol by default, allowing them to be moved across scopes freely because they lack any lifetime dependencies.

In contrast, values of types that suppress their implicit conformance to `Escapable` (by writing `~Escapable`) carry a lifetime dependency. These dependencies ensure the `~Escapable` value does not live longer than the value it depends on. Explicit lifetime dependency annotations may be required when working with these types.

In generic contexts, `~Escapable` works much in the same way as `~Copyable`. It allows functions and types to work with values that may or may not be Escapable, and types can be conditionally `Escapable` based on their generic arguments. A conformance requirement for `Escapable` is automatically inferred in extensions and for generic type parameters, unless suppressed with `~Escapable`.

## Relationships

- **Conforming Types**: [Anchor](../regexbuilder/anchor.md), [AnyBidirectionalCollection](anybidirectionalcollection.md), [AnyCollection](anycollection.md), [AnyHashable](anyhashable.md), [AnyIterator](anyiterator.md), [AnyKeyPath](anykeypath.md), [AnyRandomAccessCollection](anyrandomaccesscollection.md), [AnyRegexOutput](anyregexoutput.md), [AnySequence](anysequence.md), [Array](array.md), [ArraySlice](arrayslice.md), [AsyncCompactMapSequence](asynccompactmapsequence.md), [AsyncDropFirstSequence](asyncdropfirstsequence.md), [AsyncDropWhileSequence](asyncdropwhilesequence.md), [AsyncFilterSequence](asyncfiltersequence.md), [AsyncFlatMapSequence](asyncflatmapsequence.md), [AsyncMapSequence](asyncmapsequence.md), [AsyncPrefixSequence](asyncprefixsequence.md), [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md), [AsyncStream](asyncstream.md), [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md), [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md), [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md), [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md), [AsyncThrowingMapSequence](asyncthrowingmapsequence.md), [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md), [AsyncThrowingStream](asyncthrowingstream.md), [AtomicLoadOrdering](../synchronization/atomicloadordering.md), [AtomicStoreOrdering](../synchronization/atomicstoreordering.md), [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [Bool](bool.md), [CVaListPointer](cvalistpointer.md), [Capture](../regexbuilder/capture.md), [Character](character.md), [CharacterClass](../regexbuilder/characterclass.md), [ChoiceOf](../regexbuilder/choiceof.md), [ClosedRange](closedrange.md), [CollectionDifference](collectiondifference.md), [Change](collectiondifference/change.md), [CollectionOfOne](collectionofone.md), [Iterator](collectionofone/iterator.md), [ContiguousArray](contiguousarray.md), [ContinuousClock](continuousclock.md), [Instant](continuousclock/instant.md), [DecodingError](decodingerror.md), [DefaultIndices](defaultindices.md), [DefaultStringInterpolation](defaultstringinterpolation.md), [Dictionary](dictionary.md), [Iterator](dictionary/iterator.md), [Keys](dictionary/keys-swift.struct.md), [Values](dictionary/values-swift.struct.md), [DiscontiguousSlice](discontiguousslice.md), [Index](discontiguousslice/index.md), [Double](double.md), [DropFirstSequence](dropfirstsequence.md), [DropWhileSequence](dropwhilesequence.md), [Iterator](dropwhilesequence/iterator.md), [Duration](duration.md), [TimeFormatStyle](duration/timeformatstyle.md), [Attributed](duration/timeformatstyle/attributed-swift.struct.md), [UnitsFormatStyle](duration/unitsformatstyle.md), [Attributed](duration/unitsformatstyle/attributed-swift.struct.md), [EmptyCollection](emptycollection.md), [Iterator](emptycollection/iterator.md), [EncodingError](encodingerror.md), [EnumeratedSequence](enumeratedsequence.md), [Iterator](enumeratedsequence/iterator.md), [FlattenSequence](flattensequence.md), [Iterator](flattensequence/iterator.md), [Float](float.md), [Float16](float16.md), [Float80](float80.md), [FloatingPointSign](floatingpointsign.md), [IndexingIterator](indexingiterator.md), [InlineArray](inlinearray.md), [Int](int.md), [Int128](int128.md), [Int16](int16.md), [Int32](int32.md), [Int64](int64.md), [Int8](int8.md), [IteratorSequence](iteratorsequence.md), [JoinedSequence](joinedsequence.md), [Iterator](joinedsequence/iterator.md), [KeyValuePairs](keyvaluepairs.md), [LazyDropWhileSequence](lazydropwhilesequence.md), [Iterator](lazydropwhilesequence/iterator.md), [LazyFilterSequence](lazyfiltersequence.md), [Iterator](lazyfiltersequence/iterator.md), [LazyMapSequence](lazymapsequence.md), [Iterator](lazymapsequence/iterator.md), [LazyPrefixWhileSequence](lazyprefixwhilesequence.md), [Iterator](lazyprefixwhilesequence/iterator.md), [LazySequence](lazysequence.md), [Local](../regexbuilder/local.md), [Lookahead](../regexbuilder/lookahead.md), [Mirror](mirror.md), [NegativeLookahead](../regexbuilder/negativelookahead.md), [Never](never.md), [ObjectIdentifier](objectidentifier.md), [ObservationRegistrar](../observation/observationregistrar.md), [Options](../observation/observationtracking/options.md), [OneOrMore](../regexbuilder/oneormore.md), [OpaquePointer](opaquepointer.md), [Optional](optional.md), [Optionally](../regexbuilder/optionally.md), [PartialRangeFrom](partialrangefrom.md), [Iterator](partialrangefrom/iterator.md), [PartialRangeThrough](partialrangethrough.md), [PartialRangeUpTo](partialrangeupto.md), [PrefixSequence](prefixsequence.md), [Iterator](prefixsequence/iterator.md), [Range](range.md), [RangeSet](rangeset.md), [Ranges](rangeset/ranges-swift.struct.md), [Repeat](../regexbuilder/repeat.md), [Repeated](repeated.md), [Result](result.md), [ReversedCollection](reversedcollection.md), [Iterator](reversedcollection/iterator.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [Set](set.md), [Iterator](set/iterator.md), [Slice](slice.md), [StaticBigInt](staticbigint.md), [StaticString](staticstring.md), [StrideThrough](stridethrough.md), [StrideThroughIterator](stridethroughiterator.md), [StrideTo](strideto.md), [StrideToIterator](stridetoiterator.md), [String](string.md), [Encoding](string/encoding.md), [Index](string/index.md), [LocalizationValue](string/localizationvalue.md), [UTF16View](string/utf16view.md), [UTF8View](string/utf8view.md), [UnicodeScalarView](string/unicodescalarview.md), [Substring](substring.md), [UTF16View](substring/utf16view.md), [UTF8View](substring/utf8view.md), [UnicodeScalarView](substring/unicodescalarview.md), [SuspendingClock](suspendingclock.md), [Instant](suspendingclock/instant.md), [TaskGroup](taskgroup.md), [TaskPriority](taskpriority.md), [ThrowingTaskGroup](throwingtaskgroup.md), [TryCapture](../regexbuilder/trycapture.md), [UInt](uint.md), [UInt128](uint128.md), [Words](uint128/words-swift.struct.md), [UInt16](uint16.md), [UInt32](uint32.md), [UInt64](uint64.md), [UInt8](uint8.md), [ASCII](unicode/ascii.md), [Parser](unicode/ascii/parser.md), [Scalar](unicode/scalar.md), [UTF16View](unicode/scalar/utf16view.md), [UTF8View](unicode/scalar/utf8view.md), [UTF16](unicode/utf16.md), [ForwardParser](unicode/utf16/forwardparser.md), [ReverseParser](unicode/utf16/reverseparser.md), [UTF32](unicode/utf32.md), [Parser](unicode/utf32/parser.md), [UTF8](unicode/utf8.md), [ForwardParser](unicode/utf8/forwardparser.md), [ReverseParser](unicode/utf8/reverseparser.md), [ValidationError](unicode/utf8/validationerror.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md), [Unmanaged](unmanaged.md), [UnownedJob](unownedjob.md), [UnsafeBufferPointer](unsafebufferpointer.md), [Iterator](unsafebufferpointer/iterator.md), [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawBufferPointer](unsaferawbufferpointer.md), [Iterator](unsaferawbufferpointer/iterator.md), [UnsafeRawPointer](unsaferawpointer.md), [WordPair](../synchronization/wordpair.md), [ZeroOrMore](../regexbuilder/zeroormore.md), [Zip2Sequence](zip2sequence.md), [Iterator](zip2sequence/iterator.md)

## See Also

### Copying

- [Copyable](copyable.md) — A type whose values can be implicitly or explicitly copied.
- [BitwiseCopyable](bitwisecopyable.md)
