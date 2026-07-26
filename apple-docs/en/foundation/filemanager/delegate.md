---
title: delegate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/delegate
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/delegate.json'
content_hash: 'sha256:ebff1f45a40fc0e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# delegate

<sub>Instance Property</sub>

The delegate of the file manager object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
unowned(unsafe) var delegate: (any FileManagerDelegate)? { get set }
```

## Discussion

It is recommended that you assign a delegate to the file manager object only if you allocated and initialized the object yourself. Avoid assigning a delegate to the shared file manager obtained from the [defaultManager](default.md) method.

The default value of this property is `nil`. When assigning a delegate to this property, your object must conform to the [FileManagerDelegate](../filemanagerdelegate.md) protocol.
