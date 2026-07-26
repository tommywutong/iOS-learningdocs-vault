---
title: 'canLoadObjects(ofClass:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidragdropsession/canloadobjects(ofclass:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidragdropsession/canloadobjects(ofclass:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragdropsession/canloadobjects%28ofclass%3A%29.json'
content_hash: 'sha256:b9c3bc41326f6c25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragDropSession](../uidragdropsession.md)

# canLoadObjects(ofClass:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether at least one drag item in the session can create an instance of the specified class.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func canLoadObjects(ofClass aClass: any NSItemProviderReading.Type) -> Bool
```

## Parameters

- `aClass` — A class conforming to the [NSItemProviderReading](../../foundation/nsitemproviderreading.md) protocol.

## Return Value

[true](../../swift/true.md) if at least one drag item in the session can create an instance of the specified class; otherwise, [false](../../swift/false.md).

## Default Implementations

### UIDragDropSession Implementations

- [canLoadObjects(ofClass:)](<canloadobjects(ofclass_)-6x43t.md>)

## See Also

### Checking for drag items

- [- hasItemsConformingToTypeIdentifiers:](<hasitemsconforming(totypeidentifiers_).md>) — Returns a Boolean value that indicates whether at least one drag item in the session conforms to at least one of the specified UTIs.
- [items](items.md) — An array of drag items in the drag session or drop session.
