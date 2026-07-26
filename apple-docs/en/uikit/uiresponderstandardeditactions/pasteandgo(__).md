---
title: 'pasteAndGo(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/pasteandgo(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/pasteandgo(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/pasteandgo%28_%3A%29.json'
content_hash: 'sha256:56469e60f8adcc51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# pasteAndGo(_:)

<sub>Instance Method</sub>

Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func pasteAndGo(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

UIKit calls this method when the user selects the Paste and Go command from an editing menu. Your implementation should read the data from the pasteboard, add the resulting content to your interface, and begin navigating to the entity the content references.

## See Also

### Handling copy, cut, paste, and delete commands

- [- cut:](<cut(__).md>) — Removes the selected content and writes the data for it to the pasteboard.
- [- copy:](<copy(__).md>) — Copies the selected content to the pasteboard.
- [- paste:](<paste(__).md>) — Pastes the current contents of the pasteboard into your app’s interface.
- [- pasteAndMatchStyle:](<pasteandmatchstyle(__).md>) — Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [- pasteAndSearch:](<pasteandsearch(__).md>) — Pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [- delete:](<delete(__).md>) — Removes the selected content from your interface.
