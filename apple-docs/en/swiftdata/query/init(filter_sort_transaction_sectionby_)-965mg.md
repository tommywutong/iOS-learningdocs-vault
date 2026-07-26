---
title: 'init(filter:sort:transaction:sectionBy:)'
framework: SwiftData
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/query/init(filter:sort:transaction:sectionby:)-965mg'
source_url: 'https://developer.apple.com/documentation/swiftdata/query/init(filter:sort:transaction:sectionby:)-965mg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/init%28filter%3Asort%3Atransaction%3Asectionby%3A%29-965mg.json'
content_hash: 'sha256:ec9be69b8d3163b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# init(filter:sort:transaction:sectionBy:)

<sub>Initializer</sub>

Creates a sectioned query with sort descriptors, grouped by an optional String key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(filter: Predicate<Element>? = nil, sort descriptors: [SortDescriptor<Element>] = [], transaction: Transaction? = nil, sectionBy sectionKeyPath: KeyPath<Element, String?>? = nil) where Result == [Element]
```

## See Also

### Creating a sorted, sectioned query

- [init(filter:sort:animation:sectionBy:)](<init(filter_sort_animation_sectionby_)-5wk67.md>) — Creates a sectioned query with sort descriptors, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:animation:sectionBy:)](<init(filter_sort_animation_sectionby_)-8e78r.md>) — Creates a sectioned query with sort descriptors, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<init(filter_sort_order_animation_sectionby_)-2e9oh.md>) — Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<init(filter_sort_order_animation_sectionby_)-2e9oh.md>) — Creates a sectioned query sorted by a key path, grouped by an optional String key path. `nil` values share the empty-string section. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<init(filter_sort_order_animation_sectionby_)-4pdmu.md>) — Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<init(filter_sort_order_animation_sectionby_)-6b4tq.md>) — Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:order:animation:sectionBy:)](<init(filter_sort_order_animation_sectionby_)-7d51r.md>) — Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<init(filter_sort_order_transaction_sectionby_)-5ym3e.md>) — Creates a sectioned query sorted by a key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<init(filter_sort_order_transaction_sectionby_)-8hx6i.md>) — Creates a sectioned query sorted by an optional key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<init(filter_sort_order_transaction_sectionby_)-930wx.md>) — Creates a sectioned query sorted by a key path, grouped by an optional String key path. Pass `nil` for the key path to disable sectioning. _(beta)_
- [init(filter:sort:order:transaction:sectionBy:)](<init(filter_sort_order_transaction_sectionby_)-l6d4.md>) — Creates a sectioned query sorted by an optional key path, grouped into sections by a String key path. Pass `nil` to disable sectioning. _(beta)_
- [init(filter:sort:transaction:sectionBy:)](<init(filter_sort_transaction_sectionby_)-2b0zd.md>) — Creates a sectioned query with sort descriptors, grouped into sections by a String key path. _(beta)_
