---
title: waitUntilCompleted()
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/cirendertask/waituntilcompleted()
source_url: 'https://developer.apple.com/documentation/coreimage/cirendertask/waituntilcompleted()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cirendertask/waituntilcompleted%28%29.json'
content_hash: 'sha256:d71de21cb170174d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIRenderTask](../cirendertask.md)

# waitUntilCompleted()

<sub>Instance Method</sub>

Waits until the [CIRenderTask](../cirendertask.md) finishes and returns.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func waitUntilCompleted() throws -> CIRenderInfo
```

## Discussion

Synchronously blocks execution until the [CIRenderTask](../cirendertask.md) either completes or fails (with error).  Calling this method after [- startTaskToRender:toDestination:error:](<../cicontext/starttask(torender_to_).md>) or [- startTaskToRender:fromRect:toDestination:atPoint:error:](<../cicontext/starttask(torender_from_to_at_).md>) makes the render task behave synchronously, as if the CPU and GPU were operating as a single unit.
