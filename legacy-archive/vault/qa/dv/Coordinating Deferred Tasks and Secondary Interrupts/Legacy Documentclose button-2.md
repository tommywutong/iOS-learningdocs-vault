---
title: InterfaceLib and Native Drivers
apple_id: DTS10001184
resource_type: QA
platform: macOS
topic: null
technology: null
published: '2000-09-22'
source_url: https://developer.apple.com/library/archive/qa/dv/dv43.html
archived_at: '2026-07-18T02:29:28.188294Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md) · [Coordinating Deferred Tasks and Secondary Interrupts](Legacy%20Documentclose%20button.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [Hardware & Drivers](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxHardwareDrivers-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [Reference Library > Hardware & Drivers](https://developer.apple.com/referencelibrary/HardwareDrivers/index.html)

|  |
| --- |
| Technical Q&A DV43InterfaceLib and Native Drivers |

|  |  |  |
| --- | --- | --- |
| ---   Q: Is it legal to call system functionality exported by InterfaceLib from a native driver (`'ndrv'`)? [Designing PCI Cards and Drivers for Power Macintosh Computers](https://developer.apple.com/documentation/hardware/DeviceManagers/pci_srvcs/pci_cards_drivers/index.html) indicates that this is illegal, but some drivers (for example, disk drivers) can't be written without using InterfaceLib routines.  A: It depends on your definition of "legal". Designing PCI Cards and Drivers for Power Macintosh Computers describes a model for native disk drivers (the DriverServicesLib model). The original intention was that drivers written to the model would be binary compatible with future generations of Mac OS (specifically, a long-deceased project known as Copland). However, in current systems this model has a number of flaws.   - There are significant areas where the model does not   match the actual implementation on traditional Mac OS   (System 7.5.2 through Mac OS   9.x). DTS has documented a number of these   problems over the years (examples include Technote 1104   [Interrupt-Safe   Routines](https://developer.apple.com/library/archive/technotes/tn/tn1104.html) and Q&A DV 32 [`PrepareMemoryForIO`   and Execution Levels](dv32.md)), but they continue to crop   up. - In many areas Designing PCI Cards and Drivers   for Power Macintosh Computers is confusing because   it is trying to document the model rather than the   underlying implementation. - Because of changes in the design of Copland, the   DriverServicesLib model does not even match the   implementation that shipped   on the pre-release versions of that system. - Certain device drivers, for example disk drivers,   can't be written within the bounds of the DriverServicesLib model.   However, it is advantageous to write such drivers as   native drivers because it simplifies the development   process (and may yield performance enhancements). - The DriverServicesLib model duplicates functionality   provided by InterfaceLib routines. For example, it is   possible to schedule a timer callback using either   `SetInterruptTimer` (from DriverServicesLib)   or `InsTime` (from InterfaceLib). The old   routines still work just fine, but the model strongly   discourages developers from using them.   So, you might ask, why doesn't Apple abandon the DriverServicesLib model and officially recommend that developers link their native drivers with InterfaceLib? The reason is compatibility. If your driver sticks vigorously to the DriverServicesLib model, it may be possible for future system software to run it in some sort of compatibility environment. This is good for both Apple and you.   |  | | --- | | __Note:__  An example of this is the video `'ndrv'` support in Mac OS X. Mac OS X can load and run native video drivers from the ROM of PCI video cards. This allows Mac OS X to provide basic video functionality on any card that supports traditional Mac OS boot-time video, without having a real Mac OS X video driver available. In order for this to work your video driver must:   - link with only the   standard libraries (DriverServicesLib,   NameRegistryLib, VideoServicesLib, and   PCILib) - not access low-memory   globals - recognize that it's   possible for the logical and physical addresses   of its PCI hardware to be different, and always   access the appropriate addresses through the   appropriate Name Registry   properties. |   On the other hand, if there's no way to implement your class of driver within the DriverServicesLib model, you have no choice: you must link with InterfaceLib.  The decisions are trickier if DriversServicesLib and InterfaceLib offer two different flavors of the same functionality (for example, `PrepareMemoryForIO` versus `LockMemory` and `GetPhysical`). To allow for future compatibility we recommend that you favor the DriverServicesLib routines over their InterfaceLib equivalents. However, there may be factors that prevent you from using the DriverServicesLib routines. For example, the DriverServicesLib timer interrupt facility, `SetInterruptTimer`, is limited to 32 outstanding timer requests across the entire system. The Time Manager, however, can handle a much larger number of timer requests, as long as you pre-allocate the memory for each (the `TMTask` structure). If you find that your driver is using so many timers that it encounters the `SetInterruptTimer` limit, you may consider switching to the Time Manager. An even better solution, of course, would be to architect your driver to use fewer timers.   |  | | --- | | __IMPORTANT:__  If you decide to switch from using a DriverServicesLib service to an InterfaceLib service, you must be aware that their may be subtle differences between the services. To continue the example above, the `SetInterruptTimer` routine calls you back at secondary interrupt level, whereas the Time Manager calls you back at hardware interrupt level. Technote 1104 [Interrupt-Safe Routines](https://developer.apple.com/library/archive/technotes/tn/tn1104.html#ExecutionLevels) discusses the differences between these execution environment. |   Another factor to consider is whether your driver is to be placed in non-flashable ROM on a PCI card. If so, you should try harder to conform to the DriverServicesLib model because there's no way to change your code after it has shipped. In any case you should attempt to keep a ROM-based driver as simple, and as compatible, as possible. One good technique is to burn a simple driver in the ROM on your card and then provide an enhanced driver for the System Folder that replaces the simple ROM driver during system startup. This allows for both plug'n'play installation and easy maintenance.  In summary, if your native driver can only achieve its goals by calling InterfaceLib, it is legal to link with and call InterfaceLib. It will work just fine, but may present some compatibility issues in the future.  The above is not carte blanche for you to use a native driver for all the old sleazy hacks that 68K drivers (`'DRVR'`s) were used for. For example, your native driver should not put up dialogs boxes! Drivers should be used to drive hardware (or at least virtual hardware), not as mini-applications or as a poor man's shared library mechanism. This rule is simply good software design: splitting your code into a hardware component and a user interface component will make it more maintainable (especially with respect to new system software developments, such as Mac OS X).  If you do link your native driver to DriverServicesLib and InterfaceLib, make sure that you link with DriverServicesLib first and InterfaceLib second. Some symbols, such as `UpTime`, are now available in both stub libraries. However, older versions of the system do not export those symbols from InterfaceLib. If your driver is installed on such a system it will not load because the symbols are missing from the runtime copy of InterfaceLib (despite the fact that the symbol is available in DriverServicesLib). Linking with DriverServicesLib first will ensure that your driver gets these duplicate symbols from DriverServicesLib, and thus loads on older systems. For example, if your driver calls `UpTime` and links with InterfaceLib before DriverServicesLib, it will not run on systems prior to Mac OS 8.5. InterfaceLib on Mac OS 8.1 and earlier did not export the `UpTime` symbol. |

#### [Sep 22 2000]

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

---
