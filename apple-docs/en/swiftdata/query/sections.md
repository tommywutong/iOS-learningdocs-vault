---
title: sections
framework: SwiftData
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftdata/query/sections
source_url: 'https://developer.apple.com/documentation/swiftdata/query/sections'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/query/sections.json'
content_hash: 'sha256:330c0915a3267c33'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [Query](../query.md)

# sections

<sub>Instance Property</sub>

The sections computed from the current results, grouped by the `sectionBy` key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency var sections: ResultsSectionCollection<Element, String> { get }
```

## Discussion

Section names are `String`-typed. Both `KeyPath<Element, String>` and `KeyPath<Element, String?>` section keys produce `String` names — `nil` values map to the empty-string section.

Returns an empty collection when the query was not created with a `sectionBy` parameter. Access this from the query’s stored property using the underscore prefix:

```swift
struct ItemList: View {
    @Query(sort: \.category, sectionBy: \.category)
    var items: [Item]

    var body: some View {
        List {
            ForEach(_items.sections) { section in
                Section(section.name) {
                    ForEach(section) { item in Text(item.name) }
                }
            }
        }
    }
}
```

## See Also

### Accessing sections

- [ResultsSectionCollection](../resultssectioncollection.md) — A collection of sections as returned by [sections](../resultsobserver/sections.md) or `Query.sections`. _(beta)_
