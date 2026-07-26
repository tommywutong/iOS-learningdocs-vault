---
title: selectedAlternativeStringNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.8+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nstextalternatives/selectedalternativestringnotification
source_url: 'https://developer.apple.com/documentation/appkit/nstextalternatives/selectedalternativestringnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nstextalternatives/selectedalternativestringnotification.json'
content_hash: 'sha256:cff2535987dc2715'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSTextAlternatives](../nstextalternatives.md)

# selectedAlternativeStringNotification

<sub>Type Property</sub>

Posted when the user selects an alternate string.

<sub>macOS</sub>

```swift
class let selectedAlternativeStringNotification: NSNotification.Name
```

## Discussion

Arbitrary objects can listen for for this notification to get user selections of alternative strings. The `userInfo` dictionary contains the following information:

| Key | Value |
|---|---|
| `@"NSAlternativeString"` | The selected alternative string. |

To observe this notification using Swift concurrency, use [SelectedAlternativeStringMessage](selectedalternativestringmessage.md).
