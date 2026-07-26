---
title: 'searchTextField(_:itemProviderForCopying:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchtextfielddelegate/searchtextfield(_:itemproviderforcopying:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfielddelegate/searchtextfield(_:itemproviderforcopying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfielddelegate/searchtextfield%28_%3Aitemproviderforcopying%3A%29.json'
content_hash: 'sha256:5429347b2ac078fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextFieldDelegate](../uisearchtextfielddelegate.md)

# searchTextField(_:itemProviderForCopying:)

<sub>Instance Method</sub>

Asks the delegate for an object that can provide a token when the copied token is pasted.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func searchTextField(_ searchTextField: UISearchTextField, itemProviderForCopying token: UISearchToken) -> NSItemProvider
```

## Parameters

- `searchTextField` — The search field that contains the token the user is copying or dragging.

- `token` — The token the user is copying or dragging.

## Return Value

An item provider that provides a token if the user pastes or drops the token.

## Discussion

To support drag and drop and the Cut and Copy commands, your delegate must implement this method and return an [NSItemProvider](../../foundation/nsitemprovider.md) for the requested token. Your delegate can provide a plain text representation for pasting in other contexts, but should register a custom type identifier so it can recognize and reconstruct the token when pasted into the same field.

The system only calls this delegate method if either [allowsCopyingTokens](../uisearchtextfield/allowscopyingtokens.md) or [allowsDeletingTokens](../uisearchtextfield/allowsdeletingtokens.md) is [true](../../swift/true.md).
