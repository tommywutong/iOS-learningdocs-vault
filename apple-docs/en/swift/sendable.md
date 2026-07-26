---
title: Sendable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/sendable
source_url: 'https://developer.apple.com/documentation/swift/sendable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sendable.json'
content_hash: 'sha256:0bcd4cd52002a9cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# Sendable

<sub>Protocol</sub>

A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol Sendable : SendableMetatype
```

## Overview

Values of the type may have no shared mutable state, or they may protect that state with a lock or by forcing it to only be accessed from a specific actor.

You can safely pass values of a sendable type from one concurrency domain to another — for example, you can pass a sendable value as the argument when calling an actor’s methods. All of the following can be marked as sendable:

- Value types
- Reference types with no mutable storage
- Reference types that internally manage access to their state
- Functions and closures (by marking them with `@Sendable`)

Although this protocol doesn’t have any required methods or properties, it does have semantic requirements that are enforced at compile time. These requirements are listed in the sections below. Conformance to `Sendable` must be declared in the same file as the type’s declaration.

To declare conformance to `Sendable` without any compiler enforcement, write `@unchecked Sendable`. You are responsible for the correctness of unchecked sendable types, for example, by protecting all access to its state with a lock or a queue. Unchecked conformance to `Sendable` also disables enforcement of the rule that conformance must be in the same file.

For information about the language-level concurrency model that `Task` is part of, see [Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/).

### Sendable Structures and Enumerations

To satisfy the requirements of the `Sendable` protocol, an enumeration or structure must have only sendable members and associated values. In some cases, structures and enumerations that satisfy the requirements implicitly conform to `Sendable`:

- Frozen structures and enumerations
- Structures and enumerations that aren’t public and aren’t marked `@usableFromInline`.

Otherwise, you need to declare conformance to `Sendable` explicitly.

Structures that have nonsendable stored properties and enumerations that have nonsendable associated values can be marked as `@unchecked Sendable`, disabling compile-time correctness checks, after you manually verify that they satisfy the `Sendable` protocol’s semantic requirements.

### Sendable Actors

All actor types implicitly conform to `Sendable` because actors ensure that all access to their mutable state is performed sequentially.

### Sendable Classes

To satisfy the requirements of the `Sendable` protocol, a class must:

- Be marked `final`
- Contain only stored properties that are immutable and sendable
- Have no superclass or have `NSObject` as the superclass

Classes marked with `@MainActor` are implicitly sendable, because the main actor coordinates all access to its state. These classes can have stored properties that are mutable and nonsendable.

Classes that don’t meet the requirements above can be marked as `@unchecked Sendable`, disabling compile-time correctness checks, after you manually verify that they satisfy the `Sendable` protocol’s semantic requirements.

### Sendable Functions and Closures

Instead of conforming to the `Sendable` protocol, you mark sendable functions and closures with the `@Sendable` attribute. Any values that the function or closure captures must be sendable. In addition, sendable closures must use only by-value captures, and the captured values must be of a sendable type.

In a context that expects a sendable closure, a closure that satisfies the requirements implicitly conforms to `Sendable` — for example, in a call to `Task.detached(priority:operation:)`.

You can explicitly mark a closure as sendable by writing `@Sendable` as part of a type annotation, or by writing `@Sendable` before the closure’s parameters — for example:

```swift
let sendableClosure = { @Sendable (number: Int) -> String in
    if number > 12 {
        return "More than a dozen."
    } else {
        return "Less than a dozen"
    }
}
```

### Sendable Tuples

To satisfy the requirements of the `Sendable` protocol, all of the elements of the tuple must be sendable. Tuples that satisfy the requirements implicitly conform to `Sendable`.

### Sendable Metatypes

Metatypes such as `Int.Type` implicitly conform to the `Sendable` protocol.

## Relationships

- **Inherits From**: [SendableMetatype](sendablemetatype.md)

- **Inherited By**: [Actor](actor.md), [Clock](clock.md), [CodingKey](codingkey.md), [DistributedActor](../distributed/distributedactor.md), [DistributedActorSystem](../distributed/distributedactorsystem.md), [DistributedActorSystemError](../distributed/distributedactorsystemerror.md), [DurationProtocol](durationprotocol.md), [Error](error.md), [Executor](executor.md), [InstantProtocol](instantprotocol.md), [SerialExecutor](serialexecutor.md), [TaskExecutor](taskexecutor.md), [UnsafeSendable](unsafesendable.md)

- **Conforming Types**: [Array](array.md), [ArraySlice](arrayslice.md), [AsyncCompactMapSequence](asynccompactmapsequence.md), [Iterator](asynccompactmapsequence/iterator.md), [AsyncDropFirstSequence](asyncdropfirstsequence.md), [Iterator](asyncdropfirstsequence/iterator.md), [AsyncDropWhileSequence](asyncdropwhilesequence.md), [Iterator](asyncdropwhilesequence/iterator.md), [AsyncFilterSequence](asyncfiltersequence.md), [Iterator](asyncfiltersequence/iterator.md), [AsyncFlatMapSequence](asyncflatmapsequence.md), [Iterator](asyncflatmapsequence/iterator.md), [AsyncMapSequence](asyncmapsequence.md), [Iterator](asyncmapsequence/iterator.md), [AsyncPrefixSequence](asyncprefixsequence.md), [Iterator](asyncprefixsequence/iterator.md), [AsyncPrefixWhileSequence](asyncprefixwhilesequence.md), [Iterator](asyncprefixwhilesequence/iterator.md), [AsyncStream](asyncstream.md), [Continuation](asyncstream/continuation.md), [BufferingPolicy](asyncstream/continuation/bufferingpolicy.md), [Termination](asyncstream/continuation/termination.md), [YieldResult](asyncstream/continuation/yieldresult.md), [AsyncThrowingCompactMapSequence](asyncthrowingcompactmapsequence.md), [Iterator](asyncthrowingcompactmapsequence/iterator.md), [AsyncThrowingDropWhileSequence](asyncthrowingdropwhilesequence.md), [Iterator](asyncthrowingdropwhilesequence/iterator.md), [AsyncThrowingFilterSequence](asyncthrowingfiltersequence.md), [Iterator](asyncthrowingfiltersequence/iterator.md), [AsyncThrowingFlatMapSequence](asyncthrowingflatmapsequence.md), [Iterator](asyncthrowingflatmapsequence/iterator.md), [AsyncThrowingMapSequence](asyncthrowingmapsequence.md), [Iterator](asyncthrowingmapsequence/iterator.md), [AsyncThrowingPrefixWhileSequence](asyncthrowingprefixwhilesequence.md), [Iterator](asyncthrowingprefixwhilesequence/iterator.md), [AsyncThrowingStream](asyncthrowingstream.md), [Continuation](asyncthrowingstream/continuation.md), [BufferingPolicy](asyncthrowingstream/continuation/bufferingpolicy.md), [Termination](asyncthrowingstream/continuation/termination.md), [YieldResult](asyncthrowingstream/continuation/yieldresult.md), [Atomic](../synchronization/atomic.md), [AtomicLazyReference](../synchronization/atomiclazyreference.md), [AtomicLoadOrdering](../synchronization/atomicloadordering.md), [AtomicStoreOrdering](../synchronization/atomicstoreordering.md), [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md), [Bool](bool.md), [ByteOrder](byteorder.md), [CancellationError](cancellationerror.md), [Character](character.md), [CheckedContinuation](checkedcontinuation.md), [ClosedRange](closedrange.md), [Index](closedrange/index.md), [CodingUserInfoKey](codinguserinfokey.md), [CollectionDifference](collectiondifference.md), [Change](collectiondifference/change.md), [Index](collectiondifference/index.md), [CollectionOfOne](collectionofone.md), [Iterator](collectionofone/iterator.md), [CommandLine](commandline.md), [ContiguousArray](contiguousarray.md), [Continuation](continuation.md), [ContinuousClock](continuousclock.md), [Instant](continuousclock/instant.md), [DecodingError](decodingerror.md), [Context](decodingerror/context.md), [DefaultIndices](defaultindices.md), [DefaultStringInterpolation](defaultstringinterpolation.md), [Dictionary](dictionary.md), [Index](dictionary/index.md), [Iterator](dictionary/iterator.md), [Keys](dictionary/keys-swift.struct.md), [Iterator](dictionary/keys-swift.struct/iterator.md), [Values](dictionary/values-swift.struct.md), [Iterator](dictionary/values-swift.struct/iterator.md), [DiscontiguousSlice](discontiguousslice.md), [Index](discontiguousslice/index.md), [DistributedActorCodingError](../distributed/distributedactorcodingerror.md), [Double](double.md), [SIMD16Storage](double/simd16storage.md), [SIMD2Storage](double/simd2storage.md), [SIMD32Storage](double/simd32storage.md), [SIMD4Storage](double/simd4storage.md), [SIMD64Storage](double/simd64storage.md), [SIMD8Storage](double/simd8storage.md), [DropFirstSequence](dropfirstsequence.md), [DropWhileSequence](dropwhilesequence.md), [Iterator](dropwhilesequence/iterator.md), [Duration](duration.md), [TimeFormatStyle](duration/timeformatstyle.md), [Attributed](duration/timeformatstyle/attributed-swift.struct.md), [Pattern](duration/timeformatstyle/pattern-swift.struct.md), [UnitsFormatStyle](duration/unitsformatstyle.md), [Attributed](duration/unitsformatstyle/attributed-swift.struct.md), [FractionalPartDisplayStrategy](duration/unitsformatstyle/fractionalpartdisplaystrategy.md), [Unit](duration/unitsformatstyle/unit.md), [UnitWidth](duration/unitsformatstyle/unitwidth-swift.struct.md), [ZeroValueUnitsDisplayStrategy](duration/unitsformatstyle/zerovalueunitsdisplaystrategy.md), [EmptyCollection](emptycollection.md), [Iterator](emptycollection/iterator.md), [EncodingError](encodingerror.md), [Context](encodingerror/context.md), [EnumeratedSequence](enumeratedsequence.md), [Iterator](enumeratedsequence/iterator.md), [ExecuteDistributedTargetError](../distributed/executedistributedtargeterror.md), [ExecutorJob](executorjob.md), [FlattenSequence](flattensequence.md), [Index](flattensequence/index.md), [Iterator](flattensequence/iterator.md), [Float](float.md), [SIMD16Storage](float/simd16storage.md), [SIMD2Storage](float/simd2storage.md), [SIMD32Storage](float/simd32storage.md), [SIMD4Storage](float/simd4storage.md), [SIMD64Storage](float/simd64storage.md), [SIMD8Storage](float/simd8storage.md), [Float16](float16.md), [SIMD16Storage](float16/simd16storage.md), [SIMD2Storage](float16/simd2storage.md), [SIMD32Storage](float16/simd32storage.md), [SIMD4Storage](float16/simd4storage.md), [SIMD64Storage](float16/simd64storage.md), [SIMD8Storage](float16/simd8storage.md), [Float80](float80.md), [FloatingPointClassification](floatingpointclassification.md), [FloatingPointRoundingRule](floatingpointroundingrule.md), [FloatingPointSign](floatingpointsign.md), [Hasher](hasher.md), [IndexingIterator](indexingiterator.md), [InlineArray](inlinearray.md), [Int](int.md), [SIMD16Storage](int/simd16storage.md), [SIMD2Storage](int/simd2storage.md), [SIMD32Storage](int/simd32storage.md), [SIMD4Storage](int/simd4storage.md), [SIMD64Storage](int/simd64storage.md), [SIMD8Storage](int/simd8storage.md), [Words](int/words-swift.struct.md), [Int128](int128.md), [Int16](int16.md), [SIMD16Storage](int16/simd16storage.md), [SIMD2Storage](int16/simd2storage.md), [SIMD32Storage](int16/simd32storage.md), [SIMD4Storage](int16/simd4storage.md), [SIMD64Storage](int16/simd64storage.md), [SIMD8Storage](int16/simd8storage.md), [Words](int16/words-swift.struct.md), [Int32](int32.md), [SIMD16Storage](int32/simd16storage.md), [SIMD2Storage](int32/simd2storage.md), [SIMD32Storage](int32/simd32storage.md), [SIMD4Storage](int32/simd4storage.md), [SIMD64Storage](int32/simd64storage.md), [SIMD8Storage](int32/simd8storage.md), [Words](int32/words-swift.struct.md), [Int64](int64.md), [SIMD16Storage](int64/simd16storage.md), [SIMD2Storage](int64/simd2storage.md), [SIMD32Storage](int64/simd32storage.md), [SIMD4Storage](int64/simd4storage.md), [SIMD64Storage](int64/simd64storage.md), [SIMD8Storage](int64/simd8storage.md), [Words](int64/words-swift.struct.md), [Int8](int8.md), [SIMD16Storage](int8/simd16storage.md), [SIMD2Storage](int8/simd2storage.md), [SIMD32Storage](int8/simd32storage.md), [SIMD4Storage](int8/simd4storage.md), [SIMD64Storage](int8/simd64storage.md), [SIMD8Storage](int8/simd8storage.md), [Words](int8/words-swift.struct.md), [IteratorSequence](iteratorsequence.md), [Job](job.md), [JobPriority](jobpriority.md), [JoinedSequence](joinedsequence.md), [Iterator](joinedsequence/iterator.md), [KeyValuePairs](keyvaluepairs.md), [Index](lazyprefixwhilesequence/index.md), [LazySequence](lazysequence.md), [LocalTestingActorID](../distributed/localtestingactorid.md), [LocalTestingDistributedActorSystem](../distributed/localtestingdistributedactorsystem.md), [LocalTestingDistributedActorSystemError](../distributed/localtestingdistributedactorsystemerror.md), [MainActor](mainactor.md), [MemoryLayout](memorylayout.md), [DisplayStyle](mirror/displaystyle-swift.enum.md), [MutableRawSpan](mutablerawspan.md), [MutableRef](mutableref.md), [MutableSpan](mutablespan.md), [Mutex](../synchronization/mutex.md), [Never](never.md), [ObjectIdentifier](objectidentifier.md), [ObservationRegistrar](../observation/observationregistrar.md), [ObservationTracking](../observation/observationtracking.md), [Kind](../observation/observationtracking/event/kind-swift.struct.md), [Options](../observation/observationtracking/options.md), [Observations](../observation/observations.md), [Iteration](../observation/observations/iteration.md), [Optional](optional.md), [OutputRawSpan](outputrawspan.md), [OutputSpan](outputspan.md), [PartialRangeFrom](partialrangefrom.md), [Iterator](partialrangefrom/iterator.md), [PartialRangeThrough](partialrangethrough.md), [PartialRangeUpTo](partialrangeupto.md), [PrefixSequence](prefixsequence.md), [Iterator](prefixsequence/iterator.md), [Range](range.md), [RangeSet](rangeset.md), [Ranges](rangeset/ranges-swift.struct.md), [RawSpan](rawspan.md), [Ref](ref.md), [Repeated](repeated.md), [Result](result.md), [ReversedCollection](reversedcollection.md), [Index](reversedcollection/index.md), [Iterator](reversedcollection/iterator.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [SIMDMask](simdmask.md), [Set](set.md), [Index](set/index.md), [Iterator](set/iterator.md), [Slice](slice.md), [Span](span.md), [StaticBigInt](staticbigint.md), [StaticString](staticstring.md), [StrideThrough](stridethrough.md), [StrideThroughIterator](stridethroughiterator.md), [StrideTo](strideto.md), [StrideToIterator](stridetoiterator.md), [String](string.md), [Comparator](string/comparator.md), [Encoding](string/encoding.md), [Index](string/index.md), [Iterator](string/iterator.md), [LocalizationValue](string/localizationvalue.md), [Placeholder](string/localizationvalue/placeholder.md), [StandardComparator](string/standardcomparator.md), [UTF16View](string/utf16view.md), [Iterator](string/utf16view/iterator.md), [UTF8View](string/utf8view.md), [UnicodeScalarView](string/unicodescalarview.md), [Iterator](string/unicodescalarview/iterator.md), [Substring](substring.md), [UTF16View](substring/utf16view.md), [UTF8View](substring/utf8view.md), [UnicodeScalarView](substring/unicodescalarview.md), [SuspendingClock](suspendingclock.md), [Instant](suspendingclock/instant.md), [SystemRandomNumberGenerator](systemrandomnumbergenerator.md), [Task](task.md), [TaskLocal](tasklocal.md), [TaskPriority](taskpriority.md), [UInt](uint.md), [SIMD16Storage](uint/simd16storage.md), [SIMD2Storage](uint/simd2storage.md), [SIMD32Storage](uint/simd32storage.md), [SIMD4Storage](uint/simd4storage.md), [SIMD64Storage](uint/simd64storage.md), [SIMD8Storage](uint/simd8storage.md), [Words](uint/words-swift.struct.md), [UInt128](uint128.md), [Words](uint128/words-swift.struct.md), [UInt16](uint16.md), [SIMD16Storage](uint16/simd16storage.md), [SIMD2Storage](uint16/simd2storage.md), [SIMD32Storage](uint16/simd32storage.md), [SIMD4Storage](uint16/simd4storage.md), [SIMD64Storage](uint16/simd64storage.md), [SIMD8Storage](uint16/simd8storage.md), [Words](uint16/words-swift.struct.md), [UInt32](uint32.md), [SIMD16Storage](uint32/simd16storage.md), [SIMD2Storage](uint32/simd2storage.md), [SIMD32Storage](uint32/simd32storage.md), [SIMD4Storage](uint32/simd4storage.md), [SIMD64Storage](uint32/simd64storage.md), [SIMD8Storage](uint32/simd8storage.md), [Words](uint32/words-swift.struct.md), [UInt64](uint64.md), [SIMD16Storage](uint64/simd16storage.md), [SIMD2Storage](uint64/simd2storage.md), [SIMD32Storage](uint64/simd32storage.md), [SIMD4Storage](uint64/simd4storage.md), [SIMD64Storage](uint64/simd64storage.md), [SIMD8Storage](uint64/simd8storage.md), [Words](uint64/words-swift.struct.md), [UInt8](uint8.md), [SIMD16Storage](uint8/simd16storage.md), [SIMD2Storage](uint8/simd2storage.md), [SIMD32Storage](uint8/simd32storage.md), [SIMD4Storage](uint8/simd4storage.md), [SIMD64Storage](uint8/simd64storage.md), [SIMD8Storage](uint8/simd8storage.md), [Words](uint8/words-swift.struct.md), [UnboundedRange_](unboundedrange_.md), [UnfoldSequence](unfoldsequence.md), [Unicode](unicode.md), [ASCII](unicode/ascii.md), [Parser](unicode/ascii/parser.md), [CanonicalCombiningClass](unicode/canonicalcombiningclass.md), [GeneralCategory](unicode/generalcategory.md), [NumericType](unicode/numerictype.md), [ParseResult](unicode/parseresult.md), [Scalar](unicode/scalar.md), [Properties](unicode/scalar/properties-swift.struct.md), [UTF16View](unicode/scalar/utf16view.md), [UTF8View](unicode/scalar/utf8view.md), [UTF16](unicode/utf16.md), [ForwardParser](unicode/utf16/forwardparser.md), [ReverseParser](unicode/utf16/reverseparser.md), [UTF32](unicode/utf32.md), [Parser](unicode/utf32/parser.md), [UTF8](unicode/utf8.md), [ForwardParser](unicode/utf8/forwardparser.md), [ReverseParser](unicode/utf8/reverseparser.md), [ValidationError](unicode/utf8/validationerror.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md), [UnicodeDecodingResult](unicodedecodingresult.md), [UniqueArray](uniquearray.md), [UniqueBox](uniquebox.md), [Unmanaged](unmanaged.md), [UnownedJob](unownedjob.md), [UnownedSerialExecutor](unownedserialexecutor.md), [UnownedTaskExecutor](unownedtaskexecutor.md), [UnsafeContinuation](unsafecontinuation.md), [WordPair](../synchronization/wordpair.md), [Zip2Sequence](zip2sequence.md), [Iterator](zip2sequence/iterator.md)

## See Also

### Actors

- [Actor](actor.md) — Common protocol to which all actors conform.
- [MainActor](mainactor.md) — A singleton actor whose executor is equivalent to the main dispatch queue.
- [GlobalActor](globalactor.md) — A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [SendableMetatype](sendablemetatype.md) — A type whose metatype can be shared across arbitrary isolation domains without introducing a risk of data races.
- [isolation()](<isolation().md>) — Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
