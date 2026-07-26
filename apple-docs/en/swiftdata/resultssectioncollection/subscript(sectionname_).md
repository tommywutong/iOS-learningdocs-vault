---
title: 'subscript(sectionName:)'
framework: SwiftData
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftdata/resultssectioncollection/subscript(sectionname:)'
source_url: 'https://developer.apple.com/documentation/swiftdata/resultssectioncollection/subscript(sectionname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftdata/resultssectioncollection/subscript%28sectionname%3A%29.json'
content_hash: 'sha256:615ad7dbc79d1c9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftData](../../swiftdata.md) · [ResultsSectionCollection](../resultssectioncollection.md)

# subscript(sectionName:)

<sub>Instance Subscript</sub>

Returns the section with the given name, or `nil` if no such section exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(sectionName name: SectionName) -> ResultsSection<Element, SectionName>? { get }
```

## Overview

> [!abstract] Complexity
> O(1)

## See Also

### Retrieving sections

- [ResultsSection](../resultssection.md) — A section of fetched results grouped by a common section key path value. _(beta)_
