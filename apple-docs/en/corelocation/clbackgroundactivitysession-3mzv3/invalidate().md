---
title: invalidate()
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbackgroundactivitysession-3mzv3/invalidate()
source_url: 'https://developer.apple.com/documentation/corelocation/clbackgroundactivitysession-3mzv3/invalidate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbackgroundactivitysession-3mzv3/invalidate%28%29.json'
content_hash: 'sha256:94ba150677cc6550'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBackgroundActivitySession](../clbackgroundactivitysession-3mzv3.md)

# invalidate()

<sub>Instance Method</sub>

Invalidates the background activity session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
final func invalidate()
```

## Discussion

This method ends the session immediately. The system terminates any UI that displays a visual indication to this background session. After you invalidate a session, it can’t become active again and you need to create a new session to begin receiving updates again.
