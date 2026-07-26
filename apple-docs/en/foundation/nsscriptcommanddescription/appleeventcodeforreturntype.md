---
title: appleEventCodeForReturnType
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommanddescription/appleeventcodeforreturntype
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/appleeventcodeforreturntype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/appleeventcodeforreturntype.json'
content_hash: 'sha256:21765358994a20df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# appleEventCodeForReturnType

<sub>Instance Property</sub>

Returns the Apple event code that identifies the command’s return type.

<sub>Mac Catalyst, macOS</sub>

```swift
var appleEventCodeForReturnType: FourCharCode { get }
```

## Return Value

The event code for the command’s return type.

## See Also

### Related Documentation

- [- appleEventCodeForArgumentWithName:](<appleeventcodeforargument(withname_).md>) — Returns the Apple event code for the specified command argument of the receiver.

### Getting Command Return-Type Information

- [returnType](returntype.md) — Returns the return type of the command.
