---
title: Wallet
framework: PassKit (Apple Pay and Wallet)
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/passkit/wallet
source_url: 'https://developer.apple.com/documentation/passkit/wallet'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/passkit/wallet.json'
content_hash: 'sha256:ca7dbac6321037c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [PassKit (Apple Pay and Wallet)](../passkit.md)

# Wallet

<sub>API Collection</sub>

Manage tickets, boarding passes, payment cards and other passes in the Wallet app.

## Overview

To access your pass using PassKit, add the Wallet capability to your app. Use the API in Wallet to access and manage different types of passes, including identity passes, payment passes, and digital car keys. You can choose to access all of the passes signed with your developer team identifier, or access a subset of pass types. For information on adding capabilities to your app, see [Adding capabilities to your app](../xcode/adding-capabilities-to-your-app.md). For information on signing a pass, see [Wallet Passes](../walletpasses.md).

## Topics

### Essentials

- [Pass Type IDs Entitlement](../bundleresources/entitlements/com.apple.developer.pass-type-identifiers.md) — A list of identifiers that specify pass types that your app can access in Wallet.
- [Merchant IDs Entitlement](../bundleresources/entitlements/com.apple.developer.in-app-payments.md) — A list of merchant IDs your app uses for Apple Pay support.
- [com.apple.developer.in-app-identity-presentment](../bundleresources/entitlements/com.apple.developer.in-app-identity-presentment.md) — An entitlement that verifies age or identity.
- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md) — Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md) — Decrypt and verify an in-app presentment request on your server.

### Wallet Passes

- [Wallet Passes](../walletpasses.md) — Create, distribute, and update passes for the Wallet app.

### Common data types

- [PKObject](pkobject.md) — An opaque type that acts as the superclass for the pass object.
- [PKAddPassButton](pkaddpassbutton.md) — Provides a button that enables users to add passes to Wallet.
- [PKLabeledValue](pklabeledvalue.md) — An object that can represent a detail about a payment card or other item.
- [AddPassToWalletButton](addpasstowalletbutton.md) — A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [AddPassToWalletButtonFilter](addpasstowalletbuttonfilter.md)
- [AddPassToWalletButtonResponse](addpasstowalletbuttonresponse.md)
- [AddPassToWalletButtonStyle](addpasstowalletbuttonstyle.md)

### Pass library

- [PKPassLibrary](pkpasslibrary.md) — Provides an interface to the user’s library of passes.

### General purpose passes

- [PKSecureElementPass](pksecureelementpass.md) — A pass with a credential that the device stores in a certified payment information chip.
- [PKAddSecureElementPassConfiguration](pkaddsecureelementpassconfiguration.md) — An object that describes the configuration of a secure element payment pass.
- [PKAddSecureElementPassViewController](pkaddsecureelementpassviewcontroller.md) — A view controller that manages the addition of secure element payment passes.
- [PKPass](pkpass.md) — An object that represents a single pass.
- [PKAddPassesViewController](pkaddpassesviewcontroller.md) — Lets your app show a pass and prompt the user to add that pass to the pass library.
- [AsyncShareablePassConfiguration](asyncshareablepassconfiguration.md)
- [PKShareSecureElementPassViewController](pksharesecureelementpassviewcontroller.md)
- [PKShareSecureElementPassViewControllerDelegate](pksharesecureelementpassviewcontrollerdelegate.md)
- [Preview](pkshareablepassmetadata/preview-swift.class.md)
- [PKShareSecureElementPassResult](pksharesecureelementpassresult.md)

### Identity passes and authorization

- [Requesting identity data from a Wallet pass](requesting-identity-data-from-a-wallet-pass.md) — Initiate a request for identity information by prompting a user for permission and decrypting a response payload.
- [Configuring your environment for the Verify with Wallet API](configuring-your-environment-for-the-verify-with-wallet-api.md) — Set up your environment to use Verify with Wallet.
- [Verifying Wallet identity requests](verifying-wallet-identity-requests.md) — Decrypt and verify an in-app presentment request on your server.
- [PKIdentityPhotoIDDescriptor](pkidentityphotoiddescriptor.md) — An object you use to request information from a user’s photo ID or equivalent document.
- [PKIdentityAnyOfDescriptor](pkidentityanyofdescriptor.md) — An object you use to request information from multiple identity documents.
- [PKIdentityDriversLicenseDescriptor](pkidentitydriverslicensedescriptor.md) — An object for requesting information from a user’s driver’s license or equivalent document.
- [PKAddIdentityDocumentMetadata](pkaddidentitydocumentmetadata.md) — The object for specifying the metadata necessary to provision identity documents.
- [PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md) — Configuration to define the identity document.
- [PKAddIdentityDocumentType](pkaddidentitydocumenttype.md) — Classifications that reflect the type of identity document.
- [JPKIPassContents](jpkipasscontents.md) — A set of actions for viewing and updating PINs, passwords, and signing abilities associated with digital identities on the JPKI applet.
- [PKAddIdentityDocumentConfiguration](pkaddidentitydocumentconfiguration.md) — Configuration to define the identity document.
- [PKAddPassMetadataPreview](pkaddpassmetadatapreview.md) — A preview object that contains information representing the pass you add to Wallet.
- [PKIdentityDocumentMetadata](pkidentitydocumentmetadata.md) — A set of configured metadata that defines the required information to add the corresponding pass to Wallet.
- [PKIdentityNationalIDCardDescriptor](pkidentitynationalidcarddescriptor.md) — An object for requesting information from a user’s national ID card.
- [PKJapanIndividualNumberCardMetadata](pkjapanindividualnumbercardmetadata.md) — A class that contains metadata indicating the specific product instance to provision.

### Identity sheet interactions and authorization

- [PKIdentityAuthorizationController](pkidentityauthorizationcontroller.md) — An object that presents a sheet that prompts the user to allow a request for identity information.
- [PKIdentityRequest](pkidentityrequest.md) — An object that represents a request for identity information from a Wallet pass.
- [PKIdentityDocument](pkidentitydocument.md) — An object that represents the response to a request.
- [PKIdentityElement](pkidentityelement.md) — An object that represents the elements an app requests from identity documents.
- [PKIdentityButton](pkidentitybutton.md) — An object that displays a button to trigger the identity verification flow.
- [VerifyIdentityWithWalletButton](verifyidentitywithwalletbutton.md) — A type that displays a button to present the identity verification flow.
- [VerifyIdentityWithWalletButtonLabel](verifyidentitywithwalletbuttonlabel.md) — A type that represents the label you use with a verify identity button.
- [VerifyIdentityWithWalletButtonStyle](verifyidentitywithwalletbuttonstyle.md) — A type that represents the style you use with a verify identity button.

### Payment passes

- [PKPaymentPass](pkpaymentpass.md) — An object that represents a provisioned payment card for in-app payments.
- [PKAddPaymentPassViewController](pkaddpaymentpassviewcontroller.md) — Displays an interface that lets users add cards to Apple Pay from within your app.

### Stored-value passes

- [PKTransitPassProperties](pktransitpassproperties.md) — The properties of a transit pass.
- [PKSuicaPassProperties](pksuicapassproperties.md) — The properties of a pass used as a ticket for the Suica transportation system.
- [PKStoredValuePassProperties](pkstoredvaluepassproperties.md) — An object that represents the properties of a pass that contains a balance used for specific transactions, such as a transit pass or loyalty card.
- [PKStoredValuePassBalance](pkstoredvaluepassbalance.md) — An object that represents a balance that’s available for transactions, such as points or money.

### Shareable passes

- [PKAddShareablePassConfiguration](pkaddshareablepassconfiguration.md) — An object that represents the data and action for a shared copy of pass.
- [PKShareablePassMetadata](pkshareablepassmetadata.md) — Information that you use to configure the sharing sheet for a pass.
- [PKAddShareablePassConfigurationPrimaryAction](pkaddshareablepassconfigurationprimaryaction.md) — The kind of add action that the system performs with a pass.

### Digital car keys

- [PKAddCarKeyPassConfiguration](pkaddcarkeypassconfiguration.md) — A specialized configuration object that PassKit uses when it creates a digital car key.
- [PKVehicleConnectionSession](pkvehicleconnectionsession.md)
- [PKVehicleConnectionDelegate](pkvehicleconnectiondelegate.md)
- [PKVehicleConnectionSessionConnectionState](pkvehicleconnectionsessionconnectionstate.md)

### Issuer cards

- [Implementing Wallet Extensions](implementing-wallet-extensions.md) — Support adding an issued card to Apple Pay from directly within Apple Wallet using Wallet Extensions.
- [PKIssuerProvisioningExtensionHandler](pkissuerprovisioningextensionhandler.md) — An abstract superclass for an app extension to add a payment card to Wallet.
- [PKIssuerProvisioningExtensionAuthorizationProviding](pkissuerprovisioningextensionauthorizationproviding.md) — A protocol for a UI app extension to authorize a user to add a payment card to Wallet.

### Errors

- [PKPassKitError](pkpasskiterror.md) — Errors that the PassKit framework uses.
- [PKAddSecureElementPassError](pkaddsecureelementpasserror.md) — An error object that PassKit uses when it adds Secure Element passes.
- [Code](pkpasskiterror/code.md) — Errors that the PassKit framework uses.
- [Code](pkaddsecureelementpasserror/code.md) — Error codes for problems that occur when you add a secure element passes.
- [PKAddPaymentPassError](pkaddpaymentpasserror.md) — Error codes for adding payment passes.
- [PKIdentityError](pkidentityerror-swift.struct.md) — A structure that represents an identity error.
- [Code](pkidentityerror-swift.struct/code.md) — Error codes for identity operations.
- [PKShareSecureElementPassError](pksharesecureelementpasserror.md)
- [Code](pksharesecureelementpasserror/code.md)
- [PKVehicleConnectionErrorCode](pkvehicleconnectionerrorcode.md)
- [PayWithApplePayButtonPaymentAuthorizationPhase](paywithapplepaybuttonpaymentauthorizationphase.md)
- [PKPassKitErrorDomain](pkpasskiterrordomain.md) — The error domain for PassKit errors.
- [PKIdentityErrorDomain](pkidentityerrordomain.md) — The error domain for identity errors.
- [PKAddSecureElementPassErrorDomain](pkaddsecureelementpasserrordomain.md) — The error domain for errors that occur when adding a secure pass.
- [PKShareSecureElementPassErrorDomain](pksharesecureelementpasserrordomain.md)

### Deprecated

- [PayLaterView](paylaterview.md) — A view that displays the Apple Pay Later visual merchandising widget. _(deprecated)_
- [PKPayLaterView](pkpaylaterview.md) — A view that displays the Apple Pay Later visual merchandising widget. _(deprecated)_
