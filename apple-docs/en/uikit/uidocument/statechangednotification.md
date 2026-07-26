---
title: stateChangedNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidocument/statechangednotification
source_url: 'https://developer.apple.com/documentation/uikit/uidocument/statechangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocument/statechangednotification.json'
content_hash: 'sha256:f2b6b15942788062'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocument](../uidocument.md)

# stateChangedNotification

<sub>Type Property</sub>

A notification the document object posts when there’s a change in the state of the document.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let stateChangedNotification: NSNotification.Name
```

## Discussion

When handling this notification, check the value of the [documentState](documentstate.md) property to see what the new state is, and then proceed accordingly. There’s no `userInfo` dictionary.
