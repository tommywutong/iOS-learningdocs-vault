---
title: UIAction.Identifier
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaction/identifier-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiaction/identifier-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaction/identifier-swift.struct.json'
content_hash: 'sha256:f7553f5a0569a361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIAction](../uiaction.md)

# UIAction.Identifier

<sub>Structure</sub>

A type that represents an action identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Identifier
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIActionPaste](identifier-swift.struct/paste.md) — Identifies the action that pastes the current contents of the pasteboard into your app’s interface.
- [UIActionPasteAndGo](identifier-swift.struct/pasteandgo.md) — Identifies the action that pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [UIActionPasteAndMatchStyle](identifier-swift.struct/pasteandmatchstyle.md) — Identifies the action that pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [UIActionPasteAndSearch](identifier-swift.struct/pasteandsearch.md) — Identifies the action that pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [UIActionNewFromPasteboard](identifier-swift.struct/newfrompasteboard.md)

### Initializers

- [init(_:)](<identifier-swift.struct/init(__).md>) — Creates an action identifier from the specified string.
- [init(rawValue:)](<identifier-swift.struct/init(rawvalue_).md>) — Creates an action identifier from the specified string.

## See Also

### Creating an action

- [init(title:subtitle:image:identifier:discoverabilityTitle:attributes:state:handler:)](<init(title_subtitle_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, subtitle, image, identifier, discoverability title, attributes, state, and handler.
- [init(title:image:identifier:discoverabilityTitle:attributes:state:handler:)](<init(title_image_identifier_discoverabilitytitle_attributes_state_handler_).md>) — Creates an action with the specified title, image, identifier, discoverability title, attributes, state, and handler.
- [+ captureTextFromCameraActionForResponder:identifier:](<capturetextfromcamera(responder_identifier_).md>) — Creates an action for capturing text using the device’s camera.
- [UIActionHandler](../uiactionhandler.md) — A type that defines the closure for an action handler.
