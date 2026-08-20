---
title: iAd Creative Management Manual
apple_id: TP40012029
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: null
technology: null
published: '2012-09-26'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/iAdCreativeManagementManual/Overview/Overview.html
archived_at: '2026-07-15T08:17:00.774841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iAd Creative Management Manual](Introduction%20to%20iAd%20Creative%20Management.md)


[Next](Reviewing%20Ad%20Bundle%20History%20and%20Analytics.md)[Previous](Introduction%20to%20iAd%20Creative%20Management.md)

# Overview

The following provides an overview of the setup of the portal.

__Figure 2-1__  Creative Management Portal

!

| Field | Description |
| --- | --- |
| Favorites | Users can bookmark ad bundles and projects as favorites so that they might appear under the appropriate Favorites section. Doing so would allow users to return to projects or ad bundles they are working on. |
| Recently Viewed | Items which users have recently seen will appear here. This includes projects and ad bundles. |
| New Ad Bundle or Project | When a user wants to create a new project or ad bundle, they can click on the “+” sign, which is a familiar Apple heuristic. |
| Resizing Handle | The resizing handle allows the user to drag the handle to another location so that the sidebar can be expanded or contracted. |
| Link to OMT Portal | For internal iAd Admin users who have access to the OMT (Org Management Tool), a link will be provided so that users can launch the portal.  Account Managers already have access to the portal and will see a link to the portal. |
| Global Search | Global Search allows users to search for ad bundles and projects belonging to non-iAd Creative Agencies. The most common use case is to support third parties in creating projects or ad bundles. Users can search by the following fields:   - Search by project - Search by advertiser - Search by Creative Agency - Search by Ad Bundle   Once the user performs the search, a tab will appear called “Global Search” which displays all the ad bundles which match the criteria across all organizations. |
| Help link | Link which launches the frequently asked questions. |
| User ID | Name of the logged in user. |
| Sign out | Allows the current user to log out and another user/Apple ID to log in. |
| Tabs | Major functionality grouped as tabs. |

When you log into the portal for the first time, you’ll be prompted to accept the Terms & Conditions.

__Figure 2-2__  iAd Terms and Conditions

!

Once you’re accepted the terms and conditions, you will be taken to the Ad Bundle Summary.

The Ad Bundle Summary is a listing of ad bundles which belong to a specific organization.

__Figure 2-3__  Ad Bundle Summary

!

| Field | Description |
| --- | --- |
| Filter | Allows a user to filter the listing of ad bundles by any of the following dimensions:   - Filter by ad bundle - Filter by project - Filter by advertiser - Filter by creative agency - Filter by status - Filter by updated by |
| Create Ad Bundle button | Clicking on this button will create a new ad bundle. |
| Ad Bundle Summary table | Table of ad bundles. The following fields are displayed:   - Ad Bundle Name — the names of the ad bundles in the table are hyperlinked to the ad bundle details - Project Name — the names of the projects in the table are hyperlinked to the project details - advertiser - status - updated by - last updated - last live version —latest version of the ad bundle which was published   Note that clicking on any of the columns in the table will sort in ascending/descending order by that column. The default sort is by last updated in descending order. |
| Pagination | Pagination markers provide users the ability to navigate to other pages and change the number of visible rows per page. |

The Project Summary is a listing of the projects which a specific organization has access to.

__Figure 2-4__  Project Summary

!

| Field | Description |
| --- | --- |
| Filter | Allows a user to filter the listing of ad bundles by any of the following dimensions:   - Filter by project - Filter by advertiser - Filter by updated by |
| Create Project button | Clicking on this button will create a new project. |
| Ad Bundle Summary table | Table of ad bundles. The following fields are displayed:   - Project Name — the names of the projects in the table are hyperlinked to the project details - advertiser name - updated by - last updated   Note that clicking on any of the columns in the table will sort in ascending/descending order by that column. The default sort is by last updated in descending order. |
| Pagination | Pagination markers provide users the ability to navigate to other pages and change the number of visible rows per page. |

To create a project, simply click on the “+” icon at the lower left corner or the “Create Project” button.

__Figure 2-5__  Create a Project

!!

| Field | Description |
| --- | --- |
| Project | Name of the project. |
| Creative Agency | The Creative Agency who created the project.   - The creative agency will default to the current user’s organization. - Internal iAd users can modify the Creative Agency. This functionality might be useful if a Creative Agency asks an Account Manager or PS resource to assist in creating a project. |
| Description | (Optional) Description of the project |
| Advertiser | Indicates the Advertiser associated with the project. |
| Action Buttons | Allows the user to Cancel or Save the project. |

Here’s an example of a saved Project:

__Figure 2-6__  Saved Project

!

To upload an ad bundle, simply click on the “+” icon at the lower left corner or the “Create Ad Bundle” button.

__Figure 2-7__  Create new ad bundle

!

| Field | Description |
| --- | --- |
| Ad Bundle Name | Name of the ad bundle.  Note that the name of the ad bundle determines the uniqueness of the ad. |
| Creative Agency | The Creative Agency who created the project.   - The creative agency will default to the current user’s organization. - If creating an ad bundle on behalf of another organization, the iAd team can change the Creative Agency. However, if the iAd PS team is serving as Creative Agency--that is, it is developing the ad--the Creative Agency should remain iAd (i.e. Quattro Wireless). |
| Project | Project that the ad bundle resides in.   - Assignment to a project is only required when submitting the ad bundle for certification. - As noted above, the project the ad bundle is assigned to must be associated with an Advertiser which has an Advertiser SAP ID. Otherwise, the ad bundle cannot be submitted for certification. - This is a preventative measure to stop Creative Agencies from submitting multiple ad bundles for certification. |
| Type of Ad Bundle | The types of ad bundles include:   - iAd for brand - iAd for developers (not available until Q4 2012) |
| Version Notes | (Optional) Description of the Ad Bundle. |
| Ad Bundle Zip File | Compressed (ZIP) version of the ad bundle. |
| Ad Bundle Password | (Optional) Allows user to set a password which will be required when any user attempts to:   - Download the ad bundle - Run the ad using iAd Tester   If a password is set, and the user tries to access the ad via one of the two options listed above, the user will have to enter a “Name” and “Password”, as follows:   - Name: The Name to use is on the Ad Bundle Details page. Please copy and paste the name from the Name for Download field. - The Password to use is the password created when the ad bundle was uploaded into the iAd Creative Management portal or assigned in iAd Producer. |
| Action Buttons | Allows the user to Cancel or Save the ad bundle. |

Users can select a project by clicking on the “Assign” button next to the Project field. Doing so will bring up the following pop-up window.

__Figure 2-8__  Select a project

!!

| Field | Description |
| --- | --- |
| Project Filter | Allows the user to filter the listing of projects by entering some text into the filter. |
| Project Name | Name of the project to assign the ad bundle to.  Note that a user can assign bundles to the “SANDBOX” project which will only be visible to that user (based on his/her Apple ID). |
| Advertiser Name | Name of the advertiser associated with the project. Possible values include:   - Advertiser name — this is the name of the actual advertiser - Un-Assigned — when an advertiser has not yet been assigned to a project. - Not Applicable — used with sandbox. |
| Project Description | The description of the project. |
| Pagination Markers | Pagination markers provide users the ability to navigate to other pages and change the number of visible rows per page. |
| Action Buttons | Allows the user to Cancel selection or Select the project to assign the ad bundles to. |

Select the Ad Bundle Zip file you would like to upload.

__Figure 2-9__  Selecting a zip file

!!

Once an ad bundle has been selected and the “Choose” button pressed, a popup will appear displaying a progress bar, followed by a processing spinner.

__Figure 2-10__  Upload progress

!!

| Field | Description |
| --- | --- |
| Upload Progress Bar | Displays the progress of the upload process. |
| Processing Spinner | Upon completion of the upload process, the iAd Creative Management portal will review the ad bundle to determine if there are any errors. Note that the review process may take some time and there is no progress indicator to indicate time remaining.  There are 2 classes of errors that are possible:   - Errors which prevent the Zip file from being uploaded – this class of errors indicates any errors it has found in the structure of the ad bundle that prevents it from being accepted. These errors must be corrected and the correct ad bundle uploaded again before proceeding. - Errors which do not prevent the Zip file from being uploaded. The portal will provide warnings to indicate any potential issues it has found which does not prevent it from being uploaded. These warnings should be corrected before the ad bundle is submitted for certification. |
| Cancel Button | The user can cancel the upload process by clicking on the Cancel button. If the upload has not reached 100% completion, the upload will be canceled. If upload has reach 100% completion and review process has started, canceling will cancel the processing but the ad bundle will still appear in the portal.  Note that canceling while the portal is processing the ad bundle may result in missed warnings which could prevent the ad bundle from being certified. |

An example of a potential warning is as follows:

__Figure 2-11__  Potential warning

!

Upon successfully uploading the compressed ad bundle file, the status of the ad bundle will change to Draft status. A tooltip will also appear next to the status to provide information on the significance of the status.

__Figure 2-12__  Successful upload

!!

￼Additional new information is provided at the bottom of the page:

__Figure 2-13__  Additional information

!!

| Field | Description |
| --- | --- |
| Ad Bundle Password | Indicates whether there was a password associated with the ad bundle. |
| Plist Info | Displays the information in the plist, or property list, which provides detail on the properties of the banner and the ad unit.  Note that the information in the plist cannot be modified in the iAd Creative Management portal. That information must be changed outside the portal in the ad bundle which must then be re-uploaded into the portal. |
| Date/time Stamp of Last Update | The data and time stamp of the updated status, and the individual who updated the ad bundle.  There are 2 classes of errors that are possible: |
| Banner OTA Test URLs (Copper URLs) | (Also known as “Copper URLs”) The remote URLs used by the iAd Tester test tool to view the banner and ad unit over-the-air (OTA). |

The following are menu items associated with the newly created ad bundle.

__Figure 2-14__  Menu items

!!

| Field | Description |
| --- | --- |
| Edit | Permits editing of ad bundles. The only items which can be edited are:   - Ad Bundle Name - Project the ad bundle is assigned to   Note that once the ad bundle has been submitted, the ad bundle can no longer be edited. |
| Upload New Ad Bundle | Allows a new ad bundle to be uploaded. Every upload represents a new version of the ad bundle. During this process, only version notes, the new ad bundle, and an optional password can be changed. |
| Download Ad Bundle | Allows the user to download the ad bundle. |
| Delete Ad Bundle | Allows the user to delete the ad bundle. Only ad bundles in Draft and Needs Revision statuses can be deleted. Deletion of ad bundles are irreversible. |
| Move Ad Bundle | Permits moving of ad bundles from the Sandbox to a project. Note that an ad bundle cannot be moved from a project to another project. Also note that moving of an ad bundle is irreversible. |
| Send Creative URL | Sends the banner OTA test URLs to the email associated with the logged in user’s Apple ID. |
| Change Status | Allows the user to change the status.  The user can only change the status of an ad bundle in Draft and Needs Revision modes. |
| Add to Favorites | Indicating the ad bundle as a Favorite will make it appear in the list of Favorite Ad Bundles in the left-hand nav. |

[Next](Reviewing%20Ad%20Bundle%20History%20and%20Analytics.md)[Previous](Introduction%20to%20iAd%20Creative%20Management.md)

