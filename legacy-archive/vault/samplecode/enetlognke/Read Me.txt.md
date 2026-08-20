---
title: enetlognke
apple_id: DTS10003579
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2014-05-12'
source_url: https://developer.apple.com/library/archive/samplecode/enetlognke/Listings/Read_Me_txt.html
archived_at: '2026-07-18T03:29:08.957500Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [enetlognke](enetlognke.md)


[Next](Document%20Revision%20History.md)[Previous](enetlognke.c.md)

# Read Me.txt

```shell
Read Me About enetlognke
========================
2.0

enetlognke is an NKE (network kernel extension) that demonstrates the interface filter KPI (kernel programming interface).  It has two different features:

o it will log packets being transferred via the interface

o it can, optionally, delay packets being transferred via the interface

enetlognke supports OS X 10.9 and later although the core techniques work all the way back to OS X 10.4.

Packing List
------------
The sample contains the following items:

o Read Me.txt -- This file.

o enetlognke.c -- C source code for the NKE.

o enetlognke.xcodeproj -- An Xcode project for the NKE.

o Info.plist -- An information property list for the NKE.

Building the Sample
-------------------
The sample was developed using Xcode 5.1 on OS X 10.9.2.  You should be able to just open the project and choose Product > Build.

OS X 10.9 and later require that KEXTs be code signed.  For more information about this, watch WWDC 2013 Session 707 "What's New in Kext Development".

<https://developer.apple.com/videos/>

The sample comes pre-configured to sign the KEXT using your Developer ID code signing identity.  Such an identity must be enabled for KEXT development.  To determine if that's the case, look in the certificate for a custom extension with OID 1.2.840.113635.100.6.1.18.  If it's present, you're all set.  Otherwise, to enable your Developer ID code signing identity for KEXT development, follow the instructions on the page below.

<https://developer.apple.com/contact/kext/>

Finally, if you have more than one Developer ID, make sure you select the right one via the Code Signing Identity (CODE_SIGN_IDENTITY) build setting.

Using the Sample
----------------
Before testing the sample you should decide on an interface to test with.  The default interface is "en0", which is typically the first built-in Ethernet-like interface (the built-in Wi-Fi on modern machines, the built-in Ethernet on older machines).  If you need to use a different interface, you should open "enetlognke.c", change gNameOfInterfaceToFilter to be the name of that interface, and rebuild.

Once you've selected the correct interface, you must install the NKE.  To start, change into the directory containing the newly-built extension and install it as follows.

$ sudo cp -R enetlognke.kext /Library/Extensions/
Password: ********
$ sudo kextutil /Library/Extensions/enetlognke.kext

To confirm that it is installed, take a look at the system log.  You should see a startup message from the sample.

$ grep "enetlognke start" /var/log/system.log
Apr  1 10:42:29 Guy-Smiley kernel[0]: enetlognke start 'en0'

Next you should test the packet logging feature.  To start, open a Terminal window to monitor the system log.

$ tail -f /var/log/system.log
[...]

Then, in another Terminal window, do something to start transferring packets over the interface.  For example:

$ ping www.apple.com
[...]

In your system log monitoring window you should start seeing a record of these packets.

[...] enetlognke out IPv4 a820662e49ca|000c29f281ec|0800|45000054   98
[...] enetlognke in  IPv4 000c29f281ec|a820662e49ca|0800|45000054   98

To finish up, use the following command to unload the KEXT.

$ sudo kextunload -b com.example.apple-samplecode.kext.enetlognke

Finally, you can test the packet re-injection feature by changing kSwallowPackets (in "enetlognke.c") to TRUE, rebuilding and reinstalling the NKE, and then repeating the above test.  This time the system log will show something like this.

[...] enetlognke out IPv4 a820662e49ca|000c29f281ec|0800|45000054   98
[...] enetlognke out IPv4 a820662e49ca|000c29f281ec|0800|45000054   98 +
[...] enetlognke in  IPv4 000c29f281ec|a820662e49ca|0800|45000054   98
[...] enetlognke in  IPv4 000c29f281ec|a820662e49ca|0800|45000054   98 +

Each packet is logged by the NKE twice, with the second copy (the one tagged with "+") being the version that's been re-injected after a short delay.

Code Notes
----------
The enetlognke demonstrates the implementation of an interface filter by showing how to set up the iff_filter structure and to register the filter using the iflt_attach call. This sample filter is designed to look at each packet which passes to and from the specified interface. In addition, the sample demonstrates how to swallow packets and re-inject them after a delay. The sample queues swallow packets into an input or output queue, each protected by its own mutex.

All NKE packet filters, including interface filters, socket filters and IP filters, must be prepared to process (see) a specific packet multiple times. When a packet is swallowed by an interface filter and later re-injected, all interface filters will again be called to reprocess the packet on the re-injection path. If there are multiple interface filters, and all of the filters swallow and re-inject packets, then all filters will see the re-injected packet for each re-injection.

When a packet is re-injected, the corresponding input or output routine will be called to process the re-injected packet. The sample demonstrates the use of the tag mechanism to mark a packet which has been previously processed. The tag mechanism provides a means to allocate a small amount of memory on a per packet basis. When calling mbuf_tag_id_find use a unique value, like the reverse DNS name for your company to ensure the uniqueness of the tag ID value.

To conserve memory, do not allocate multiple tags for the same packet to track different events. Instead, use the allocated memory to store all packet-specific information. For example if your filter process swallows an outbound packet and later re-injects the packet on the inbound path, use the allocated memory to track which paths the packet has already been processed on. The small amount of memory associated with the tag, is for the use by your code and will not be modified by the system until the mbuf_t reference is freed.

If your interface filter duplicates an mbuf, the tags associated with the original mbuf, will not be copied to the duplicated mbuf. For example your interface filter might be layered atop multiple interfaces and make a copy of a packet to pass through a different interface. The duplicate packet will not have the tags from the original packet. Your filter will have to allocate new tags for the duplicated packet to track this processing.

When an input packet is swallowed, the kernel extension uses the ifnet_input routine to re-inject the packet back into the packet stream. This simulates the injection of a packet from an interface driver. Your injection code must make sure to set the packet header field of the first mbuf of the packet, else a panic results when the kernel tries to dereference an invalid packet header field pointer.

If the interface filter receives a packet on one interface and re-injects the packet into a second interface, you must ensure that one of the following criteria is true:

o the destination address in the frame header is the broadcast address, a supported multicast address for the destination interface, or the unicast address associated with the destination interface

o the MBUF_PROMISC flag is set in the packet header flags

If neither condition is true, the packet will be dumped on re-injection.

If you create a new incoming packet from scratch and expect to pass the packet into the system using the  ifnet_input routine, use the mbuf_pkthdr_setrcvif function to set the interface that the packet was received on.  If you don't do this the system will panic when it references an invalid ifnet_t reference.

When using fine grain locking as demonstrated in this sample, do not hold the lock over a system call. Other code in your kernel extension could be called while processing the system call, resulting in another access to code which accesses the lock. If the lock were held at the time of making the system call, a deadlock could occur. The typical symptom that a deadlock has occurred is that network activity across the filter stops.

Feedback
--------
If you find any problems with this sample, or you'd like to suggest improvements, please file a bug against it.

<http://developer.apple.com/bugreporter/>

Version History
---------------
1.0 (2 Jun 2005) was the original release

1.1 (12 Jul 2005) was an update to include a project to produce a universal binary. No code changes were necessary for this sample to run correctly on a Developer Transition System. Also added a note to the read me about using the mbuf_pkthdr_setrcvif function to set the source interface for a new  incoming packet.

2.0 (21 Apr 2014) was a major update to adopt the latest tools and techniques.  There were no feature-level changes but most of the code was rewritten to be smaller, more reliable and easier to understand.

21 Apr 2014
```

[Next](Document%20Revision%20History.md)[Previous](enetlognke.c.md)

