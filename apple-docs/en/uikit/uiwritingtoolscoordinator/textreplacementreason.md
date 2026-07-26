---
title: UIWritingToolsCoordinator.TextReplacementReason
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textreplacementreason
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textreplacementreason.json'
content_hash: 'sha256:a110f0fb2d2c1ab8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# UIWritingToolsCoordinator.TextReplacementReason

<sub>Enumeration</sub>

Options that indicate whether Writing Tools is animating changes to your view’s text.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum TextReplacementReason
```

## Overview

During an operation, Writing Tools delivers replacement text to the delegate of the active [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md) object. Depending on the configured experience for your view, it delivers these changes as either interactive or noninteractive replacements. For interactive replacements, Writing Tools animates the change automatically and provides you with the information you need to perform any related animations.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the reasons

- [UIWritingToolsCoordinatorTextReplacementReasonInteractive](textreplacementreason/interactive.md) — An option to animate the replacement of text in your view.
- [UIWritingToolsCoordinatorTextReplacementReasonNoninteractive](textreplacementreason/noninteractive.md) — An option to replace the text in your view without animating the change.

### Enumeration Cases

- [UIWritingToolsCoordinatorTextReplacementReasonAccepted](textreplacementreason/accepted.md) — An option to replace the text in your view when a grammar suggestion is accepted. _(beta)_
- [UIWritingToolsCoordinatorTextReplacementReasonRejected](textreplacementreason/rejected.md) — An option to replace the text in your view when a grammar suggestion is rejected. _(beta)_
- [UIWritingToolsCoordinatorTextReplacementReasonTemporary](textreplacementreason/temporary.md) — An option to replace the text in your view when a grammar suggestion is temporarily shown to preview the proposed change in the text. _(beta)_

### Initializers

- [init(rawValue:)](<textreplacementreason/init(rawvalue_).md>)

## See Also

### Getting the supporting types

- [ContextScope](contextscope.md) — Options that indicate how much of your content Writing Tools requested.
- [TextAnimation](textanimation.md) — The types of animations that Writing Tools performs during an interactive update of your view.
