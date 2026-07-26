---
title: UIFocusSoundIdentifier
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocussoundidentifier
source_url: 'https://developer.apple.com/documentation/uikit/uifocussoundidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussoundidentifier.json'
content_hash: 'sha256:e32b118d546e6efb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusSoundIdentifier

<sub>Structure</sub>

An identifier for a focus-related sound.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIFocusSoundIdentifier
```

## Overview

To assign an identifier to a custom sound file, call the [+ registerURL:forSoundIdentifier:](<uifocussystem/register(__forsoundidentifier_).md>) method of [UIFocusSystem](uifocussystem.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIFocusSoundIdentifierDefault](uifocussoundidentifier/default.md) — The identifier for the default system sound to play during focus updates.
- [UIFocusSoundIdentifierNone](uifocussoundidentifier/none.md) — The identifier for disabling sound during a focus update.

### Initializers

- [init(_:)](<uifocussoundidentifier/init(__).md>) — Creates an identifier for a focus sound.
- [init(rawValue:)](<uifocussoundidentifier/init(rawvalue_).md>) — Creates an identifier for a focus sound with the specified raw value.

## See Also

### Getting the sound to play during updates

- [Using custom sounds for focus movement](using-custom-sounds-for-focus-movement.md) — Customize the sounds users hear when focus moves.
- [- soundIdentifierForFocusUpdateInContext:](<uifocusenvironment/soundidentifierforfocusupdate(in_).md>) — Asks the delegate for the identifier of the sound to play when the object gains focus.
