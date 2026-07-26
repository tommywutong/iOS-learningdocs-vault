---
title: 'makeResidencySet(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makeresidencyset(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makeresidencyset(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makeresidencyset%28descriptor%3A%29.json'
content_hash: 'sha256:1cf36de8b840dd80'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeResidencySet(descriptor:)

<sub>Instance Method</sub>

Creates a residency set, which can move resources in and out of memory residency.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeResidencySet(descriptor desc: MTLResidencySetDescriptor) throws -> any MTLResidencySet
```

## Parameters

- `desc` — A descriptor instance that configures the residency set the method creates.

## Return Value

A new [MTLResidencySet](../mtlresidencyset.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Discussion

Create an [MTLResidencySet](../mtlresidencyset.md) by creating and configuring an [MTLResidencySetDescriptor](../mtlresidencysetdescriptor.md) instance and pass it to this method.

See [Simplifying GPU resource management with residency sets](../simplifying-gpu-resource-management-with-residency-sets.md) for more information.
