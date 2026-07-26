---
title: 'setConstantValue(_:type:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunctionconstantvalues/setconstantvalue(_:type:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalue(_:type:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionconstantvalues/setconstantvalue%28_%3Atype%3Aindex%3A%29.json'
content_hash: 'sha256:f1f8526e90ad47a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionConstantValues](../mtlfunctionconstantvalues.md)

# setConstantValue(_:type:index:)

<sub>Instance Method</sub>

Sets a value for a function constant at a specific index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setConstantValue(_ value: UnsafeRawPointer, type: MTLDataType, index: Int)
```

## Parameters

- `value` — A pointer to the constant value.

- `type` — The data type of the function constant.

- `index` — The index of the function constant.

## Discussion

Declare a single function constant in Metal Shading Language (MSL).

```metal
constant bool a [[ function_constant(0) ]];
```

Set its value by assigning with a specific index.

**Swift**

```swift
var a = true
let constantValues = MTLFunctionConstantValues()
constantValues.setConstantValue(&a, type: .bool, at: 0)
```

**Objective-C**

```objective-c
const bool a = true;
MTLFunctionConstantValues* constantValues = [MTLFunctionConstantValues new];
[constantValues setConstantValue:&a type:MTLDataTypeBool atIndex:0];
```

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Setting constant values

- [- setConstantValue:type:withName:](<setconstantvalue(__type_withname_).md>) — Sets a value for a function constant with a specific name.
- [setConstantValues(_:type:range:)](<setconstantvalues(__type_range_).md>) — Sets values for a group of function constants within a specific index range.
