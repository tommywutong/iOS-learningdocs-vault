---
title: rowsDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsruleeditor/rowsdidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsruleeditor/rowsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsruleeditor/rowsdidchangenotification.json'
content_hash: 'sha256:72dd1783b7661192'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSRuleEditor](../nsruleeditor.md)

# rowsDidChangeNotification

<sub>Type Property</sub>

This notification is posted to the default notification center whenever the view’s rows change.

<sub>macOS</sub>

```swift
class let rowsDidChangeNotification: NSNotification.Name
```

## Discussion

The object is the rule editor; there is no `userInfo` object.

To observe this notification using Swift concurrency, use [RowsDidChangeMessage](rowsdidchangemessage.md).
