---
title: Making Certificates and Keys Available To Your App
apple_id: DTS40011636
resource_type: QA
platform: iOS
topic: Security
technology: Security
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/qa/qa1745/_index.html
archived_at: '2026-07-18T02:34:32.635131Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1745

# Making Certificates and Keys Available To Your App

## Q:  I've installed a certificate and private key onto my iOS device by downloading it using Safari. But when I run my app, it can't find the identity I just installed. Why is that?

A: Users can install digital identities (certificates plus their associated private keys) onto their iOS devices by downloading them from within Safari, by opening them as email attachments, and by installing them with configuration profiles. Or, identities can be pushed from a Mobile Device Management (MDM) server. However, identities installed in any of these ways are added to the Apple keychain access group.

Apps can only access keychain items in their own keychain access groups. This means that items in the Apple access group are only available to Apple-provided apps such as Safari or Mail.

To use digital identities in your own apps, you will need to write code to import them. This typically means reading in a PKCS#12-formatted blob and then importing the contents of the blob into the app's keychain using the function `SecPKCS12Import` documented in [Certificate, Key, and Trust Services Reference](https://developer.apple.com/documentation/security/1396915-secpkcs12import).

This way, your new keychain items are created with your app's keychain access group.

The reference contains a link to the _[AdvancedURLConnections](../samplecode/AdvancedURLConnections/AdvancedURLConnections.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydsnjvha)_ sample which shows how to establish secure network connections in an iOS application.

One way to provision an identity is via email. When you provision a device, send the associated user an email with their client identity attached as a PKCS#12 file. Except don't give it the standard PKCS#12 MIME type or extension, give it a MIME type and extension claimed by your app. (The extension ".p12" is claimed by iOS and cannot be claimed by another app.) The user can then open the attachment, which will launch your app, at which point you can offer to import the identity. This same technique will work if you host the identity as a web download.

You can learn more about claiming file extensions in _[Document Interaction Programming Topics for iOS](../documentation/File%20Management/Document%20Interaction%20Programming%20Topics%20for%20iOS/About%20Document%20Interaction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydimbt)_.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-09-17 | Remove reference to obsolete iPhone Configuration Utility. |
| 2012-01-20 | New document that explains what developers need to do if they want to use certificates and identities from an outside source in their app. |

