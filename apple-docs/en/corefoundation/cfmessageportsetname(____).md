---
title: 'CFMessagePortSetName(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportsetname(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportsetname(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportsetname%28_%3A_%3A%29.json'
content_hash: 'sha256:fcbd4fbd0fe765d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortSetName(_:_:)

<sub>Function</sub>

Sets the name of a local CFMessagePort object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortSetName(_ ms: CFMessagePort!, _ newName: CFString!) -> Bool
```

## Parameters

- `ms` — The local message port to examine.

- `newName` — The new name for `ms`.

## Return Value

`true` if the name change succeeds, otherwise `false`.

## Discussion

Other threads and processes can connect to a named message port with [CFMessagePortCreateRemote](<cfmessageportcreateremote(____).md>).

## See Also

### Configuring a CFMessagePort Object

- [CFMessagePortCreateRunLoopSource](<cfmessageportcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFMessagePort object.
- [CFMessagePortSetInvalidationCallBack](<cfmessageportsetinvalidationcallback(____).md>) — Sets the callback function invoked when a CFMessagePort object is invalidated.
