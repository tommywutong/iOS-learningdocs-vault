---
title: 'CFMessagePortSetInvalidationCallBack(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfmessageportsetinvalidationcallback(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfmessageportsetinvalidationcallback(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfmessageportsetinvalidationcallback%28_%3A_%3A%29.json'
content_hash: 'sha256:fd27e14f7aaa55f6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFMessagePortSetInvalidationCallBack(_:_:)

<sub>Function</sub>

Sets the callback function invoked when a CFMessagePort object is invalidated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFMessagePortSetInvalidationCallBack(_ ms: CFMessagePort!, _ callout: CFMessagePortInvalidationCallBack!)
```

## Parameters

- `ms` — The message port to examine.

- `callout` — The callback function to invoke when `ms` is invalidated. Pass `NULL` to remove a callback.

## Discussion

If `ms` is already invalid, `callout` is invoked immediately.

## See Also

### Configuring a CFMessagePort Object

- [CFMessagePortCreateRunLoopSource](<cfmessageportcreaterunloopsource(______).md>) — Creates a CFRunLoopSource object for a CFMessagePort object.
- [CFMessagePortSetName](<cfmessageportsetname(____).md>) — Sets the name of a local CFMessagePort object.
