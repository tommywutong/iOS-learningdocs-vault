---
title: 'withValue(_:operation:isolation:file:line:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/tasklocal/withvalue(_:operation:isolation:file:line:)'
source_url: 'https://developer.apple.com/documentation/swift/tasklocal/withvalue(_:operation:isolation:file:line:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/tasklocal/withvalue%28_%3Aoperation%3Aisolation%3Afile%3Aline%3A%29.json'
content_hash: 'sha256:4d298c835a326cde'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [TaskLocal](../tasklocal.md)

# withValue(_:operation:isolation:file:line:)

<sub>Instance Method</sub>

> [!warning] Deprecated
> Prefer the 'nonisolated(nonsending)' overload with stricter execution on caller context semantics: withValue(_:operation:file:line:)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@backDeployed(before: macOS 15.0, iOS 18.0, watchOS 11.0, tvOS 18.0, visionOS 2.0)
@discardableResult final func withValue<R>(_ valueDuringOperation: Value, operation: () async throws -> R, isolation: isolated (any Actor)? = #isolation, file: String = #fileID, line: UInt = #line) async rethrows -> R
```
