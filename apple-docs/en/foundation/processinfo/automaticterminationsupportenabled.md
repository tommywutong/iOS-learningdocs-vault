---
title: automaticTerminationSupportEnabled
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/processinfo/automaticterminationsupportenabled
source_url: 'https://developer.apple.com/documentation/foundation/processinfo/automaticterminationsupportenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/processinfo/automaticterminationsupportenabled.json'
content_hash: 'sha256:3161e47002368c30'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [ProcessInfo](../processinfo.md)

# automaticTerminationSupportEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether the app supports automatic termination.

<sub>macOS</sub>

```swift
var automaticTerminationSupportEnabled: Bool { get set }
```

## Discussion

Without setting this property or setting the equivalent `Info.plist` key (`NSSupportsAutomaticTermination`), the methods [- disableAutomaticTermination:](<disableautomatictermination(__).md>) and [- enableAutomaticTermination:](<enableautomatictermination(__).md>) have no effect, although the counter tracking automatic termination opt-outs is still kept up to date to ensure correctness if this is called later. Currently, setting this property to [false](../../swift/false.md) has no effect. This property should be set in the app delegate method [applicationDidFinishLaunching(_:)](<../../appkit/nsapplicationdelegate/applicationdidfinishlaunching(__).md>) or earlier.

## See Also

### Controlling automatic termination

- [- disableAutomaticTermination:](<disableautomatictermination(__).md>) — Disables automatic termination for the application.
- [- enableAutomaticTermination:](<enableautomatictermination(__).md>) — Enables automatic termination for the application.
