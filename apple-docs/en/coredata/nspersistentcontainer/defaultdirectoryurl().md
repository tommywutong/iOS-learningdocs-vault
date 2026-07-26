---
title: defaultDirectoryURL()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentcontainer/defaultdirectoryurl()
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentcontainer/defaultdirectoryurl()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentcontainer/defaultdirectoryurl%28%29.json'
content_hash: 'sha256:006ffc45b6313d9a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentContainer](../nspersistentcontainer.md)

# defaultDirectoryURL()

<sub>Type Method</sub>

Returns the location of the directory that contains the persistent stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func defaultDirectoryURL() -> URL
```

## Return Value

An [NSURL](../../foundation/nsurl.md) that references the directory in which the persistent store(s) will be located or are currently located.

## Discussion

This method returns a platform-dependent [NSURL](../../foundation/nsurl.md) at which the persistent store(s) will be located or are currently located. This method can be overridden in a subclass of [NSPersistentContainer](../nspersistentcontainer.md).

## See Also

### Accessing the Default Directory

- [defaultDirectoryURL](defaultdirectoryurl-swift.type.property.md) — The location of the directory that contains the persistent stores.
