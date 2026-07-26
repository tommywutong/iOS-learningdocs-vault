---
title: UITextItemInteraction
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+（17.0 起废弃）, iPadOS 10.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS 10.0+（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uitextiteminteraction
source_url: 'https://developer.apple.com/documentation/uikit/uitextiteminteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextiteminteraction.json'
content_hash: 'sha256:810f9f98ee3f59db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextItemInteraction

<sub>Enumeration</sub>

Constants that indicate the type of interaction the user expects to have with a URL or text attachment.

> [!warning] Deprecated
> Use text item methods in [UITextViewDelegate](uitextviewdelegate.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITextItemInteraction
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextItemInteractionInvokeDefaultAction](uitextiteminteraction/invokedefaultaction.md) — The user wants to perform the default action on the text item; for example, opening a URL. _(deprecated)_
- [UITextItemInteractionPresentActions](uitextiteminteraction/presentactions.md) — The user wants to be presented with a list of actions that can be taken on the text item, such as opening the link in a different way or downloading content from the link. _(deprecated)_
- [UITextItemInteractionPreview](uitextiteminteraction/preview.md) — The user wants to get a preview of the content represented by the text item, such as by initiating a peek and pop on a link. _(deprecated)_

### Initializers

- [init(rawValue:)](<uitextiteminteraction/init(rawvalue_).md>) _(deprecated)_

## See Also

### Deprecated

- [- textView:shouldInteractWithTextAttachment:inRange:interaction:](<uitextviewdelegate/textview(__shouldinteractwith_in_interaction_)-5qha9.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithURL:inRange:interaction:](<uitextviewdelegate/textview(__shouldinteractwith_in_interaction_)-622ub.md>) — Asks the delegate whether the specified text view allows the specified type of user interaction with the specified URL in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithTextAttachment:inRange:](<uitextviewdelegate/textview(__shouldinteractwith_in_)-97zx6.md>) — Asks the delegate whether the specified text view allows user interaction with the provided text attachment in the specified range of text. _(deprecated)_
- [- textView:shouldInteractWithURL:inRange:](<uitextviewdelegate/textview(__shouldinteractwith_in_)-98tho.md>) — Asks the delegate whether the specified text view allows user interaction with the specified URL in the specified range of text. _(deprecated)_
