---
title: AVContentKeySession
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeysession
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeysession'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeysession.json'
content_hash: 'sha256:4408ea6b6dedcf4c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeySession

<sub>Class</sub>

An object that creates and tracks decryption keys for media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVContentKeySession
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a session

- [+ contentKeySessionWithKeySystem:](<avcontentkeysession/init(keysystem_).md>) — Creates a content key session to manage a collection of content decryption keys.
- [+ contentKeySessionWithKeySystem:storageDirectoryAtURL:](<avcontentkeysession/init(keysystem_storagedirectoryat_).md>) — Creates a content key session to manage a collection of content decryption keys; points to a directory that stores abnormal session termination reports.

### Inspecting the session

- [keySystem](avcontentkeysession/keysystem.md) — The type of key system used to retrieve keys.
- [AVContentKeySystem](avcontentkeysystem.md) — A key-delivery method for a content key session.
- [storageURL](avcontentkeysession/storageurl.md) — A URL that points to a writable storage directory.

### Managing the delegate object

- [- setDelegate:queue:](<avcontentkeysession/setdelegate(__queue_).md>) — Sets the session’s delegate object and the dispatch queue on which to call the delegate’s methods.
- [delegate](avcontentkeysession/delegate.md) — The content key session’s delegate object.
- [delegateQueue](avcontentkeysession/delegatequeue.md) — The dispatch queue the session uses to invoke delegate callbacks.

### Managing content key recipients

- [contentKeyRecipients](avcontentkeysession/contentkeyrecipients.md) — An array of content key recipients.
- [AVContentKeyRecipient](avcontentkeyrecipient.md) — A protocol for requiring decryption keys for media data.
- [- addContentKeyRecipient:](<avcontentkeysession/addcontentkeyrecipient(__).md>) — Tells the delegate that the specified recipient should have access to the decryption keys loaded with the session.
- [- removeContentKeyRecipient:](<avcontentkeysession/removecontentkeyrecipient(__).md>) — Tells the delegate to remove the specified recipient.

### Processing requests

- [- processContentKeyRequestWithIdentifier:initializationData:options:](<avcontentkeysession/processcontentkeyrequest(withidentifier_initializationdata_options_).md>) — Tells the delegate to start loading the content decryption key with the specified identifier and initialization data.

### Managing expiration

- [- expire](<avcontentkeysession/expire().md>) — Tells the delegate that the session expired as the result of normal, intentional processes.
- [- makeSecureTokenForExpirationDateOfPersistableContentKey:completionHandler:](<avcontentkeysession/makesecuretokenforexpirationdate(ofpersistablecontentkey_completionhandler_).md>) — Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.
- [- renewExpiringResponseDataForContentKeyRequest:](<avcontentkeysession/renewexpiringresponsedata(for_).md>) — Tells the delegate that previously provided response data for a content key request is about to expire.
- [contentProtectionSessionIdentifier](avcontentkeysession/contentprotectionsessionidentifier.md) — The identifier for the current content protection session.

### Invalidating content keys

- [- invalidatePersistableContentKey:options:completionHandler:](<avcontentkeysession/invalidatepersistablecontentkey(__options_completionhandler_).md>) — Invalidates the persistable content key and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [- invalidateAllPersistableContentKeysForApp:options:completionHandler:](<avcontentkeysession/invalidateallpersistablecontentkeys(forapp_options_completionhandler_).md>) — Invalidates all of an app’s persistable content keys and creates a secure server playback context (SPC) to verify the outcome of an invalidation request.
- [AVContentKeySessionServerPlaybackContextOption](avcontentkeysessionserverplaybackcontextoption.md) — Options for specifying additional information for generating server playback context (SPC).

### Handling expired session reports

- [+ pendingExpiredSessionReportsWithAppIdentifier:storageDirectoryAtURL:](<avcontentkeysession/pendingexpiredsessionreports(withappidentifier_storagedirectoryat_).md>) — Returns the expired session reports for content key sessions created with the specified app identifier.
- [+ removePendingExpiredSessionReports:withAppIdentifier:storageDirectoryAtURL:](<avcontentkeysession/removependingexpiredsessionreports(__withappidentifier_storagedirectoryat_).md>) — Removes expired session reports from storage.

### Initializers

- [init(keySystem:storageDirectoryAtURL:)](<avcontentkeysession/init(keysystem_storagedirectoryaturl_).md>)

### Instance Properties

- [supportsAdvisoryKeys](avcontentkeysession/supportsadvisorykeys.md) — Boolean indicating whether advisory keys are enabled on the client. _(beta)_

## See Also

### FairPlay streaming

- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKey](avcontentkey.md) — An object that represents the content key decryptor.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVContentKeyRequest](avcontentkeyrequest.md) — An object that encapsulates information about a content decryption key request issued from a content key session object.
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [AVContentKeyResponse](avcontentkeyresponse.md) — An object that encapsulates information about a response to a content decryption key request.
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — Constants that specify whether sufficient protection exists to display the content.
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — Attaches a content key to a sample buffer for the purpose of content decryption. _(deprecated)_
