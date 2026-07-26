---
title: scriptErrorString
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsscriptcommand/scripterrorstring
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptcommand/scripterrorstring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptcommand/scripterrorstring.json'
content_hash: 'sha256:0fb4feddfa2d3017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptCommand](../nsscriptcommand.md)

# scriptErrorString

<sub>Instance Property</sub>

Sets a script error string that is associated with execution of the command.

<sub>Mac Catalyst, macOS</sub>

```swift
var scriptErrorString: String? { get set }
```

## Parameters

- `errorString` — A string that describes an error.

## Discussion

If you override [- performDefaultImplementation](<performdefaultimplementation().md>) and an error occurs, you should call this method to supply a string that provides a useful explanation. In fact, any script handler should call this method when an error occurs.

Calling this method alone does not cause an error message to be displayed—you must also call [scriptErrorNumber](scripterrornumber.md) to supply an error number.

## See Also

### Handling script execution errors

- [scriptErrorExpectedTypeDescriptor](scripterrorexpectedtypedescriptor.md) — Sets a descriptor for the expected type that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
- [scriptErrorNumber](scripterrornumber.md) — Sets a script error number that is associated with the execution of the command and is returned in the reply Apple event, if a reply was requested by the sender.
- [scriptErrorOffendingObjectDescriptor](scripterroroffendingobjectdescriptor.md) — Sets a descriptor for an object that will be put in the reply Apple event if the sender requested a reply, execution of the receiver completes, and an error number was set.
