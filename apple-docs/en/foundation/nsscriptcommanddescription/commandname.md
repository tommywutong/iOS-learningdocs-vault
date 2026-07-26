---
title: commandName
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/commandname
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/commandname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/commandname.json'
content_hash: 'sha256:d2f4c897239794f1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# commandName

<sub>Instance Property</sub>

Returns the name of the command.

<sub>Mac Catalyst, macOS</sub>

```swift
var commandName: String { get }
```

## Return Value

The command name as it appears in the application’s scriptability information; may be different from what is displayed to the scripter.

## See Also

### Getting Basic Information About the Command

- [appleEventClassCode](appleeventclasscode.md) — Returns the four-character code for the Apple event class of the receiver’s command.
- [appleEventCode](appleeventcode.md) — Returns the four-character code for the Apple event ID of the receiver’s command.
- [commandClassName](commandclassname.md) — Returns the name of the class that will be instantiated to handle the command.
- [suiteName](suitename.md) — Returns the name of the suite that contains the command described by the receiver.
