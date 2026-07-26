---
title: UIApplicationCategoryDefaultStatus
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.2+, iPadOS 18.2+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplicationcategorydefaultstatus
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationcategorydefaultstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationcategorydefaultstatus.json'
content_hash: 'sha256:b40a82f5ea98acc9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIApplicationCategoryDefaultStatus

<sub>Enumeration</sub>

The default status of an application for some category.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
enum UIApplicationCategoryDefaultStatus : NSInteger;
```

## Topics

### Enumeration Cases

- [UIApplicationCategoryDefaultStatusIsDefault](uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusisdefault.md) — The application is the default for the category.
- [UIApplicationCategoryDefaultStatusNotDefault](uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusnotdefault.md) — The application is not the default for the category.
- [UIApplicationCategoryDefaultStatusUnavailable](uiapplicationcategorydefaultstatus/uiapplicationcategorydefaultstatusunavailable.md) — The status was not available. This is an error condition and the returned error object has more information.

## See Also

### Discovering if your app is the default app in a category

- [defaultStatusForCategory:error:](uiapplication/defaultstatusforcategory_error_.md) — Reports whether this app is the person’s default app in the given category.
- [Category](uiapplication/category.md) — Constants that describe the types of apps in the system.
- [UIApplicationCategoryDefaultErrorDomain](uiapplicationcategorydefaulterrordomain.md) — A string that identifies errors the system encounters when it determines if your app is the default in a category.
- [UIApplicationCategoryDefaultRetryAvailabilityDateErrorKey](uiapplicationcategorydefaultretryavailabilitydateerrorkey.md) — A dictionary key, with a value that’s a date when a result is next available.
- [UIApplicationCategoryDefaultStatusLastProvidedDateErrorKey](uiapplicationcategorydefaultstatuslastprovideddateerrorkey.md) — A dictionary key, with a value that’s the date your app last received a successful result.
