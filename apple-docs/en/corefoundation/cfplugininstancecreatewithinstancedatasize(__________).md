---
title: 'CFPlugInInstanceCreateWithInstanceDataSize(_:_:_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.0+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfplugininstancecreatewithinstancedatasize(_:_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfplugininstancecreatewithinstancedatasize(_:_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfplugininstancecreatewithinstancedatasize%28_%3A_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:0a2b74ccfc6d88b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPlugInInstanceCreateWithInstanceDataSize(_:_:_:_:_:)

<sub>Function</sub>

Not recommended.

> [!warning] Deprecated
> Use UUID-based plugins instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFPlugInInstanceCreateWithInstanceDataSize(_ allocator: CFAllocator!, _ instanceDataSize: CFIndex, _ deallocateInstanceFunction: CFPlugInInstanceDeallocateInstanceDataFunction!, _ factoryName: CFString!, _ getInterfaceFunction: CFPlugInInstanceGetInterfaceFunction!) -> CFPlugInInstance!
```

## See Also

### Deprecated

- [CFPlugInInstanceGetFactoryName](<cfplugininstancegetfactoryname(__).md>) — Not recommended. _(deprecated)_
- [CFPlugInInstanceGetInstanceData](<cfplugininstancegetinstancedata(__).md>) — Not recommended. _(deprecated)_
- [CFPlugInInstanceGetInterfaceFunctionTable](<cfplugininstancegetinterfacefunctiontable(______).md>) — Not recommended. _(deprecated)_
- [CFPlugInInstanceGetTypeID](<cfplugininstancegettypeid().md>) — Not recommended. _(deprecated)_
