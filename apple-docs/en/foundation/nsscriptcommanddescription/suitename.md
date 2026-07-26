---
title: suiteName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/suitename
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/suitename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/suitename.json'
content_hash: 'sha256:21d5ec6cf2ae6a24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# suiteName

<sub>Instance Property</sub>

Returns the name of the suite that contains the command described by the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
var suiteName: String { get }
```

## Return Value

The receiver’s suite name. Within an application’s scriptability information, named suites contain related sets of information.

## See Also

### Getting Basic Information About the Command

- [appleEventClassCode](appleeventclasscode.md) — Returns the four-character code for the Apple event class of the receiver’s command.
- [appleEventCode](appleeventcode.md) — Returns the four-character code for the Apple event ID of the receiver’s command.
- [commandClassName](commandclassname.md) — Returns the name of the class that will be instantiated to handle the command.
- [commandName](commandname.md) — Returns the name of the command.
