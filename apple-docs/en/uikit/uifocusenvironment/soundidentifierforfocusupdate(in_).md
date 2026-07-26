---
title: 'soundIdentifierForFocusUpdate(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uifocusenvironment/soundidentifierforfocusupdate(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uifocusenvironment/soundidentifierforfocusupdate(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocusenvironment/soundidentifierforfocusupdate%28in%3A%29.json'
content_hash: 'sha256:6f7b20588f130336'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIFocusEnvironment](../uifocusenvironment.md)

# soundIdentifierForFocusUpdate(in:)

<sub>Instance Method</sub>

Asks the delegate for the identifier of the sound to play when the object gains focus.

<sub>tvOS</sub>

```swift
optional func soundIdentifierForFocusUpdate(in context: UIFocusUpdateContext) -> UIFocusSoundIdentifier?
```

## Parameters

- `context` — The context object associated with the update.

## Return Value

The identifier of the sound to be played. Return `nil` if you want to let the parent focus environment determine which sound to play.

## Discussion

Use this method to return a custom sound when the focus environment object gains focus. Return [UIFocusSoundIdentifierDefault](../uifocussoundidentifier/default.md) to play the default system sound, or return [UIFocusSoundIdentifierNone](../uifocussoundidentifier/none.md) to avoid playing a sound altogether. If you previously registered custom sounds using the [+ registerURL:forSoundIdentifier:](<../uifocussystem/register(__forsoundidentifier_).md>) method of [UIFocusSystem](../uifocussystem.md), you may also return an identifier for a sound that you registered.

If you do not implement this method, the system assumes a `nil` return value. If no ancestor environment defines a custom sound, the system plays the [UIFocusSoundIdentifierDefault](../uifocussoundidentifier/default.md) sound.

> [!important] Important
> You must register custom sounds before returning the associated identifiers from this method. Returning an identifier that is unknown to UIKit will result in an assertion failure and an immediate crash.

## See Also

### Getting the sound to play during updates

- [Using custom sounds for focus movement](../using-custom-sounds-for-focus-movement.md) — Customize the sounds users hear when focus moves.
- [UIFocusSoundIdentifier](../uifocussoundidentifier.md) — An identifier for a focus-related sound.
