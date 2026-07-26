---
title: 'index(ofSectionNamed:)'
framework: SwiftData
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/resultssectioncollection/index(ofsectionnamed:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/resultssectioncollection/index(ofsectionnamed:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultssectioncollection/index%28ofsectionnamed%3A%29.json'
content_hash: 'sha256:e36fdced07169662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsSectionCollection](../resultssectioncollection.md)

# index(ofSectionNamed:)

<sub>Instance Method</sub>

Returns the ordered index of the section with the given name, or `nil` if not found.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(ofSectionNamed name: SectionName) -> Int?
```

## Discussion

> [!abstract] Complexity
> O(1)

## See Also

### Finding sections

- [sectionNames](sectionnames.md) — The section names in order. _(beta)_
- [contains(sectionName:)](<contains(sectionname_).md>) — Returns whether a section with the given name exists in the collection. _(beta)_
