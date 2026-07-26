---
title: body
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/gesturestategesture/body
source_url: 'https://developer.apple.com/documentation/swiftui/gesturestategesture/body'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/gesturestategesture/body.json'
content_hash: 'sha256:93fb71087af1fd88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [GestureStateGesture](../gesturestategesture.md)

# body

<sub>Instance Property</sub>

The updating gesture containing the originating gesture’s value, the updated state of the gesture, and a transaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var body: (GestureStateGesture<Base, State>.Value, inout State, inout Transaction) -> Void
```
