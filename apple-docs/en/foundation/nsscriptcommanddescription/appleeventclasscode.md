---
title: appleEventClassCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/appleeventclasscode
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventclasscode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/appleeventclasscode.json'
content_hash: 'sha256:fa62427e0cb40499'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# appleEventClassCode

<sub>Instance Property</sub>

Returns the four-character code for the Apple event class of the receiver’s command.

<sub>Mac Catalyst, macOS</sub>

```swift
var appleEventClassCode: FourCharCode { get }
```

## Return Value

The Apple event code associated with the receiver’s command. This is the primary code used to identify the command in Apple events.

## Discussion

In an Apple event that specifies a script command, two four character codes—the event class and event ID—together identify the command. You use this method to obtain the event class. You use [appleEventCode](appleeventcode.md) to obtain the event ID.

For example, commands in AppleScript’s Core suite, such as `clone`, `count`, and `create`, have an event class code of `'core'`. This code and the event ID code returned by `appleEventCode` together specify the necessary information for identifying and dispatching an Apple event.

## See Also

### Getting Basic Information About the Command

- [appleEventCode](appleeventcode.md) — Returns the four-character code for the Apple event ID of the receiver’s command.
- [commandClassName](commandclassname.md) — Returns the name of the class that will be instantiated to handle the command.
- [commandName](commandname.md) — Returns the name of the command.
- [suiteName](suitename.md) — Returns the name of the suite that contains the command described by the receiver.
