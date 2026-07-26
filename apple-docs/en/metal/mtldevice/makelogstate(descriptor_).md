---
title: 'makeLogState(descriptor:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makelogstate(descriptor:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makelogstate(descriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makelogstate%28descriptor%3A%29.json'
content_hash: 'sha256:245f4141f6b7f449'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeLogState(descriptor:)

<sub>Instance Method</sub>

Creates a shader log state with the provided configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeLogState(descriptor: MTLLogStateDescriptor) throws -> any MTLLogState
```

## Parameters

- `descriptor` — The configuration for the new shader log state.

## Return Value

A new [MTLLogState](../mtllogstate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.
