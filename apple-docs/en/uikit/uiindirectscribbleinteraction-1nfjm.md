---
title: UIIndirectScribbleInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiindirectscribbleinteraction-1nfjm
source_url: 'https://developer.apple.com/documentation/uikit/uiindirectscribbleinteraction-1nfjm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiindirectscribbleinteraction-1nfjm.json'
content_hash: 'sha256:19aef5092d7df9cd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIIndirectScribbleInteraction

<sub>Class</sub>

An interaction for using Scribble to enter text by writing on a view that isn’t formally a text input.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency class UIIndirectScribbleInteraction<Delegate> where Delegate : UIIndirectScribbleInteractionDelegate
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIInteraction](uiinteraction.md)

## Topics

### Creating an indirect Scribble interaction

- [init(delegate:)](<uiindirectscribbleinteraction-1nfjm/init(delegate_).md>) — Creates an indirect Scribble interaction item with the specified delegate.

### Managing indirect Scribble interactions

- [delegate](uiindirectscribbleinteraction-1nfjm/delegate.md) — The delegate for the interaction, to supply and customize writable elements in the interaction’s view.

### Detecting writing

- [isHandlingWriting](uiindirectscribbleinteraction-1nfjm/ishandlingwriting.md) — A Boolean value that indicates whether the user is actively writing.

## See Also

### Custom views

- [UIIndirectScribbleInteractionDelegate](uiindirectscribbleinteractiondelegate-hdh.md) — Methods that customize behavior on views that aren’t formally text input views.
- [ElementIdentifier](uiindirectscribbleinteractiondelegate-hdh/elementidentifier.md) — A unique identifier for a control that isn’t a text field in a Scribble interaction.
