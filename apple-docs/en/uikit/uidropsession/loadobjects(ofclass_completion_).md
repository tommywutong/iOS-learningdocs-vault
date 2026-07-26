---
title: 'loadObjects(ofClass:completion:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropsession/loadobjects(ofclass:completion:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropsession/loadobjects(ofclass:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropsession/loadobjects%28ofclass%3Acompletion%3A%29.json'
content_hash: 'sha256:55072cc47906d153'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropSession](../uidropsession.md)

# loadObjects(ofClass:completion:)

<sub>Instance Method</sub>

Creates and loads a new instance of the specified class for each drag item in the session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func loadObjects(ofClass aClass: any NSItemProviderReading.Type, completion: @escaping ([any NSItemProviderReading]) -> Void) -> Progress
```

## Parameters

- `aClass` — A class conforming to the [NSItemProviderReading](../../foundation/nsitemproviderreading.md) protocol.

- `completion` — The block that is executed after all objects are loaded.

## Return Value

An aggregate of the load progress for each object that is loaded.

## Discussion

You can use this method only in the drop interaction delegate’s implementation of the [- dropInteraction:performDrop:](<../uidropinteractiondelegate/dropinteraction(__performdrop_).md>) method. This method is called after the user drops the items into the destination view.

The completion handler is called on the main queue. It provides an array of all objects created, in the same order that the drag items were added to the drag session.

## Default Implementations

### UIDropSession Implementations

- [loadObjects(ofClass:completion:)](<loadobjects(ofclass_completion_)-3ab01.md>)
