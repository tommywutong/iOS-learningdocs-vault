---
title: LocalAuthenticationView
framework: LocalAuthentication
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 13.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/localauthentication/localauthenticationview
source_url: 'https://developer.apple.com/documentation/localauthentication/localauthenticationview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/localauthentication/localauthenticationview.json'
content_hash: 'sha256:34d03138a0a979cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Local Authentication](../localauthentication.md)

# LocalAuthenticationView

<sub>Structure</sub>

A SwiftUI view that displays an authentication interface.

<sub>macOS</sub>

```swift
@MainActor @preconcurrency struct LocalAuthenticationView<Label> where Label : View
```

## Overview

Use a [LocalAuthenticationView](localauthenticationview.md) to display a view that prompts users to authenticate with the app. The view visually represents the state of an [LAPolicy](lapolicy.md) evaluation from the [Local Authentication](../localauthentication.md) framework.

The following shows a [LocalAuthenticationView](localauthenticationview.md) in a Mac app with an implicit [LAContext](lacontext.md) instance:

```swift
var body: some View {
    LocalAuthenticationView(
        "Continue with Touch ID",
        reason: Text("Access sandcastle competition designs")
    ) { result in
        switch result {
        case .success:
            print("Authorized")
        case .failure(let error):
            print("Authorization failed: \(error)")
        }
    }
    .controlSize(.large)
}
```

If your app’s authorization flow reuses an existing [LAContext](lacontext.md), pass it as part of initializing a [LocalAuthenticationView](localauthenticationview.md) and call its [- evaluatePolicy:localizedReason:reply:](<lacontext/evaluatepolicy(__localizedreason_reply_).md>) method after the view appears.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [View](../swiftui/view.md)

## Topics

### Authenticating with an implicit context

- [init(reason:context:result:label:)](<localauthenticationview/init(reason_context_result_label_).md>) — Creates a local authentication view.
- [init(_:reason:context:result:)](<localauthenticationview/init(__reason_context_result_)-8ubaq.md>) — Creates a local authentication view with a title.
- [init(_:reason:context:result:)](<localauthenticationview/init(__reason_context_result_)-917ds.md>) — Creates a local authentication view with a localizable title.
- [init(_:reason:context:result:)](<localauthenticationview/init(__reason_context_result_)-4pkpi.md>) — Creates a local authentication view with a title text view.

### Authenticating with a context you supply

- [init(_:context:)](<localauthenticationview/init(__context_)-9xeoo.md>) — Creates a local authentication view with a required context.
- [init(context:label:)](<localauthenticationview/init(context_label_).md>) — Creates a local authentication view with a label and required context.
- [init(_:context:)](<localauthenticationview/init(__context_)-676qx.md>) — Creates a local authentication view with a localizable title and required context.

### Initializers

- [init(_:context:)](<localauthenticationview/init(__context_)-7ejbu.md>) — Creates a new view and pairs it with the specified authentication context.
- [init(_:reason:context:result:)](<localauthenticationview/init(__reason_context_result_)-88u6u.md>) — Creates a new `LocalAuthenticationView`.
