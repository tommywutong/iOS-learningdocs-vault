---
title: localSession
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/dropsession/localsession-swift.property
source_url: 'https://developer.apple.com/documentation/swiftui/dropsession/localsession-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/dropsession/localsession-swift.property.json'
content_hash: 'sha256:5c2c943fc68e8983'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DropSession](../dropsession.md)

# localSession

<sub>Instance Property</sub>

Provides additional information about a session if it originated within the app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var localSession: DropSession.LocalSession?
```

## Discussion

This property is set to `nil` if drag originated outside the app.

## See Also

### Getting drop session details

- [id](id-swift.property.md) — The unique identifier of the drop session.
- [ID](id-swift.struct.md) — The identifier of a drag session.
- [LocalSession](localsession-swift.struct.md) — Describes the session originated within the app.
- [phase](phase-swift.property.md) — The phase of the current drop session.
- [Phase](phase-swift.enum.md) — The phase of the current drop session.
- [suggestedOperations](suggestedoperations.md) — Operations suggested by the drag source.
