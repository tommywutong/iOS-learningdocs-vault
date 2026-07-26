---
title: 'setConstantValues(_:type:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 10.0+, macOS 10.12+, tvOS 10.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunctionconstantvalues/setconstantvalues(_:type:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalues(_:type:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionconstantvalues/setconstantvalues%28_%3Atype%3Arange%3A%29.json'
content_hash: 'sha256:07f7b4afcd97b2b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionConstantValues](../mtlfunctionconstantvalues.md)

# setConstantValues(_:type:range:)

<sub>Instance Method</sub>

Sets values for a group of function constants within a specific index range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setConstantValues(_ values: UnsafeRawPointer, type: MTLDataType, range: Range<Int>)
```

## Parameters

- `values` — A pointer to the constant values.

- `type` — The data type of the function constants.

- `range` — The range of the function constant indices.

## Discussion

Declare multiple function constants in Metal Shading Language (MSL).

```metal
constant bool a [[ function_constant(0) ]];
constant bool b [[ function_constant(1) ]];
constant bool c [[ function_constant(2) ]];
```

Set their values by assigning an index range of an array.

```swift
let abc = [true, true, true]
let constantValues = MTLFunctionConstantValues()
constantValues.setConstantValues(abc,
                                 type: .bool,
                                 with: NSMakeRange(0, 3))
```

## See Also

### Setting constant values

- [- setConstantValue:type:atIndex:](<setconstantvalue(__type_index_).md>) — Sets a value for a function constant at a specific index.
- [- setConstantValue:type:withName:](<setconstantvalue(__type_withname_).md>) — Sets a value for a function constant with a specific name.
