---
title: 'merge(with:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/merge(with:)-7fk3a'
source_url: 'https://developer.apple.com/documentation/combine/publisher/merge(with:)-7fk3a'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/merge%28with%3A%29-7fk3a.json'
content_hash: 'sha256:1872a62dda4a5d98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# merge(with:)

<sub>Instance Method</sub>

Combines elements from this publisher with those from another publisher of the same type, delivering an interleaved sequence of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merge(with other: Self) -> Publishers.MergeMany<Self>
```

## Parameters

- `other` — Another publisher of this publisher’s type.

## Return Value

A publisher that emits an event when either upstream publisher emits an event.

## See Also

### Republishing elements from multiple publishers as an interleaved stream

- [merge(with:)](<merge(with_)-7qt71.md>) — Combines elements from this publisher with those from another publisher, delivering an interleaved sequence of elements.
- [merge(with:_:)](<merge(with___).md>) — Combines elements from this publisher with those from two other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:)](<merge(with_____).md>) — Combines elements from this publisher with those from three other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:)](<merge(with_______).md>) — Combines elements from this publisher with those from four other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:)](<merge(with_________).md>) — Combines elements from this publisher with those from five other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:_:)](<merge(with___________).md>) — Combines elements from this publisher with those from six other publishers, delivering an interleaved sequence of elements.
- [merge(with:_:_:_:_:_:_:)](<merge(with_____________).md>) — Combines elements from this publisher with those from seven other publishers, delivering an interleaved sequence of elements.
