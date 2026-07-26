---
title: 'appleEventCodeForArgument(withName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcommanddescription/appleeventcodeforargument(withname:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventcodeforargument(withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/appleeventcodeforargument%28withname%3A%29.json'
content_hash: 'sha256:93567afde60a68ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# appleEventCodeForArgument(withName:)

<sub>Instance Method</sub>

Returns the Apple event code for the specified command argument of the receiver.

<sub>Mac Catalyst, macOS</sub>

```swift
func appleEventCodeForArgument(withName argumentName: String) -> FourCharCode
```

## Parameters

- `argumentName` — The argument name (used as a key) for which to obtain the corresponding Apple event code.

## Return Value

The code for the specified argument.

## See Also

### Getting Command Argument Information

- [argumentNames](argumentnames.md) — Returns the names (or keys) for all arguments of the receiver’s command.
- [- isOptionalArgumentWithName:](<isoptionalargument(withname_).md>) — Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.
- [- typeForArgumentWithName:](<typeforargument(withname_).md>) — Returns the type of the command argument identified by the specified key.
