---
title: WebObjects Tutorial
apple_id: TP40008108
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-02-04'
source_url: https://developer.apple.com/library/archive/documentation/DeveloperTools/Conceptual/WOTutorial/InstallingEclipseandtheWOLipsPlug-in/InstallingEclipseandtheWOLipsPlug-in.html
archived_at: '2026-07-15T07:27:10.470208Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Tutorial](Introduction.md)


[Next](Creating%20a%20WebObjects%20Database%20Application.md)[Previous](Introduction.md)

# Installing WebObjects, Eclipse, and the WOLips Plug-in

The WOLips plug-in for the Eclipse integrated development environment (IDE) is the recommended environment for WebObjects development. This chapter will guide you through the process of installing Eclipse and the plug-in.

You must have the Apple developer tools installed in order to install WebObjects. Both WebObjects and the Apple developer tools are available from the Downloads page linked from the Apple Developer Connection homepage ([http://connect.apple.com](http://connect.apple.com/)). If you already have WebObjects installed, ensure that you are using the latest update of WebObjects and read any release notes regarding the update. You do not need to download separate WebObjects updates if you are running Mac OS X Server, because WebObjects updates are included in operating system updates downloaded with Software Update. Apple developer tools updates are not included in Mac OS X Server updates, however, so you should still ensure that you have the latest version of the Apple developer tools.

Eclipse v3.3.2 is available for download from the Eclipse Foundation website at [http://www.eclipse.org/downloads/packages/release/europa/winter](http://www.eclipse.org/downloads/packages/release/europa/winter). Download and install the Mac OS X package of the Eclipse IDE for Java Developers.

The simplest way to download the WOLips plug-in is from within Eclipse.

1. Open Eclipse.
2. Choose Help > Software Updates > Find and Install.
3. Select “Search for new features to install” and click Next.
4. Add the WOLips site to the list of sites to search.

   - Click the New Remote Site button.
   - In the dialog, enter `WOLips` in the name field and `http://webobjects.mdimension.com/wolips/stable` in the URL field.
   - Click OK.
5. Select the WOLips site that appears in the site list and click Finish.
6. Expand the WOLips item that appears in the Search Results dialog. Select Standard Install and click Next.
7. Read and accept the terms in the license agreements and click Next.
8. Click Finish. The plug-in will download. A Feature Verification dialog appears, noting that the plug-in is not digitally signed. Click Install All.
9. Click Yes to restart Eclipse. The plug-in is installed and ready to use.

[Next](Creating%20a%20WebObjects%20Database%20Application.md)[Previous](Introduction.md)

