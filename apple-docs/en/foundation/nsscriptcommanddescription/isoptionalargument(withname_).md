---
title: 'isOptionalArgument(withName:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcommanddescription/isoptionalargument(withname:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/isoptionalargument(withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/isoptionalargument%28withname%3A%29.json'
content_hash: 'sha256:fb726d5f386f82c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# isOptionalArgument(withName:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the command argument identified by the specified argument key is an optional argument.

<sub>Mac Catalyst, macOS</sub>

```swift
func isOptionalArgument(withName argumentName: String) -> Bool
```

## Parameters

- `argumentName` — Argument name (used as a key) that identifies the command argument to examine.

## Return Value

[true](../../swift/true.md) if the specified argument exists and is optional; otherwise, [false](../../swift/false.md).

## See Also

### Getting Command Argument Information

- [- appleEventCodeForArgumentWithName:](<appleeventcodeforargument(withname_).md>) — Returns the Apple event code for the specified command argument of the receiver.
- [argumentNames](argumentnames.md) — Returns the names (or keys) for all arguments of the receiver’s command.
- [- typeForArgumentWithName:](<typeforargument(withname_).md>) — Returns the type of the command argument identified by the specified key.
