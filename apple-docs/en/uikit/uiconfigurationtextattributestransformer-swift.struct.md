---
title: UIConfigurationTextAttributesTransformer
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiconfigurationtextattributestransformer-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiconfigurationtextattributestransformer-swift.struct.json'
content_hash: 'sha256:949949d944c4ab53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIConfigurationTextAttributesTransformer

<sub>Structure</sub>

Defines a text transformation that can affect the visual appearance of a string.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIConfigurationTextAttributesTransformer
```

## Overview

Use a transformer to affect how your attributed text appears on the UI. You provide a closure when initializing the transformer. Your closure accepts a container with the current text attributes and returns a container with the new text attributes.

```swift
let transformer = UIConfigurationTextAttributesTransformer { incoming in
    var outgoing = incoming
    outgoing.foregroundColor = UIColor.black
    outgoing.font = UIFont.boldSystemFont(ofSize: 20)
    return outgoing
}
```

## Topics

### Creating a text attributes transformer

- [init(_:)](<uiconfigurationtextattributestransformer-swift.struct/init(__).md>) — Creates a new text attributes transformer.

### Defining a text transformation

- [transform](uiconfigurationtextattributestransformer-swift.struct/transform.md) — A closure that defines the text transformation.

### Calling a text transformer

- [callAsFunction(_:)](<uiconfigurationtextattributestransformer-swift.struct/callasfunction(__).md>) — Calls the transform closure of the text attributes transformer.

## See Also

### Configuring titles

- [title](uibutton/configuration-swift.struct/title.md) — The text of the title label the button displays.
- [subtitle](uibutton/configuration-swift.struct/subtitle.md) — The text the subtitle label of the button displays.
- [attributedTitle](uibutton/configuration-swift.struct/attributedtitle.md) — The text and style attributes for the button’s title label.
- [attributedSubtitle](uibutton/configuration-swift.struct/attributedsubtitle.md) — The text and style attributes for the button’s subtitle label.
- [titleTextAttributesTransformer](uibutton/configuration-swift.struct/titletextattributestransformer.md) — A structure to update the attributed title when the button state changes.
- [subtitleTextAttributesTransformer](uibutton/configuration-swift.struct/subtitletextattributestransformer.md) — A structure to update the attributed subtitle when the button state changes.
- [titlePadding](uibutton/configuration-swift.struct/titlepadding.md) — The distance between the title and subtitle labels.
- [titleAlignment](uibutton/configuration-swift.struct/titlealignment-swift.property.md) — The text alignment the button uses to lay out the title and subtitle.
- [TitleAlignment](uibutton/configuration-swift.struct/titlealignment-swift.enum.md) — Specifies how to align a button’s title and subtitle.
- [titleLineBreakMode](uibutton/configuration-swift.struct/titlelinebreakmode.md) — The line break mode the button uses to lay out the button’s title.
- [subtitleLineBreakMode](uibutton/configuration-swift.struct/subtitlelinebreakmode.md) — The line break mode the button uses to lay out the button’s subtitle.
