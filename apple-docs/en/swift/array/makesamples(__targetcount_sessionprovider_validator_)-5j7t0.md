---
title: 'makeSamples(_:targetCount:sessionProvider:validator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/array/makesamples(_:targetcount:sessionprovider:validator:)-5j7t0'
source_url: 'https://developer.apple.com/documentation/swift/array/makesamples(_:targetcount:sessionprovider:validator:)-5j7t0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/makesamples%28_%3Atargetcount%3Asessionprovider%3Avalidator%3A%29-5j7t0.json'
content_hash: 'sha256:72a6143f720e02ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# makeSamples(_:targetCount:sessionProvider:validator:)

<sub>Instance Method</sub>

Generates synthetic data based on this dataset and returns a stream of new samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func makeSamples<T>(_ prompt: Prompt, targetCount: Int, sessionProvider: (@Sendable () -> LanguageModelSession)? = nil, validator: (nonisolated(nonsending) @Sendable (ModelSample<T>) async throws -> Bool)? = nil) -> some AsyncSequence<ModelSample<T>, any Error> where Element == ModelSample<T>, T : Generable, T : Decodable, T : Encodable, T : Sendable

```

## Discussion

For more control over generation, create a `SampleGenerator` directly.
