---
title: UIWritingToolsCoordinator.Delegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.2+, iPadOS 18.2+, Mac Catalyst 18.2+, visionOS 2.4+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol
source_url: 'https://developer.apple.com/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiwritingtoolscoordinator/delegate-swift.protocol.json'
content_hash: 'sha256:3e526add6ed8466e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md)

# UIWritingToolsCoordinator.Delegate

<sub>Protocol</sub>

An interface that you use to manage interactions between Writing Tools and your custom text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
protocol Delegate : NSObjectProtocol
```

## Overview

Adopt the `UIWritingToolsCoordinator.Delegate` protocol in the type you use to manage your custom text view. When you add a [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md) object to your view, the coordinator uses this protocol to communicate with that view. The protocol lets Writing Tools fetch your view’s text, report suggested changes back to your view, and deliver visual feedback when Writing Tools features are active. Make sure the type that adopts this protocol has access to your view’s text storage and can perform relevant tasks on behalf of the view.

Writing Tools expects you to call the provided handler blocks at the end of your delegate methods. It’s crucial that you execute these blocks in a timely manner to allow Writing Tools to perform subsequent tasks. For example, Writing Tools waits for you to execute the handlers for animation-related methods before moving on to the next stage of the animations.

## Relationships

- **Inherits From**: [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Starting a Writing Tools operation

- [- writingToolsCoordinator:requestsContextsForScope:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestscontextsfor_completion_).md>) — Asks your delegate to provide the text to evaluate during the Writing Tools operation.

### Incorporating Writing Tools suggestions

- [- writingToolsCoordinator:replaceRange:inContext:proposedText:reason:animationParameters:completion:](<delegate-swift.protocol/writingtoolscoordinator(__replace_in_proposedtext_reason_animationparameters_completion_).md>) — Tells the delegate that there are text changes to incorporate into the view.
- [- writingToolsCoordinator:selectRanges:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__select_in_completion_).md>) — Asks the delegate to update your view’s current text selection.

### Responding to lifecycle changes

- [- writingToolsCoordinator:willChangeToState:completion:](<delegate-swift.protocol/writingtoolscoordinator(__willchangeto_completion_).md>) — Notifies your delegate of relevant state changes when Writing Tools is running in your view.

### Animating inline text changes

- [- writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestspreviewfor_of_in_completion_).md>) — Asks the delegate for a preview image and layout information for the specified text.
- [- writingToolsCoordinator:prepareForTextAnimation:forRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__preparefor_for_in_completion_).md>) — Prepare for animations for the content that Writing Tools is evaluating.
- [- writingToolsCoordinator:finishTextAnimation:forRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__finish_for_in_completion_).md>) — Asks the delegate to clean up any state related to the specified Writing Tools animation.

### Displaying proofreading marks

- [- writingToolsCoordinator:requestsRangeInContextWithIdentifierForPoint:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestsrangeincontextwithidentifierfor_completion_).md>) — Asks the delegate to provide the location of the character at the specified point in your view’s coordinate system. _(deprecated)_
- [- writingToolsCoordinator:requestsBoundingBezierPathsForRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestsboundingbezierpathsfor_in_completion_).md>) — Asks the delegate to provide the bounding paths for the specified text in your view.
- [- writingToolsCoordinator:requestsUnderlinePathsForRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestsunderlinepathsfor_in_completion_).md>) — Asks the delegate to provide an underline shape for the specified text during a proofreading session.

### Providing animation container views dynamically

- [- writingToolsCoordinator:requestsSingleContainerSubrangesOfRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestssinglecontainersubrangesof_in_completion_).md>) — Asks the delegate to divide the specified range of text into the separate containers that render that text.
- [- writingToolsCoordinator:requestsDecorationContainerViewForRange:inContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestsdecorationcontainerviewfor_in_completion_).md>) — Asks the delegate to provide a decoration view for the specified range of text.

### Instance Methods

- [- writingToolsCoordinator:requestsGrammarResultsForContext:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestsgrammarresultsfor_completion_).md>) — Asks the delegate for information about grammar issues in the specified context. _(beta)_
- [- writingToolsCoordinator:requestsPreviewForTextAnimation:ofRange:inContext:textDecoration:completion:](<delegate-swift.protocol/writingtoolscoordinator(__requestspreviewfor_of_in_textdecoration_completion_).md>) _(beta)_
- [- writingToolsCoordinator:setGrammarCheckingEnabled:](<delegate-swift.protocol/writingtoolscoordinator(__setgrammarcheckingenabled_).md>) — Notifies the delegate when the user chooses to disable grammar checking. _(beta)_

## See Also

### Writing Tools for custom views

- [Adding Writing Tools support to a custom UIKit view](../adding-writing-tools-support-to-a-custom-uiview.md) — Add Writing Tools support, including support for inline replacement animations, to your custom iOS views that contain text.
- [UIWritingToolsCoordinator](../uiwritingtoolscoordinator.md) — An object that manages interactions between Writing Tools and your custom text view.
- [Context](context.md) — A data object that you use to share your custom view’s text with Writing Tools.
- [AnimationParameters](animationparameters.md) — An object you use to configure additional tasks or animations to run alongside the Writing Tools animations.
