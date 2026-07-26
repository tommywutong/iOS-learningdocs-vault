---
title: 'loadSuite(with:from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsscriptsuiteregistry/loadsuite(with:from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/loadsuite(with:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsscriptsuiteregistry/loadsuite%28with%3Afrom%3A%29.json'
content_hash: 'sha256:50e31547830d6659'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSScriptSuiteRegistry](../nsscriptsuiteregistry.md)

# loadSuite(with:from:)

<sub>Instance Method</sub>

Loads the suite definition encapsulated in `dictionary`; previously, this suite definition was parsed from a `.scriptSuite` property list contained in a framework or in `bundle`.

<sub>Mac Catalyst, macOS</sub>

```swift
func loadSuite(with suiteDeclaration: [AnyHashable : Any], from bundle: Bundle)
```

## Discussion

The method extracts information from the dictionary and caches it in various internal collection objects. If keys are missing or values are of the wrong type, it logs messages to the console. It also registers class descriptions and command descriptions. In registering a class description, it invokes the [NSClassDescription](../nsclassdescription.md) class method [+ registerClassDescription:forClass:](<../nsclassdescription/register(__for_).md>). In registering a command description, it arranges for the Apple event translator to handle incoming Apple events that represent the defined commands.

This method is invoked when the shared instance is initialized and when bundles are loaded at runtime. Prior to invoking it, `NSScriptSuiteRegistry` creates the dictionary argument from the `.scriptSuite` property list. If you invoke this method in your code, you should try to do it before the application receives its first Apple event.

## See Also

### Related Documentation

- [- registerClassDescription:](<register(__)-9aplw.md>) — Registers class description `classDescription` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the class name.
- [+ sharedScriptSuiteRegistry](<shared().md>) — Returns the single, shared instance of `NSScriptSuiteRegistry`, creating it first if it doesn’t exist.
- [- registerCommandDescription:](<register(__)-5mq91.md>) — Registers command description `commandDesc` for use by Cocoa’s built-in scripting support by storing it in a per-suite internal dictionary under the command name.

### Loading Suites

- [- loadSuitesFromBundle:](<loadsuites(from_).md>) — Loads the suite definitions in bundle `aBundle`, invoking [- loadSuiteWithDictionary:fromBundle:](<loadsuite(with_from_).md>) for each suite found.
