---
title: 'isDefault(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/isdefault(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/isdefault(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/isdefault%28_%3A%29.json'
content_hash: 'sha256:f32dd73ada009be3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# isDefault(_:)

<sub>Instance Method</sub>

Reports whether this app is the person’s default app in the given category.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
nonisolated func isDefault(_ category: UIApplication.Category) throws -> Bool
```

## Parameters

- `category` — The type of app for which you test whether your app is the default.

## Return Value

If the system determines the status of the app, this method returns `true` if the app is the default app in the category, and `false` otherwise. If the system doesn’t determine the status, or the app exceeds the threshold rate for calling this method, it throws an error.

## Discussion

To reduce the likelihood that users face continuous requests to set a browser as their default, this API only tells the browser app if it’s the default up to four times in a year. If you call the method too frequently, it throws an error with the domain [UIApplicationCategoryDefaultErrorDomain](../uiapplicationcategorydefaulterrordomain.md) and the code [rateLimited](categorydefaulterror/ratelimited.md). The error’s user information dictionary contains these keys:

- **[statusLastProvidedDateErrorKey](categorydefaulterror/statuslastprovideddateerrorkey.md)** — The date at which the app most recently received a `true` or `false` response from this method.
- **[retryAvailableDateErrorKey](categorydefaulterror/retryavailabledateerrorkey.md)** — The date at which the app can next request an updated response.

## See Also

### Discovering if your app is the default app in a category

- [Category](category.md) — Constants that describe the types of apps in the system.
- [CategoryDefaultError](categorydefaulterror.md) — Errors that can happen when the system checks if your app is the default app in a category.
