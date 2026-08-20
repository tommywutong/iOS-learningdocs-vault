---
title: SimpleDial
apple_id: DTS10003237
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: SystemConfiguration
published: '2005-07-26'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleDial/Listings/Read_Me_About_SimpleDial_txt.html
archived_at: '2026-07-18T03:23:59.616357Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleDial](SimpleDial.md)


[Next](SimpleDial.c.md)[Previous](SimpleDial.md)

# Read Me About SimpleDial.txt

```
Read Me About SimpleDial
========================
1.1

SimpleDial is a demonstration of the System Configuration framework network connection API, which lets you manage dialup connections such as PPP.

SimpleDial requires the System Configuration framework network connection API, which was introduced with Mac OS X 10.3.

Packing List
------------
The sample contains the following items:

o Read Me About SimpleDial.txt -- This file.
o SimpleDial.c -- Source for the program.
o SimpleDial.xcodeproj -- An Xcode 2.1 project for the program.
o SimpleDial.xcode -- An Xcode 1.1 project for the program.

Using the Sample
----------------
To try out SimpleDial, create (or switch to) a dialup network configuration. Make sure that PPP is disconnected. Then run SimpleDial from the command line. SimpleDial will display status messages while it initiates a PPP connection, waits for a few seconds, and then terminates the PPP connection. The following is a typical example.

% ./SimpleDial 
Connecting...
16:47:39 kSCNetworkConnectionConnecting (1)
16:47:39     kSCNetworkConnectionPPPInitializing (1)
16:47:39     kSCNetworkConnectionPPPConnectingLink (2)
16:48:37     kSCNetworkConnectionPPPNegotiatingLink (4)
16:48:39     kSCNetworkConnectionPPPAuthenticating (5)
16:48:39     kSCNetworkConnectionPPPNegotiatingNetwork (7)
16:48:39 kSCNetworkConnectionConnected (2)
16:48:39     kSCNetworkConnectionPPPConnected (8)
Connection succeeded
Waiting for a few seconds...
Disconnecting...
16:48:44 kSCNetworkConnectionDisconnecting (3)
16:48:44     kSCNetworkConnectionPPPTerminating (9)
16:48:44     kSCNetworkConnectionPPPDisconnectingLink (10)
16:48:48     kSCNetworkConnectionPPPDisconnected (0)
16:48:48 kSCNetworkConnectionDisconnected (0)
16:48:48     kSCNetworkConnectionPPPDisconnected (0)
Disconnection succeeded

Building the Sample
-------------------
The sample was built using Xcode 2.1 on Mac OS X 10.4.  You should be able to just open the project and choose Build from the Build menu.  This will build the SimpleDial command line tool in the "Build" directory.

How it Works
------------
SimpleDial uses the System Configuration framework network connection API to:

o determine the user's preferred PPP dialup preferences (SCNetworkConnectionCopyUserPreferences), 

o create an instance of the SCNetworkConnectionRef type (SCNetworkConnectionCreateWithServiceID), 

o schedule its callback on the runloop (SCNetworkConnectionScheduleWithRunLoop), 

o get the current status of the connection (SCNetworkConnectionGetStatus),

o initiate a PPP connection (SCNetworkConnectionStart), and 

o terminate the PPP connection (SCNetworkConnectionStop).

Credits and Version History
---------------------------
If you find any problems with this sample, mail <dts@apple.com> and IÕll try to fix them up.

1.0 (Apr 2004) was the first shipping version.

1.1 (Jul 2005) was updated to include an Xcode 2.1 project to produce a universal binary; there were no code changes required for it to run correctly on the Developer Transition Systems.

Share and Enjoy.

Apple Developer Technical Support
Networking, Communications, Hardware

21 Jul 2005

$Log: Read\040Me\040About\040SimpleDial.txt,v $
Revision 1.3  2005/07/21 14:51:04  eskimo1
Updated for version 1.1.

Revision 1.2  2004/07/13 15:17:36  eskimo1
Update example to match results from latest code.

Revision 1.1  2004/04/28 16:26:26  eskimo1
First checked in.
```

[Next](SimpleDial.c.md)[Previous](SimpleDial.md)

