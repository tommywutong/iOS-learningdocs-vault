---
title: iAd Creative Management Manual
apple_id: TP40012029
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: null
technology: null
published: '2012-09-26'
source_url: https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/iAdCreativeManagementManual/ReviewingAdBundleHistoryandAnalytics/ReviewingAdBundleHistoryandAnalytics.html
archived_at: '2026-07-15T08:17:08.094660Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [iAd Creative Management Manual](Introduction%20to%20iAd%20Creative%20Management.md)


[Next](Submitting%20an%20Ad%20Bundle.md)[Previous](Overview.md)

# Reviewing Ad Bundle History and Analytics

The iAd Creative Management portal has several features to help Creative Agencies analyze ad bundles and assess analytics associated with the ad bundle.

The History tab gives users a summary of the changes to the ad bundle throughout its certification lifecycle.

__Figure 3-1__  View history

!!

| Field | Description |
| --- | --- |
| View by Filter | Dropdown which allows the user to filter the events by the Current Version or all versions. This is useful auditing the events related to the most current version of the ad bundle. |
| Date/Time Stamp | Date/time that the event occurred. A link is provided to the appropriate version of the ad bundle to view more information. |
| Event Summary | Automated event title. |
| Event Notes | If the user entered any notes while changing the status of the ad bundle, the notes will appear in this field. |
| Submitted By | Indicates the Apple ID (or “Apple” if it belongs to a member of the Apple team) who made the change. |
| Pagination Marker | Pagination markers provide users the ability to navigate to other pages and change the number of visible rows per page. |

The default tab is sorted by descending Date. Clicking on any of the columns will sort the table by that column in ascending/descending order.

The iAd Creative Management portal has four sets of reports which can be used to ensure that the ad bundle is performing as expected.

This report displays all the transactions associated with the ad bundle and the specified UDID. Specifying a UDID focuses the results on the activity for that ad specific to that UDID and filters all other metrics associated with other ad bundles or UDIDs.

The steps to follow are:

- Navigate to the ad bundle of interest
- Select “Analytics” tab
- Select the “All Transactions” report from the dropdown
- Enter a UDID (use a UDID which has clicked on the ad unit)
- Select a day when the UDID visited the ad unit
- Click the “Analyze” button

__Figure 3-2__  Ad bundle analytics

!!

| Field | Description |
| --- | --- |
| View by Filter | Filter for selecting the type of analytics report. The options are:   - All Transactions - Top Page Views - Conversions - Event Validation |
| UDID | The UDID, or Universal Device ID, of the device which launched the ad unit. This is used to filter the list of events to a UDID. |
| Date Range | Filter to constrain the listing of events to a subset based on a date. Also specify one to two days from this date to include more days. |
| Analyze button | Launches the report based on the parameters above. |
| Export to CSV | Allows the report to be exported to CSV file. |
| Session Identifier | Identifies the session. A session is a combination of the UDID, the ad bundle, and the time/date. |
| Date/Time of Event | Date and time of the recorded event. |
| Event Sender | The event sender is the name given by the user (if specific to the ad bundle) or by the system (if not specific to the ad bundle). |
| Event Name | The event name is the sub-type of the event. |
| Event Type | A specific type specified by the event. |
| Arguments | If the event has arguments, the arguments are indicated in this field. |
| Pagination Marker | Pagination markers provide users the ability to navigate to other pages and change the number of visible rows per page. |

This report aggregates identical page views and reports on them for a specific ad bundle. This mimics the Views report in the iAd Advertising Portal.

To find the report:

- Navigate to the ad bundle of interest
- Select “Analytics” tab
- Select the “Top Page Views” report from the dropdown
- Enter a UDID (use a UDID which has clicked on the ad unit)
- Select a day when the UDID visited the ad unit
- Click the “Analyze” button

The following lists changes from the All Transactions report:

__Figure 3-3__  All transactions report

!!

| Field | Description |
| --- | --- |
| Section | The section associated with the view. |
| Event Sender | The Event Sender is the name of the view given by the user. |
| Event Name | Specific Event Names will appear in the table. The listing includes:   - ViewDidAppear - Screen Update - Transition - Perspective - Overlay |
| Count | The aggregate count of specific views which appear in the portal. |
| Arguments | If the event has arguments, the arguments are indicated in this field. |
| Pagination Marker | Pagination markers provide users the ability to navigate to other pages and change the number of visible rows per page. |

This report validates the events logged in the iAd Creative Management portal against the events noted in the Analytics Sheet for that same ad bundle.

Note that the Analytics Sheet expected in the portal follows the prescribed Excel format (for more information, contact your Account Management liaison for the Analytics Sheet template).

To find the report:

- Navigate to the ad bundle of interest
- Select “Analytics” tab
- Select the “Event Validation” report from the dropdown
- Enter a UDID (use a UDID which has clicked on the ad unit)
- Select a day when the UDID visited the ad unit
- Click the “Analyze” button

The following lists changes from the All Transactions report:

__Figure 3-4__  Event validation report

!!

| Field | Description |
| --- | --- |
| Select Analytics File | Allows the user to indicate the Analytics file to be used to test against the events logged by the iAd Creative Management system. |
| Matched Events | A count of the number of events which matched between the Analytics Sheet and the logged events. |
| UnMatched Events | A count of the number of events which did not match between the Analytics Sheet and the logged events. |
| Section | Section associated with the event. |
| Event Sender | Name of the view given by the user. |
| Event Name | Specific Event Names will appear in the table. |
| Event Type | The type of event logged. |
| Arguments | If the event has arguments, the arguments are indicated in this field. |
| Status | The reason for the mismatched events. Possible options include:   - Detected, not in file — the logged event was detected but was not found in the Analytics file. - Not detected — the event was in the Analytics File but was not detected in the logged file. |
| Pagination Marker | Pagination markers provide users the ability to navigate to other pages and change the number of visible rows per page. |

[Next](Submitting%20an%20Ad%20Bundle.md)[Previous](Overview.md)

