---
title: visualDescription()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/visualdescription()
source_url: 'https://developer.apple.com/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/visualdescription()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsdiffabledatasourcesectionsnapshot-swift.struct/visualdescription%28%29.json'
content_hash: 'sha256:11a5e9bb45161dcb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSDiffableDataSourceSectionSnapshot](../nsdiffabledatasourcesectionsnapshot-swift.struct.md)

# visualDescription()

<sub>Instance Method</sub>

Returns a string with an ASCII representation of the section snapshot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func visualDescription() -> String
```

## Discussion

An asterisk (`*`) represents a visible item, a plus sign (`+`) represents an expanded item, and a minus sign (`-`) represents a collapsed item.
