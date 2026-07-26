---
title: 'init(title:message:actions:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/uikit/uisceneclosureconfirmation/init(title:message:actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisceneclosureconfirmation/init(title:message:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneclosureconfirmation/init%28title%3Amessage%3Aactions%3A%29.json'
content_hash: 'sha256:9db945a25f7b39da'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneClosureConfirmation](../uisceneclosureconfirmation.md)

# init(title:message:actions:)

<sub>Initializer</sub>

Creates a scene closure confirmation with the provided parameters.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
convenience init(title: String?, message: String?, actions: [UIAlertAction])
```

## Parameters

- `title` — The title of the confirmation. If not provided, defaults to a generic localized title.

- `message` — Optional descriptive text that provides more details.

- `actions` — Actions to be included in the confirmation dialog. Close and Cancel are shown by default.
