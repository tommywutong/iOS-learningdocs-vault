---
title: NSExtensionItemsAndErrorsKey
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsextensionitemsanderrorskey
source_url: 'https://developer.apple.com/documentation/foundation/nsextensionitemsanderrorskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsextensionitemsanderrorskey.json'
content_hash: 'sha256:f44dd0e4042e083d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSExtensionItemsAndErrorsKey

<sub>Global Variable</sub>

The extension items and errors key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSExtensionItemsAndErrorsKey: String
```

## Discussion

This key appears in the [userInfo](nserror/userinfo.md) dictionary of the [NSError](nserror.md) object that [- cancelRequestWithError:](<nsextensioncontext/cancelrequest(witherror_).md>) returns.

This key’s value is a dictionary of [NSExtensionItem](nsextensionitem.md) objects and associated [NSError](nserror.md) instances.

## See Also

### Handling requests

- [- completeRequestReturningItems:completionHandler:](<nsextensioncontext/completerequest(returningitems_completionhandler_).md>) — Tells the host app to complete the app extension request with an array of result items.
- [- cancelRequestWithError:](<nsextensioncontext/cancelrequest(witherror_).md>) — Tells the host app to cancel the app extension request, with a supplied error.
