---
title: shared
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/shared
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/shared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/shared.json'
content_hash: 'sha256:80ad01b235f42aba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# shared

<sub>Type Property</sub>

The singleton app instance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class var shared: UIApplication { get }
```

## Return Value

The app instance is created in the [UIApplicationMain](<../uiapplicationmain(________)-1yub7.md>) function.

## Discussion

The [UIApplicationMain](<../uiapplicationmain(________)-1yub7.md>) function creates the shared app instance at launch time.
