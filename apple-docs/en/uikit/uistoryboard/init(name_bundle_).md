---
title: 'init(name:bundle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uistoryboard/init(name:bundle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistoryboard/init(name:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistoryboard/init%28name%3Abundle%3A%29.json'
content_hash: 'sha256:00b17f2fc767e289'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStoryboard](../uistoryboard.md)

# init(name:bundle:)

<sub>Initializer</sub>

Creates and returns a storyboard object for the specified resource file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(name: String, bundle storyboardBundleOrNil: Bundle?)
```

## Parameters

- `name` — The name of the storyboard resource file without the filename extension. This method raises an exception if this parameter is `nil`.

- `storyboardBundleOrNil` — The bundle containing the storyboard file and its related resources. If you specify `nil`, this method looks in the main bundle of the current application.

## Return Value

A storyboard object for the specified file. If no storyboard resource file matching `name` exists, an exception is thrown with description: `Could not find a storyboard named 'XXXXXX' in bundle...`.

## Discussion

Use this method to retrieve the storyboard object containing the view controller graph you want to access. All of the resources associated with the storyboard must be in the bundle indicated by the `storyboardBundleOrNil` parameter.
