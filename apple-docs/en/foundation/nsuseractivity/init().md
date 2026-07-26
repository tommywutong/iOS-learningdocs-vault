---
title: init()
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（10.0 起废弃）, iPadOS 8.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.10+（10.12 起废弃）, tvOS 9.0+（10.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（3.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsuseractivity/init()
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/init()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/init%28%29.json'
content_hash: 'sha256:758f5c30196e401e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# init()

<sub>Initializer</sub>

Creates a user activity object using the first activity type declared in the app’s information property list file.

> [!warning] Deprecated
> Use initWithActivityType: with a specific activity type string

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init()
```

## Return Value

An [NSUserActivity](../nsuseractivity.md) object.

## Discussion

This method retrieves the first string of the [NSUserActivityTypes](https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW28) key declared in the app’s `Info.plist` file.
