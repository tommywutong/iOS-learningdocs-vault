---
title: 'setConstantValue(_:type:withName:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunctionconstantvalues/setconstantvalue(_:type:withname:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalue(_:type:withname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionconstantvalues/setconstantvalue%28_%3Atype%3Awithname%3A%29.json'
content_hash: 'sha256:35b756a4f0d5e3b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionConstantValues](../mtlfunctionconstantvalues.md)

# setConstantValue(_:type:withName:)

<sub>Instance Method</sub>

Sets a value for a function constant with a specific name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setConstantValue(_ value: UnsafeRawPointer, type: MTLDataType, withName name: String)
```

## Parameters

- `value` — A pointer to the constant value.

- `type` — The data type of the function constant.

- `name` — The name of the function constant.

## Discussion

The first example declares a single function constant in a Metal Shading Language file.

```metal
constant bool a [[ function_constant(0) ]];
```

The next example sets that Boolean value by providing its specific name.

**Swift**

```swift
var a = true
let constantValues = MTLFunctionConstantValues()
constantValues.setConstantValue(&a, type: .bool, withName: "a")
```

**Objective-C**

```objective-c
const bool a = true;
MTLFunctionConstantValues* constantValues = [MTLFunctionConstantValues new];
[constantValues setConstantValue:&a type:MTLDataTypeBool withName:@"a"];
```

## See Also

### Setting constant values

- [- setConstantValue:type:atIndex:](<setconstantvalue(__type_index_).md>) — Sets a value for a function constant at a specific index.
- [setConstantValues(_:type:range:)](<setconstantvalues(__type_range_).md>) — Sets values for a group of function constants within a specific index range.
