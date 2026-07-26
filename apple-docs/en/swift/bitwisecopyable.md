---
title: BitwiseCopyable
framework: Swift
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/bitwisecopyable
source_url: 'https://developer.apple.com/documentation/swift/bitwisecopyable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/bitwisecopyable.json'
content_hash: 'sha256:4ef0f28e998e1e1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# BitwiseCopyable

<sub>Protocol</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol BitwiseCopyable : ~Escapable
```

## Relationships

- **Inherited By**: [ConvertibleFromBytes](convertiblefrombytes.md), [SIMDScalar](simdscalar.md)

- **Conforming Types**: [AtomicLoadOrdering](../synchronization/atomicloadordering.md), [AtomicStoreOrdering](../synchronization/atomicstoreordering.md), [AtomicUpdateOrdering](../synchronization/atomicupdateordering.md), [AutoreleasingUnsafeMutablePointer](autoreleasingunsafemutablepointer.md), [Bool](bool.md), [ByteOrder](byteorder.md), [CVaListPointer](cvalistpointer.md), [Index](collectiondifference/index.md), [CollectionOfOne](collectionofone.md), [DiscardingTaskGroup](discardingtaskgroup.md), [Double](double.md), [SIMD16Storage](double/simd16storage.md), [SIMD2Storage](double/simd2storage.md), [SIMD32Storage](double/simd32storage.md), [SIMD4Storage](double/simd4storage.md), [SIMD64Storage](double/simd64storage.md), [SIMD8Storage](double/simd8storage.md), [Duration](duration.md), [EmptyCollection](emptycollection.md), [Iterator](emptycollection/iterator.md), [Float](float.md), [SIMD16Storage](float/simd16storage.md), [SIMD2Storage](float/simd2storage.md), [SIMD32Storage](float/simd32storage.md), [SIMD4Storage](float/simd4storage.md), [SIMD64Storage](float/simd64storage.md), [SIMD8Storage](float/simd8storage.md), [Float16](float16.md), [SIMD16Storage](float16/simd16storage.md), [SIMD2Storage](float16/simd2storage.md), [SIMD32Storage](float16/simd32storage.md), [SIMD4Storage](float16/simd4storage.md), [SIMD64Storage](float16/simd64storage.md), [SIMD8Storage](float16/simd8storage.md), [Float80](float80.md), [FloatingPointClassification](floatingpointclassification.md), [FloatingPointSign](floatingpointsign.md), [Hasher](hasher.md), [InlineArray](inlinearray.md), [Int](int.md), [SIMD16Storage](int/simd16storage.md), [SIMD2Storage](int/simd2storage.md), [SIMD32Storage](int/simd32storage.md), [SIMD4Storage](int/simd4storage.md), [SIMD64Storage](int/simd64storage.md), [SIMD8Storage](int/simd8storage.md), [Words](int/words-swift.struct.md), [Int128](int128.md), [Int16](int16.md), [SIMD16Storage](int16/simd16storage.md), [SIMD2Storage](int16/simd2storage.md), [SIMD32Storage](int16/simd32storage.md), [SIMD4Storage](int16/simd4storage.md), [SIMD64Storage](int16/simd64storage.md), [SIMD8Storage](int16/simd8storage.md), [Words](int16/words-swift.struct.md), [Int32](int32.md), [SIMD16Storage](int32/simd16storage.md), [SIMD2Storage](int32/simd2storage.md), [SIMD32Storage](int32/simd32storage.md), [SIMD4Storage](int32/simd4storage.md), [SIMD64Storage](int32/simd64storage.md), [SIMD8Storage](int32/simd8storage.md), [Words](int32/words-swift.struct.md), [Int64](int64.md), [SIMD16Storage](int64/simd16storage.md), [SIMD2Storage](int64/simd2storage.md), [SIMD32Storage](int64/simd32storage.md), [SIMD4Storage](int64/simd4storage.md), [SIMD64Storage](int64/simd64storage.md), [SIMD8Storage](int64/simd8storage.md), [Words](int64/words-swift.struct.md), [Int8](int8.md), [SIMD16Storage](int8/simd16storage.md), [SIMD2Storage](int8/simd2storage.md), [SIMD32Storage](int8/simd32storage.md), [SIMD4Storage](int8/simd4storage.md), [SIMD64Storage](int8/simd64storage.md), [SIMD8Storage](int8/simd8storage.md), [Words](int8/words-swift.struct.md), [JobPriority](jobpriority.md), [Never](never.md), [ObjectIdentifier](objectidentifier.md), [OpaquePointer](opaquepointer.md), [Optional](optional.md), [PartialRangeFrom](partialrangefrom.md), [Iterator](partialrangefrom/iterator.md), [PartialRangeThrough](partialrangethrough.md), [PartialRangeUpTo](partialrangeupto.md), [RawSpan](rawspan.md), [Ref](ref.md), [SIMD16](simd16.md), [SIMD2](simd2.md), [SIMD3](simd3.md), [SIMD32](simd32.md), [SIMD4](simd4.md), [SIMD64](simd64.md), [SIMD8](simd8.md), [Span](span.md), [StaticBigInt](staticbigint.md), [StaticString](staticstring.md), [Index](string/index.md), [SystemRandomNumberGenerator](systemrandomnumbergenerator.md), [TaskGroup](taskgroup.md), [ThrowingDiscardingTaskGroup](throwingdiscardingtaskgroup.md), [ThrowingTaskGroup](throwingtaskgroup.md), [UInt](uint.md), [SIMD16Storage](uint/simd16storage.md), [SIMD2Storage](uint/simd2storage.md), [SIMD32Storage](uint/simd32storage.md), [SIMD4Storage](uint/simd4storage.md), [SIMD64Storage](uint/simd64storage.md), [SIMD8Storage](uint/simd8storage.md), [Words](uint/words-swift.struct.md), [UInt128](uint128.md), [Words](uint128/words-swift.struct.md), [UInt16](uint16.md), [SIMD16Storage](uint16/simd16storage.md), [SIMD2Storage](uint16/simd2storage.md), [SIMD32Storage](uint16/simd32storage.md), [SIMD4Storage](uint16/simd4storage.md), [SIMD64Storage](uint16/simd64storage.md), [SIMD8Storage](uint16/simd8storage.md), [Words](uint16/words-swift.struct.md), [UInt32](uint32.md), [SIMD16Storage](uint32/simd16storage.md), [SIMD2Storage](uint32/simd2storage.md), [SIMD32Storage](uint32/simd32storage.md), [SIMD4Storage](uint32/simd4storage.md), [SIMD64Storage](uint32/simd64storage.md), [SIMD8Storage](uint32/simd8storage.md), [Words](uint32/words-swift.struct.md), [UInt64](uint64.md), [SIMD16Storage](uint64/simd16storage.md), [SIMD2Storage](uint64/simd2storage.md), [SIMD32Storage](uint64/simd32storage.md), [SIMD4Storage](uint64/simd4storage.md), [SIMD64Storage](uint64/simd64storage.md), [SIMD8Storage](uint64/simd8storage.md), [Words](uint64/words-swift.struct.md), [UInt8](uint8.md), [SIMD16Storage](uint8/simd16storage.md), [SIMD2Storage](uint8/simd2storage.md), [SIMD32Storage](uint8/simd32storage.md), [SIMD4Storage](uint8/simd4storage.md), [SIMD64Storage](uint8/simd64storage.md), [SIMD8Storage](uint8/simd8storage.md), [Words](uint8/words-swift.struct.md), [UTF8Span](utf8span.md), [UnicodeScalarIterator](utf8span/unicodescalariterator.md), [UnboundedRange_](unboundedrange_.md), [ASCII](unicode/ascii.md), [Parser](unicode/ascii/parser.md), [Scalar](unicode/scalar.md), [UTF16View](unicode/scalar/utf16view.md), [UTF8View](unicode/scalar/utf8view.md), [UTF16](unicode/utf16.md), [ForwardParser](unicode/utf16/forwardparser.md), [ReverseParser](unicode/utf16/reverseparser.md), [UTF32](unicode/utf32.md), [Parser](unicode/utf32/parser.md), [UTF8](unicode/utf8.md), [ForwardParser](unicode/utf8/forwardparser.md), [ReverseParser](unicode/utf8/reverseparser.md), [Kind](unicode/utf8/validationerror/kind-swift.struct.md), [UnicodeDecodingResult](unicodedecodingresult.md), [Unmanaged](unmanaged.md), [UnownedJob](unownedjob.md), [UnownedSerialExecutor](unownedserialexecutor.md), [UnownedTaskExecutor](unownedtaskexecutor.md), [UnsafeBufferPointer](unsafebufferpointer.md), [UnsafeContinuation](unsafecontinuation.md), [UnsafeMutableBufferPointer](unsafemutablebufferpointer.md), [UnsafeMutablePointer](unsafemutablepointer.md), [UnsafeMutableRawBufferPointer](unsafemutablerawbufferpointer.md), [UnsafeMutableRawPointer](unsafemutablerawpointer.md), [UnsafePointer](unsafepointer.md), [UnsafeRawBufferPointer](unsaferawbufferpointer.md), [Iterator](unsaferawbufferpointer/iterator.md), [UnsafeRawPointer](unsaferawpointer.md), [WordPair](../synchronization/wordpair.md)

## See Also

### Copying

- [Copyable](copyable.md) — A type whose values can be implicitly or explicitly copied.
- [Escapable](escapable.md) — A type whose values can persist beyond their immediate local scope.
