---
title: 'register(_:forSoundIdentifier:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocussystem/register(_:forsoundidentifier:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocussystem/register(_:forsoundidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussystem/register%28_%3Aforsoundidentifier%3A%29.json'
content_hash: 'sha256:b3a5ae1aea7b8d04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusSystem](../uifocussystem.md)

# register(_:forSoundIdentifier:)

<sub>Type Method</sub>

Registers the specified sound file with the focus engine.

<sub>tvOS</sub>

```swift
class func register(_ soundFileURL: URL, forSoundIdentifier identifier: UIFocusSoundIdentifier)
```

## Parameters

- `soundFileURL` — A URL specifying the location of a sound file. The sound file must be local to the current device and must not point to a resource on a remote server. Sound files must be less than 30 seconds in length and must be in a format recognized by the system.

- `identifier` — The identifier for the sound. You use this value later to tell the focus engine which sounds you want to play. Do not specify one of the UIKit sound identifiers (such as [UIFocusSoundIdentifierDefault](../uifocussoundidentifier/default.md)); doing so will cause an immediate assertion failure and crash your app.

## Discussion

Use this method to register custom sounds that you want played in response to focus changes. Register sound files early in your app’s life cycle so that the focus system has time to process those files and make them ready for playback. You must register sound files before attempting to play them.

To play your custom sounds, override the [- soundIdentifierForFocusUpdateInContext:](<../uifocusenvironment/soundidentifierforfocusupdate(in_).md>) method in the focus-related objects of your interface and return the associated identifier. You can play the standard UIKit sounds or play your custom sounds when the object gains or loses focus.
