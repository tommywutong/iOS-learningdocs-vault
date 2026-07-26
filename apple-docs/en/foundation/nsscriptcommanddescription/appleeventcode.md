---
title: appleEventCode
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/appleeventcode
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventcode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/appleeventcode.json'
content_hash: 'sha256:f39acc17b8d3a87f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# appleEventCode

<sub>Instance Property</sub>

Returns the four-character code for the Apple event ID of the receiver’s command.

<sub>Mac Catalyst, macOS</sub>

```swift
var appleEventCode: FourCharCode { get }
```

## Return Value

The code for the event ID of the receiver’s command.

## Discussion

This value of the event ID returned by this method, together with the event class code returned by [appleEventClassCode](appleeventclasscode.md), specifies the necessary information for identifying and dispatching an Apple event.

## See Also

### Related Documentation

- [appleEventCodeForReturnType](appleeventcodeforreturntype.md) — Returns the Apple event code that identifies the command’s return type.
- [- appleEventCodeForArgumentWithName:](<appleeventcodeforargument(withname_).md>) — Returns the Apple event code for the specified command argument of the receiver.

### Getting Basic Information About the Command

- [appleEventClassCode](appleeventclasscode.md) — Returns the four-character code for the Apple event class of the receiver’s command.
- [commandClassName](commandclassname.md) — Returns the name of the class that will be instantiated to handle the command.
- [commandName](commandname.md) — Returns the name of the command.
- [suiteName](suitename.md) — Returns the name of the suite that contains the command described by the receiver.
