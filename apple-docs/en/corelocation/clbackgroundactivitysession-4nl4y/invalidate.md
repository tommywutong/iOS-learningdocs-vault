---
title: invalidate
framework: Core Location
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbackgroundactivitysession-4nl4y/invalidate
source_url: 'https://developer.apple.com/documentation/corelocation/clbackgroundactivitysession-4nl4y/invalidate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbackgroundactivitysession-4nl4y/invalidate.json'
content_hash: 'sha256:d825b1c7f47fec44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLBackgroundActivitySession](../clbackgroundactivitysession-4nl4y.md)

# invalidate

<sub>Instance Method</sub>

Invalidates the background activity session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
- (void) invalidate;
```

## Discussion

This method ends the session immediately. The system terminates any UI that displays a visual indication to this background session. After you invalidate a session, it can’t become active again and you need to create a new session to begin receiving updates again.
