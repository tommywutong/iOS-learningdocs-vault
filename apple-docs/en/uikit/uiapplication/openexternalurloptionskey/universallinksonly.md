---
title: universalLinksOnly
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/openexternalurloptionskey/universallinksonly
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/openexternalurloptionskey/universallinksonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/openexternalurloptionskey/universallinksonly.json'
content_hash: 'sha256:35c8e037e5c054b8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIApplication](../../uiapplication.md) · [OpenExternalURLOptionsKey](../openexternalurloptionskey.md)

# universalLinksOnly

<sub>Type Property</sub>

URLs must be universal links and have an app configured to open them.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let universalLinksOnly: UIApplication.OpenExternalURLOptionsKey
```

## Discussion

When you include this key in the options dictionary of the [- openURL:options:completionHandler:](<../open(__options_completionhandler_).md>) method, the method opens the URL only if the URL is a valid universal link and there is an installed app capable of opening that URL. The value of this key is an [NSNumber](../../../foundation/nsnumber.md) object containing a Boolean value.
