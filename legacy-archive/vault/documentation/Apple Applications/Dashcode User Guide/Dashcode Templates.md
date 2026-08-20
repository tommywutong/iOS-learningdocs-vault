---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/Templates/Templates.html
archived_at: '2026-07-15T05:17:47.038808Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Dashcode%20Parts.md)[Previous](Advanced%20Topics%20for%20Widgets.md)

# Dashcode Templates

Apple provides a number of templates with Dashcode. Read this appendix to learn more about the features of each of the Dashcode templates.

All widget templates allow you to set values that identify the widget in the widget attributes pane. To learn about these, see [Providing Widget Attributes](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknlte). Some widget templates include template-specific attributes you can set in the Properties section of widget attributes; these are described below.

The Custom template for widgets creates a blank widget that contains the basic files and images needed to make a widget. A widget made from this template contains no other preconfigured abilities.

The Countdown template creates a widget with a preconfigured digital-style countdown timer. To customize this template, add a picture or other artwork and set the target event for the countdown. To set the target event for the countdown, click Widget Attributes in the navigator and modify the options available under Properties.

Options that you can set include:

**_Target Kind_**
: Set a specific date and time or a shared iCal calendar as the target for your widget. If you associate your widget with a shared iCal calendar, it counts down towards the next event on the calendar. After that event, the widget counts down to the next event on the calendar, and so forth. For more information on iCal and calendar publishing, read [Mac 101, Lesson 10: iCal](http://www.apple.com/support/mac101/work/10/).

**_When Reached_**
: When the target event is reached, your widget can stop counting or start counting upwards from the event. Also, if you choose Do Action and provide a handler, it can trigger a JavaScript function, allowing your widget to respond to the event programmatically.

**_Display_**
: Select whether the separator colons between the units of time flash and whether leading zero characters for each single-digit unit of time are shown.

The Maps template creates a widget that displays locations and location-specific information on a map. To customize this template, change its appearance on the canvas and provide the URL of a map you publish. Also, you can change how your widget displays location information.

The Maps template works with KML files and GeoRSS feeds. To set the target map for your widget, click Widget Attributes in the navigator and modify the options available under Properties.

Options you can set include:

**_Maps API Key_**
: Supply your Maps API key here. For more information on signing up for the Maps API, see [Google Maps API](http://www.google.com/apis/maps/signup.html) on the Google developer website.

**_Initial Address_**
: Supply the starting address you want to display in your widget here.

**_Mashup URL_**
: Paste the URL for your map feed here.

The RSS template creates a widget that displays headlines from an RSS source. It is suited for RSS feeds that update very frequently because it shows a number of headlines at once. To customize this template, change its appearance on the canvas and provide an RSS feed URL for the widget to display. To set the target RSS feed for your widget, click Widget Attributes in the navigator and modify the options available under Properties.

Options that you can set include:

**_Feed URL_**
: Paste the URL for an RSS feed here.

**_Show Articles_**
: Adjust how many articles your widget shows and within what period of time the articles originate.

**_Display_**
: Select whether date and time and whether a new content badge is shown with articles.

The Podcast template creates a widget that displays and plays episodes from a podcast. To customize this template, change its appearance on the canvas and provide a podcast URL for the widget to play back. To set the target podcast feed for your widget, click Widget Attributes in the navigator and modify the options available under Properties.

Options that you can set include:

**_Podcast URL_**
: Paste the URL for a podcast here.

**_Check for updates_**
: Set how often the widget should check for new episodes.

The Photocast template creates a widget that displays a slideshow of pictures obtained from an iPhoto Photocast. To customize this template, change its appearance on the canvas and provide a Photocast URL for the widget to display. To set the target Photocast for your widget, click Widget Attributes in the navigator and modify the options available under Properties.

Options that you can set include:

**_Photocast URL_**
: Paste the URL for a Photocast here.

**_Change Picture_**
: Adjust how often pictures should change.

**_Transition and Direction_**
: Set the transition used when pictures change and, if available, the direction the transition should occur.

**_Show Title_**
: Set the conditions under which the title of the Photocast should display.

The Quartz Composer template creates a widget that displays a Quartz Composer composition. Quartz Composer compositions can be used in widgets to process and display graphical data. To customize this template, show the Files list and open `Default.qtz` in Quartz Composer. Quartz Composer is installed as part of the Developer Tools for OS X v10.5.

For more information on using Quartz Composer, read _[Quartz Composer Programming Guide](../../Graphics%20Imaging/Quartz%20Composer%20Programming%20Guide/Introduction%20to%20Quartz%20Composer%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgnjx)_. For more information on the Quartz Composer WebKit plug-in (the plug-in that powers the Quartz Composer template) read _[Quartz Composer WebKit Plug-in JavaScript Reference](../../Internet%20Web/Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference/Introduction%20to%20Quartz%20Composer%20WebKit%20Plug-in%20JavaScript%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dkmjx)_.

The Video Podcast template creates a widget that displays and plays episodes from a video podcast. To customize this template, change its appearance on the canvas and provide a video podcast URL for the widget to play back. To set the target video podcast feed for your widget, click Widget Attributes in the navigator and modify the options available under Properties.

Options that you can set include:

**_Podcast URL_**
: Paste the URL for a video podcast here.

**_Check for updates_**
: Set how often the widget should check for new episodes.

The Gauge template creates a widget with gauges and indicators useful for monitoring activities. To change the sources of data for the gauges and indicators, choose `CommandMonitor.js` from the Files list and write code to interpret your source data and feed results to the gauges and indicators.

The Daily Feed template creates a widget that displays individual articles or images from an RSS source. It is suited for RSS feeds that don’t update frequently since it shows one article at a time. To customize this template, change its appearance on the canvas and provide an RSS feed URL for the widget to display. To set the target RSS feed for your widget, click Widget Attributes in the navigator and modify the options available under Properties.

Options that you can set include:

**_Feed URL_**
: Paste the URL for an RSS feed here.

**_Feed Type_**
: Specify what kind of information the feed provides. If it provides HTML content, choose HTML. If your feed provides an image (such as a comic strip or daily photo), choose Image.

All Dashcode web application templates are available for both dual-product and single-product projects. See [Creating a Project from a Template](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknltg) for more information about these two project types.

All web application templates allow you to set some options in the application attributes pane. To learn about these, see [Providing Attributes for a Web Application](Starting%20a%20Project.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknlto). If you’re developing a mobile Safari web application, be sure to set these options appropriately because they affect how users view and interact with your application on an iOS-based device. Some templates include template-specific attributes that you can set in the Properties section of application attributes; these template-specific attributes are described in the sections below.

The Custom template for web applications creates a blank web application that contains the basic files and images to make a web application. A web application made from this template contains no other preconfigured abilities.

The Browser template creates a web application that supports navigation through multiple levels of content. A web application developed with the Browser template is well-suited to displaying hierarchical information through which users can drill down.

The default web application provided by the Browser template contains a list view for the top level of the content and a detail view for the second level of the content. Selecting an item in the top-level list automatically reveals the detail view associated with that item. You can add additional list levels and you can add content to the detail views.

The Podcast template creates a web application that displays and plays episodes of a podcast that you publish. The template is set up to display a list of episodes that are played when when users select them.

To customize this template, provide the URL of a podcast that you publish. One way to do this is to put the URL in the URL field of the data model view for the podcast data source (see [Viewing a Project’s Data Sources and Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcna) to learn how to reveal this view). Alternatively, you can click Application Attributes in the navigator and modify the option under Properties.

The option you can set is:

**_Podcast URL_**
: Paste the URL for the podcast you publish here.

The RSS template creates a web application that displays headlines and articles from an RSS source. A web application developed with this template can handle RSS feeds that update very frequently because the template allows you to show numerous headlines at once.

To customize this template, provide an RSS feed URL that you publish. You can also adjust how many articles are displayed and for how long. To customize these attributes, click Application Attributes in the navigator and modify the options under Properties.

Options that you can set include:

**_Feed URL_**
: Paste the URL for the feed you publish here.

**_Show Articles_**
: Adjust how many articles to display in your web application, within what time period the articles originate, and how many “top stories” to display.

You can also specify the feed URL in the URL field of the data model view for the feed data source. See [Viewing a Project’s Data Sources and Bindings](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcna) to learn how to reveal this view.

The Utility template creates a web application that displays a text entry area. In the Safari product it displays a toolbar that contains editing controls; in the mobile Safari product it includes a reverse side you can use to display configuration options or a different view.

To customize this template for a mobile Safari product, place your content in the front view and the configuration options or alternative view you want to offer in the settings view. Be sure to leave the Info button in place (the template provides this button in the lower-right corner of the front view), because users know they can tap this control to see the reverse side of a mobile Safari web application.

[Next](Dashcode%20Parts.md)[Previous](Advanced%20Topics%20for%20Widgets.md)

