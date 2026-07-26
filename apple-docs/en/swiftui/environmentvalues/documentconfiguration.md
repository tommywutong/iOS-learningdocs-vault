---
title: documentConfiguration
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/environmentvalues/documentconfiguration
source_url: 'https://developer.apple.com/documentation/swiftui/environmentvalues/documentconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/environmentvalues/documentconfiguration.json'
content_hash: 'sha256:f6e2043dc657b845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [EnvironmentValues](../environmentvalues.md)

# documentConfiguration

<sub>Instance Property</sub>

The configuration of a document in a [DocumentGroup](../documentgroup.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var documentConfiguration: DocumentConfiguration? { get }
```

## Discussion

The value is `nil` for views that are not enclosed in a [DocumentGroup](../documentgroup.md).

For example, if the app shows the document path in the footer of each document, it can get the URL from the environment:

```swift
struct ContentView: View {
    @Binding var document: TextDocument
    @Environment(\.documentConfiguration) private var configuration: DocumentConfiguration?

    var body: some View {
        …
        Label(
            configuration?.fileURL?.path ??
                "", systemImage: "folder.circle"
        )
    }
}
```

## See Also

### Accessing document configuration

- [DocumentConfiguration](../documentconfiguration.md) — The configuration of a document in a [DocumentGroup](../documentgroup.md).
- [undoManager](undomanager.md) — The undo manager used to register a view’s undo operations.
