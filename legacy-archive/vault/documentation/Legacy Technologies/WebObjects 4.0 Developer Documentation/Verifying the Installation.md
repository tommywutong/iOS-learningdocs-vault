---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.7.html
archived_at: '2026-07-15T08:00:23.627243Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Post-Install Guide](About%20This%20Document.md)

[!Table of Contents](About%20This%20Document.md) [!Previous Section](Setting%20Up%20the%20Sample%20Databases.md)

#   Verifying the Installation

At this point, you should have installed WebObjects as described in the _WebObjects Installation Guide_ (included with the WebObjects 4.0 CD), perform the post-installation steps for your operating system as described in the first part of this document, and rebooted your computer.

After you have completed the installation and the post-installation, verify the installation by performing the following steps:

> 
>
> Note: These steps assume you've installed WebObjects Developer. The examples mentioned below are not installed with WebObjects Deployment. To verify a Deployment installation, you might complete these same steps running other applications.

- 

  Try to run a simple scripted application.

> 
>
> Open a command-shell window (on Windows NT, open a Bourne shell window) and enter the following commands:

> ```
> > cd NEXT_ROOT/Developer/Examples/WebObjects/WebScript/HelloWorld
> ```

> ```
> > NEXT_ROOT/Library/WebObjects/Executables/WODefaultApp[.exe]
> ```

> 
>
> where:

> 
>
> _NEXT_ROOT_ is the directory in which you installed WebObjects software (_NEXT_ROOT_ isn't applicable on Mac OS X systems).

> 
>
> These commands should run the HelloWorld example application, launch a web browser, and enter HelloWorld's URL in the browser. If this doesn't work, go to the topic _[Troubleshooting](Troubleshooting.md#apple-gqyteobt)
> ._

> 
>
> After you have verified that HelloWorld runs, type Control-C to shut it down.

- 

  If scripted applications work, try running compiled applications. If your operating system has Java support (Mac OS X Server, Windows NT, or Solaris), enter the following commands:

> ```
> > cd ../../Java/Movies/Movies.woa> ./Movies[.exe]
> ```

> 
>
> If your operating system does not have Java support (HP-UX), open the Objective-C version:

> ```
> > cd ../../ObjectiveC/HelloWorldCompiled/HelloWorldCompiled.woa> HelloWorldCompiled
> ```

> 
>
> If you have trouble running compiled applications, go to the topic _[Troubleshooting.](Troubleshooting.md#apple-gqyteobt)_

> 
>
> After you have verified that Movies or HelloWorldCompiled runs, type Control-C to shut it down.

[!Table of Contents](About%20This%20Document.md) [!Next Section](Troubleshooting.md)
