---
title: NavigationPath
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationpath
source_url: 'https://developer.apple.com/documentation/swiftui/navigationpath'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationpath.json'
content_hash: 'sha256:70abeb1d1c5fd2b5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# NavigationPath

<sub>Structure</sub>

A type-erased list of data representing the content of a navigation stack.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NavigationPath
```

## Overview

You can manage the state of a [NavigationStack](navigationstack.md) by initializing the stack with a binding to a collection of data. The stack stores data items in the collection for each view on the stack. You also can read and write the collection to observe and alter the stack’s state.

When a stack displays views that rely on only one kind of data, you can use a standard collection, like an array, to hold the data. If you need to present different kinds of data in a single stack, use a navigation path instead. The path uses type erasure so you can manage a collection of heterogeneous elements. The path also provides the usual collection controls for adding, counting, and removing data elements.

### Serialize the path

When the values you present on the navigation stack conform to the [Codable](../swift/codable.md) protocol, you can use the path’s [codable](navigationpath/codable.md) property to get a serializable representation of the path. Use that representation to save and restore the contents of the stack. For example, you can define an [ObservableObject](../combine/observableobject.md) that handles serializing and deserializing the path:

```swift
class MyModelObject: ObservableObject {
    @Published var path: NavigationPath

    static func readSerializedData() -> Data? {
        // Read data representing the path from app's persistent storage.
    }

    static func writeSerializedData(_ data: Data) {
        // Write data representing the path to app's persistent storage.
    }

    init() {
        if let data = Self.readSerializedData() {
            do {
                let representation = try JSONDecoder().decode(
                    NavigationPath.CodableRepresentation.self,
                    from: data)
                self.path = NavigationPath(representation)
            } catch {
                self.path = NavigationPath()
            }
        } else {
            self.path = NavigationPath()
        }
    }

    func save() {
        guard let representation = path.codable else { return }
        do {
            let encoder = JSONEncoder()
            let data = try encoder.encode(representation)
            Self.writeSerializedData(data)
        } catch {
            // Handle error.
        }
    }
}
```

Then, using that object in your view, you can save the state of the navigation path when the [Scene](scene.md) enters the [ScenePhase.background](scenephase/background.md) state:

```swift
@StateObject private var pathState = MyModelObject()
@Environment(\.scenePhase) private var scenePhase

var body: some View {
    NavigationStack(path: $pathState.path) {
        // Add a root view here.
    }
    .onChange(of: scenePhase) { phase in
        if phase == .background {
            pathState.save()
        }
    }
}
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md)

## Topics

### Creating a navigation path

- [init()](<navigationpath/init().md>) — Creates a new, empty navigation path.
- [init(_:)](<navigationpath/init(__).md>) — Creates a new navigation path from a serializable version.

### Managing path contents

- [isEmpty](navigationpath/isempty.md) — A Boolean that indicates whether this path is empty.
- [count](navigationpath/count.md) — The number of elements in this path.
- [append(_:)](<navigationpath/append(__).md>) — Appends a new codable value to the end of this path.
- [removeLast(_:)](<navigationpath/removelast(__).md>) — Removes values from the end of this path.

### Encoding a path

- [codable](navigationpath/codable.md) — A value that describes the contents of this path in a serializable format.
- [CodableRepresentation](navigationpath/codablerepresentation.md) — A serializable representation of a navigation path.

## See Also

### Stacking views in one column

- [NavigationStack](navigationstack.md) — A view that displays a root view and enables you to present additional views over the root view.
- [navigationDestination(for:destination:)](<view/navigationdestination(for_destination_).md>) — Associates a destination view with a presented data type for use within a navigation stack.
- [navigationDestination(isPresented:destination:)](<view/navigationdestination(ispresented_destination_).md>) — Associates a destination view with a binding that can be used to push the view onto a [NavigationStack](navigationstack.md).
- [navigationDestination(item:destination:)](<view/navigationdestination(item_destination_).md>) — Associates a destination view with a bound value for use within a navigation stack or navigation split view
