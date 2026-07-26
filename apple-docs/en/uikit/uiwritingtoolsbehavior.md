---
title: UIWritingToolsBehavior
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolsbehavior
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolsbehavior'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolsbehavior.json'
content_hash: 'sha256:d0844358b093bfad'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIWritingToolsBehavior

<sub>Enumeration</sub>

Constants that specify the writing tools experience for the underlying view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIWritingToolsBehavior
```

## Overview

Writing tools provide proofreading and rewriting support for the content of text views. On devices that support writing tools features, people engage the system UI to choose how to rewrite all or part of the available text. These constants indicate whether people experience writing tools inline with their text, in an overlay panel, or not at all.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the writing tools behaviors

- [UIWritingToolsBehaviorNone](uiwritingtoolsbehavior/none.md) — An option to prevent the writing tools from modifying the text in the view.
- [UIWritingToolsBehaviorDefault](uiwritingtoolsbehavior/default.md) — An option to let the system determine the best way to enable writing tools for the view.
- [UIWritingToolsBehaviorComplete](uiwritingtoolsbehavior/complete.md) — An option to provide the complete writing tools experience for the text view.
- [UIWritingToolsBehaviorLimited](uiwritingtoolsbehavior/limited.md) — An option to provide a limited, overlay-panel experience for the text view.

### Initializers

- [init(rawValue:)](<uiwritingtoolsbehavior/init(rawvalue_).md>)

## See Also

### Configuration

- [Customizing Writing Tools behavior for UIKit views](customizing-writing-tools-behavior-for-system-views.md) — Modify the behavior of Writing Tools in standard iOS text views, and adjust your app’s behavior while the feature is active.
- [UIWritingToolsResultOptions](uiwritingtoolsresultoptions.md) — Constants to specify what type of content to allow in Writing Tools suggestions or rewrites.
