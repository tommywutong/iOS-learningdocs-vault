---
title: 'graphBuilderTensor(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/graphbuildertensor(_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/graphbuildertensor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/graphbuildertensor%28_%3A%29.json'
content_hash: 'sha256:f711f07bc7772ab4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# graphBuilderTensor(_:)

<sub>Instance Method</sub>

Returns a tensor for the specified BNNS Graph builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func graphBuilderTensor(_ builder: BNNSGraph.Builder) -> BNNSGraph.Builder.Tensor<Element>
```

## Discussion

The following code shows how to use this function to register a tensor from an array.

```swift
   let x = [1, 2, 3, 4] as [Float]
   let y = [5, 6, 7, 8] as [Float]

   let context = try BNNSGraph.makeContext {
       builder in

       let x = lhs.graphBuilderTensor(builder)

       let z = x.matmul(transpose: true,
                        other: y)

       return [z] // On return, `z[0]` equals `70`.
   }
```
