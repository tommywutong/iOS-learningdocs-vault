---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/Setting_Up_Applications.html
archived_at: '2026-07-15T08:12:01.715063Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Installing_Applications.md)[!](Configuring_Sites.md)

## Setting Up Applications

To deploy an application on your site, it must be installed
in the appropriate directories on the hosts that run instances of
it. For more information, see ["Installing Applications"](Installing_Applications.md#apple-ijbusrcjjfcei).

Setting up an application in your site involves three main
steps:

- __Adding
  the application,__ which is described in ["Adding an Application"](#apple-krifqusfiyytcna).
- __Configuring the application__, which
  includes the following subtasks:
  - defining a default
    configuration for new instances of the application
  - defining the recipients of email notifications
  - defining a schedule (only available for existing instances)
  - choosing a load-balancing algorithm

  These
  steps are detailed in ["Configuring an Application"](#apple-krifqusfiyytcni).
- __Adding application instances,__ which
  is described in ["Adding Application Instances"](#apple-ijbusskjiveeu).

### Adding an Application

You add applications to your site using Monitor's Applications
page, shown in [Figure 6-5](#apple-krifqusfiyytamy).

__Figure
6-5 Adding an application using Monitor's
Applications page__

![[image: ../Art/applicationadd.gif]](../Art/applicationadd.gif)

Follow these steps to add an application:

1. Enter the
   application's name (without the extension) in the Add Application
   Named text field.
2. Click Add Application.

### Configuring an Application

After you add an application, the application configuration
page is displayed. This page has five major sections, which you
can show and hide using the disclosure triangles:

- The [New Instance Defaults](#apple-krifqusfiyytcnq) section
  lets you set the default values for the instance settings for application
  instances you add afterward. See ["New Instance Defaults"](#apple-krifqusfiyytcnq) for details.
- The [Application Settings](#apple-krifqusfiyytcny) section contains properties that apply to all
  the instances of the application. For more, see ["Application Settings"](#apple-krifqusfiyytcny).
- The [Scheduling](#apple-krifqusfiyytcoa) section
  allows you to individually schedule instances to restart at specific
  intervals. See ["Scheduling"](#apple-krifqusfiyytcoa) for
  details.
- The [Email Notifications](#apple-krifqusfiyytcoi) section is where you specify the list of
  email addresses you want email notifications to be sent to. For
  details, see ["Email Notifications"](#apple-krifqusfiyytcoi).
- The [Load Balancing and Adaptor Settings](#apple-ijbusqsfjjeeg) section lets you choose
  the algorithm that the HTTP adaptor uses to perform load balancing
  among the instances of the application. See ["Load Balancing and Adaptor Settings"](#apple-ijbusqsfjjeeg).

#### New Instance Defaults

[Figure 6-6](#apple-ijbusskii5ceg) shows the section of the application configuration
page that allows you to set defaults for the application instances
you create afterward and for current ones (which are updated after
you restart them). For details on each of the properties shown on
this page, see ["Instance Settings"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).

__Figure
6-6 The New Instance Defaults section
of the application configuration page__

![[image: ../Art/newinstancedefaults.gif]](../Art/newinstancedefaults.gif)

Here's an explanation of the buttons you see on the page:

- __Push__ updates
  the value of the property for new and configured (registered) instances of
  the application. The changes take effect after the instances are
  restarted.
- __Push All__ updates the value of the all
  the properties for new and configured instances of the application.
  As with Push, the changes become effective when the instances are restarted.
- __Update for New Instances Only__ sets
  the defaults to be used when you create new instances of the application.
  The properties of existing instances are not changed.
- __Path Wizard__ opens a tool that allows
  you to navigate through a host's file system.

#### Application Settings

[Figure 6-7](#apple-ijbusskhizcem) shows the Application Settings section of the application
configuration page. In it, you define application settings that
apply to all the instances of the application. For details of the
properties shown in this section, see ["Application Settings"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).

__Figure
6-7 The Application Settings section of
the Applications page__

![[image: ../Art/applicationsettings.gif]](../Art/applicationsettings.gif)

#### Scheduling

[Figure 6-8](#apple-ijbusrsgifduu) shows the Scheduling section of the application configuration
page. After you add instances of an application, you can schedule
them individually here. For details, see ["Scheduling Settings"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).

__Figure
6-8 The Scheduling section of the application
configuration page__

![[image: ../Art/scheduling.gif]](../Art/scheduling.gif)

#### Email Notifications

|  |
| --- |
| __Note:__  Before you can configure email notifications, you have to tell Monitor which SMTP server to use. See ["Configuring Sites"](Configuring_Sites.md#apple-ijbusrkijjcuq). |

[Email Notification Settings](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html) shows the [Email Notification Settings](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html) section
of the application configuration page. In it you can enter the email
addresses of people that are to be notified when instances of the
application terminate unexpectedly.

__Figure
6-9 The Email Notifications section of
the Application Configuration page__

![[image: ../Art/emailnotifications.gif]](../Art/emailnotifications.gif)

#### Load Balancing and Adaptor Settings

[Figure 6-10](#apple-ijbusq2ejjeeu) shows the Load Balancing and Adaptor Settings section
of the application configuration page. This is where you enter values
for the HTTP adaptor's configuration properties, including the
load-balancing algorithm the adaptor will use to balance user load
among the application's instances. These settings override the
values entered in the HTTP Adaptor Settings section of the Site
page. For information on the properties you can set, see ["Load Balancing and Adaptor Settings"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).

__Figure
6-10 The Load Balancing and Adaptor Settings
section of the application configuration page__

![[image: ../Art/adaptorsettings.gif]](../Art/adaptorsettings.gif)

### Adding Application Instances

After you have configured an application in Monitor, you can
create application instances with ease.

1. In Monitor,
   click the Applications tab. The Applications page is displayed,
   as shown in [Figure 6-11](#apple-ijbusssjijeeu).

   __Figure
   6-11 The Applications page with one application__

   ![[image: ../Art/applications.gif]](../Art/applications.gif)
2. Click the Detail View button under View Instances. The application
   detail page is displayed, as shown in [Figure 6-12](#apple-ijbusrkcjjbes).

   __Figure 6-12 The
   application detail page__

   ![[image: ../Art/applicationdetail.gif]](../Art/applicationdetail.gif)
3. Enter the number of instances you want to add in the text
   input field.
4. Choose the application host you want the instances to run
   on from the pop-up menu.

   The application must be installed
   on the host you choose; otherwise, an error message is displayed
   when you try to start the instance. See ["Installing Applications"](Installing_Applications.md#apple-ijbusrcjjfcei) for
   details.
5. Click Add. Your Web browser displays a page like the one in [Figure 6-13](#apple-ijbusrkkirdeo).

   __Figure
   6-13 The application detail page after
   an instance has been added__

   ![[image: ../Art/instanceadded.gif]](../Art/instanceadded.gif)

The Status column indicates whether the instance is on or
off. The first time the page is displayed, the newly added instances
are off. After a moment (or if you click Refresh Now), and if [Auto Recover](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html) is enabled for the
instance, the page refreshes, showing that the instance is active.
(You can change the length of the interval between the automatic updates
of the application detail page; see ["Setting Monitor Preferences"](Setting_Mon_Preferences.md#apple-ijbusrsgjjdue) for
details.)

[Figure 6-14](#apple-ijbegr2giveue) shows the application detail page of the HR application,
with two instances configured.

__Figure
6-14 The Application Detail page with
two instances added__

![[image: ../Art/detailview.gif]](../Art/detailview.gif)

The following list describes the instance configuration information
that appears in the application detail page:

- __Page
  heading__ A link to the application through the HTTP adaptor.
  When you click it, the adaptor uses load balancing to determine
  which of the application's instances receives the request. Then,
  your Web browser displays a new window showing your application's
  entry page. For this to work, the HTTP adaptor URL has to be set ( ["Configuring Sites"](Configuring_Sites.md#apple-ijbusrkijjcuq) shows
  you how to do this).
- __Name__ A link to the instance through
  the HTTP adaptor. When you click it, the request goes through the
  adaptor, but it's not load balanced. The URL is derived in the
  same way the URL of the page heading is derived, but with the addition
  of the instance number. Such a URL looks similar to the following:

  ```
  http://ebruce2.apple.com/cgi-bin/WebObjects/HR.woa/1
  ```
- __Host-Port__ A direct link to the instance;
  does not go through the HTTP adaptor.
- __Status__ Tells whether the instance is
  on, off, starting, or stopping.
- __Start-Stop__ Click the green button to
  turn the instance on, or the red button to turn it off.
- __Auto Recover__ Click to toggle between
  ON and OFF. This is available only if the instance is not scheduled.
  See ["Auto Recover"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).
- __Refuse New Sessions__ Click to toggle
  between ON and OFF. When ON, the instance does not accept new users.
  This is available only if the instance is not scheduled.
- __Scheduled__ Click to toggle between ON
  and OFF. When ON, the schedule defined for the instance is used.
- __Configure__ Click the Config button to
  go to the instance configuration page for the instance.
- __Delete__ Click the Delete button to delete
  the instance. You'll see a confirmation page before the deletion
  takes place.

For an explanation of the columns under Statistics, see ["The Application Detail Page"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Administration/iMonitoring_Activity.html).

The row with the caption ALL INSTANCES contains buttons that
perform some of the functions listed above on all the instances
of the application. Clicking Config displays the application configuration
page.

### Configuring Instances

After you have added an instance, you can change its configuration
in the instance configuration page, shown in [Figure 6-15](#apple-ijbusrkgizauk). You can access this
page through the instance's Config button in the application detail
page. It contains two sections: [Instance Settings](#apple-ijbusssjijcus) and [Adaptor Settings](#apple-ijbusqshjfeeg).

__Figure
6-15 Instance configuration page__

![[image: ../Art/instanceconfigure.gif]](../Art/instanceconfigure.gif)

#### Instance Settings

This section is very similar to the [New Instance Defaults](#apple-krifqusfiyytcnq) section of
the application configuration page. It has two additional properties: [ID](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html) and [Port](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html), which can only be changed
after an instance has been added. For details, see ["ID"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html) and ["Port"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).

#### Adaptor Settings

In this section you can change a subset of the properties
available in the [Load Balancing and Adaptor Settings](#apple-ijbusqsfjjeeg) section of the application
configuration page. For details, see ["Load Balancing and Adaptor Settings"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Reference/iApplication__Properties.html).

#### Setting a Password for the Instance Statistics Page

For each instance of your application, there's a statistics
page that displays information such as its running time and memory
usage. See ["The Instance Statistics Page"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Administration/iMonitoring_Activity.html) for
more information on this page. If you want to prevent outside agents
from gaining access to the instance statistics page, you can set
a password in the Instance Settings section of the instance configuration
page. Add the following to the Additional Arguments property: `-WOStatisticsPassword` _password_. [Figure 6-16](#apple-krifqusfiyytana) shows
an example where the `WOStatisticsPassword` argument
has been added to the Additional Arguments field.

__Figure
6-16 Setting a password for an instance's
statistics page__

![[image: ../Art/statisticspassword.gif]](../Art/statisticspassword.gif)

[!](Installing_Applications.md)[!](Configuring_Sites.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
