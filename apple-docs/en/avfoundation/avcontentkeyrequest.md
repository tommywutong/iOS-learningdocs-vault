---
title: AVContentKeyRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontentkeyrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontentkeyrequest.json'
content_hash: 'sha256:3cfab69b5f0d25de'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVContentKeyRequest

<sub>Class</sub>

An object that encapsulates information about a content decryption key request issued from a content key session object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVContentKeyRequest
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting content key request data

- [- makeStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:](<avcontentkeyrequest/makestreamingcontentkeyrequestdata(forapp_contentidentifier_options_completionhandler_).md>) — Obtains encrypted key request data for a specific combination of app and content.
- [AVContentKeyRequestProtocolVersionsKey](avcontentkeyrequestprotocolversionskey.md) — A key that specifies the versions of the content protection protocol supported by the application.
- [AVContentKeyRequestRequiresValidationDataInSecureTokenKey](avcontentkeyrequestrequiresvalidationdatainsecuretokenkey.md) — A key that requires the secure token to have extended validation data.
- [AVContentKeyRequestRandomDeviceIdentifierSeedKey](avcontentkeyrequestrandomdeviceidentifierseedkey.md) — Value is an NSData containing a 16-byte seed to randomize the user’s deviceID contained in the SPC blob during FairPlay key exchange
- [AVContentKeyRequestShouldRandomizeDeviceIdentifierKey](avcontentkeyrequestshouldrandomizedeviceidentifierkey.md) — Value is an Boolean indicating whether the user’s deviceID contained in the SPC blob during FairPlay key exchange should be randomized using a system generated seed

### Responding to the content key request

- [- processContentKeyResponse:](<avcontentkeyrequest/processcontentkeyresponse(__).md>) — Sends the specified content key response to the receiver for processing.
- [- processContentKeyResponseError:](<avcontentkeyrequest/processcontentkeyresponseerror(__).md>) — Tells the receiver that the app was unable to obtain a content key response.
- [- respondByRequestingPersistableContentKeyRequest](<avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest().md>) — Tells the receiver that the app requires a persistable content key request object for processing. _(deprecated)_

### Getting content key request properties

- [identifier](avcontentkeyrequest/identifier.md) — The identifier for the content key.
- [originatingRecipient](avcontentkeyrequest/originatingrecipient.md) — The AVContentKeyRecipient which initiated this request, if any.
- [canProvidePersistableContentKey](avcontentkeyrequest/canprovidepersistablecontentkey.md) — The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [error](avcontentkeyrequest/error.md) — The error description for a failed key request.
- [initializationData](avcontentkeyrequest/initializationdata.md) — The data used to obtain a key response.
- [renewsExpiringResponseData](avcontentkeyrequest/renewsexpiringresponsedata.md) — A Boolean value that indicates whether the content key request renews previously provided response data.
- [status](avcontentkeyrequest/status-swift.property.md) — The current state of the content key request.
- [Status](avcontentkeyrequest/status-swift.enum.md) — The status for a content key request.

### Inspecting a request

- [contentKey](avcontentkeyrequest/contentkey.md) — The generated content key.
- [contentKeySpecifier](avcontentkeyrequest/contentkeyspecifier.md) — The requested content key specifier.
- [options](avcontentkeyrequest/options.md) — A dictionary of options used to initialize key loading.
- [RetryReason](avcontentkeyrequest/retryreason.md) — The reason for asking the client to retry a content key request.

### Instance Properties

- [canBeFulfilledWithAdvisoryKey](avcontentkeyrequest/canbefulfilledwithadvisorykey.md) — Indicates whether this key request was initiated for an advisory key. _(beta)_

### Instance Methods

- [- makeOptionalStreamingContentKeyRequestDataForApp:contentIdentifier:options:completionHandler:](<avcontentkeyrequest/makeoptionalstreamingcontentkeyrequestdata(forapp_contentidentifier_options_completionhandler_).md>) — Obtains an optional content key request data for a specific combination of application and content. _(beta)_
- [- respondByRequestingPersistableContentKeyRequestAndReturnError:](<avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequestandreturnerror().md>) — Tells the receiver that the app requires a persistable content key request object for processing.

## See Also

### FairPlay streaming

- [AVContentKeySession](avcontentkeysession.md) — An object that creates and tracks decryption keys for media data.
- [AVContentKeySessionDelegate](avcontentkeysessiondelegate.md) — A protocol that handles content key requests.
- [AVContentKey](avcontentkey.md) — An object that represents the content key decryptor.
- [AVContentKeySpecifier](avcontentkeyspecifier.md) — An object that uniquely identifies a content key.
- [AVPersistableContentKeyRequest](avpersistablecontentkeyrequest.md) — An object that encapsulates information about a persistable content decryption key request issued from a content key session.
- [AVContentKeyResponse](avcontentkeyresponse.md) — An object that encapsulates information about a response to a content decryption key request.
- [AVExternalContentProtectionStatus](avexternalcontentprotectionstatus.md) — Constants that specify whether sufficient protection exists to display the content.
- [AVSampleBufferAttachContentKey](<avsamplebufferattachcontentkey(______).md>) — Attaches a content key to a sample buffer for the purpose of content decryption. _(deprecated)_
