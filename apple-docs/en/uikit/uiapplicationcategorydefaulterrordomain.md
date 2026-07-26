---
title: UIApplicationCategoryDefaultErrorDomain
framework: UIKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationcategorydefaulterrordomain
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationcategorydefaulterrordomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationcategorydefaulterrordomain.json'
content_hash: 'sha256:0196f2d0885fb2d2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIApplicationCategoryDefaultErrorDomain

<sub>Global Variable</sub>

A string that identifies errors the system encounters when it determines if your app is the default in a category.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
extern NSErrorDomain const UIApplicationCategoryDefaultErrorDomain;
```

## See Also

### Discovering if your app is the default app in a category

- [defaultStatusForCategory:error:](uiapplication/defaultstatusforcategory_error_.md) — Reports whether this app is the person’s default app in the given category.
- [UIApplicationCategoryDefaultStatus](uiapplicationcategorydefaultstatus.md) — The default status of an application for some category.
- [Category](uiapplication/category.md) — Constants that describe the types of apps in the system.
- [UIApplicationCategoryDefaultRetryAvailabilityDateErrorKey](uiapplicationcategorydefaultretryavailabilitydateerrorkey.md) — A dictionary key, with a value that’s a date when a result is next available.
- [UIApplicationCategoryDefaultStatusLastProvidedDateErrorKey](uiapplicationcategorydefaultstatuslastprovideddateerrorkey.md) — A dictionary key, with a value that’s the date your app last received a successful result.
