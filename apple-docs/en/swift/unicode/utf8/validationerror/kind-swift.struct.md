---
title: Unicode.UTF8.ValidationError.Kind
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unicode/utf8/validationerror/kind-swift.struct
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8/validationerror/kind-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8/validationerror/kind-swift.struct.json'
content_hash: 'sha256:38600c474103810e'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Swift](../../../../swift.md) · [Unicode](../../../unicode.md) · [UTF8](../../utf8.md) · [ValidationError](../validationerror.md)

# Unicode.UTF8.ValidationError.Kind

<sub>Structure</sub>

The kind of encoding error encountered during validation

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct Kind
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../bitwisecopyable.md), [Copyable](../../../copyable.md), [CustomStringConvertible](../../../customstringconvertible.md), [Equatable](../../../equatable.md), [Error](../../../error.md), [Escapable](../../../escapable.md), [Hashable](../../../hashable.md), [RawRepresentable](../../../rawrepresentable.md), [Sendable](../../../sendable.md), [SendableMetatype](../../../sendablemetatype.md)

## Topics

### Initializers

- [init(rawValue:)](<kind-swift.struct/init(rawvalue_).md>) — Creates a new instance with the specified raw value.

### Instance Properties

- [rawValue](kind-swift.struct/rawvalue-swift.property.md) — The corresponding value of the raw type.

### Type Aliases

- [RawValue](kind-swift.struct/rawvalue-swift.typealias.md) — The raw type that can be used to represent all values of the conforming type.

### Type Properties

- [invalidNonSurrogateCodePointByte](kind-swift.struct/invalidnonsurrogatecodepointbyte.md) — A byte in an invalid, non-surrogate code point (`>U+10FFFF`) sequence
- [overlongEncodingByte](kind-swift.struct/overlongencodingbyte.md) — A byte in an overlong encoding sequence
- [surrogateCodePointByte](kind-swift.struct/surrogatecodepointbyte.md) — A byte in a surrogate code point (`U+D800..U+DFFF`) sequence
- [truncatedScalar](kind-swift.struct/truncatedscalar.md) — A multi-byte sequence that is the start of a valid multi-byte scalar but is cut off before ending correctly
- [unexpectedContinuationByte](kind-swift.struct/unexpectedcontinuationbyte.md) — A continuation byte (`10xxxxxx`) outside of a multi-byte sequence

### Default Implementations

- [CustomStringConvertible Implementations](kind-swift.struct/customstringconvertible-implementations.md)
- [Equatable Implementations](kind-swift.struct/equatable-implementations.md)
- [RawRepresentable Implementations](kind-swift.struct/rawrepresentable-implementations.md)
