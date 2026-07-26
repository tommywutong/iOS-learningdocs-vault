---
title: UIPreviewAction.Style
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+（17.1 起废弃）, iPadOS 9.0+（17.1 起废弃）, Mac Catalyst 13.1+（17.1 起废弃）, tvOS 9.0+（17.1 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipreviewaction/style
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewaction/style'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewaction/style.json'
content_hash: 'sha256:201903b2a5b08d83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewAction](../uipreviewaction.md)

# UIPreviewAction.Style

<sub>Enumeration</sub>

The style for a peek quick action.

> [!warning] Deprecated
> For more information, see [UIPreviewAction](../uipreviewaction.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum Style
```

## Overview

Use these styles with instances of the [UIPreviewAction](../uipreviewaction.md) and [UIPreviewActionGroup](../uipreviewactiongroup.md) classes.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPreviewActionStyleDefault](style/default.md) — The default style. _(deprecated)_
- [UIPreviewActionStyleSelected](style/selected.md) — The style for a selected peek quick action. _(deprecated)_
- [UIPreviewActionStyleDestructive](style/destructive.md) — The style for a peek quick action that changes or deletes data. _(deprecated)_

### Initializers

- [init(rawValue:)](<style/init(rawvalue_).md>) _(deprecated)_

## See Also

### Creating a peek quick action

- [+ actionWithTitle:style:handler:](<init(title_style_handler_).md>) — Creates a peek quick action using a specified title, style, and handler. _(deprecated)_
- [handler](handler.md) — The block called when the peek quick action is selected by the user. _(deprecated)_
