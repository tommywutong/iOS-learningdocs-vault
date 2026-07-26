---
title: 'CTTypesetterSuggestLineBreakWithOffset(_:_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttypesettersuggestlinebreakwithoffset(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttypesettersuggestlinebreakwithoffset(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttypesettersuggestlinebreakwithoffset%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:1bb6834e46a21182'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTypesetterSuggestLineBreakWithOffset(_:_:_:_:)

<sub>Function</sub>

Suggests a contextual line breakpoint based on the width provided and the specified offset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTypesetterSuggestLineBreakWithOffset(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double, _ offset: Double) -> CFIndex
```

## Parameters

- `typesetter` — The typesetter that creates the line. This parameter is required and cannot be set to `NULL`.

- `startIndex` — The starting point for the line-break calculations. The break calculations include the character starting at `startIndex`.

- `width` — The requested line-break width.

- `offset` — The line position offset.

## Return Value

A count of the characters from `startIndex` and `offset` that would cause the line break. The value returned can be used to construct a character range for [CTTypesetterCreateLine](<cttypesettercreateline(____).md>).

## Discussion

The line break can be triggered either by a hard-break character in the stream or by filling the specified width with characters.

## See Also

### Breaking Lines

- [CTTypesetterSuggestLineBreak](<cttypesettersuggestlinebreak(______).md>) — Suggests a contextual line breakpoint based on the width provided.
- [CTTypesetterSuggestClusterBreak](<cttypesettersuggestclusterbreak(______).md>) — Suggests a cluster line breakpoint based on the width provided.
- [CTTypesetterSuggestClusterBreakWithOffset](<cttypesettersuggestclusterbreakwithoffset(________).md>) — Suggests a cluster line breakpoint based on the specified width and line offset.
