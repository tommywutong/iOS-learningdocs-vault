---
title: UIWritingToolsCoordinator.TextAnimation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textanimation
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textanimation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textanimation.json'
content_hash: 'sha256:7d470f5e730048fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# UIWritingToolsCoordinator.TextAnimation

<sub>Enumeration</sub>

The types of animations that Writing Tools performs during an interactive update of your view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum TextAnimation
```

## Overview

Use the `UIWritingToolsCoordinator/TextAnimation` constants to determine the type of animation that is occurring. During an interactive change to your view, Writing Tools creates animations to provide feedback about what’s happening. During the setup for each animation, Writing Tools reports the type of animation to the coordinator’s delegate, so that you can perform additional actions related to that animation. For example, during an insertion animation, you might animate changes to other views in your interface.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the animation types

- [UIWritingToolsCoordinatorTextAnimationAnticipate](textanimation/anticipate.md) — The animation that Writing Tools performs when waiting to receive results from the large language model.
- [UIWritingToolsCoordinatorTextAnimationInsert](textanimation/insert.md) — The animation that Writing Tools performs when inserting text into your view.
- [UIWritingToolsCoordinatorTextAnimationRemove](textanimation/remove.md) — The animation that Writing Tools performs when removing text from your view.

### Enumeration Cases

- [UIWritingToolsCoordinatorTextAnimationIndicateGrammar](textanimation/indicategrammar.md) — The animation effect that Writing Tools performs on grammar issues when they are first indicated. _(beta)_

### Initializers

- [init(rawValue:)](<textanimation/init(rawvalue_).md>)

## See Also

### Getting the supporting types

- [ContextScope](contextscope.md) — Options that indicate how much of your content Writing Tools requested.
- [TextReplacementReason](textreplacementreason.md) — Options that indicate whether Writing Tools is animating changes to your view’s text.
