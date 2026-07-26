---
title: resolvedKeyDictionary
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscreatecommand/resolvedkeydictionary
source_url: 'https://developer.apple.com/documentation/foundation/nscreatecommand/resolvedkeydictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscreatecommand/resolvedkeydictionary.json'
content_hash: 'sha256:92e928723937d46c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCreateCommand](../nscreatecommand.md)

# resolvedKeyDictionary

<sub>Instance Property</sub>

Returns a dictionary that contains the properties that were specified in the `make` Apple event command that has been converted to this `NSCreateCommand` object.

<sub>Mac Catalyst, macOS</sub>

```swift
var resolvedKeyDictionary: [String : Any] { get }
```

## Return Value

A dictionary that contains the properties that were specified in the `make` Apple event script command that has been converted to this `NSCreateCommand` object.

## Discussion

The keys in the returned dictionary are the names of properties (attributes or relationships, in the script suite) that have been specified for the command, and the corresponding values in the dictionary are the values that those properties should take. The required and optional arguments for the `make` command are specified in the core suite definition, `NSCoreSuite.scriptSuite`.

## See Also

### Getting information about a create command

- [createClassDescription](createclassdescription.md) — Returns the class description for the class that is to be created.
