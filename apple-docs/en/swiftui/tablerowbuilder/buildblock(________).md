---
title: 'buildBlock(_:_:_:_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 12.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/tablerowbuilder/buildblock(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/tablerowbuilder/buildblock%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:ec3698954bb76168'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [TableRowBuilder](../tablerowbuilder.md)

# buildBlock(_:_:_:_:)

<sub>Type Method</sub>

Creates a row result from four sources.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) static func buildBlock<C0, C1, C2, C3>(_ c0: C0, _ c1: C1, _ c2: C2, _ c3: C3) -> TupleTableRowContent<Value, (C0, C1, C2, C3)> where Value == C0.TableRowValue, C0 : TableRowContent, C1 : TableRowContent, C2 : TableRowContent, C3 : TableRowContent, C0.TableRowValue == C1.TableRowValue, C1.TableRowValue == C2.TableRowValue, C2.TableRowValue == C3.TableRowValue
```

## See Also

### Building a row from sources

- [buildBlock(_:)](<buildblock(__).md>) — Creates a single row result.
- [buildBlock(_:_:)](<buildblock(____).md>) — Creates a row result from two sources.
- [buildBlock(_:_:_:)](<buildblock(______).md>) — Creates a row result from three sources.
- [buildBlock(_:_:_:_:_:)](<buildblock(__________).md>) — Creates a row result from five sources.
- [buildBlock(_:_:_:_:_:_:)](<buildblock(____________).md>) — Creates a row result from six sources.
- [buildBlock(_:_:_:_:_:_:_:)](<buildblock(______________).md>) — Creates a row result from seven sources.
- [buildBlock(_:_:_:_:_:_:_:_:)](<buildblock(________________).md>) — Creates a row result from eight sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:)](<buildblock(__________________).md>) — Creates a row result from nine sources.
- [buildBlock(_:_:_:_:_:_:_:_:_:_:)](<buildblock(____________________).md>) — Creates a row result from ten sources.
