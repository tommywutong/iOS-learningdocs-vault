---
title: bundle()
framework: Foundation
symbol_kind: macro
role: symbol
role_heading: Macro
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/bundle()
source_url: 'https://developer.apple.com/documentation/foundation/bundle()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle%28%29.json'
content_hash: 'sha256:d2bb15c552156083'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# bundle()

<sub>Macro</sub>

Expands to a bundle instance that’s most likely to contain resources for the calling code.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@freestanding(expression) macro bundle() -> Bundle
```

## Overview

Use the `#bundle` macro when you want to load resources like localized strings, images, or other items in a bundle regardless of whether your code executes in an app, a framework, or a Swift package. When invoked from an app, app extension, framework, or similar context, the expanded macro instantiates the bundle associated with that target. For code in a Swift package target, the macro provides the resource bundle associated with that target.

For example, the following code sets the localized text of a UIKit `UILabel` by explicitly loading the bundle associated with one of the app’s view controllers:

```swift
label.text = String(localized:"Game Over.",
                    bundle: Bundle(for: MyViewController.self),
                    comment: "Text for game over banner.")
```

You can simplify the `bundle:` parameter by invoking the `#bundle` macro instead, like this:

```swift
label.text = String(localized:"Game Over.",
                    bundle: #bundle,
                    comment: "Text for game over banner.")
```

The `#bundle` macro back-deploys to earlier versions of the OS, as indicated by the macro’s availability.

## See Also

### Bundle Resources

- [Bundle](bundle.md) — A representation of the code and resources stored in a bundle directory on disk.
