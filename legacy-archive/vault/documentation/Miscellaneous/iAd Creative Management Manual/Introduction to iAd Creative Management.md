---
title: iAd Creative Management Manual
apple_id: TP40012029
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: null
technology: null
published: '2012-09-26'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/iAdCreativeManagementManual/Introduction/Introduction.html
archived_at: '2026-07-15T08:16:59.195800Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Overview.md)

# Introduction to iAd Creative Management

The document provides an overview of the iAd Creative Management portal, a web application which will be made available to third party Creative Agencies to manage ad bundles through its lifecycle (upload, analysis, certification, and production).

The iAd Creative Management portal and this manual refer to several terms which are defined below:

- Advertiser — an advertiser vis-a-vis the iAd Creative Management portal is the organization which will be billed for the campaign. Note that this is often the media agency, although this may also be the brand if the brand is directly paying for the campaign.
- Ad Bundle — an ad bundle refers to the ad and consists of the banner and the ad unit. A banner is the creative asset which appears when the ad is served on the iOS device. The ad unit is the unit which appears when the user taps on the banner.
- Project — a project is a container of ad bundles. A project can be created for each campaign or a set of campaigns for an advertiser. Each project must be associated with a single advertiser, as defined above.

  As such, the best practice for the use of a project is that one project should be created for each Advertiser brand.

  Note that more than one project can be created for a single Advertiser, but only one Advertiser can be assigned to a single project.

__Figure 1-1__  The relationship between an advertiser, a project, and ad bundles

!

Access to the iAd Creative Management portal is provided via OMT, the Organization Management Tool. If a user has access to OMT, he/she will be provided a link on the masthead to the OMT tool, as noted in the image below:

__Figure 1-2__  Organizer Management Tool

!

As with other tools which use OMT, permissions are set up in Groups with Apple IDs assigned to specific groups. The following table lists the Groups which should exist both with the iAd organization as well as at third party creative agencies.

__Figure 1-3__  Group permissions

!

For third-party creative agencies who have individuals who need access to the iAd Creative Management portal, the permissions are divided into two primary personas:

- Project Managers — these individuals can create, edit, and delete projects within their organization.
- Developers — these individuals need the ability to create, edit, and delete ad bundles.

iAd internal users will have additional permissions, depending on the persona:

- iAd Admin — superuser who has rights to do everything within the iAd Creative Management portal.
- iAd Project Manager — individual which are part of the PS organization who, like Admin, have rights to everything except modifying the statuses.
- iAd Developer — similar to developers at third parties except they have the ability to perform global searches.
- iAd Certification team — similar permissions to an iAd PM but with the ability to approve/reject the ad bundle.
- iAd NOC — has ability to change the ad bundle status to Published.
- iAd AM — has rudimentary abilities to support the Creative Agency. Has the ability to assign Advertisers to projects.

[Next](Overview.md)

