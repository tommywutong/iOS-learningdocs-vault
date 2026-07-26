---
title: saveOptions
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsquitcommand/saveoptions
source_url: 'https://developer.apple.com/documentation/foundation/nsquitcommand/saveoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsquitcommand/saveoptions.json'
content_hash: 'sha256:66f050d09ae77398'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSQuitCommand](../nsquitcommand.md)

# saveOptions

<sub>Instance Property</sub>

Returns a constant indicating how to deal with closing any modified documents.

<sub>Mac Catalyst, macOS</sub>

```swift
var saveOptions: NSSaveOptions { get }
```

## Return Value

A constant indicating how to deal with closing any modified documents. The default value returned is `NSSaveOptionsAsk`. See “Constants” in [NSCloseCommand](../nsclosecommand.md) for a list of possible return values.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
