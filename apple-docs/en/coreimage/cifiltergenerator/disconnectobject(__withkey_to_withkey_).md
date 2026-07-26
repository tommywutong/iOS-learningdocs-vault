---
title: 'disconnectObject(_:withKey:to:withKey:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifiltergenerator/disconnectobject(_:withkey:to:withkey:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifiltergenerator/disconnectobject(_:withkey:to:withkey:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifiltergenerator/disconnectobject%28_%3Awithkey%3Ato%3Awithkey%3A%29.json'
content_hash: 'sha256:a646ee009cf13bcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilterGenerator](../cifiltergenerator.md)

# disconnectObject(_:withKey:to:withKey:)

<sub>Instance Method</sub>

Removes the connection between two objects in the filter chain.

<sub>macOS</sub>

```swift
func disconnectObject(_ sourceObject: Any, withKey sourceKey: String, to targetObject: Any, withKey targetKey: String)
```

## Parameters

- `sourceObject` — A [CIFilter](../cifilter-swift.class.md) object, a  [CIImage](../ciimage.md) object, or the path (an [NSString](../../foundation/nsstring.md) or [NSURL](../../foundation/nsurl.md) object) to an image.

- `sourceKey` — The key that specifies the source object. Pass `nil` if the source object is used directly.

- `targetObject` — The object from which you want to disconnect the source object.

- `targetKey` — The key that specifies the target that the source object is currently connected to.

## See Also

### Connecting and Disconnecting Objects

- [- connectObject:withKey:toObject:withKey:](<connect(__withkey_to_withkey_).md>) — Adds an object to the filter chain.
