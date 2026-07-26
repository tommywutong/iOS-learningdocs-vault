---
title: UIDocumentViewController.LaunchOptions
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentviewcontroller/launchoptions-swift.class.json'
content_hash: 'sha256:b05a5c0df5d70202'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentViewController](../uidocumentviewcontroller.md)

# UIDocumentViewController.LaunchOptions

<sub>Class</sub>

Options for customizing the document launch view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class LaunchOptions
```

## Overview

When your app launches, the document view controller displays a view that contains a title and buttons to create new documents. It also displays the document browser as a sheet over the title view. For more information, see [Customizing a document-based app’s launch experience](../customizing-a-document-based-app-s-launch-experience.md).

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md), [Sendable](../../swift/sendable.md)

## Topics

### Configuring the appearance

- [title](launchoptions-swift.class/title.md) — The title that appears in the title view.
- [background](launchoptions-swift.class/background.md) — A configuration that describes the launch scene’s background.
- [documentTargetView](launchoptions-swift.class/documenttargetview.md) — The document target view.
- [browserViewController](launchoptions-swift.class/browserviewcontroller.md) — The document browser view controller.

### Adding accessory views

- [backgroundAccessoryView](launchoptions-swift.class/backgroundaccessoryview.md) — A view that appears behind the title view in the launch scene.
- [foregroundAccessoryView](launchoptions-swift.class/foregroundaccessoryview.md) — A view that appears in front of the title view in the launch scene.

### Adding actions

- [primaryAction](launchoptions-swift.class/primaryaction.md) — The launch scene’s primary action.
- [secondaryAction](launchoptions-swift.class/secondaryaction.md) — The launch scene’s secondary action.

### Creating documents

- [+ createDocumentActionWithIntent:](<launchoptions-swift.class/createdocumentaction(withintent_).md>) — Creates an action that uses the specified intent.

### Instance Properties

- [subtitle](launchoptions-swift.class/subtitle.md) — The subtitle of the launch view. Default is `nil`. If `nil`, no subtitle will be displayed. _(beta)_

## See Also

### Customizing the launch experience

- [launchOptions](launchoptions-swift.property.md) — Options that customize a document-based app’s launch view.
