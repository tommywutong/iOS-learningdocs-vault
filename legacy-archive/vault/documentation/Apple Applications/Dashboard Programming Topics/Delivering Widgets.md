---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/Delivery.html
archived_at: '2026-07-15T05:17:20.915663Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Document%20Revision%20History.md)[Previous](Calling%20Objective-C%20Methods.md)

# Delivering Widgets

After you've created your widget, you need to distribute it to your customers. This chapter outlines steps that you should take to ensure that your customers have a pleasant experience downloading and installing your widget.

Widgets are much less complex than applications and should provide a light-weight install experience. The preferred packaging experience is to have widgets delivered in zip archive format and placed on your web server for download. Only archive the `.wdgt` bundle, omitting all other files. Link to the widget archive from your website to enable the download.

When downloaded using Safari, the zipped widget is automatically unarchived and the user is presented with an install dialog, asking them if they want the widget to be installed. When downloaded using other web browsers, users need to manually open the widget to show the widget installer.

Here are some tips for you to keep in mind when readying your widget for delivery:

- Follow these steps to create a zip archive:

  - Select the widget in the Finder
  - Choose File > Create Archive
  - Upload resulting archived widget to your web server
- Avoid multi-step installations, registration, and purchasing after the widget is downloaded. If registration, purchase, and the display of an End User License Agreement is required, perform these functions locally on your website prior to download. If it's necessary to communicate with your widget after download, use cookies.
- Include the instructions below on your widget download page for users to follow:

  _OS X v.10.4 Tiger is required. If you're using Safari, click the download link. When the widget download is complete, the widget installer appears. Click Install if you want the widget installed on your Mac. If you're using a browser other than Safari, click the download link. When the widget download is complete, unarchive and open it to show the widget installer._

[Next](Document%20Revision%20History.md)[Previous](Calling%20Objective-C%20Methods.md)

