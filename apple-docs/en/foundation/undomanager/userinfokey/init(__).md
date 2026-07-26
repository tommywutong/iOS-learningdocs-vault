---
title: 'init(_:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/undomanager/userinfokey/init(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/undomanager/userinfokey/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/undomanager/userinfokey/init%28_%3A%29.json'
content_hash: 'sha256:b5ab241be36ddf1a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [UndoManager](../../undomanager.md) · [UserInfoKey](../userinfokey.md)

# init(_:)

<sub>Initializer</sub>

Creates a user info key from the given string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ rawValue: String)
```

## Parameters

- `rawValue` — The raw value string.

## Discussion

Don’t use this initializer. Instead, extend the [UserInfoKey](../userinfokey.md) namespace as follows:

```swift
extension UndoManager.UserInfoKey {
    static let icon: UndoManager.UserInfoKey = "icon"
}
```

## See Also

### Creating a user info key from a raw value

- [init(rawValue:)](<init(rawvalue_).md>)
