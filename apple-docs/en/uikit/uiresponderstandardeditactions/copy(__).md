---
title: 'copy(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/copy(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/copy(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/copy%28_%3A%29.json'
content_hash: 'sha256:284374bca19c2169'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# copy(_:)

<sub>Instance Method</sub>

Copies the selected content to the pasteboard.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func copy(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

UIKit calls this method when the user selects the Copy command from an editing menu. Your implementation should write the selected content to the pasteboard without removing the selection from your interface.

## See Also

### Handling copy, cut, paste, and delete commands

- [- cut:](<cut(__).md>) — Removes the selected content and writes the data for it to the pasteboard.
- [- paste:](<paste(__).md>) — Pastes the current contents of the pasteboard into your app’s interface.
- [- pasteAndGo:](<pasteandgo(__).md>) — Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [- pasteAndMatchStyle:](<pasteandmatchstyle(__).md>) — Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [- pasteAndSearch:](<pasteandsearch(__).md>) — Pastes the current contents of the pasteboard into your app’s interface and performs a search.
- [- delete:](<delete(__).md>) — Removes the selected content from your interface.
