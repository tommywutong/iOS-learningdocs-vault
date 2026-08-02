---
title: Xgrid Programming Guide
apple_id: TP40006246
resource_type: Guide
platform: macOS
topic: Performance
technology: XgridFoundation
published: '2007-10-31'
source_url: https://developer.apple.com/library/archive/documentation/MacOSXServer/Conceptual/Xgrid_Programming_Guide/WritingaCocoaXgridClient/WritingaCocoaXgridClient.html
archived_at: '2026-07-15T08:16:48.262104Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xgrid Programming Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Overriding%20the%20Job%20Specification%20Function.md)

# Writing a Cocoa Xgrid Client

As you learned in the previous chapter, you can create a client application by simply modifying the GridSample sample code. You may need to go further, however, and develop your own application, or add Xgrid capability to an existing application. This chapter describes the basic steps.

There are six steps that any Xgrid client application must take:

1. Locate a controller—You need to locate a controller, which typically involves bringing up a service browser and letting the user choose a controller.
2. Connect and authenticate—You need to connect to the controller, which is typically password protected.
3. Submit the job—The tasks must be assembled and submitted to the controller with the proper syntax, specifying a grid.
4. Identify the job—When you submit a job, an action monitor object is returned. Use this object to determine whether your job submission was successful and to obtain the job ID for future reference.
5. Receive notifications—Once you have a job ID, you can register to be notified when the job completes, when tasks complete, or when errors occur.
6. Collect the data—When the job completes, you need to collect the returned data and deal with it appropriately.

Of course, there are housekeeping tasks as well, such as deleting the job when you are done.

This chapter highlights the functions you need to use to accomplish each step, and points you to code samples that illustrate their use.

All code samples are included as part of the GridSample project, which is installed in the `Developer/Examples/Xcode` directory on your hard disk when you install the Mac OS X Developer Tools (Tiger) or XCode Tools (Leopard).

To browse for Xgrid controllers, use the [NSNetServiceBrowser](https://developer.apple.com/documentation/foundation/netservicebrowser) function. `GridSampleServiceBrowser.m` in GridSample provides a working code sample of an Xgrid service browser.

Connect to an Xgrid server using the `XGConnection` and `XGController` functions. See `GridSampleConnectionController.m` in GridSample for working code samples.

You may not need to authenticate to access an Xgrid controller, but you typically do.

Authentication by means of a simple password is supported, as is authentication using single sign-on (SSO or Kerberos). The `XGConnection` function requires an authentication parameter. If the controller is unprotected, pass `nil`. If it is protected, pass the user name and password, using `XGTwoWayRandomAuthenticator`. If using Kerberos, use `XGGSSAuthenticator`.

`GridSampleConnectionController.m` attempts an initial connection with the connection authenticator set to `nil`. If the connection fails with an authentication error, the user is prompted for login information and `XGAuthenticator` is set.

Refer to `GridSampleLoginController.m` in GridSample for a working code sample.

Submit jobs to Xgrid using the `XGController` function, using this syntax:

`-[XGController performSubmitJobActionWithJobSpecification:gridIdentifier:]`

Note that you need to pass a job specification and a grid identifier, of type `XGGrid`.

`GridSampleNewJobWindow.m` includes sample code for a pop-up window that allows the user to choose an available grid.

Constructing a properly formatted job submission is non-trivial. Refer to the man page for `xgrid` for the correct syntax.

Refer to `GridSampleNewJobWindowController.m` in GridSample for working job submission sample code. You may also find `GridCalendarNewJobWindowController.m` helpful. If you have not already done so, download the GridCalendar sample code from [http://developer.apple.com/samplecode/GridCalendar/](https://developer.apple.com/samplecode/GridCalendar/).

When you submit a job using `XGController`, an `XGActionMonitor` object is returned. Monitor the `XGActionMonitor` object until the `isUpdating` attribute is false, then verify that the dictionary contains a “success” entry. If the job submission is successful, the `jobIdentifier` attribute contains the job ID, an object of type `XGJob`. Pass this identifier to the appropriate functions to monitor the job status and retrieve the data.

Refer to `GridSampleNewJobWindowController.m` in GridSample for working sample code.

Register for notification of job state changes, or query the controller for the current job state, using the `XGActionMonitor` function. Pass in the job identifier you received in step four.

Refer to `GridSampleNewJobWindowController.m` in GridSample for working sample code.

When the job completes, collect your data using `XGFile` and `XGFileDownload` functions. Identify the job using the identifier object (`XGJob`).

Refer to `GridSampleJobResultsWindowController.m` in GridSample for working sample code.

When the job is complete, and you have collected the results, the job should be deleted, notification observers should be removed, and unneeded structures and objects should be deallocated.

See the `dealloc` function in `GridSampleJobResultsWindowController.m` for an example of good housekeeping practices.

[Next](Document%20Revision%20History.md)[Previous](Overriding%20the%20Job%20Specification%20Function.md)

