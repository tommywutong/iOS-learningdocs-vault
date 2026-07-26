---
title: UISearchTextFieldDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfielddelegate
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfielddelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfielddelegate.json'
content_hash: 'sha256:5cdfddb31ecc73ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISearchTextFieldDelegate

<sub>Protocol</sub>

The interface for the delegate of a search field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UISearchTextFieldDelegate : UITextFieldDelegate
```

## Overview

A search field asks its delegate for an [NSItemProvider](../foundation/nsitemprovider.md) when the user starts to copy or move a token. To support these interactions, set the search field’s [delegate](uitextfield/delegate.md) to an instance of [UISearchTextFieldDelegate](uisearchtextfielddelegate.md) that implements [- searchTextField:itemProviderForCopyingToken:](<uisearchtextfielddelegate/searchtextfield(__itemproviderforcopying_).md>) and set the search field’s [allowsCopyingTokens](uisearchtextfield/allowscopyingtokens.md) property to [true](../swift/true.md).

The search field’s [pasteDelegate](uitextpasteconfigurationsupporting/pastedelegate.md) handles pasting and dropping tokens as well as text.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [UITextFieldDelegate](uitextfielddelegate.md)

## Topics

### Providing information to copy and drag

- [- searchTextField:itemProviderForCopyingToken:](<uisearchtextfielddelegate/searchtextfield(__itemproviderforcopying_).md>) — Asks the delegate for an object that can provide a token when the copied token is pasted.

### Responding to search suggestion selections

- [- searchTextField:didSelectSuggestion:](<uisearchtextfielddelegate/searchtextfield(__didselect_).md>) — Tells the delegate when a person selects a search suggestion in the search text field.

## See Also

### Search field

- [UISearchTextField](uisearchtextfield.md) — A view for displaying and editing text and search tokens.
- [UISearchToken](uisearchtoken.md) — Search criteria in a search text field, represented by text and an optional icon.
