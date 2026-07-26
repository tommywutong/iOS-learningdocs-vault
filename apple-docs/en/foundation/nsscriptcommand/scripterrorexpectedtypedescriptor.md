---
title: scriptErrorExpectedTypeDescriptor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/scripterrorexpectedtypedescriptor
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/scripterrorexpectedtypedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/scripterrorexpectedtypedescriptor.json'
content_hash: 'sha256:63167eb7cfdda071'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# scriptErrorExpectedTypeDescriptor

<sub>Instance Property</sub>

Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.

<sub>macOS</sub>

```swift
var scriptErrorExpectedTypeDescriptor: NSAppleEventDescriptor? { get set }
```

## Parameters

- `errorExpectedTypeDescriptor` — A descriptor that specifies a type.

## See Also

### Handling script execution errors

- [scriptErrorNumber](scripterrornumber.md) — Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.
- [scriptErrorOffendingObjectDescriptor](scripterroroffendingobjectdescriptor.md) — Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [scriptErrorString](scripterrorstring.md) — Sets a script error string that is associated with execution of the command.
