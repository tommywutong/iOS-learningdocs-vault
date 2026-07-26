---
title: UIDataSourceModelAssociation
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidatasourcemodelassociation
source_url: 'https://developer.apple.com/documentation/uikit/uidatasourcemodelassociation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidatasourcemodelassociation.json'
content_hash: 'sha256:9308e7c17676aa09'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIDataSourceModelAssociation

<sub>Protocol</sub>

A set of methods that defines an interface for providing persistent references to data objects in your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIDataSourceModelAssociation
```

## Overview

Your data source objects can adopt this protocol to assist a corresponding table or collection view during the state restoration process. Those classes use the methods of this protocol to ensure that the same data objects (and not just the same row indexes) are scrolled into view and selected.

Before you can implement this protocol, your app must be able to identify data objects consistently between app launches. This requires being able to take some identifying marker of the object and convert that marker into a string that can then be saved with the rest of the app state. For example, a Core Data app could convert a managed object’s ID into a URI that it could then convert into a string.

Currently, only the [UITableView](uitableview.md) and [UICollectionView](uicollectionview.md) classes support this protocol. You’d implement this protocol in any objects you use as the data source for those classes. If you don’t adopt the protocol in your data source, the views don’t attempt to restore the selected and visible rows.

## Topics

### Locating the data

- [- modelIdentifierForElementAtIndexPath:inView:](<uidatasourcemodelassociation/modelidentifierforelement(at_in_).md>) — Returns the string that uniquely identifies the data at the specified location in the view.
- [- indexPathForElementWithModelIdentifier:inView:](<uidatasourcemodelassociation/indexpathforelement(withmodelidentifier_in_).md>) — Returns the current index of the data object with the specified identifier.
