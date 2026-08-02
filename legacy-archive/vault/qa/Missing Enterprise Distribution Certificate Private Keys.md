---
title: Missing Enterprise Distribution Certificate Private Keys
apple_id: DTS40014760
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: Security
published: '2014-07-29'
source_url: https://developer.apple.com/library/archive/qa/qa1868/_index.html
archived_at: '2026-07-18T02:35:09.499213Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1868

# Missing Enterprise Distribution Certificate Private Keys

## Q:  How do I recover a lost enterprise distribution certificate or its private keys?

A: There are a few points to consider with regard to missing Enterprise Distribution Certificates Private Keys. Code signing new enterprise apps or enterprise app updates for distribution will not work until both are restored. The particular circumstances of your situation will determine the appropriate resolution path among those numbered below.

Following are the options available to restore a working distribution code signing configuration:

1. Transfer the certificate from the OS X user account in which the certificate was originally created. This can be done using the steps in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/Introduction/Introduction.html)__> Maintaining Your Signing Identities and Certificates > Exporting and Importing Certificates and Profiles__. Doing this reenables distribution code signing without disturbing any currently deployed enterprise apps.

2. If you are unable to locate the certificate for transferring, you will need to create a new one. Following is a discussion along with two options for creating new enterprise distribution certificates.

2A. If Member Center allows you to create the second of two certificates then you should to do that. This can be done using the plus “+” button in the upper-right on [Member Center](https://developer.apple.com/membercenter/index.action) __> Certificates, Identifiers, & Profiles > (your program) > Certificates > Production__. After doing this, create a new enterprise distribution profile associated to the newly created certificate, and then sign and distribute a new version of the app. Doing this reenables distribution code signing without disturbing any currently deployed enterprise apps.

2B. If Member Center does not allow you to create another distribution certificate then the distribution certificate whose private keys are missing must be revoked and re-created. To do this, follow the steps in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/Introduction/Introduction.html) __> Maintaining Your Signing Identities and Certificates > Re-Creating Certificates and Updating Related Provisioning Profiles__. Doing this will invalidate all currently deployed apps and therefore requires you to re-sign, and re-distribute all currently deployed apps once the new working distribution code signing configuration is created.

Finally, after a working distribution code signing configuration has been restored, you should create a backup to more easily recover from this situation in the future. You can back up the newly created identity using the process in [App Distribution Guide](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/Introduction/Introduction.html) __> Maintaining Your Signing Identities and Certificates > Exporting and Importing Certificates and Profiles__.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-07-29 | New document that covers all options and consequences to a company's missing enterprise certificate or private keys. |

