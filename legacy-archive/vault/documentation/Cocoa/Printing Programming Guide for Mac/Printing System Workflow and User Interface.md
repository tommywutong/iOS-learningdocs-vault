---
title: Printing Programming Guide for Mac
apple_id: 10000083i
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-12-20'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Printing/osxp_flexible/osxp_flexible.html
archived_at: '2026-07-15T07:17:42.144402Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Printing Programming Guide for Mac](About%20Printing%20on%20the%20Mac.md)


[Next](The%20AppKit%20Printing%20API.md)[Previous](About%20Printing%20on%20the%20Mac.md)

# Printing System Workflow and User Interface

Gone are the days when users had to download and install printer drivers and OS X had to package and distribute large packages of them. Printing on the Mac is not only easy for the user, but the modern API provided by OS X is easy for you to use in your app. Printing a single page from an app can take just a few lines of code. The code for controlling pagination, margins, headers, and footers for multipage documents with precise layout needs more code, but it is straightforward to write.

Printing is generally initiated by the user choosing the Print menu command. An app uses the AppKit printing API to assemble the elements of a print job, including the content to print and information about the print job. The app then presents the Print panel as described in [The Printing User Interface](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga4dg2jninedclktk43q). The user can then set printing options before clicking Print. At that point, the AppKit framework asks the app to draw the content to print. AppKit records what the app draws as PDF data and then hands off that data to the printing subsystem.

__Figure 1-1__  The printing system architecture

!

The printing subsystem writes the PDF data it receives to storage (that is, spools the data). It also captures information about the print job. The printing subsystem manages the combined print data and metadata for each print job in a first-in-first-out print queue. Multiple apps on a computer can submit multiple print jobs to the printing subsystem, and all of these are placed in the print queue. Each computer has one queue for all print jobs regardless of the originating app or destination printer.

When a print job rises to the top of the queue, the system printing daemon (`cupsd`) considers the destination printer’s requirements and, if necessary, converts the print data to a form that is usable by the printer. The printing subsystem reports error conditions such as “Out of Paper” to the user as alerts. It also reports the progress of print jobs programmatically to the PrintProxy app, which displays information such as “page 2 of 5” for a print job. (The PrintProxy app takes on the name of the printer. It’s the app the displays the queued print jobs for that printer and allows the user to pause, resume, and cancel jobs that are in the queue.)

When the user chooses Print from the File menu, they are presented with a Print panel as shown in Figure 1-2. The Printer pop-up menu is populated with the last printer used. The user can page through a preview of a document that has multiple pages and can choose to print all pages or set a range. For most users, the simple Print panel is all they ever need. They might never see any of the other user interface elements described in this section. But for those users who require more control over the printing process and the printers they use, OS X provides it.

__Figure 1-2__  The Print panel as a sheet in Preview

!

The user can click the Show Details button to control a variety of printing options including layout, color matching, and paper handling. Many options are dependent on the features available for the specified printer, such as the availability of duplex printing. An app can supply its own options, as shown in Figure 1-3. In this example, Preview supports rotation, scaling, copies per page, and how to fill the page with the image.

__Figure 1-3__  The Print panel with Preview’s custom accessory view

!

Apps can choose whether to display the Print panel as a sheet or a a separate window, although it’s most common to show a sheet so the user can easily see the window to which the panel applies.

Choosing a printer for printing is easy for the user, which they do through the Printer pop-up menu in the Print panel. The user can choose from a list of nearby printers and OS X sets up the printer automatically. A user who needs more control on adding printing devices can choose Add Printer to access the Add window as shown in Figure 1-4. This window is automatically populated by the devices that OS X can detect, including AirPrint printers. Users have the option to add specific host name or IP addresses as well as to add Fax and Windows workgroup printers.

__Figure 1-4__  The Add Printer window

!

Some apps also provide users with the option to setup the page through the Page Setup pane as shown in Figure 1-5. Most of the time users shouldn’t need to perform any setup through this panel. So if your app doesn’t need it, make the user experience simpler by not providing a Page Setup command.

__Figure 1-5__  The Page Setup panel

!

Users can manage printers through the Print & Scan preference pane in System Preferences, as shown in Figure 1-6.

__Figure 1-6__  The Print & Scan preferences pane

!!

OS X automatically adds recently used printers to the list but a user can add others as well as delete any in the list. Opening a print queue provides the user with the option to pause a print job and to access printer settings. By clicking the Options & Supplies button, the user can set the printer name, manage driver options, check supply levels, and open a printer’s utility app.

[Next](The%20AppKit%20Printing%20API.md)[Previous](About%20Printing%20on%20the%20Mac.md)

