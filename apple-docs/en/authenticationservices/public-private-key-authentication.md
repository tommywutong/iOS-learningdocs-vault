---
title: Public-Private Key Authentication
framework: Authentication Services
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/authenticationservices/public-private-key-authentication
source_url: 'https://developer.apple.com/documentation/authenticationservices/public-private-key-authentication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/authenticationservices/public-private-key-authentication.json'
content_hash: 'sha256:ee92b88f0b1a199e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Authentication Services](../authenticationservices.md)

# Public-Private Key Authentication

<sub>API Collection</sub>

Register and authenticate users with passkeys and security keys, without using passwords.

## Overview

Eliminating passwords simplifies account creation and authentication for apps and websites. Additionally, it reduces risks that arise from the reuse of one password across multiple services, brute force attacks, and social engineering that bad actors use to obtain credential information. By implementing public-private authentication according to the [W3C Web Authentication](https://www.w3.org/TR/webauthn-2/) specification, your users no longer need to remember complicated passwords or rely on password managers.

Instead of using a password, your macOS, iOS, or iPadOS device, known as the _authenticator_, generates a public-private key pair at account creation time, and sends the public key to the server. The server, known as the _relying party_, holds the public key for subsequent authentication, and uses _assertion_ to challenge the authenticator to prove its identity is valid.

There are two forms of public-private key authentication: _passkeys_ and _security keys._ With passkeys, the device stores its public-private key pair in the user’s iCloud Keychain and syncs the keys across the user’s devices. Security keys store the public-private key pair on a physical medium, such as a security card or a USB key.

## Topics

### Fundamentals

- [Connecting to a service with passkeys](connecting-to-a-service-with-passkeys.md) — Allow users to sign in to a service without typing a password.
- [Supporting passkeys](supporting-passkeys.md) — Eliminate passwords for your users when they sign in to apps and websites.
- [Supporting Security Key Authentication Using Physical Keys](supporting-security-key-authentication-using-physical-keys.md) — Allow users to authenticate using NFC, USB, and Lightning security keys in your app or service.

### Account registration

- [ASAuthorizationPublicKeyCredentialRegistration](asauthorizationpublickeycredentialregistration.md) — An interface that credential registration requests adhere to.
- [ASAuthorizationPlatformPublicKeyCredentialRegistration](asauthorizationplatformpublickeycredentialregistration.md) — A newly created platform credential that results from a credential registration request.
- [ASAuthorizationSecurityKeyPublicKeyCredentialRegistration](asauthorizationsecuritykeypublickeycredentialregistration.md) — A newly created security key credential that results from a credential registration request.
- [ASAuthorizationPublicKeyCredentialRegistrationRequest](asauthorizationpublickeycredentialregistrationrequest.md) — An interface that defines properties for a credential registration request.
- [ASAuthorizationPlatformPublicKeyCredentialRegistrationRequest](asauthorizationplatformpublickeycredentialregistrationrequest.md) — The object for registering a new platform public key credential.
- [ASAuthorizationSecurityKeyPublicKeyCredentialRegistrationRequest](asauthorizationsecuritykeypublickeycredentialregistrationrequest.md) — The object for registering a new security key credential.

### Account authentication

- [ASAuthorizationPublicKeyCredentialAssertion](asauthorizationpublickeycredentialassertion.md) — An interface for establishing a public key-based assertion.
- [ASAuthorizationPlatformPublicKeyCredentialAssertion](asauthorizationplatformpublickeycredentialassertion.md) — A class that represents the platform credential assertion type.
- [ASAuthorizationSecurityKeyPublicKeyCredentialAssertion](asauthorizationsecuritykeypublickeycredentialassertion.md) — A class that represents the security key credential assertion type.
- [ASAuthorizationPublicKeyCredentialAssertionRequest](asauthorizationpublickeycredentialassertionrequest.md) — An interface for requesting a public key-based credential assertion.
- [ASAuthorizationPlatformPublicKeyCredentialAssertionRequest](asauthorizationplatformpublickeycredentialassertionrequest.md) — The concrete assertion request type for platform credentials.
- [ASAuthorizationSecurityKeyPublicKeyCredentialAssertionRequest](asauthorizationsecuritykeypublickeycredentialassertionrequest.md) — A class that defines the assertion request type for security key credentials.

### Credential providers

- [ASAuthorizationPlatformPublicKeyCredentialProvider](asauthorizationplatformpublickeycredentialprovider.md) — A mechanism for providing public key credential requests to an app or service with iCloud Keychain.
- [ASAuthorizationSecurityKeyPublicKeyCredentialProvider](asauthorizationsecuritykeypublickeycredentialprovider.md) — A mechanism for providing public key credential requests to an app or service with a physical security key.

### Request configuration

- [ASPublicKeyCredential](aspublickeycredential.md) — An interface that defines the properties of the public key.
- [ASAuthorizationPublicKeyCredentialParameters](asauthorizationpublickeycredentialparameters.md) — An object that provides required parameters for the credential during registration.
- [ASCOSEAlgorithmIdentifier](ascosealgorithmidentifier.md) — An identifier for the algorithm that a credential’s key pair uses.
- [ASCOSEEllipticCurveIdentifier](ascoseellipticcurveidentifier.md) — A structure that contains the elliptic curve identifier.
- [ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialattestationkind.md) — A structure that defines the types of attestations a developer can request.
- [ASAuthorizationPublicKeyCredentialResidentKeyPreference](asauthorizationpublickeycredentialresidentkeypreference.md) — A structure that specifies the relying party’s preference for resident key storage.
- [ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialuserverificationpreference.md) — A structure that defines the relying party’s user verification preference.
- [ASAuthorizationPublicKeyCredentialDescriptor](asauthorizationpublickeycredentialdescriptor.md) — An interface that defines the credential identifier.
- [ASAuthorizationPlatformPublicKeyCredentialDescriptor](asauthorizationplatformpublickeycredentialdescriptor.md) — An object that holds the credential.
- [ASAuthorizationSecurityKeyPublicKeyCredentialDescriptor](asauthorizationsecuritykeypublickeycredentialdescriptor.md) — An object that holds public key credential transport information.
- [Transport](asauthorizationsecuritykeypublickeycredentialdescriptor/transport.md) — A structure that defines the security key credential transport type.
- [ASAuthorizationAllSupportedPublicKeyCredentialDescriptorTransports](asauthorizationsecuritykeypublickeycredentialdescriptor/transport/allsupported.md) — An array of currently supported transport types.

## See Also

### Passkeys

- [Passkey use in web browsers](passkey-use-in-web-browsers.md) — Register and authenticate website users by using passkeys.
- [Performing fast account creation with passkeys](performing-fast-account-creation-with-passkeys.md) — Allow people to quickly create an account with passkeys and associated domains.
- [Connecting to a service with passkeys](connecting-to-a-service-with-passkeys.md) — Allow users to sign in to a service without typing a password.
