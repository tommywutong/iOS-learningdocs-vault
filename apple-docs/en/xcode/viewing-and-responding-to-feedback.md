---
title: Viewing and responding to feedback from beta testers
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/viewing-and-responding-to-feedback
source_url: 'https://developer.apple.com/documentation/xcode/viewing-and-responding-to-feedback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/viewing-and-responding-to-feedback.json'
content_hash: 'sha256:0fc36efb1b996a40'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Distribution](distribution.md)

# Viewing and responding to feedback from beta testers

<sub>Article</sub>

Follow up on feedback from beta testers using the Feedback organizer.

## Overview

When you distribute a beta version of your app through the TestFlight app, testers can provide you with screenshots and feedback about their experiences. This feedback can give you an important perspective on how your app functions in real-world-scenarios, and help you iterate on features, improve your UI, and address issues.

You can view people’s feedback in Xcode‘s Feedback organizer and on your app’s TestFlight page in [App Store Connect](https://developer.apple.com/app-store-connect/). The Feedback organizer provides the ability to respond to the tester, share the feedback among your development team, take notes as you work on issues, and mark items as you resolve them.

For more information about distributing a beta version of your app, see [Distributing your app for beta testing and releases](distributing-your-app-for-beta-testing-and-releases.md).

> [!note] Note
> Feedback from testers for iOS 12 and earlier, tvOS, and watchOS doesn’t appear in the Feedback organizer. That feedback goes to the email address you provide in the Feedback Email field of your app’s Test Information page in App Store Connect.

### View feedback from testers

To view feedback from your app’s testers:

1. In Xcode, choose Window \> Organizer from the menu bar.
2. Select Feedback from the Reports section of the sidebar.
3. Select your app from the pop-up button at the top of the sidebar.

Xcode shows the list of available apps organized by platform. The feedback for the selected app appears in a grid. To focus on specific reports, use the filter bar at the top of the window to filter by kind, app version and build, type, and run destination.

The items in the grid show previews of feedback, including screenshots when available, and a summary of the feedback text. An inspector to the right of the grid shows the details for the selected report.

![](../../../attachments/d7cb0ec11b756c21e666d519998a9c2d/viewing-and-responding-to-feedback-1@2x.png)

<sub>A screenshot of the Feedback organizer with the Feedback option selected in the Reports section of the sidebar. The app selection pop-up button appears at the top of the sidebar. The center of the organizer displays a grid of feedback previews with one selected and a filter bar at the top for filtering reports. The inspector to the right of the organizer displays details about the selected feedback.</sub>

Double-click a preview to display the report’s complete text and larger versions of any attached screenshots.

### Follow up and track progress

To follow up with a tester who provides feedback, click the email button at the top of the inspector.

> [!note] Note
> If you send a tester an invitation email, their email address displays in the inspector. If you invite a tester with a public link, they display as anonymous unless they enter their email address when submitting feedback. The email address only displays for that particular piece of feedback.

To share a link to a report with another member of your development team, select the item you want to share from the grid and click the Share button at the trailing edge of the window‘s toobar. If the team member has the necessary authorization, they can click the shared link to open the Feedback organizer in Xcode with the preview of the report.

To rename reports to help keep them organized and to add notes, use the controls at the bottom of the inspector. Use the Mark as Resolved button in the inspector, or the checkbox next to each preview, to keep track of issues as you resolve them.

![](../../../attachments/79bf99da60cc6d50edcd0af7d156dd34/viewing-and-responding-to-feedback-2@2x.png)

<sub>A screenshot of the Feedback organizer with the Feedback option selected in the Reports section of the sidebar. The center of the organizer displays the text of the feedback with one large screenshot below it. Below the large screenshot is a series of screenshot thumbnails. At the top of the inspector to the right is a button for emailing the tester. At the bottom of the inspector are controls for renaming, adding notes, and marking the feedback as resolved.</sub>
