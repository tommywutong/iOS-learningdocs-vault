---
title: Code Signing Guide
apple_id: TP40005929
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Security
technology: Security
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/AboutCS/AboutCS.html
archived_at: '2026-07-18T02:06:11.341547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Code Signing Guide](About%20Code%20Signing.md)


[Next](Code%20Signing%20Tasks.md)[Previous](About%20Code%20Signing.md)

# Understanding the Code Signature

All sorts of code can be signed, including tools, applications, scripts, libraries, plug-ins, and other “code-like” data. In addition, you can create signed installer packages, and signed disk images. In all cases, the code signature consists of three parts:

- __A seal.__ This is a collection of checksums or hashes of the various parts of the code, created by the code signing software. The seal can be used at verification time to detect alterations.
- __A digital signature.__ The code signing software encrypts the seal using the signer’s identity to create a digital signature. This guarantees the seal’s integrity.
- __Code requirements.__ These are the rules governing verification of the code signature. Some are inherent to the verifier (depending on its goals). Others are specified by the signer and sealed with the rest of the code.

The code signing machinery generates the seal by running different parts of your final bundle (app, library, or framework), including executables, resources, the `Info.plist` file, code requirements, and so on, through a one-way hashing algorithm. This produces a series of digests, or checksums, which are short strings of digits that are unique to a particular input block, but which cannot be used to reconstruct the original input.

A verifying entity that has both the code under evaluation, and the corresponding collection of hashes, runs the same hashing algorithm on the code in exactly the same way as the signer, and compares the results to the original, stored hashes to see if anything has changed. Even a small modification in the code results in a different digest, which indicates tampering or corruption. However, this verification is only as reliable as the reliability of the stored hash. The digital signature guarantees this.

As explained in _[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_, a digital signature uses public key cryptography to ensure data integrity. Like a signature written with ink on paper, a digital signature can be used to identify and authenticate the signer. However, a digital signature is more difficult to forge, and goes one step further: it can ensure that the signed data has not been altered. This is somewhat like designing a paper check or money order in such a way that if someone alters the written amount of money, a watermark with the text “Invalid” becomes visible on the paper.

In the context of code signing, the signing software creates the digital signature by encrypting the seal’s hashes with the signer’s private key. Because only the signer possesses the private key, only the signer is able to perform this encryption. It is this collection of encrypted hashes that the signer stores in the app (or framework, archive, or other signed object), along with the matching certificate, which collectively represent the digital signature.

To verify the signature, the verifying software computes the same set of hashes across the various blocks of code and data. It then uses the signer’s public key, which is embedded in the certificate, to decrypt the encrypted hashes that came with the code, thus obtaining the original hash as computed by the signer. If the two hashes match, the data has not been modified since it was signed by someone in possession of the signer’s private key.

Although not strictly required for code signing to work, the certificate itself is usually signed by a trusted certificate authority. If not, the verifier can be sure of the certificate’s stability from one release to another, but not of its origin. If it is, the certificate authority, often Apple, vouches for the identity of the signer.

Signed code may contain several different digital signatures:

- If the code is universal, the object code for each slice (architecture) is signed separately. This signature is stored within the binary file itself.
- Various data components of the application bundle (such as the `Info.plist` file, if there is one) are also signed. These signatures are stored in a file called `_CodeSignature/CodeResources` within the bundle.
- Nested code, such as libraries, helper tools, and other bits of code that are embedded in the app are themselves signed, and their signatures are also stored in `_CodeSignature/CodeResources` within the bundle.

Code requirements are the rules macOS uses to evaluate a code signature. The system doing the evaluating decides what code requirements to apply at evaluation time, depending on its goals. For example, Gatekeeper has a rule that, before an app is allowed to launch for the first time, it must be signed by a Mac App Store or Developer ID certificate. As another example, an app could enforce a code requirement that all plug-ins used by that app should be signed by Apple.

Code requirements specified by the signer and included as part of the code signature are known as _internal requirements_. These are available to the system verifying a code signature, but the system may choose to use them or not. A plug-in for the app in the previous example might come with its own internal requirements, but it would be up to the evaluating system, the app using the plug-in, to decide whether to apply them. Because the seal covers the code requirements, the internal requirements are also certain to be intact as long as the signature is valid.

The most important internal requirement is the _designated requirement_, or DR. This rule tells an evaluating system how to identify a particular piece of code. Any two pieces of code that have (and successfully verify against) the same DR are considered to be the same code. This allows a code signer to publish a new version of an app that is treated as the same app. For example, the DR for Apple Mail might be "was signed by Apple and has the identifier `com.apple.Mail`". When a new version of the app is published, as long as a new version of the app has the same DR, it is still considered Apple Mail, even if the binary executable is completely different. Further, only Apple can sign as Apple, so no one else can make an app that masquerades as the Mail app.

The program identifier or the entire designated requirement can be specified explicitly by the signer. Typically, the signing machinery automatically builds a designated requirement using the name of the program found in its `Info.plist` file as the `CFBundleIdentifier`, and the chain of signatures securing the code signature.

In practical terms, code requirements are stated as scripts, written in a dedicated language, that describe conditions (restrictions) code must satisfy to be acceptable for some purpose. See [Code Signing Requirement Language](Code%20Signing%20Requirement%20Language.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqnjnknltc) for a detailed description of the code requirement scripting language.

macOS subsystems perform validation of signed code against a set of requirements when they need to determine whether it is safe to trust that code for some purpose. As described in [The Digital Signature](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrzfvbuqmznknlte), internal requirements, and especially the designated requirement, come from the code signature itself. Other requirements are inherent to the system doing the verification.

Table 2-1 gives concrete examples of how code signatures are used by different subsystems in macOS to enforce trust policies that are specific to a particular kind of system resource. Note that these are default behaviors; you can modify many of the code signing polices of macOS with the `spctl(8)` command.

__Table 2-1__  Examples of macOS subsystems that verify the validity of code

| Subsystem | Function | Initial policy | Tracking policy |
| App Sandbox | Gates access to system resources based on entitlements. | Allow if entitlement is present in the app's code signature. | Initial policy decision verified against the application's DR. |
| Gatekeeper | Restricts launching of applications from unidentified developers | A configurable trusted anchor check (Developer ID or Mac App Store). | None (each request evaluated independently). |
| Application Firewall | Restricts inbound network access by applications. | Allow if a trusted anchor check succeeds; otherwise prompt the user. | Initial policy decision verified against the application's DR. |
| Parental Controls (MCX) | Restricts what applications a managed user can run. | Explicit administrator decision (no code signing involved in the initial decision). | Initial policy decision verified against the application's DR. |
| Keychain Access Controls | Controls what applications can do with specific keychain items. | The creating application is automatically trusted with its item, and determines the access policy using code signing requirements. | Free access to the keychain item by the creating application and tracked with its DR (No automatic tracking for custom ACLs). |
| Developer Tools Access (DTA) | Restricts what programs are allowed to call DTA APIs (task_for_pid, etc.) | A hard-coded trusted anchor check. | None (each request evaluated independently). |

The above examples demonstrate how policy decisions are determined by specific subsystems and not by code signing itself. In addition, they highlight the diversity of policies. For example:

- DTA doesn't have a tracking policy. It simply applies a set requirement to every requester without needing to retain any information.
- Application Firewall uses code signing for both its initial and tracking policy decisions.
- The keychain acts on the tracking policy by default but it can also allow arbitrary requirement-bearing ACLs to be added to express arbitrary policies determined by the owner of a specific keychain item.
- App Sandbox relies on entitlements embedded in the code signature to decide when to grant access to the system resources that your app requires, such as network connections, the camera, parts of the file system, and so on. Because entitlements are part of, and thus sealed by, the code signature, App Sandbox trusts that these are the resources the developer intended to request.

  In fact, all entitlements (for App Sandbox or otherwise) are stored in and sealed by the code signature, so any app that uses entitlements of any kind requires a code signature.

Some parts of macOS do not care about the identity of the signer. They care only whether the app is _validly signed and stable_. Stability is determined through the DR, and does not depend on the nature of the certificate authority used. The keychain system and parental controls are examples of such usage. Self-signed identities and homemade certificate authorities (CA) work by default for this case. Because they do not work for Gatekeeper, they are generally not recommended for distribution, but they may be useful during development or for test purposes.

Other parts of macOS constrain acceptable signatures to only those drawn from certificate authorities that are trusted on the system performing the validation. For those checks, the nature of the identity certificate used does matter. The Application Firewall is one example of this usage. Self-signed identities and self-created certificate authorities are not valid for this check unless the verifying system has been told to trust them for Application Firewall purposes.

For the most part, policy decisions are made at a single point in time, which may affect system behavior. For example, unsigned code injected into an application through a buffer overflow can still execute because it was not part of the application at launch time, and thus not evaluated by Gatekeeper.

[Next](Code%20Signing%20Tasks.md)[Previous](About%20Code%20Signing.md)

