---
title: maximumConcurrentCompilationTaskCount
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 13.3+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/maximumconcurrentcompilationtaskcount
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maximumconcurrentcompilationtaskcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maximumconcurrentcompilationtaskcount.json'
content_hash: 'sha256:ae1d080eaac1238b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# maximumConcurrentCompilationTaskCount

<sub>Instance Property</sub>

The maximum number of concurrent compilation tasks the device is running.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maximumConcurrentCompilationTaskCount: Int { get }
```

## Discussion

The property’s value can change when you set the [shouldMaximizeConcurrentCompilation](shouldmaximizeconcurrentcompilation.md) property to a new value.
