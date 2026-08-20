---
title: Component Definitions
apple_id: DTS10001957
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2000-09-22'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc14.html
archived_at: '2026-07-18T02:38:47.178166Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [QuickTime Component Creation](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxQuickTimeComponentCreation-date.html) >

# Not Recommended Documentclose button

__Important:__ The information in this document is __Not Recommended__ and should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime Component Creation](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeComponentCreation-date.html)

|  |
| --- |
| Technical Q&A QTMCC14Component Definitions |

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| |  | | --- | |  Q: Please explain the difference between Components, Component Instances, Component Storage, and Component `RefCons`.  A: A Component is a 32-bit value that identifies a particular component -- for example, Graphics Exporter Components, which know how to export image files in a variety of formats. This value is not a pointer. |      |  | | --- | | ``` // Finding Components void FindGraphicsExporterComponents(void) {     Component c = 0;    // The Component Identifier     ComponentDescription cd;      cd.componentType = GraphicsExporterComponentType;     cd.componentSubType = 0;     cd.componentManufacturer = 0;     cd.componentFlags = 0;     cd.componentFlagsMask = graphicsExporterIsBaseExporter;   while((c = FindNextComponent(c, &cd)) != 0) {   ... // do something with the found component  } } ``` |     |  | | --- | | A `ComponentInstance` is a 32-bit value which identifies a particular connection that has been opened to a component using `OpenComponent`, `OpenAComponent`, `OpenDefaultComponent` or `OpenADefaultComponent`. This value is not a pointer. |      |  | | --- | | ``` // Open and return an Instance of the Sequence Grabber Component SeqGrabComponent OpenSequenceGrabber(void) {     ComponentInstance seqGrabComponent = 0;     OSErr err = noErr;      err = OpenADefaultComponent(SeqGrabComponentType, 0, &seqGrabComponent);     if(err || !seqGrabComponent) return 0;      return seqGrabComponent; } ``` |     |  | | --- | | Components are analogous to classes in object-oriented languages. Component Instances are analogous to objects of those classes.  A Component's Instance Storage (or Globals) is a pointer or handle to a block of memory which has been allocated in the component's `Open` routine and set up using `SetComponentInstanceStorage`. This must be a pointer or handle.  When someone calls a component function, the first parameter must be a valid `ComponentInstance` or a valid Component. If the first parameter is a Component, the component is opened, the call is made, and then the component is closed again; this is called a one-shot call. By the time the implementation of that component function is called, the first parameter has been replaced by the component's instance storage.  Generally, a component's Open function allocates memory for the instance storage (usually using `NewPtrClear`) and calls `SetComponentInstanceStorage` to associate it with itself. The `Open` function is also passed to the component instance value (as a parameter called _self_); components usually store this value inside their instance storage if they might need it in another call. |      |  | | --- | | ``` typedef struct {     ComponentInstance delegate; // keep track who we are delegating it to.     ComponentInstance self;     // self instance needed if targeted } PrivateGlobals;  // Open Component call pascal ComponentResult MyOpen(ComponentInstance self) {     PrivateGlobals *myPrivateGlobals;      myPrivateGlobals = NULL;      // Set up an environment to service the connection.     ...      // Create private variables -- allocate memory for our PrivateGlobals.     myPrivateGlobals = (PrivateGlobals *)NewPtrClear(sizeof(PrivateGlobals));     if (myPrivateGlobals == NULL)         goto bail;      // Initialize private variables, etc.     myPrivateGlobals->self = self;     ...      // Associates the newly allocated instance globals with the     // connection specified by the ComponentInstance parameter. Make sure to     // dispose of any allocated memory for the connection in response to the     // close request.     SetComponentInstanceStorage(self, (Handle)myPrivateGlobals);      return noErr;  bail:     if (myPrivateGlobals)         DisposePtr((Ptr)myPrivateGlobals);      return memFullErr; } ``` |    Remember, any memory allocated during the `Open` function should be deallocated in `Close` when the connection to the component is closed.     |  | | --- | | ``` pascal ComponentResult MyClose(Handle storage, ComponentInstance self) {     if (storage)         // Dispose of private globals.         DisposePtr((Ptr)storage));      return noErr; } ``` |    A component's `Refcon` (or Shared Globals) is a value which the Component Manager associates with a component if it so requests by calling `SetComponentRefcon`. Although this `Refcon` can be any value the component requires, many components use this `Refcon` value to store a pointer to data structures shared by multiple instances of the component.  Some components set up their shared globals the first time they are opened and dispose them when they are unregistered, while other components use shared globals, and avoid having multiple copies of lookup tables in memory when there are multiple instances of the component open. Dispose of them when the last instance is closed.   |  | | --- | | ``` typedef struct {     long shared; } SharedGlobals;  pascal ComponentResult MyOpen(ComponentInstance self) {     SharedGlobals *mySharedGlobals;      mySharedGlobals = NULL;      // Set up an environment to service the connection.     ...       // Create shared variables if they don’t exist.     mySharedGlobals = (SharedGlobals *)GetComponentRefcon((Component)self);     if (mySharedGlobals == NULL) {         mySharedGlobals=(SharedGlobals *)NewPtrSysClear(sizeof(SharedGlobals));         if (mySharedGlobals == NULL)             goto bail;         SetComponentRefcon((Component)self, (long)mySharedGlobals);          // Initialize shared variables.         mySharedGlobals->shared = 0;     }      // Initialize private variables, set up connection, etc.     ...      return noErr;  bail:     if (mySharedGlobals)         DisposePtr((Ptr)mySharedGlobals);      return memFullErr; } ``` |    A final note regarding shared globals: if you allocate memory for shared globals on the Macintosh, you should allocate them in the System heap (using `NewPtrSysClear`), since they may be shared between multiple applications.   ---  [Sep 22 2000] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
