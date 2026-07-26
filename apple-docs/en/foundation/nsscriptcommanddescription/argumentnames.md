---
title: argumentNames
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/argumentnames
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/argumentnames'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/argumentnames.json'
content_hash: 'sha256:3c386230ee11e995'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# argumentNames

<sub>Instance Property</sub>

Returns the names (or keys) for all arguments of the receiver’s command.

<sub>Mac Catalyst, macOS</sub>

```swift
var argumentNames: [String] { get }
```

## Return Value

The array of argument names. If there are no arguments for the command, returns an empty array.

## See Also

### Getting Command Argument Information

- [- appleEventCodeForArgumentWithName:](<appleeventcodeforargument(withname_).md>) — Returns the Apple event code for the specified command argument of the receiver.
- [- isOptionalArgumentWithName:](<isoptionalargument(withname_).md>) — Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.
- [- typeForArgumentWithName:](<typeforargument(withname_).md>) — Returns the type of the command argument identified by the specified key.
