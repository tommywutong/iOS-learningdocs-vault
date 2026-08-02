---
title: Xserve RAID Using RAID Admin 1.2 and Disk Utility
apple_id: TP40001991
resource_type: Guide
platform: macOS
topic: System Administration
technology: null
published: '2008-06-09'
source_url: http://images.apple.com/server/docs/RAIDAdmin1.2_121406.pdf
archived_at: '2026-07-27T06:31:37.399007Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md)



# Xserve RAID Using RAID Admin 1.2 and Disk Utility

[打开 Apple 原始 PDF](attachments/original.pdf)

## 第 1 页

Xserve RAID
Using RAID Admin 1.2
and Disk Utility

Includes instructions for creating RAID
arrays and monitoring Xserve RAID systems

## 第 2 页

K

 Apple Computer, Inc.
© 2006 Apple Computer, Inc. All rights reserved.
Under the copyright laws, this manual may not be
copied, in whole or in part, without the written consent
of Apple. Your rights to the software are governed by
the accompanying software license agreement.
The Apple logo is a trademark of Apple Computer, Inc.,
registered in the U.S. and other countries. Use of the
“keyboard” Apple logo (Option-Shift-K) for commercial
purposes without the prior written consent of Apple
may constitute trademark infringement and unfair
competition in violation of federal and state laws.
Every effort has been made to ensure that the
information in this manual is accurate. Apple is not
responsible for printing or clerical errors.
Apple
1 Infinite Loop
Cupertino, CA  95014-2084
408-996-1010
www.apple.com
Apple, the Apple logo, Mac, Mac OS, Macintosh, and
Xserve are trademarks of Apple Computer, Inc.,
registered in the U.S. and other countries.
Bonjour is a trademark of Apple Computer, Inc.
Java is a trademark of Sun Microsystems, Inc.
Other company and product names mentioned herein
are trademarks of their respective companies. Mention
of third-party products is for informational purposes
only and constitutes neither an endorsement nor a
recommendation. Apple assumes no responsibility with
regard to the performance or use of these products.
Simultaneously published in the United States and
Canada.
019-0905/1 2-14-06

## 第 3 页

3

3

Contents

Preface 5 About Software for Xserve RAID Systems
Chapter 1 7 Configuring an Xserve RAID System
8

Installing the RAID Admin Application

8

Connecting to the System

10

Entering Basic Settings for an Xserve RAID System

10

System Identity and Access

14

Configuring Additional Systems

Chapter 2 15 Working With RAID Arrays
15

Creating a RAID Array

17

About Spare Drives

17

Modifying a RAID Array

18

Rebuilding a RAID Array

19

Deleting a RAID Array

20

Formatting and Mounting Arrays on a Host System

21

Adding Software RAID to Two or More Arrays

Chapter 3 25 Monitoring Status and Changing Settings
25

Monitoring System Status

25

Adding a System to the Monitoring List

25

Getting System Information

29

Removing a System From the Monitoring List

29

Changing RAID Admin Preferences

29

Changing System Settings

29

Revising Basic Information and Network Settings

30

Setting Fibre Channel Speed and Topology

31

Setting Up Drive Cache and Controller Cache

33

Using System Commands

34

Turning the System Identifier On or Off

34

Updating System Firmware

Chapter 4 35 Using Advanced Features of RAID Admin
35

Slicing an Array

## 第 4 页

4

Contents

37

Merging Slices in an Array

38

Expanding an Array

39

Verifying or Rebuilding Parity for an Array

## 第 5 页

5

Preface

About Software for
Xserve RAID Systems

You can set up and manage an Xserve RAID system from
a host computer or a remote computer.

You use three applications to configure and monitor your Xserve RAID system. Two of
these applications, RAID Admin and Fibre Channel Utility, are included on a CD with the
system. (In some instances, the CD with RAID Admin and Fibre Channel Utility is
supplied with other systems or cards as well.) You also can download the latest version
of RAID Admin and Fibre Channel Utility using Software Update in System Preferences.
The third application, Disk Utility, is part of Mac OS X and Mac OS X Server.
You use RAID Admin to set up the Xserve RAID hardware, including:

•

Creating, deleting, and expanding RAID arrays (known as “hardware RAID”)

•

Monitoring the status of one or more Xserve RAID systems

•

Adjusting settings, including system name and password, network address for each
RAID controller, fibre channel communication speed, drive cache, and controller
cache

•

Setting up email notification for system alerts

•

Implementing advanced features, such as dividing arrays into “slices” and updating
the firmware of an Xserve RAID system.
You use the Fibre Channel Utility to view and modify settings on the Apple Fibre
Channel PCI Card, including:

•

Identifying the World Wide Node Name (WWNN) and World Wide Port Name (WWPN)
associated with each card port

•

Setting the fibre channel speed from the host card

•

Setting the fibre channel topology from the host card

•

Setting the hard loop ID
You use Disk Utility for:

•

Mounting arrays on the host system (which includes putting the file system on arrays
and creating volumes)

•

Implementing software RAID (striping or mirroring two or more RAID arrays)

## 第 6 页

6 Preface

    About Software for Xserve RAID Systems


This guide provides instructions for using RAID Admin and Fibre Channel Utility to
configure and monitor Xserve RAID systems and using Disk Utility to enhance
hardware RAID arrays. (For descriptions of RAID levels and the types of arrays you can
set up on an Xserve RAID system, see Chapter 7 , “RAID Overview,” and Chapter 8,
“Planning RAID Storage for the Xserve RAID System,” in the

Xserve RAID User’s Guide.)

See Chapter 1, “Configuring an Xserve RAID System,” on page 7 for details on
configuring a system for the first time.
See Chapter 2, “Working With RAID Arrays,” on page 1 5 for instructions on creating and
deleting RAID arrays.
See Chapter 3, “Monitoring Status and Changing Settings,” on page 25 for information
on managing systems, changing settings, and getting details of a system alert.
See Chapter 4, “Using Advanced Features of RAID Admin,” on page 35 for information
on slicing arrays, expanding arrays, and verifying or rebuilding parity.

## 第 7 页

1





7

1

Configuring an
Xserve RAID System

Use the RAID Admin application to configure or monitor
one or more Xserve RAID systems.

You use RAID Admin to enter basic information, such as system name, access level and
password, and network settings, on the Xserve RAID system. Monitoring buttons
require the monitoring password; management buttons require the management
password. (The default passwords are “public” for monitoring and “private” for
management.)
Before creating RAID arrays, it’s a good idea to configure the system with the name,
password, and network settings you want. You may need to get some information from
the network administrator for your location.
Toolbar management buttons
Monitoring buttons
(for selected system)
System information
Icons for monitoring
buttons; an icon
changes color (and
shape, if selected in
Preferences) to indicate
a change in status.
Toolbar monitoring buttons
(to connect to systems)
List of systems
being monitored
Message area

## 第 8 页

8 Chapter 1

    Configuring an Xserve RAID System


Be sure to write down the information you enter for the system and keep that record in
a safe place. If you plan to share your Xserve RAID system, other users will need to
know some or all of these details.

Installing the RAID Admin Application

You must install RAID Admin on all computers that you want to use to monitor or
administer Xserve RAID systems. Each monitoring computer must be using Java 1 .3. 1 or
a more recent version. (Java 1 .3. 1 is supported in Mac OS X v10.2 and later versions.)

To install or update RAID Admin on a monitoring computer, do one of the
following:

•

Insert the

Xserve RAID Admin Tools

 disc in the optical drive of the monitoring
computer and copy the folder “RAID Admin” to that computer.

•

Use Software Update in System Preferences to update a version already installed on
the computer.
You can also copy the software folder from a remote system or server if the computer
you want to use for monitoring does not have an optical drive.

Note:

When you update the software, be sure to read the “Read Me” files associated
with each new version.

Connecting to the System

RAID Admin uses Bonjour discovery to simplify connecting to an Xserve RAID system
the first time. The application lists the IP addresses of the systems on the same subnet
as your monitoring computer.
The system’s default configuration is to use DHCP for a network address. If no DHCP
server is available, the system will automatically use a link local address of 169.254.x.x.

Important:

The first time you configure an Xserve RAID system, you must use RAID
Admin on a computer that is on the same subnet as the system. By doing so, you can
connect to the system without knowing the IP address of the system.

## 第 9 页

Chapter 1

 Configuring an Xserve RAID System

9



To connect to an Xserve RAID system:
1

Turn on the Xserve RAID system.

Note:

The drives on the Xserve RAID have been preconfigured at the factory into a
RAID Level 5 array with RAID Now background initialization in effect. When you turn on
the system, the drives will begin initializing the array. This process will take a number of
hours. You can use the default RAID Level 5 array (or arrays, depending on the number
of drives in the system) immediately (as the drives are initializing) or delete the
preconfigured arrays and configure the drives as you wish. Connecting during
initialization and deleting an array will not harm the system. If you have written any
data on an array, deleting that array will cause that data to be lost.

2

Start RAID Admin on a computer that is on the same subnet as the system and click
Add System.

3

In the Add window, select the system you want from the list or type the IP address of
the system in the Address field.

4

Type the Monitoring Password.
Monitoring access allows you to monitor a system but not make changes. When you
want to create an array or make other changes, the software asks you to enter the
management password.

Note:

The default monitoring password is “public.” The default management password
is “private.”

5

Click Add.

6

Select the system in the list to display its settings and information in the monitoring
panes.
List of systems on subnet
(Bonjour names)

## 第 10 页

10 Chapter 1

    Configuring an Xserve RAID System



Entering Basic Settings for an Xserve RAID System

You can enter or change a number of settings for the Xserve RAID system. These
include:

•

System name

•

Location of the system and key contact

•

Management or monitoring password

•

System time synchronization with the monitoring computer or a network server

•

Audible alarm on or off; automatic restart after power outage on or off

•

Network address configuration

•

Fibre channel options for transmission speed and connection type

•

Turning drive cache on or off for each array and controller cache on or off (for each
RAID controller)
Changing some settings will cause the Xserve RAID system to restart.

System Identity and Access

You use the Settings window in RAID Admin to add or change most information for
your Xserve RAID system.

To open the Settings window:
1

In the RAID Admin window, click the Settings button.

2

If necessary, enter the management password and click OK.

## 第 11 页

Chapter 1

 Configuring an Xserve RAID System

11



Note:

You can save the management password for a system (until you quit RAID
Admin) by checking “Remember management password” when you enter the
password. A small lock icon appears at the right side of the message area for the
system in RAID Admin’s main window. Any subsequent tasks requiring the
management password will authenticate using the saved password without prompting
you. For security, you can delete the saved password by choosing Forget Management
Password from RAID Admin’s System menu.

System Name and Contact Information

Use the System pane in the Settings window to enter or change the system name. (The
default name Xserve RAID is set at the factory.) You can also enter reference
information, including the physical location of the Xserve RAID system and the primary
contact for that system.
Choose an option from the Time Synchronization Method pop-up menu. You can
synchronize the system’s time with the host computer or a network time server (for
which you enter the name).
You can change the password for management or monitoring access using the
appropriate Change button. When setting up the system, you may want to change
both passwords. Be sure to write them down and make them available to anyone else
who is authorized to make changes (management) or monitor system status
(monitoring).
The option for audible alerts is turned on by default.
The option for SNMP access is turned on by default. This option allows SNMP
community “public” access.

## 第 12 页

12 Chapter 1

    Configuring an Xserve RAID System



Network Address

You use the Network pane of the Settings window to set the IP address for each RAID
controller in the system.

•

If you have one or two static IP addresses, choose Manually from the Configure pop-
up menu and type the address, subnet mask, and router information.

•

If you don’t have a static IP address, choose Using DHCP from the Configure pop-up
menu. (DHCP is the default setting for the system.)
For specific information about the IP address and other network details for your system,
check with the network administrator at your location.

## 第 13 页

Chapter 1

 Configuring an Xserve RAID System

13



Email Notification

The Xserve RAID system sends email messages whenever it detects an error condition.
You can add as many email addresses as you wish for notification; separate the names
with commas.

To set up email notification:
1

In the RAID Admin window, click the Email button.

2

If necessary, enter the management password and click OK.

3

In the Email Notification window, click Add.

4

Enter one or more email addresses in the text field and click OK.

5

Enter the address of the SMTP server and the sender’s email address. You can use your
own address or create a new address on the SMTP server with a name such as “Xserve
RAID 3 alert” to identify the system and the purpose of the email message. (The
address you use must be a valid one on the SMTP server.)

6

If the SMTP server requires authentication, click the authentication checkbox and enter
the appropriate user name and password.
You can use the Send Test Email button to verify that notification is working.

7

Click OK.

## 第 14 页

14 Chapter 1

    Configuring an Xserve RAID System



Configuring Additional Systems

If you plan to configure multiple Xserve RAID systems, you must enter the information
and choose settings for each system individually.
If the other systems you want to set up are on the same subnet, you can add each one
to the monitoring list and then add name and contact information, change passwords,
and enter IP addresses for each system. Each time you begin a management task, you
have to enter the management password for that system, unless you have previously
saved it in RAID Admin Preferences.
If you need to configure a system for the first time that is not on the same subnet with
your monitoring computer, you must find out its IP address or use RAID Admin on
another computer on the subnet with that system. Once you know the IP address of
the systems you want to monitor, you can connect to them from any location with TCP/
IP access.
Once you’ve configured the system with basic settings, you can begin using the RAID
Level 5 arrays preconfigured at the factory, or you can create other RAID arrays and
begin storing data on the system.

## 第 15 页

2





15

2

Working With RAID Arrays

Use RAID Admin and Disk Utility to configure arrays and
volumes and use Fibre Channel Utility to refine fibre
channel performance.

Once you’ve configured the Xserve RAID system with basic settings, you can create
RAID arrays (also known as RAID sets). For explanations of RAID levels and
combinations offered by the Xserve RAID system, see Chapter 7 , “RAID Overview,” and
Chapter 8, “Planning RAID Storage for the Xserve RAID System,” in the

Xserve RAID User’s
Guide.

Creating a RAID Array

You use the Create Array window of RAID Admin to set up an array. This window lists
the hardware RAID levels you can create and displays a picture of the system’s front
panel so that you can easily choose the drives to include in each array. A checkbox is
on each available drive in the picture.

Note:

The Xserve RAID system uses two RAID controllers. The upper controller manages
drives 1 through 7 on the left side of the system (when viewed from the front); the
lower controller manages drives 8 through 14 on the right side. If your system has
fewer than 14 drives, you may want to rearrange the drive modules to take advantage
of both RAID controllers, which provide greater performance and redundancy.
You cannot create a RAID array that spans both controllers. (You can use Disk Utility to
add software RAID to two or more arrays, however; see “Adding Software RAID to Two
or More Arrays” on page 21 for details.)

Important:

Do not remove drive modules when the Xserve RAID system is powered.
When the system is powered on and you remove a drive module that is a member of a
RAID array, the array will either become degraded or will be lost if the RAID level is
unprotected.
Any drives not used in an array are treated as global spares (also called “hot spares”) for
all arrays on that controller.

## 第 16 页

16 Chapter 2

    Working With RAID Arrays



Important:

Once you create an array, you cannot change its type or remove drives
from it. Be sure to plan the arrays carefully to avoid having to remove an array later. You
can expand an array by adding one or more drives to it. See “Expanding an Array” on
page 38 for more information.
As you plan your arrays, keep in mind that each RAID controller can have up to three
arrays.

To create a RAID array:
1 In the RAID Admin window, click Create Array.
2 If necessary, enter the management password and click OK.
3 In the Create Array window, select the RAID level you want to use.
This window provides brief details about each RAID level or drive when you click the
button for a RAID level or put the pointer on the picture of a drive module.
4 Click the box on each drive you want to include in the array.
5 Choose the options you want.
• “Use RAID Now background initialization” lets you use the RAID array without waiting
for initialization to finish. While the array is being initialized, data read and write
speeds will be somewhat reduced. If this option is off, initialization takes place before
the array is visible on the host system.
Note:  The array cannot be seen by the host computer before initialization is
complete unless RAID Now is used.

## 第 17 页

Chapter 2    Working With RAID Arrays 17

• “Use drive cache” enables the built-in write cache on each drive in the array. This
option improves efficiency and speed of data transfer, but the drive cache contents
will be lost if power to the system fails, unless you are using an uninterruptible
power supply (UPS).
Important:  It is recommended that you use a UPS when you have drive cache
enabled. Without UPS backup, you could lose data in the event of a power failure.
In the event of a power failure, the system detects UPS power, immediately flushes
the data in the drive cache on a drive, and then turns off the cache. When AC power
is restored, the system turns on the drive cache again.
6 Check the summary of the array you’ve chosen and click Create Array.
Note:  The RAID controller automatically treats any drive not assigned to an array as a
global hot spare for all arrays on that controller.
About Spare Drives
A spare drive is any drive that has not been assigned to an array. On the Xserve RAID
system, an unassigned drive is “hot” (always spinning and ready for use) and global
(available to any array on its controller). A spare drive is used automatically by the RAID
controller for its group of drives (either drives 1 to 7 or drives 8 to 14) whenever a drive
within an array fails. (A controller can only use available drives on its side of the system;
it cannot treat a drive on the other side as a hot spare.)
When you assign a previously unused drive to a new array, it no longer serves as a hot
spare.
Modifying a RAID Array
Once a RAID array is established, you can expand it by adding one or more drives to it.
Expanding an array preserves the data on the original array. Be sure that your file
system supports expansion. See “Expanding an Array” on page 38 for details on
expanding an array.
You can also subdivide, or “slice,” an array into as many as six parts. Slicing an array
erases any data on it. See “Slicing an Array” on page 35 for details on slicing.
Note:  You cannot change an array’s type or remove drives from it. You can turn the
drive cache on or off.
Should you want to make any change except adding available drives to an array or
slicing it, you must back up all data in the array, delete the array, and create a new array
with the parameters you want.

## 第 18 页

18 Chapter 2     Working With RAID Arrays

Rebuilding a RAID Array
If a drive fails and the array RAID level is 1, 3, 5, or 0+1, data availability will be
unaffected, but the data is no longer protected. The array is in a degraded state. The
RAID controller that controls the affected array will automatically attempt to
reconstruct the data in order to return the system to a protected state. For example, if a
hot spare drive is available when a drive fails in an array, the controller takes the
available drive and integrates it into the array. The controller then rebuilds the RAID
array using the new drive.
Array performance will be diminished until the drive is rebuilt. During this rebuilding
process, an indicator on the drive module being added to the array alternately flashes
amber and green. The system displays a warning signal (yellow) in the main RAID
Admin when an array is degraded. Rebuilding progress is shown in the Arrays & Drives
monitoring pane.
The Xserve RAID system automatically rebuilds a RAID array in certain instances.
• If you have created a protected array (RAID 1, 3, 5, or 0+1) and you have an
unassigned drive (a hot spare), each RAID controller automatically uses the spare
drive to rebuild the array if a drive in the array fails.
• If no hot spare drive is available on the RAID controller, the array operates in a
degraded state until you replace the failed drive.
• If you have a RAID 0 array, the system cannot rebuild the array in the event of a drive
failure or other interruption. All data on the array will be lost.

## 第 19 页

Chapter 2    Working With RAID Arrays 19

Deleting a RAID Array
You delete a RAID array in the Delete Array window.
To delete an array:
1 In the RAID Admin window, click Delete Array.
2 If necessary, enter the management password and click OK.
3 In the Delete Array window, click the button for the array you want to delete.
The drives for that array turn red in the picture of the system.
4 Click the confirmation checkbox to confirm that you want to remove the array.
5 Click Delete Array (or click Cancel if you don’t want to delete the array).
WARNING:  Be sure to back up all data before you delete an array. If you delete an
array without first backing up all the data stored on the array, you will lose that data
with no possibility of recovery.

## 第 20 页

20 Chapter 2     Working With RAID Arrays

Formatting and Mounting Arrays on a Host System
Creating an array creates a virtual device without a file system. You add a file system to
each RAID array on the host system using Disk Utility. The array appears in Disk Utility
as an unformatted disk.
Disk Utility is part of Mac OS X (or Mac OS X Server) and is stored in the Utilities folder
inside the Applications folder.
Important:  You must use Disk Utility on the host system to format arrays and mount
them. This procedure can be done remotely with the diskutil command-line tool.  Refer
to the diskutil man page for more information.
To format and mount an array on the host system:
1 Restart the host system.
In some instances, restarting the host system may not be necessary, but if you are
creating or adding arrays, you generally must restart before the arrays are visible in Disk
Utility.
2 Open Disk Utility on the host system.
3 Select the array in the list at the left side of the window.
4 Click the Erase button.

## 第 21 页

Chapter 2    Working With RAID Arrays 21

5 Choose a format for the array from the Volume Format pop-up menu.
Note:  You can take advantage of disk journaling by using the journaled volume format
in Mac OS X Server. Journaling is a technique that helps protect the integrity of HFS+
disks in RAID arrays. It limits the exposure for data loss and expedites repair if the
volume gets into an inconsistent state. Performance diminishes slightly when
journaling is on.
When you enable journaling on a volume, a continuous record of changes to files on
the volume is maintained in the journal. If your system stops running because of a
power failure or some other problem, when you restart the system the journal is used
to restore the volume to a known good state. Although you may experience loss of
user data that was buffered at the time of the failure, the file system is returned to a
consistent state. In addition, restarting the system is much faster.
You can also turn journaling on or off for a volume at any time in the Information
section of Disk Utility.
6 Type a name for the volume.
7 Click Erase and confirm your decision by clicking Erase again.
Once formatting is complete, the volume mounts on the host system.
Repeat this procedure for each new volume.
Note:  If you want to add software RAID to two or more arrays, you can skip this
formatting procedure and instead use the RAID section of Disk Utility to stripe or mirror
the arrays together in a volume. This procedure also formats and mounts the resulting
volume. See “Adding Software RAID to Two or More Arrays” on page 21 for details.
Adding Software RAID to Two or More Arrays
Once you’ve set up arrays with RAID Admin, you can either stripe or mirror two
or more arrays using the Disk Utility application. Disk Utility is part of Mac OS X
(or Mac OS X Server) and is stored in the Utilities folder inside the Applications folder.
Use software stripe on RAID arrays to combine array capacities and improve
performance by taking advantage of multiple RAID controllers.
Use software mirror on RAID arrays to increase data protection through redundancy.
Note:  You must use Disk Utility on the host computer to add software RAID to two
or more arrays.

## 第 22 页

22 Chapter 2     Working With RAID Arrays

To add software RAID to two or more arrays:
1 Open Disk Utility on the host system and click the RAID tab.
2 Drag the arrays you want to stripe or mirror from the left side of the window to the
Disk list at the center of the window.
Note:  You must use two or more arrays to create a software RAID set.
3 Select the arrays in the Disk list.
4 Choose Stripe or Mirror from the RAID Scheme pop-up menu.
5 Enter a name for the new software RAID volume.

## 第 23 页

Chapter 2    Working With RAID Arrays 23

6 Choose a format for the array.
Note:  You can take advantage of disk journaling by using the journaled volume format
in Mac OS X Server. Journaling is a technique that helps protect the integrity of HFS+
disks in RAID arrays. It limits the exposure for data loss and expedites repair if the
volume gets into an inconsistent state.
When you enable journaling on an array, a continuous record of changes to files on the
volume is maintained in the journal. If your system stops running because of a power
failure or some other problem, when you restart the system the journal is used to
restore the volume to a known good state. Although you may experience loss of user
data that was buffered at the time of the failure, the file system is returned to a
consistent state. In addition, restarting the system is much faster.
You can also turn journaling on or off for a volume at any time in the Information
section of Disk Utility.
7 Click Create.
Once you’ve created your RAID arrays, you can use RAID Admin to monitor the Xserve
RAID system.

## 第 25 页

3
     25
3 Monitoring Status
and Changing Settings
Use RAID Admin to check the status and to change the
settings of one or more Xserve RAID systems.
You monitor the status of your Xserve RAID system with the RAID Admin application.
You can also adjust most settings with this software.
Monitoring System Status
RAID Admin displays a variety of information about your system as it is operating.
Adding a System to the Monitoring List
You can monitor many systems at the same time. You simply need to add each one to
the monitoring list.
See “Connecting to the System” on page 8 for details on adding a system to the list.
Getting System Information
To get details about the system’s operation, open RAID Admin and add the system to
the monitoring list. Click a monitoring button to display information for that category.
Using Contextual Menus in RAID Admin
Many menu and toolbar operations are available from a contextual menu in the
monitoring list.
To use the contextual menu:
m Hold down the Control key while pressing the mouse button, then choose the option
you want from the menu.
The items in a contextual menu vary according to the status of the system being
monitored.

## 第 26 页

26 Chapter 3     Monitoring Status and Changing Settings

• Info reports system name, lock status, controller details, and whether there is a
problem or power failure.
• Arrays & Drives shows details of each array and the drives in use and available. Click
Show Arrays and then click an array in the picture to see details of the array. Click
Show Drives and then click a drive to see details of that drive.

## 第 27 页

Chapter 3    Monitoring Status and Changing Settings 27

• Components shows the operating information about the power supplies, RAID
controllers, cooling modules, and cache backup batteries. You click the component
to view its details.
• Fibre Channel shows information about each RAID controller and the type of fibre
channel connection in use. Topology and Speed show the actual operating setting
and the configured setting (configured is in parentheses).

## 第 28 页

28 Chapter 3     Monitoring Status and Changing Settings

• Network displays the IP address and related network details for each RAID controller.
• Events displays a list of events that have occurred for both RAID controllers, in
chronological order.  Each event has a color symbol indicating the severity, a time
stamp, and a description.

## 第 29 页

Chapter 3    Monitoring Status and Changing Settings 29

Removing a System From the Monitoring List
You can take a system off the monitoring list when you’ve finished adjusting or
monitoring it.
Note:  If you remove a system, you must supply its IP address and monitoring password
when you add it again.
m To remove a system from the monitoring list, select it in the list and click Remove
System.
Changing RAID Admin Preferences
You can change status buttons to shapes in the main RAID Admin window and change
the time display to a 24-hour clock using the application’s preferences.
To use shapes or buttons to indicate system status:
1 Choose RAID Admin Preferences.
2 Check or uncheck “Use shapes to indicate status” to use shapes in addition to color for
status indicators, then click OK.
Use the “shapes to indicate status” option if you have difficulty distinguishing between
the different colored status indicators. When shapes are turned on, you see a green
circle for OK, a yellow triangle for warning, and a red square for failure status.
To adjust time settings for the event log:
1 Choose RAID Admin Preferences.
2 Click either “1 2-hour clock” or “24-hour clock” and click OK.
Changing System Settings
You can adjust most settings for the Xserve RAID system while the system is operating.
In a few instances, the Xserve RAID system must restart for a change to take effect,
temporarily disrupting data availability.
Revising Basic Information and Network Settings
See “System Name and Contact Information” on page 1 1 for instructions on adjusting
basic system settings, including changing passwords for management and monitoring
access.
See “Network Address” on page 1 2 for instructions on adjusting the network
information.

## 第 30 页

30 Chapter 3     Monitoring Status and Changing Settings

Setting Fibre Channel Speed and Topology
The default settings for fibre channel speed and topology are auto-negotiation and
auto-topology. If you have a requirement for fixed settings, you can use RAID Admin to
adjust settings on Xserve RAID systems and Fibre Channel Utility to adjust settings on a
Macintosh or Xserve host.
To adjust the fibre channel settings for an Xserve RAID system:
1 Open RAID Admin and click Settings.
2 If necessary, enter the management password and click OK.
3 In the Settings window, click the Fibre Channel button.
4 Click the buttons for the settings you want to change.
• Change the Speed setting for auto-negotiate or a fixed speed.
• Change the Topology setting for auto-topology or a fixed topology. Consult your
network administrator if you aren’t sure whether to change this setting.
5 Click OK.
6 In the confirmation window, click OK.
Note:  The fibre channel changes take effect when the Xserve RAID system restarts.
Data availability will be interrupted during the RAID controller’s restart.

## 第 31 页

Chapter 3    Monitoring Status and Changing Settings 31

To adjust fibre channel settings for a host computer:
1 Open Fibre Channel Utility on the host computer for which you want to adjust settings.
2 Click the lock icon, enter the admin password for the system, and click OK.
3 Select the port for which you want to adjust speed or topology.
4 Choose a speed or topology setting from the appropriate pop-up menu.
5 Select Enable Hard Loop ID if you must assign a fixed address on your fibre channel
loop. Check with your network administrator if you need more information about this
setting.
6 Click Apply.
7 Click the lock icon to prevent further changes.
Note:  You must restart the host computer for the change in fibre channel settings to
take effect.
Setting Up Drive Cache and Controller Cache
RAID Admin lets you turn on two separate types of cache to enhance performance of
your Xserve RAID system.
• Drive cache enables the built-in write cache on each drive in the array. This option
improves efficiency and speed of data transfer, but the drive cache is not backed up
should the system lose power unless you are using an uninterruptible power supply
(UPS).
Important:  It is recommended that you use a UPS when you have drive cache
enabled. Without UPS backup, you could lose data in the drive cache in the event of
a power failure.
• Controller cache is a write cache used by the RAID controller. This cache is backed up
by the optional Xserve RAID Cache Backup Battery Modules.
Important:  It is recommended that you have the optional controller cache backup
battery modules installed if you use controller cache. Using controller cache with no
battery backup could result in data loss in the controller cache if there is a power
failure.
Note:  Using a UPS and cache backup battery modules lessens the potential for data
loss, but these safeguards are not a guarantee against data loss. See your system
administrator or other expert for advice on preventing data loss.

## 第 32 页

32 Chapter 3     Monitoring Status and Changing Settings

To set up drive cache and controller cache:
1 Open RAID Admin and click Settings.
2 If necessary, enter the management password and click OK.
3 Click the Performance button.
4 To set up drive cache, click checkbox for the array for which you want to enable or
disable the drive cache.
5 To set up controller cache, click the button you want for Write Cache and Read Prefetch
for each controller.
• Write Cache is used to complete data transactions from the host computer before
actually writing the data to the drives.
• Read Prefetch anticipates that data should be retrieved from the arrays in sequential
order and “reads ahead.” In general, a large Read Prefetch setting is recommended
for video playback, and a small Read Prefetch setting is recommended for database
applications. Tuning the Read Prefetch setting may be required for optimal
performance, depending on your actual data.
6 Click OK.
7 In the confirmation window that appears, click OK.
Note:  Drive cache and controller write cache are required for applications that have a
very high throughput, such as high-resolution video editing. UPS backup for drive
cache is highly recommended.

## 第 33 页

Chapter 3    Monitoring Status and Changing Settings 33

Using System Commands
System commands are useful for system installation, maintenance, and
troubleshooting. These commands are located in the System menu of RAID Admin.
The system commands include:
• Shutdown, which puts the system into standby power mode. When you shut down a
system, the data held in all caches is safely written to disk before the system powers
off.
Note:  Use the Shutdown command or the Power button on the Xserve RAID system
to safely write all data in the caches to disk and power off the system. If you power
off the system by removing power (unplugging a cord, for example), the data in the
caches is not written to disk and you can experience data loss. Also, if the optional
cache backup batteries are installed, removing power will cause the system to think
there is a power failure and begin discharging the batteries that protect the contents
of the controller cache.
• Power Up, which starts up the system when it is in standby mode.
• Restart the Upper or Lower RAID Controller. These commands should only be used
when troubleshooting the RAID controller. Restarting the RAID controller will disrupt
the availability of your data.
• Restart the Upper or Lower Management Coprocessor. These commands should only
be used when troubleshooting communications problems between RAID Admin and
the Xserve RAID system. Restarting a coprocessor will not affect data availability.
Important:  Restarting both the upper and lower coprocessors within 30 seconds of
each other may cause your Xserve RAID system to go into standby power mode. If
you ever need to restart both coprocessors, wait at least 30 seconds after restarting
the first to restart the second.
Note:  Use the Restart system commands with care, because any of them may disrupt
the orderly transmission and storage of data.
• Clear Error Status. This command clears the alarm indicator on an Xserve RAID
system after it has detected a problem and the problem has been corrected. When a
problem is detected, the Xserve RAID system blinks the system identifier light,
sounds the audible alarm (if enabled), and sends an email notification (if enabled).
Until the error status is cleared, by either choosing Clear Error Status or pressing the
system identifier button on the system, the Xserve RAID system will not send further
email notifications or sound the alarm for problems of the same type or with the
same component.
• Clear Event Log. This command clears the contents of the event log.
• Forget Management Password. This command deletes the saved management
password.
• Update Now. This command gets the current status for the system and its
components.

## 第 34 页

34 Chapter 3     Monitoring Status and Changing Settings

Turning the System Identifier On or Off
You can use RAID Admin to turn on the system identifier light should you want to
locate a particular Xserve RAID system or assist another administrator in finding that
system. You can also turn off the system identifier when it’s on.
To turn the system identifier on or off:
1 Choose System > Turn Service ID On or Turn Service ID Off.
2 If necessary, enter the management password and click OK.
Updating System Firmware
You can use RAID Admin to update the firmware of the Xserve RAID system. Firmware
updates may be available to add new features or to fix problems. Apple recommends
that you update to the latest firmware available.
Xserve RAID firmware updates are available as a single file with both coprocessor and
RAID controller firmware images.
Check the Xserve RAID website regularly for news about your system and any updates
to firmware or software. Use your browser to go to www.info.apple.com and search
Downloads for Xserve.
To update the firmware of your system:
1 Download the firmware update file from the Xserve website, if necessary.
2 Unmount all Xserve RAID volumes on the host computer.
3 Open RAID Admin on the host or a monitoring computer for your Xserve RAID system.
4 Choose System > Update Firmware.
5 If necessary, enter the management password and click OK.
The default management password is “private.”
6 Select the firmware file you want to use and click Open.
Firmware update files have the extension “xfb.”
7 Click Update to begin the update process.
A progress bar indicates when the update is complete. The system restarts at the end
of this process.

## 第 35 页

4
     35
4 Using Advanced Features of
RAID Admin
The advanced features of RAID Admin give you several
options as you work with RAID arrays.
With RAID Admin’s advanced features you can:
• Subdivide arrays into as many as six “slices”
• Merge multiple slices into one slice
• Expand array capacity by adding drives
• Verify or rebuild parity in a protected RAID array (RAID 3 and 5)
Slicing an Array
You can subdivide a RAID array into segments, or slices. These slices are effectively
hardware partitions of all drives on the array. Each slice is a separate LUN and appears
as a separate volume on a host computer.

## 第 36 页

36 Chapter 4     Using Advanced Features of RAID Admin

On an Xserve RAID system, you can create up to six slices on a controller. There is a
limitation of eight LUNs on each controller, so the total number of unique arrays and
slices cannot exceed eight.
The example in the illustration below shows six slices in a RAID 5 array that contains
four drives. (All slices are the same size.)
Because slices are partitions of the several drives in an array, they provide a way to
manage storage as separate LUNs without having to create an array for each LUN.
Important:  When you create slices in an array, all data on the drives in that array will be
erased.
To slice a RAID array:
1 In the RAID Admin window, click Advanced.
2 If necessary, enter the management password and click OK.
3 Select Slicing in the Advanced window and click Continue.
4 In the Slicing window, select the array you want to slice.
This window provides brief details about each RAID level or drive when you click the
button for a RAID level or put the pointer on the picture of a drive module.
RAID 5 array
Yields
LUN 5 LUN 6
LUN 3 LUN 4
LUN 1 LUN 2
Slices across
RAID array
(up to 6)

## 第 37 页

Chapter 4    Using Advanced Features of RAID Admin 37

5 Select the number of slices into which you want to divide the array.
All slices are the same size, ranging from one-half to one-sixth of the total capacity of
the array, depending on the number you choose.
Note:  If the chosen array has already been sliced, you will only be able to merge the
slices. See “Merging Slices in an Array” below to details.
6 Click the Confirmation checkbox to confirm that you want to slice the array.
Any data on the array will be lost when the array is sliced.
7 Click Slice Array.
Merging Slices in an Array
Merging allows you to collapse all the slices in an array into a single slice. Data on every
slice except the first one will be lost when you merge slices. Merging is the second of
two steps that you must do when you expand an array.
To merge slices in a RAID array:
1 In the RAID Admin window, click Advanced.
2 If necessary, enter the management password and click OK.
3 Select Slicing in the Advanced window and click Continue.
4 In the Slicing window, select the array on which you want to merge slices.
All slices on the array will be merged into one.
5 Click the Confirmation checkbox to confirm that you want to merge the slices.
6 Click Merge Slices.

## 第 38 页

38 Chapter 4     Using Advanced Features of RAID Admin

Expanding an Array
You can easily add one or more available drives to an array. The drives must be on the
same controller as the array.
Expanding an array is a two-stage procedure. These stages are:
• Using the Expansion window to add one or more drives to an array
• Using the Slicing window to merge the slices in that array
Important:  Only expand an array that has not been sliced previously. If you expand an
array that already has slices on it, all the data on the array will be erased when you
merge the slices in the array.
Any data on a drive will be erased when you add that drive to an array.
To expand a RAID array:
1 In the RAID Admin window, click Advanced.
2 If necessary, enter the management password and click OK.
3 Click Expansion in the Advanced window and click Continue.
4 In the Expansion window, select the array you want to expand.
This window provides brief details about each RAID level or drive when you click the
button for a RAID level or put the pointer on the picture of a drive module.
5 Select the number of drives you want to add to the array.
The controller automatically selects available drives to add to the array.
6 Click the Confirmation checkbox to confirm that you want to expand the array.
7 Click Expand Array.

## 第 39 页

Chapter 4    Using Advanced Features of RAID Admin 39

The RAID controller begins restriping data across all the drives. The added drives’
capacity is added to the array as an unmapped slice. To make the added drive or drives
available to the array, merge the slices on that array.
To complete the expansion procedure by merging:
m Return to the Advanced window, select Slicing, and merge the slices on the array that
you just expanded.
See “Merging Slices in an Array” on page 37 for details on merging slices.
Verifying or Rebuilding Parity for an Array
You can verify the integrity of an array that uses parity (RAID 3 or 5) on an Xserve RAID
system. If necessary, you can also rebuild the parity data for an array.
Note:  Verifying or rebuilding parity on an array does not affect the file system or the
data on the array. These procedures make sure the array’s data is protected and verify
the integrity of the RAID set.
When you verify or rebuild parity for an array, the operation takes several hours and the
results are reported in the list of events (in the Events pane of the RAID Admin
window).
To verify or rebuild parity for a RAID array:
1 In the RAID Admin window, click Advanced.
2 If necessary, enter the management password and click OK.
3 Select Verify or Rebuild Parity and click Continue.
4 In the Verify or Rebuild window, select the array for which you want to verify or rebuild
parity data.

## 第 40 页

40 Chapter 4     Using Advanced Features of RAID Admin

5 Select Verify or Rebuild.
The controller automatically selects available drives to add to the array.
6 Click the confirmation checkbox to confirm that you want to verify or rebuild.
7 Click Verify Array or Rebuild Array.
Note:  The verification or rebuilding procedure takes a number of hours. You can
continue to use the array during this procedure.
If verifying parity data detects a problem, the recommended procedure for repair is as
follows:
• Perform an integrity check of the file system in the Finder.
• Verify data on the volumes.
• Use the rebuild function to rebuild the array’s parity data.
Rebuilding parity on an array does not repair any problems with the data on the array.
Rather, the data that is present on the array is used to create new parity data.
