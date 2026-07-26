---
title: enableEditing()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/enableediting()
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/enableediting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/enableediting%28%29.json'
content_hash: 'sha256:904d775202f84d0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# enableEditing()

<sub>Instance Method</sub>

Enables editing when it’s safe again to make changes to a document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func enableEditing()
```

## Discussion

Subclasses should override this method to allow the user to edit the document when it’s safe to do so. This method override should be paired with an override of [- disableEditing](<disableediting().md>). The default implementation of this method does nothing.

## See Also

### Disabling and enabling editing

- [- disableEditing](<disableediting().md>) — Disables editing when it’s unsafe to make changes to a document.
