---
title: scriptErrorOffendingObjectDescriptor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/scripterroroffendingobjectdescriptor
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/scripterroroffendingobjectdescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/scripterroroffendingobjectdescriptor.json'
content_hash: 'sha256:6e0f4300074c65e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# scriptErrorOffendingObjectDescriptor

<sub>Instance Property</sub>

Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.

<sub>macOS</sub>

```swift
var scriptErrorOffendingObjectDescriptor: NSAppleEventDescriptor? { get set }
```

## Parameters

- `errorOffendingObjectDescriptor` — A descriptor that specifies an object that was responsible for an error.

## See Also

### Handling script execution errors

- [scriptErrorExpectedTypeDescriptor](scripterrorexpectedtypedescriptor.md) — Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [scriptErrorNumber](scripterrornumber.md) — Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.
- [scriptErrorString](scripterrorstring.md) — Sets a script error string that is associated with execution of the command.
