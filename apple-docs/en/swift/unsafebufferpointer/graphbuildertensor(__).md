---
title: 'graphBuilderTensor(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafebufferpointer/graphbuildertensor(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/graphbuildertensor(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/graphbuildertensor%28_%3A%29.json'
content_hash: 'sha256:60bf02920366f925'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# graphBuilderTensor(_:)

<sub>Instance Method</sub>

Returns a tensor for the specified BNNS Graph builder.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func graphBuilderTensor(_ builder: BNNSGraph.Builder) -> BNNSGraph.Builder.Tensor<Element>
```

## Discussion

The following code shows how to use this function to register a tensor from an unsafe buffer pointe:.

```swift
   let context = try BNNSGraph.makeContext {
       builder in

       ([1, 2, 3, 4] as [Float]).withUnsafeBufferPointer { x in
           ([5, 6, 7, 8] as [Float]).withUnsafeBufferPointer { y in

               let x = x.graphBuilderTensor(builder)

               let z = x.matmul(transpose: true,
                                other: y)

               return [z] // On return, `z[0]` equals `70`.
           }
       }
   }
```

> [!note] Note
> This function copies the values in `self`.
