---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Administration/Monitoring_Activity.html
archived_at: '2026-07-15T08:11:57.004658Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


[!](Application%20Administration.md)[!](Improving_Performance.md)

## Monitoring Activity

There are several ways to obtain information about the applications
deployed on your site. You can

- use Monitor
- analyze logs from application instances and adaptors
- view instance statistics (WOStats) pages

### Monitoring Application Performance

Monitor's Applications page gives you an overall view of
a site. [Figure 7-1](#apple-ijauurkgincuq) illustrates the kind of information you can access
through the Applications page:

- configured
  applications
- number of configured instances per application
- number of running instances per application

__Figure
7-1 The Applications page__

![[image: ../Art/applications2.gif]](../Art/applications2.gif)

From this page, you can perform several tasks:

- __Connect
  to an instance of an application__ The entry page of the
  application is displayed in a new Web browser window.
- __Display the application detail page of an application__ For
  details on the information provided, see ["Adding an Application"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Up_Applications.html)
- __Delete an application__ You confirm that
  you really want to delete the application (including all of its
  instances) in a confirmation page before the deletion takes place.

#### The Application Detail Page

[Figure 7-2](#apple-ijauurcjiveec) depicts the application detail page.

__Figure
7-2 The Application Detail page__

![[image: ../Art/applicationdetail2.gif]](../Art/applicationdetail2.gif)

The application's name is displayed centered and in bold
letters. When there are active instances, it is a link to the application
through the HTTP adaptor; the request is load balanced. (For this
to work, the HTTP adaptor URL property must be set; see ["Configuring Sites"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iConfiguring_Sites.html) for
details. If no value has been entered for the property, the default
URL `(http://localhost/cgi-bin/WebObjects/`)
is used instead.) The URL used to connect to the application looks
similar to the following:

```
http://localhost/cgi-bin/WebObjects/Payroll
```

The following list describes the performance-related information
shown on the application detail page in the Statistics columns:

- __Transactions__ The
  number of requests the instance has received since it was started.
- __Active Sessions__ The number of active
  sessions (users) currently maintained by the instance.
- __Average Transaction__ Average time, in
  seconds, the instance has taken to process requests.
- __Average Idle Period__ The average time,
  in seconds, that the instance is idle (average time between requests).
- __Deaths__ The number of unexpected failures
  or deaths the instance has had since it was started. These exclude
  scheduled shutdowns or manual shutdowns through Monitor.
- __WOStats__ Click to display the statistics
  page for the instance in a new Web browser window. See ["The Instance Statistics Page"](#apple-krifqusfiyytanq) for details.

  Before you can view the instance
  statistics page, you have to enter the password you set on the instance
  configuration page. See ["Setting a Password for the Instance Statistics Page"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DeployingWebObjects/Deployment/iSetting_Up_Applications.html) for details.

The row with the caption ALL INSTANCES contains application-wide
performance information, including the average number of transactions
processed per minute (TPM).

#### The Instance Statistics Page

You can access the instance statistics (WOStats) page of an
instance through Monitor or directly through a Web browser.

To use Monitor, go to the application detail page and click
WOStats for the instance whose statistics you want to view.

To use your Web browser, access the following URL:

```
http://myhost/cgi-bin/WebObjects/MyApp.woa/wa/WOStats
```

If there are multiple instances, specify the instance number
as well:

```
http://myhost/cgi-bin/WebObjects/MyApp.woa/1/wa/WOStats
```

[Figure 7-3](#apple-ijauurcdizdee) and [Figure 7-4](#apple-ijauuq2eifeue) show the information the instance statistics page
provides.

__Figure
7-3 The instance statistics page—part
1 of 2__

![[image: ../Art/wostats.gif]](../Art/wostats.gif)

__Figure
7-4 The instance statistics page—part
2 of 2__

![[image: ../Art/wostats2.gif]](../Art/wostats2.gif)

### Logging and Analyzing Application Activity

WebObjects applications can record information in a log file
that can be analyzed by a Common Log File Format (CLFF) standard
analysis tool. Applications do not maintain this log file by default;
log-file recording must be enabled through an application's code.
When enabled, the application records a list of components accessed
during each session. By default, only component names are recorded,
but you may add more information.

### Logging and Analyzing Adaptor Activity

To enable adaptor logging, you create a file called logWebObjects in
the temporary directory of the computer where the Web server runs.
When logging is enabled, the adaptor logs its activity in a file
called `WebObjects.log` in
the temporary directory. Logging adaptor activity significantly
decreases performance. Use this feature only as a troubleshooting
aid; do not use it during regular deployment.

The location of the temporary directory depends on the platform:

- Mac OS X
  Server and Solaris: `/tmp`
- Windows 2000: The directory indicated by the `TEMP` environment
  variable.

#### Creating the Adaptor Log File

On UNIX-based platforms, do the following to create the `logWebObjects` file
(you must have root privileges):

1. Start a command-shell
   window.
2. Set the working directory to the temporary directory.
3. Enter the following command:

   ```
   touch logWebObjects
   ```

On Windows 2000, create a blank file using a text editor and
save it as `logWebObjects` in
the temporary directory.

You can use the `tail` (UNIX)
or `type` (Windows 2000)
commands to display the adaptor log file in your console.

On UNIX-based systems, use the following:

```
tail -f WebObjects.log
```

On Windows 2000, type the following in a DOS prompt:

```
type WebObjects.log
```


#### Analyzing the Adaptor Log File's Contents

You can analyze the information in the log to find out such
things as which applications are being requested, which applications
are being auto-started, and what the HTTP headers of requests are.
You can also use the log to verify that the HTTP adaptor is properly
configured for load balancing.

The following excerpt includes an error message that indicates
that an instance of Payroll wasn't running when a request for
it came in:

```
Info: <WebObjects Apache Module> new request: /cgi-bin/WebObjects/Payroll
Debug: App Name: Payroll (7)
Info: Specific instance Payroll: not found. Reloading config.
```

After Payroll is started, the same request produces the following
log-file entries:

```swift
Info: New response: HTTP/1.0 200 Apple WebObjects
Info: ac_newInstance(): added Payroll:2 (2001)
Info: V4 URL: /cgi-bin/WebObjects/Payroll
Info: loadaverage: selected instance at index 4
Info: Selected new app instance at index 4
Debug: Composed URL to '/cgi-bin/WebObjects/Payroll.woa/1'
Info: New request is GET /cgi-bin/WebObjects/Payroll.woa/1 HTTP/1.0

Info: Sending request to instance number 1, port 2001
Info: Trying to contact Payroll:1 on (2001)
Info: attempting to connect to ebruce.apple.com on port 2001
Info: Created new pooled connection [1] to ebruce.apple.com:2001
Info: Using pooled connection to ebruce.apple.com:2001
Info: Payroll:1 on (2001) connected [pooled: Yes]
Info: Request GET /cgi-bin/WebObjects/Payroll.woa/1 HTTP/1.0
 sent, awaiting response
Debug: ac_readConfiguration(): skipped reading config
Info: New response: HTTP/1.0 200 Apple WebObjects
Info: Payroll 1 load avg = 1
Info: received ->200 Apple
```

[!](Application%20Administration.md)[!](Improving_Performance.md)

---

© 2001 Apple Computer, Inc. (Last Updated August 25, 2001)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
