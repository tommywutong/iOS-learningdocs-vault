---
title: 'CTTypesetterSuggestClusterBreak(_:_:_:)'
framework: Core Text
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coretext/cttypesettersuggestclusterbreak(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/coretext/cttypesettersuggestclusterbreak(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coretext/cttypesettersuggestclusterbreak%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:3472783f566b9fb3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Text](../coretext.md)

# CTTypesetterSuggestClusterBreak(_:_:_:)

<sub>Function</sub>

Suggests a cluster line breakpoint based on the width provided.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CTTypesetterSuggestClusterBreak(_ typesetter: CTTypesetter, _ startIndex: CFIndex, _ width: Double) -> CFIndex
```

## Parameters

- `typesetter` — The typesetter that creates the line. This parameter is required and cannot be set to `NULL`.

- `startIndex` — The starting point for the typographic cluster-break calculations. The break calculations include the character starting at `startIndex`.

- `width` — The requested typographic cluster-break width.

## Return Value

A count of the characters from `startIndex` that would cause the cluster break. The value returned can be used to construct a character range for [CTTypesetterCreateLine](<cttypesettercreateline(____).md>).

## Discussion

This cluster break is similar to a character break, except that it does not break apart linguistic clusters. No other contextual analysis is done. This can be used by the caller to implement a different line-breaking scheme, such as hyphenation. A typographic cluster break can also be triggered by a hard-break character in the stream. This function is equivalent to [CTTypesetterSuggestClusterBreakWithOffset](<cttypesettersuggestclusterbreakwithoffset(________).md>) with an offset of 0.0.

## See Also

### Breaking Lines

- [CTTypesetterSuggestLineBreak](<cttypesettersuggestlinebreak(______).md>) — Suggests a contextual line breakpoint based on the width provided.
- [CTTypesetterSuggestLineBreakWithOffset](<cttypesettersuggestlinebreakwithoffset(________).md>) — Suggests a contextual line breakpoint based on the width provided and the specified offset.
- [CTTypesetterSuggestClusterBreakWithOffset](<cttypesettersuggestclusterbreakwithoffset(________).md>) — Suggests a cluster line breakpoint based on the specified width and line offset.
