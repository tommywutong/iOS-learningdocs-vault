---
title: disableEditing()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/disableediting()
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/disableediting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/disableediting%28%29.json'
content_hash: 'sha256:e321e1f6f769fd82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# disableEditing()

<sub>Instance Method</sub>

Disables editing when it’s unsafe to make changes to a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func disableEditing()
```

## Discussion

Subclasses should override this method to prevent the user from editing the document when it’s unsafe to do so, such as during a save-and-close or revert operation. When editing is safe again, UIKit class calls [- enableEditing](<enableediting().md>). The default implementation of this method does nothing.

## See Also

### Disabling and enabling editing

- [- enableEditing](<enableediting().md>) — Enables editing when it’s safe again to make changes to a document.
