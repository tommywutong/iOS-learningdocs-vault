---
title: Quartz Composer CommandLineTool
apple_id: DTS40009314
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2009-10-27'
source_url: https://developer.apple.com/library/archive/samplecode/CommandLineTool/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:04:06.129423Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer CommandLineTool](Quartz%20Composer%20CommandLineTool.md)


[Next](CommandLineToolPlugIn.h.md)[Previous](Quartz%20Composer%20CommandLineTool.md)

# ReadMe.txt

```
Copyright © 2007-2009 by Apple Inc.  All Rights Reserved.

Quartz Composer Plugin

CommandLineTool                 A Quartz Composer plug-in that executes synchronously a 
                        command line tool.

Sample Requirements             The plugin was created using the Xcode editor running 
                        under Mac OS X 10.6.x or later. 

About the sample                A Quartz Composer plug-in that uses NSTask and NSPipe to 
                        execute synchronously a command line tool.

Using the Sample                Open the project using the Xcode editor which can be found 
                        in /Developer/Applications. From the main menu, 
                        choose "Project", set "Active Configuration" to "Release", 
                        and "Active Target" to "Build & Copy".  These settings are
                        also available from the top left corner of the 'Overview' 
                        pop-up window. Build the project. Once the build has 
                        completed successfully, the plug-in can be used as a 
                        regular QC patch in the Quartz Composer editor (also 
                        installed under /Developer/Applications), by selecting it 
                        from the Library - Plugin panel.

                        The command line standard input is set in the plug-in 
                        input port "Standard In". The command with full path is 
                        set in the input port "Path". To add command arguments, 
                        click on the patch, open the "Patch Inspector", in the top 
                        pull-down menu, select "Settings", increase the "Number of 
                        Arguments", new input argument ports will be added in the 
                        patch.

Installation                    n/a

Changes from Previous Versions          n/a

Feedback and Bug Reports            Please send all feedback about this sample to:
                        http://developer.apple.com/contact/feedback.html

                        Please submit any bug reports about this example to 
                        http://developer.apple.com/bugreport
```

[Next](CommandLineToolPlugIn.h.md)[Previous](Quartz%20Composer%20CommandLineTool.md)

