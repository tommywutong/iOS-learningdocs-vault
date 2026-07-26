---
title: Keychains
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/keychains
source_url: 'https://developer.apple.com/documentation/security/keychains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/keychains.json'
content_hash: 'sha256:eb0a59de49ae8f5e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Keychain services](keychain-services.md)

# Keychains

<sub>API Collection</sub>

Create and manage entire keychains in macOS.

## Overview

In iOS, apps have access to a single keychain (which logically encompasses the iCloud keychain). This keychain is automatically unlocked when the user unlocks the device and then locked when the device is locked. An app can access only its own keychain items, or those shared with a group to which the app belongs. It can’t manage the keychain container itself.

In macOS, however, the system supports an arbitrary number of keychains. You typically rely on the user to manage these with the Keychain Access app and work implicitly with the default keychain, much as you would in iOS. Nevertheless, the keychain services API does provide functions that you can use to manipulate keychains directly. For example, you can create and manage a keychain that is private to your app. On the other hand, robust access control mechanisms typically make this unnecessary for anything other than an app trying to replicate the keychain access utility.

## Topics

### Creation and Deletion

- [SecKeychainCreate](<seckeychaincreate(____________).md>) — Creates an empty keychain. _(deprecated)_
- [SecKeychainDelete](<seckeychaindelete(__).md>) — Deletes one or more keychains from the default keychain search list, and removes the keychain itself if it is a file. _(deprecated)_
- [SecKeychain](seckeychain.md) — An opaque type that represents a keychain.
- [SecKeychainGetTypeID](<seckeychaingettypeid().md>) — Returns the unique identifier of the opaque type to which a keychain object belongs. _(deprecated)_

### Locking and Unlocking

- [SecKeychainLock](<seckeychainlock(__).md>) — Locks a keychain. _(deprecated)_
- [SecKeychainLockAll](<seckeychainlockall().md>) — Locks all keychains belonging to the current user. _(deprecated)_
- [SecKeychainUnlock](<seckeychainunlock(________).md>) — Unlocks a keychain. _(deprecated)_

### Settings

- [SecKeychainSetSettings](<seckeychainsetsettings(____).md>) — Changes the settings of a keychain. _(deprecated)_
- [SecKeychainCopySettings](<seckeychaincopysettings(____).md>) — Obtains a keychain’s settings. _(deprecated)_
- [SecKeychainSettings](seckeychainsettings.md) — A structure that contains information about keychain settings.
- [SEC_KEYCHAIN_SETTINGS_VERS1](sec_keychain_settings_vers1.md) — Defines the keychain settings version.

### Keychain Management

- [SecKeychainGetVersion](<seckeychaingetversion(__).md>) — Determines the version of keychain services installed on the user’s system. _(deprecated)_
- [SecKeychainOpen](<seckeychainopen(____).md>) — Opens a keychain. _(deprecated)_
- [SecKeychainSetDefault](<seckeychainsetdefault(__).md>) — Sets the default keychain. _(deprecated)_
- [SecKeychainCopyDefault](<seckeychaincopydefault(__).md>) — Retrieves a pointer to the default keychain. _(deprecated)_
- [SecKeychainGetPath](<seckeychaingetpath(______).md>) — Determines the path of a keychain. _(deprecated)_
- [SecKeychainGetStatus](<seckeychaingetstatus(____).md>) — Retrieves status information of a keychain. _(deprecated)_
- [SecKeychainStatus](seckeychainstatus.md) — A value that defines the current status of a keychain.
- [SecKeychainStatus Values](seckeychainstatus-values.md) — Valid values for the keychain status type.

### Search

- [SecKeychainSetSearchList](<seckeychainsetsearchlist(__).md>) — Specifies the list of keychains to use in the default keychain search list. _(deprecated)_
- [SecKeychainCopySearchList](<seckeychaincopysearchlist(__).md>) — Retrieves a keychain search list. _(deprecated)_
- [SecKeychainSearch](seckeychainsearch.md) — An opaque type that contains information about a keychain search.

### User Interaction

- [SecKeychainSetUserInteractionAllowed](<seckeychainsetuserinteractionallowed(__).md>) — Enables or disables the user interface for keychain services functions that automatically display a user interface. _(deprecated)_
- [SecKeychainGetUserInteractionAllowed](<seckeychaingetuserinteractionallowed(__).md>) — Indicates whether keychain services functions that normally display a user interaction are allowed to do so. _(deprecated)_

### Callbacks

- [SecKeychainAddCallback](<seckeychainaddcallback(______).md>) — Registers your keychain event callback function. _(deprecated)_
- [SecKeychainRemoveCallback](<seckeychainremovecallback(__).md>) — Unregisters your keychain event callback function. _(deprecated)_
- [SecKeychainCallback](seckeychaincallback.md) — A customized callback function that keychain services call when a keychain event has occurred. _(deprecated)_
- [SecKeychainCallbackInfo](seckeychaincallbackinfo.md) — Information about a keychain event that keychain services deliver to your app via a callback function.
- [SecKeychainEvent](seckeychainevent.md) — The list of keychain events that can trigger a callback.
- [SecKeychainEventMask](seckeychaineventmask.md) — Bit masks corresponding to the events that can trigger a keychain callback.

### Preference Domains

- [SecKeychainGetPreferenceDomain](<seckeychaingetpreferencedomain(__).md>) — Gets the current keychain preference domain. _(deprecated)_
- [SecKeychainSetPreferenceDomain](<seckeychainsetpreferencedomain(__).md>) — Sets the keychain preference domain. _(deprecated)_
- [SecKeychainCopyDomainDefault](<seckeychaincopydomaindefault(____).md>) — Retrieves the default keychain from a specified preference domain. _(deprecated)_
- [SecKeychainSetDomainDefault](<seckeychainsetdomaindefault(____).md>) — Sets the default keychain for a specified preference domain. _(deprecated)_
- [SecKeychainCopyDomainSearchList](<seckeychaincopydomainsearchlist(____).md>) — Retrieves the keychain search list for a specified preference domain. _(deprecated)_
- [SecKeychainSetDomainSearchList](<seckeychainsetdomainsearchlist(____).md>) — Sets the keychain search list for a specified preference domain. _(deprecated)_
- [SecPreferencesDomain](secpreferencesdomain.md) — The keychain preference domains.

### Access

- [SecKeychainSetAccess](<seckeychainsetaccess(____).md>) — Sets the application access for a keychain. _(deprecated)_
- [SecKeychainCopyAccess](<seckeychaincopyaccess(____).md>) — Retrieves the application access of a keychain. _(deprecated)_
