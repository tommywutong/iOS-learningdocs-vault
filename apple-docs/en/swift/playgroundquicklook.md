---
title: PlaygroundQuickLook
framework: Swift
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（4.2 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/swift/playgroundquicklook
source_url: 'https://developer.apple.com/documentation/swift/playgroundquicklook'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/playgroundquicklook.json'
content_hash: 'sha256:272cd288be17c411'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift](../swift.md)

# PlaygroundQuickLook

<sub>Type Alias</sub>

The sum of types that can be used as a Quick Look representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias PlaygroundQuickLook
```

## Discussion

The `PlaygroundQuickLook` protocol is deprecated, and will be removed from the standard library in a future Swift release. To customize the logging of your type in a playground, conform to the `CustomPlaygroundDisplayConvertible` protocol, which does not use the `PlaygroundQuickLook` enum.

If you need to provide a customized playground representation in Swift 4.0 or Swift 3.2 or earlier, use a conditional compilation block:

```swift
#if swift(>=4.1) || (swift(>=3.3) && !swift(>=4.0))
    // With Swift 4.1 and later (including Swift 3.3 and later), use
    // the CustomPlaygroundDisplayConvertible protocol.
#else
    // With Swift 4.0 and Swift 3.2 and earlier, use PlaygroundQuickLook
    // and the CustomPlaygroundQuickLookable protocol.
#endif
```

## See Also

### Customizing Your Type’s Reflection

- [CustomReflectable](customreflectable.md) — A type that explicitly supplies its own mirror.
- [CustomLeafReflectable](customleafreflectable.md) — A type that explicitly supplies its own mirror, but whose descendant classes are not represented in the mirror unless they also override `customMirror`.
- [CustomPlaygroundDisplayConvertible](customplaygrounddisplayconvertible.md) — A type that supplies a custom description for playground logging.
- [DebugDescription()](<debugdescription().md>) — Converts description definitions to a debugger Type Summary.
