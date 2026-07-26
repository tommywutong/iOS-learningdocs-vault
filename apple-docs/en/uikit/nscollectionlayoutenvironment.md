---
title: NSCollectionLayoutEnvironment
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/nscollectionlayoutenvironment
source_url: 'https://developer.apple.com/documentation/uikit/nscollectionlayoutenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nscollectionlayoutenvironment.json'
content_hash: 'sha256:8a0c55c08ba01a86'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# NSCollectionLayoutEnvironment

<sub>Protocol</sub>

A protocol used to provide information about the layout’s container and environment traits, such as size classes and display scale factor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol NSCollectionLayoutEnvironment : NSObjectProtocol
```

## Overview

In a section provider, you use the layout environment to get information about the context that the layout appears in. You can get information about the layout’s container, such as its size and content insets, and the traits of its environment, such as size classes, display scale factor, and user interface idiom. You use this information while rendering the layout’s sections to help you make decisions about how to display the layout.

For example, the following code uses the layout environment’s trait collection to check whether the UI is in Dark Mode while creating the layout’s sections.

**Swift**

```swift
let layout = UICollectionViewCompositionalLayout { (sectionIndex: Int,
    layoutEnvironment: NSCollectionLayoutEnvironment) -> NSCollectionLayoutSection in
        
    if layoutEnvironment.traitCollection.userInterfaceStyle == .dark {
        return sectionForUserInterfaceStyle(.dark)
    } else {
        return sectionForUserInterfaceStyle(.light)
    }
}
```

**Objective-C**

```objc
UICollectionViewCompositionalLayout *layout = [[UICollectionViewCompositionalLayout alloc] initWithSectionProvider:^NSCollectionLayoutSection *(NSInteger section, id<NSCollectionLayoutEnvironment> layoutEnvironment) {
    if (layoutEnvironment.traitCollection.userInterfaceStyle == UIUserInterfaceStyleDark) {
        return [self sectionForUserInterfaceStyle: UIUserInterfaceStyleDark];
    } else {
        return [self sectionForUserInterfaceStyle: UIUserInterfaceStyleLight];
    }
}];
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting the layout’s container

- [container](nscollectionlayoutenvironment/container.md) — Information about the layout’s container, such as its size and content insets.

### Getting the trait collection

- [traitCollection](nscollectionlayoutenvironment/traitcollection.md) — The traits that describe the current environment of the layout, such as the size classes and display scale factor.

## See Also

### Configuration

- [UICollectionViewCompositionalLayoutConfiguration](uicollectionviewcompositionallayoutconfiguration.md) — An object that defines scroll direction, section spacing, and headers or footers for the layout.
- [UICollectionViewCompositionalLayoutSectionProvider](uicollectionviewcompositionallayoutsectionprovider.md) — A closure that creates and returns each of the layout’s sections.
