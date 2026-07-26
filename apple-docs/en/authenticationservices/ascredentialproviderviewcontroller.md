---
title: ASCredentialProviderViewController
framework: Authentication Services
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/authenticationservices/ascredentialproviderviewcontroller
source_url: 'https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/authenticationservices/ascredentialproviderviewcontroller.json'
content_hash: 'sha256:f64745613c89b175'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Authentication Services](../authenticationservices.md)

# ASCredentialProviderViewController

<sub>Class</sub>

A view controller that a credential manager app uses to extend AutoFill.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class ASCredentialProviderViewController
```

## Overview

To integrate a password, passkey, or one-time passcode manager app with AutoFill:

1. Add a Credential Provider Extension target to your project that subclasses [ASCredentialProviderViewController](ascredentialproviderviewcontroller.md). Add the [AutoFill Credential Provider Entitlement](../bundleresources/entitlements/com.apple.developer.authentication-services.autofill-credential-provider.md) to both the extension and its containing app.
2. Override the view controller’s [- prepareCredentialListForServiceIdentifiers:](<ascredentialproviderviewcontroller/preparecredentiallist(for_).md>) method to prepare a view with a list of credentials that the person can choose from after opening your extension from the AutoFill suggestions list.
3. Optionally add [ASPasswordCredentialIdentity](aspasswordcredentialidentity.md) and [ASPasskeyCredentialIdentity](aspasskeycredentialidentity.md) instances to the shared [ASCredentialIdentityStore](ascredentialidentitystore.md) to make identities available directly in the AutoFill suggestions list. Then override the [- provideCredentialWithoutUserInteractionForRequest:](<ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for_)-3mo23.md>) method to provide the associated credentials when the person taps a suggestion.
4. Optionally, override the [- prepareInterfaceForExtensionConfiguration](<ascredentialproviderviewcontroller/prepareinterfaceforextensionconfiguration().md>) method to specify a configuration interface that you can show when people first enable your credentials manager in Settings.

### Receiving credential updates

Apps and websites that allow sign-ins can signal updates to the operating system with the [ASCredentialUpdater](ascredentialupdater.md) class. The various “report” methods of [ASCredentialUpdater](ascredentialupdater.md) work like the “signal” methods of `PublicKeyCredential` when using WebAuthn on the web. For example, a website or app can notify credential manager apps that it updated a user name or email for a given account, allowing the manager to stay consistent with the website.

Your credential manager manager receives these updates in the “report” methods of `ASCredentialProviderViewController`. Use these calls to update your manager’s stored credential data or behavior. For example, a call to [- reportUnusedPasswordCredentialForDomain:userName:](<ascredentialproviderviewcontroller/reportunusedpasswordcredential(fordomain_username_).md>) can indicate that someone using a passkey will no longer use a password to sign in to a given domain, or that they deleted their account. In this case, the manager should stop showing the user name and password for that domain.

> [!note] Note
> This class ignores calls from Mac apps built with Mac Catalyst.

## Relationships

- **Inherits From**: [NSViewController](../appkit/nsviewcontroller.md), [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSEditor](../appkit/nseditor.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSeguePerforming](../appkit/nssegueperforming.md), [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md), [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## Topics

### Getting the extension context

- [extensionContext](ascredentialproviderviewcontroller/extensioncontext.md) — The context your credential provider extension uses to provide information to the system.
- [ASCredentialProviderExtensionContext](ascredentialproviderextensioncontext.md) — A mechanism that credential provider extensions use to communicate with the system.

### Configuring the credential provider extension

- [- prepareInterfaceForExtensionConfiguration](<ascredentialproviderviewcontroller/prepareinterfaceforextensionconfiguration().md>) — Prepares the interface to enable the user to configure the extension.
- [ASCredentialIdentityStore](ascredentialidentitystore.md) — A container that your extension fills to provide credentials through the QuickType bar.

### Selecting a credential

- [- prepareCredentialListForServiceIdentifiers:](<ascredentialproviderviewcontroller/preparecredentiallist(for_).md>) — Prepares the interface to display a list of credentials from which the user can select.
- [- prepareCredentialListForServiceIdentifiers:requestParameters:](<ascredentialproviderviewcontroller/preparecredentiallist(for_requestparameters_).md>) — Prepares the interface to display a list of passkey and password credentials from which the user can select.
- [- prepareOneTimeCodeCredentialListForServiceIdentifiers:](<ascredentialproviderviewcontroller/prepareonetimecodecredentiallist(for_).md>) — Prepares the interface to display a list of one-time passcodes (OTPs) that people can select from.
- [- prepareInterfaceForPasskeyRegistration:](<ascredentialproviderviewcontroller/prepareinterface(forpasskeyregistration_).md>) — Prepare the view controller to show user interface for registering a new passkey.
- [- prepareInterfaceToProvideCredentialForRequest:](<ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for_)-68qpo.md>) — Prepare the view controller to show user interface for providing the requested credential.
- [- provideCredentialWithoutUserInteractionForRequest:](<ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for_)-3mo23.md>) — Attempts to provide the user-requested credential with no further user interaction.
- [- performPasskeyRegistrationWithoutUserInteractionIfPossible:](<ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible(passkeyregistration_).md>) — Perform a conditional passkey registration, if possible.
- [ASCredentialServiceIdentifier](ascredentialserviceidentifier.md) — An identifier representing a particular service for which the user needs a credential, like a web site.
- [ASCredentialRequest](ascredentialrequest.md) — A protocol that describes a request from the user for your extension to provide a credential.
- [ASPasswordCredentialRequest](aspasswordcredentialrequest.md) — A class that represents a request to supply a password credential.
- [ASOneTimeCodeCredentialRequest](asonetimecodecredentialrequest.md)
- [ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md) — An interface that defines properties for a credential registration request.
- [ASPasskeyCredentialRequest](aspasskeycredentialrequest.md) — A class that represents a request to supply a passkey credential.
- [ASPasskeyCredentialRequestParameters](aspasskeycredentialrequestparameters.md) — A class that represents information about a passkey credential request.

### Providing text to AutoFill

- [- prepareInterfaceForUserChoosingTextToInsert](<ascredentialproviderviewcontroller/prepareinterfaceforuserchoosingtexttoinsert().md>) — Prepare the view controller to show a list of all insertable text with user selectable fields.

### Recognizing errors

- [ASExtensionError](asextensionerror.md) — A credential provider extension error.
- [ASExtensionErrorDomain](asextensionerrordomain.md) — The domain for a credential provider extension error.
- [Code](asextensionerror/code.md) — The codes for a credential provider extension error.

### Accessing settings

- [ASSettingsHelper](assettingshelper.md) — A class that opens Settings and navigates to the settings for configuring credential providers.

### Receiving credential updates

- [- reportAllAcceptedPublicKeyCredentialsForRelyingParty:userHandle:acceptedCredentialIDs:](<ascredentialproviderviewcontroller/reportallacceptedpublickeycredentials(forrelyingparty_userhandle_acceptedcredentialids_).md>) — Receives a report from the system that a relying party sent a snapshot of all accepted credentials for an account.
- [- reportPublicKeyCredentialUpdateForRelyingParty:userHandle:newName:](<ascredentialproviderviewcontroller/reportpublickeycredentialupdate(forrelyingparty_userhandle_newname_).md>) — Receives a report from the system that a relying party indicated that a passkey’s user name updated.
- [- reportUnknownPublicKeyCredentialForRelyingParty:credentialID:](<ascredentialproviderviewcontroller/reportunknownpublickeycredential(forrelyingparty_credentialid_).md>) — Receives a report from the system that a relying party indicated a passkey credential is invalid.
- [- reportUnusedPasswordCredentialForDomain:userName:](<ascredentialproviderviewcontroller/reportunusedpasswordcredential(fordomain_username_).md>) — Receives a report from the system that a relying party indicatd that a password credential isn’t needed anymore for a given user name.

### Deprecated methods

- [- provideCredentialWithoutUserInteractionForIdentity:](<ascredentialproviderviewcontroller/providecredentialwithoutuserinteraction(for_)-7jlg0.md>) — Attempts to provide the user-requested credential with no further user interaction. _(deprecated)_
- [- prepareInterfaceToProvideCredentialForIdentity:](<ascredentialproviderviewcontroller/prepareinterfacetoprovidecredential(for_)-18ukb.md>) — Prepares the interface for a user interaction, like a database login, that enables it to access and return the credential for the given identity. _(deprecated)_

### Instance Methods

- [- performGeneratePasswordsRequestWithoutUserInteraction:](<ascredentialproviderviewcontroller/performwithoutuserinteraction(generatepasswordsrequest_).md>) — Attempt to generate passwords based on developer-specified rules.
- [- performSavePasswordRequestWithoutUserInteractionIfPossible:](<ascredentialproviderviewcontroller/performwithoutuserinteractionifpossible(savepasswordrequest_).md>) — Attempt to save a password credential.
- [- prepareInterfaceForSavePasswordRequest:](<ascredentialproviderviewcontroller/prepareinterface(for_)-69elg.md>) — Prepares the interface to display a prompt to save a password credential.
- [- prepareInterfaceForGeneratePasswordsRequest:](<ascredentialproviderviewcontroller/prepareinterface(for_)-7ideq.md>) — Prepares the interface to display a prompt to generate passwords based on developer-specified rules.

## See Also

### AutoFill credentials

- [Providing one-time passcodes to AutoFill](providing-one-time-passcodes-to-autofill.md) — Help people efficiently perform multifactor authentication.
- [AutoFill Credential Provider Entitlement](../bundleresources/entitlements/com.apple.developer.authentication-services.autofill-credential-provider.md) — A Boolean value that indicates whether the app may, with user permission, provide user names and passwords for AutoFill in Safari and other apps.
