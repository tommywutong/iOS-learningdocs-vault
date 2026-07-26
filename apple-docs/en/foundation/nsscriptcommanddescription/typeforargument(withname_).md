---
title: 'typeForArgument(withName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcommanddescription/typeforargument(withname:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/typeforargument(withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/typeforargument%28withname%3A%29.json'
content_hash: 'sha256:e79505cb9ccf2c6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# typeForArgument(withName:)

<sub>Instance Method</sub>

Returns the type of the command argument identified by the specified key.

<sub>Mac Catalyst, macOS</sub>

```swift
func typeForArgument(withName argumentName: String) -> String?
```

## Parameters

- `argumentName` — Argument name (used as a key) that identifies the command argument to examine.

## Return Value

The type of the specified command argument. Returns `nil` if there is no such argument.

## See Also

### Getting Command Argument Information

- [- appleEventCodeForArgumentWithName:](<appleeventcodeforargument(withname_).md>) — Returns the Apple event code for the specified command argument of the receiver.
- [argumentNames](argumentnames.md) — Returns the names (or keys) for all arguments of the receiver’s command.
- [- isOptionalArgumentWithName:](<isoptionalargument(withname_).md>) — Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.
