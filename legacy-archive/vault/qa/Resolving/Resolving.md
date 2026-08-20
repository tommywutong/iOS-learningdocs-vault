---
title: Resolving
apple_id: DTS40008077
resource_type: QA
platform: iOS
topic: Xcode
technology: null
published: '2009-05-26'
source_url: https://developer.apple.com/library/archive/qa/qa1618/_index.html
archived_at: '2026-07-18T02:32:47.069376Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1618

# Resolving

## Q:  Why do I get a "CodeSign: no certificate found in keychain for code signing identity" error?

A: The "CodeSign: no certificate found in keychain for code signing identity" error generally means one of several things:

1. Your Keychain is missing the private key associated with your iPhone Developer or iPhone Distribution certificate.
2. Your Keychain is missing the Apple Worldwide Developer Relations Intermediate Certificate.
3. Your certificate was revoked or has expired.
4. Online Certificate Status Protocol (OCSP) or Certificate Revocation List (CRL) are turned on in Keychain Access preferences.

The first two situations might happen if you deleted your keychain or certificate, reinstalled your system, or moved to a new computer. Here's how to troubleshoot this error.

Launch Keychain Access (/Applications/Utilities/Keychain Access), select "My Certificates" on the left side under Category, and search for your "iPhone Developer" (or "iPhone Distribution") certificate. If you don't have such a certificate, or if there is not a grey disclosure triangle next to the certificate (see Figure Figure 1), you will need to either import your certificate and private key from another working system or retrieve them from your backup (these would have been exported as a .p12 file). Double-click the .p12 file to add the certificate and private key to your Keychain.

__Figure 1__  A certificate and its assoicated private key in Keychain Access.

!

If you don't have a copy of your certificate and private key, you will need to revoke the certificate on the iPhone Portal, delete the certificate from your keychain, and generate a new certificate. To revoke your certificate, go to the [iPhone Portal](https://developer.apple.com/iphone), find the certificate you want to revoke, and select the "Revoke" button. Then follow the "Obtaining your iPhone Development Certificate" or "Obtaining your iPhone Distribution Certificate" section in the iPhone Developer Program Portal User Guide to generate a new certificate.

If your certificate has an associated private key, click on the certificate to select it. A valid certificate will show a green checkmark and "This certificate is valid" in the top pane of the window (see Figure 2).

__Figure 2__  A valid certificate.

!

If your certificate is not valid, it will have a red "x" and state the reason why. Generally the reason is "This certificate has expired" or "This certificate was signed by an unknown authority" (see Figure 3).

__Figure 3__  An invalid certificate.

!

If your certificate has expired, renew it at the iPhone Portal, download it, and double-click it to add it to your Keychain. If it's "signed by an unknown authority", download the "Apple Worldwide Developer Relations" certificate from the Certificates section of the [iPhone Portal](https://developer.apple.com/iphone) and double-click it to add it to your Keychain.

If your certificate was revoked, delete the certificate from your Keychain, then follow the "Obtaining your iPhone Development Certificate" or "Obtaining your iPhone Distribution Certificate" section in the iPhone Developer Program Portal User Guide to generate a new certificate.

Make sure you create a backup of your private key. The steps for doing this are described in the iPhone Developer Program Portal User Guide, under "Saving your Private Key and Transferring to other Systems".

If you have the iPhone Developer (or iPhone Distribution) certificate and its associated private key, the Apple WWDR Intermediate certificate is installed, and your certificate is valid, confirm that Online Certificate Status Protocol (OCSP) and Certificate Revocation List (CRL) are set to "Off" in Keychain Access > Preferences > Certificates.

If after following this Q&A you continue to get this error, or you need additional assistance, please contact [Developer Technical Support](https://developer.apple.com/support/iphone/techsupport/#submittsi). Include screenshots of each section of your Keychain Access window from the above troubleshooting steps, and as much additional information about your project and setup as possible.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2009-05-26 | Minor editorial changes. |
| 2008-11-12 | New document that describes why you might get a "no certificate found" error and how to resolve it. |

