---
title: 'CFPlugInInstanceGetInstanceData(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfplugininstancegetinstancedata(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugininstancegetinstancedata(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugininstancegetinstancedata%28_%3A%29.json'
content_hash: 'sha256:36bd6fda315a0b3f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInInstanceGetInstanceData(_:)

<sub>Function</sub>

Not recommended.

> [!warning] Deprecated
> Use UUID-based plugins instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInInstanceGetInstanceData(_ instance: CFPlugInInstance!) -> UnsafeMutableRawPointer!
```

## See Also

### Deprecated

- [CFPlugInInstanceCreateWithInstanceDataSize](<cfplugininstancecreatewithinstancedatasize(__________).md>) — Not recommended. _(deprecated)_
- [CFPlugInInstanceGetFactoryName](<cfplugininstancegetfactoryname(__).md>) — Not recommended. _(deprecated)_
- [CFPlugInInstanceGetInterfaceFunctionTable](<cfplugininstancegetinterfacefunctiontable(______).md>) — Not recommended. _(deprecated)_
- [CFPlugInInstanceGetTypeID](<cfplugininstancegettypeid().md>) — Not recommended. _(deprecated)_
