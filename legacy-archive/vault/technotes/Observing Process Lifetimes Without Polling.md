---
title: Observing Process Lifetimes Without Polling
apple_id: DTS10003081
resource_type: Technical Note
platform: macOS
topic: Data Management
technology: null
published: '2008-09-10'
source_url: https://developer.apple.com/library/archive/technotes/tn2050/_index.html
archived_at: '2026-07-26T19:53:49.427693Z'
---
> 导航：[总目录](../README.md) · [technotes](../_indexes/technotes.md)



Technical Note TN2050

# Observing Process Lifetimes Without Polling

This technote describes how to track the lifetime of a process on the system. There are a variety of different ways to do this, and the best approach depends on your specific circumstances. This technote describes the common approaches and the situations in which they are appropriate.

You should read this technote if you are developing Mac OS X software that uses one or more cooperating processes. Specifically, the technote covers all levels of the Mac OS X software stack (from BSD to Cocoa).

[Introduction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjukq2ujfhu4mi)[The Service-Oriented Alternative](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjukq2ujfhu4mq)[Observing Processes That You Started](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjukq2ujfhu4my)[NSTask](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjvkqstivbviskpjyzq)[Application Died Events](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjvkqstivbviskpjy2a)[The UNIX Way](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjvkqstivbviskpjy2q)[UNIX Alternatives](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjvkqstivbviskpjy3a)[Observing Arbitrary Processes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjukq2ujfhu4oa)[NSWorkspace](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjvkqstivbviskpjy4a)[Carbon Event Manager](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjvkqstivbviskpjy4q)[kqueues](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjvkqstivbviskpjyyta)[On Process Serial Numbers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjukq2ujfhu4mjs)[Further Reading](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewugsbrfvjukq2ujfhu4mjt)[Document Revision History](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydgmbygewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq)

## Introduction

After programming Mac OS X for a while, you will inevitably come across situations where it's necessary to create a suite of cooperating processes. For example:

- If you're writing an application, you may want to factor some code out into a separate helper process. Perhaps you want to put some unreliable code in a separate process so that, if it crashes, it doesn't crash your main application. Or perhaps you want to access certain APIs that aren't thread safe without locking up your application's user interface.
- You may be writing a suite of cooperating applications. Perhaps you're writing a word processor and want to call on the services of a separate equation editor.
- If you're writing a daemon, you may need to interface with a variety of agent programs that have access to per-user state.

Once you have multiple processes you inevitably run into the issue of process lifetime: that is, one process needs to know whether another process is running. This technote explains various techniques that you can use to be notified when a process launches or terminates. It is split into two main sections. Observing Processes That You Started shows how to monitor a process that you launched, while Observing Arbitrary Processes shows how to monitor a process that you didn't launch. Finally, On Process Serial Numbers contains some important information about the process serial number based APIs discussed in this technote.

But first, let's start with a discussion of an alternative approach that offers a number of key advantages.

__Important:__ All of the techniques discussed here notify you when things change. It is possible to get the same information by polling the process list, but polling is generally a bad idea (it consumes CPU time, reduces battery life, increase the working set of your process, and increases your latency in responding to an event).

[Back to Top](#)

## The Service-Oriented Alternative

One of the most common reasons for monitoring the lifecycle of a process is that the process provides some service to you. For example, consider a movie transcoding application that sublaunches a worker process to do the actual transcoding. The main application needs to monitor the state of the worker process so that it can relaunch it if it quits unexpectedly.

You can avoid this requirement by rethinking your approach. Rather than explicitly managing the state of your helper process, reimagine it as a service that your application calls upon. You can then use [launchd](x-man-page://8/launchd) to manage that service; it will take care of all the nitty-gritty details of launching and terminating the process that provides that service.

A full discussion of this service-oriented approach is outside the scope of this technote. For more information you should read up on `launchd`. A good place to start is the [launchd page](http://launchd.macosforge.org/) on [Mac OS Forge](http://www.macosforge.org/). I specifically recommend that you watch the Google TechTalk that's referenced by that page.

[Back to Top](#)

## Observing Processes That You Started

There are many different techniques for monitoring the lifetime of a process that you started. Each technique has a number of pros and cons. Read the following sections to determine which is most appropriate for your circumstances.

### NSTask

[NSTask](https://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSTask_Class/Reference/Reference.html) makes it easy to launch a helper process and wait for it to terminate. You can wait synchronously (using `-[NSTask waitUntilExit]`) or install a notification callback for the `NSTaskDidTerminateNotification` notification. Listing 1 shows the synchronous approach and Listing 2 show the asynchronous one.

__Listing 1__  Using NSTask synchronously

```objc
- (IBAction)testNSTaskSync:(id)sender {     NSTask *    syncTask;      syncTask = [NSTask          launchedTaskWithLaunchPath:@"/bin/sleep"          arguments:[NSArray arrayWithObject:@"1"]     ];     [syncTask waitUntilExit]; }
```

__Listing 2__  Using NSTask asynchronously

```objc
- (IBAction)testNSTaskAsync:(id)sender {     task = [[NSTask alloc] init];      [task setLaunchPath:@"/bin/sleep"];     [task setArguments:[NSArray arrayWithObject:@"1"]];      [[NSNotificationCenter defaultCenter]          addObserver:self          selector:@selector(taskExited:)          name:NSTaskDidTerminateNotification          object:task     ];      [task launch];      // Execution continues in -taskExited:, below. }  - (void)taskExited:(NSNotification *)note {     // You've been notified!      [[NSNotificationCenter defaultCenter]          removeObserver:self          name:NSTaskDidTerminateNotification          object:task     ];     [task release];     task = nil; }
```

### Application Died Events

If you launch an application using a process serial number based API, you can learn about its termination by registering for the `kAEApplicationDied` Apple event.

__Important:__ This event is only delivered for applications that you launched.

Listing 3 shows how to register for and handle an application died event.

__Listing 3__  Using application died events

```objc
- (IBAction)testApplicationDied:(id)sender {     NSURL *     url;     static BOOL sHaveInstalledAppDiedHandler;      if ( ! sHaveInstalledAppDiedHandler ) {         (void) AEInstallEventHandler(             kCoreEventClass,              kAEApplicationDied,              (AEEventHandlerUPP) AppDiedHandler,              (SRefCon) self,              false         );         sHaveInstalledAppDiedHandler = YES;     }      url = [NSURL fileURLWithPath:@"/Applications/TextEdit.app"];     (void) LSOpenCFURLRef( (CFURLRef) url, NULL);      // Execution continues in AppDiedHandler, below. }  static OSErr AppDiedHandler(     const AppleEvent *  theAppleEvent,      AppleEvent *        reply,      SRefCon             handlerRefcon ) {     SInt32              errFromEvent;     ProcessSerialNumber psn;     DescType            junkType;     Size                junkSize;      (void) AEGetParamPtr(         theAppleEvent,          keyErrorNumber,          typeSInt32,          &junkType,          &errFromEvent,          sizeof(errFromEvent),          &junkSize     );     (void) AEGetParamPtr(         theAppleEvent,          keyProcessSerialNumber,          typeProcessSerialNumber,          &junkType,          &psn,          sizeof(psn),          &junkSize     );      // You've been notified!      NSLog(         @"died %lu.%lu %d",          (unsigned long) psn.highLongOfPSN,          (unsigned long) psn.lowLongOfPSN,          (int) errFromEvent     );      return noErr; }
```

__Important:__ Application died events are based on serial numbers, a fact which has a number of important consequences. See On Process Serial Numbers for details.

### The UNIX Way

Mac OS X's BSD subsystem has two fundamental APIs for starting new processes:

- [fork](x-man-page://2/fork) and [exec](x-man-page://2/execve) — This technique has its origins in the first UNIX systems. The `fork` routine creates a new process that is an exact clone of the current process, and the exec routine (which is actually a [family of routines](x-man-page://3/exec), all based on the [execve](x-man-page://2/execve) routine) causes the current process to start running a new executable.
- [posix_spawn](x-man-page://2/posix_spawn) — This API acts like a combination of `fork` and `exec`. It was introduced in Mac OS X 10.5.

In both cases the resulting process is a child of the current process. There are two traditional UNIX ways to learn about the death of a child process:

- synchronously, using one of the family of [wait routines](x-man-page://2/wait) (typically `waitpid`)
- asynchronously, by way of the `SIGCHLD` signal

Waiting synchronously is appropriate in many situations. For example, if the parent process can make no progress until the child is done, it's reasonable to wait synchronously. Listing 4 shows an example of how to fork, then exec, then wait.

__Listing 4__  Fork, exec, wait

```
extern char **environ;  - (IBAction)testWaitPID:(id)sender {     pid_t       pid;     char *      args[3] = { "/bin/sleep", "1", NULL };     pid_t       waitResult;     int         status;      // I used fork/exec rather than posix_spawn because I would like this      // code to be compatible with 10.4.x.      pid = fork();     switch (pid) {         case 0:             // child             (void) execve(args[0], args, environ);             _exit(EXIT_FAILURE);             break;         case -1:             // error             break;         default:             // parent             break;     }     if (pid >= 0) {         do {             waitResult = waitpid(pid, &status, 0);         } while ( (waitResult == -1) && (errno == EINTR) );     } }
```

On the other hand there are circumstances where waiting synchronously is a really bad idea. For example, if you're running on the main thread of an application and the child process might operate for an extended period of time, you don't want to lock up your application's user interface waiting for the child to quit. In cases like this, you can wait asynchronously by listening for the `SIGCHLD` signal.

__Important:__ If you use the `SIGCHLD` technique you must still reap the child by calling a [wait routine](x-man-page://2/wait). Failure to do so will result in a [zombie process](http://en.wikipedia.org/wiki/Zombie_process).

Listening for a signal can be tricky because of the wacky execution environment associated with signal handlers. Specifically, if you install a signal handler (using [signal](x-man-page://3/signal) or [sigaction](x-man-page://2/sigaction)), you must be very careful about what you do in that handler. Very few functions are safe to call from a signal handler. For example, it is not safe to allocate memory using `malloc`!

The functions that are safe from a signal handler (the __async-signal safe__ functions) are listed on the [sigaction man page](x-man-page://2/sigaction).

In most cases you must take extra steps to redirect incoming signals to a more sensible environment. There are two standard techniques for doing this:

- sockets — In this technique you create a UNIX domain socket pair and add one end to your runloop using CFSocket. When a signal arrives, the signal handler writes a dummy message to the socket. This wakes up the runloop and allows you to process the signal in a safe environment.

  To see this technique in action, look at the `InstallSignalToSocket` routine in [Sample Code 'CFLocalServer'](https://developer.apple.com/samplecode/CFLocalServer/index.html).
- kqueues — The kqueue mechanism allows you to listen for a signal without installing any signal handlers. So you can create a kqueue, instruct it to listen for `SIGCHLD` signals, and then wrap it up in a CFFileDescriptor and add it to your runloop. When a signal arrives, the callback routine associated with the CFFileDescriptor runs and you can process the signal in a safe environment.

  To see this technique in action, look at the `InstallHandleSIGTERMFromRunLoop` routine in [Sample Code 'PreLoginAgents'](https://developer.apple.com/samplecode/PreLoginAgents/index.html).

__Important:__ The kqueue technique requires Mac OS X 10.5 or later because it uses CFFileDescriptor.

### UNIX Alternatives

There are numerous pitfalls associated with handing the `SIGCHLD` signal. The previous section described the deepest one, but there are others. Using `SIGCHLD` is particularly tricky when you're writing library code, because the disposition of `SIGCHLD` is controlled by the main program itself and your library code can't require that it be set one way or another.

There are various techniques to avoid all of this messing around with `SIGCHLD`. One such technique is to create a UNIX domain socket pair, and organize for the child to have the only descriptor that references one end, and for the parent to have a descriptor for the other end. When the child terminates, the system closes the child's descriptor and that causes the other end of the socket to indicate an end of file (that is, it becomes readable but, when you read from it, the `read` routine returns 0). When the parent detects this end of file condition it can reap the child.

Listing 5 shows an example of this technique.

__Listing 5__  Using a socket to detect child termination

```objc
- (IBAction)testSocketPair:(id)sender {     int                 fds[2];     int                 remoteSocket;     int                 localSocket;     CFSocketContext     context = { 0, self, NULL, NULL, NULL };     CFRunLoopSourceRef  rls;     char *              args[3] = { "/bin/sleep", "1", NULL } ;      // Create a socket pair and wrap the local end up in a CFSocket.      (void) socketpair(AF_UNIX, SOCK_STREAM, 0, fds);      remoteSocket = fds[0];     localSocket  = fds[1];     socket = CFSocketCreateWithNative(         NULL,          localSocket,          kCFSocketDataCallBack,          SocketClosedSocketCallBack,          &context     );     CFSocketSetSocketFlags(         socket,          kCFSocketAutomaticallyReenableReadCallBack | kCFSocketCloseOnInvalidate     );      // Add the CFSocket to our runloop.      rls = CFSocketCreateRunLoopSource(NULL, socket, 0);     CFRunLoopAddSource(CFRunLoopGetCurrent(), rls, kCFRunLoopDefaultMode);     CFRelease(rls);      // fork and exec the child process.      childPID = fork();     switch (childPID) {         case 0:             // child             (void) execve(args[0], args, environ);             _exit(EXIT_FAILURE);             break;         case -1:             // error             break;         default:             // parent             break;     }      // Close our reference to the remote socket. The only reference remaining      // is the one in the child. When that dies, the socket will become readable.      (void) close(remoteSocket);      // Execution continues in SocketClosedSocketCallBack, below. }  static void SocketClosedSocketCallBack(     CFSocketRef             s,      CFSocketCallBackType    type,      CFDataRef               address,      const void *            data,      void *                  info ) {     int             waitResult;     int             status;      // Reap the child.      do {         waitResult = waitpid( ((AppDelegate *) info)->childPID, &status, 0);     } while ( (waitResult == -1) && (errno == EINTR) );      // You've been notified! }
```

[Back to Top](#)

## Observing Arbitrary Processes

There are fewer options available if you want monitor the status of a process that you did not launch. However, the facilities that are available should be enough to meet most needs. Again, the right choice of API depends on your circumstances. Read the following sections to understand which API is appropriate and when.

### NSWorkspace

[NSWorkspace](https://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSWorkspace_Class/Reference/Reference.html) provides a very easy way for you to learn about applications being launched and quit. To register for these notifications you must:

1. get NSWorkspace's custom notification center by calling `-[NSWorkspace notificationCenter]`
2. add observers for the `NSWorkspaceDidLaunchApplicationNotification` and `NSWorkspaceDidTerminateApplicationNotification` events

When you get a notification, the user info dictionary contains information about the affected process. The keys for that dictionary are listed in `NSWorkspace.h`, starting with "NSApplicationPath".

Listing 6 shows an example of how to use NSWorkspace to learn application launch and termination.

__Listing 6__  Using NSWorkspace to learn about application launch and termination

```objc
- (IBAction)testNSWorkspace:(id)sender {     NSNotificationCenter *  center;      NSLog(@"-[AppDelegate testNSWorkspace:]");      // Get the custom notification center.      center = [[NSWorkspace sharedWorkspace] notificationCenter];      // Install the notifications.      [center addObserver:self          selector:@selector(appLaunched:)          name:NSWorkspaceDidLaunchApplicationNotification          object:nil     ];     [center addObserver:self          selector:@selector(appTerminated:)          name:NSWorkspaceDidTerminateApplicationNotification          object:nil     ];      // Execution continues in -appLaunched: and -appTerminated:, below. }  - (void)appLaunched:(NSNotification *)note {     NSLog(@"launched %@\n", [[note userInfo] objectForKey:@"NSApplicationName"]);      // You've been notified! }  - (void)appTerminated:(NSNotification *)note {     NSLog(@"terminated %@\n", [[note userInfo] objectForKey:@"NSApplicationName"]);      // You've been notified! }
```

__Important:__ NSWorkspace is a process serial number based API, a fact which has a number of important consequences. See On Process Serial Numbers for details.

### Carbon Event Manager

[Carbon Event Manager](https://developer.apple.com/documentation/Carbon/Conceptual/Carbon_Event_Manager/index.html) sends a number of events related to process management. Specifically, the `kEventAppLaunched` event is sent when an application is launched and the `kEventAppTerminated` when an application terminates. You register for these events as you would any other Carbon event. Listing 7 shows an example of this.

When your event handler is called the `kEventParamProcessID` parameter will contain the `ProcesSerialNumber` of the affected process. You can call Process Manager to get more information about the process.

__Important:__ By the time your application has received the `kEventAppTerminated` event, the terminating application has probably quit. Thus you can't get information about that application using `GetProcessInformation`. If you need information about terminating applications, you will have to cache it in advance.

__Listing 7__  Using Carbon events to learn about application launch and termination

```objc
- (IBAction)testCarbonEvents:(id)sender {     static EventHandlerRef sCarbonEventsRef = NULL;     static const EventTypeSpec kEvents[] = {         { kEventClassApplication, kEventAppLaunched },         { kEventClassApplication, kEventAppTerminated }     };      if (sCarbonEventsRef == NULL) {         (void) InstallEventHandler(             GetApplicationEventTarget(),             (EventHandlerUPP) CarbonEventHandler,             GetEventTypeCount(kEvents),             kEvents,             self,             &sCarbonEventsRef         );     }      // Execution continues in CarbonEventHandler, below. }  static OSStatus CarbonEventHandler(     EventHandlerCallRef inHandlerCallRef,      EventRef            inEvent,      void *              inUserData ) {     ProcessSerialNumber psn;      (void) GetEventParameter(         inEvent,          kEventParamProcessID,          typeProcessSerialNumber,          NULL,          sizeof(psn),          NULL,          &psn     );     switch ( GetEventKind(inEvent) ) {         case kEventAppLaunched:             NSLog(                 @"launched %u.%u",                  (unsigned int) psn.highLongOfPSN,                  (unsigned int) psn.lowLongOfPSN             );             // You've been notified!             break;         case kEventAppTerminated:             NSLog(                 @"terminated %u.%u",                  (unsigned int) psn.highLongOfPSN,                  (unsigned int) psn.lowLongOfPSN             );             // You've been notified!             break;         default:             assert(false);     }     return noErr; }
```

__Important:__ These Carbon events are based on process serial numbers, a fact which has a number of important consequences. See On Process Serial Numbers for details.

### kqueues

Both NSWorkspace and Carbon events only work within a single GUI login context. If you're writing a program that does not run within a GUI login context (a daemon perhaps), or you need to monitor a process in a different context from the one in which you're running, you will need to consider alternatives.

One such alternative is the [kqueue](x-man-page://2/kqueue) `NOTE_EXIT` event. You can use this to detect when a process quits, regardless of what context it's running in. Unlike NSWorkspace and Carbon events, you must specify exactly which process to monitor; there is no way to be notified when any process terminates.

Listing 8 is a simplistic example of how you can use kqueues to watch for the termination of a specific process.

__Listing 8__  Using kqueues to monitor a specific process

```
static pid_t gTargetPID = -1;     // We assume that some other code sets up gTargetPID.  - (IBAction)testNoteExit:(id)sender {     FILE *                  f;     int                     kq;     struct kevent           changes;     CFFileDescriptorContext context = { 0, self, NULL, NULL, NULL };     CFRunLoopSourceRef      rls;      // Create the kqueue and set it up to watch for SIGCHLD. Use the      // new-in-10.5 EV_RECEIPT flag to ensure that we get what we expect.      kq = kqueue();      EV_SET(&changes, gTargetPID, EVFILT_PROC, EV_ADD | EV_RECEIPT, NOTE_EXIT, 0, NULL);     (void) kevent(kq, &changes, 1, &changes, 1, NULL);      // Wrap the kqueue in a CFFileDescriptor (new in Mac OS X 10.5!). Then      // create a run-loop source from the CFFileDescriptor and add that to the      // runloop.      noteExitKQueueRef = CFFileDescriptorCreate(NULL, kq, true, NoteExitKQueueCallback, &context);     rls = CFFileDescriptorCreateRunLoopSource(NULL, noteExitKQueueRef, 0);     CFRunLoopAddSource(CFRunLoopGetCurrent(), rls, kCFRunLoopDefaultMode);     CFRelease(rls);      CFFileDescriptorEnableCallBacks(noteExitKQueueRef, kCFFileDescriptorReadCallBack);      // Execution continues in NoteExitKQueueCallback, below. }  static void NoteExitKQueueCallback(     CFFileDescriptorRef f,      CFOptionFlags       callBackTypes,      void *              info ) {     struct kevent   event;      (void) kevent( CFFileDescriptorGetNativeDescriptor(f), NULL, 0, &event, 1, NULL);      NSLog(@"terminated %d", (int) (pid_t) event.ident);      // You've been notified! }
```

[Back to Top](#)

## On Process Serial Numbers

Mac OS X has a number of high-level APIs for process management that work in terms of process serial numbers (of type `ProcessSerialNumber`). These include Launch Services, Process Manager, and NSWorkspace. These APIs all share three important features:

- They work in the context of a single GUI login session. For example, if you use NSWorkspace to observe applications being launched and terminated, you will only be notified about applications running in the same GUI login session.
- They only see processes that connect to the window server. For example, if you use NSTask to run a BSD command line tool like [find](https://developer.apple.com/library/archive/technotes/tn2050/<x-man-page:/1/find>), an NSWorkspace-based observer will not be notified of the tool's launch or termination.
- They are, in general, not usable by processes that run outside of a GUI login context (for example, daemons).

See [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html) for more information about execution contexts and their effect on high-level APIs.

[Back to Top](#)

## Further Reading

- [Advanced Programming in the UNIX® Environment](http://www.apuebook.com/)
- [UNIX Network Programming](http://www.unpbook.com/)
- [Technical Note TN2083, 'Daemons and Agents'](https://developer.apple.com/technotes/tn2005/tn2083.html)
- [launchd page](http://launchd.macosforge.org/) on [Mac OS Forge](http://www.macosforge.org/)
- [NSTask Class Reference](https://developer.apple.com/documentation/Cocoa/Reference/Foundation/Classes/NSTask_Class/Reference/Reference.html)
- [NSWorkspace Class Reference](https://developer.apple.com/documentation/Cocoa/Reference/ApplicationKit/Classes/NSWorkspace_Class/Reference/Reference.html)
- [Carbon Event Manager Programming Guide](https://developer.apple.com/documentation/Carbon/Conceptual/Carbon_Event_Manager/index.html)
- [Sample Code 'CFLocalServer'](https://developer.apple.com/samplecode/CFLocalServer/index.html)
- [Sample Code 'PreLoginAgents'](https://developer.apple.com/samplecode/PreLoginAgents/index.html)
- [launchd man page](x-man-page://8/launchd)
- [fork man page](x-man-page://2/fork)
- [execve man page](x-man-page://2/execve)
- [exec family man page](x-man-page://3/exec)
- [posix_spawn man page](x-man-page://2/posix_spawn)
- [wait family man page](x-man-page://2/wait)
- [signal man page](x-man-page://3/signal)
- [sigaction man page](x-man-page://2/sigaction)
- [kqueue man page](x-man-page://2/kqueue)

[Back to Top](#)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2008-09-10 | A major rewrite to eliminate use of deprecated APIs and to update the technote to reference the latest techniques. |
|  | A major rewrite to eliminate use of deprecated APIs and to update the technote to reference the latest techniques. |
| 2008-09-08 | A major rewrite to eliminate use of deprecated APIs and to update the technote to reference the latest techniques. |
| 2002-07-01 | New document that shows a variety of methods to observe process lifetimes without polling. |

