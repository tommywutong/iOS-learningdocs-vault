---
title: PresentationDetent.Context
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/presentationdetent/context
source_url: 'https://developer.apple.com/documentation/swiftui/presentationdetent/context'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/presentationdetent/context.json'
content_hash: 'sha256:105597274b13b68e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [PresentationDetent](../presentationdetent.md)

# PresentationDetent.Context

<sub>Structure</sub>

Information that you use to calculate the presentation’s height.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@dynamicMemberLookup struct Context
```

## Topics

### Getting the height

- [maxDetentValue](context/maxdetentvalue.md) — The height that the presentation appears in.

### Supporting types

- [subscript(dynamicMember:)](<context/subscript(dynamicmember_).md>) — Returns the value specified by the keyPath from the environment.

## See Also

### Creating custom detents

- [custom(_:)](<custom(__).md>) — A custom detent with a calculated height.
- [fraction(_:)](<fraction(__).md>) — A custom detent with the specified fractional height.
- [height(_:)](<height(__).md>) — A custom detent with the specified height.
