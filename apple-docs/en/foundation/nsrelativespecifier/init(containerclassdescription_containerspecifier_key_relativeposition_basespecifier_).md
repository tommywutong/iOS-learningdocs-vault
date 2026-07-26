---
title: 'init(containerClassDescription:containerSpecifier:key:relativePosition:baseSpecifier:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsrelativespecifier/init(containerclassdescription:containerspecifier:key:relativeposition:basespecifier:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsrelativespecifier/init(containerclassdescription:containerspecifier:key:relativeposition:basespecifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsrelativespecifier/init%28containerclassdescription%3Acontainerspecifier%3Akey%3Arelativeposition%3Abasespecifier%3A%29.json'
content_hash: 'sha256:5e33b6a5aae2601e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSRelativeSpecifier](../nsrelativespecifier.md)

# init(containerClassDescription:containerSpecifier:key:relativePosition:baseSpecifier:)

<sub>Initializer</sub>

Invokes the super class’s [- initWithContainerClassDescription:containerSpecifier:key:](<../nsscriptobjectspecifier/init(containerclassdescription_containerspecifier_key_).md>) method and initializes the relative position and base specifier to `relPos` and `baseSpecifier`.

<sub>Mac Catalyst, macOS</sub>

```swift
init(containerClassDescription classDesc: NSScriptClassDescription, containerSpecifier container: NSScriptObjectSpecifier?, key property: String, relativePosition relPos: NSRelativeSpecifier.RelativePosition, baseSpecifier: NSScriptObjectSpecifier?)
```

## See Also

### Related Documentation

- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
