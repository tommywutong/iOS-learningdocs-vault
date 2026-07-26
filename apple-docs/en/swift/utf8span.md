---
title: UTF8Span
framework: Swift
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span
source_url: 'https://developer.apple.com/documentation/swift/utf8span'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span.json'
content_hash: 'sha256:39dd9df608600c31'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# UTF8Span

<sub>Structure</sub>

A borrowed view into contiguous memory that contains validly-encoded UTF-8 code units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct UTF8Span
```

## Relationships

- **Conforms To**: [BitwiseCopyable](bitwisecopyable.md), [ContiguousBytes](../foundation/contiguousbytes.md)

## Topics

### Structures

- [CharacterIterator](utf8span/characteriterator.md) — Iterate the `Character` contents of a `UTF8Span`.
- [UnicodeScalarIterator](utf8span/unicodescalariterator.md) — Iterate the `Unicode.Scalar`s contents of a `UTF8Span`.

### Initializers

- [init(unchecked:isKnownASCII:)](<utf8span/init(unchecked_isknownascii_).md>) — Creates a UTF8Span, bypassing safety and security checks. The caller must guarantee that `codeUnits` contains validly-encoded UTF-8, or else undefined behavior may result upon use. If `isKnownASCII: true is passed`, the contents must be ASCII, or else undefined behavior may result upon use.
- [init(validating:)](<utf8span/init(validating_).md>) — Creates a UTF8Span containing `codeUnits`. Validates that the input is valid UTF-8, otherwise throws an error.

### Instance Properties

- [count](utf8span/count.md) — The number of UTF-8 code units in the span.
- [isEmpty](utf8span/isempty.md) — A Boolean value that indicates whether the UTF-8 span is empty.
- [isKnownASCII](utf8span/isknownascii.md) — Returns whether contents are known to be all-ASCII. A return value of `true` means that all code units are ASCII. A return value of `false` means there _may_ be non-ASCII content.
- [isKnownNFC](utf8span/isknownnfc.md) — Returns whether the contents are known to be NFC. This is not always checked at initialization time and is set by `checkForNFC`.
- [span](utf8span/span.md) — A span used to access the code units.

### Instance Methods

- [bytesEqual(to:)](<utf8span/bytesequal(to_).md>) — Whether this span has the same bytes as `other`.
- [charactersEqual(to:)](<utf8span/charactersequal(to_).md>) — Whether this span has the same `Character`s as `other`.
- [checkForASCII()](<utf8span/checkforascii().md>) — Do a scan checking for whether the contents are all-ASCII.
- [checkForNFC(quickCheck:)](<utf8span/checkfornfc(quickcheck_).md>) — Do a scan checking for whether the contents are in Normal Form C. When the contents are in NFC, canonical equivalence checks are much faster.
- [isCanonicallyEquivalent(to:)](<utf8span/iscanonicallyequivalent(to_).md>) — Whether `self` is equivalent to `other` under Unicode Canonical Equivalence.
- [isCanonicallyLessThan(_:)](<utf8span/iscanonicallylessthan(__).md>) — Whether `self` orders less than `other` under Unicode Canonical Equivalence using normalized code-unit order (in NFC).
- [isTriviallyIdentical(to:)](<utf8span/istriviallyidentical(to_).md>) — Returns a Boolean value indicating whether two instances refer to the same memory region, and have the same flags (such as [isKnownASCII](utf8span/isknownascii.md)).
- [makeCharacterIterator()](<utf8span/makecharacteriterator().md>) — Returns an iterator that will construct `Character`s from the underlying UTF-8 content.
- [makeUnicodeScalarIterator()](<utf8span/makeunicodescalariterator().md>) — Returns an iterator that will decode the code units into `Unicode.Scalar`s.
- [unicodeScalarsEqual(to:)](<utf8span/unicodescalarsequal(to_).md>) — Whether this span has the same `Unicode.Scalar`s as `other`.

## See Also

### Safe Memory Access

- [Span](span.md) — `Span<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [RawSpan](rawspan.md) — `RawSpan` represents a contiguous region of memory which contains initialized bytes.
- [OutputSpan](outputspan.md) — `OutputSpan` is a reference to a contiguous region of memory that starts with some number of initialized `Element` instances followed by uninitialized memory. It provides operations to access the items it stores, as well as to add new elements and to remove existing ones.
- [OutputRawSpan](outputrawspan.md) — `OutputRawSpan` is a reference to a contiguous region of memory which starts with some number of initialized bytes, followed by uninitialized memory. It provides operations to access the bytes it stores, as well as to append and to remove bytes.
- [MutableSpan](mutablespan.md) — `MutableSpan<Element>` represents a contiguous region of memory which contains initialized instances of `Element`.
- [MutableRawSpan](mutablerawspan.md) — `MutableRawSpan` represents a contiguous region of memory which contains initialized bytes.
- [SpanIterator](spaniterator.md) _(beta)_
