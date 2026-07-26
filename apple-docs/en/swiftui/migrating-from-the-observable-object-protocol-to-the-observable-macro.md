---
title: Migrating from the Observable Object protocol to the Observable macro
framework: SwiftUI
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, Xcode 15.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro
source_url: 'https://developer.apple.com/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/migrating-from-the-observable-object-protocol-to-the-observable-macro.json'
content_hash: 'sha256:b766eade906c5e9b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Model data](model-data.md)

# Migrating from the Observable Object protocol to the Observable macro

<sub>Sample Code</sub>

Update your existing app to leverage the benefits of Observation in Swift.

## Overview

Starting with iOS 17, iPadOS 17, macOS 14, tvOS 17, and watchOS 10, SwiftUI provides support for [Observation](../observation.md), a Swift-specific implementation of the observer design pattern. Adopting Observation provides your app with the following benefits:

- Tracking optionals and collections of objects, which isn’t possible when using [ObservableObject](../combine/observableobject.md).
- Using existing data flow primitives like [State()](<state().md>) and [Environment](environment.md) instead of object-based equivalents such as [StateObject](stateobject.md) and [EnvironmentObject](environmentobject.md).
- Updating views based on changes to the observable properties that a view’s [body](view/body-8kl5o.md) reads instead of any property changes that occur to an observable object, which can help improve your app’s performance.

To take advantage of these benefits in your app, you’ll discover how to replace existing source code that relies on [ObservableObject](../combine/observableobject.md) with code that leverages the [Observable()](<../observation/observable().md>) macro.

> [!note] Note
> Download this sample to see the migrated version of the sample app. To see the premigrated version, download the sample available in [Monitoring data changes in your app](monitoring-model-data-changes-in-your-app.md). You can also use the premigrated version to code along with this article.

### Use the Observable macro

To adopt [Observation](../observation.md) in an existing app, begin by replacing [ObservableObject](../combine/observableobject.md) in your data model type with the [Observable()](<../observation/observable().md>) macro. The [Observable()](<../observation/observable().md>) macro generates source code at compile time that adds observation support to the type.

```swift
// BEFORE
import SwiftUI

class Library: ObservableObject {
    // ...
}
```

```swift
// AFTER
import SwiftUI

@Observable class Library {
    // ...
}
```

Then remove the [Published](../combine/published.md) property wrapper from observable properties. Observation doesn’t require a property wrapper to make a property observable. Instead, the accessibility of the property in relationship to an observer, such as a view, determines whether a property is observable.

```swift
// BEFORE
class Library {
    @Published var books: [Book] = [Book(), Book(), Book()]
}
```

```swift
// AFTER
@Observable class Library {
    var books: [Book] = [Book(), Book(), Book()]
}
```

If you have properties that are accessible to an observer that you don’t want to track, apply the [ObservationIgnored()](<../observation/observationignored().md>) macro to the property.

### Migrate incrementally

You don’t need to make a wholesale replacement of the [ObservableObject](../combine/observableobject.md) protocol throughout your app. Instead, you can make changes incrementally. Start by changing one data model type to use the [Observable()](<../observation/observable().md>) macro. Your app can mix data model types that use different observation systems. However, SwiftUI tracks changes differently based on the observation system that a data model type uses, `Observable` versus `ObservableObject`.

You may notice slight behavioral differences in your app based on the tracking method. For instance, when tracking as [Observable()](<../observation/observable().md>), SwiftUI updates a view only when an observable property changes and the view’s [body](view/body-8kl5o.md) reads the property directly. The view doesn’t update when observable properties not read by `body` changes. In contrast, a view updates when any published property of an [ObservableObject](../combine/observableobject.md) instance changes, even if the view doesn’t read the property that changes, when tracking as `ObservableObject`.

> [!note] Note
> To learn more about when SwiftUI updates views when observable properties change, see [Managing model data in your app](managing-model-data-in-your-app.md).

### Migrate other source code

The only change made to the sample app so far is to apply the [Observable()](<../observation/observable().md>) macro to `Library` and remove support for the [ObservableObject](../combine/observableobject.md) protocol. The app still uses the [ObservableObject](../combine/observableobject.md) data flow primitive like [StateObject](stateobject.md) to manage an instance of `Library`. If you were to build and run the app, SwiftUI still updates the views as expected. That’s because data flow property wrappers such as [StateObject](stateobject.md) and [EnvironmentObject](environmentobject.md) support types that use the [Observable()](<../observation/observable().md>) macro. SwiftUI provides this support so apps can make source code changes incrementally.

However, to fully adopt [Observation](../observation.md), replace the use of [StateObject](stateobject.md) with [State()](<state().md>) after updating your data model type. For example, in the following code the main app structure creates an instance of `Library` and stores it as a `StateObject`. It also adds the `Library` instance to the environment using the [environmentObject(_:)](<view/environmentobject(__).md>) modifier.

```swift
// BEFORE
@main
struct BookReaderApp: App {
    @StateObject private var library = Library()

    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environmentObject(library)
        }
    }
}
```

Now that `Library` no longer conforms to [ObservableObject](../combine/observableobject.md), the code can change to use [State()](<state().md>) instead of [StateObject](stateobject.md) and to add `library` to the environment using the [environment(_:)](<view/environment(__).md>) modifier.

```swift
// AFTER
@main
struct BookReaderApp: App {
    @State private var library = Library()

    var body: some Scene {
        WindowGroup {
            LibraryView()
                .environment(library)
        }
    }
}
```

One more change must happen before `Library` fully adopts [Observation](../observation.md). Previously the view `LibraryView` retrieved a `Library` instance from the environment using the [EnvironmentObject](environmentobject.md) property wrapper. The new code, however, uses the [Environment](environment.md) property wrapper instead.

```swift
// BEFORE
struct LibraryView: View {
    @EnvironmentObject var library: Library

    var body: some View {
        List(library.books) { book in
            BookView(book: book)
        }
    }
}
```

```swift
// AFTER
struct LibraryView: View {
    @Environment(Library.self) private var library
    
    var body: some View {
        List(library.books) { book in
            BookView(book: book)
        }
    }
}
```

### Remove the ObservedObject property wrapper

To wrap up the migration of the sample app, change the data model type `Book` to support [Observation](../observation.md) by removing [ObservableObject](../combine/observableobject.md) from the type declaration and apply the [Observable()](<../observation/observable().md>) macro. Then remove the [Published](../combine/published.md) property wrapper from observable properties.

```swift
// BEFORE
class Book: ObservableObject, Identifiable {
    @Published var title = "Sample Book Title"
    
    let id = UUID() // A unique identifier that never changes.
}
```

```swift
// AFTER
@Observable class Book: Identifiable {
    var title = "Sample Book Title"
    
    let id = UUID() // A unique identifier that never changes.
}
```

Next, remove the [ObservedObject](observedobject.md) property wrapper from the `book` variable in the `BookView`. This property wrapper isn’t needed when adopting [Observation](../observation.md). That’s because SwiftUI automatically tracks any observable properties that a view’s [body](view/body-8kl5o.md) reads directly. For example, SwiftUI updates `BookView` when `book.title` changes.

```swift
// BEFORE
struct BookView: View {
    @ObservedObject var book: Book
    @State private var isEditorPresented = false
    
    var body: some View {
        HStack {
            Text(book.title)
            Spacer()
            Button("Edit") {
                isEditorPresented = true
            }
        }
        .sheet(isPresented: $isEditorPresented) {
            BookEditView(book: book)
        }
    }
}
```

```swift
// AFTER
struct BookView: View {
    var book: Book
    @State private var isEditorPresented = false
    
    var body: some View {
        HStack {
            Text(book.title)
            Spacer()
            Button("Edit") {
                isEditorPresented = true
            }
        }
        .sheet(isPresented: $isEditorPresented) {
            BookEditView(book: book)
        }
    }
}
```

However, if a view needs a binding to an observable type, replace [ObservedObject](observedobject.md) with the [Bindable](bindable.md) property wrapper. This property wrapper provides binding support to an observable type so that views that expect a binding can change an observable property. For instance, in the following code [TextField](textfield.md) receives a binding to `book.title`:

```swift
// BEFORE
struct BookEditView: View {
    @ObservedObject var book: Book
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        VStack() {
            TextField("Title", text: $book.title)
                .textFieldStyle(.roundedBorder)
                .onSubmit {
                    dismiss()
                }
                
            Button("Close") {
                dismiss()
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}
```

```swift
// AFTER
struct BookEditView: View {
    @Bindable var book: Book
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        VStack() {
            TextField("Title", text: $book.title)
                .textFieldStyle(.roundedBorder)
                .onSubmit {
                    dismiss()
                }
                
            Button("Close") {
                dismiss()
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}
```

## See Also

### Creating model data

- [Managing model data in your app](managing-model-data-in-your-app.md) — Create connections between your app’s data model and views.
- [Observable()](<../observation/observable().md>) — Defines and implements conformance of the Observable protocol.
- [Monitoring data changes in your app](monitoring-model-data-changes-in-your-app.md) — Show changes to data in your app’s user interface by using observable objects.
- [StateObject](stateobject.md) — A property wrapper type that instantiates an observable object.
- [ObservedObject](observedobject.md) — A property wrapper type that subscribes to an observable object and invalidates a view whenever the observable object changes.
- [ObservableObject](../combine/observableobject.md) — A type of object with a publisher that emits before the object has changed.

## Download

- [ObservationSample.zip](https://docs-assets.developer.apple.com/published/b78f7ecb6749/ObservationSample.zip)
