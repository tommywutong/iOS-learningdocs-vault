---
title: UIApplication.CategoryDefaultError.Code.rateLimited
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/categorydefaulterror/code/ratelimited
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/categorydefaulterror/code/ratelimited'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/categorydefaulterror/code/ratelimited.json'
content_hash: 'sha256:b662be7dc5f2a901'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [UIKit](../../../../uikit.md) · [UIApplication](../../../uiapplication.md) · [CategoryDefaultError](../../categorydefaulterror.md) · [Code](../code.md)

# UIApplication.CategoryDefaultError.Code.rateLimited

<sub>Case</sub>

The system didn’t determine if your app is the default in a category because the app made the request too many times.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
case rateLimited
```

## Discussion

When you receive an error with this code, the error’s user info dictionary contains these keys:

- **[statusLastProvidedDateErrorKey](../statuslastprovideddateerrorkey.md)** — The date at which the app most recently received a result indicating whether it’s the default app in a category.
- **[retryAvailableDateErrorKey](../retryavailabledateerrorkey.md)** — The date at which the app can next request an updated response.
