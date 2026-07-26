---
title: 'activityViewControllerShareRecipients(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiactivityitemsource/activityviewcontrollersharerecipients(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactivityitemsource/activityviewcontrollersharerecipients(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactivityitemsource/activityviewcontrollersharerecipients%28_%3A%29.json'
content_hash: 'sha256:cd88e5a4996b2a97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActivityItemSource](../uiactivityitemsource.md)

# activityViewControllerShareRecipients(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func activityViewControllerShareRecipients(_ activityViewController: UIActivityViewController) -> [INPerson]
```

## Discussion

Allows the activity item source to provide recipients who will be filled in by default in the compose view if that sharing app supports it.

This might fail to pre-fill correctly if the sharing app chosen by the user can’t recognize the provided person. Also, if a people suggestion is chosen, that suggestion will override this provided value.
