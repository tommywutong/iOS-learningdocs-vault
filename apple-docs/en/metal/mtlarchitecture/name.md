---
title: name
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarchitecture/name
source_url: 'https://developer.apple.com/documentation/metal/mtlarchitecture/name'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarchitecture/name.json'
content_hash: 'sha256:f829049f67235650'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLArchitecture](../mtlarchitecture.md)

# name

<sub>Instance Property</sub>

The name of a GPU device’s architecture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var name: String { get }
```

## Discussion

The property’s value is equivalent to the output from the `metal-arch` command line tool on the same system.

```shell
% xcrun metal-arch
applegpu_g13s
```

Apps can use this property’s value to make decisions at runtime. For example, an app could retrieve a GPU-specific file from its developer’s content delivery network (CDN), such as a shader library or binary archive. See [Shader libraries](../shader-libraries.md) and [Shader library and archive creation](../shader-library-and-archive-creation.md) for more information.
