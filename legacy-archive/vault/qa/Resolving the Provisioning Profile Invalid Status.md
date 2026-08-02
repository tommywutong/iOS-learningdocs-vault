---
title: Resolving the Provisioning Profile Invalid Status
apple_id: DTS40014931
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: Security
published: '2014-08-28'
source_url: https://developer.apple.com/library/archive/qa/qa1878/_index.html
archived_at: '2026-07-18T02:35:11.930324Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1878

# Resolving the Provisioning Profile Invalid Status

## Q:  What causes the provisioning profile "Invalid" status? How do I resolve it, and how do I prevent it?

A: The provisioning profile invalid status is caused by changes to the profile’s associated certificate or App ID. Any time an App ID or certificate changes, all profiles that are associated to it are marked Invalid. This does not apply to Xcode's team profiles, but applies to all profiles that Xcode does not manage, specifically, custom development profiles and distribution profiles. This document explains the causes in detail and provides steps to resolve and avoid the profile invalid status.

If a profile’s associated code signing certificate expires or becomes revoked, the profile must be edited and associated to a new certificate to move the status back to active. At that point the profile can again be used for code signing.

When an App ID changes (for example, a target capability was turned on or off in Xcode), the profiles associated to the App ID must be updated in order to reflect the proper entitlements that correspond to the newly enabled or disabled capability.

Xcode's team profiles are updated automatically to reflect those changes, however, all custom profiles that are tied to the App ID must be regenerated manually. To do that, you must edit the profile on the Certificates, Identifiers & Profiles website, and click the Generate button. Custom profiles include any development or distribution profiles your team has created manually through Certificates, Identifiers & Profiles.

A provisioning profile attaining Invalid status due to App ID changes does not affect any currently deployed apps that were signed with that profile. It's just an indication that the profile must be regenerated/updated to reflect changes in services and entitlements made to its associated App ID before it can again be used for code signing.

For standard developer program teams (those whose distribution method is the iOS App Store), expiration or revocation of a code signing certificate does not affect any apps that were signed with that certificate (this includes development builds, beta test builds, and live App Store apps). Its just an indication that the profile must be regenerated/updated to be associated with a new, valid certificate.

Since Xcode started managing services on App IDs (through the Xcode > Target > Capabilities tab), Invalidating provisioning profiles became as easy as enabling or disabling a target capability. Remember that every time the App ID changes with respect to its enabled services, all profiles attached to that ID become invalid.

Once all profiles are moved from Invalid to Active status in Member Center by way of the above steps, [Refresh Profiles in Xcode](https://developer.apple.com/library/ios/documentation/IDEs/Conceptual/AppDistributionGuide/MaintainingProfiles/MaintainingProfiles.html#//apple_ref/doc/uid/TP40012582-CH30-SW26) to sync Xcode with those changes before attempting to code sign apps with those profiles.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-08-28 | New document that explains causes, resolution and prevention of the provisioning profile "Invalid" status. |

