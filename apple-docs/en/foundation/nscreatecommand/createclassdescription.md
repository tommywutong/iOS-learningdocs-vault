---
title: createClassDescription
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscreatecommand/createclassdescription
source_url: 'https://developer.apple.com/documentation/foundation/nscreatecommand/createclassdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscreatecommand/createclassdescription.json'
content_hash: 'sha256:1653116137c8fb5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCreateCommand](../nscreatecommand.md)

# createClassDescription

<sub>Instance Property</sub>

Returns the class description for the class that is to be created.

<sub>Mac Catalyst, macOS</sub>

```swift
var createClassDescription: NSScriptClassDescription { get }
```

## Return Value

The class description for the class that is to be created.

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)

### Getting information about a create command

- [resolvedKeyDictionary](resolvedkeydictionary.md) — Returns a dictionary that contains the properties that were specified in the `make` Apple event command that has been converted to this `NSCreateCommand` object.
