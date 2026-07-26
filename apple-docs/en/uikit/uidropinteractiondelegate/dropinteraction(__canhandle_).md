---
title: 'dropInteraction(_:canHandle:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:canhandle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidropinteractiondelegate/dropinteraction(_:canhandle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropinteractiondelegate/dropinteraction%28_%3Acanhandle%3A%29.json'
content_hash: 'sha256:3b4e1143ffd29d43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropInteractionDelegate](../uidropinteractiondelegate.md)

# dropInteraction(_:canHandle:)

<sub>Instance Method</sub>

Asks the delegate whether it can handle the session’s drag items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func dropInteraction(_ interaction: UIDropInteraction, canHandle session: any UIDropSession) -> Bool
```

## Parameters

- `interaction` — The interaction that called this method.

- `session` — The current drop session.

## Return Value

[true](../../swift/true.md) if the interaction supports the drag items in the sessions; otherwise, [false](../../swift/false.md).

## Discussion

Returning [true](../../swift/true.md) doesn’t mean the interaction will accept the drop. Instead, it tells the system that the interaction has interest in, and can handle, the drop session.

To determine if the interaction can handle the session, check the data type of session’s drag items. For instance, if you’re interested in drop activities that contain images, you can do the following:

```swift
func dropInteraction(_ interaction: UIDropInteraction, canHandle session: UIDropSession) -> Bool {
    // Ensure the drop session has an object of the appropriate type
    return session.canLoadObjects(ofClass: UIImage.self)
}
```

You can also be more specific by using a uniform type identifier (UTI) for the data type. For instance, if you’re interested in only PNG images, use the UTI for PNG files:

```swift
import MobileCoreServices // for kUTTypePNG

func dropInteraction(_ interaction: UIDropInteraction, canHandle session: UIDropSession) -> Bool {
    return session.hasItemsConforming(toTypeIdentifiers: [kUTTypePNG as String])
}
```

> [!note] Note
> You can’t check the actual data the user is dragging because it isn’t available when the interaction calls this method. Only the data type is available inside this method.

## See Also

### Handling the drop

- [- dropInteraction:performDrop:](<dropinteraction(__performdrop_).md>) — Tells the delegate it can request the item provider data from the session’s drag items.
