---
title: Deprecated symbols
framework: SwiftUI
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/navigationlink-deprecated
source_url: 'https://developer.apple.com/documentation/swiftui/navigationlink-deprecated'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/navigationlink-deprecated.json'
content_hash: 'sha256:6fd0a51d6861dc51'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md) · [Navigation](navigation.md) · [NavigationLink](navigationlink.md)

# Deprecated symbols

<sub>API Collection</sub>

Review deprecated navigation link initializers.

## Overview

For information about updating your use of navigation symbols, see [Migrating to new navigation types](migrating-to-new-navigation-types.md).

## Topics

### Creating links with content builders

- [init(_:isActive:destination:)](<navigationlink/init(__isactive_destination_).md>) — Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key. _(deprecated)_
- [init(isActive:destination:label:)](<navigationlink/init(isactive_destination_label_).md>) — Creates a navigation link that presents the destination view when active. _(deprecated)_
- [init(_:tag:selection:destination:)](<navigationlink/init(__tag_selection_destination_).md>) — Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string. _(deprecated)_
- [init(tag:selection:destination:label:)](<navigationlink/init(tag_selection_destination_label_).md>) — Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value. _(deprecated)_

### Creating links for WatchKit

- [init(destinationName:isActive:label:)](<navigationlink/init(destinationname_isactive_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard when active. _(deprecated)_
- [init(destinationName:tag:selection:label:)](<navigationlink/init(destinationname_tag_selection_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard when a bound selection variable matches a value you provide. _(deprecated)_
- [init(destinationName:label:)](<navigationlink/init(destinationname_label_).md>) — Creates a navigation link that presents a view from a WatchKit storyboard. _(deprecated)_

### Creating links with view arguments

- [init(_:destination:isActive:)](<navigationlink/init(__destination_isactive_).md>) — Creates a navigation link that presents a destination view when active, with a text label that the link generates from a localized string key. _(deprecated)_
- [init(destination:isActive:label:)](<navigationlink/init(destination_isactive_label_).md>) — Creates a navigation link that presents the destination view when active. _(deprecated)_
- [init(_:destination:tag:selection:)](<navigationlink/init(__destination_tag_selection_).md>) — Creates a navigation link that presents a destination view when a bound selection variable matches a value you provide, using a text label that the link generates from a title string. _(deprecated)_
- [init(destination:tag:selection:label:)](<navigationlink/init(destination_tag_selection_label_).md>) — Creates a navigation link that presents the destination view when a bound selection variable equals a given tag value. _(deprecated)_
