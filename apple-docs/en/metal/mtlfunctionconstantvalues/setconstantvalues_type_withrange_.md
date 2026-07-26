---
title: 'setConstantValues:type:withRange:'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlfunctionconstantvalues/setconstantvalues:type:withrange:'
source_url: 'https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues/setconstantvalues:type:withrange:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlfunctionconstantvalues/setconstantvalues%3Atype%3Awithrange%3A.json'
content_hash: 'sha256:ad5c6cc6b0a16ab6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLFunctionConstantValues](../mtlfunctionconstantvalues.md)

# setConstantValues:type:withRange:

<sub>Instance Method</sub>

Sets values for a group of function constants within a specific index range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
- (void) setConstantValues:(const void *) values type:(MTLDataType) type withRange:(NSRange) range;
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

```objective-c
const bool abc[3] = { true, true, true };
MTLFunctionConstantValues* constantValues = [MTLFunctionConstantValues new];
[constantValues setConstantValues:&abc
                             type:MTLDataTypeBool
                        withRange:NSMakeRange(0, 3)];
```

## See Also

### Setting constant values

- [- setConstantValue:type:atIndex:](<setconstantvalue(__type_index_).md>) — Sets a value for a function constant at a specific index.
- [- setConstantValue:type:withName:](<setconstantvalue(__type_withname_).md>) — Sets a value for a function constant with a specific name.
