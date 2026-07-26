---
title: UIWritingToolsCoordinator.TextDecoration
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textdecoration
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textdecoration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textdecoration.json'
content_hash: 'sha256:029a10ceb5884c71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# UIWritingToolsCoordinator.TextDecoration

<sub>Enumeration</sub>

Use the `UIWritingToolsCoordinator.TextDecoration` constants to determine the type of decoration to be applied to a preview for grammar animation. The grammar animation needs previews of the text of the issue in two forms, without and with the grammar indication underline applied. If you use grammar animation, you must implement the delegate method [- writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:textDecoration:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestspreviewfor_of_in_textdecoration_completion_).md>) to provide both forms of previews, based on the specified decoration.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum TextDecoration
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [UIWritingToolsCoordinatorTextDecorationGrammarUnderline](textdecoration/grammarunderline.md) — Requests a preview of the text with the grammar indication underline. _(beta)_
- [UIWritingToolsCoordinatorTextDecorationNone](textdecoration/none.md) — Requests a preview of the text without any additional decoration. _(beta)_

### Initializers

- [init(rawValue:)](<textdecoration/init(rawvalue_).md>) _(beta)_
