---
title: Security Overview
apple_id: TP30000976
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Security
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/EndUserSecurityFeatures/EndUserSecurityFeatures.html
archived_at: '2026-07-18T02:06:30.109609Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Overview](About%20Software%20Security.md)


[Next](Other%20Security%20Resources.md)[Previous](Security%20Server%20and%20Security%20Agent.md)

# End-User Security Features

macOS and iOS have many built-in security features, including industry-standard digital signatures and encryption for Apple’s Mail app, and authentication for the Safari web browser.

In iOS, these features are largely invisible to the user, because security is handled by the system without the user’s intervention.

In macOS, the following four features are most visible to users:

- The Security system preferences pane
- FileVault, which users can configure through the Security system preferences pane
- The Accounts system preferences pane
- The Keychain Access app

These features are described in this appendix.

Security and Privacy system preferences in macOS let the user configure FileVault and control some aspects of authorization on the computer. For example, users can indicate whether a password should be required after sleep or the screen saver begins.

At the bottom of the dialog is the lock icon provided by the authorization view (see [Designing Secure User Interfaces](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/AppInterfaces.html#//apple_ref/doc/uid/TP40002862) in _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_). When this icon shows a closed lock, authorization is required before the user can change the settings in this system preferences pane.

When the user turns on FileVault, macOS uses 128-bit AES encryption to encrypt everything on the root volume (or everything in the user’s home folder prior to OS X 10.7).

The system automatically decrypts files upon access if an authorized user is logged in, but the files remain encrypted on disk. This provides maximum security for a user’s files if all of the following are true:

- All sensitive data is stored on an encrypted volume (or in the user’s home directory prior to OS X 10.7).
- Permissions are set appropriately to protect the data from other users on the system.
- Automatic login is disabled.
- A password is required to wake from sleep or to wake from the screen saver.

A user can also create new external volumes with FileVault encryption using Disk Utility. Alternatively, if a user wants to securely store files somewhere other than a FileVault-protected volume (such as on an external hard disk or removable media), the user can create an encrypted disk image.

For more information about FileVault, see [Apple Knowledge Base Article HT4790](http://support.apple.com/kb/HT4790).

When a user installs macOS on a computer, that user automatically becomes a member of the `admin` group (described in [The Admin Group](../../File%20Management/File%20System%20Programming%20Guide/File%20System%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzsfvbuqobnknltenq)). Subsequently, the user or any other member of the `admin` group can use the _Users & Groups_ system preferences panes to add new users to the system.

For each new user, the administrator can specify whether that user should be a member of the `admin` group. If not, the administrator can limit the system features and apps to which that user has access.

_Keychain Access_ is an macOS utility that lets users see and modify the passwords, certificates, and other data that are stored in their keychains.

With Keychain Access, users can:

- Create new keychains
- Add and delete keychain items
- Lock and unlock keychains
- Choose one keychain to be the default
- See which certificates are available for use by email and web apps, who owns each certificate, and who issued each certificate
- See and change passwords stored for various apps, tools, and websites
- Securely store other secrets, such as passwords, credit card numbers, and notes

When a keychain is locked and an app or other tool needs to gain access to a keychain item, Keychain Services prompts the user for a password.

In addition, the Keychain Access menu includes items to open the Certificate Assistant and Kerberos Ticket Viewer utilities. The Certificate Assistant enables users to create certificates, request certificates from a certificate authority, create a public/private key pair, or evaluate a certificate. The Kerberos Ticket Viewer lets users see any Kerberos tickets in use on the system, and enables them to renew or destroy a ticket, or change a ticket’s password. Kerberos is described in more detail in _[Authentication, Authorization, and Permissions Guide](../Authentication%2C%20Authorization%2C%20and%20Permissions%20Guide/About%20Authentication%2C%20Authorization%2C%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytembq)_.

Apple’s Mail app and other email apps can extract a public key from the signing certificate of any signed email and use it to encrypt messages sent to the owner of that key. See [Digital Signatures](../Cryptographic%20Services%20Guide/Cryptography%20Concepts%20In%20Depth.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzsfvbuqobnineeisshijbuc) in _[Cryptographic Services Guide](../Cryptographic%20Services%20Guide/About%20Cryptographic%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzs)_ for more information about digital signatures, and see Help in the Mail app for details on sending encrypted email.

[Next](Other%20Security%20Resources.md)[Previous](Security%20Server%20and%20Security%20Agent.md)

