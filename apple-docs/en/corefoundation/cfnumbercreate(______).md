---
title: 'CFNumberCreate(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfnumbercreate(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfnumbercreate(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfnumbercreate%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d239d43b5f617641'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFNumberCreate(_:_:_:)

<sub>Function</sub>

Creates a CFNumber object using a specified value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFNumberCreate(_ allocator: CFAllocator!, _ theType: CFNumberType, _ valuePtr: UnsafeRawPointer!) -> CFNumber!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the default allocator.

- `theType` — A constant that specifies the data type of the value to convert. See [CFNumberType](cfnumbertype.md) for a list of possible values.

- `valuePtr` — A pointer to the value for the returned number object.

## Return Value

A new number with the value specified by `valuePtr`. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The `theType` parameter is not necessarily preserved when creating a new CFNumber object. The CFNumber object will be created using whatever internal storage type the creation function deems appropriate. Use the function [CFNumberGetType](<cfnumbergettype(__).md>) to find out what type the CFNumber object used to store your value.
