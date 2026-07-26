---
title: UIApplication.Category
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/category
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/category'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/category.json'
content_hash: 'sha256:ce5bdcf324556914'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# UIApplication.Category

<sub>Enumeration</sub>

Constants that describe the types of apps in the system.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum Category
```

## Overview

Use the values in this enumeration with [isDefault(_:)](<isdefault(__).md>) (or, in Objective-C, [defaultStatusForCategory:error:](defaultstatusforcategory_error_.md)) to find if your app is the person’s default for a category.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Application categories

- [UIApplicationCategoryWebBrowser](category/webbrowser.md) — The app is a web browser.

### Initializers

- [init(rawValue:)](<category/init(rawvalue_).md>)

## See Also

### Discovering if your app is the default app in a category

- [isDefault(_:)](<isdefault(__).md>) — Reports whether this app is the person’s default app in the given category.
- [CategoryDefaultError](categorydefaulterror.md) — Errors that can happen when the system checks if your app is the default app in a category.
