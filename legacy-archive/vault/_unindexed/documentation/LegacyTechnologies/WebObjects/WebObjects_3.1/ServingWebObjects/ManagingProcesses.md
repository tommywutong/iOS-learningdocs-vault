---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/ServingWebObjects/ManagingProcesses.html
archived_at: '2026-07-15T07:49:59.730965Z'
---
> 导航：[总目录](../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Previous Section](ManualStarting.md)

# Managing Application Processes

The platforms on which WebObjects can be installed have various means for monitoring running processes, including WebObjects application processes, and for terminating those processes (called rather violently, on UNIX platforms, "killing" processes). There can be many reasons for terminating processes, such as to upgrade to a modified version of an application or to debug a scripted application when page-recreation is turned off.

## __Solaris, HPUX, and Mach__

Using a shell program (such as the Terminal application on Mach) enter the __ps__ command on the command line. This command, without any arguments, lists minimal information about running processes. To narrow the search for a particular WebObjects application, give the following compound piped command on Solaris and HPUX:

```
  ps -eaf | grep ApplicationName
```

On Mach, the __ps__ argumentsare different:

```
  ps -auxwww | grep ApplicationName
```

If you want to check on a scripted application, use __WODefaultApp__ as _ApplicationName_. Here's some sample output:

```
  nobody    3012   0.0 11.7 5.49M 2.81M co S     0:13 WODefaultApp -d   /NextLibrary/WebServer/htdocs Examples/TimeOff
```

Note that the command-line arguments are shown, thereby allowing you to learn, in the case of __WODefaultApp__, which scripted applications are running.

To terminate an application, note its process ID (PID) number (3012 in the above example) and "kill" it:

```
  kill 3012
```

If you cannot kill the application from your own account, enter __su__, log into the superuser account, and try the __kill__ command again.

## __Windows NT__

On Windows NT 4.0 use the Task Manager program to monitor and terminate processes.

1. To activate the Task Manager, click the right mouse button on a blank area of the status bar (the rectangular strip containing the Start menu).
2. Choose Task Manager from the pop-up menu.
3. In the Task Manager window locate the WebObjects application process that you're interested in. If it's a scripted application, look for __WODefaultApp__. Task Manager presents options for customizing the information displayed, so if you're interested in a certain aspect of the process, be sure to select the appropriate option.
4. To terminate a process, select its name (so that it's highlighted) and click End Process.

On Windows NT 3.51, use Visual C++'s __Pview__ program (if installed) to terminate processes.

### __Notes__

If you cannot terminate an autostarted application on Windows NT, it is probably because it is started under an account for which you don't have privileges. See "[Autostarting Applications](Autostarting.md#apple-kjcumojugu3dq)" for instructions on rectifying this situation.

[!Table of Contents](ServingWebObjectsTOC.mif.md)
[!Next Section](Logging.md)
