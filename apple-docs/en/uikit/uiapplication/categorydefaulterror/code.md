---
title: UIApplication.CategoryDefaultError.Code
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/categorydefaulterror/code
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/categorydefaulterror/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/categorydefaulterror/code.json'
content_hash: 'sha256:3193b2e31296e018'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [CategoryDefaultError](../categorydefaulterror.md)

# UIApplication.CategoryDefaultError.Code

<sub>Enumeration</sub>

An enumeration of reasons an error happens when the system discovers whether your app is the default in a category.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Error codes

- [UIApplicationCategoryDefaultErrorRateLimited](code/ratelimited.md) — The system didn’t determine if your app is the default in a category because the app made the request too many times.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Getting information about the error

- [retryAvailableDateErrorKey](retryavailabledateerrorkey.md) — A dictionary key, with a value that’s a date when a result is next available.
- [statusLastProvidedDateErrorKey](statuslastprovideddateerrorkey.md) — A dictionary key, with a value that’s the date your app last received a successful result.
