---
title: 'constantData(at:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlargumentencoder/constantdata(at:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlargumentencoder/constantdata(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlargumentencoder/constantdata%28at%3A%29.json'
content_hash: 'sha256:e89d766d78b6f4c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArgumentEncoder](../mtlargumentencoder.md)

# constantData(at:)

<sub>Instance Method</sub>

Returns a pointer to an inline, constant-data argument within the argument buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func constantData(at index: Int) -> UnsafeMutableRawPointer
```

## Parameters

- `index` — The index of an inline, constant-data argument within the argument buffer. The value corresponds to either the index ID of a declaration in Metal Shading Language (MSL) or the [index](../mtlargumentdescriptor/index.md) property of an [MTLArgumentDescriptor](../mtlargumentdescriptor.md) instance.

## Return Value

A pointer to the location in the buffer to which you should write the constant data.

## Discussion

Constants declared contiguously in the Metal shading language (in an array or structure) are contiguous in memory. You can encode contiguous ranges of inlined constant data through a pointer to the first constant.

To encode inlined constant data into the argument buffer, perform a memory copy operation from your data’s source pointer to the returned destination pointer.

**Swift**

```swift
let sourceConstants: [SourceConstants] = [
    // Inlined constant data.
    /* ... */
]
let destinationPointer = abEncoder.constantData(: 0)
destinationPointer.copyBytes(from: sourceConstants, count: MemoryLayout<SourceConstants>.size)
```

**Objective-C**

```objective-c
static const SourceConstants sourceConstants[] =
{    
    // Inlined constant data.
    /* ... */
};
void *destinationPointer = [abEncoder constantDataAtIndex:0];
memcpy(destinationPointer, sourceConstants, sizeof(SourceConstants));
```
