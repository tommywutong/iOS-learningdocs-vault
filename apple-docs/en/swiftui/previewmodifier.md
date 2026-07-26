---
title: PreviewModifier
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/previewmodifier
source_url: 'https://developer.apple.com/documentation/swiftui/previewmodifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/previewmodifier.json'
content_hash: 'sha256:19f944aa1a3317a2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# PreviewModifier

<sub>Protocol</sub>

A type that defines an environment in which previews can appear.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor protocol PreviewModifier
```

## Overview

Conforming types can define shared contexts that will be cached by the preview system, then reused across participating previews. For example, you might create a model container here and populate it with sample data; in your `body` method you would then apply it to the preview using the `.modelContainer` view modifier.

```swift
struct SampleData: PreviewModifier {
    static func makeSharedContext() throws -> ModelContainer {
        let container = try ModelContainer(for: Snack.self)
        container.mainContext.insert(Snack.potatoChips)
        return container
    }

    func body(content: Content, context: ModelContainer) -> some View {
        content.modelContainer(context)
    }
 }
```

Use the `.modifier` preview trait to attach modifiers to a preview.

```swift
#Preview(traits: .modifier(SampleData())) {
    @Previewable @Query var snacks: [Snack]
    return SnackView(snack: snacks.first!)
}
```

## Topics

### Associated Types

- [Body](previewmodifier/body.md)
- [Context](previewmodifier/context.md)

### Instance Methods

- [body(content:context:)](<previewmodifier/body(content_context_).md>) — Modify a preview by applying the shared context.

### Type Aliases

- [Content](previewmodifier/content.md) — The type-erased content of a preview.

### Type Methods

- [makeSharedContext()](<previewmodifier/makesharedcontext().md>) — Create shared context to apply to previews. The context returned here will be cached and passed into the `body` method for every preview that applies a modifier of this type.

## See Also

### Customizing a preview

- [Previewable()](<previewable().md>) — Tag allowing a dynamic property to appear inline in a preview.
- [PreviewModifierContent](previewmodifiercontent.md) — The type-erased content of a preview.
