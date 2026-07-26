---
title: 'unsafeDowncast(_:to:)'
framework: Swift
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafedowncast(_:to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafedowncast(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafedowncast%28_%3Ato%3A%29.json'
content_hash: 'sha256:1861fe84ff822076'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# unsafeDowncast(_:to:)

<sub>Function</sub>

Returns the given instance cast unconditionally to the specified type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unsafeDowncast<T>(_ x: AnyObject, to type: T.Type) -> T where T : AnyObject
```

## Parameters

- `x` — An instance to cast to type `T`.

- `type` — The type `T` to which `x` is cast.

## Return Value

The instance `x`, cast to type `T`.

## Discussion

The instance passed as `x` must be an instance of type `T`.

Use this function instead of `unsafeBitcast(_:to:)` because this function is more restrictive and still performs a check in debug builds. In -O builds, no test is performed to ensure that `x` actually has the dynamic type `T`.

> [!warning] Warning
> This function trades safety for performance. Use `unsafeDowncast(_:to:)` only when you are confident that `x is T` always evaluates to `true`, and only after `x as! T` has proven to be a performance problem.

## See Also

### Instance Casting

- [unsafeBitCast(_:to:)](<unsafebitcast(__to_).md>) — Returns the bits of the given instance, interpreted as having the specified type.
