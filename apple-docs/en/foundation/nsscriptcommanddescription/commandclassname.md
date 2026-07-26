---
title: commandClassName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/commandclassname
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/commandclassname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/commandclassname.json'
content_hash: 'sha256:855bdaca3e32452a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# commandClassName

<sub>Instance Property</sub>

Returns the name of the class that will be instantiated to handle the command.

<sub>Mac Catalyst, macOS</sub>

```swift
var commandClassName: String { get }
```

## Return Value

The Objective-C class name (for example, `"NSGetCommand"`). This is always [NSScriptCommand](../nsscriptcommand.md) or a subclass.

## See Also

### Getting Basic Information About the Command

- [appleEventClassCode](appleeventclasscode.md) — Returns the four-character code for the Apple event class of the receiver’s command.
- [appleEventCode](appleeventcode.md) — Returns the four-character code for the Apple event ID of the receiver’s command.
- [commandName](commandname.md) — Returns the name of the command.
- [suiteName](suitename.md) — Returns the name of the suite that contains the command described by the receiver.
