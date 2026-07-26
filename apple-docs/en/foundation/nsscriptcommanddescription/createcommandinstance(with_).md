---
title: 'createCommandInstance(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptcommanddescription/createcommandinstance(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommanddescription/createcommandinstance(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommanddescription/createcommandinstance%28with%3A%29.json'
content_hash: 'sha256:58905846efefde1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommandDescription](../nsscriptcommanddescription.md)

# createCommandInstance(with:)

<sub>Instance Method</sub>

Creates and returns an instance of the command object described by the receiver in the specified memory zone.

<sub>Mac Catalyst, macOS</sub>

```swift
func createCommandInstance(with zone: NSZone? = nil) -> NSScriptCommand
```

## Parameters

- `zone` — The memory zone from which to allocate the command.

## Return Value

The command object, instantiated from [NSScriptCommand](../nsscriptcommand.md) or a subclass.

## See Also

### Creating Commands

- [- createCommandInstance](<createcommandinstance().md>) — Creates and returns an instance of the command object described by the receiver.
