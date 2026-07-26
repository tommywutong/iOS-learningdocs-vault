---
title: 'init(contact:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplicationshortcuticon/init(contact:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplicationshortcuticon/init(contact:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplicationshortcuticon/init%28contact%3A%29.json'
content_hash: 'sha256:aca76b44c311e06e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplicationShortcutIcon](../uiapplicationshortcuticon.md)

# init(contact:)

<sub>Initializer</sub>

Creates a Home Screen quick action icon from the picture for a contact or a monogram of the contact name if the picture is unavailable.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
convenience init(contact: CNContact)
```

## Parameters

- `contact` — The [CNContact](../../contacts/cncontact.md) contact object to derive the icon from.

## Return Value

A Home Screen quick action icon initialized with the contact’s picture or monogram.

## Discussion

To use this method, pass in a contact from the user’s contacts database, available through the [CNContactStore](../../contacts/cncontactstore.md) object. If the contact you specify has a picture, the system creates a full-color quick action icon from that picture. If the contact has no picture, the system employs the contact’s initials and displays instead a monogram.

> [!note] Note
> This method employs the [Contacts](../../contacts.md) framework.

You can, alternatively, pass in a [CNContact](../../contacts/cncontact.md) object you create at runtime. Such a contact must have at least a first name or a last name. The quick action icon returned from this method is then a monogram built from the contact’s name. With this approach, it isn’t possible for you to provide an image for the quick action icon.

Finally, you can call this method with an empty contact that you create by using the [CNContact](../../contacts/cncontact.md) class’s inherited [alloc](../../objectivec/nsobject-swift.class/alloc.md) and `init` methods. With this approach, the resulting icon is a monochrome silhouette.

When providing a set of contact quick actions, ensure that every one of them has an icon. This ensures the best appearance for the set of quick actions.

## See Also

### Creating a quick action icon

- [+ iconWithType:](<init(type_).md>) — Creates a Home Screen quick action icon using a system-defined image.
- [+ iconWithTemplateImageName:](<init(templateimagename_).md>) — Creates a Home Screen quick action icon based on an image in your app’s bundle, preferably in an asset catalog.
- [+ iconWithSystemImageName:](<init(systemimagename_).md>) — Creates a Home Screen quick action icon using a system symbol image.
