---
title: searchSuggestions
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchtextfield/searchsuggestions
source_url: 'https://developer.apple.com/documentation/uikit/uisearchtextfield/searchsuggestions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchtextfield/searchsuggestions.json'
content_hash: 'sha256:ecd1af3567357835'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchTextField](../uisearchtextfield.md)

# searchSuggestions

<sub>Instance Property</sub>

A list of suggestions to offer as shortcuts below the search field.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var searchSuggestions: [any UISearchSuggestion]? { get set }
```

## Discussion

Provide search suggestions to help people complete their query quickly. Update the suggestions as a person types by registering for the [UITextFieldTextDidChangeNotification](../uitextfield/textdidchangenotification.md) notification and implementing [- textFieldDidEndEditing:reason:](<../uitextfielddelegate/textfielddidendediting(__reason_).md>).

The suggestions appear in a menu under the search field. When you assign new suggestions to this property, the suggestions onscreen refresh automatically. When a person chooses a suggestion, the system sets this property to `nil` and dismisses the search suggestions menu. Implement [- searchTextField:didSelectSuggestion:](<../uisearchtextfielddelegate/searchtextfield(__didselect_).md>) in your delegate to execute any necessary updates when a person chooses a suggestion.

If the search suggestions menu dismisses for other reasons, such as a person tapping outside the search bar, [searchSuggestions](searchsuggestions.md) doesn’t reset to `nil` immediately. The system sets [searchSuggestions](searchsuggestions.md) to `nil` only when a person interacts with search directly — for example, by typing in the search field, canceling search, or changing the search scope using the search bar’s scope bar. To dismiss the menu manually, set this property to `nil` or `[]`.

> [!important] Important
> UIKit allows setting this property directly on an instance of [UISearchTextField](../uisearchtextfield.md) only when the search field isn’t associated with a [UISearchController](../uisearchcontroller.md). If the search field is associated with a search controller, the system raises an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) to use the [searchSuggestions](../uisearchcontroller/searchsuggestions.md) property on [UISearchController](../uisearchcontroller.md) instead.
