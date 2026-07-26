---
title: UIWritingToolsCoordinator.TextUpdateReason
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/textupdatereason
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/textupdatereason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/textupdatereason.json'
content_hash: 'sha256:82fd3b9e3a5c6bfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# UIWritingToolsCoordinator.TextUpdateReason

<sub>Enumeration</sub>

Constants that specify the reason you updated your view’s content outside of the Writing Tools workflow.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum TextUpdateReason
```

## Overview

If you modify your view’s text storage while Writing Tools is active, report those changes to your [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md) object so it can track them correctly. Call the [- updateRange:withText:reason:forContextWithIdentifier:](<updaterange(__with_reason_forcontextwithidentifier_).md>) method to report changes that occur inside one of your context objects. Call the [- updateForReflowedTextInContextWithIdentifier:](<updateforreflowedtextincontextwithidentifier(__).md>) method for changes that affect the layout of your text, such as text insertions before a context object or changes to your view’s frame rectangle.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the reasons

- [UIWritingToolsCoordinatorTextUpdateReasonTyping](textupdatereason/typing.md) — An operation that involved a person editing the text in your view.
- [UIWritingToolsCoordinatorTextUpdateReasonUndoRedo](textupdatereason/undoredo.md) — An operation that changed the view’s text as part of an undo or redo command.

### Initializers

- [init(rawValue:)](<textupdatereason/init(rawvalue_).md>)

## See Also

### Reporting changes to Writing Tools

- [- updateRange:withText:reason:forContextWithIdentifier:](<updaterange(__with_reason_forcontextwithidentifier_).md>) — Informs the coordinator about changes your app made to the text in the specified context object.
- [- updateForReflowedTextInContextWithIdentifier:](<updateforreflowedtextincontextwithidentifier(__).md>) — Informs the coordinator that a change occurred to the view or its text that requires a layout update.
