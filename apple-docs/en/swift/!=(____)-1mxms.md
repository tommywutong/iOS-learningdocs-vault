---
title: '!=(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/!=(_:_:)-1mxms'
source_url: 'https://developer.apple.com/documentation/swift/!=(_:_:)-1mxms'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/%21%3D%28_%3A_%3A%29-1mxms.json'
content_hash: 'sha256:f135c537deeaa7e3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# !=(_:_:)

<sub>Operator</sub>

Returns a Boolean value indicating whether two types are not identical.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func != (t0: (any (~Copyable & ~Escapable).Type)?, t1: (any (~Copyable & ~Escapable).Type)?) -> Bool
```

## Parameters

- `t0` — A type to compare.

- `t1` — Another type to compare.

## Return Value

`true` if one, but not both, of `t0` and `t1` are `nil`, or if they represent different types; otherwise, `false`.

## See Also

### Tuple Comparison

- [==(_:_:)](<==(____)-958in.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-2htbb.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-h88g.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-7lhq7.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-1hbor.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-1ud2a.md>) — Returns a Boolean value indicating whether the corresponding components of two tuples are equal.
- [==(_:_:)](<==(____)-9kf9y.md>) — Returns a Boolean value indicating whether two types are identical.
- [!=(_:_:)](<!=(____)-18co7.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-7er1l.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-754t2.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-7ao4l.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-4fzl6.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
- [!=(_:_:)](<!=(____)-3nrcc.md>) — Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.
