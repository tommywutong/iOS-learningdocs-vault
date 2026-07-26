---
title: 'init(name:parameters:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coreimage/cifilter-swift.class/init(name:parameters:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cifilter-swift.class/init(name:parameters:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cifilter-swift.class/init%28name%3Aparameters%3A%29.json'
content_hash: 'sha256:1b5762f3bd7fb5eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIFilter](../cifilter-swift.class.md)

# init(name:parameters:)

<sub>Initializer</sub>

Creates a new filter of type ‘name’. The filter’s input parameters are set from the dictionary of key-value pairs. On OSX, any of the filter input parameters not specified in the dictionary will be undefined. On iOS, any of the filter input parameters not specified in the dictionary will be set to default values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(name: String, parameters params: [String : Any]?)
```
