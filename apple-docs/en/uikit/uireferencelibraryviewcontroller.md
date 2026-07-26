---
title: UIReferenceLibraryViewController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uireferencelibraryviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uireferencelibraryviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uireferencelibraryviewcontroller.json'
content_hash: 'sha256:520f01db2d92d003'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIReferenceLibraryViewController

<sub>Class</sub>

A view controller that displays a standard interface for looking up the definition of a word or term.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIReferenceLibraryViewController
```

## Overview

A [UIReferenceLibraryViewController](uireferencelibraryviewcontroller.md) object should not be used to display wordlists, create a standalone dictionary app, or republish the content in any form.

You create and initialize a reference library view controller using the [- initWithTerm:](<uireferencelibraryviewcontroller/init(term_).md>) method. You pass the term to define as the parameter to this method and the definition is displayed. You can present this view controller modally or as part of another interface. On iPad, you can set the reference library view controller as the content view controller of a [UIPopoverController](uipopovercontroller.md) object. Optionally, use the [+ dictionaryHasDefinitionForTerm:](<uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm_).md>) class method to check if a definition is available for a given term before creating an instance—for example, use this method if you want to change the user interface depending on whether a definition is available.

## Relationships

- **Inherits From**: [UIViewController](uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](uiresponderstandardeditactions.md), [UIStateRestoring](uistaterestoring.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md), [UIUserActivityRestoring](uiuseractivityrestoring.md)

## Topics

### Creating a reference-library view controller

- [+ dictionaryHasDefinitionForTerm:](<uireferencelibraryviewcontroller/dictionaryhasdefinition(forterm_).md>) — Returns whether a definition is available for the given term.
- [- initWithTerm:](<uireferencelibraryviewcontroller/init(term_).md>) — Initializes a newly created reference-library view controller to display the definition of the given term.
- [- initWithCoder:](<uireferencelibraryviewcontroller/init(coder_).md>) — Creates a reference-library view controller from data in an unarchiver.
