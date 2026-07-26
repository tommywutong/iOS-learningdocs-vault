---
title: AuthenticationServices updates
framework: Updates
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/updates/authenticationservices
source_url: 'https://developer.apple.com/documentation/updates/authenticationservices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/updates/authenticationservices.json'
content_hash: 'sha256:e73d0ff9fc44aaba'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Updates](../updates.md)

# AuthenticationServices updates

<sub>Article</sub>

Learn about important changes to AuthenticationServices.

## Overview

Browse notable changes in [Authentication Services](../authenticationservices.md).

## June 2024

### Passkeys

- Automatically upgrade someone’s password to a passkey after your app supplies a password to AutoFill if they’re eligible, while still retaining their password in case they need it. To do this, call [createCredentialRegistrationRequest(challenge:name:userID:requestStyle:)](<../authenticationservices/asauthorizationplatformpublickeycredentialprovider/createcredentialregistrationrequest(challenge_name_userid_requeststyle_).md>), passing [ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest.RequestStyle.conditional](../authenticationservices/asauthorizationplatformpublickeycredentialregistrationrequest/requeststyle-swift.enum/conditional.md) for the `requestStyle` parameter.
- Use the `prf` WebAuthentication extension to generate a symmetric key from a passkey, which you use for encrypting and decrypting someone’s data. Each passkey generates its own symmetric keys, which you can retrieve any time a user signs in with that passkey, in apps or on the web.

### Credential providers

- Indicate to the system that your credential provider participates in OTP AutoFill by adding the key `ProvidesOneTimeCodes` with the value `true` to the `ASCredentialProviderExtensionCapabilities` dictionary in your app’s information property list. Implement [provideCredentialWithoutUserInteraction(for:)](<../authenticationservices/ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for_)-3mo23.md>) and [prepareInterfaceToProvideCredential(for:)](<../authenticationservices/ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for_)-68qpo.md>) to handle the [ASOneTimeCodeCredentialRequest](../authenticationservices/asonetimecodecredentialrequest.md) type. Use [completeOneTimeCodeRequest(using:completionHandler:)](<../authenticationservices/ascredentialproviderextensioncontext/completeonetimecoderequest(using_completionhandler_).md>) to return the one time code to the system.
- Supply AutoFill for text in arbitrary text fields, for example to complete information about an account that someone manages in your credential provider, or AutoFill text in secure notes. Indicate to the system that your credential provider supplies AutoFill text by adding the key ProvidesTextToInsert with the value true to the `ASCredentialProviderExtensionCapabilities` dictionary in your app’s information property list, and implement [prepareInterfaceForUserChoosingTextToInsert()](<../authenticationservices/ascredentialproviderviewcontroller/prepareinterfaceforuserchoosingtexttoinsert().md>). When the person chooses the text to AutoFill in your UI, call [completeRequest(withTextToInsert:completionHandler:)](<../authenticationservices/ascredentialproviderextensioncontext/completerequest(withtexttoinsert_completionhandler_).md>) to supply the text to the system.
- Use [ASPasskeyCredentialExtensionInput](../authenticationservices/aspasskeycredentialextensioninput.md) to represent `largeBlob` and `prf` extension input data in a passkey credential request. Return output for these WebAuthentication extensions using [ASPasskeyAssertionCredentialExtensionOutput](../authenticationservices/aspasskeyassertioncredentialextensionoutput-swift.struct.md) and [ASPasskeyRegistrationCredentialExtensionOutput](../authenticationservices/aspasskeyregistrationcredentialextensionoutput-swift.struct.md) as part of the [ASPasskeyAssertionCredential](../authenticationservices/aspasskeyassertioncredential.md) and [ASPasskeyRegistrationCredential](../authenticationservices/aspasskeyregistrationcredential.md) objects you return to the system.

### Platform Single Sign-On

- Support stronger encryption and signing options by specifying [supportedDeviceEncryptionAlgorithms](../authenticationservices/asauthorizationproviderextensionregistrationhandler/supporteddeviceencryptionalgorithms.md), [supportedDeviceSigningAlgorithms](../authenticationservices/asauthorizationproviderextensionregistrationhandler/supporteddevicesigningalgorithms.md), and [supportedUserSecureEnclaveKeySigningAlgorithms](../authenticationservices/asauthorizationproviderextensionregistrationhandler/supportedusersecureenclavekeysigningalgorithms.md) in the SSO extension. You can now use Hybrid Public Key Encryption (HPKE) algorithms defined in [ASAuthorizationProviderExtensionEncryptionAlgorithm](../authenticationservices/asauthorizationproviderextensionencryptionalgorithm.md): `ecdhe_A256GCM`, `hpke_P256_SHA256_AES_GCM_256`, `hpke_P384_SHA384_AES_GCM_256`, and `hpke_Curve25519_SHA256_ChachaPoly`.
- If you use HPKE, receive notifications when the system rotates the encryption key by implementing [keyWillRotate(for:newKey:loginManager:completion:)](<../authenticationservices/asauthorizationproviderextensionregistrationhandler/keywillrotate(for_newkey_loginmanager_completion_).md>) in your SSO extension. The system automatically rotates the encryption key about once per week. This lets you register the new key on the server.
- Rotate the keys you use for platform SSO by calling the [ASAuthorizationProviderExtensionLoginManager](../authenticationservices/asauthorizationproviderextensionloginmanager.md) methods [beginKeyRotation(_:)](<../authenticationservices/asauthorizationproviderextensionloginmanager/beginkeyrotation(__).md>) and [completeKeyRotation(_:)](<../authenticationservices/asauthorizationproviderextensionloginmanager/completekeyrotation(__).md>).

## See Also

### Technology and frameworks

- [Accelerate updates](accelerate.md) — Learn about important changes to Accelerate.
- [Accessibility updates](accessibility.md) — Learn about important changes to Accessibility.
- [ActivityKit updates](activitykit.md) — Learn about important changes in ActivityKit.
- [AdAttributionKit Updates](adattributionkit.md) — Learn about important changes to AdAttributionKit.
- [App Clips updates](appclips.md) — Learn about important changes in App Clips.
- [App Intents updates](appintents.md) — Learn about important changes in App Intents.
- [AppKit updates](appkit.md) — Learn about important changes to AppKit.
- [Apple Intelligence updates](apple-intelligence.md) — Learn about important changes to Apple Intelligence.
- [AppleMapsServerAPI Updates](applemapsserverapi.md) — Learn about important changes to AppleMapsServerAPI.
- [Apple Pencil updates](applepencil.md) — Learn about important changes to Apple Pencil.
- [ARKit updates](arkit.md) — Learn about important changes to ARKit.
- [Audio Toolbox updates](audiotoolbox.md) — Learn about important changes to Audio Toolbox.
- [AVFAudio updates](avfaudio.md) — Learn about important changes to AVFAudio.
- [AVFoundation updates](avfoundation.md) — Learn about important changes to AVFoundation.
- [Background Tasks updates](backgroundtasks.md) — Learn about important changes in Background Tasks.
