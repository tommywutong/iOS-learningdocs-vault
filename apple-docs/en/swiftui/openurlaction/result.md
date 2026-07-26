---
title: OpenURLAction.Result
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/openurlaction/result
source_url: 'https://developer.apple.com/documentation/swiftui/openurlaction/result'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/openurlaction/result.json'
content_hash: 'sha256:07d8a3ab6d55e100'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [OpenURLAction](../openurlaction.md)

# OpenURLAction.Result

<sub>Structure</sub>

The result of a custom open URL action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Result
```

## Overview

If you declare a custom [OpenURLAction](../openurlaction.md) in the [Environment](../environment.md), return one of the result values from its handler.

- Use [handled](result/handled.md) to indicate that the handler opened the URL.
- Use [discarded](result/discarded.md) to indicate that the handler discarded the URL.
- Use [systemAction](result/systemaction.md) without an argument to ask SwiftUI to open the URL with the system handler.
- Use [systemAction(_:)](<result/systemaction(__).md>) with a URL argument to ask SwiftUI to open the specified URL with the system handler.

You can use the last option to transform URLs, while still relying on the system to open the URL. For example, you could append a path component to every URL:

```swift
.environment(\.openURL, OpenURLAction { url in
    .systemAction(url.appendingPathComponent("edit"))
})
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting the results

- [discarded](result/discarded.md) — The handler discarded the URL.
- [handled](result/handled.md) — The handler opened the URL.
- [systemAction](result/systemaction.md) — The handler asks the system to open the original URL.
- [systemAction(_:)](<result/systemaction(__).md>) — The handler asks the system to open the modified URL.

### Type Methods

- [systemAction(_:prefersInApp:)](<result/systemaction(__prefersinapp_).md>)

## See Also

### Creating the action

- [init(handler:)](<init(handler_).md>) — Creates an action that opens a URL.
