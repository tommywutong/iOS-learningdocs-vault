---
title: When should I use a wildcard App ID?
apple_id: DTS40010248
resource_type: QA
platform: iOS
topic: Languages & Utilities
technology: null
published: '2016-08-23'
source_url: https://developer.apple.com/library/archive/qa/qa1713/_index.html
archived_at: '2026-07-18T02:34:22.346015Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1713

# When should I use a wildcard App ID?

## Q:  When should I use a wildcard App ID vs. an explicit App ID?

A: You should use a Wildcard App ID for all apps and app targets that do not enable app-specific capabilities. However, because Xcode 8 offers to manage signing automatically, it prevents the need to create App IDs manually. Therefore, the explanations in this document are only useful to developers who find a need to opt out of Xcode's automatic signing.

__Figure 1__  App targets opting into Xcode's automatic signing do not need to create and configure App IDs manually.

!

If you do find a need to manually create an App ID, read on to learn about the difference between the two types. The first type is called a Wildcard App ID.

__Figure 2__  Creating a Wildcard App ID on the Certificates, Identifiers and Profiles website.

!

The wildcard portion of the string entered for Bundle ID is the __asterisk__ character. All Wildcard App IDs must end with an asterisk, and an associated provisioning profile can be used to code sign any app whose Bundle ID is compatible with the wildcard string, such as:

- com.myGreatCompany.app1
- com.myGreatCompany.app2
- com.myGreatCompany.anything
- ... and so on.

The second type of App ID is called an Explicit App ID.

__Figure 3__  Creating an Explicit App ID on the Certificates, Identifiers and Profiles website.

!

The Bundle ID specified for an Explicit App ID cannot contain a wildcard asterisk character, and its associated provisioning profile can be used to code sign one app only - the app that declares this bundle Identifier as its own.

__How do I choose one or the other?__

Because an App ID specifies a unique configuration of entitlements, Wildcard App IDs are for use with code signing all apps that do not enable app-specific capabilities. Those capabilities are pictured as follows:

__Figure 4__  Xcode 8's target capabilities pane.

!!

Even when using a Wildcard App ID, remember to remove the asterisk and fully-qualify the string when entering the Bundle Identifier field in your Xcode project:

__Figure 5__  Defining the target Bundle ID in Xcode.

!

Using a Wildcard App ID is convenient for all apps that do not use capabilities, as they can reuse the same provisioning profile for code signing. For example, if App1's targets do not enable capabilities, they may reuse the provisioning profile associated to the Wildcard App ID in __Figure 2__ to code sign all targets.

In this example, App1 has four targets whose Bundle IDs are:

- com.myGreatCompany.app1-watch
- com.myGreatCompany.app1-macOS
- com.myGreatCompany.app1-tvOS
- com.myGreatCompany.app1-iOS

Since Explicit App IDs are for use with a single Bundle ID, it can be used to code sign only one app or app target.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-08-23 | Major rewrite. |
| 2010-08-20 | New document that describes the differences between wildcard and explicit App IDs |

