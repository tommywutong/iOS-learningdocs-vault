---
title: ScriptingBridgeFinder
apple_id: DTS10004283
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: ScriptingBridge
published: '2011-08-05'
source_url: https://developer.apple.com/library/archive/samplecode/ScriptingBridgeFinder/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:23:33.483838Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ScriptingBridgeFinder](ScriptingBridgeFinder.md)


[Next](main.m.md)[Previous](ScriptingBridgeFinder.md)

# ReadMe.txt

```objc
ScriptingBridgeFinder
=====================


Introduction

This file details the steps involved in putting together a project that uses Scripting Bridge to send Apple events to the Finder application for finding
and launching applications.  



1. Start with a new Objective-C application.

This targets the Finder application and was built using the 'Cocoa Application' Xcode template.  The techniques we are demonstrating in this sample can be used in any Cocoa Application. 




2. Add a Scripting Bridge build rule to the project.

The first thing to do is to set up Xcode to automatically generate the Scripting Bridge source for the application you would like to target.  The following steps describe how you can do that:

(a) In the project navigator, choose the project file and select the "ScriptingBridgeFinder" target.   

(b) With the "ScriptingBridgeFinder" target selected, switch to the "Build Rules" tab.

(c) In the build rules tab, click on the + button at the bottom to add a new rule.

(d) Set up the new rule as follows:

    Process 'Source files with names matching:'   *.app

    using: 'Custom Script'

    set the script field to:

    sdef "$INPUT_FILE_PATH" | sdp -fh -o "$DERIVED_FILES_DIR" --basename "$INPUT_FILE_BASE" --bundleid `defaults read "$INPUT_FILE_PATH/Contents/Info" CFBundleIdentifier`

    click on the "+" icon below the 'with output files:' field, and then set the field to contain:

    $(DERIVED_FILES_DIR)/$(INPUT_FILE_BASE).h

    NOTE: if you're typing this rule in by hand, note that it should all be one one line, and it must be typed exactly as shown above.  If you have difficulty entering the above command, then copy and paste the command from the readme into the rule.

(e) All done.  Xcode is now set up to automatically generate Scripting Bridge source for any applications you add to your project.

NOTE: this rule uses the sdef and sdp command line tools.  To learn more about these tools, use the following commands in the Terminal window:
   man sdp
   man sdef




3. Select a target application.

To do this, drag and drop the application you would like to target into the project files group inside of the "Groups & Files" list in the project window.   

You can drop the application among the source files you are using for your application.  Because of the build rule we added in step 2, Xcode will treat the Finder application as if it were one of the source files during the build.  

You should uncheck the 'Copy items into destination group's folder (if needed)' option so the application is not copied into your project directory.  In this sample we have selected 'Absolute Path' as the reference type so we can easily move the project around from machine to machine without invalidating the reference (so long as the Finder application is present in the System/Library/CoreServices folder,  Xcode will be able to find it).

In this case, we are adding the Finder to our project.  The Finder application is located in the /System/Library/CoreServices folder.




4. Add the target application to the Compile Sources.

After you have added the target application to your project, you must also add it to the main target's Compile Sources.  You can do that by adding the application to the 'Compile Sources' build phase under the main target.




5. Add the Scripting Bridge framework to your project.

In the Build Phases of the main target, expand the group titled "Link With Libraries".  Click the + button and select the ScriptingBridge.framework and click the Add button. 




6. Add a minimum system version Info.plist key.

Since the ScriptingBridge.framework is necessary for this application to run and that framework is not present on previous system versions, you should add the following key/value pair to the Info.plist file for the application.  If someone tries to run this application on a system earlier than Mac OS X 10.5, then they will receive a notice from launch services letting them know that the application is meant to be run on a later version of Mac OS X.

    <key>LSMinimumSystemVersion</key>
    <string>10.5</string>

You can edit the Info.plist file by either clicking on its icon in the resources section, or by clicking on the ScriptingBridgeFinder target, clicking on the Info icon, selecting the Properties tab, and then clicking on "Open Info.plist as File".




7. Build your project.

If you have followed the steps above, Xcode will generate the Scripting Bridge source for your project.  They will be put inside of your build folder in a place where the linker and compiler can find them.  

The build rule that we installed will create a .h file with the same name as the application.  For example, if you added Finder to our project, then the build rule will create Finder.h.  The files will be created inside of the build directory in the DerivedSources directory where the compiler can find them.

For the Debug build, the Finder.h file will be located in this sub folder of the build directory:
/build/Intermediates/ScriptingBridgeFinder.build/Debug/ScriptingBridgeFinder.build/DerivedSources/Finder.h

For the Release build, the Finder.h file will be located in this sub folder of the build directory:
/build/Intermediates/ScriptingBridgeFinder.build/Release/ScriptingBridgeFinder.build/DerivedSources/Finder.h

A convenient way for you to open and inspect these files is to use the 'Open Quickly' command in the file menu.  For most purposes, the .h file will contain most of the interesting information so to view that file you open the 'Finder.h' file.  

In some cases, depending on what frameworks are in your project, the 'Open Quickly' command may open the system's 'Finder.h' file that includes constants and definitions used by the file system and the Finder application.  If that happens for you, then you will need to navigate into the build folder to find the correct header file.




8. Add in the Finder's Scripting Bridge header.

In the file Controller.h, add '#import "Finder.h"' near the top of the file below '#import <Cocoa/Cocoa.h>'.  This will include all of the Scripting Bridge definitions for the Finder.

When you're done, the imports section should look like this:

    #import <Cocoa/Cocoa.h>
    #import "Finder.h"

In your own application, of course, you would import the Finder.h file in the file where you intend to use the definitions it contains.  In this sample, we are using the Scripting Bridge interface inside of three methods and for a property in our Controller class so that is why we are importing it into Controller.h.




9. Roadmap - check out what the Scripting Bridge Finder sample is doing.

So, we've set up our sample and installed the basic parts.  Let's take a moment to look at the bigger picture so we can see where we're going and how Scripting Bridge fits into this sample.

In this sample we're displaying a list of applications in a window and if the user double clicks on one of them (or selects one and clicks on the Launch button), then we ask the Finder to launch it.  So, what are the different parts of that picture, how are we accomplishing that, and how does Scripting Bridge fit into that picture?  The following points should help explain those questions.

(a) We're storing all of the information about the applications we find in the Application's folder in a table of records (implemented as an NSArray containing instances of NSDictionary).  For every application we find, we store the 'display name' of the application and a reference to the Scripting Bridge object for the application in a NSDictionary in the main NSArray.

(b) In the awakeFromNib method, we designate our Controller object as the data source and delegate for the list in the window.  That means that when the list is being drawn on the screen, it will ask our controller object for the data to display in the list.  In our Controller object we have implemented the methods numberOfRowsInTableView: and tableView:objectValueForTableColumn:row: for this purpose.  Inside of those methods, we simply return values stored in our table of records.

(c) There are some other methods associated with the list view for the purpose of receiving double clicks.  For more information about those, see the comments in the Controller.m file.

(d) Repopulating the data stored inside of the table of records is where Scripting Bridge comes in.  You'll notice that at the end of the awakeFromNib method we have designated the updateApplicationsTable method to receive NSApplicationDidBecomeActiveNotification notifications.  This means that our updateApplicationsTable method will be called whenever ScriptingBridgeFinder is switched into the forground in front of other applications.

And that's a great time to update the list of applications.  If our application was in the background it may very well be the case that the user made some changes or added some new programs.  By refreshing our list every time we're switched in, we can be reasonbly sure that our list is up to date with what is actually there.

Inside of the updateApplicationsTable method we call Scripting Bridge to scan through the Application's folder (two levels deep) to scrounge for applications.  Any applications that we find, we add into the table of records that we are displaying in the list in the window.  And, then we tell the list to re-draw itself.

(e) The second place where we put Scripting Bridge to work is inside of the launchSelected: method.  We have set up this method so that it will be called whenever the Launch button is clicked in the window or when the user double clicks on an item in the list of applications in the window.

In the launchSelected: method we get the scripting bridge object for the application selected in the list view out of the table of records and then we use Scripting Bridge to ask the Finder to launch the application for us.


In the following steps discuss adding in the Scripting Bridge parts that fit into this roadmap into the sample, and we'll provide some additional explanation along the way.



10. Allocate an instance of the Finder Scripting Bridge object.

In this application the Finder SBApplication object is used in a number of routines so rather than allocating the object whenever it is needed it is allocated once at startup time and a reference to it is stored in a property of the Controller class.

        /* allocate our scripting bridge object */
    self.finder = [SBApplication applicationWithBundleIdentifier:@"com.apple.finder"];

Note that the SBApplication object is being created using the -applicationWithBundleIdentifier: method.  This method will dynamically load and build the Scripting Bridge classes for the Finder from the Finder application.



11. Start populating the list of applications.

The first thing we're going to want to do is start building the list of applications we can launch.  One of the simplest ways to do that, of course, is to ask the Finder to find the applications in the Applications folder for you.  So, that's what we're doing here.  Interesting points about in this section are:

(a) We're using the construct '[[[[finder startupDisk] folders] objectWithName:@"Applications"] exists]' to determine if a Applications folder exists.  The formulation '[[ <collection>  objectWithName: <name> ] exists]' is a pattern you'll use again and again in Scripting Bridge code when testing for the existence of named elements.

(b) There's really no searching to do.  If we want the applications, we can ask the Finder for a list of them all by calling the applicationFiles method on the Application's folder object.  

(c) We call the 'displayedName' access on the individual application objects to find out what name is being displayed in the Finder interface.  This value will be set correctly according to the user's view settings for the file. 

(d) We're calling the NSArray method sortUsingFunction:context: to sort the list of applications.   This is a good example of using standard Cocoa functionality together with Scripting Bridge to accomplish tasks that are difficult to do in AppleScript alone.

The following code in the -updateApplicationsTable method in the file Controller.m performs the operations described above.  Note we have left out the part that does a second level search for applications.  We'll talk about that in the next step. 



        /* if the applications folder exists... */
    if ( [[[[finder startupDisk] folders] objectWithName:@"Applications"] exists]) {

            /* first, retrieve all of the applications in the main applications folder.  */
        SBElementArray* topLevelApps = [[[[finder startupDisk] folders] objectWithName:@"Applications"] applicationFiles];
        for ( FinderApplicationFile* nthApplication in topLevelApps ) {

                    /* add each application to our list of applications */
            [applications addObject:
                [[NSDictionary alloc] initWithObjectsAndKeys:
                    nthApplication, @"sb-object", /* the scripting bridge object */
                    [nthApplication displayedName], @"name", /* name - used for display and sorting */
                    nil]];

        }


            /* step 12 code here -- second level search for applications */


            /* sort the list of applications by name */
        [applications sortUsingFunction:AppCompare context:nil];

            /* tell the table view that the data has changed */
        [applicationsTable reloadData];

    }






12.  The second level search for applications.

Searching the top level of the application's directory really doesn't buy us much.  After all, we could simply open the Application's folder in Finder and there they all are.  It would be more interesting find all those ones that are hidden away inside of folders in the Applications folder.  Displaying those in our list would be much more interesting because it would save us the trouble of poking around in sub folders looking for applications.

So, in this step we're going to add in an extra level of search to go through all of the folders inside of the Applications folder to find applications stored in there.  

Now, you might think, why not make it entirely recursive and go through everything in the Application's folder?  Well, the reason why we've chosen the two level route here is because it's not too common to have apps buried down more than two levels deep.  And, perhaps more importantly, it is very common for larger applications to include immense directory hierarchies among their resources for their help files, and other supporting data.  Searching through all of that would take a long time, and the odds of finding more apps there are pretty slim.  So, there's the reasoning behind our two level approach.  Now, on to implementing the rest of it...  

In this step we're inserting some code into the code we added in the last step.  We're adding it into the code we added previously because we would like the additional applications we find in this step sorted into the list we started building in the last step.

Here, we ask the Finder for a list of all of the folders inside of the Applications folder and then we iterate through them adding all of the applications inside of them to our list of applications.


Adding in our second level search, we replace the comment mentioned in the last section, '/* step 12 code here */', with the following code:


            /* second, search every folder inside of the applications folder for
            applications and add all of the applications we find into our list. */

            /* get all of the folders inside of the Application's folder on the startup disk */
        SBElementArray* appFolders =[[[[finder startupDisk] folders] objectWithName:@"Applications"] folders];
        for ( FinderFolder* nthFolder in appFolders ) {

                /* get all of the applications in the ith folder */
            SBElementArray* secondLevelApps = [nthFolder applicationFiles];
            for ( FinderApplicationFile* nthSecondLevelApp in secondLevelApps ) {

                    /* add each of those applications to our list of applications */
                [applications addObject:
                    [[NSDictionary alloc] initWithObjectsAndKeys:
                        nthSecondLevelApp, @"sb-object", /* the scripting bridge object */
                        [nthSecondLevelApp displayedName], @"name", /* name - used for display and sorting */
                        nil]];

            }
        }



13. The launching code

So far we have talked about the code to populate the list of applications displayed in the window.  Now that we have that information in place, we can go ahead and add in code for launching them.

At the point where this code is executed, we have already determined that there is a selection in the list and we know the index of the selection (stored in the integer variable theRow).  Here, we use that index to retrieve the scripting bridge object from our table of records and then we ask the Finder to launch the application.

It's worth mentioning here that though we're asking the Finder to launch the application through the Scripting Bridge, you may have noticed that the way we're doing it appears at though we're asking the application object to use the Finder to launch itself.  Namely, we're calling the openUsing:withProperties: method on the on the selected application rather than calling an open method on the FinderApplication instance.  Here, it's worth pointing out that this is all perfectly normal and the arrangement of methods here is purely a matter of how the Finder's scripting dictionary has been set up.  


Here is the relevant code from the launchSelected: method near the bottom of the file Controller.m with the following code:


            /* retrieve the selected application from our list
            of applications. */
        FinderApplicationFile* selectedApplication =
            (FinderApplicationFile*) [(NSDictionary*)
                [applications objectAtIndex: theRow] objectForKey:@"sb-object"];

            /* ask the finder to open the application.  */
        [selectedApplication openUsing:finder withProperties:nil];





14. Where to next?

Documentation for Scripting Bridge can be found in the Scripting Bridge Release Note.  To find the Scripting Bridge Release Note, select 'Documentation' from the Help Menu in Xcode, select "Release Notes" from the "Jump To:" menu in the top right of the document window, click on the "View the complete Release Notes List." link near the top left of the window and scroll down to the Scripting Bridge Release Note.

There are man pages available for the Scripting Bridge command line tools.  To access those pages, enter the following commands into the Terminal window:

   man sdp
   man sdef

There are two other Scripting Bridge samples available including ScriptingBridgeiCal and ScriptingBridgeiTunes showing how to use Scripting Bridge together with the Apps named in their titles.



===========================================================================
BUILD REQUIREMENTS

Xcode 3.2, Mac OS X 10.6 Snow Leopard or later.

===========================================================================
RUNTIME REQUIREMENTS

Mac OS X 10.6 Snow Leopard or later.

===========================================================================
CHANGES FROM PREVIOUS VERSIONS

Version 1.1
- Updated setup instructions in the ReadMe.
- Project updated for Xcode 4.
Version 1.0
- Initial Version

===========================================================================
Copyright (C) 2007-2011 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](ScriptingBridgeFinder.md)

