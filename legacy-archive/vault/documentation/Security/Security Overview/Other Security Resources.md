---
title: Security Overview
apple_id: TP30000976
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: Security
technology: null
published: '2012-12-13'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/Security_Overview/SeeAlso/SeeAlso.html
archived_at: '2026-07-18T02:06:31.493353Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Security Overview](About%20Software%20Security.md)


[Next](Document%20Revision%20History.md)[Previous](End-User%20Security%20Features.md)

# Other Security Resources

Now that you’ve read about the basics, there are a few more things you should learn. First, read these two documents:

- _[App Sandbox Design Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/AppSandboxDesignGuide/AboutAppSandbox/AboutAppSandbox.html#//apple_ref/doc/uid/TP40011183)_ tells you the things you need to know about designing code to run in a sandboxed environment before you write the first line of code.
- _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_ describes in more detail how to design code in ways that maximize security, and also describes what you do while actually writing the code to avoid security holes.

When you’re ready to test your code, the static analyzer in Xcode is a great tool for uncovering a lot of common security bugs. Read [Xcode Help](https://help.apple.com/xcode) to learn more about the kinds of testing and analysis that you can perform with Xcode.

After reading those documents, consider reading some of the documents listed in the rest of this appendix.

Here are a few other Apple documents you might be interested in, depending on what technologies you want to learn more about.

__Authentication and Authorization__

- _[Authentication, Authorization, and Permissions Guide](../Authentication%2C%20Authorization%2C%20and%20Permissions%20Guide/About%20Authentication%2C%20Authorization%2C%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytembq)_ provides additional information about authentication and authorization at a conceptual level. (macOS only)
- _[Authorization Services Programming Guide](../Authorization%20Services%20Programming%20Guide/Introduction%20to%20Authorization%20Services%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojv)_ and _[Authorization Services C Reference](https://developer.apple.com/documentation/security/authorization_services)_ explain how to perform certain authorization-related tasks. (macOS only; note that many of these tasks, such as elevating privilege, are not allowed in a sandboxed environment)
- _[Open Directory Programming Guide](https://developer.apple.com/library/archive/documentation/Networking/Conceptual/Open_Directory/Introduction/Introduction.html#//apple_ref/doc/uid/TP40000917)_ explains how to use Open Directory APIs to authenticate a user or obtain information about a user. (macOS only)
- _[Security Interface Framework Reference](https://developer.apple.com/documentation/securityinterface)_ describes the Objective-C interface to Authorization Services. This interface also provides a variety of security-related user interface elements. (macOS only)
- Technical Note TN2095, _[Authorization for Everyone](https://developer.apple.com/library/archive/technotes/tn2095/_index.html#//apple_ref/doc/uid/DTS10003110)_, also discusses the use of Authorization Services. (macOS only)

__Cryptography__

- _[Cryptographic Services Guide](../Cryptographic%20Services%20Guide/About%20Cryptographic%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzs)_ describes encryption, decryption, signing, verifying, digital certificates, and other related concepts in more detail at a conceptual level.
- _[Security Transforms Programming Guide](../Security%20Transforms%20Programming%20Guide/About%20Security%20Transforms.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydqmbr)_ describes a macOS API for certain cryptographic tasks. (macOS only)
- _[Certificate, Key, and Trust Services Reference](https://developer.apple.com/documentation/security/certificate_key_and_trust_services)_ explains how to work with certificates, keys, and other related technologies in more detail.

__Code And Application Signing__

- [Cryptography Concepts In Depth](https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/CryptographyConcepts/CryptographyConcepts.html#//apple_ref/doc/uid/TP40011172-CH8) in _[Cryptographic Services Guide](../Cryptographic%20Services%20Guide/About%20Cryptographic%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytcnzs)_ explains code signing concepts in greater depth.
- _[Code Signing Guide](../Code%20Signing%20Guide/About%20Code%20Signing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2tsmrz)_ tells you how to perform code signing on the command line and other unusual signing-related tasks.

__Secure Storage__

- _[Keychain Services Reference](https://developer.apple.com/documentation/security/keychain_services)_ explains how to use the keychain in your code.
- [Protecting Data Using On-Disk Encryption](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/StrategiesforImplementingYourApp/StrategiesforImplementingYourApp.html#//apple_ref/doc/uid/TP40007072-CH5-SW21) in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_ explains how to use the iOS data protection feature in your app. (iOS only)

__Secure Networking__

- _[CFNetwork Programming Guide](../../Networking/CFNetwork%20Programming%20Guide/Introduction%20to%20CFNetwork%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcmzs)_ and [URL Loading System](https://developer.apple.com/documentation/foundation/url_loading_system) explain how to make secure network connections using high-level APIs.
- _[Secure Transport Reference](https://developer.apple.com/documentation/security/secure_transport)_ tells how to make secure network connections at the socket layer. (macOS only)

__Privilege Separation__

- [Designing Secure Helpers and Daemons](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/DesigningSecureHelpers/DesigningSecureHelpers.html#//apple_ref/doc/uid/TP40002415-CH2) in _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_ provides guidance on how to securely perform privilege separation.
- _[Daemons and Services Programming Guide](../../Mac%20OSX/Daemons%20and%20Services%20Programming%20Guide/About%20Daemons%20and%20Services.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3te2i)_ describes XPC services, which is the preferred way of launching and communicating with helper apps in a sandboxed environment. (macOS only)

__Miscellaneous__

- [Apple's Open Source website](http://www.opensource.apple.com/) provides Apple’s open source security code. You can examine it to see which security protocols and algorithms are supported by Apple’s macOS and iOS security implementation and to find additional documentation.
- The Security topic areas in the macOS Developer Library and the iOS Developer Library contain a number of security-specific release notes.

There are a number of excellent books on computer security that you should consider reading. Here are just a few of them, grouped into subject areas.

- __Cocoa Security__

  - Lee, Graham J. _Professional Cocoa Application Security_, Wrox Professional Guides, 2010.
- __Threat Modeling__

  - Howard, Michael, and David LeBlanc. _Writing Secure Code_ (second edition), Microsoft Press, 2003.
  - Anderson, Ross. _Security Engineering: A Guide to Building Dependable Distributed Systems_, 2d ed. John Wiley & Sons, 2001.
- __Fuzz Testing__

  - Sutton, Michael, Adam Greene, and Pedram Amini. _Fuzzing: Brute Force Vulnerability Discovery_, Pearson Education, 2007.
- __Cryptography__

  - Schneier, Bruce. _Applied Cryptography_. 2d ed. John Wiley & Sons. 1996.
  - Brands, Stefan. _Rethinking PKI and Digital Certificates: Building in Privacy_. The MIT Press. 2000.
- __Secure Networking__

  - Gray, John Shapley. _Interprocess Communications in UNIX_. 2d ed. Prentice Hall Professional. 1997.
  - Stevens, W. Richard. _UNIX Network Programming: Interprocess Communications_. Vol. 2, 2d ed. Prentice Hall Professional. 1998.
  - Stevens, W. Richard, Bill Fenner, and Andres M. Rudoff. _UNIX Network Programming: The Sockets Networking API_. Vol. 1. 3d ed. Addison Wesley Professional. 2004.
- __General__

  - Garfinkel, Simson, Gene Spafford, and Alan Schwartz. _Practical Unix & Internet Security_. 3d ed. O’Reilly. 2003.
  - Viega, John, and Gary McGraw. _Building Secure Software_. Addison-Wesley Professional. 2002.
  - McKusick, Marshall Kirk, Keith Bostic, Michael Karels, and John Quarterman. _The Design and Implementation of the 4.4 BSD Operating System_. Addison-Wesley. 1996.

The following pages describe some of the standards, protocols, and algorithms used by Apple. Although many of these pages are fairly old, the standards have not changed enough to invalidate their usefulness.

__Common Criteria__

- For more information about the Common Criteria, including links to download the complete official criteria, see the Common Criteria portal at [http://www.commoncriteriaportal.org/](http://www.commoncriteriaportal.org/) and the website of the Common Criteria Evaluation and Validation Scheme (CCEVS) ([http://www.niap-ccevs.org/cc-scheme/](http://www.niap-ccevs.org/cc-scheme/)).

__Kerberos__

- For information on Kerberos authentication, see the [MIT Kerberos website](http://web.mit.edu/kerberos/).
- See [macOS server help](https://help.apple.com/serverapp/mac) for details on the services that support Kerberos and on how to implement a Kerberos KDC on your macOS server.

__Other Secure Networking Protocols__

- The authentication model for HTTP is described in [RFC 2617](http://www.ietf.org/rfc/rfc2617.txt), _HTTP Authentication: Basic and Digest Access Authentication_.
- For information on the SSL protocol for secure networking, see the [IETF SSL Version 3.0 Draft Specification](http://tools.ietf.org/html/draft-ietf-tls-ssl-version3-00). For the TLS protocol, see the [TLS Working Group website](https://datatracker.ietf.org/wg/tls/charter) and [RFC 5246](http://tools.ietf.org/html/rfc5246).
- Documentation of the AES encryption algorithm used for FileVault is available on the [National Institute of Standards and Technology (NIST) website](http://csrc.nist.gov/archive/aes/rijndael/wsdindex.html).

[Next](Document%20Revision%20History.md)[Previous](End-User%20Security%20Features.md)

