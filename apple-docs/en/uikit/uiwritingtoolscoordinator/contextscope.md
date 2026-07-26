---
title: UIWritingToolsCoordinator.ContextScope
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/contextscope
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/contextscope'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/contextscope.json'
content_hash: 'sha256:f36fb642e875c6bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# UIWritingToolsCoordinator.ContextScope

<sub>Enumeration</sub>

Options that indicate how much of your content Writing Tools requested.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum ContextScope
```

## Overview

At the start of any Writing Tools interaction, you provide the text for the system to evaluate from your [Delegate](delegate-swift.protocol.md) object. The request for your content comes with a scope constant that indicates how much of your view’s text to provide.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the scope

- [UIWritingToolsCoordinatorContextScopeUserSelection](contextscope/userselection.md) — An option to provide only the view’s currently selected text.
- [UIWritingToolsCoordinatorContextScopeFullDocument](contextscope/fulldocument.md) — An option to provide all of your view’s text.
- [UIWritingToolsCoordinatorContextScopeVisibleArea](contextscope/visiblearea.md) — An option to provide only the text in the currently visible portion of your view.

### Initializers

- [init(rawValue:)](<contextscope/init(rawvalue_).md>)

## See Also

### Getting the supporting types

- [TextReplacementReason](textreplacementreason.md) — Options that indicate whether Writing Tools is animating changes to your view’s text.
- [TextAnimation](textanimation.md) — The types of animations that Writing Tools performs during an interactive update of your view.
