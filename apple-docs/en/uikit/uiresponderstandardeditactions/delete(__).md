---
title: 'delete(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiresponderstandardeditactions/delete(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiresponderstandardeditactions/delete(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponderstandardeditactions/delete%28_%3A%29.json'
content_hash: 'sha256:0ef61c7a599348ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponderStandardEditActions](../uiresponderstandardeditactions.md)

# delete(_:)

<sub>Instance Method</sub>

Removes the selected content from your interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func delete(_ sender: Any?)
```

## Parameters

- `sender` — The object calling this method.

## Discussion

UIKit calls this method when the user selects the Delete command from an editing menu. Your implementation should remove the selected content from your interface.

## See Also

### Handling copy, cut, paste, and delete commands

- [- cut:](<cut(__).md>) — Removes the selected content and writes the data for it to the pasteboard.
- [- copy:](<copy(__).md>) — Copies the selected content to the pasteboard.
- [- paste:](<paste(__).md>) — Pastes the current contents of the pasteboard into your app’s interface.
- [- pasteAndGo:](<pasteandgo(__).md>) — Pastes the current contents of the pasteboard into your app’s interface and navigates to the entity it references.
- [- pasteAndMatchStyle:](<pasteandmatchstyle(__).md>) — Pastes the current contents of the pasteboard into your app’s interface using the text style of the target.
- [- pasteAndSearch:](<pasteandsearch(__).md>) — Pastes the current contents of the pasteboard into your app’s interface and performs a search.
