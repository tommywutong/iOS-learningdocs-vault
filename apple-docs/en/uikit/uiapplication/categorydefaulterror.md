---
title: UIApplication.CategoryDefaultError
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/categorydefaulterror
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/categorydefaulterror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/categorydefaulterror.json'
content_hash: 'sha256:88af0bf55a17f1ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# UIApplication.CategoryDefaultError

<sub>Structure</sub>

Errors that can happen when the system checks if your app is the default app in a category.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
struct CategoryDefaultError
```

## Relationships

- **Conforms To**: [CustomNSError](../../foundation/customnserror.md), [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Getting information about the error

- [Code](categorydefaulterror/code.md) — An enumeration of reasons an error happens when the system discovers whether your app is the default in a category.
- [retryAvailableDateErrorKey](categorydefaulterror/retryavailabledateerrorkey.md) — A dictionary key, with a value that’s a date when a result is next available.
- [statusLastProvidedDateErrorKey](categorydefaulterror/statuslastprovideddateerrorkey.md) — A dictionary key, with a value that’s the date your app last received a successful result.

### Errors when discovering if an app is the default in a category

- [errorDomain](categorydefaulterror/errordomain.md) — A string that indicates that an error happened when the system attempted to determine if your app is the default in a category.
- [rateLimited](categorydefaulterror/ratelimited.md) — An error code that indicates your app requested its status too frequently.

## See Also

### Discovering if your app is the default app in a category

- [isDefault(_:)](<isdefault(__).md>) — Reports whether this app is the person’s default app in the given category.
- [Category](category.md) — Constants that describe the types of apps in the system.
