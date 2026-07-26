---
title: 'CFStringTokenizerCreate(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringtokenizercreate(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringtokenizercreate(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringtokenizercreate%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:596f295a77fce002'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringTokenizerCreate(_:_:_:_:_:)

<sub>Function</sub>

Returns a tokenizer for a given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringTokenizerCreate(_ alloc: CFAllocator!, _ string: CFString!, _ range: CFRange, _ options: CFOptionFlags, _ locale: CFLocale!) -> CFStringTokenizer!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new object. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `string` — The string to tokenize.

- `range` — The range of the characters in `string` to tokenize.

- `options` — A tokenization unit option that specifies how `string` should be tokenized. The options can be modified by adding unit modifier options to tell the tokenizer to prepare specified attributes when it tokenizes `string`. For possible values, see [Tokenization Modifiers](1588024-tokenization-modifiers.md).

- `locale` — A locale that specifies language- or region-specific behavior for the tokenization. You can pass `NULL` to use the default system locale, although this is typically not recommended—instead use [CFLocaleCopyCurrent](<cflocalecopycurrent().md>) to specify the locale of the current user. For more information, see [Tokenization Modifiers](1588024-tokenization-modifiers.md).

## Return Value

A tokenizer to analyze the range `range` of `string` for the given locale and options. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).
