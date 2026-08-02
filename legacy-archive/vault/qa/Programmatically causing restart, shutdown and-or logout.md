---
title: Programmatically causing restart, shutdown and/or logout
apple_id: DTS10001681
resource_type: QA
platform: macOS
topic: General
technology: Carbon
published: '2008-09-24'
source_url: https://developer.apple.com/library/archive/qa/qa1134/_index.html
archived_at: '2026-07-18T02:29:56.049056Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1134

# Programmatically causing restart, shutdown and/or logout

## Q:  How do I programmatically shutdown, restart, sleep or logout a machine running Mac OS X?

A: How do I programmatically shutdown, restart, sleep or logout a machine running Mac OS X?

An application can do all of the above by sending specific Apple events to the loginwindow process. The loginwindow process will interpret the Apple events and cause the requested event. You can target the loginwindow process for Apple events using the constant {0,kSystemProcess} as the ProcessSerialNumber of the target application. Note that the restart, shutdown or logout sequence initiated using this method can be cancelled by running applications.

For details on applications canceling the restart/shutdown/logout sequence see "Terminating Processes" in [System Startup Programming Topics](https://developer.apple.com/DOCUMENTATION/MacOSX/Conceptual/BPSystemStartup/BPSystemStartup.html).

The specific Apple events sent to initiate system restart, shutdown, logout or sleep are kAERestart, kAEShutDown, kAEReallyLogOut or kAESleep, respectively.

The code below demonstrates how to programmatically cause restart, shutdown, sleep or logout by sending Apple events to the loginwindow process. The function SendAppleEventToSystemProcess does the work of sending the Apple event.

__Listing 1__  Demonstration of how to programatically restart, shutdown, sleep and logout the system

```c
#include <stdio.h>  #include <CoreServices/CoreServices.h> #include <Carbon/Carbon.h>  static OSStatus SendAppleEventToSystemProcess(AEEventID EventToSend);  int main(void) {     const int bufferSize = 256;     OSStatus error = noErr;     char select [bufferSize];      printf("1: Restart computer\n");     printf("2: Shutdown computer\n");     printf("3: Logout computer\n");     printf("4: Sleep computer\n");     printf("q: quit program\n");      printf("please enter choice:\n");fflush(stdout);     fgets(select, bufferSize, stdin);      switch (select[0])     {          case '1':             //sending restart event to system             error = SendAppleEventToSystemProcess(kAERestart);             if (error == noErr)                 {printf("Computer is going to restart!\n");}             else                 {printf("Computer wouldn't restart\n");}          break;          case '2':             //sending shutdown event to system             error = SendAppleEventToSystemProcess(kAEShutDown);             if (error == noErr)                 {printf("Computer is going to shutdown!\n");}             else                 {printf("Computer wouldn't shutdown\n");}          break;          case '3':             //sending logout event to system             error = SendAppleEventToSystemProcess(kAEReallyLogOut);             if (error == noErr)                 {printf("Computer is going to logout!\n");}             else                 {printf("Computer wouldn't logout");}          break;          case '4':             //sending sleep event to system             error = SendAppleEventToSystemProcess(kAESleep);             if (error == noErr)                 {printf("Computer is going to sleep!\n");}             else                 {printf("Computer wouldn't sleep");}     };      return(0); }  OSStatus SendAppleEventToSystemProcess(AEEventID EventToSend) {     AEAddressDesc targetDesc;     static const ProcessSerialNumber kPSNOfSystemProcess = { 0, kSystemProcess };     AppleEvent eventReply = {typeNull, NULL};     AppleEvent appleEventToSend = {typeNull, NULL};      OSStatus error = noErr;      error = AECreateDesc(typeProcessSerialNumber, &kPSNOfSystemProcess,                                              sizeof(kPSNOfSystemProcess), &targetDesc);      if (error != noErr)     {         return(error);     }      error = AECreateAppleEvent(kCoreEventClass, EventToSend, &targetDesc,                     kAutoGenerateReturnID, kAnyTransactionID, &appleEventToSend);      AEDisposeDesc(&targetDesc);     if (error != noErr)     {         return(error);     }      error = AESend(&appleEventToSend, &eventReply, kAENoReply,                    kAENormalPriority, kAEDefaultTimeout, NULL, NULL);      AEDisposeDesc(&appleEventToSend);     if (error != noErr)     {         return(error);     }      AEDisposeDesc(&eventReply);      return(error);  }
```


On Mac OS X daemons are run within the global context and without a connection to the window server. For this reason they should not, and often cannot, use the method outlined above for generating power state changes.

See [Technical Note TN2083: Daemons and Agents](https://developer.apple.com/technotes/tn2005/tn2083.html) for detailed information about daemons and execution contexts.

In the case where there are no GUI login sessions a daemon can issue the standard shutdown command to power the system down, appending the "`-r`" flag if a restart is desired. A daemon can also sleep the system by calling [IOPMSleepSystem](https://developer.apple.com/documentation/Darwin/Reference/IOKit/IOPMLib/CompositePage.html#//apple_ref/c/func/IOPMSleepSystem).

However, if one or more GUI login sessions are active, a daemon can use a separate per-user launchd agent to implement the Apple event power state commands outlined above. Interprocess communication between daemons and agents is outlined in [Technical Note TN2083: Daemons and Agents](https://developer.apple.com/technotes/tn2005/tn2083.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-24 | Updated source listing. |
| 2008-01-23 | Added information for daemon authors. |
| 2003-02-10 | New document that describes how to programmatically cause restart, shutdown, sleep or logout. |

