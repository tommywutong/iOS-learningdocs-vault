---
title: 'CFPreferencesCopyApplicationList(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/corefoundation/cfpreferencescopyapplicationlist(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfpreferencescopyapplicationlist(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfpreferencescopyapplicationlist%28_%3A_%3A%29.json'
content_hash: 'sha256:24fa45aede9988ed'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFPreferencesCopyApplicationList(_:_:)

<sub>Function</sub>

Constructs and returns the list of all applications that have preferences in the scope of the specified user and host.

> [!warning] Deprecated
> Unsupported API

<sub>tvOS, visionOS, watchOS</sub>

```swift
func CFPreferencesCopyApplicationList(_ userName: CFString, _ hostName: CFString) -> CFArray?
```

## Parameters

- `userName` — [kCFPreferencesCurrentUser](kcfpreferencescurrentuser.md) to search the current-user domain, otherwise [kCFPreferencesAnyUser](kcfpreferencesanyuser.md) to search the any-user domain.

- `hostName` — [kCFPreferencesCurrentHost](kcfpreferencescurrenthost.md) to search the current-host domain, otherwise [kCFPreferencesAnyHost](kcfpreferencesanyhost.md) to search the any-host domain.

## Return Value

The list of application IDs. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Miscellaneous Functions

- [CFPreferencesAppValueIsForced](<cfpreferencesappvalueisforced(____).md>) — Determines whether or not a given key has been imposed on the user.
