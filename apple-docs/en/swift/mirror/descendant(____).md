---
title: 'descendant(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mirror/descendant(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/mirror/descendant(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mirror/descendant%28_%3A_%3A%29.json'
content_hash: 'sha256:10bb4dbddf79a2a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Mirror](../mirror.md)

# descendant(_:_:)

<sub>Instance Method</sub>

Returns a specific descendant of the reflected subject, or `nil` if no such descendant exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func descendant(_ first: any MirrorPath, _ rest: any MirrorPath...) -> Any?
```

## Parameters

- `first` — The first mirror path component to access.

- `rest` — Any remaining mirror path components.

## Return Value

The descendant of this mirror specified by the given mirror path components if such a descendant exists; otherwise, `nil`.

## Discussion

Pass a variadic list of string and integer arguments. Each string argument selects the first child with a matching label. Each integer argument selects the child at that offset. For example, passing `1, "two", 3` as arguments to `myMirror.descendant(_:_:)` is equivalent to:

```swift
var result: Any? = nil
let children = myMirror.children
if let i0 = children.index(
    children.startIndex, offsetBy: 1, limitedBy: children.endIndex),
    i0 != children.endIndex
{
    let grandChildren = Mirror(reflecting: children[i0].value).children
    if let i1 = grandChildren.firstIndex(where: { $0.label == "two" }) {
        let greatGrandChildren =
            Mirror(reflecting: grandChildren[i1].value).children
        if let i2 = greatGrandChildren.index(
            greatGrandChildren.startIndex,
            offsetBy: 3,
            limitedBy: greatGrandChildren.endIndex),
            i2 != greatGrandChildren.endIndex
        {
            // Success!
            result = greatGrandChildren[i2].value
        }
    }
}
```

This function is suitable for exploring the structure of a mirror in a REPL or playground, but is not intended to be efficient. The efficiency of finding each element in the argument list depends on the argument type and the capabilities of the each level of the mirror’s `children` collections. Each string argument requires a linear search, and unless the underlying collection supports random-access traversal, each integer argument also requires a linear operation.

## See Also

### Querying Descendants

- [MirrorPath](../mirrorpath.md) — A protocol for legitimate arguments to `Mirror`’s `descendant` method.
